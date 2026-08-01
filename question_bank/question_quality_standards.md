# Question Bank — Question Quality Standards

## Purpose

This is the acceptance bar every question must clear before it can pass Technical Review and DAMA Review (see `review_process.md`). It exists so "quality" is a checkable list of criteria, not a subjective impression — the same philosophy already applied to `knowledge_base/` modules via `reviews/review_template.md`.

## The Standards

### 1. CDMP Accuracy
The question, its correct answer, and its explanation must be factually consistent with DAMA-DMBOK2 as the primary authority, per `research/source_map.md`'s priority hierarchy. Where a question touches an area of genuine ambiguity (e.g., MDM architecture-style naming, which `reference_and_master_data.md` itself flags as varying across practitioner sources), the question must be written so that ambiguity doesn't affect which option is correct — never test a fact that isn't settled.

### 2. DAMA Terminology
The question must use DMBOK2's own terms precisely (e.g., "Data Steward" not "data person," "Survivorship Rule" not "conflict rule"). If a question deliberately tests a commonly-confused term pair (a documented Exam Trap from the relevant `knowledge_base/` module), the terminology itself must still be precise — the *trap* should be in the reasoning required, not in sloppy question wording.

### 3. Clear Wording
No unnecessarily complex sentence structure, no ambiguous pronouns, no idioms that could confuse a non-native English speaker (the real CDMP exam explicitly accommodates ESL candidates — see `research/cdmp_exam_overview.md`). A learner who knows the material should never be unsure what is being asked.

### 4. No Ambiguity
Exactly one interpretation of the stem must be possible. If two DAMA-literate readers could reasonably disagree about what's being asked (not about the *answer* — about the *question*), it fails this standard regardless of how well-written the options are.

### 5. One Best Answer
For Multiple Choice, True/False, Matching, and Ordering types, exactly one option/arrangement is correct — never two defensible "best" answers, and never a correct answer that depends on an interpretation not stated in the stem. For Multiple Select, the full and exact set of correct options must be unambiguous, and the stem must indicate the type of selection expected (e.g., "select all that apply" or a stated count, per `authoring_guidelines.md`).

### 6. Plausible Distractors
Every incorrect option must represent a genuine, realistic misconception — ideally one already documented as an Exam Trap or Common Mistake in the relevant `knowledge_base/` module — not an arbitrary or absurd wrong answer included only to fill a slot. A distractor that no reasonably-prepared candidate would ever select adds no discriminating value and fails this standard. See `authoring_guidelines.md`, "Distractor Design," for the full method.

### 7. Educational Explanation
Every question must include an explanation that teaches the concept, not just confirms the answer — matching the standard already set by the completed `knowledge_base/` modules' Quiz Questions sections (e.g., `data_quality.md`, `reference_and_master_data.md`), which give a full explanation for the correct answer plus a reasoned rebuttal of every incorrect option. A bare "Correct answer: B" with no reasoning fails this standard outright.

### 8. Cross-Reference to Knowledge Area
Every question must cite the specific `knowledge_base/*.md` file and section it is drawn from (the `related_knowledge_areas` and `references` metadata fields — see `metadata_schema.md`). A question with no traceable source cannot be DAMA-reviewed, because there is nothing to check it against.

## Additional Standards (beyond the base list, required by this project's existing conventions)

### 9. Source Tagging Discipline
Every question's underlying concept must be classified via the `dama_concept` / `industry_practice_concept` metadata fields (see `metadata_schema.md`), exactly mirroring the `[DAMA]` / `[Industry Practice]` convention used throughout `knowledge_base/`. A question testing an Industry Practice concept (e.g., "Customer 360," a Data Contract) must never be framed as if it were DAMA-official content, and vice versa.

### 10. No Copyrighted Reproduction
No question stem, scenario, or explanation may reproduce DMBOK2 text verbatim beyond a short (<25 word), explicitly marked and cited quotation — identical to the rule already enforced in `sources/README.md` and every `knowledge_base/` module's editorial note. Scenario-Based and Mini Case Study questions in particular must be **original** business scenarios, not paraphrased DMBOK2 examples.

### 11. Non-Duplication
Before authoring, an author must check the target Topic/Subtopic (`taxonomy.md`) and existing `keywords` for near-duplicate questions already in the bank. A near-duplicate is acceptable only if it deliberately targets a different Bloom's level, question type, or difficulty (per `difficulty_framework.md`) — duplication for its own sake dilutes the bank without adding assessment value.

### 12. Fairness and Accessibility
No question may assume knowledge outside the DMBOK2/DAMA domain (e.g., assuming familiarity with a specific commercial vendor's UI) to determine the correct answer — a named tool may appear in a scenario for realism, but the *reasoning required* must be domain-general. No question may rely on cultural idioms, regional assumptions, or trick wording (double negatives, hidden absolutes) that test reading comprehension instead of DAMA knowledge.

## Pre-Publish Checklist

A question is not eligible for the Approval gate (`question_lifecycle.md`) until every item below is checked:

- [ ] Correct answer verified against `knowledge_base/` and, where possible, DMBOK2 directly.
- [ ] DAMA terminology used precisely throughout stem, options, and explanation.
- [ ] Stem has exactly one valid interpretation.
- [ ] Exactly one correct answer (or, for Multiple Select, an unambiguous correct set).
- [ ] Every distractor is plausible and tied to a real misconception where possible.
- [ ] Explanation covers the correct answer's reasoning AND why every incorrect option is wrong.
- [ ] `related_knowledge_areas` and `references` resolve to a real, specific `knowledge_base/` section.
- [ ] `dama_concept` / `industry_practice_concept` correctly classified.
- [ ] No verbatim DMBOK2 reproduction beyond a short, cited quote.
- [ ] Checked against existing bank content for unjustified duplication.
- [ ] No unfair, culturally-biased, or trick wording.
- [ ] All required `metadata_schema.md` fields populated.

This checklist is the operational form of `review_process.md`'s Gate 1 and Gate 2 criteria — reviewers apply it directly rather than re-deriving standards from prose each time.
