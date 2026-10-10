"""Plot imagined vs executed fist movement at the motor cortex (PhysioNet EEG Motor Movement/Imagery).

Downloads the EEGMMI runs from PhysioNet into data/eeg/ (gitignored) and draws:
  A) one raw single trial at C3 for imagined and for executed right-fist clenching,
  B) trial- and subject-averaged band-power change (ERD/ERS, % vs pre-cue rest)
     in mu (8-12 Hz) and beta (16-26 Hz) at C3 (contralateral) and C4 (ipsilateral).

Runs (Schalk et al. 2004): 3/7/11 = executed left/right fist, 4/8/12 = imagined.
Annotations: T0 rest, T1 left fist, T2 right fist.

Example: python scripts/plot_motor_erd.py --subjects 1-10 --example-subject 1
"""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mne
import numpy as np
from mne.datasets import eegbci

ROOT = Path(__file__).resolve().parent.parent
RUNS = {"imagined": [4, 8, 12], "executed": [3, 7, 11]}
BANDS = {"mu (8–12 Hz)": (8, 12), "beta (16–26 Hz)": (16, 26)}
TMIN, TMAX = -2.0, 5.0
REF = (-1.5, -0.25)      # pre-cue rest window used as the ERD reference
TASK = (0.5, 3.0)        # window summarised in the printed table


def load(subject: int, runs: list[int]) -> mne.io.BaseRaw:
    files = eegbci.load_data(subject, runs, path=str(ROOT / "data" / "eeg"), update_path=False,
                             verbose="error")
    raw = mne.concatenate_raws([mne.io.read_raw_edf(f, preload=True, verbose="error") for f in files])
    eegbci.standardize(raw)
    raw.set_eeg_reference("average", verbose="error")
    return raw


def right_fist_epochs(raw: mne.io.BaseRaw, l_freq: float, h_freq: float) -> mne.Epochs:
    filt = raw.copy().filter(l_freq, h_freq, verbose="error")
    events, ids = mne.events_from_annotations(filt, verbose="error")
    return mne.Epochs(filt, events, {"right": ids["T2"]}, TMIN, TMAX, baseline=None,
                      picks=["C3", "C4"], preload=True, verbose="error")


def erd(raw: mne.io.BaseRaw, band: tuple[int, int]) -> tuple[np.ndarray, np.ndarray]:
    ep = right_fist_epochs(raw, *band)
    ep.apply_hilbert(envelope=True, verbose="error")
    power = (ep.get_data() ** 2).mean(axis=0)            # (2 channels, time)
    t = ep.times
    ref = power[:, (t >= REF[0]) & (t <= REF[1])].mean(axis=1, keepdims=True)
    pct = (power - ref) / ref * 100
    k = int(0.25 * ep.info["sfreq"])                      # 250 ms moving average
    pct = np.apply_along_axis(lambda x: np.convolve(x, np.ones(k) / k, mode="same"), 1, pct)
    return t, pct


def parse_range(s: str) -> list[int]:
    a, _, b = s.partition("-")
    return list(range(int(a), int(b or a) + 1))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--subjects", default="1-10")
    ap.add_argument("--example-subject", type=int, default=1)
    ap.add_argument("--example-trial", type=int, default=0)
    ap.add_argument("--out", default=str(ROOT / "figures" / "eegmmi-imagined-vs-executed.png"))
    a = ap.parse_args()
    subjects = parse_range(a.subjects)

    curves = {(c, b): [] for c in RUNS for b in BANDS}
    examples = {}
    for s in subjects:
        for cond, runs in RUNS.items():
            raw = load(s, runs)
            for bname, band in BANDS.items():
                t, pct = erd(raw, band)
                curves[(cond, bname)].append(pct)
            if s == a.example_subject:
                ep = right_fist_epochs(raw, 1, 40)
                mu = right_fist_epochs(raw, 8, 12)
                examples[cond] = (ep.times, ep.get_data(picks="C3")[a.example_trial, 0] * 1e6,
                                  mu.get_data(picks="C3")[a.example_trial, 0] * 1e6, len(ep))

    fig = plt.figure(figsize=(12, 9), constrained_layout=True)
    gs = fig.add_gridspec(3, 2, height_ratios=[1, 1, 1])
    colors = {"C3": "#1f77b4", "C4": "#d62728"}

    for j, cond in enumerate(RUNS):
        times, broad, mu, n = examples[cond]
        ax = fig.add_subplot(gs[0, j])
        ax.plot(times, broad, color="0.6", lw=0.7, label="C3, 1–40 Hz")
        ax.plot(times, mu - 60, color=colors["C3"], lw=0.9, label="C3, mu band only (offset −60 µV)")
        ax.axvspan(0, 4.1, color="orange", alpha=0.12, lw=0)
        ax.axvline(0, color="k", lw=0.8)
        ax.set_title(f"A{j+1}. {cond.capitalize()} right fist — one raw trial "
                     f"(subject {a.example_subject}, trial {a.example_trial+1}/{n})", fontsize=10)
        ax.set_xlabel("time from cue (s)"); ax.set_ylabel("µV")
        ax.set_xlim(TMIN, TMAX); ax.legend(fontsize=8, loc="upper right")

    print(f"Mean ERD/ERS in {TASK[0]}–{TASK[1]} s, right fist, {len(subjects)} subjects (mean ± SEM, %):")
    for i, bname in enumerate(BANDS):
        for j, cond in enumerate(RUNS):
            arr = np.array(curves[(cond, bname)])         # (subjects, 2, time)
            m, se = arr.mean(0), arr.std(0, ddof=1) / np.sqrt(len(arr))
            ax = fig.add_subplot(gs[i + 1, j])
            for c, ch in enumerate(["C3", "C4"]):
                lab = f"{ch} ({'contralateral' if ch == 'C3' else 'ipsilateral'})"
                ax.plot(t, m[c], color=colors[ch], label=lab)
                ax.fill_between(t, m[c] - se[c], m[c] + se[c], color=colors[ch], alpha=0.2, lw=0)
                w = (t >= TASK[0]) & (t <= TASK[1])
                vals = arr[:, c, w].mean(1)
                print(f"  {bname:16s} {cond:9s} {ch}: {vals.mean():6.1f} ± {vals.std(ddof=1)/np.sqrt(len(vals)):4.1f}")
            ax.axhline(0, color="k", lw=0.6); ax.axvline(0, color="k", lw=0.8)
            ax.axvspan(0, 4.1, color="orange", alpha=0.12, lw=0)
            ax.set_title(f"B. {cond.capitalize()}: {bname} power vs rest "
                         f"(mean ± SEM, {len(subjects)} subjects)", fontsize=10)
            ax.set_xlabel("time from cue (s)"); ax.set_ylabel("% change")
            ax.set_xlim(TMIN, TMAX); ax.legend(fontsize=8, loc="lower left")

    fig.suptitle("PhysioNet EEG Motor Movement/Imagery — right-fist clenching, imagined vs executed "
                 "(orange = 4.1 s task period; common-average reference)", fontsize=11)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(a.out, dpi=130)
    print("saved", a.out)


if __name__ == "__main__":
    main()
