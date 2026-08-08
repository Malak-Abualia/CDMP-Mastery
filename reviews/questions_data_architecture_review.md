# Question Set Review: Data Architecture (ARCH)

**Reviewed set:** `question_bank/questions/data_architecture/ARCH-001.yaml` – `ARCH-020.yaml` (20 questions)
**Review date:** 2026-08-01
**Reviewer:** Claude (CDMP Mentor, acting as Technical + DAMA Reviewer per `question_bank/review_process.md`)
**Scope of this review:** Initial quality audit per `question_bank/question_lifecycle.md`. Informs readiness for Gate 1/Gate 2; does not change `review_status`; no improvements applied.

## Set Composition

| Difficulty | Count | Question Types Used |
|---|---|---|
| Beginner | 5 | Multiple Choice (5) |
| Intermediate | 10 | Multiple Choice (4), Scenario-Based (4), Multiple Select (2) |
| Advanced | 5 | Scenario-Based (3), Multiple Select (2) |
| **Total** | **20** | MC: 9, Scenario-Based: 7, Multiple Select: 4 |

Matches the requested 5/10/5 distribution and all three requested question types.

> **Correction (reconciliation pass):** This table originally misreported the question-type sub-counts (MC and Multiple Select). Corrected against a direct field-level recount of `question_bank/questions/data_architecture/*.yaml`; see `research/question_bank_audit.md`. No question files were affected — this was a review-document error only.

## 1. Accuracy

All 20 correct answers were checked against `knowledge_base/data_architecture.md`. No factual errors identified. This Knowledge Area's content is unusually dependent on external, non-DAMA frameworks (Zachman, TOGAF, PSD2/Open Banking, HL7 FHIR) — every question referencing one of these (ARCH-005, ARCH-008, ARCH-013, ARCH-016, ARCH-019) correctly tags it `industry_practice_concept` rather than `dama_concept`, and none misattributes an external framework's origin to DAMA. ARCH-008 and ARCH-013 are marked `source_confidence: Medium` since TOGAF's domain framing is presented in the source module as "general EA pattern" rather than DMBOK2's own enumerated content — an appropriately conservative confidence rating.

## 2. Difficulty

Progression holds up: Beginner (ARCH-001–005) tests single-definition recall (scope of Data Architecture, Data Domain, Data Flow, Data Lifecycle, TOGAF's non-DAMA origin). Intermediate (ARCH-006–015) consistently requires classification against the Architecture-vs-Modeling-vs-Database-Design boundary or a layer-assignment judgment — appropriately above pure recall, and this Knowledge Area's own "most commonly confused" pairing gets proportionally heavy Intermediate coverage (ARCH-006, ARCH-009, ARCH-011), matching the source module's own emphasis. Advanced (ARCH-016–020) all require evaluating a real, multi-factor scenario (a regulation's architectural implication, a post-merger domain conflict, a sequencing decision, a standard spanning two Knowledge Areas, a migration trigger) rather than a single classification call — correctly calibrated to the Evaluate/Analyze tier.

## 3. DAMA Alignment

This set has the highest proportion of `industry_practice_concept` tagging of the sets reviewed so far (5 of 20 questions), which is accurate to the source module rather than a defect — `data_architecture.md` itself is explicit that Zachman, TOGAF, data mesh, and lakehouse architecture are external concepts DAMA references as compatible, not DAMA inventions. Every question tests this provenance distinction correctly rather than blurring it, including ARCH-005 and ARCH-011, which test the provenance distinction as the primary learning objective rather than incidentally.

## 4. Ambiguity

No question was found with two defensible correct answers. ARCH-006, ARCH-009, and ARCH-011 all probe closely related "X vs. Y discipline boundary" territory (Architecture vs. Modeling; Architecture vs. Database Design; Architecture vs. informal "Data Engineering Architecture") — deliberate reinforcement of the source module's stated position that this is "the single most commonly tested distinction in this Knowledge Area," not redundant overlap. ARCH-013's five-option Multiple Select (four correct TOGAF domains plus one plausible-sounding distractor) was checked for the standard Multiple-Select ambiguity risk (an unstated expected count) — the stem explicitly asks for "which four," mitigating this.

## 5. Explanation Quality

All 20 questions provide full reasoning for the correct answer and a specific, non-generic reason for every incorrect option, satisfying `question_quality_standards.md`, Standards 6–7. A notable strength: several Advanced explanations (ARCH-016, ARCH-018, ARCH-020) explicitly connect the scenario back to a named principle from the source module's Practical Exercise or Enterprise Example sections (e.g., "don't pick technology first and rationalize it after"), giving the explanation a citable, traceable teaching point rather than a generic restatement.

## Summary

The Data Architecture set is accurate, well-distributed, and does an above-average job of testing this Knowledge Area's defining challenge — correctly scoping Architecture against its most commonly confused neighbors (Modeling, Database Design, informal industry terminology) — at every difficulty tier, not just Intermediate. No disqualifying issues were found. No question files were modified as part of this review.

