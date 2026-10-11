---
slug: magnetic-resonance-imaging
fields: [neuro-clinical, eeg]
familiarity: introduced     # human's level: new | introduced | understood | skip
---

# magnetic-resonance-imaging

## Field-neutral description
A method that images the inside of the body using a strong magnetic field and radio waves, which make hydrogen nuclei in different tissues give off distinguishable signals. In its standard form it shows detailed structure. A variant (fMRI) tracks slow changes in blood oxygenation as an indirect proxy for activity.

## Synonyms by community
- **EEG:** MRI, structural MRI (used for source localization head models), simultaneous EEG-fMRI
- **Neuroscience / clinical:** MRI (T1 / T2 / FLAIR sequences), epilepsy-protocol MRI, fMRI / BOLD signal (blood-oxygen-level dependent), "MRI-negative" (lesional vs non-lesional) epilepsy
- **Signal processing:** k-space reconstruction (inverse Fourier transform)
- **General ML:** 3D volumetric imaging; fMRI as a low-rate 4D spatiotemporal signal

## What it is for, relative to EEG 🤖
*Textbook knowledge; unsourced in the vault except where cited.*
- **Structural MRI** is the most sensitive way to find epilepsy-causing lesions (scars, malformations of cortical development, hippocampal sclerosis), but many people with epilepsy have a normal MRI ("MRI-negative"). It shows a candidate cause, not whether seizures occur.
- **fMRI** measures blood oxygenation (BOLD) with mm spatial resolution, but the signal lags neural activity by seconds and recording happens inside a scanner. EEG has ms resolution and works at the bedside for days.
- **Complementary in epilepsy surgery:** MRI finds a lesion, EEG (scalp, then intracranial) shows where seizures start. MR-negative cases rely on multimodal combinations ([[riha2022multimodal]], screening).
- EEG "can be combined with MRI, fNIRS and PET" [[chaddad2023electroencephalography]] (§1).
- → [[q1-what-is-eeg]] *Is EEG redundant to imaging?* (comparison table of EEG, MEG, fMRI, PET, fNIRS, ultrasound)

## Papers
- [[chaddad2023electroencephalography]]: mentions only that EEG can be combined with MRI (§1).
- Candidates (screening, not read): [[bank2022structural]] (structural imaging in new focal epilepsy), [[riha2022multimodal]] (multimodal localization in MR-negative epilepsy).

## Variants & disagreements
- Structural MRI vs fMRI answer different questions (anatomy vs a slow activity proxy). Keep them apart when comparing with EEG.

## Open questions
- How often is MRI normal in confirmed epilepsy, and how often does EEG change the diagnosis when MRI is normal? (needs a 2022+ clinical source)

## Related concepts
- [[computed-tomography]]: faster, cruder structural imaging; uses radiation
- [[seizure-detection]]: MRI finds the lesion; EEG finds the seizures
- [[electrode-types]]: intracranial EEG, guided by MRI, in surgical workups
