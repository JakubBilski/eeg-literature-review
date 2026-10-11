---
slug: electrode-types
fields: [eeg, neuro-clinical, signal-processing]
familiarity: introduced     # human's level: new | introduced | understood | skip
---

# electrode-types

## Field-neutral description
A sensor that picks up a weak electrical signal through a poorly conducting surface can either use a conductive filler to bridge the gap, or press directly against the surface. The filler improves signal quality but costs setup time and comfort. Sensors may also amplify the signal on the spot, before the cable can pick up interference.

## Synonyms by community
- **EEG:** gel / wet (saline, sponge) / dry electrodes; Ag/AgCl; active vs passive electrodes; shielded cables; hybrid (dry or gel); electrode impedance
- **Neuroscience / clinical:** electrode–skin interface, contact impedance, cup electrodes, "prep" (skin abrasion)
- **Signal processing:** sensor front-end, pre-amplification, contact noise, impedance mismatch, EMI pickup
- **General ML:** (no direct term) sensor modality / acquisition domain shift

## Papers
- [[niso2022wireless]]: the trade-offs (§3.4–3.5):
  - **Gel:** the outer skin layer conducts poorly, so electrolyte gel is injected under each Ag/AgCl disk, often after lightly abrading the skin. Best signal quality and some buffering against movement. Costs: the most work, the gel dries (which limits duration), and it leaves residue (pp. 5–6).
  - **Dry:** contact by pressure alone, so setup is fast. Downsides: discomfort, "sometimes as low as 15 min"; higher noise, because noise is inversely proportional to contact area; and drift below 2 Hz from sweat, which forces higher high-pass cut-offs. Best for "short-term recordings in relatively stationary settings" (p. 6).
  - **Wet (saline):** Ag/AgCl in a soaked sponge, an intermediate option. Recording time is shorter than with gel because the solution evaporates (p. 6).
  - **Active:** a pre-amplifier inside the electrode, so the cable can't act as an antenna. Better at high impedance (dry electrodes, rushed setup), but passive electrodes are cleaner at low impedance in the lab. Active electrodes are heavier and costlier (§3.5).
  - **Shielded:** a metal layer around the cable against interference in transit. Heavier and more expensive (§3.5).
- [[varbu2022past]]: second-hand comparisons (p. 15). Soufineyestani: dry headsets are more robust to line noise but carry more artifacts, and both types degrade over time as moisture evaporates. Hinrichs 2020: wireless dry vs wired wet clinical EEG were "comparable", with slightly more artifacts on dry, less sensitivity to electromagnetic interference, and both patients and volunteers preferred dry for self-application.
- [[gans2024sleep]]: form factors in sleep wearables (Table 1): dry electrodes in a headband (Dreem), hydrogel forehead patches (LANMAO, Bittium silver-ink, Onera), a pre-gelled self-applied grid (trEEGrid), a flex-printed adhesive strip behind the ear (cEEGrid), in-ear electrodes (IDUN). The dry Dreem had <20% artifacts in most tests (p. 9). There is no head-to-head comparison by electrode type.
- [[sabio2024scoping]]: consumer headsets use "minimal or no conductive medium" (§Consumer-grade EEG devices). 🤖 This is plausibly one cause of the higher noise floor reported in §Validation. *(see [[consumer-grade-eeg-devices]])*

## Variants & disagreements
- Dry-electrode quality: some reports find new dry systems comparable to conventional ones (Kam 2019), others find worse signal in moving participants (Mathewson 2017), both as cited in [[niso2022wireless]] (p. 6). There are "very few published results" with dry electrodes in mobile settings (p. 6). Hinrichs 2020 (clinical, comparable) is on the optimistic side, as cited in [[varbu2022past]] (p. 15).
- Active vs passive: no general winner; it depends on impedance and setting [[niso2022wireless]] (§3.5).

## Open questions
- Does electrode type leave a learnable "device fingerprint" that hurts cross-dataset transfer for foundation models? No source in the vault.
- New materials (conductive polymers, graphene, textile, tattoo electrodes): how good are they? Casson 2019 is cited as the review [[niso2022wireless]] (p. 6).

## Related concepts
- [[signal-quality-and-noise]]: electrode type is the main hardware-side factor.
- [[consumer-grade-eeg-devices]]: mostly dry or saline electrodes.
