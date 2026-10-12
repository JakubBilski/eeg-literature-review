"""Re-tally EEG-Arena (chen2026benchmarking) result tables from fulltext/chen2026benchmarking.md.

1. Fig. 3 (p. 10): best FM vs best supervised baseline per task x split (first metric column).
2. Tables 27-31 (App. E.2.3): runs collapsed to a constant prediction (Cohen's kappa exactly 0.00%)
   per adaptation strategy and label budget, plus mean balanced accuracy.

Line ranges are specific to the pymupdf conversion of arXiv 2609.32743v1.
"""
from __future__ import annotations

import collections
import re
import statistics as st

from notes import ROOT

COLS = ("U-Sleep EEGNeX SleepEEGNet ShallowConvNet CTNet ATCNet DeepSleepNet SleepTransformer SlimSeiz "
        "IFNet EEGConformer EEGInceptionERP BiDANN TMSA-Net TSception FBCNet MSCFormer DeepConvNet "
        "DBConformer EEGNet MSVTNet EEGWaveNet YASA ADFCNN HSLT BENDR BIOT-p16 BIOT-shhs BIOT-six EEGPT "
        "LaBraM NeuroGPT CBraMod CSBrain EEGMamba LEAD LUNA-b LUNA-l LUNA-h mdJPT NeuroRVQ REVE-b REVE-l "
        "CodeBrain STEF-s STEF-b STEF-l HEAR-b HEAR-l SleepFM-ss SleepFM-dx SleepFM-up SleepGPT TFM "
        "UniDMFM").split()
N_BASE = 25


def fig3(lines: list[str]) -> None:
    txt = " ".join(l for l in lines[964:1329] if len(l) > 40)
    parts = re.split(r"((?:[A-Za-z][\w-]*\s)?Task\s?\d+\s(?:WS|CS))", txt)
    rows = []
    for i in range(1, len(parts), 2):
        vals, ranks = [], {}
        for t in parts[i + 1].split():
            if re.fullmatch(r"\d+\.\d+|-", t):
                vals.append(t)
            elif re.fullmatch(r"[123]", t) and vals:
                ranks[len(vals) - 1] = int(t)
            else:
                break
        if len(vals) < len(COLS):
            continue
        nums = [(float(v), j) for j, v in enumerate(vals[:len(COLS)]) if v != "-"]
        margin = max(v for v, j in nums if j >= N_BASE) - max(v for v, j in nums if j < N_BASE)
        top1 = COLS[min(ranks, key=ranks.get)] if ranks else None
        rows.append((parts[i], margin, top1))
    print(f"Fig. 3: {len(rows)} rows; best FM > best baseline on {sum(m > 0 for _, m, _ in rows)}")
    for s in ("WS", "CS"):
        m = [x for n, x, _ in rows if n.endswith(s)]
        print(f"  {s}: n={len(m)} median margin {st.median(m):.2f}")
    print("  top-1:", collections.Counter(t for *_, t in rows).most_common(8))


def budgets(lines: list[str]) -> None:
    txt = " ".join(lines[5992:6627])
    pat = re.compile(r"(Baseline|Linear Probe|Full-FT|Scratch-ST)((?:\s+-?\d+\.\d+%){18})")
    coll = collections.defaultdict(lambda: [0] * 6)
    ba = collections.defaultdict(lambda: [[] for _ in range(6)])
    for m in pat.finditer(txt):
        v = [float(x[:-1]) for x in m.group(2).split()]
        for b in range(6):
            coll[m.group(1)][b] += v[3 * b + 1] == 0.0
            ba[m.group(1)][b].append(v[3 * b])
    print("Tables 27-31, budgets 2/5/10/25/50/100%:")
    for s in coll:
        n = len(ba[s][0])
        print(f"  {s} (n={n}) collapsed:", coll[s],
              "mean BA:", [round(sum(x) / len(x), 1) for x in ba[s]])


if __name__ == "__main__":
    lines = (ROOT / "fulltext" / "chen2026benchmarking.md").read_text(encoding="utf-8").split("\n")
    fig3(lines)
    budgets(lines)
