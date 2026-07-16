# Measuring...the Unmeasurable? An Iterative Framework for Using LLMs to Study Text

*SICSS 2026 project deliverable*

## Why

Concepts like masculinity, populism, humiliation, identity threat, sarcasm, and humour have no objective ground truth. They're theory-dependent, context-sensitive, and contested. Social science has always struggled to measure them.

LLMs are increasingly used to classify text for exactly these concepts. But if the concept itself isn't directly observable, and prompt wording changes what gets measured, then prompt design isn't a technical detail — it's part of construct validity: whether the thing you're scoring is the thing you claim to be scoring.

Human coders handle ambiguity well but don't scale. LLMs scale but their read on ambiguity is opaque. This project asks: **when you can't hand-code everything, how do you refine a prompt until you can trust what it's measuring?**

This repository is a reproducible framework for iteratively testing and refining prompts before treating LLM output as scientific data. We are not asking which prompt performs best. We're asking how researchers can build prompts for nuanced constructs — transparently, theoretically grounded, and reproducibly.

## Data

StormFront forum posts from 99 users (49 with a documented history of violence, 50 without), a dataset used in prior extremism research (e.g., Scrivens, 2022). We focus on conspiratorial rhetoric within these posts.

## Approach: Start Where Models Disagree

Reading every post by hand doesn't scale — our full corpus was 383K posts. Instead, we used model disagreement as a triage signal: posts where two LLMs (GROK and GEMMA) gave polar-opposite scores on the same 0–3 conspiracy scale are the posts most likely to expose differences in how each model *conceptualizes* conspiracy, not just how it applies a scale.

From the full corpus, we isolated 1.7K posts where one model scored 0 and the other scored 3 on the baseline prompt. From those, we randomly sampled 250 GROK0/GEMMA3 posts and 250 GROK3/GEMMA0 posts — 500 posts total — as our working set for iteration.

Across every experiment, we compared not just final labels but **model reasoning**: how each model justified its output, and where the two models' justifications diverged. That comparison is what informed each prompt revision.

## Experiment Pipeline

Each experiment reuses the same 500-post set, so results are directly comparable across stages.

| # | Name | Change from baseline | Question |
|---|------|----------------------|----------|
| 0 | Baseline | Generic conspiracy prompt, 0–3 Likert | What do the models say with no scaffolding? |
| 1 | Justification | Same prompt, model must justify its score | Does requiring justification change the score itself? |
| 2 | Decomposition | Conspiracy broken into 11 sub-dimensions, binary label | Does decomposing the construct produce more interpretable, defensible labels? |
| 3 | Refined Likert | Revised 0–3 Likert informed by Experiments 1–2, no justification required | Does a more precise scale definition retain meaningful variation without the cost of full decomposition? |

**Experiment 0 scale:** 0 = absent, 1 = present but minimal, 2 = present but supporting other content, 3 = central — the message is structured around it.

**Experiment 2 dimensions:** 8 structural dimensions (hidden actor, coordination, hidden truth, causal simplicity, certainty, us-vs-them, urgency, target) plus 3 pragmatic dimensions (sarcasm/irony, mockery/ridicule, coded language). A post required at minimum a hidden actor or coordination to receive a positive label.

## What Iterating Taught Us

Experiment 2's original decision rule — a positive label required *both* a hidden actor and coordination — turned out to be too restrictive. Posts that clearly expressed a conspiratorial worldview (concealed truths, manipulated realities) were scored non-conspiratorial simply because no explicit actor or coordinated group was named. A flat-earth post, for example, implies coordinated concealment without ever stating who's coordinating — and was scored 0 under the original rule.

That forced a revision: alternative pathways to a positive label, reflecting how conspiracy narratives are actually expressed in this context (StormFront; far-right and white-supremacist online extremism) rather than a textbook definition of the construct.

We also saw the two models track extremist argot and coded language differently, which shaped later prompt revisions. Iteration surfaced these gaps; a single-pass "best prompt" search would not have.

## What We Evaluated

At each stage, we assessed whether model reasoning was:

- theoretically coherent
- interpretable
- internally consistent
- transparent
- useful for a researcher deciding what to do next

The goal was never a universal best prompt — it was matching prompting strategy to research purpose.

## Failure Modes

Four recurring failure patterns emerged across iterations. We treat these as checkpoints for anyone building their own measurement prompts.

**1. Construct interchangeability** — the model substitutes one construct for another: ideology treated as conspiracy, conspiracy treated as generalized distrust, grievance treated as anger.

**2. Over-picking / under-picking** — the model either accepts weak evidence too readily (inflated false positives) or misses implicit/contextual evidence (false negatives).

**3. Reasoning–score mismatch** — the model's justification does not actually support the score it assigned.

**4. Inconsistent thresholds** — different models apply different implicit thresholds to identical prompts. Requiring justification is what makes this visible; without it, the disagreement is invisible.

## Repository Contents

- **Prompt library** — every prompt version used across Experiments 0–3.
- **Comparative reasoning** — side-by-side comparisons of how GEMMA and GROK justified the same classification differently, and what that implies about each model's implicit thresholds.
- **Failure catalogue** — documented examples of the four failure modes above, as a checklist for future prompt development.
- **Results report** (`report.html`) — descriptive summary and visualizations of how scores and model agreement shifted across all four experiments.

## Status

This is a working deliverable from a two-week SICSS 2026 project, not a finished paper. Open items before wider publication: full author list, citation for the license/terms under which the StormFront data is shared, and any additional data-source citations beyond Scrivens (2022).
