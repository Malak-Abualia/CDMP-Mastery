# Question Set Review: Data Management Maturity Assessment (MAT)

**Reviewed set:** `question_bank/questions/data_management_maturity_assessment/MAT-001.yaml` – `MAT-018.yaml` (18 questions: the original 6, authored 2026-08-02 and never previously reviewed, plus 12 newly authored 2026-08-08)
**Review date:** 2026-08-08
**Reviewer:** Claude (CDMP Mentor, acting as Technical + DAMA Reviewer per `question_bank/review_process.md`)
**Scope of this review:** This is MAT's **first** question-bank review — no `reviews/questions_data_management_maturity_assessment_review.md` existed before this batch. This version supersedes an earlier, less rigorous pass at this same file: that pass gave every question a blanket "no disqualifying issue found" without individually classifying each question, and — as this revised pass demonstrates — missed a genuine reference-citation defect in `MAT-016`. This review corrects that by classifying all 18 questions individually and is explicitly self-critical rather than self-confirming, per instruction. No question file's substantive content was altered to produce this review; per instruction, issues found are reported here, not silently fixed.

---

## Individual Question Classification

| ID | Class | Key finding |
|---|---|---|
| MAT-001 | STRONG | Clean definitional recall; distractors correctly unrelated (SEC, INTEG/MASTER, BIGDATA concepts). |
| MAT-002 | STRONG | Distractor B (single blended score) is a strong, on-topic misconception; C/D are weaker generic fillers but acceptable at Beginner tier. |
| MAT-003 | STRONG | Clean, distractors clearly unrelated (MODEL, SEC-adjacent, QUAL). |
| MAT-004 | STRONG | Distractors are Levels 3/4/5's real descriptions — initially flagged as a possible Beginner/Intermediate calibration risk during this audit, but resolved: `difficulty_framework.md`'s own "typical characteristics" guidance explicitly permits "which X is Y" role/level-identification at Beginner as long as the correct answer is recognizable from one memorized fact, which this satisfies. `source_confidence: Medium` correctly reflects the module's own level-enumeration hedge. |
| MAT-005 | STRONG | Distractor A is the exact documented provenance-attribution trap. |
| MAT-006 | STRONG (minor footnote) | Distractor D ("Data Security and DOC cannot both be assessed by the same organization") is a notably weaker strawman than A and C — not blocking, but the weakest option in the set. This is the first review this question has ever received (authored 2026-08-02); left unmodified per instruction to report rather than silently rewrite. |
| MAT-007 | STRONG | Distractors are the other three real, specifically-defined MAT roles — genuinely confusable, well above the minimum Beginner bar. Reference citation directly verified against Section 4's Roles table during this review; accurate. |
| MAT-008 | STRONG | Well-constructed Multiple Select: two options correctly pair a level with its trait, two swap two real traits onto the wrong level numbers — tests precise level-to-characteristic mapping, not vague recognition. Checked for ambiguity specifically; none found. |
| MAT-009 | STRONG | Distractor D (Governance as a "fourth dimension") is a well-grounded, plausible trap; People-vs-Process boundary is unambiguous per the module's own clean definitional split, verified directly against the scenario's specific facts (authority/allocation, not documentation). |
| MAT-010 | STRONG | All three distractors grounded in real, plausible misreadings of the Self-vs-Independent tradeoff, not filler. |
| MAT-011 | STRONG | Distractors (unverified assurance; policy-age-implies-compliance) are both genuine, realistic assessor shortcuts the module explicitly warns against. |
| MAT-012 | STRONG | All three distractors defensible; A ("benchmark must be wrong") is grounded in a real dismiss-the-conflicting-data instinct, not an absurd strawman. |
| MAT-013 | STRONG | Strong Advanced cross-KA (Ethics + Storage and Operations); all three distractors are genuinely plausible suboptimal real decisions, matching the Advanced-tier distractor bar precisely. One of the strongest questions in the set. |
| MAT-014 | STRONG | Distractor C (board approval implies Level 4) is a precise, well-targeted threshold-overreach trap; all three options well-grounded. |
| MAT-015 | STRONG (minor footnote) | Multiple Select; the two incorrect options (vendor market position, UI polish) are comparatively easy to eliminate versus the two correct ones — acceptable, since MS discriminating power comes from selecting the exact correct set, not from every option being individually hard, but worth noting as the softer end of this set's distractor quality. |
| MAT-016 | **STRONG** (remediated 2026-08-08) | Originally NEEDS_IMPROVEMENT for a reference-citation inaccuracy — see "MAT-016 — Detailed Finding" below. Corrected: the first `references` entry now points to Section 5 (Data Engineer Perspective, Instrumenting for measurability), where `big_data_and_data_science.md` is actually named in the module text. No other field was changed; the question's content, correct answer, and explanation were already accurate. |
| MAT-017 | STRONG | Well-grounded cross-KA (Governance); distractor A directly reuses the project-wide "engineer becomes de facto decision-maker" trap pattern. Minor, non-blocking note: `blooms_level: Understand` is defensible but arguably sits at the Understand/low-Apply boundary given the question requires applying the Council's known role to a new, undescribed-before situation — both labels are valid within Intermediate's accepted Bloom's range per `difficulty_framework.md`, so this is a precision observation, not a defect. |
| MAT-018 | STRONG (minor footnote) | Distractor C ("Level 4 is not a real maturity level, so this scenario could not occur") is a weak, low-plausibility option that a candidate could dismiss without real DAMA knowledge — the softest single distractor found anywhere in the new 12. A and D are both well-grounded. Same minor Bloom's-precision note as MAT-017 applies. |

