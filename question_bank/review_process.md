# Question Bank — Review Process

## Purpose

The concrete, gated pipeline a question passes through between `Draft` and `Published` (`question_lifecycle.md`), with explicit pass/fail criteria at each gate. This is the question-level counterpart to the module-level review system already established for `knowledge_base/` in `CLAUDE.md` and `reviews/review_template.md` — related in philosophy, but a distinct process operating at a different grain (a single question vs. an entire Knowledge Area module). Do not conflate the two: a Knowledge Area module can be Approved while most of its individual questions are still in Draft, and vice versa is impossible (a question cannot be authored against a module that isn't Approved — see `authoring_guidelines.md`, Step 1).

## Reviewer Roles

- **Technical Reviewer** — checks wording, format, metadata completeness, and answer-design soundness. Does not require deep DAMA subject-matter expertise, but does require familiarity with `question_quality_standards.md` and `authoring_guidelines.md`.
- **DAMA Reviewer** — checks DMBOK2 accuracy, correct `[DAMA]`/`[Industry Practice]` tagging, and citation validity. Requires the same subject-matter fluency already demonstrated across the completed `knowledge_base/` modules and their reviews in `reviews/`.
- **Approval Authority** — confirms both prior gates passed, confirms the record is complete, and performs final sign-off.

In this project's current single-author context, one person (assisted by the CDMP-mentor working mode defined in `CLAUDE.md`) may hold all three roles for a given question. The roles remain distinct **checkpoints** even when held by the same identity — each gate's checklist must still be run explicitly and in order; skipping straight to Approval is not permitted regardless of who is performing the review.

## Gate 1 — Technical Review

**Runs against:** `question_quality_standards.md`, Standards 3, 4, 5, 6, 7, 11, 12 (wording, ambiguity, answer design, explanation completeness, duplication, fairness).

**Checklist:**
- [ ] Stem is clear, complete, and has exactly one interpretation.
- [ ] No negative-phrasing, double-negative, or "all/none of the above" violations (`authoring_guidelines.md`, Stem Writing Rules).
- [ ] Options are grammatically parallel and similarly sized.
- [ ] Exactly one correct answer (or an unambiguous correct set for Multiple Select).
- [ ] Every distractor is plausible, not absurd or trivially eliminable.
- [ ] Explanation includes reasoning for the correct answer and a stated reason for every incorrect option.
- [ ] All required `metadata_schema.md` fields are populated and correctly typed.
- [ ] No unjustified duplication against existing bank content.
- [ ] No fairness/accessibility violations.

**Pass →** DAMA Review. **Fail →** back to `Draft` with specific, itemized revision notes (which checklist item failed and why) attached to the question's review history.

## Gate 2 — DAMA Review

**Runs against:** `question_quality_standards.md`, Standards 1, 2, 8, 9, 10 (accuracy, terminology, cross-reference, source tagging, copyright).

**Checklist:**
- [ ] Correct answer is verified accurate against the cited `knowledge_base/` section and, where feasible, DMBOK2 directly.
- [ ] DAMA terminology is used precisely in stem, options, and explanation.
- [ ] `references` field resolves to a real, specific `knowledge_base/*.md` section — not just the file, the section.
- [ ] `dama_concept` / `industry_practice_concept` classification is correct.
- [ ] `source_confidence` is set accurately per `metadata_schema.md`'s definitions.
- [ ] No verbatim DMBOK2 reproduction beyond a short, explicitly cited quote.
- [ ] If the question targets a documented Exam Trap or Common Mistake, the trap is represented accurately (not a strawman).
- [ ] `taxonomy.md` classification (Knowledge Area / Topic / Subtopic) is correct.
- [ ] `difficulty` and `blooms_level` are consistent with each other and with the actual cognitive demand of the question, per `difficulty_framework.md`'s Level-Selection Guidance.

**Pass →** Approval. **Fail →** back to `Draft` with specific DAMA-accuracy revision notes.

## Gate 3 — Approval

**Runs against:** record completeness and lifecycle integrity, not content quality (already verified by Gates 1–2).

**Checklist:**
- [ ] Both Gate 1 and Gate 2 passed and are recorded in `reviewer`.
- [ ] `question_id` is assigned and unique (per `naming_conventions.md`).
- [ ] `version` is set to `1.0` (first Approval) or the correct next version (`versioning.md`).
- [ ] `creation_date` and `last_modified` are populated.
- [ ] Every `metadata_schema.md` required field is present with no placeholder values remaining.
- [ ] If this is a new major version superseding a Published question, the `supersedes` link is correctly set and the prior version is queued for Retirement on this version's Publication (`versioning.md`).

**Pass →** `Published`. **Fail →** back to `Draft` (rare — reserved for a completeness gap both prior reviewers missed).

## Handling Revision Requests

Every failed gate produces a specific, itemized note (not a vague "needs work") tied to the exact checklist item that failed, attached to the question's review history alongside `reviewer` and the date. This mirrors the specificity standard already modeled in `reviews/reference_and_master_data_review.md` — a review finding names the exact gap and the exact fix, not just a score. A question re-submitted after revision re-enters at the gate it failed, not necessarily from Gate 1, unless the revision was substantive enough to plausibly affect an earlier gate's findings.

## Relationship to the Module-Level Review System

| | Module-level review (`reviews/`) | Question-level review (this document) |
|---|---|---|
| Unit of review | An entire `knowledge_base/*.md` file | A single question record |
| Template | `reviews/review_template.md` | The three gate checklists above |
| Scoring | 0–100 overall score across 11 criteria | Binary pass/fail per gate |
| Threshold to "complete" | 90/100 | All three gates passed |
| Output artifact | `reviews/<module_name>_review.md` | Updated `review_status` / `approval_status` fields on the question record itself, plus review history |
| Trigger | After a Knowledge Area module is completed (`CLAUDE.md`) | After a question is drafted or a revision is resubmitted |

The two systems are deliberately parallel in spirit (both are gated, both produce a durable record of why something passed or failed) but operate independently — a question's Gate 1–3 pipeline never substitutes for, and is never substituted by, its source module's `reviews/` review.
