# Question Set Review: Big Data and Data Science (BIGDATA)

**Reviewed set:** `question_bank/questions/big_data_and_data_science/BIGDATA-001.yaml` – `BIGDATA-020.yaml` (20 questions)
**Review date:** 2026-08-02
**Reviewer:** Claude (CDMP Mentor, acting as Technical Reviewer + DAMA Reviewer + Approval Authority per `question_bank/review_process.md`'s single-author context)
**Scope of this review:** Full Gate 1 (Technical Review) → Gate 2 (DAMA Review) → Gate 3 (Approval) pass per `question_bank/question_lifecycle.md`, run against the source module `knowledge_base/big_data_and_data_science.md` (Approved, 92/100 — `reviews/big_data_and_data_science_review.md`).

## Set Composition

| Difficulty | Count | Question Types Used |
|---|---|---|
| Beginner | 5 | Multiple Choice (5) |
| Intermediate | 10 | Multiple Choice (3), Scenario-Based (6), Multiple Select (1) |
| Advanced | 5 | Scenario-Based (3), Multiple Select (2) |
| **Total** | **20** | MC: 8, Scenario-Based: 9, Multiple Select: 3 |

Matches the 5/10/5 difficulty distribution established as precedent, consistent with the type-mix pattern used across recent question sets.

## Non-Duplication Check

Per `question_quality_standards.md`, Standard 11, this set was checked against `knowledge_base/big_data_and_data_science.md`'s own 13 in-module Quiz Questions (Section 13). No direct duplication found — all 20 bank questions use original scenarios and wording. BIGDATA-016 and the module's own Q7 both test subgroup fairness evaluation but use distinct scenarios (a hiring-screening model vs. a healthcare readmission model). BIGDATA-014 specifically targets the Lambda/Kappa Architecture content added during the source module's own improvement pass, which the module's original 12-question quiz predated (Q13 was the module's own only post-improvement quiz addition).

## Gate 1 — Technical Review

- [x] Every stem is clear, complete, with exactly one interpretation.
- [x] No negative-phrasing, double-negative, or "all/none of the above" violations found.
- [x] Options are grammatically parallel and similarly sized across all 20 questions.
- [x] Exactly one correct answer for all Multiple Choice/Scenario-Based questions; unambiguous correct sets for all three Multiple Select questions (BIGDATA-012 "select three," BIGDATA-017 and BIGDATA-020 "select two").
- [x] Every distractor is plausible and tied to a documented misconception (e.g., BIGDATA-019's "models are inherently exempt" distractor and BIGDATA-016's "aggregate accuracy is sufficient" distractor are pulled directly from this Knowledge Area's documented Exam Traps and Common Mistakes, per `authoring_guidelines.md`'s Distractor Design priority order).
- [x] All required `metadata_schema.md` fields populated and correctly typed across all 20 records.
- [x] No unjustified duplication (see above).
- [x] No fairness/accessibility violations — no vendor-specific tooling required; no idioms or trick wording found.

**Gate 1 result: Pass**, all 20 questions.

## Gate 2 — DAMA Review

- [x] Every correct answer verified against `knowledge_base/big_data_and_data_science.md`'s Approved content; no factual errors identified.
- [x] DAMA terminology used precisely throughout (Big Data, Data Science, Data Lake, Model Governance all used exactly as defined in the source module).
- [x] `references` fields resolve to a real, specific section of the source module for all 20 records.
- [x] `dama_concept` / `industry_practice_concept` classification checked against the source module's own tagging — Overfitting, Kappa/Lambda Architecture, CRISP-DM, Citizen Data Science, and the ML vocabulary are correctly tagged `industry_practice_concept` rather than flattened to `[DAMA]`, mirroring the source module's own hedging.
- [x] `source_confidence` set accurately: `High` for core `[DAMA]`-tagged content (Big Data, Data Science, Data Lake/Warehouse distinction, Model Governance, explainability stakes principle, governance-exemption fallacy); `Medium` for `[Industry Practice]`-hedged content (data swamp, ML vocabulary, Lambda/Kappa, CRISP-DM, Citizen Data Science).
- [x] No verbatim DMBOK2 reproduction — all stems and scenarios are original compositions.
- [x] Where a question targets a documented Exam Trap or Common Mistake (BIGDATA-006 targets the Big Data/Data Science conflation trap; BIGDATA-007/BIGDATA-003 target the Lake/Warehouse conflation trap; BIGDATA-016/BIGDATA-019 target the governance-exemption and aggregate-accuracy traps), the trap is represented accurately, not as a strawman.
- [x] `taxonomy.md` classification checked against the BIGDATA Topic/Subtopic breakdown added to `question_bank/taxonomy.md` alongside this module's Approval — all 20 records use a valid Topic from that breakdown.
- [x] `difficulty` and `blooms_level` consistent with actual cognitive demand: Beginner (BIGDATA-001–005) is single-fact recall; Intermediate (BIGDATA-006–015) requires classification or scenario-based application of one concept; Advanced (BIGDATA-016–020) requires multi-factor evaluative or analytical reasoning (fairness evaluation defense, governance-vs-technical distinction, remediation strategy evaluation, exemption-fallacy analysis, success-metric selection) — correctly calibrated above the Intermediate tier.

**Gate 2 result: Pass**, all 20 questions.

## Gate 3 — Approval

- [x] Both Gate 1 and Gate 2 passed and recorded (`reviewer` field updated on each record).
- [x] `question_id` assigned and unique: BIGDATA-001 through BIGDATA-020, no gaps, no collisions with other Knowledge Areas' ID space.
- [x] `version` set to `1.0` on all 20 records.
- [x] `creation_date` and `last_modified` populated on all 20 records.
- [x] Every `metadata_schema.md` required field present with no placeholder values remaining.
- [x] No prior version exists for any of these IDs, so no `supersedes` link applies.

**Gate 3 result: Pass**, all 20 questions. `review_status` updated to `Published` and `approval_status` updated to `Approved` on all 20 records as part of this review.

## Metadata Validation Detail

- **ID/sequence integrity:** BIGDATA-001–020, sequential, zero-padded, no gaps.
- **Cross-reference integrity:** All `references` entries point to `knowledge_base/big_data_and_data_science.md` with a specific section name (or, for BIGDATA-018, an additional cross-module reference to `data_integration_and_interoperability.md`), and resolve to real content in the Approved modules (spot-checked against the live files).
- **Related exercises:** BIGDATA-008, BIGDATA-018 correctly link to Exercise 1; BIGDATA-013, BIGDATA-017 correctly link to Exercise 2; BIGDATA-016 correctly links to Exercise 3 — all three of the module's Section 11 exercises are represented.
- **Type-specific answer structure:** All three Multiple Select records (BIGDATA-012, BIGDATA-017, BIGDATA-020) use the array `correct_answer` shape specified in `metadata_schema.md`; all other records use the single-label shape.

## Summary

The Big Data and Data Science set is accurate, correctly distributed, confirmed non-duplicative against the source module's own quiz, and gives strong targeted coverage to the module's central theme (governance applies to big data/ML, not an exception from it), the Data Lake/Warehouse and data swamp distinctions, and the Lambda/Kappa Architecture and Citizen Data Science content added during the module's own improvement pass. No disqualifying issues were found at any of the three gates.

**Outcome: All 20 questions published.** `review_status: Published`, `approval_status: Approved`, `reviewer: ["Claude (CDMP Mentor) — Technical Review", "Claude (CDMP Mentor) — DAMA Review", "Claude (CDMP Mentor) — Approval Authority"]` set on every `BIGDATA-001.yaml` through `BIGDATA-020.yaml` record, with `last_modified` updated to the review date.