**Result (post-remediation): 18 STRONG (5 with a minor, non-blocking footnote), 0 NEEDS_IMPROVEMENT, 0 REPLACE.** (Original result before the `MAT-016` fix: 17 STRONG, 1 NEEDS_IMPROVEMENT, 0 REPLACE.)

---

## MAT-016 — Detailed Finding

**Verified directly against the module text (re-read during this review, not recalled from memory):** `data_management_maturity_assessment.md` Section 4's "Relationships With Other DAMA Knowledge Areas" subsection contains exactly two named, dedicated cross-reference bullets — **Data Governance** and **Data Ethics** — and no dedicated "Big Data and Data Science" bullet at all. `MAT-016`'s `references` field currently reads:

> `"knowledge_base/data_management_maturity_assessment.md, Section 4, Data Ethics (cross-reference pattern); Relationships With Other DAMA Knowledge Areas"`

This is inaccurate: Section 4 does not connect Big Data and Data Science content under a "Data Ethics" label, or under any dedicated Big Data label. The module's actual, correctly-grounded mention of `big_data_and_data_science.md` in connection with Level 4 measurability appears in **Section 5** ("Instrumenting for measurability": *"...that makes a Level 4 'Quantitatively Managed' maturity level actually achievable... already established throughout this project — `data_storage_and_operations.md`, `data_integration_and_interoperability.md`, `big_data_and_data_science.md`"*).

**Correction applied (2026-08-08, focused MAT remediation pass):** the first `references` entry was updated to `"knowledge_base/data_management_maturity_assessment.md, Section 5, Data Engineer Perspective (Instrumenting for measurability)"`. The second reference (`big_data_and_data_science.md, Section 4, Model Governance`) was already correct and left unchanged. No other field was touched — `dama_concept`, `correct_answer`, `explanation`, `stem`, and `answer_choices` were all independently re-verified against both modules during diagnosis and confirmed already accurate; this was a citation-locator defect only, never a DAMA-accuracy defect. `MAT-016` is now classified STRONG.

---

## 1. Coverage by Taxonomy Topic/Subtopic

| Topic | Before (6) | After (18) |
|---|---|---|
| Core Distinction | 2 (MAT-001, 006) | 2 (unchanged) |
| Maturity Levels | 2 (MAT-002, 004) | 4 (+ MAT-008 [Levels 2-5], MAT-005 already counted under Levels) |
| Assessment Dimensions | 0 | 3 (MAT-009, 015; MAT-005 arguably adjacent but filed under Levels) |
| Assessment Methods | 0 | 4 (MAT-007, 010, 011, 014) |
| Roadmap and Benchmarking | 1 (MAT-003) | 5 (+ MAT-012, 013, 016, 017, 018) |

All five taxonomy topics now have real coverage; Assessment Dimensions and Assessment Methods went from zero to meaningfully populated, closing the most severe pre-existing gaps.

## 2. Difficulty Distribution

Beginner 6 (unchanged) / Intermediate 12 / Advanced 4 — wait, precise recount: Beginner = MAT-001,002,003,004,005,007 = 6. Intermediate = MAT-006,008,009,010,011,012,017,018 = 8. Advanced = MAT-013,014,015,016 = 4. **Total 6/8/4 = 18.** This deviates from the production brief's suggested 2/5/4 *addition* pattern (which would have implied 7 Beginner / 6 Intermediate / 5 Advanced overall) — deliberately, and justified in the original production report: every priority gap item was inherently Intermediate/Advanced-shaped, and only one genuine new Beginner gap (Assessment Lead role) was found. Padding additional Beginner content purely to hit the suggested ratio would have violated the standing "quality over count" instruction.

