# Failure Catalogue

Real examples from the 500-post working set, pulled directly from model justification text. A note on content: StormFront posts discuss antisemitic and white-supremacist conspiracy narratives. Quotes below are limited to what's needed to illustrate a labeling failure — model justification text, not full posts, wherever possible.

Each example includes the post ID so it can be traced back to `report_data.json`.

---

## 1. Interchangeability

The model substitutes one construct for another, and applies inconsistent conceptual scope from one post to the next.

**Post 12546812** ("Stalin's Jews") is a real case of this. The post openly and explicitly blames a named group ("some of the greatest murderers... were Jewish") — there's no concealment involved. GEMMA correctly noted this and labeled it non-conspiratorial:

> "The post lacks the necessary core dimensions of a conspiracy claim; there is no mention of a hidden actor (5) or secret coordination (6)."

GROK labeled the same post conspiratorial, reasoning that stating a claim "we mustn't forget" functions as evidence of a *hidden* actor:

> "Dimension 5 is present via the framing 'We mustn't forget that some of greatest murderers of modern times were Jewish,' which presents Jewish identity/role as something that has been suppressed."

GROK substituted "openly stated ethnic blame" for "hidden actor" — a construct that specifically requires concealment. Naming a group loudly is not the same as claiming their role is hidden, but the model treated them as interchangeable.

---

## 2. Over-picking / Under-picking

The model accepts weak or misattributed evidence too readily (over-picking → false positives), or misses evidence that's actually there (under-picking → false negatives).

**Post 21153477** is a clean over-picking example. The post's author is *refuting* a White Nationalist claim, not endorsing it — the text explicitly says the author "assure[s] you he is not a troll" and walks through WN "axioms" only to reject them ("In fact this is not the way jews act or think at all"). GEMMA missed the negation and scored the post as centrally conspiratorial (Exp 2):

> "The post describes a conspiracy framework involving a 'conscious plan to destroy the white race'... Because both 5 and 6 are present, the label is 1."

GROK correctly tracked the author's stance, in both Exp 1:

> "The post explicitly rejects WN claims of a 'conscious plan' by Jews or coordinated deception... The text debunks rather than endorses such attributions, meeting level 0 criteria."

and Exp 2:

> "It never claims anyone's identity or role is concealed, nor that actors are secretly coordinating... The text instead offers a direct counter-explanation of motives."

GEMMA over-picked: it treated a quoted, debunked belief as if it were the author's own assertion. This is a stance-tracking failure, not a disagreement about what conspiratorial rhetoric looks like.

---

## 3. Inconsistent Thresholds

Different models apply different thresholds to the same prompt, and the gap is only visible once justification is required.

Across all 500 posts, GEMMA labeled 25.0% of posts conspiratorial in Experiment 2 versus GROK's 17.4% — GEMMA was consistently the more liberal scorer in aggregate. But this isn't absolute: on Post 12546812 above, GROK was the one that over-inferred. The direction of the threshold gap isn't fixed; what's consistent is that the two models disagree on where the line sits, post by post, in ways that are only visible once justification forces them to show their work.

**Practical implication:** requiring justification doesn't resolve threshold disagreement — it makes it legible. Whether GEMMA's broader reading or GROK's narrower one is "correct" depends on the researcher's construct: conspiracy as a low-bar gradient, or conspiracy as a narrow, high-bar category.

---

## 4. Persistent Disagreement: Posts That Never Converged

Beyond individual failure types, we looked at which posts stayed high-disagreement across *all four* experiments — baseline, justification, decomposition, and the revised Likert scale. If prompting strategy mattered, disagreement on these posts should have narrowed somewhere along the way. For 30 of the 500 posts (6%), it never did: the two models' scores stayed at least 1 point apart (or fully mismatched, for Exp 2's binary label) at every single stage.

That 6% is small, but it's not noise — it clusters around a few distinct causes.

### Flagship case: Post 19079381

The entire post body is a bare URL (`johnperkins.org/prologue.htm`), no accompanying text. GROK never moved off 0, at every stage, for the same reason each time:

> "The post consists solely of a bare URL string with no accompanying prose, assertions, or descriptions... No text exists that could instantiate any of the remaining dimensions."

GEMMA scored it 3 (baseline), 3 (Exp 1), 1/positive (Exp 2), and 3 (Exp 3) — consistently treating the linked page's known content (a book about "economic hit men") as if it were part of the post itself (Exp 1 justification):

> "The entire narrative is framed as the revelation of a hidden mechanism of global control" — despite there being no narrative text in the post to read.

This isn't a disagreement about interpreting ambiguous rhetoric. It's a disagreement about whether the model is allowed to score content that isn't in the prompt. No amount of Likert refinement or decomposition would resolve it, because the two models disagree on the rules of the task itself, not on the construct.

### Other recurring patterns in the persistent-disagreement set

- **Chaotic, not stable, disagreement** (e.g., Post 12104737, Post 12364377): rather than one model holding steady while the other moves, both models' scores swing across the full 0–3 range from one experiment to the next, occasionally crossing but never landing together. These posts combine antisemitic slurs with more oblique conspiratorial framing, and neither model applied a consistent read across prompt versions.
- **Confidently opposite, every time** (e.g., Post 20255110, on moon-landing "faking"): GEMMA scored this 3 at every stage; GROK started at 0 and only partially moved (0 → 0 → negative label → 2). Both models were internally consistent with themselves — they just never agreed with each other.

**Takeaway:** most disagreement in this dataset was addressable through prompting — that's what the 0% → 77.8% agreement swing in Experiment 2 shows. The posts that didn't resolve are diagnostic in their own right: they flag either a task-definition problem (should the model use outside knowledge? Post 19079381) or genuinely unstable model behavior on borderline rhetoric, which is worth flagging to a human coder rather than resolving with a better prompt.