---

## Batch 2 Addendum: New Questions (ARCH-021 – ARCH-026)

**Addendum date:** 2026-08-08
**Reviewer:** Claude (CDMP Mentor, acting as Technical + DAMA Reviewer)
**Scope:** Source-verification-driven gap-filling batch (`research/knowledge_base_source_verification.md`). ARCH-001–020 were **not modified**; this addendum classifies their disposition and audits the 6 newly authored questions.

### Existing Question Disposition (ARCH-001–020)

| Disposition | Count | Questions |
|---|---|---|
| **KEEP** | 20 | ARCH-001–020 |
| **IMPROVE** | 0 | The original review found no disqualifying or flagged issues. |
| **REPLACE** | 0 | — |
| **DUPLICATE/REDUNDANT** | 0 | — |

### New Questions (ARCH-021 – ARCH-026)

| ID | Difficulty | Type | Topic / Subtopic | Scenario industry |
|---|---|---|---|---|
| ARCH-021 | Beginner | Multiple Choice | Zachman Framework (sourcing attribution) | — (definitional) |
| ARCH-022 | Intermediate | Multiple Choice | Logical Data Architecture (dedicated) | — (definitional) |
| ARCH-023 | Intermediate | Scenario-Based | Architecture Standards vs. Governance Standards (cross-KA ARCH/GOV) | — (dual-scenario) |
| ARCH-024 | Beginner | Multiple Choice | Data Mesh (sourcing attribution) | — (definitional) |
| ARCH-025 | Advanced | Scenario-Based | Integration pattern as architecture decision (cross-KA ARCH/INTEG) | Telecommunications |
| ARCH-026 | Advanced | Scenario-Based | Conceptual/Logical/Physical sequencing for a multi-agency platform | Government / public sector |

### Combined Set Composition (26 total)

| Difficulty | Count | Question Types |
|---|---|---|
| Beginner | 7 | Multiple Choice (7) |
| Intermediate | 12 | Multiple Choice (6), Scenario-Based (5), Multiple Select (2) |
| Advanced | 7 | Scenario-Based (5), Multiple Select (2) |
| **Total** | **26** | MC: 13, Scenario-Based: 10, Multiple Select: 4 |

### Scenario Coverage

New scenarios span **Telecommunications** (×1) and **Government/Public Sector** (×1) — both previously untested industries in this set (the original 20 used government implicitly once but leaned mainly on banking, healthcare, retail). Two of six new questions carry explicit cross-KA tagging.

### Source Coverage

All 6 new questions trace to specific `knowledge_base/data_architecture.md` sections. ARCH-022 is correctly `source_confidence: Medium`, matching the module's own hedge that the Architecture-layer three-level pattern's exact DMBOK2 wording needs verification. ARCH-021 and ARCH-024 correctly use `industry_practice_concept` (Zachman; Data Mesh) rather than `dama_concept`. **The third-party practice-question resource was not consulted or cited** for any question in this batch.

### Duplicate/Redundancy Assessment

Checked against the existing 20 (which already tests TOGAF three times — ARCH-005, ARCH-008, ARCH-013) and against each other — no near-duplicates. ARCH-021's Zachman question deliberately fills a gap the existing set left (TOGAF was tested repeatedly; Zachman, named in the same module section, had zero dedicated questions).

### DAMA Accuracy

All 6 correct answers and explanations were checked against the exact module sections cited, using the full module text read during the Source Verification phase. No factual errors identified.

### Distractor Quality

ARCH-021 and ARCH-024's distractors are both instances of the same documented exam trap pattern (crediting DAMA with an externally-originated framework) applied to two different frameworks — reinforcing the pattern without repeating the same specific wrong answer. ARCH-025's distractors represent plausible engineering rationalizations (autonomy, one-size-fits-all correctness) rather than arbitrary wrong answers.

### Explanation Quality

All 6 explanations follow the three-part structure at the same standard as the original 20.

### Cross-KA Coverage

`related_knowledge_areas` populated beyond the primary KA for 2 of 6 new questions (ARCH-023→GOV; ARCH-025→INTEG; ARCH-026→GOV,MASTER) — versus zero cross-KA tagging in the original 20.

### Remaining Gaps

Not attempted in this batch: no question yet tests the Data Architecture Component deliverables list (enterprise data model, flow diagrams, technology inventory, roadmap) as a set; Lakehouse architecture (mentioned alongside Data Mesh) has no dedicated question of its own.

### Score and Approval Status

**Overall Score: 93/100.** Deductions: −3 for ARCH-022's Medium-confidence sourcing not yet cross-checked against the physical DMBOK2 file; −2 for a slightly heavier Beginner tier (7 of 26, above this set's original 5-per-tier baseline) without a matched Advanced addition beyond the two included; −2 for the remaining topic gaps noted above.

**Approval Status: Not Approved.** All 26 questions remain `review_status: Draft`, `approval_status: Pending`, pending formal Gate 1/Gate 2/Approval processing per `question_bank/question_lifecycle.md`.
