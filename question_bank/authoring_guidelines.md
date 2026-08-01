# Question Bank — Authoring Guidelines

## Purpose

The practical, step-by-step guide for producing a new question that will actually survive `review_process.md`'s gates. `question_quality_standards.md` defines *what* must be true of a finished question; this document explains *how* to get there.

## Step-by-Step Authoring Process

1. **Choose the target.** Pick a Knowledge Area, Topic, and Subtopic from `taxonomy.md`. The Knowledge Area's `knowledge_base/*.md` module must already be **Approved** (per `CLAUDE.md`'s Approval Workflow) — do not author questions against template-only or still-under-review modules, since there is nothing stable to cite yet.
2. **Check for duplication.** Search existing bank content (by Topic/Subtopic and `keywords`) for a near-duplicate before writing anything new (`question_quality_standards.md`, Standard 11).
3. **Choose the question type.** See "Question Types" below — pick the type that best matches what you're actually testing (recall vs. application vs. sequencing vs. multi-part scenario), not by default habit.
4. **Choose difficulty and Bloom's level together.** These should be a deliberate pair, not independently guessed — see `difficulty_framework.md` for the mapping.
5. **Identify the source.** Locate the exact `knowledge_base/*.md` section the question will test. If you can't point to one, the question isn't ready to be written yet.
6. **Draft the stem.** See "Stem Writing Rules" below.
7. **Draft the options** (or matching pairs, or sequence items). See "Distractor Design" below.
8. **Write the explanation.** Must cover the correct answer's reasoning and why each incorrect option is wrong (`question_quality_standards.md`, Standard 7).
9. **Populate all metadata fields**, including the `[DAMA]` / `[Industry Practice]` classification (`metadata_schema.md`).
10. **Self-check against the Pre-Publish Checklist** in `question_quality_standards.md` before submitting for Technical Review.

## Reuse-First Principle

Every Approved `knowledge_base/` module already contains a Quiz Questions section written to a high bar (full explanations, "why others are wrong" reasoning, related-KA tagging — see `reference_and_master_data.md` and `data_quality.md` for the standard). **Migrating and upgrading these existing questions into full Question Bank records is the fastest, lowest-risk path to Phase 1 content** (`roadmap.md`) — prefer this over writing entirely new questions from scratch where a suitable one already exists. Migration still requires the full metadata schema to be populated and the full review pipeline to run; an existing module quiz question is a strong draft, not a pre-approved bank entry.

## Question Types

| Type | What it tests | Structural notes |
|---|---|---|
| **Multiple Choice** | Recall or single-step application of one concept | One stem, typically 4 options, exactly one correct. The default type for definitional/terminology questions. |
| **Multiple Select** | Recall of a set (e.g., "which of the following are Data Quality dimensions?") | Stem must explicitly state "select all that apply" or a specific count (e.g., "select the three..."). Never leave the expected number of correct answers ambiguous. |
| **True/False** | A single, precise factual claim | Lowest cognitive demand — reserve for claims with genuinely no room for interpretation. Avoid compound claims (two assertions joined by "and," where one is true and one false) — this tests reading carefully, not DAMA knowledge. |
| **Scenario-Based** | Application of a concept to a described business situation | A short (2–5 sentence), original narrative followed by an MCQ or Multiple Select question. Must not paraphrase a `knowledge_base/` Enterprise Example directly — write a new scenario in the same spirit. |
| **Matching** | Correct pairing across a concept set | Two columns (e.g., Role ↔ Responsibility, Term ↔ Definition). A strong fit for content already structured as tables in `knowledge_base/` (role tables, dimension tables). |
| **Ordering** | Correct sequencing of a process or hierarchy | E.g., the DQM lifecycle steps, or Policy → Standard → Procedure. A strong fit for any `knowledge_base/` content already described as a lifecycle, hierarchy, or ordered progression. |
| **Mini Case Study** | Cross-Knowledge-Area integration | One longer (1–2 paragraph), original scenario followed by 2–4 related sub-questions, potentially spanning multiple Knowledge Areas and multiple question types. The highest-effort type to author and review; typically Advanced/Expert difficulty (`difficulty_framework.md`). Directly mirrors the cross-KA integration approach already planned in `roadmap/four_month_plan.md`, Week 12. |