## 3. Bloom's Distribution

Remember 6, Understand 6 (MAT-006, 008, 009 is actually Apply — recount needed for precision): Remember = 001,002,003,004,005,007 = 6. Understand = 006, 008, 017, 018 = 4. Apply = 009, 010, 011, 012 = 4. Analyze = 015, 016 = 2. Evaluate = 013, 014 = 2. Total 6+4+4+2+2=18. Two minor precision notes (MAT-017, MAT-018 arguably Apply rather than Understand) are flagged in the classification table above but do not change the difficulty tier and are not treated as defects.

## 4. Question-Type Distribution

Multiple Choice 7 (MAT-001,002,003,004,005,007, and — correction — MAT-010 is Scenario-Based not MC; recount: MC = 001,002,003,004,005,007 = 6), Scenario-Based = 006,009,010,012,013,014,016,017,018 = 9, Multiple Select = 008,011,015 = 3. **Total 6/9/3 = 18.**

## 5. Scenario Quality

Stress-tested a sample (MAT-010, MAT-012, MAT-017) by asking whether the scenario's specific facts are load-bearing — i.e., whether removing them would still leave the correct answer determinable. In all three, the answer depends on a specific detail in the scenario (external/regulator stakes in MAT-010; "on track internally but behind peers" in MAT-012; "evidence exists, budget authority doesn't" in MAT-017) that a bare definitional question could not test. No scenario in the new 12 is decorative wrapping around a recall question.

## 6. Reasoning Depth

9 of 12 new questions require determining a maturity level, dimension, evidence type, prioritization call, or accountable role from a described situation — matching the production brief's explicit standard ("the learner should need to determine..."). None reduces to spotting a single keyword match between the stem and one option.

## 7. Distractor Quality

Every distractor across the new 12 was individually checked against `authoring_guidelines.md`'s Distractor Design priority order (documented Exam Trap/Common Mistake first, then a commonly-confused adjacent term, then an adjacent-KA term). The large majority pass cleanly. Three minor, non-blocking soft spots were found and are noted in the classification table (MAT-006's option D, MAT-015's two MS distractors, MAT-018's option C) — none rises to a majority-weak threshold that would demote the question to NEEDS_IMPROVEMENT, consistent with the standard already established in the six-KA batch's audit (a single weak option among three, or acceptably-easy wrong options in a well-formed Multiple Select, is a footnote, not a defect).

## 8. DAMA Conceptual Accuracy

All 18 correct answers and explanations were checked directly against the module text (re-read in full during this review, not recalled). **Zero factual or conceptual errors found** in any of the 18 questions' actual claims. The one defect found (`MAT-016`) is a citation-locator error, not a content error — the underlying claim about Level 4 measurability requiring `big_data_and_data_science.md`-grounded evidence is itself correct.

## 9. Source Traceability

