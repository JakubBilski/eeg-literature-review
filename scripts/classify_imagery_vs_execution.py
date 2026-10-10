"""Classify imagined vs executed fist movement with CSP + LDA (PhysioNet EEG Motor Movement/Imagery).

Uses the files fetched for plot_motor_erd.py (data/eeg/, runs 3/7/11 executed, 4/8/12 imagined).
Labels: executed = 1, imagined = 0 (left- and right-fist trials pooled). Epochs 0.5–3.5 s after the cue,
skipping the cue-evoked response.

Protocols (all per subject unless stated):
  shuffled   5-fold stratified CV over trials, ignoring which run they came from (leaky: train and test
             share recording blocks, and condition == run, so the model can learn "which recording")
  by-block   leave-one-run-pair-out: train on 2 of (3,4) (7,8) (11,12), test on the third (3 folds)
  rest-ctrl  by-block CV on the *rest* (T0) periods of the same runs; nobody is moving or imagining,
             so anything above chance = recording-block differences, not the task
  LOSO       cross-subject: train on 9 subjects, test on the held-out one (task epochs, by-block irrelevant)
Bands: 8–30 Hz (mu/beta, brain) and 30–75 Hz (mostly muscle / EMG at 160 Hz sampling).

Example: python scripts/classify_imagery_vs_execution.py --subjects 1-10
"""
from __future__ import annotations

import argparse
import warnings
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mne
import numpy as np
from mne.datasets import eegbci
from mne.decoding import CSP
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import LeaveOneGroupOut, StratifiedKFold, cross_val_score
from sklearn.pipeline import make_pipeline

warnings.filterwarnings("ignore")
mne.set_log_level("error")
ROOT = Path(__file__).resolve().parent.parent
PAIRS = [(3, 4), (7, 8), (11, 12)]          # (executed, imagined) recorded back to back
BANDS = {"8–30 Hz (mu/beta)": (8, 30), "30–75 Hz (muscle)": (30, 75)}
TMIN, TMAX = 0.5, 3.5


def pipeline() -> object:
    return make_pipeline(CSP(n_components=6, reg="ledoit_wolf", log=True),
                         LDA(solver="lsqr", shrinkage="auto"))


