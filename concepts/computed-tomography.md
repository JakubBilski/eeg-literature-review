---
slug: computed-tomography
fields: [neuro-clinical]
familiarity: introduced     # human's level: new | introduced | understood | skip
---

# computed-tomography

## Field-neutral description
A method that builds a 3D image of the inside of an object from many X-ray projections taken at different angles. It shows how dense each small volume is, so it reveals structure (shape, mass, fluid, bone), not activity.

## Synonyms by community
- **EEG:** CT, "head CT" (the structural scan done alongside or before EEG)
- **Neuroscience / clinical:** computed tomography, CAT scan, non-contrast head CT (emergency), CT angiography / perfusion (blood vessels, blood flow)
- **Signal processing:** tomographic reconstruction (filtered back-projection, the inverse Radon transform)
- **General ML:** 3D volumetric medical imaging

## What it is for, relative to EEG 🤖
*Textbook knowledge; unsourced in the vault.*
- **Fast, widely available, emergency-first:** used to rule out bleeding, large strokes, tumours or skull fractures in minutes (e.g. after a first seizure or head injury).
- **Uses ionizing radiation**, so it gives single snapshots and is never used for monitoring.
- **Shows structure only**, so a normal CT says nothing about whether seizures are happening. It is less detailed than [[magnetic-resonance-imaging]] for the subtle lesions that cause epilepsy.
- **Historical role:** CT (1970s) replaced EEG for *finding* structural lesions, which narrowed EEG to functional questions → [[q1-what-is-eeg]] *Is EEG redundant to imaging?*

## Papers
- No vault paper discusses CT yet. Candidate: [[bank2022structural]] (structural neuroimaging in new focal epilepsy; screening, not read).

## Variants & disagreements

## Open questions
- What fraction of first-seizure / epilepsy workups find something on CT vs MRI vs EEG? (needs a clinical source)

## Related concepts
- [[magnetic-resonance-imaging]]: the more detailed structural method, also functional (fMRI)
- [[seizure-detection]]: CT rules out structural causes; EEG detects the seizures themselves
