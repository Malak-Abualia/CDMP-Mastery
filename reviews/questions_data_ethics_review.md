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

---

## Addendum: ETH-021–024 (New Questions, 2026-08-08)

**Reviewed set:** `ETH-021.yaml` – `ETH-024.yaml` (4 new questions), evaluated alongside the full 24-question bank.
**Trigger:** Gap-first production pass for ETH, part of a combined ETH + DOC batch following `roadmap/remaining_eight_question_production_plan.md`-style planning. Planned maximum was "+6, not a mandatory quota" — 4 questions were judged genuinely justified after a Phase A gap analysis; two candidate ideas (ETH↔BIGDATA bias/fairness cross-KA, and a second SEC-boundary question) were deliberately **not** produced (see Gap Analysis below).
**Status of this addendum:** This is a Gate 1 + Gate 2 pass only. **Gate 3 (Approval/Publish) is explicitly withheld** per task instruction — `review_status: Draft`, `approval_status: Pending` remain set on all four new records pending the user's explicit approval of this KA.

### Gap Analysis (what was produced, and what wasn't)

| Gap | Action | Reasoning |
|---|---|---|
| Direct Harm never tested as a correct answer (only ever a distractor in ETH-007) | **Produced — ETH-021** | Real, checked gap: Dignitary and Societal/Aggregate harm are each the correct answer somewhere in the set; Direct Harm is not. |
| Data Ethicist / Ethics Officer role (Section 4 role table) never tested | **Produced — ETH-022** | Every other named role in the module's role table has bank coverage; this one didn't. |
| Governance Council's ethical-review escalation authority (Section 4 cross-reference to `data_governance.md`) | **Produced — ETH-023** | Checked all 6 GOV questions referencing "Governance Council" (GOV-003/005/011/016/020/026): none test its extended ethics-escalation function, only definitional disputes, BCBS 239, and composition. |
| Division of labor between SEC's anonymization/pseudonymization technique choice and ETH's re-identification risk-acceptance for release | **Produced — ETH-024** | ETH-008 (single-KA) tests "de-identification ≠ zero risk"; SEC-009 (single-KA) tests GDPR pseudonymization classification. Neither tests the responsibility boundary between choosing a compliant technique and accepting release risk. |
| ETH↔BIGDATA model bias/fairness cross-KA tagging | **Not produced** | BIGDATA-016 and ETH-007/ETH-010/ETH-015 already cover aggregate-accuracy-vs-subgroup-fairness reasoning thoroughly from both sides; a cross-tagged version would be filler, not a gap-closer. Judgment call, logged here per the task's "do not assume every listed gap requires a question" instruction. |
| A second ETH↔SEC question on the "authorized-but-inappropriate-use" boundary | **Not produced** | ETH-013 (single-KA) already tests this exact boundary (fully authorized, policy-compliant access that is still ethically inappropriate) in depth; a SEC-side restatement would not add a distinct cognitive task. |

### Non-Duplication Check

**Against the existing 20:** Each new question was checked for stem intent, cognitive task, scenario structure, answer pattern, and subtopic overlap — not keyword matching alone (per the QUAL-022 standing caution).

- **ETH-021** (Direct Harm as the correct classification) vs. ETH-007 (Societal/Aggregate harm as the correct classification, Direct Harm only a distractor): distinct correct-answer target and distinct scenario (individualized dynamic pricing vs. population-level scoring system); no overlap.
- **ETH-022** (Data Ethicist / Ethics Officer role recall) vs. no existing question: confirmed via whole-bank grep for "Data Ethicist" / "Ethics Officer" — ETH-022 is the only match in the entire question bank.
- **ETH-023** (Governance Council ethics-escalation authority) vs. all 6 GOV questions mentioning "Governance Council" and vs. ETH-006/ETH-013 (single-KA ethics-vs-compliance/security questions): distinct cognitive task — identifying the correct escalation body for a contested ethical question, not classifying a compliance fallacy or a security/ethics boundary.
- **ETH-024** (SEC technique selection vs. ETH risk-acceptance for release) vs. ETH-008 (single-KA re-identification-via-aggregation scenario) and SEC-009 (single-KA GDPR pseudonymization classification): distinct decision-allocation task — neither existing question tests that a compliant technique choice does not itself resolve the release-justification question.

**Result: No duplication found**, against the existing 20 ETH questions, the 6 relevant GOV questions, or the relevant SEC questions (SEC-005/008/009/012 covering anonymization/pseudonymization).

### Gate 1 — Technical Review

- [x] Every stem clear, complete, single interpretation.
- [x] No negative-phrasing or "all/none of the above" violations.
- [x] Options grammatically parallel and comparably sized (no correct-answer length-tell — the DWBI batch's most common defect was specifically checked for and avoided here: longer options exist only where the correct answer's *label itself* is inherently longer, e.g. ETH-023/ETH-024, and even there each distractor carries a comparable explanatory clause, not a bare short label).
- [x] Exactly one correct answer for all four (all Multiple Choice/Scenario-Based; no Multiple Select in this batch — not forced, since no candidate question naturally fit a "select N" structure).
- [x] Every distractor plausible and grounded: ETH-021's harm-category distractors are the module's own other two harm categories plus the compliance-sufficiency fallacy; ETH-022's role distractors are real, adjacent DAMA/DOC roles (Custodian, Records Manager) and a generic technical title (DBA); ETH-023's distractors are a technical role, the compliance-sufficiency fallacy, and a lack-of-independence failure mode; ETH-024's distractors are the compliance-sufficiency fallacy, a technique-substitution non-fix, and a contractual-safeguard non-fix.
- [x] All `metadata_schema.md` required fields populated and correctly typed on all 4 records (confirmed by direct read-back after write).
- [x] No unjustified duplication (see Non-Duplication Check above).
- [x] No fairness/accessibility violations.