def epochs_for(subject: int, band: tuple[int, int], kind: str):
    """Return X (trials, ch, time), y (1 = executed), groups (run pair) for task or rest epochs."""
    X, y, g = [], [], []
    for gi, pair in enumerate(PAIRS):
        for run in pair:
            f = eegbci.load_data(subject, [run], path=str(ROOT / "data" / "eeg"), update_path=False)[0]
            raw = mne.io.read_raw_edf(f, preload=True)
            eegbci.standardize(raw)
            raw.filter(*band, fir_design="firwin")
            events, ids = mne.events_from_annotations(raw)
            want = {k: ids[k] for k in (["T1", "T2"] if kind == "task" else ["T0"])}
            ep = mne.Epochs(raw, events, want, TMIN, TMAX, baseline=None, preload=True)
            X.append(ep.get_data()); n = len(ep)
            y += [int(run == pair[0])] * n; g += [gi] * n
    return np.concatenate(X), np.array(y), np.array(g)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--subjects", default="1-10")
    ap.add_argument("--out", default=str(ROOT / "figures" / "eegmmi-imagined-vs-executed-csp.png"))
    a = ap.parse_args()
    lo, _, hi = a.subjects.partition("-")
    subjects = list(range(int(lo), int(hi or lo) + 1))

    res = {}                                    # (band, protocol) -> list of per-subject accuracies
    task_data = {}
    for bname, band in BANDS.items():
        for s in subjects:
            X, y, g = epochs_for(s, band, "task")
            task_data[(bname, s)] = (X, y)
            sh = cross_val_score(pipeline(), X, y, cv=StratifiedKFold(5, shuffle=True, random_state=0)).mean()
            bb = cross_val_score(pipeline(), X, y, groups=g, cv=LeaveOneGroupOut()).mean()
            Xr, yr, gr = epochs_for(s, band, "rest")
            rc = cross_val_score(pipeline(), Xr, yr, groups=gr, cv=LeaveOneGroupOut()).mean()
            for k, v in (("shuffled", sh), ("by-block", bb), ("rest-ctrl", rc)):
                res.setdefault((bname, k), []).append(v)
            print(f"S{s:03d} {bname:18s} n={len(y):3d} shuffled={sh:.2f} by-block={bb:.2f} rest-ctrl={rc:.2f}",
                  flush=True)
        # cross-subject: leave one subject out
        for s in subjects:
            Xtr = np.concatenate([task_data[(bname, t)][0] for t in subjects if t != s])
            ytr = np.concatenate([task_data[(bname, t)][1] for t in subjects if t != s])
            Xte, yte = task_data[(bname, s)]
            res.setdefault((bname, "LOSO"), []).append(pipeline().fit(Xtr, ytr).score(Xte, yte))

    print(f"\nAccuracy, imagined vs executed (chance 0.50), mean ± SEM over {len(subjects)} subjects:")
    protocols = ["shuffled", "by-block", "rest-ctrl", "LOSO"]
    print(f"{'band':20s}" + "".join(f"{p:>16s}" for p in protocols))
    for bname in BANDS:
        row = ""
        for p in protocols:
            v = np.array(res[(bname, p)])
            row += f"{v.mean():10.2f} ± {v.std(ddof=1) / np.sqrt(len(v)):.2f}"
        print(f"{bname:20s}{row}")

    # Figure: per-subject accuracies + CSP patterns of subject 1 (8–30 Hz)
    fig = plt.figure(figsize=(13, 5.5), constrained_layout=True)
    gs = fig.add_gridspec(2, 5, width_ratios=[2.2, 2.2, 1, 1, 1])
    for i, bname in enumerate(BANDS):
        ax = fig.add_subplot(gs[:, i])
        for j, p in enumerate(protocols):
            v = np.array(res[(bname, p)])
            ax.scatter(np.full(len(v), j) + np.random.default_rng(j).uniform(-0.12, 0.12, len(v)), v,
                       s=14, color="0.5", zorder=2)
            ax.errorbar(j, v.mean(), yerr=v.std(ddof=1) / np.sqrt(len(v)), fmt="o", color="C3",
                        capsize=4, zorder=3)
        ax.axhline(0.5, color="k", ls="--", lw=0.8)
        ax.set_xticks(range(len(protocols)), protocols)
        ax.set_ylim(0.2, 1.02); ax.set_ylabel("accuracy")
        ax.set_title(f"{bname}: imagined vs executed\n(grey = subjects, red = mean ± SEM; dashed = chance)",
                     fontsize=9)

    X, y = task_data[(list(BANDS)[0], subjects[0])]
    f = eegbci.load_data(subjects[0], [3], path=str(ROOT / "data" / "eeg"), update_path=False)[0]
    info_raw = mne.io.read_raw_edf(f); eegbci.standardize(info_raw)
    info_raw.set_montage("standard_1005")
    csp = CSP(n_components=6, reg="ledoit_wolf", log=True).fit(X, y)
    patterns = csp.patterns_[[0, 1, -1]]           # most "executed"-ish, next, most "imagined"-ish
    titles = ["CSP 1", "CSP 2", "CSP 64 (last)"]
    for k in range(3):
        ax = fig.add_subplot(gs[0 if k < 2 else 1, 2 + (k % 2) if k < 2 else 2])
        mne.viz.plot_topomap(patterns[k], info_raw.info, axes=ax, show=False, contours=0)
        ax.set_title(f"S{subjects[0]:03d} {titles[k]}", fontsize=9)
    fig.suptitle("CSP + LDA on PhysioNet EEGMMI: can one tell imagined from executed fist clenching? "
                 "(epochs 0.5–3.5 s after cue)", fontsize=11)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(a.out, dpi=130)
    print("saved", a.out)


if __name__ == "__main__":
    main()
