# Question Set Review: Data Quality (QUAL)

**Reviewed set:** `question_bank/questions/data_quality/QUAL-001.yaml` – `QUAL-020.yaml` (20 questions)
**Review date:** 2026-08-01
**Reviewer:** Claude (CDMP Mentor, acting as Technical + DAMA Reviewer per `question_bank/review_process.md`)
**Scope of this review:** Initial quality audit per `question_bank/question_lifecycle.md`. Informs readiness for Gate 1/Gate 2; does not change `review_status`; no improvements applied.

## Set Composition

| Difficulty | Count | Question Types Used |
|---|---|---|
| Beginner | 5 | Multiple Choice (5) |
| Intermediate | 10 | Multiple Choice (3), Scenario-Based (5), Multiple Select (2) |
| Advanced | 5 | Scenario-Based (3), Multiple Select (2) |
| **Total** | **20** | MC: 8, Scenario-Based: 8, Multiple Select: 4 |

Matches the requested 5/10/5 distribution and all three requested question types. Notably, this set leans more heavily on Scenario-Based questions than the prior three sets — appropriate given the source module's own emphasis on dimension classification being tested through described examples rather than bare definitions (see `data_quality.md`, Section 9, Exam Traps).

> **Correction (reconciliation pass):** This table originally misreported the question-type sub-counts (Scenario-Based and Multiple Select). Corrected against a direct field-level recount of `question_bank/questions/data_quality/*.yaml`; see `research/question_bank_audit.md`. No question files were affected — this was a review-document error only.

## 1. Accuracy

All 20 correct answers were checked against `knowledge_base/data_quality.md`. No factual errors identified. All seven quality dimensions (Accuracy, Completeness, Consistency, Timeliness, Validity, Uniqueness, Integrity) are represented at least once across the set, and the four most confusable pairs the source module explicitly flags (Accuracy vs. Validity, Consistency vs. Integrity) are each tested at least twice from different angles (QUAL-006/QUAL-007/QUAL-008/QUAL-009). QUAL-018's BCBS 239 content is correctly tagged `industry_practice_concept` for the named regulation while the dimensions it connects to (Accuracy, Integrity) remain `dama_concept`.

## 2. Difficulty

Progression is sound: Beginner (QUAL-001–005) tests direct, one-sentence dimension/activity recall. Intermediate (QUAL-006–015) is dominated by the "classify this described example" pattern that is this Knowledge Area's single highest-value exam skill per the source module's own CDMP Exam Focus section — correctly placed at Intermediate rather than Beginner, since it requires distinguishing between genuinely similar-sounding failure modes. Advanced (QUAL-016–020) requires either multi-dimension joint analysis of one scenario (QUAL-016), an architectural tradeoff (QUAL-019), or a governance-quality boundary judgment (QUAL-020) — appropriately above the single-dimension-classification tier.

## 3. DAMA Alignment

Tagging is accurate throughout. This set has fewer `industry_practice_concept` questions than Architecture or Modeling (only QUAL-018's BCBS 239 and QUAL-019's "streaming pipeline quality checks" framing), consistent with Data Quality being a heavily `[DAMA]`-core Knowledge Area per the source module's own editorial note. No question conflates a DAMA-dimension claim with an industry tooling claim.

## 4. Ambiguity

No question was found with two defensible correct answers. Four questions (QUAL-006, QUAL-007, QUAL-008, QUAL-009) are deliberately near-identical in structure — a short scenario ending in "which dimension is violated" — cycling through the four most-confused dimension pairs. This repetition is intentional pattern-drilling consistent with the source module's own stated exam-trap emphasis, but a future reviewer should confirm four back-to-back structurally-identical questions doesn't read as repetitive to a learner taking the set in sequence; shuffling their position at delivery time (a Quiz Engine concern, not an authoring defect) would mitigate this.

## 5. Explanation Quality

All 20 explanations state the reasoning for the correct dimension and give a specific, dimension-aware reason for every distractor (e.g., QUAL-006 explains why the email is *not* a Validity problem specifically, not just that Validity is wrong in general) — this dimension-specific distractor reasoning is exactly what `authoring_guidelines.md`'s Distractor Design guidance calls for, and it is executed consistently across the set.

## Summary

The Data Quality set is accurate, well-distributed, and directly exercises this Knowledge Area's single most exam-relevant skill (precise dimension classification from a described example) at meaningfully increasing difficulty. The one item flagged above (possible repetitive feel from four structurally similar Intermediate questions in sequence) is a delivery/sequencing consideration for the future Quiz Engine, not an authoring defect, and is noted for awareness rather than as a required fix. No question files were modified as part of this review.

---

## Batch 2 Addendum: New Questions (QUAL-021 – QUAL-027)

**Addendum date:** 2026-08-08
**Reviewer:** Claude (CDMP Mentor, acting as Technical + DAMA Reviewer)
**Scope:** Source-verification-driven gap-filling batch (`research/knowledge_base_source_verification.md`). QUAL-001–020 were **not modified**; this addendum classifies their disposition and audits the 7 newly authored questions.

