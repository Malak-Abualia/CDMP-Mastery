# Question Set Review: Metadata Management (META)

**Reviewed set:** `question_bank/questions/metadata_management/META-001.yaml` – `META-020.yaml` (20 questions)
**Review date:** 2026-08-01
**Reviewer:** Claude (CDMP Mentor, acting as Technical + DAMA Reviewer per `question_bank/review_process.md`)
**Scope of this review:** Initial quality audit per `question_bank/question_lifecycle.md`. Informs readiness for Gate 1/Gate 2; does not change `review_status`; no improvements applied.

## Set Composition

| Difficulty | Count | Question Types Used |
|---|---|---|
| Beginner | 5 | Multiple Choice (5) |
| Intermediate | 10 | Multiple Choice (4), Scenario-Based (4), Multiple Select (2) |
| Advanced | 5 | Multiple Choice (1), Scenario-Based (3), Multiple Select (1) |
| **Total** | **20** | MC: 10, Scenario-Based: 7, Multiple Select: 3 |

Matches the requested 5/10/5 distribution and all three requested question types.

> **Correction (reconciliation pass):** This table originally misreported the question-type sub-counts (MC and Scenario-Based were transposed). Corrected against a direct field-level recount of `question_bank/questions/metadata_management/*.yaml`; see `research/question_bank_audit.md`. No question files were affected — this was a review-document error only.

## 1. Accuracy

All 20 correct answers were checked against `knowledge_base/metadata_management.md`. No factual errors identified. The three-category classification (Business/Technical/Operational) — the source module's own highest-value skill — is tested from multiple angles (direct recall in META-001–003; applied classification in META-006–008, META-015), and the "classify by meaning, not storage location" trap is tested twice (META-008, META-015) without redundant phrasing, reinforcing the same principle with two different concrete examples rather than repeating one.

## 2. Difficulty

Progression is sound: Beginner (META-001–005) tests direct category/artifact recall. Intermediate (META-006–015) consistently requires classification of a described, sometimes deliberately tricky example (an ownership field stored in a technical table; a column comment) — correctly above pure recall. Advanced (META-016–020) each require evaluating a real operational or architectural consequence (undocumented downstream breakage, enterprise strategy scoping, a regulatory audit requirement, a storage-layer architectural shift, an instrumentation misconception) rather than a single classification call.

## 3. DAMA Alignment

Tagging is accurate and appropriately mixed: META-012 (data swamp), META-019 (lakehouse-embedded metadata) are correctly tagged `industry_practice_concept` per the source module's own explicit framing of these as industry vocabulary, not DMBOK2-defined terms. META-018's HIPAA content is correctly tagged as a named regulation (`industry_practice_concept`) while the underlying metadata category (Operational) remains `dama_concept`. No question conflates industry tooling/terminology with DAMA-official definitions.

## 4. Ambiguity

No question was found with two defensible correct answers. META-008 and META-015 both test the "classify by meaning, not storage location" principle — reviewed for redundancy and found to use sufficiently distinct scenarios (an ownership field vs. a column comment) that they reinforce rather than duplicate. One item for a future DAMA reviewer to double-check: META-011's phrasing ("data flow diagrams are always more detailed than lineage" as a distractor) inverts the source module's actual claim rather than stating an unrelated falsehood — this is a stronger, more discriminating distractor design, but worth confirming it isn't so close to the correct answer's negation that it reads as a wording trick rather than a knowledge test.

## 5. Explanation Quality

All 20 explanations state the reasoning for the correct classification/answer and a specific reason for every distractor, satisfying `question_quality_standards.md`, Standards 6–7. A notable strength: this set's explanations frequently name the *specific* exam trap being tested (e.g., META-008 and META-010 both explicitly reference "the exam trap" they represent), which is good for a learner reviewing wrong answers but should be checked during formal DAMA Review to confirm it doesn't over-telegraph the pattern in a way that reduces future test validity if the same trap phrasing recurs verbatim across many questions.

## Summary

The Metadata Management set is accurate, well-distributed, and gives strong, repeated coverage to this Knowledge Area's two highest-value skills: three-category classification and the lineage-vs-data-flow-diagram / lineage-composition distinctions. The two items flagged above (META-011's distractor phrasing; explanation phrasing that names traps explicitly) are minor stylistic considerations for a future improvement pass, not defects. No question files were modified as part of this review.

---

## Batch 2 Addendum: New Questions (META-021 – META-026)

**Addendum date:** 2026-08-08
**Reviewer:** Claude (CDMP Mentor, acting as Technical + DAMA Reviewer)
**Scope:** Source-verification-driven gap-filling batch (`research/knowledge_base_source_verification.md`). META-001–020 were **not modified**; this addendum classifies their disposition and audits the 6 newly authored questions.

