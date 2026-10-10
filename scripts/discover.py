"""Paper discovery and acquisition (OpenAlex, arXiv; Semantic Scholar if S2_API_KEY is set).

Subcommands:
  search "<title query>"     OpenAlex title search, ranked by citations (2022+ by default)
  lookup <id> [<id> ...]     metadata for DOIs / arXiv IDs / OpenAlex IDs
  refs <id>                  works cited by <id> (backward snowballing)
  cites <id>                 works citing <id> (forward snowballing)
  pdf <citekey> [...]        download OA full text -> pdf/<citekey>.pdf (or .xml from Europe PMC)

search/lookup/refs/cites print a table; add --add to append new rows to
data/screening.csv (deduplicated by DOI / arXiv / citekey) with --source and
optional --decision/--reason.

Examples:
  python scripts/discover.py search "(EEG OR electroencephalography) AND foundation" -n 20
  python scripts/discover.py lookup 10.1109/tnsre.2022.3230250 arxiv:2405.18765 --add --source seed
  python scripts/discover.py cites 10.1109/tnsre.2022.3230250 -n 30
  python scripts/discover.py pdf song2022eeg jiang2024large
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from datetime import date

from notes import ROOT

SCREENING = ROOT / "data" / "screening.csv"
COLUMNS = ["citekey", "title", "year", "doi", "arxiv", "pmid", "cited_by",
           "source", "decision", "reason", "pdf_status"]
OA_SELECT = ("id,doi,title,publication_year,authorships,ids,cited_by_count,"
             "best_oa_location,locations,primary_location,type")
STOP = {"a", "an", "the", "on", "of", "for", "toward", "towards", "using", "in", "with",
        "and", "to", "from", "via", "is", "are", "what", "how", "do", "does", "can", "by"}
UA = {"User-Agent": "eeg-literature-review/0.1 (personal research script)"}


# ---------------------------------------------------------------- HTTP

def fetch(url: str, *, headers: dict | None = None, raw: bool = False, tries: int = 5):
    req = urllib.request.Request(url, headers={**UA, **(headers or {})})
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
                return data if raw else json.loads(data)
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and attempt < tries - 1:
                time.sleep(2 ** attempt * 2)
                continue
            raise


def openalex(path: str, **params) -> dict:
    params.setdefault("select", OA_SELECT)
    return fetch(f"https://api.openalex.org/{path}?" + urllib.parse.urlencode(params))


def s2_citations(doi: str, arxiv: str) -> int | None:
    """Semantic Scholar citation count (better coverage of ML venues). Needs S2_API_KEY."""
    key = os.environ.get("S2_API_KEY")
    if not key or not (doi or arxiv):
        return None
    pid = f"ARXIV:{arxiv}" if arxiv else f"DOI:{doi}"
    try:
        d = fetch(f"https://api.semanticscholar.org/graph/v1/paper/{urllib.parse.quote(pid)}"
                  "?fields=citationCount", headers={"x-api-key": key})
        time.sleep(1)
        return d.get("citationCount")
    except urllib.error.HTTPError:
        return None


# ---------------------------------------------------------------- records

def ascii_slug(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", s.lower())


def make_citekey(author: str, year, title: str) -> str:
    last = ascii_slug(author.split()[-1]) if author else "anon"
    words = [ascii_slug(w) for w in re.split(r"[\s\-–:/]+", title or "")]
    word = next((w for w in words if w and w not in STOP), "untitled")
    return f"{last}{year or ''}{word}"


def arxiv_id(work: dict) -> str:
    doi = (work.get("doi") or "").lower()
    if "10.48550/arxiv." in doi:
        return doi.split("arxiv.")[1]
    for loc in work.get("locations") or []:
        url = loc.get("landing_page_url") or loc.get("pdf_url") or ""
        if m := re.search(r"arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5})", url):
            return m.group(1)
    return ""


def record(work: dict) -> dict:
    auth = work.get("authorships") or []
    first = auth[0]["author"]["display_name"] if auth else ""
    doi = (work.get("doi") or "").replace("https://doi.org/", "")
    pmid = ((work.get("ids") or {}).get("pmid") or "").rsplit("/", 1)[-1]
    oa = work.get("best_oa_location") or {}
    ax = arxiv_id(work)
    pdf_url = oa.get("pdf_url") or (f"https://arxiv.org/pdf/{ax}" if ax else "")
    return {
        "citekey": make_citekey(first, work.get("publication_year"), work.get("title") or ""),
        "title": (work.get("title") or "").strip(),
        "year": work.get("publication_year") or "",
        "doi": "" if doi.lower().startswith("10.48550/arxiv") else doi,
        "arxiv": ax,
        "pmid": pmid,
        "cited_by": work.get("cited_by_count") or 0,
        "openalex": work.get("id", "").rsplit("/", 1)[-1],
        "pdf_url": pdf_url,
        "venue": (((work.get("primary_location") or {}).get("source") or {}).get("display_name") or ""),
    }


def resolve(ident: str) -> dict | None:
    """DOI, arxiv:ID / bare arXiv ID, or OpenAlex W-id -> OpenAlex work."""
    ident = ident.strip().replace("https://doi.org/", "")
    if re.fullmatch(r"W\d+", ident):
        return openalex(f"works/{ident}", select=OA_SELECT)
    ax = re.sub(r"^arxiv:", "", ident, flags=re.I)
    if re.fullmatch(r"\d{4}\.\d{4,5}(v\d+)?", ax):
        ax = re.sub(r"v\d+$", "", ax)
        res = openalex("works", filter=f"doi:10.48550/arxiv.{ax}")["results"]
        if res:
            return res[0]
        # Not in OpenAlex under the arXiv DOI: fall back to the arXiv API.
        xml = fetch(f"https://export.arxiv.org/api/query?id_list={ax}", raw=True).decode()
        title = re.search(r"<entry>.*?<title>(.*?)</title>", xml, re.S)
        author = re.search(r"<author>\s*<name>(.*?)</name>", xml, re.S)
        year = re.search(r"<published>(\d{4})", xml)
        if not title:
            return None
        return {"id": "", "doi": f"https://doi.org/10.48550/arxiv.{ax}",
                "title": " ".join(title.group(1).split()),
                "publication_year": int(year.group(1)) if year else None,
                "authorships": [{"author": {"display_name": author.group(1)}}] if author else [],
                "locations": [{"landing_page_url": f"https://arxiv.org/abs/{ax}"}]}
    try:
        return openalex(f"works/https://doi.org/{ident}", select=OA_SELECT)
    except urllib.error.HTTPError:
        return None


# ---------------------------------------------------------------- screening.csv

def load_screening() -> list[dict]:
    if not SCREENING.exists():
        return []
    with open(SCREENING, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def save_screening(rows: list[dict]) -> None:
    with open(SCREENING, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in COLUMNS})


def add_rows(recs: list[dict], source: str, decision: str, reason: str) -> None:
    rows = load_screening()
    dois = {r["doi"].lower() for r in rows if r["doi"]}
    axs = {r["arxiv"] for r in rows if r["arxiv"]}
    keys = {r["citekey"] for r in rows}
    added = 0
    for rec in recs:
        if (rec["doi"] and rec["doi"].lower() in dois) or (rec["arxiv"] and rec["arxiv"] in axs):
            print(f"  skip (already screened): {rec['title'][:70]}")
            continue
        key, n = rec["citekey"], 0
        while key in keys:
            key = rec["citekey"] + "abcdefgh"[n]
            n += 1
        rows.append({**rec, "citekey": key, "source": source, "decision": decision,
                     "reason": reason, "pdf_status": "pending" if rec["pdf_url"] else "needs_manual"})
        keys.add(key)
        dois.add(rec["doi"].lower())
        axs.add(rec["arxiv"])
        added += 1
        print(f"  added {key}")
    save_screening(rows)
    print(f"{added} added to data/screening.csv")


# ---------------------------------------------------------------- output

def show(recs: list[dict]) -> None:
    this_year = date.today().year
    print(f"{'cites':>5} {'/yr':>5} {'year':4}  {'citekey':24} {'id':32} title")
    for r in recs:
        age = max(1, this_year - int(r["year"] or this_year) + 1)
        ident = r["doi"] or (f"arxiv:{r['arxiv']}" if r["arxiv"] else r["openalex"])
        s2 = f" [S2 {r['s2']}]" if r.get("s2") is not None else ""
        print(f"{r['cited_by']:5} {r['cited_by'] / age:5.0f} {r['year']:4}  {r['citekey'][:24]:24} "
              f"{ident[:32]:32} {r['title'][:80]}{s2}")


def enrich(recs: list[dict]) -> list[dict]:
    for r in recs:
        r["s2"] = s2_citations(r["doi"], r["arxiv"])
    return recs


# ---------------------------------------------------------------- commands

def cmd_search(a) -> list[dict]:
    flt = f"title.search:{a.query},publication_year:>{a.since - 1},type:article|review|preprint"
    res = openalex("works", filter=flt, sort="cited_by_count:desc", **{"per-page": a.n})
    print(f"OpenAlex: {res['meta']['count']} matches; top {a.n} by citations")
    return [record(w) for w in res["results"]]


def cmd_lookup(a) -> list[dict]:
    recs = []
    for ident in a.ids:
        w = resolve(ident)
        if w is None:
            print(f"  NOT FOUND: {ident}")
            continue
        recs.append(record(w))
        time.sleep(0.3)
    return recs


def cmd_refs(a) -> list[dict]:
    w = resolve(a.id)
    if not w or not w.get("id"):
        sys.exit(f"not found in OpenAlex: {a.id}")
    wid = w["id"].rsplit("/", 1)[-1]
    res = openalex("works", filter=f"cited_by:{wid}", sort="cited_by_count:desc", **{"per-page": a.n})
    print(f"{res['meta']['count']} references of {w['title'][:70]}")
    return [record(x) for x in res["results"]]


def cmd_cites(a) -> list[dict]:
    w = resolve(a.id)
    if not w or not w.get("id"):
        sys.exit(f"not found in OpenAlex: {a.id}")
    wid = w["id"].rsplit("/", 1)[-1]
    res = openalex("works", filter=f"cites:{wid}", sort="cited_by_count:desc", **{"per-page": a.n})
    print(f"{res['meta']['count']} works citing {w['title'][:70]}")
    return [record(x) for x in res["results"]]


def europepmc_xml(doi: str) -> bytes | None:
    """JATS full-text XML from Europe PMC for an OA article with a PMC copy."""
    if not doi:
        return None
    q = urllib.parse.quote(f'DOI:"{doi}"')
    hits = fetch(f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={q}"
                 "&format=json&resultType=lite")["resultList"]["result"]
    pmcid = next((h.get("pmcid") for h in hits if h.get("pmcid")), None)
    if not pmcid:
        return None
    try:
        data = fetch(f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML", raw=True)
    except urllib.error.HTTPError:
        return None
    return data if b"<article" in data[:2000] else None


def cmd_pdf(a) -> None:
    """Download OA full text: PDF (arXiv, OA locations) else Europe PMC JATS XML."""
    rows = load_screening()
    todo = [r for r in rows if r["citekey"] in a.citekeys] if a.citekeys else         [r for r in rows if r["decision"] == "include" and r["pdf_status"] in ("pending", "needs_manual", "")]
    for r in todo:
        pdf, xml = ROOT / "pdf" / f"{r['citekey']}.pdf", ROOT / "pdf" / f"{r['citekey']}.xml"
        if pdf.exists() or xml.exists():
            r["pdf_status"] = "downloaded"
            print(f"have {r['citekey']}")
            continue
        urls = []
        if r["arxiv"]:
            urls.append(f"https://arxiv.org/pdf/{r['arxiv']}")
        w = resolve(r["doi"] or f"arxiv:{r['arxiv']}") if (r["doi"] or r["arxiv"]) else None
        if w:
            for loc in [w.get("best_oa_location") or {}] + (w.get("locations") or []):
                if loc.get("pdf_url") and loc["pdf_url"] not in urls:
                    urls.append(loc["pdf_url"])
        ok = False
        for url in urls:
            try:
                data = fetch(url, raw=True, tries=2)
            except Exception as e:
                print(f"  {r['citekey']}: {url} -> {e}")
                continue
            if data[:5] == b"%PDF-":
                pdf.write_bytes(data)
                print(f"ok   {r['citekey']} <- {url} ({len(data) // 1024} KB)")
                ok = True
                break
            print(f"  {r['citekey']}: {url} -> not a PDF (probably a landing/bot page)")
        if not ok and (data := europepmc_xml(r["doi"])):
            # Publisher/PMC PDF pages block scripts; the Europe PMC XML API does not.
            xml.write_bytes(data)
            print(f"ok   {r['citekey']} <- Europe PMC JATS XML ({len(data) // 1024} KB)")
            ok = True
        r["pdf_status"] = "downloaded" if ok else "needs_manual"
        if not ok:
            print(f"MANUAL {r['citekey']}: no OA full text retrievable (doi {r['doi'] or '-'})")
    save_screening(rows)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    def listing(p):
        p.add_argument("-n", type=int, default=15, help="max results (default 15)")
        p.add_argument("--add", action="store_true", help="append new results to screening.csv")
        p.add_argument("--source", default="", help="screening 'source' value, e.g. 'seed', 'search: ...'")
        p.add_argument("--decision", default="", help="include | exclude | maybe (default: blank)")
        p.add_argument("--reason", default="")

    p = sub.add_parser("search", help="OpenAlex title search ranked by citations")
    p.add_argument("query", help='OpenAlex title.search syntax, e.g. "(EEG OR electroencephalography) AND sleep"')
    p.add_argument("--since", type=int, default=2022, help="earliest publication year (default 2022)")
    listing(p)
    p = sub.add_parser("lookup", help="metadata for DOIs / arXiv IDs / OpenAlex IDs")
    p.add_argument("ids", nargs="+")
    listing(p)
    p = sub.add_parser("refs", help="references of a work (backward snowball)")
    p.add_argument("id")
    listing(p)
    p = sub.add_parser("cites", help="works citing a work (forward snowball)")
    p.add_argument("id")
    listing(p)
    p = sub.add_parser("pdf", help="download OA PDFs (default: included rows with pdf_status pending)")
    p.add_argument("citekeys", nargs="*")
    a = ap.parse_args()

    if a.cmd == "pdf":
        cmd_pdf(a)
        return
    recs = enrich({"search": cmd_search, "lookup": cmd_lookup, "refs": cmd_refs,
                   "cites": cmd_cites}[a.cmd](a))
    show(recs)
    if a.add:
        add_rows(recs, a.source or a.cmd, a.decision, a.reason)


if __name__ == "__main__":
    main()