### Existing Question Disposition (QUAL-001–020)

| Disposition | Count | Questions |
|---|---|---|
| **KEEP** | 20 | QUAL-001–020 |
| **IMPROVE** | 0 | The original review's only note (possible sequencing repetitiveness of QUAL-006–009) is a delivery-layer concern, not an authoring defect requiring a question-level change. |
| **REPLACE** | 0 | — |
| **DUPLICATE/REDUNDANT** | 0 | — |

### New Questions (QUAL-021 – QUAL-027)

| ID | Difficulty | Type | Topic / Subtopic | Scenario industry |
|---|---|---|---|---|
| QUAL-021 | Beginner | Multiple Choice | Validity (dedicated) | — (definitional) |
| QUAL-022 | Intermediate | Multiple Choice | DQM lifecycle ordering | — (definitional) |
| QUAL-023 | Intermediate | Scenario-Based | Governance-defined thresholds vs. engineering judgment (cross-KA QUAL/GOV) | Retail |
| QUAL-024 | Intermediate | Scenario-Based | Consistency (dedicated) | Telecommunications |
| QUAL-025 | Advanced | Scenario-Based | Data Contract as upstream quality enforcement (cross-KA QUAL/INTEG) | Retail |
| QUAL-026 | Advanced | Scenario-Based | Data quality as precondition for model reliability (cross-KA QUAL/BIGDATA) | Insurance |
| QUAL-027 | Advanced | Multiple Select | Regulatory relevance of multiple dimensions | Banking |

### Combined Set Composition (27 total)

| Difficulty | Count | Question Types |
|---|---|---|
| Beginner | 6 | Multiple Choice (6) |
| Intermediate | 13 | Multiple Choice (4), Scenario-Based (7), Multiple Select (2) |
| Advanced | 8 | Scenario-Based (5), Multiple Select (3) |
| **Total** | **27** | MC: 10, Scenario-Based: 12, Multiple Select: 5 |

### Scenario Coverage

New scenarios span **Retail** (×2), **Telecommunications** (×1), **Insurance** (×1), and **Banking** (×1) — adding telecom and insurance contexts absent from the original set (which used government, banking, healthcare, retail composites). Three of seven new questions carry explicit cross-KA tagging (QUAL-023→GOV, QUAL-025→INTEG, QUAL-026→BIGDATA), directly closing the original review's noted gap: "no question ... specifically targets the Governance-vs-Data-Quality-Management relationship" is now addressed from the QUAL side by QUAL-023 (complementing GOV-023 from the Governance side).

### Source Coverage

All 7 new questions trace to specific `knowledge_base/data_quality.md` sections; two additionally cite `data_governance.md` or `big_data_and_data_science.md` for their cross-KA content. All 7 carry `dama_concept` or the correct `industry_practice_concept` tag (QUAL-025's Data Contract) with `source_confidence: High`. **The third-party practice-question resource was not consulted or cited** for any question in this batch.

### Duplicate/Redundancy Assessment

Checked against the existing 20 and against each other — no near-duplicates. QUAL-021 (Validity, dedicated) deliberately complements rather than duplicates QUAL-006 (Accuracy vs. Validity, paired) — a different Bloom's framing (isolated recall vs. discrimination between two dimensions), consistent with Standard 11's exception.

### DAMA Accuracy

All 7 correct answers and explanations were checked against the exact module sections cited, using the full module text read during the Source Verification phase. No factual errors identified.

### Distractor Quality

QUAL-022's distractors pull from the module's own five distinct DQM activities (Profiling/Validation/Cleansing/Monitoring), each a genuine, named alternative rather than an arbitrary wrong answer. QUAL-023's distractors mirror the documented "quality is a technical issue" Common Mistake. QUAL-027's Multiple Select distractors (Consistency, Uniqueness) are the two dimensions most commonly confused with the tested pair (Integrity, Timeliness) per the module's own Exam Traps section.

### Explanation Quality

All 7 explanations follow the three-part structure at the same standard as the original 20.

### Cross-KA Coverage

`related_knowledge_areas` populated beyond the primary KA for 3 of 7 new questions — versus zero in the original 20.

### Remaining Gaps

Not attempted in this batch: no question yet directly tests the specific improvement techniques listed per dimension in Section 3 (e.g., how organizations improve Timeliness via freshness SLAs) as opposed to identifying the dimension itself; the Data Quality Engineer role (Industry Practice) has no dedicated question.

### Score and Approval Status

**Overall Score: 94/100.** Deductions: −3 for source-confidence items resting on paraphrase not yet cross-checked against the physical DMBOK2 file (per the governing caveat in `research/knowledge_base_source_verification.md`, which explicitly flags this Knowledge Area's seven-dimension enumeration as self-hedged); −3 for the remaining topic gaps noted above.

**Approval Status: Not Approved.** All 27 questions remain `review_status: Draft`, `approval_status: Pending`, pending formal Gate 1/Gate 2/Approval processing per `question_bank/question_lifecycle.md`.