**Gate 1 result: Pass**, all 4 new questions.

### Gate 2 — DAMA Review

- [x] Every correct answer verified against `knowledge_base/data_ethics.md`'s Approved content: Direct Harm's definition (Section 4, ETH-021), the Data Ethicist/Ethics Officer role (Section 4 role table, ETH-022), the Governance Council ethical-review extension (Section 4 Relationships, ETH-023), and the anonymization/pseudonymization re-identification risk framing (Section 4, ETH-024) all match the source module directly — no invented facts.
- [x] Cross-KA claims independently re-verified against the secondary module, not just recalled from ETH's own cross-reference: `data_governance.md, Section 3` confirms the Governance Council's escalation/dispute-resolution function and the Policy→Standard→Procedure hierarchy (ETH-023); `data_security.md, Section 4` confirms pseudonymization's reversible-by-design characteristic and `Section 8`'s Security-vs-Ethics boundary framing (ETH-024).
- [x] `dama_concept`/`industry_practice_concept` tagging checked against source-module tags: ETH-021 tagged `dama_concept` (harm categories are `[DAMA]`-tagged in the module); ETH-022 tagged `industry_practice_concept`-only (the module tags the Data Ethicist/Ethics Officer role `[Industry Practice, DAMA-referenced]`); ETH-023 tagged `dama_concept` (both underlying concepts — Governance Council and the ethics-review extension — are `[DAMA]`-framed); ETH-024 tagged `industry_practice_concept`-only, reflecting that the cross-KA division-of-labor framing is this reviewer's own synthesis across two `[DAMA]`/`[Industry Practice]`-mixed sources, not a single verbatim module statement.
- [x] `source_confidence`: ETH-021 and ETH-023 set `High` (core, directly-stated module content); ETH-022 and ETH-024 set `Medium` (`[Industry Practice]`-hedged role terminology, and a cross-module synthesis respectively) — consistent with `metadata_schema.md`'s Source Confidence definitions.
- [x] No verbatim DMBOK2 reproduction — all stems and scenarios are original compositions; no scenario paraphrases an existing Enterprise Example from either source module.
- [x] `taxonomy.md` Topic/Subtopic classification valid for all 4: Impact and Harm (ETH-021), Data Ethics in Practice (ETH-022, ETH-023, ETH-024) — all four use Topics already present in the ETH taxonomy breakdown; no taxonomy changes were required.
- [x] `difficulty`/`blooms_level` consistency: ETH-021 (Intermediate/Understand — classifying a described consequence against a defined framework) and ETH-022 (Beginner/Remember — single-fact role recall, no scenario) are calibrated below ETH-023 and ETH-024 (both Advanced/Analyze — ETH-023 requires identifying the correct escalation body across two Knowledge Areas' authority structures; ETH-024 requires allocating responsibility between two KAs' distinct decisions, not just recalling either one). No decorative-scenario risk: all four stems require the described cognitive task to reach the answer, not just a re-statement of a definition wrapped in a company name.
- [x] Cross-KA `related_knowledge_areas` correctly set: ETH-023 `["ETH", "GOV"]`, ETH-024 `["ETH", "SEC"]`, both ETH-primary (ETH listed first, matching precedent); ETH-021/ETH-022 correctly left single-KA (`["ETH"]`), no forced cross-referencing where none is warranted.

**Gate 2 result: Pass**, all 4 new questions.

### Gate 3 — Approval

**Explicitly withheld.** Per task instruction, the four new questions remain `review_status: Draft`, `approval_status: Pending`. No `reviewer` entries have been added to these records, and none should be until the user explicitly approves this KA for progression.

### Updated Set Composition (all 24 questions)

| Difficulty | Count | Question Types Used |
|---|---|---|
| Beginner | 6 | Multiple Choice (6) |
| Intermediate | 11 | Multiple Choice (4), Scenario-Based (6), Multiple Select (1) |
| Advanced | 7 | Scenario-Based (5), Multiple Select (2) |
| **Total** | **24** | MC: 10, Scenario-Based: 11, Multiple Select: 3 |

**Status mix:** 20 `Published`/`Approved` (ETH-001–020), 4 `Draft`/`Pending` (ETH-021–024).

**Cross-KA questions in the full ETH set:** ETH-023 (→GOV) and ETH-024 (→SEC) are the only two; both new, both ETH-primary, both independently re-verified against fresh reads of the secondary module rather than relying on ETH's own cross-reference text alone.

### Addendum Summary

The four new questions are factually accurate (independently re-verified against both the primary module and, for the two cross-KA questions, the secondary module), non-duplicative against the existing 20 ETH questions and all relevant GOV/SEC questions, correctly tagged for DAMA/Industry Practice provenance, and calibrated at a difficulty level matching their actual cognitive demand. Two candidate ideas (an ETH↔BIGDATA bias/fairness cross-tag, and a second ETH↔SEC boundary question) were deliberately not produced, on the judgment that existing coverage already closed those gaps. No disqualifying issues found at Gate 1 or Gate 2.

**Outcome: 4 questions pass Gate 1 and Gate 2. Gate 3 (Publish/Approve) is intentionally not executed.** `review_status: Draft`, `approval_status: Pending` remain on `ETH-021.yaml` through `ETH-024.yaml`, awaiting the user's explicit approval of this Knowledge Area before any status change or progression.