### Existing Question Disposition (META-001–020)

| Disposition | Count | Questions |
|---|---|---|
| **KEEP** | 19 | META-001–010, 012–020 |
| **IMPROVE** (flagged, not applied now) | 1 | META-011 — distractor phrasing (inverted-claim style) flagged for a future DAMA-reviewer fairness check, per the original review's §4 note |
| **REPLACE** | 0 | — |
| **DUPLICATE/REDUNDANT** | 0 | — |

### New Questions (META-021 – META-026)

| ID | Difficulty | Type | Topic / Subtopic | Scenario industry |
|---|---|---|---|---|
| META-021 | Intermediate | Multiple Choice | Metadata Management vs. Master Data Management (cross-KA META/MASTER) | — (definitional, closes a documented gap) |
| META-022 | Beginner | Multiple Choice | Metadata Standards | — (definitional) |
| META-023 | Intermediate | Scenario-Based | Catalog deployed without governance (cross-KA META/GOV) | Government |
| META-024 | Advanced | Scenario-Based | Classification as Business Metadata (cross-KA META/SEC) | Banking |
| META-025 | Advanced | Scenario-Based | Semantic layer as Business Metadata application (cross-KA META/DWBI) | Insurance |
| META-026 | Intermediate | Multiple Choice | Metadata Integration | — (definitional) |

### Combined Set Composition (26 total)

| Difficulty | Count | Question Types |
|---|---|---|
| Beginner | 6 | Multiple Choice (6) |
| Intermediate | 13 | Multiple Choice (6), Scenario-Based (5), Multiple Select (2) |
| Advanced | 7 | Multiple Choice (1), Scenario-Based (5), Multiple Select (1) |
| **Total** | **26** | MC: 13, Scenario-Based: 9, Multiple Select: 3 |

### Scenario Coverage

New scenarios span **Government** (×1), **Banking** (×1), and **Insurance** (×1) — adding three enterprise contexts to a set whose original scenarios leaned on government/banking/healthcare/retail composites without a dedicated insurance context. Three of six new questions carry explicit cross-KA tagging.

### Source Coverage

All 6 new questions trace to specific `knowledge_base/metadata_management.md` sections; META-024 and META-025 additionally cite `data_security.md` and `data_warehousing_and_business_intelligence.md` respectively for their cross-KA content. META-025 (Semantic Layer) is correctly `source_confidence: Medium` since the source concept is explicitly `[Industry Practice, widely referenced]`, not `[DAMA]`, in both the Metadata Management and DW/BI modules. **The third-party practice-question resource was not consulted or cited** for any question in this batch.

### Duplicate/Redundancy Assessment

Checked against the existing 20 and against each other — no near-duplicates. META-021 directly closes a gap the Reference and Master Data review independently flagged as an important trap (MDM vs. Metadata Management naming confusion); it is a genuinely new question, not a restatement of MASTER-015, since it tests the distinction from META's classification angle rather than MASTER's.

### DAMA Accuracy

All 6 correct answers and explanations were checked against the exact module sections cited, using the full module text read during the Source Verification phase. No factual errors identified.

### Distractor Quality

META-021's distractors are the two most plausible name-confusion misreadings (same discipline; subset relationship) documented as an Exam Trap in both `metadata_management.md` and `reference_and_master_data.md`. META-023's distractors mirror the "tool vs. discipline" Common Mistake already established across multiple Knowledge Areas in this project.

### Explanation Quality

All 6 explanations follow the three-part structure at the same standard as the original 20.

### Cross-KA Coverage

`related_knowledge_areas` populated beyond the primary KA for 3 of 6 new questions (META-021→MASTER; META-023→GOV; META-024→SEC; META-025→DWBI) — versus zero cross-KA tagging in the original 20.

### Remaining Gaps

Not attempted in this batch: no question yet tests the Metadata Repository vs. Metadata Management Strategy distinction directly; named catalog tooling (Purview, Atlas, OpenMetadata, Collibra) is illustrative-only in the module and correctly has no dedicated question, but a build-vs-buy reasoning question (per the module's own Data Architect-level interview question) could be a future addition.

### Score and Approval Status

**Overall Score: 92/100.** Deductions: −3 for the carried-over META-011 distractor-phrasing note (not addressed in this gap-filling batch); −3 for META-025's Medium-confidence Industry Practice sourcing being the primary content of an Advanced question (acceptable per `source_confidence` rules but appropriately scored below a pure-DAMA Advanced item); −2 for the remaining topic gaps noted above.

**Approval Status: Not Approved.** All 26 questions remain `review_status: Draft`, `approval_status: Pending`, pending formal Gate 1/Gate 2/Approval processing per `question_bank/question_lifecycle.md`.
