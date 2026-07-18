# Measuring the Unmeasurable?

**Auditing and Optimization of LLM-Based Text Classification in the Social Sciences**

*SICSS 2026 project by Bo Min Keum (International CyberCrime Research Institute, SFU) and Roman Pomeshchikov (Near and Middle Eastern Studies Interdisciplinary Program, UW).*

View the interactive report: [https://bomin-keum.github.io/SICSS-llm/](https://bomin-keum.github.io/SICSS-llm/)

## Why? (Problem Statement)

Generative LLMs are increasingly used to classify text for abstract, contested social science concepts. Human coders read nuance well but don't scale. LLMs scale but we don't know how good they are at these tasks, and LLM-generated labels need extensive human validation, which is slow and expensive.

Since LLM labeling runs on prompting, and prompting affects what gets measured, we made prompting itself the object of study. We also propose a sampling strategy: instead of validating every label across hundreds of thousands of texts by hand, focus validation on the texts where two models disagree most.

## Data

383K StormFront.org posts were LLM-labeled on 6 radicalization signals, each on a 0-3 scale.

## Sampling

1. From 383K posts, we sampled 1.7K posts where gemma-3-27B and xai-grok-3.1 gave polar-opposite baseline scores (one model 0, the other 3) on how conspiratorial a post reads.
2. From those, we randomly sampled 500 posts: 250 gemma-3-27B-3 / xai-grok-3.1-0, and 250 gemma-3-27B-0 / xai-grok-3.1-3.
3. Those same 500 posts were rescored across 5 experiments, using gemma-3-27B and xai-grok-3.4.

## Experiments

| Exp | Design | Question |
|---|---|---|
| 0 | Baseline, 0-3 Likert | What do the models say with no scaffolding? |
| 1 | 0-3 Likert + justification required | Does requiring justification change the score? |
| 2 | Detailed 0-3 Likert, no justification | Does a more precise scale (i.e. what counts as "1" vs "2", etc) change the score? |
| 3 | Detailed 0-3 Likert + justification | Does combining both change the score further? |
| 4 | Binary label from 11 sub-dimensions | Does decomposing the construct produce more interpretable labels? |

Cross-model agreement: Exp 1 reached 56.6%, Exp 2 reached 35.4%, Exp 3 reached 65.1%, Exp 4 reached 77.8%.

## Report

Check out here! [https://bomin-keum.github.io/SICSS-llm/](https://bomin-keum.github.io/SICSS-llm/)

Sections:

1. Problem Statement
2. Overview of methodology
3. Results: Likert (Exp 0-3)
4. Results: Binary (Exp 4)
5. Label breakdown
6. Where the models disagree, by dimension
7. Consistent disagreements, worked examples
8. Concluding thoughts on optimization
9. Therefore: a 5-point checklist for anyone building a similar measurement prompt

## What we mean by "optimization"

We can't hand-code ground truth for 383K posts. What we can do is track where gemma-3-27B and xai-grok-3.4 agree and disagree, and how that shifts as the prompt changes. That tells us which posts produce persistent disagreement despite prompt refinement, which instructions move one or both models, and which post types would be worth early human coding because they discriminate between competing labelling tendencies. We propose that this offers a leverage: don't validate every label, validate the ones that could help see the shifts to investigate how, and where, the models disagree.

## Repository contents

- `index.html`: the interactive report.
- `README.md`: this file.
- `five_recommendations.md`: five patterns we observed across iterations that could be useful as a checklist for anyone building a similar measurement prompt.

## Acknowledgment

This is a report made during the 2026 Summer Institute of Computational Social Sciences (SICSS) at University of Washington. 
