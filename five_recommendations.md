# Five Recommendations

Real examples from the 500-post working set, pulled directly from model justification text. A note on content: StormFront posts discuss antisemitic and white-supremacist conspiracy narratives. Quotes below are limited to what's needed to illustrate a labeling failure: model justification text, not full posts.

Each example includes the post ID so it can be traced back to the interactive report where you can see per-post outputs across Exp 0-3. Experiment numbering matches `index.html`: Exp 0 (0-3 Likert), Exp 1 (0-3 Likert + justification), Exp 2 (0-3 detailed Likert), Exp 3 (0-3 detailed Likert + justification), Exp 4 (binary, 11-dimension decomposition). All experiments were run on gemma-3-27B and xai-grok-3.4.

---

## 1. Interchangeability

The model substitutes one construct for another, and applies inconsistent conceptual scope from one post to the next.

**Post 12546812** ("Stalin's Jews") is an example. The post openly and explicitly blames a named group ("some of the greatest murderers... were Jewish"). There's no concealment involved. gemma-3-27B correctly noted this and labeled it non-conspiratorial (Exp 4):

> "The post lacks the necessary core dimensions of a conspiracy claim; there is no mention of a hidden actor (5) or secret coordination (6)."

xai-grok-3.4 labeled the same post conspiratorial, reasoning that stating a claim "we mustn't forget" functions as evidence of a *hidden* actor:

> "Dimension 5 is present via the framing 'We mustn't forget that some of greatest murderers of modern times were Jewish,' which presents Jewish identity/role as something that has been suppressed."

xai-grok-3.4 substituted "openly stated ethnic blame" for "hidden actor," a construct that specifically requires concealment. Naming a group loudly is not the same as claiming their role is hidden, but the model treated them as interchangeable.

**Recommendation:** In the prompt, state explicitly that the presence of one dimension should not imply another. For criteria-based prompts, define each dimension's boundary. For 0-3 Likert prompts, be explicit about what counts toward the score and what doesn't.

---

## 2. Over-picking / Under-picking

The model accepts weak or misattributed evidence too readily (over-picking, producing false positives), or misses evidence that's actually there (under-picking, producing false negatives).

**Post 21153477** is an over-picking example. The post's author is *refuting* a White Nationalist claim, not endorsing it. The text explicitly says the author "assure[s] you he is not a troll" and walks through WN "axioms" only to reject them ("In fact this is not the way jews act or think at all"). gemma-3-27B missed the negation and scored the post as centrally conspiratorial (Exp 4):

> "The post describes a conspiracy framework involving a 'conscious plan to destroy the white race'... Because both 5 and 6 are present, the label is 1."

xai-grok-3.4 correctly tracked the author's stance, in both Exp 1:

> "The post explicitly rejects WN claims of a 'conscious plan' by Jews or coordinated deception... The text debunks rather than endorses such attributions, meeting level 0 criteria."

and Exp 4:

> "It never claims anyone's identity or role is concealed, nor that actors are secretly coordinating... The text instead offers a direct counter-explanation of motives."

gemma-3-27B over-picked: it treated a quoted, debunked belief as if it were the author's own argument. This appears to be an oversight of being able to recognize author's stance, not a disagreement about what conspiratorial rhetoric looks like.

**Recommendation:** Sample high-disagreement posts and, if available, read the models' justifications directly. Pay attention to what each model treats as relevant evidence, not just the score.

---

## 3. Inconsistent Thresholds

Different models apply different thresholds to the same prompt, and the gap can be hugely informative when reading the justifications.

Across all 500 posts, gemma-3-27B labeled 25.0% of posts conspiratorial in Exp 4 versus xai-grok-3.4's 17.4%. gemma-3-27B was consistently the more liberal scorer in aggregate. On Post 12546812 above, xai-grok-3.4 was the one that over-inferred. The direction of the threshold gap isn't fixed. What's consistent is that the two models disagree on where the line sits, post by post, in ways that are only visible once justification forces them to show their work.

**Recommendation:** Require the model to produce justifications (and, as we have observed, is also a condition that led to greater agreement). This turns these less-visible threshold disagreement into what researchers can audit. Whether gemma-3-27B's broader reading or xai-grok-3.4's narrower one is "correct" depends on the researcher's construct: it might be of interest to consider conspiracy as a low-bar gradient to consider a wider scope of narratives (for instance, of an emerging online community space where conspiracy is less documented) or conspiracy as a narrow, high-bar category (for instance, for labelling specific forms of conspiracy that is of researcher's interest).

---

## 4. Per Model Justifications

