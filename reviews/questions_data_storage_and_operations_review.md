# Question Set Review: Data Storage and Operations (STOR)

**Reviewed set:** `question_bank/questions/data_storage_and_operations/STOR-001.yaml` – `STOR-020.yaml` (20 questions)
**Review date:** 2026-08-02
**Reviewer:** Claude (CDMP Mentor, acting as Technical Reviewer + DAMA Reviewer + Approval Authority per `question_bank/review_process.md`'s single-author context)
**Scope of this review:** Full Gate 1 (Technical Review) → Gate 2 (DAMA Review) → Gate 3 (Approval) pass per `question_bank/question_lifecycle.md`, run against the source module `knowledge_base/data_storage_and_operations.md` (Approved, 92/100 — `reviews/data_storage_and_operations_review.md`).

## Set Composition

| Difficulty | Count | Question Types Used |
|---|---|---|
| Beginner | 5 | Multiple Choice (5) |
| Intermediate | 10 | Multiple Choice (4), Scenario-Based (5), Multiple Select (1) |
| Advanced | 5 | Scenario-Based (4), Multiple Select (1) |
| **Total** | **20** | MC: 9, Scenario-Based: 9, Multiple Select: 2 |

Matches the 5/10/5 difficulty distribution established as precedent. Question-type mix is weighted slightly more toward Scenario-Based than prior sets, appropriate given this Knowledge Area's operational/applied nature (RPO/RTO reasoning, environment risk diagnosis, capacity planning evaluation).

## Non-Duplication Check

Per `question_quality_standards.md`, Standard 11, this set was checked against `knowledge_base/data_storage_and_operations.md`'s own 13 in-module Quiz Questions (Section 13). No direct duplication found — all 20 bank questions use original scenarios and wording. STOR-006 and the module's own Q2 both test RPO/RTO reasoning but use distinct scenarios (backup-interval math vs. a restored-but-lossy narrative) and are not near-duplicates per Standard 11's "different scenario, different wording" allowance. STOR-019 specifically targets the Data Virtualization content added during the source module's own improvement pass, which the module's original 12-question quiz predated (Q13 was the only post-improvement addition to the module's own quiz).

## Gate 1 — Technical Review

- [x] Every stem is clear, complete, with exactly one interpretation.
- [x] No negative-phrasing, double-negative, or "all/none of the above" violations found.
- [x] Options are grammatically parallel and similarly sized across all 20 questions.
- [x] Exactly one correct answer for all Multiple Choice/Scenario-Based questions; unambiguous correct sets for both Multiple Select questions (STOR-012 "select three," STOR-017 "select two").
- [x] Every distractor is plausible and tied to a documented misconception (e.g., STOR-017's "team wants to avoid learning SQL" and "newer is always better" distractors are pulled directly from this Knowledge Area's documented anti-patterns, per `authoring_guidelines.md`'s Distractor Design priority order).
- [x] All required `metadata_schema.md` fields populated and correctly typed across all 20 records.
- [x] No unjustified duplication (see above).
- [x] No fairness/accessibility violations — no vendor-specific UI knowledge required; no idioms or trick wording found.

**Gate 1 result: Pass**, all 20 questions.

## Gate 2 — DAMA Review

- [x] Every correct answer verified against `knowledge_base/data_storage_and_operations.md`'s Approved content; no factual errors identified.
- [x] DAMA terminology used precisely throughout (RPO, RTO, HA, DR/BCP, Data Virtualization all used exactly as defined in the source module).
- [x] `references` fields resolve to a real, specific section of the source module for all 20 records.
- [x] `dama_concept` / `industry_practice_concept` classification checked against the source module's own tagging — SAN/NAS/DAS, document/column-family database categories, shared responsibility model, and capacity planning are correctly tagged `industry_practice_concept` rather than flattened to `[DAMA]`, mirroring the source module's own hedging.
- [x] `source_confidence` set accurately: `High` for core `[DAMA]`-tagged content (RPO/RTO, DBA, masking, retention, HA/DR, database operations); `Medium` for `[Industry Practice]`-hedged content (SAN classification, document/column-family database fit, shared responsibility, capacity planning).
- [x] No verbatim DMBOK2 reproduction — all stems and scenarios are original compositions.
- [x] Where a question targets a documented Exam Trap or Common Mistake (STOR-010 targets Common Mistake 1; STOR-013 and STOR-006 target the RPO/RTO and cloud-governance traps in Section 9; STOR-017 targets the "newer/NoSQL is always better" trap; STOR-018 targets Common Mistakes 4 and 7), the trap is represented accurately, not as a strawman.
- [x] `taxonomy.md` classification checked against the STOR Topic/Subtopic breakdown added to `question_bank/taxonomy.md` alongside this module's Approval — all 20 records use a valid Topic from that breakdown.
- [x] `difficulty` and `blooms_level` consistent with actual cognitive demand: Beginner (STOR-001–005) is single-fact recall; Intermediate (STOR-006–015) requires classification or scenario-based application of one concept; Advanced (STOR-016–020) requires multi-factor evaluative or analytical reasoning (differentiated recovery targets, technology tradeoff evaluation, governance-boundary analysis, virtualization tradeoff analysis, proactive-vs-reactive evaluation) — correctly calibrated above the Intermediate tier.

**Gate 2 result: Pass**, all 20 questions.

## Gate 3 — Approval

- [x] Both Gate 1 and Gate 2 passed and recorded (`reviewer` field updated on each record).
- [x] `question_id` assigned and unique: STOR-001 through STOR-020, no gaps, no collisions with other Knowledge Areas' ID space.
- [x] `version` set to `1.0` on all 20 records.
- [x] `creation_date` and `last_modified` populated on all 20 records.
- [x] Every `metadata_schema.md` required field present with no placeholder values remaining.
- [x] No prior version exists for any of these IDs, so no `supersedes` link applies.

**Gate 3 result: Pass**, all 20 questions. `review_status` updated to `Published` and `approval_status` updated to `Approved` on all 20 records as part of this review.

## Metadata Validation Detail

- **ID/sequence integrity:** STOR-001–020, sequential, zero-padded, no gaps.
- **Cross-reference integrity:** All `references` entries point to `knowledge_base/data_storage_and_operations.md` with a specific section name, and resolve to real content in the Approved module (spot-checked against the live file).
- **Related exercises:** STOR-001, STOR-006, and STOR-010 correctly link to Exercise 1; STOR-011 and STOR-004 correctly link to Exercise 3; STOR-015 and STOR-018 correctly link to Exercise 2 — all three of the module's Section 11 exercises are represented.
- **Type-specific answer structure:** Both Multiple Select records (STOR-012, STOR-017) use the array `correct_answer` shape specified in `metadata_schema.md`; all other records use the single-label shape.

## Summary

The Data Storage and Operations set is accurate, correctly distributed, confirmed non-duplicative against the source module's own quiz, and gives strong targeted coverage to the module's highest-value distinction (RPO vs. RTO), its governance-boundary theme (Owner/Custodian accountability for retention and recovery targets), and the Data Virtualization content added during the module's own improvement pass. No disqualifying issues were found at any of the three gates.

**Outcome: All 20 questions published.** `review_status: Published`, `approval_status: Approved`, `reviewer: ["Claude (CDMP Mentor) — Technical Review", "Claude (CDMP Mentor) — DAMA Review", "Claude (CDMP Mentor) — Approval Authority"]` set on every `STOR-001.yaml` through `STOR-020.yaml` record, with `last_modified` updated to the review date.
