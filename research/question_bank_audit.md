# Question Bank Quality Audit — Phase 1

**Audit date:** 2026-08-01
**Auditor:** Claude (acting independently of the original authoring/review passes, per `question_bank/review_process.md`)
**Scope:** All 120 Phase 1 questions (`question_bank/questions/{data_governance,data_modeling_and_design,data_architecture,data_quality,metadata_management,reference_and_master_data}/`), audited against `question_bank/question_quality_standards.md`, `question_bank/metadata_schema.md`, and `question_bank/review_process.md`. Cross-checked against the six existing per-KA reviews in `reviews/questions_*_review.md`.
**Method:** Structural verification via direct field-level extraction across all 120 files (not a re-read of the six prior reviews' prose alone) — difficulty, Bloom's level, question type, and tagging fields were independently counted from the source YAML, and cross-referenced against what the six per-KA reviews previously reported, to catch drift between what was documented and what was actually authored.
**No question files were modified during this audit.**

---

## 1. Total Question Coverage

120 of 120 planned Phase 1 questions exist (verified by file count: 20 per Knowledge Area × 6 Knowledge Areas). Every file conforms to the `.yaml` naming convention in `question_bank/naming_conventions.md` (`<KA_CODE>-<3-digit sequence>`).

However, Phase 1 covers only the six Knowledge Areas whose `knowledge_base/` modules are currently Approved (GOV, ARCH, MODEL, QUAL, META, MASTER). The remaining eight Knowledge Areas (STOR, SEC, INTEG, DOC, DWBI, BIGDATA, MAT, ETH) — 57% of the full DMF exam's 14-Knowledge-Area scope — have **zero** questions, because their source modules are still template-only (`knowledge_base/README.md`, `CLAUDE.md` Status). This is expected and correct given Phase 1's explicit scope, but it is the single largest gap between "Phase 1 complete" and "ready to power a full CDMP Fundamentals mock exam."

**Finding:** Coverage is complete *for its declared scope* but represents less than half of the full exam blueprint by Knowledge Area count.

## 2. Knowledge Area Balance

| Knowledge Area | Questions |
|---|---|
| GOV | 20 |
| MODEL | 20 |
| ARCH | 20 |
| QUAL | 20 |
| META | 20 |
| MASTER | 20 |

Perfectly even — 20 questions per covered Knowledge Area, no imbalance. Note this is an *authoring* balance, not an *exam-weight* balance: `research/cdmp_exam_overview.md` documents GOV/MODEL/QUAL/META at the ~11% exam-weight tier and ARCH/MASTER at a lower tier, so an equal 20-per-KA question count will over-represent lower-weighted KAs and under-represent higher-weighted ones if sampled uniformly by a future Quiz/Mock Exam Engine — the engine's sampling logic must weight by exam relevance, not treat all 120 questions as equally likely to be drawn.

## 3. Difficulty Distribution

Verified by direct field count across all 120 files:

| Difficulty | Count | % of total |
|---|---|---|
| Beginner | 30 | 25% |
| Intermediate | 60 | 50% |
| Advanced | 30 | 25% |

Exactly matches the specified 5/10/5 split per Knowledge Area, with no drift. This distribution is appropriately skewed toward the Fundamentals exam's documented "definitional and conceptual" character (`research/cdmp_exam_overview.md`) while still building toward Practitioner-level (Advanced-tier) readiness per this project's stated goals in `CLAUDE.md`.

## 4. Bloom's Taxonomy Distribution

Verified by direct field count:

| Bloom's Level | Count | % of total |
|---|---|---|
| Remember | 30 | 25% |
| Understand | 39 | 32.5% |
| Apply | 20 | 16.7% |
| Analyze | 13 | 10.8% |
| Evaluate | 18 | 15% |
| Create | 0 | 0% |

The distribution skews appropriately toward Remember/Understand (57.5% combined), consistent with `difficulty_framework.md`'s own guidance that these dominate a healthy Fundamentals-focused bank. **Zero Create-level questions** is a legitimate, if minor, gap: `difficulty_framework.md` states Expert-tier questions may "occasionally" require Create ("propose the most defensible approach given these constraints"), but all 30 Advanced-tier questions in this set top out at Analyze/Evaluate. This is not a defect — Create-level items are explicitly the rarest tier — but it means the bank currently has no items exercising the highest cognitive-demand tier the framework defines.

## 5. DAMA Terminology Accuracy

Spot-verified across a representative sample plus full-text search for every named external regulation/standard in the bank (BCBS 239, ISO 4217, ISO 3166, ICD-10, PSD2, HIPAA, HL7 FHIR — 8 files matched). Terminology usage (Owner/Steward/Custodian, the seven Data Quality dimensions, the three Metadata categories, MDM implementation styles, TOGAF's four domains, etc.) is precise and consistent with the corresponding `knowledge_base/` modules throughout.

**Two confirmed tagging inconsistencies**, found by comparing all 8 regulation/standard-referencing questions against each other:

| Question | Issue |
|---|---|
| `GOV-016.yaml` | Stem and `keywords` reference "BCBS 239" prominently, but `industry_practice_concept` is left `null`. Two other questions referencing the same regulation (`QUAL-018.yaml`, `MASTER-016.yaml`) correctly set `industry_practice_concept: "BCBS 239"`. |
| `MASTER-006.yaml` | Stem references "the ISO 4217 standard," but `industry_practice_concept` is left `null`, with no corresponding tag capturing the named standard. |

By contrast, `META-018` (HIPAA), `ARCH-016` (PSD2/Open Banking), and `ARCH-019`/`MODEL-020` (HL7 FHIR) all correctly populate `industry_practice_concept` for their respective named regulation/standard. This is a small, mechanical, easily-fixed inconsistency — not a conceptual accuracy problem — but it means `dama_concept`/`industry_practice_concept`-based filtering (a stated future Access Layer capability, per `architecture.md`) would silently miss these two questions if a consumer ever queried "all questions touching a named regulation."

One additional item flagged for DAMA Reviewer attention rather than confirmed as an error: `ARCH-008` (correctly self-rated `source_confidence: Medium`) phrases TOGAF's Business Architecture domain as defining "*why* certain data is needed" — a reasonable paraphrase of `data_architecture.md`'s "Business Architecture drives Data Architecture requirements," but slightly more interpretive than the source text's own wording. The question's own Medium confidence rating already flags this appropriately; it is surfaced here as confirmation that the self-rating is accurate, not as a new defect.

## 6. Question Ambiguity

No question was found with two defensible correct answers across the full set (consistent with all six prior per-KA reviews' findings, independently re-checked here for the higher-risk Multiple Select items in particular, since ambiguous "select all" instructions are the most common real-world source of assessment ambiguity).

**One structural nuance worth documenting rather than fixing:** `GOV-016` is the only question in the bank where `question_type: "Scenario-Based"` pairs with a Multiple-Select-shaped `correct_answer` (an array, `["A", "B", "D"]`) and a "(Select all that apply.)" instruction in the stem. This is technically permitted by `metadata_schema.md`'s own Type-Specific Answer Structures table (Scenario-Based may carry "Same as Multiple Choice/Select" answer shapes), so it is not a schema violation — but it means a future Quiz Engine cannot infer answer cardinality (single- vs. multi-select) from `question_type` alone; it must inspect whether `correct_answer` is a string or an array. This is a design note for `architecture.md`'s Access Layer, not a content defect.

## 7. Distractor Quality

Confirmed, consistent with the six prior per-KA reviews: the large majority of distractors trace directly to a named Exam Trap or Common Mistake already documented in the corresponding `knowledge_base/` module (e.g., `GOV-007`'s distractor set mirrors the Owner/Steward/Custodian/Architect confusion the source module itself calls its highest-value exam trap; `QUAL-006`–`QUAL-009` each target one of the four most-confused Data Quality dimension pairs). This is the strongest dimension of the entire Phase 1 set — distractors consistently represent real, plausible misconceptions rather than arbitrary wrong answers, satisfying `question_quality_standards.md` Standard 6 well above a minimum bar.

## 8. Explanation Quality

All 120 questions include the full three-part explanation structure specified in `authoring_guidelines.md` (why the correct answer is correct; why each incorrect option is wrong; a specific `knowledge_base/` citation). No bare "this is wrong" statements were found. Explanation length is consistently appropriate for a question-bank record (2–5 sentences) rather than reproducing full module-length treatment.

## 9. Reference Quality

Every question's `references` field cites a specific `knowledge_base/*.md` file and section, not just the file. Cross-checked against each source module's actual current section structure (all six modules retain the section numbering their questions cite — `reference_and_master_data.md` in particular was restructured in an earlier revision, and all `MASTER-*` question references correctly use its *current*, post-revision section numbers rather than stale pre-revision ones). References are section-level rather than paragraph-level, which is a reasonable granularity for this phase but coarser than ideal for a learner wanting to jump to the exact sentence — a candidate refinement, not a defect.

## 10. CDMP Fundamentals Readiness

Two structural gaps limit this bank's readiness to power a full exam simulation today, both already implied above but worth stating together as the audit's central finding:

1. **Knowledge Area breadth.** Only 6 of 14 Knowledge Areas have any content. `architecture.md`'s Mock Exam Engine design explicitly requires sampling "proportionally to each Knowledge Area's documented exam weighting" (`research/cdmp_exam_overview.md`) — this is impossible to do faithfully today, since 8 of 14 weighted Knowledge Areas contribute zero questions. Any mock exam assembled from the current bank would systematically over-represent GOV/ARCH/MODEL/QUAL/META/MASTER and cannot claim to simulate the real exam's actual Knowledge Area mix.
2. **Question type mismatch with the real exam's stated format.** `research/cdmp_exam_overview.md` describes the real Data Management Fundamentals exam format as "100 multiple-choice questions" — it does not describe a "select all that apply" mechanic. This bank's 23 Multiple Select questions (19% of the total) are pedagogically valuable for precise recall but are not confirmed to reflect the real exam's actual question mechanics. A future Mock Exam Engine should either exclude Multiple Select items from full-length simulations, or clearly flag them as supplementary practice rather than exam-representative, until this is confirmed against an official exam guide (see `research/source_map.md` §2, still an open item).

Within the 6 covered Knowledge Areas, depth and quality are strong enough to support real practice-quiz use today — the readiness gap is about *breadth of exam coverage*, not the quality of what exists.

---

## Overall Score: 88 / 100

| Dimension | Score /100 |
|---|---|
| 1. Total question coverage | 90 |
| 2. Knowledge Area balance | 100 |
| 3. Difficulty distribution | 100 |
| 4. Bloom's Taxonomy distribution | 85 |
| 5. DAMA terminology accuracy | 90 |
| 6. Question ambiguity | 92 |
| 7. Distractor quality | 93 |
| 8. Explanation quality | 95 |
| 9. Reference quality | 88 |
| 10. CDMP Fundamentals readiness | 65 |

The gap between this audit's 88 and a near-perfect score is driven almost entirely by dimension 10 (exam-breadth readiness), which is a scope characteristic of Phase 1 by design, not an authoring failure — content quality within scope (dimensions 6–8) is consistently excellent.

---

## Strengths

- **Perfectly consistent structural compliance.** All 120 questions hit the exact requested 5/10/5 difficulty split and all three requested question types, with zero missing required metadata fields found during this audit's field-level extraction.
- **Distractor design is the standout strength.** The large majority of distractors are traceable to a real, named misconception already documented as an Exam Trap or Common Mistake in the source `knowledge_base/` module, rather than arbitrary wrong answers — this is a meaningfully higher bar than typical exam-prep question banks meet.
- **Explanation depth exceeds the stated minimum bar.** Every question gives full reasoning for the correct answer and a specific reason for every distractor, consistent with `authoring_guidelines.md`.
- **Confirmed non-duplication against existing `knowledge_base/` quiz content** (verified explicitly for MASTER during authoring; no cross-set duplication found elsewhere either).
- **Sourcing discipline is real, not decorative** — `[DAMA]`/`[Industry Practice]` tagging correctly reflects the underlying content's actual provenance in the overwhelming majority of cases, including correctly hedging uncertain DMBOK2 enumerations with `source_confidence: Medium` (7 questions: `GOV-015`, `ARCH-008`, `ARCH-013`, `MODEL-019`, `MASTER-011`, `MASTER-013`, `META-019`) rather than overclaiming certainty.

## Weaknesses

- **Only 6 of 14 Knowledge Areas covered** — the largest single gap relative to the ultimate goal of full CDMP Fundamentals simulation (expected at this phase, but the most important thing to communicate clearly before anyone assumes the bank is exam-representative).
- **Two confirmed metadata tagging omissions** (`GOV-016`, `MASTER-006`) where a named regulation/standard appears in the question content but not in `industry_practice_concept`.
- **Five of the six existing per-KA review documents (`reviews/questions_*_review.md`) contain inaccurate "Set Composition" tables** — see the dedicated finding below. `MASTER`'s review was accurate; `GOV`, `MODEL`, `ARCH`, `QUAL`, and `META`'s were not.
- **Zero Bloom's "Create"-level questions**, leaving the highest cognitive-demand tier `difficulty_framework.md` defines completely unexercised.
- **Multiple Select as a question type is not confirmed to match the real exam's documented format**, creating risk that a future Mock Exam built naively from this bank would misrepresent the real exam experience.
- **References are section-level, not paragraph-level** — usable but coarser than ideal for direct remediation linking.

## Documentation Accuracy Finding (new — not previously identified)

Independently re-counting `question_type` per Knowledge Area from the actual YAML files and comparing against the "Set Composition" tables in each existing `reviews/questions_*_review.md` revealed **discrepancies in 5 of 6 review documents**:

| Knowledge Area | Review document reported (MC / Scenario / MS) | Actual (verified) | Match? |
|---|---|---|---|
| GOV | 9 / 7 / 4 | 7 / 9 / 4 | **No** — MC and Scenario-Based counts were transposed |
| MODEL | 10 / 6 / 4 | 9 / 7 / 4 | **No** — off by one on MC/Scenario |
| ARCH | 10 / 7 / 3 | 9 / 7 / 4 | **No** — off by one on MC/MS |
| QUAL | 8 / 9 / 3 | 8 / 8 / 4 | **No** — off by one on Scenario/MS |
| META | 8 / 9 / 3 | 10 / 7 / 3 | **No** — MC and Scenario-Based counts swapped |
| MASTER | 10 / 6 / 4 | 10 / 6 / 4 | **Yes** |

All three type totals sum correctly to 20 per Knowledge Area and 120 overall in every case — the errors are internal miscounts within each review's summary table, not missing or extra questions. This does not affect question content quality but means the six existing review documents' composition tables should not be trusted as authoritative without this audit's correction; a future pass should update the five inaccurate tables to match the verified counts above (`research/question_bank_audit.md` §1 above, per-KA counts). This audit did not correct those files, per the "do not modify existing files" instruction governing this task.

---

## Highest-Risk Questions

Ranked by combined severity of confirmed issues, not by Knowledge Area:

1. **`GOV-016.yaml`** — Two compounding issues: (a) confirmed `industry_practice_concept` tagging omission for BCBS 239 despite prominent stem/keyword usage; (b) the bank's only `Scenario-Based`-typed question with a Multiple-Select answer shape, which is schema-permitted but requires special handling by any future consumer that infers UI behavior from `question_type` alone. Recommend DAMA Review re-confirm the tag and Technical Review confirm the type/shape combination is intentional before this question reaches Approval.
2. **`MASTER-006.yaml`** — Confirmed `industry_practice_concept` tagging omission for ISO 4217. Lower severity than `GOV-016` since it's a single, isolated issue with a mechanical fix.
3. **`ARCH-008.yaml`** — Not a confirmed defect, but the highest-interpretive-risk item in the set: its `source_confidence: Medium` rating is appropriate and should be preserved through DAMA Review rather than upgraded to High without re-verifying the TOGAF Business Architecture phrasing against DMBOK2's own text directly (per `research/source_map.md`'s priority hierarchy, DMBOK2 outranks the general-EA-pattern framing this question rests on).
4. **The 7 `source_confidence: Medium` questions collectively** (`GOV-015`, `ARCH-008`, `ARCH-013`, `MODEL-019`, `MASTER-011`, `MASTER-013`, `META-019`) plus the related but distinct set of 11 questions with `dama_concept: null` (content classified as pure `[Industry Practice]` with no DAMA-core anchor: `ARCH-005`, `ARCH-008`, `ARCH-011`, `ARCH-013`, `ARCH-019`, `MODEL-004`, `MODEL-009`, `MODEL-019`, `MASTER-013`, `META-012`, `META-019`). The two sets overlap at five questions (`ARCH-008`, `ARCH-013`, `MODEL-019`, `MASTER-013`, `META-019`) but are not identical — both groups mark genuinely uncertain-enumeration or industry-only content and warrant priority attention in the next DAMA Review pass, since they are the questions most likely to need a wording adjustment if a more authoritative DMBOK2 citation becomes available.

No question in the set was found to have a factual error, a broken answer key, or two defensible correct answers — the "highest risk" items above are tagging/consistency and confidence-calibration issues, not correctness failures.

---

## Recommendations Before Quiz Engine Implementation

1. **Do not build a full-length Mock Exam feature yet.** With 8 of 14 Knowledge Areas absent, any "simulate the real exam" feature would be misleading. Gate Mock Exam Engine work behind reaching a defined minimum Knowledge Area coverage threshold (e.g., at least 10–12 of 14 KAs populated), consistent with `question_bank/roadmap.md` Phase 2's dependency on Phase 1 breadth.
2. **Build the Quiz Engine's query layer to filter on `question_type` shape, not just its label** — specifically, branch UI/scoring behavior on whether `correct_answer` is a string or array, not solely on the `question_type` field, to correctly handle `GOV-016`'s Scenario-Based/Multi-Select combination without special-casing it.
3. **Decide, before Mock Exam assembly logic is written, how Multiple Select questions are treated** relative to the real exam's documented pure multiple-choice format — exclude them from exam-simulation sampling, or explicitly confirm via an official exam guide (per the open item in `research/source_map.md` §2) that the real exam does include this mechanic.
4. **Fix the two confirmed tagging omissions** (`GOV-016`, `MASTER-006`) during the next scheduled improvement pass for those Knowledge Areas — low effort, clears a real (if minor) metadata-accuracy gap.
5. **Correct the five inaccurate Set Composition tables** in `reviews/questions_data_governance_review.md`, `reviews/questions_data_modeling_and_design_review.md`, `reviews/questions_data_architecture_review.md`, `reviews/questions_data_quality_review.md`, and `reviews/questions_metadata_management_review.md` to match the verified counts in this audit, so future readers of those reviews aren't working from incorrect composition data.
6. **Prioritize the next Knowledge Area module (per `CLAUDE.md`'s Knowledge Base Operating Workflow) toward Data Quality's or Governance's exam-weight tier**, so Phase 1 authoring can extend into the next-highest-value KA rather than an arbitrary one, keeping the Question Bank's exam-weight coverage growing in the right order.
7. **Before any Quiz Engine ships**, confirm the Access Layer design in `architecture.md` accounts for exam-weight-proportional sampling (per this audit's §2 finding) rather than uniform per-KA sampling, since a naive "pick randomly from all 120" approach would misrepresent the real exam's emphasis even once more Knowledge Areas are added.

---

## Audit Boundaries

This audit did not: modify any question file; modify any existing review file (per instruction, despite finding the composition-table errors documented above); re-verify every one of the 120 explanations word-for-word against DMBOK2 primary text (relied on the existing per-KA reviews' accuracy checks plus this audit's own independent structural and regulation-tagging verification); or assess anything about a Quiz Engine, since none exists yet.
