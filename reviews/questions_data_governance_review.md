# Question Set Review: Data Governance (GOV)

**Reviewed set:** `question_bank/questions/data_governance/GOV-001.yaml` – `GOV-020.yaml` (20 questions)
**Review date:** 2026-08-01
**Reviewer:** Claude (CDMP Mentor, acting as Technical + DAMA Reviewer per `question_bank/review_process.md`)
**Scope of this review:** Initial quality audit of the newly authored set, per `question_bank/question_lifecycle.md`. This review informs readiness for Gate 1 (Technical Review) and Gate 2 (DAMA Review); it does **not** itself flip any question's `review_status`, and no improvements have been applied — per instruction, this is an evaluation-only pass.

## Set Composition

| Difficulty | Count | Question Types Used |
|---|---|---|
| Beginner | 5 | Multiple Choice (5) |
| Intermediate | 10 | Multiple Choice (2), Scenario-Based (5), Multiple Select (3) |
| Advanced | 5 | Scenario-Based (4), Multiple Select (1) |
| **Total** | **20** | MC: 7, Scenario-Based: 9, Multiple Select: 4 |

Matches the requested 5/10/5 distribution and uses all three requested question types (Multiple Choice, Scenario-Based, Multiple Select).

> **Correction (reconciliation pass):** This table originally misreported the question-type sub-counts (MC and Scenario-Based were transposed). Corrected against a direct field-level recount of `question_bank/questions/data_governance/*.yaml`; see `research/question_bank_audit.md`. No question files were affected — this was a review-document error only.

## 1. Accuracy

Every correct answer and explanation was checked against the corresponding `knowledge_base/data_governance.md` section (cited in each question's `references` field). All 20 questions' correct answers are consistent with that source. Two questions (GOV-015, GOV-016) rest on `[Industry Practice]`/regulatory content (zone-based governance; BCBS 239) rather than pure `[DAMA]` content — both are tagged `source_confidence: Medium` and `High` respectively and are accurately represented, but their accuracy is bounded by the source module's own caveats (e.g., GOV-015's underlying module content is itself flagged `[Industry Practice]` for the zone terminology). No factual errors identified.

## 2. Difficulty

The difficulty progression holds up on inspection: Beginner questions (GOV-001–005) are single-fact recall answerable directly from a definition; Intermediate questions (GOV-006–015) consistently require classifying a described example against a framework or applying a role distinction, matching `difficulty_framework.md`'s Intermediate criteria; Advanced questions (GOV-016–020) all require evaluating a multi-factor scenario (a merger, a regulatory requirement, a funding crisis) rather than a single lookup, matching the Advanced tier's "reasoning about a tradeoff or decision" standard. One observation: GOV-013 and GOV-008 (both Intermediate Multiple Select) are borderline — their reasoning is closer to a direct recall-and-match than genuine "Understand/Apply" synthesis, and could arguably sit at the boundary with Beginner. Not a defect, but worth a second look during formal DAMA Review.

## 3. DAMA Alignment

`dama_concept` and `industry_practice_concept` tagging is consistent throughout — 18 of 20 questions are pure `[DAMA]`; GOV-015 and GOV-016 correctly carry an `industry_practice_concept` or a named regulation alongside their DAMA concept, matching the source module's own tagging discipline. No question misrepresents an Industry Practice concept as DAMA-official or vice versa. Terminology (Owner, Steward, Custodian, Council, Policy/Standard/Procedure, operating models) is used precisely and consistently with `knowledge_base/data_governance.md` throughout.

## 4. Ambiguity

No question was found with two defensible correct answers. Several questions (GOV-007, GOV-009, GOV-013) deliberately test the Owner/Steward/Custodian boundary using near-identical scenario framing — this is intentional (mirroring the source module's own repeated emphasis on this boundary as the highest-value exam distinction) rather than accidental redundancy, but a future reviewer should confirm three separate questions probing the same boundary at Intermediate difficulty is the right density rather than over-indexing on one distinction at the expense of others in the Knowledge Area (e.g., no question in this set specifically targets the Governance-vs-Data-Quality-Management relationship). Flagged for consideration in a later improvement pass, not treated as a defect now.

## 5. Explanation Quality

All 20 questions include a full explanation for the correct answer and a distinct, specific reason for every incorrect option — none rely on a bare "this is wrong" statement. Distractor reasoning consistently ties back to a real, named misconception (e.g., GOV-007's distractors are framed around the Owner/Steward/Custodian/Architect confusion set, not arbitrary wrong answers), satisfying `question_quality_standards.md`, Standards 6 and 7. Explanation length is appropriately concise for a question-bank record (2–4 sentences) rather than reproducing the source module's full paragraph-length treatment — correct scope for this artifact type per `authoring_guidelines.md`.

## Summary

The Data Governance set is internally consistent, accurately sourced, and appropriately distributed across difficulty and type. No question is disqualifying. The two items flagged above (borderline difficulty placement on GOV-008/GOV-013; possible over-concentration on the Owner/Steward/Custodian boundary relative to other GOV topics) are minor and suitable for a future improvement pass, not blockers to proceeding through `review_process.md`'s formal gates. No changes have been made to any question file as part of this review.