Characterize each model's sensitivity to prompt instruction. We found that the two models don't just disagree on scores, they respond differently to how the prompt is written.

**xai-grok-3.4's** largest swings, across the four posts where its score moved the most (Exp 0 to Exp 1 to Exp 2), all came from bare-link posts (a URL with no other text) pointing to explicitly extremist sites. Under Exp 1, it was willing to infer conspiratorial content from the link's known context:

> "Nazi ideology (and the specific site referenced) is organized around the central claim that societal conditions and white outcomes are the result of deliberate, concealed coordination by hidden actors... This matches Level 3 criteria exactly."

Under the more detailed Likert prompt in Exp 2, it reverted to scoring these same posts 0, treating an empty post body as insufficient evidence regardless of the link. xai-grok-3.4's threshold isn't fixed, it tightens under more explicit scoring criteria.

**gemma-3-27B's** largest swings, across its four biggest movers, all involved explicit antisemitic conspiracy tropes that it confidently scored 3 under Exp 1:

> "The message is organized around a central conspiracy narrative claiming that a specific ethnic group ('the Jew') was the primary adversary in a political struggle... This reflects a core tenet of antisemitic conspiracy theories regarding global control and orchestration."

but dropped to 0 under the more detailed Likert prompt in Exp 2, on the same text. That's a caution against assuming more detailed criteria always improve precision: here, added specificity may have suppressed true positives rather than filtered false ones.

**Recommendation:** Match the model to the task. xai-grok-3.4 responds to explicit, literal criteria, tightening the prompt makes it more conservative, which suits researchers who need a strict, defensible bar (a binary flag for moderation, for example). gemma-3-27B responds to inference-friendly prompts, it catches more but at the cost of precision, which suits researchers prioritizing recall over strict evidentiary standards, provided its positives get reviewed. Neither tendency is "more accurate." They're differently useful depending on what the label needs to do.

---

## 5. Persistent Disagreement: Posts That Never Agreed

Beyond individual failure types, we looked at which posts stayed high-disagreement across every experiment we have data for: Exp 0, Exp 1, Exp 2, and Exp 3. If prompting strategy mattered, our anticipation was that the disagreement on these posts likely narrowed somewhere along the way. For 57 of the 500 posts (11.4%), it never did: the two models' scores stayed at least 1 point apart at every stage.

### Flagship case: Post 19079381

The entire post body is a bare URL (`johnperkins.org/prologue.htm`), no accompanying text. xai-grok-3.4 never moved off 0, at every stage, for the same reason each time:

> "The post consists solely of a bare URL string with no accompanying prose, assertions, or descriptions... No text exists that could instantiate any of the remaining dimensions."

gemma-3-27B scored it 3 (Exp 0), 3 (Exp 1), and 3 (Exp 2), and also labeled it positive under Exp 4's binary decomposition, consistently treating the linked page's known content (a book about "economic hit men") as if it were part of the post itself (Exp 1 justification):

> "The entire narrative is framed as the revelation of a hidden mechanism of global control."

despite there being no narrative text in the post to read. This isn't a disagreement about interpreting ambiguous rhetoric. It's a disagreement about whether the model is allowed to score content that isn't in the prompt, and it holds across every experiment we've run, including the binary decomposition. No amount of Likert refinement would resolve it, because the two models disagree on the rules of the task itself, not on the construct.

### Other recurring patterns in the persistent-disagreement set

- **Chaotic, not stable, disagreement** (for example, Post 12104737, Post 12364377): rather than one model holding steady while the other moves, both models' scores swing across the full 0-3 range from one experiment to the next, occasionally crossing but never agreeing. These posts combine antisemitic slurs with more nuanced conspiratorial framing, and neither model applied a consistent read across prompt versions.
- **Confidently opposite, every time** (for example, Post 20255110, on moon-landing "faking"): gemma-3-27B scored this 3 at every stage; xai-grok-3.4 started at 0 and only partially moved (0, then 0, then 2). Both models were internally consistent with themselves, they just never agreed with each other.

**Recommendation:** Most disagreement in this dataset was addressable through prompting. The posts that didn't resolve seem to be relevant to the content and tone of the posts themselves. They flag either a task-definition problem (should the model use outside knowledge?) or genuinely unstable model behavior on borderline rhetoric, which is worth flagging to a human coder, through human validation, and comparison, of consistently disagreed posts and those that flipped with different prompting. Targeting human validation in these subsets would inform textual characteristics that need incorporating into the prompting (i.e. better attention toward sarcasm/irony) before using LLM-generated labels in research.
