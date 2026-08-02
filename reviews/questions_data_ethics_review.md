# Question Set Review: Data Ethics (ETH)

**Reviewed set:** `question_bank/questions/data_ethics/ETH-001.yaml` – `ETH-020.yaml` (20 questions)
**Review date:** 2026-08-02
**Reviewer:** Claude (CDMP Mentor, acting as Technical Reviewer + DAMA Reviewer + Approval Authority per `question_bank/review_process.md`'s single-author context)
**Scope of this review:** Full Gate 1 (Technical Review) → Gate 2 (DAMA Review) → Gate 3 (Approval) pass per `question_bank/question_lifecycle.md`, run against the source module `knowledge_base/data_ethics.md` (Approved, 91/100 — `reviews/data_ethics_review.md`).

## Set Composition

| Difficulty | Count | Question Types Used |
|---|---|---|
| Beginner | 5 | Multiple Choice (5) |
| Intermediate | 10 | Multiple Choice (4), Scenario-Based (5), Multiple Select (1) |
| Advanced | 5 | Scenario-Based (3), Multiple Select (2) |
| **Total** | **20** | MC: 9, Scenario-Based: 8, Multiple Select: 3 |

Matches the 5/10/5 difficulty distribution established as precedent, consistent with the type-mix pattern used across recent question sets.

## Non-Duplication Check

Per `question_quality_standards.md`, Standard 11, this set was checked against `knowledge_base/data_ethics.md`'s own 12 in-module Quiz Questions (Section 13). No direct duplication found — all 20 bank questions use original scenarios and wording. ETH-006 and the module's own Q1 both test the ethics-vs-compliance distinction but use distinct scenarios (a data-sharing partnership vs. a general framing question). ETH-019 and ETH-020 specifically target the EU AI Act and Success Metrics content added during the source module's own improvement pass, which the module's original 10-question quiz predated (Q11 and Q12 were the module's own only post-improvement quiz additions).

## Gate 1 — Technical Review

- [x] Every stem is clear, complete, with exactly one interpretation.
- [x] No negative-phrasing, double-negative, or "all/none of the above" violations found.
- [x] Options are grammatically parallel and similarly sized across all 20 questions.
- [x] Exactly one correct answer for all Multiple Choice/Scenario-Based questions; unambiguous correct sets for all three Multiple Select questions (ETH-011 "select three," ETH-017 and ETH-020 "select two").
- [x] Every distractor is plausible and tied to a documented misconception (e.g., ETH-016's "full compliance means no further evaluation" distractor and ETH-019's "no specific law means no obligation" distractor are pulled directly from this Knowledge Area's documented Exam Traps and Common Mistakes, per `authoring_guidelines.md`'s Distractor Design priority order).
- [x] All required `metadata_schema.md` fields populated and correctly typed across all 20 records.
- [x] No unjustified duplication (see above).
- [x] No fairness/accessibility violations — no vendor-specific tooling required; no idioms or trick wording found; scenarios involving sensitive topics (bias, discrimination) are handled with appropriately neutral, non-inflammatory framing consistent with the source module's own composite, non-attributed scenario approach.

**Gate 1 result: Pass**, all 20 questions.

## Gate 2 — DAMA Review

- [x] Every correct answer verified against `knowledge_base/data_ethics.md`'s Approved content; no factual errors identified.
- [x] DAMA terminology used precisely throughout (Data Ethics, Informed Consent, Ethics vs. Legal Compliance all used exactly as defined in the source module).
- [x] `references` fields resolve to a real, specific section of the source module for all 20 records.
- [x] `dama_concept` / `industry_practice_concept` classification checked against the source module's own tagging — the Belmont Report, EU AI Act, Data Minimization, and Proxy Discrimination are correctly left untagged or tagged `industry_practice_concept` as appropriate, mirroring the source module's own careful, explicitly hedged tagging given its self-flagged moderate-confidence enumeration.
- [x] `source_confidence` set accurately: `High` for core, well-attested content (ethics-vs-compliance, harm categories, transparency, consent, re-identification, proxy discrimination, fairness); `Medium` for content resting on the module's own explicitly hedged enumeration or newer external grounding (Belmont Report specifics, EU AI Act).
- [x] No verbatim DMBOK2 reproduction — all stems and scenarios are original compositions, and no question references a specific real company by name, consistent with the source module's own generalized, non-attributed incident framing.
- [x] Where a question targets a documented Exam Trap or Common Mistake (ETH-006 targets Common Mistake 1; ETH-008 targets the anonymization-as-guarantee trap; ETH-010/ETH-015 target the aggregate-accuracy/proxy-discrimination traps; ETH-013 targets the Security/Ethics conflation trap; ETH-019 targets the jurisdictional-gap fallacy), the trap is represented accurately, not as a strawman.
- [x] `taxonomy.md` classification checked against the ETH Topic/Subtopic breakdown added to `question_bank/taxonomy.md` alongside this module's Approval — all 20 records use a valid Topic from that breakdown.
- [x] `difficulty` and `blooms_level` consistent with actual cognitive demand: Beginner (ETH-001–005) is single-fact recall; Intermediate (ETH-006–015) requires classification or scenario-based application of one concept; Advanced (ETH-016–020) requires multi-factor evaluative or analytical reasoning (multi-principle simultaneous evaluation, legitimate-vs-insufficient consent design evaluation, quality-to-harm compounding analysis, jurisdictional-gap fallacy analysis, success-metric selection) — correctly calibrated above the Intermediate tier.

**Gate 2 result: Pass**, all 20 questions.

## Gate 3 — Approval

- [x] Both Gate 1 and Gate 2 passed and recorded (`reviewer` field updated on each record).
- [x] `question_id` assigned and unique: ETH-001 through ETH-020, no gaps, no collisions with other Knowledge Areas' ID space.
- [x] `version` set to `1.0` on all 20 records.
- [x] `creation_date` and `last_modified` populated on all 20 records.
- [x] Every `metadata_schema.md` required field present with no placeholder values remaining.
- [x] No prior version exists for any of these IDs, so no `supersedes` link applies.

**Gate 3 result: Pass**, all 20 questions. `review_status` updated to `Published` and `approval_status` updated to `Approved` on all 20 records as part of this review.

## Metadata Validation Detail

- **ID/sequence integrity:** ETH-001–020, sequential, zero-padded, no gaps.
- **Cross-reference integrity:** All `references` entries point to `knowledge_base/data_ethics.md` with a specific section name, and resolve to real content in the Approved module (spot-checked against the live file).
- **Related exercises:** ETH-003, ETH-009, ETH-012, ETH-016 correctly link to Exercise 1; ETH-008 correctly links to Exercise 2; ETH-010 correctly links to Exercise 3 — all three of the module's Section 11 exercises are represented.
- **Type-specific answer structure:** All three Multiple Select records (ETH-011, ETH-017, ETH-020) use the array `correct_answer` shape specified in `metadata_schema.md`; all other records use the single-label shape.

## Summary

The Data Ethics set is accurate, correctly distributed, confirmed non-duplicative against the source module's own quiz, and gives strong targeted coverage to the module's central theme (legal compliance is a floor, not a ceiling), the harm/fairness/consent/re-identification principle cluster, and the EU AI Act and Success Metrics content added during the module's own improvement pass. No disqualifying issues were found at any of the three gates.

**Outcome: All 20 questions published.** `review_status: Published`, `approval_status: Approved`, `reviewer: ["Claude (CDMP Mentor) — Technical Review", "Claude (CDMP Mentor) — DAMA Review", "Claude (CDMP Mentor) — Approval Authority"]` set on every `ETH-001.yaml` through `ETH-020.yaml` record, with `last_modified` updated to the review date.