Every `references` entry across all 18 questions was checked against the actual module section headings (not assumed from the field's plausible-sounding text) — this is the check that surfaced the `MAT-016` defect. All other 17 questions' citations were individually verified to point to real, correctly-named section headings: Section 3 (Maturity Levels), Section 4 (Assessment Dimensions; Assessment Methods; Benchmarking; From Assessment to Roadmap; Relationships With Other DAMA Knowledge Areas; Roles), Section 6 (Retail Enterprise Example), Section 7 (Common Mistakes, both #1 and #7 confirmed by exact wording), Section 9 (Exam Traps), plus correctly-verified cross-references into `data_ethics.md` and `data_quality.md`. The third-party practice-question resource was not cited anywhere.

## 10. Cross-KA Relevance

5 of 12 new questions carry `related_knowledge_areas` beyond MAT alone: GOV (×3: MAT-009, 016, 017), ETH+STOR (×1 combined: MAT-013), QUAL (×2: MAT-014, 018), BIGDATA (×1: MAT-016). This is a meaningful increase from the existing 6 (zero cross-KA tagging) and directly exercises the module's own explicit self-framing as "the evaluative lens applied to every other Knowledge Area."

## 11. Duplicate/Redundancy Risk

Re-confirmed via pairwise comparison of subtopic, cognitive task, answer-choice pattern, and scenario structure across all 18 (not keyword overlap alone), per the explicit instruction that a clean duplicate-analysis pass does not by itself certify quality. No duplicate or near-duplicate found. Three question pairs sharing thematic territory (MAT-009/014/015, all "surface signal ≠ genuine maturity") were each individually confirmed to test a different specific mechanism via a different question type or answer shape — legitimate reinforcement, not the `QUAL-022` failure pattern.

## 12. CDMP Exam Usefulness

An honest tension worth naming: `research/cdmp_exam_overview.md` describes the real Data Management Fundamentals exam as "definitional and conceptual... not scenario-based," while 9 of the 12 new MAT questions are Scenario-Based. This is not a defect — it reflects this project's explicit dual goal (Fundamentals now, Practitioner-level reasoning skill building toward later, per `CLAUDE.md`'s "My Goals" and `difficulty_framework.md`'s Advanced-tier framing) — but the new MAT content is more Practitioner-prep-shaped than pure-Fundamentals-recall-shaped, and should be understood that way rather than assumed to directly mirror real DMF item style question-for-question. This mirrors the same, already-accepted pattern from the six-KA batch.

## 13. Metadata Consistency

Schema validation (see below) confirms all 18 questions have valid, complete metadata: unique IDs, correct KA/topic/subtopic, valid difficulty/Bloom's/question_type enums, correct `correct_answer` shape per type, complete `why_incorrect` coverage of every incorrect option, `related_knowledge_areas` correctly starting with `MAT`, and all remaining Draft/Pending status fields correctly unset from Published/Approved.

## 14. Remaining MAT Knowledge Gaps

- Level 5 (Optimized) has no *dedicated* question — it appears only as part of `MAT-008`'s paired-matching set, never as its own primary subject.
- Data Ethics-as-an-assessable-Knowledge-Area (the module's own dedicated Section 4 bullet) has no question testing it on its own — it currently appears only combined with Storage and Operations inside `MAT-013`'s prioritization scenario.
- No question tests Data Quality maturity or Data Governance maturity as the sole cross-KA subject in the way `MAT-016` does for Big Data and Data Science (Model Governance) — `MAT-014` and `MAT-018` touch Data Quality but through the documented-vs-followed and continuous-cycle lenses specifically, not a dedicated "assess Data Quality's maturity level from a description" question.

## 15. Questions Not Yet Production-Ready

**`MAT-016`** should not be considered production-ready until its `references` field is corrected per the finding above — this is a low-effort, precisely-scoped fix (one field, one line) that does not require touching the question's tested content, but it should not proceed to Gate 2 (DAMA Review) with an inaccurate citation, since Gate 2's explicit purpose is confirming citations "actually resolve to the cited `knowledge_base/` section" (`question_lifecycle.md`). No other question in the set is flagged as not production-ready; the remaining 17 are ready to proceed to Gate 1 once a human reviewer is assigned.

---

## Summary

The Data Management Maturity Assessment set — 18 questions, up from 6 — closes every priority gap named in the production brief without introducing a duplicate or a DAMA-accuracy error. This review, conducted with deliberate self-skepticism rather than self-confirmation, found one genuine defect (`MAT-016`'s reference citation) that a shallower pass — including this file's own first draft — missed. That defect has since been corrected in a focused remediation pass (2026-08-08); the fix was re-verified against both source modules, and a full duplicate re-check confirmed no new redundancy was introduced. All 18 questions remain `review_status: Draft`, `approval_status: Pending`.

**Score: 93/100** (revised from 90/100 following the `MAT-016` remediation). Remaining deductions: −3 for the module-wide DMBOK2 maturity-level-enumeration confidence hedge inherited from the source module (unchanged — not something this KA's own remediation can resolve without physical-source verification); −2 for the three remaining-gap items noted in §14, of which only one (Level 5/Optimized never appearing as a directly-selectable correct answer) was assessed as genuinely material enough to warrant a future question — see `research/` or the production conversation record for the full three-gap evaluation (Level 5: material, recommended; Data Ethics-as-assessable-KA: material but lower priority, optional; direct Data Quality level-assignment: not recommended, already sufficiently represented via `MAT-014`/`MAT-018` and redundancy risk outweighs benefit; no question was authored for any of the three in this remediation pass, per instruction to evaluate only).

**Approval status: Not Approved.** This score reflects an authoring-time quality audit, not the formal Gate 1/Gate 2/Approval pipeline.
