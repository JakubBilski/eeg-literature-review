"""Plot one annotated seizure from CHB-MIT (PhysioNet) as raw multichannel EEG plus a spectrogram.

Expects the EDF in data/eeg/chbmit/ (gitignored). Download, e.g. with parallel range requests:
  https://physionet.org/files/chbmit/1.0.0/chb01/chb01_03.edf
Seizure times come from chb01-summary.txt in the same folder (chb01_03: 2996–3036 s).

Draws:
  A) the 18 standard bipolar channels from 30 s before onset to 20 s after offset, seizure shaded;
  B) a spectrogram of the channel with the largest power during the seizure.

Example: python scripts/plot_seizure.py --file chb01_03.edf --onset 2996 --offset 3036
"""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mne
import numpy as np
from scipy.signal import spectrogram

ROOT = Path(__file__).resolve().parent.parent
CHANNELS = ["FP1-F7", "F7-T7", "T7-P7", "P7-O1", "FP1-F3", "F3-C3", "C3-P3", "P3-O1",
            "FP2-F4", "F4-C4", "C4-P4", "P4-O2", "FP2-F8", "F8-T8", "T8-P8", "P8-O2",
            "FZ-CZ", "CZ-PZ"]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", default="chb01_03.edf")
    ap.add_argument("--onset", type=float, default=2996)
    ap.add_argument("--offset", type=float, default=3036)
    ap.add_argument("--pre", type=float, default=30)
    ap.add_argument("--post", type=float, default=20)
    ap.add_argument("--out", default="figures/chbmit-seizure-chb01_03.png")
    a = ap.parse_args()

    raw = mne.io.read_raw_edf(ROOT / "data" / "eeg" / "chbmit" / a.file, preload=True, verbose="error")
    names = {n.upper(): n for n in raw.ch_names}
    picks = [names[c] for c in CHANNELS if c in names]   # first occurrence (T8-P8 is duplicated)
    raw.pick(picks)
    raw.filter(0.5, 40, verbose="error")
    t0, t1 = a.onset - a.pre, a.offset + a.post
    data, times = raw.get_data(tmin=t0, tmax=t1, return_times=True)
    data *= 1e6                       # V -> µV
    sf = raw.info["sfreq"]

    pre = (times >= t0) & (times < a.onset)
    ict = (times >= a.onset) & (times < a.offset)
    ratio = data[:, ict].var(axis=1) / data[:, pre].var(axis=1)
    best = int(np.argmax(data[:, ict].var(axis=1)))

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12), height_ratios=[3, 1.2], sharex=True)
    gap = 400
    for i, ch in enumerate(raw.ch_names):
        ax1.plot(times, data[i] - i * gap, lw=0.5, color="C3" if i == best else "k")
    ax1.set_yticks([-i * gap for i in range(len(raw.ch_names))], raw.ch_names, fontsize=8)
    ax1.axvspan(a.onset, a.offset, color="C1", alpha=0.15, label="seizure (expert annotation)")
    ax1.plot([t0 + 2, t0 + 2], [gap * 0.6, gap * 0.6 - 200], color="k", lw=2)
    ax1.text(t0 + 3, gap * 0.6 - 100, "200 µV", va="center", fontsize=8)
    ax1.set_ylim(-len(raw.ch_names) * gap, gap * 1.2)
    ax1.legend(loc="upper right", fontsize=8)
    ax1.set_title(f"CHB-MIT {a.file}: seizure {a.onset:.0f}–{a.offset:.0f} s "
                  f"(18 bipolar channels, 0.5–40 Hz)\nred = channel with most seizure power ({ratio[best]:.0f}× its pre-seizure power)")

    f, t, s = spectrogram(data[best], fs=sf, nperseg=int(2 * sf), noverlap=int(1.75 * sf))
    keep = f <= 30
    ax2.pcolormesh(t + times[0], f[keep], 10 * np.log10(s[keep] + 1e-12), shading="auto", cmap="viridis",
                   vmin=np.percentile(10 * np.log10(s[keep] + 1e-12), 5))
    ax2.axvline(a.onset, color="w", ls="--", lw=1)
    ax2.axvline(a.offset, color="w", ls="--", lw=1)
    ax2.set_ylabel(f"{raw.ch_names[best]}\nfrequency (Hz)")
    ax2.set_xlabel("time in recording (s)")
    ax1.tick_params(labelbottom=True)
    fig.tight_layout()
    out = ROOT / a.out
    fig.savefig(out, dpi=130)
    print(f"wrote {out}; best channel {raw.ch_names[best]} ratio {ratio[best]:.1f}")
    for ch, r, v in sorted(zip(raw.ch_names, ratio, data[:, ict].std(axis=1)), key=lambda x: -x[2])[:6]:
        print(f"  {ch:8s} ictal SD {v:6.1f} uV, {r:5.1f}x pre-seizure power")
    print("  median pre-seizure SD %.1f uV" % np.median(data[:, pre].std(axis=1)))


if __name__ == "__main__":
    main()