## Stem Writing Rules

- State the question directly and completely in the stem; a learner should be able to attempt an answer before reading the options (the "cover the options" test).
- Avoid negative phrasing ("which of the following is NOT...") unless the negative is the actual point being tested (e.g., identifying a Common Mistake) — and if used, bold or otherwise visually emphasize the negative word so it isn't missed by a fast reader.
- Never stack two negatives in one stem.
- Avoid "all of the above" / "none of the above" as options — they reward test-taking strategy over knowledge and rarely represent a real-world answer choice a CDMP question would offer.
- Keep all options grammatically parallel and similar in length — an option that's conspicuously longer/more detailed than the others is a well-documented "correct answer" tell that undermines the question's validity.
- Avoid absolute words ("always," "never," "only") in distractors unless the trap being tested is specifically about an over-generalization documented as an Exam Trap in the source module (e.g., `reference_and_master_data.md`'s "more centralized MDM styles are always better" trap).

## Distractor Design

A good distractor is not a random wrong answer — it is a **plausible answer that a specific misconception would produce**. Method, in priority order:

1. **First choice: pull directly from a documented Exam Trap or Common Mistake** in the source `knowledge_base/` module. These are, by construction, real misconceptions the module's own author already identified as likely — using them as distractors means the question directly reinforces exam readiness for that trap.
2. **Second choice: a related-but-distinct term** from the same Topic (e.g., for a question about the Data Owner role, a distractor of "Data Steward" is far more useful than "Data Engineer," because it forces the learner to actually distinguish the two, per the Owner-vs-Steward Exam Trap already documented in `data_governance.md`).
3. **Third choice: a term from an adjacent Knowledge Area** that's commonly confused with the correct one (e.g., Metadata Management vs. Master Data Management, per the trap documented in `reference_and_master_data.md`, Section 9).
4. **Avoid:** distractors from an unrelated domain, distractors that are trivially eliminable by grammar/tense mismatch with the stem, and distractors that are technically also correct under a different (unstated) interpretation — this last failure mode is the most common way a "good-looking" distractor accidentally breaks Standard 5 (One Best Answer) in `question_quality_standards.md`.

## Explanation Writing Rules

Every explanation has three required parts, matching the standard already established in every Approved module's Quiz Questions section:

1. **Why the correct answer is correct** — the specific DAMA reasoning, not just a restatement of the answer.
2. **Why each incorrect option is wrong** — one sentence minimum per distractor, naming *why* it's a plausible-but-incorrect answer (ties back to the misconception the distractor was designed around).
3. **Where to learn more** — the specific `knowledge_base/` section (used to populate `references` in `metadata_schema.md`).

## Sourcing Discipline

Applies identically to question authoring as to `knowledge_base/` authoring:

- Tag the underlying concept `[DAMA]` or `[Industry Practice]` via the `dama_concept` / `industry_practice_concept` metadata fields.
- Never reproduce DMBOK2 text verbatim; paraphrase only, per `research/source_map.md` and `question_quality_standards.md`, Standard 10.
- Where the source module itself flags a concept as uncertain or varying across practitioner sources (e.g., MDM style naming), do not write a question that requires a single unambiguous answer to that uncertain point.

## What Not to Author (this phase)

Per this design phase's explicit rules: **no real question content is authored as part of producing this documentation.** Any examples elsewhere in these `question_bank/` documents (stem patterns, ID examples, schema illustrations) are structural placeholders, not usable exam content — do not mistake them for pre-approved starting material.
