# Question Set Review: Data Security (SEC)

**Reviewed set:** `question_bank/questions/data_security/SEC-001.yaml` – `SEC-020.yaml` (20 questions)
**Review date:** 2026-08-02
**Reviewer:** Claude (CDMP Mentor, acting as Technical Reviewer + DAMA Reviewer + Approval Authority per `question_bank/review_process.md`'s single-author context)
**Scope of this review:** Full Gate 1 (Technical Review) → Gate 2 (DAMA Review) → Gate 3 (Approval) pass per `question_bank/question_lifecycle.md`, run against the source module `knowledge_base/data_security.md` (Approved, 93/100 — `reviews/data_security_review.md`).

## Set Composition

| Difficulty | Count | Question Types Used |
|---|---|---|
| Beginner | 5 | Multiple Choice (5) |
| Intermediate | 10 | Multiple Choice (4), Scenario-Based (5), Multiple Select (1) |
| Advanced | 5 | Scenario-Based (4), Multiple Select (1) |
| **Total** | **20** | MC: 9, Scenario-Based: 9, Multiple Select: 2 |

Matches the 5/10/5 difficulty distribution established as precedent, with the same type-mix pattern (weighted toward Scenario-Based) used for `data_storage_and_operations.md`'s question set, appropriate given this Knowledge Area's applied, judgment-heavy nature.

## Non-Duplication Check

Per `question_quality_standards.md`, Standard 11, this set was checked against `knowledge_base/data_security.md`'s own 13 in-module Quiz Questions (Section 13). No direct duplication found — all 20 bank questions use original scenarios and wording. SEC-006 and the module's own Q2 both test the Authentication/Authorization distinction but use distinct scenarios (a general engineer/report scenario vs. a login/table-access scenario). SEC-018 specifically targets the Encryption Key Management content added during the source module's own improvement pass, which the module's original 12-question quiz predated (Q13 was the module's own only post-improvement quiz addition).

## Gate 1 — Technical Review

- [x] Every stem is clear, complete, with exactly one interpretation.
- [x] No negative-phrasing, double-negative, or "all/none of the above" violations found.
- [x] Options are grammatically parallel and similarly sized across all 20 questions.
- [x] Exactly one correct answer for all Multiple Choice/Scenario-Based questions; unambiguous correct sets for both Multiple Select questions (SEC-012 "select two," SEC-016 "select two").
- [x] Every distractor is plausible and tied to a documented misconception (e.g., SEC-017's "more restriction is always better" distractor and SEC-016's "newer is always better" distractor are both pulled directly from this Knowledge Area's documented Exam Traps, per `authoring_guidelines.md`'s Distractor Design priority order).
- [x] All required `metadata_schema.md` fields populated and correctly typed across all 20 records.
- [x] No unjustified duplication (see above).
- [x] No fairness/accessibility violations — no vendor-specific tooling required; no idioms or trick wording found.

**Gate 1 result: Pass**, all 20 questions.

## Gate 2 — DAMA Review

- [x] Every correct answer verified against `knowledge_base/data_security.md`'s Approved content; no factual errors identified.
- [x] DAMA terminology used precisely throughout (Authentication, Authorization, Classification, Least Privilege, Segregation of Duties, and the five-technique cluster all used exactly as defined in the source module).
- [x] `references` fields resolve to a real, specific section of the source module for all 20 records.
- [x] `dama_concept` / `industry_practice_concept` classification checked against the source module's own tagging — CIA Triad, ABAC, DLP, and PCI-DSS scope reduction are correctly tagged `industry_practice_concept` rather than flattened to `[DAMA]`, mirroring the source module's own hedging; SEC-009 and SEC-013 correctly reference GDPR/HIPAA/PCI-DSS as real named regulations rather than DAMA-authored content.
- [x] `source_confidence` set accurately: `High` for core `[DAMA]`-tagged content (Authentication/Authorization, Classification, the five-technique cluster, Least Privilege/SoD, Key Management); `Medium` for `[Industry Practice]`-hedged content (ABAC framing, anonymization/pseudonymization GDPR-specific nuance, PCI-DSS scope reasoning).
- [x] No verbatim DMBOK2 reproduction — all stems and scenarios are original compositions.
- [x] Where a question targets a documented Exam Trap or Common Mistake (SEC-006 targets the Auth/Auth conflation trap; SEC-009 targets the anonymization/pseudonymization conflation trap; SEC-017 targets the over-restriction trap; SEC-018 targets the "encryption alone is sufficient" trap; SEC-015 targets Common Mistake 6), the trap is represented accurately, not as a strawman.
- [x] `taxonomy.md` classification checked against the SEC Topic/Subtopic breakdown added to `question_bank/taxonomy.md` alongside this module's Approval — all 20 records use a valid Topic from that breakdown.
- [x] `difficulty` and `blooms_level` consistent with actual cognitive demand: Beginner (SEC-001–005) is single-fact recall; Intermediate (SEC-006–015) requires classification or scenario-based application of one concept; Advanced (SEC-016–020) requires multi-factor evaluative or analytical reasoning (access-model tradeoff evaluation, over-restriction failure analysis, key-management design analysis, compliance-scope reasoning, metadata-propagation root-cause analysis) — correctly calibrated above the Intermediate tier.

**Gate 2 result: Pass**, all 20 questions.

## Gate 3 — Approval

- [x] Both Gate 1 and Gate 2 passed and recorded (`reviewer` field updated on each record).
- [x] `question_id` assigned and unique: SEC-001 through SEC-020, no gaps, no collisions with other Knowledge Areas' ID space.
- [x] `version` set to `1.0` on all 20 records.
- [x] `creation_date` and `last_modified` populated on all 20 records.
- [x] Every `metadata_schema.md` required field present with no placeholder values remaining.
- [x] No prior version exists for any of these IDs, so no `supersedes` link applies.

**Gate 3 result: Pass**, all 20 questions. `review_status` updated to `Published` and `approval_status` updated to `Approved` on all 20 records as part of this review.

## Metadata Validation Detail

- **ID/sequence integrity:** SEC-001–020, sequential, zero-padded, no gaps.
- **Cross-reference integrity:** All `references` entries point to `knowledge_base/data_security.md` with a specific section name, and resolve to real content in the Approved module (spot-checked against the live file).
- **Related exercises:** SEC-006, SEC-007, SEC-010 correctly link to Exercise 1; SEC-008, SEC-009 correctly link to Exercise 2; SEC-011 correctly links to Exercise 3 — all three of the module's Section 11 exercises are represented.
- **Type-specific answer structure:** Both Multiple Select records (SEC-012, SEC-016) use the array `correct_answer` shape specified in `metadata_schema.md`; all other records use the single-label shape.

## Summary

The Data Security set is accurate, correctly distributed, confirmed non-duplicative against the source module's own quiz, and gives strong targeted coverage to the module's highest-value distinctions (Authentication vs. Authorization; the five-technique protection cluster; the governance boundary for classification and access decisions) as well as the Key Management and DLP content added during the module's own improvement pass. No disqualifying issues were found at any of the three gates.

**Outcome: All 20 questions published.** `review_status: Published`, `approval_status: Approved`, `reviewer: ["Claude (CDMP Mentor) — Technical Review", "Claude (CDMP Mentor) — DAMA Review", "Claude (CDMP Mentor) — Approval Authority"]` set on every `SEC-001.yaml` through `SEC-020.yaml` record, with `last_modified` updated to the review date.
