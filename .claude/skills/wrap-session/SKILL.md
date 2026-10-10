---
name: wrap-session
description: End-of-session vault maintenance — sweep the conversation for unfiled knowledge, run link checks and CSV export, update interests/index, propose new core questions if warranted, log the session and commit. Use when the human says they're done, asks to wrap up/save/commit, or before a long pause.
---

# wrap-session

1. **Sweep for unfiled knowledge.** Re-scan this session's Q&A: every substantive answer, comparison or paper connection should already be in a note (see *Knowledge capture* in CLAUDE.md). File anything missing now. Check that each question asked is reflected in `interests.md`.
2. **Consolidate (anti-bloat).** For notes touched this session: merge duplicate facts (keep one home, link elsewhere); rewrite topic-note *Current answer* sections so they read as the current state, not a changelog; move resolved items out of *Open questions*.
3. **Core-question check.** If a theme in `interests.md` has ≥3 questions across ≥2 sessions, or a topic note has ≥5 sources / its own sub-topics, **propose** promoting it to a hub (`topics/q<N>-<slug>.md` + Scope + `index.md`). Ask; don't add silently.
4. **Checks.** `.venv/Scripts/python.exe scripts/check_links.py` and `scripts/export_comparison.py`. Fix broken links, non-reciprocal links and unreachable notes; leave "concepts with < 2 papers" if they're genuinely new but list them.
5. **Log.** Append to `log.md`:
   ```
   ## YYYY-MM-DD
   - Added: papers / concepts / topics (wikilinks)
   - Changed: notable updates
   - Questions explored: one line each → where filed
   - Open: questions, needs_manual PDFs, next steps
   ```
6. **Commit** with a short message summarizing the session (local commit only; never push unless asked).
7. Tell the human in ≤5 lines: what was filed, what needs their attention (manual PDFs, proposed core questions, 🤖 assessments worth reviewing).
