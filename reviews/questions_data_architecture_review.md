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
