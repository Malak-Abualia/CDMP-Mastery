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
