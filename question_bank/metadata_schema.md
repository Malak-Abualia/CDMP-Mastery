# Question Bank — Metadata Schema

## Purpose

The complete field-by-field data contract every question record must satisfy. This is the schema every future consumer (`architecture.md`) is built against — a Quiz Engine, an AI Tutor, and a REST API can all trust the same fields exist with the same meaning, because this document is the single definition of them.

No file format or database technology is chosen here (see `architecture.md`, Non-Goals) — this defines the *fields*, not their eventual serialization.

## Field Reference

| Field | Type | Required | Description | Governing document |
|---|---|---|---|---|
| `question_id` | String, fixed format | Yes | Permanent, immutable identifier, e.g. `GOV-001`. Never reused, never changed once assigned. | `naming_conventions.md` |
| `version` | String, `MAJOR.MINOR` | Yes | Current version of this question. Starts at `1.0` on first Approval. | `versioning.md` |
| `knowledge_area` | Enum (14 values) | Yes | The single primary Knowledge Area, from the Knowledge Area Index. | `taxonomy.md` |
| `topic` | String (controlled list per KA) | Yes | Subject grouping within the Knowledge Area. | `taxonomy.md` |
| `subtopic` | String (controlled list per topic) | Yes | Fine-grained grouping within the topic. | `taxonomy.md` |
| `difficulty` | Enum: Beginner / Intermediate / Advanced / Expert | Yes | See difficulty definitions and level-selection criteria. | `difficulty_framework.md` |
| `blooms_level` | Enum: Remember / Understand / Apply / Analyze / Evaluate / Create | Yes | Cognitive skill tested. `[Industry Practice]` — Bloom's Taxonomy is a general pedagogical framework, not DAMA-specific. | `difficulty_framework.md` |
| `learning_objective` | String, one sentence | Yes | What a learner who answers this correctly has demonstrated (e.g., "Can distinguish Data Owner accountability from Data Steward responsibility"). | `authoring_guidelines.md` |
| `dama_concept` | String or null | Conditional | The specific `[DAMA]`-tagged DMBOK2 concept this question tests, if any. Mutually informative with `industry_practice_concept` — a question typically populates one or both. | `question_quality_standards.md`, Standard 9 |
| `industry_practice_concept` | String or null | Conditional | The specific `[Industry Practice]`-tagged concept this question tests, if any. | `question_quality_standards.md`, Standard 9 |
| `keywords` | Array of strings | Yes | Free-text search terms, used for duplication checks and Quiz Engine filtering. | `authoring_guidelines.md` |
| `estimated_solving_time` | Integer, seconds | Yes | Expected time to answer, used to calibrate Mock Exam timing (real exam: 90 min / 100 questions ≈ 54 sec/question average, per `research/cdmp_exam_overview.md`) and to detect analytics anomalies (a question routinely taking 3x its estimate may be poorly worded). | `difficulty_framework.md` |
| `question_type` | Enum: Multiple Choice / Multiple Select / True-False / Scenario-Based / Matching / Ordering / Mini Case Study | Yes | Structural type. Determines the shape of `answer_choices` and `correct_answer` below. | `authoring_guidelines.md` |
| `stem` | String (Markdown) | Yes | The question text itself (and, for Scenario-Based/Mini Case Study, the scenario narrative). | `authoring_guidelines.md` |
| `answer_choices` | Type varies by `question_type` — see below | Yes (except True/False, which is implicit) | The full set of options/pairs/sequence items presented to the learner. | See "Type-Specific Answer Structures" below |
| `correct_answer` | Type varies by `question_type` — see below | Yes | The correct option(s)/pairing(s)/sequence. | See "Type-Specific Answer Structures" below |
| `explanation` | String (Markdown) | Yes | Full reasoning for the correct answer. | `question_quality_standards.md`, Standard 7 |
| `why_incorrect` | Array of {option, reason} | Yes (for types with distractors) | One reason per incorrect option, naming the misconception it represents. | `authoring_guidelines.md`, "Explanation Writing Rules" |
| `related_knowledge_areas` | Array of KA codes | Yes (at least the primary KA) | Every Knowledge Area this question meaningfully touches, primary first. | `taxonomy.md`, "Cross-Knowledge-Area Tagging" |
| `related_flashcards` | Array of strings | Optional | Term(s) from the source module's Flashcards section (Section 12) this question reinforces. | `architecture.md`, "Flashcard System" |
| `related_exercises` | Array of strings | Optional | Practical Exercise(s) (Section 11 of the source module) this question relates to. | — |
| `references` | Array of strings | Yes | Specific `knowledge_base/*.md` file + section citations (e.g., `data_governance.md, Section 3, Data Owner`), plus DMBOK2 chapter reference. | `question_quality_standards.md`, Standard 8 |
| `source_confidence` | Enum: High / Medium / Low | Yes | See "Source Confidence" below. | `research/source_map.md` |
| `review_status` | Enum: matches `question_lifecycle.md` states | Yes | Current lifecycle state. | `question_lifecycle.md` |
| `approval_status` | Enum: Pending / Approved / Rejected | Yes | Distinct from `review_status` — tracks the Approval gate specifically (a question can be past both reviews but still Pending Approval). | `question_lifecycle.md`, "Approval" |
| `author` | String | Yes | Who drafted the question. | `review_process.md` |
| `reviewer` | Array of strings | Yes (once past Draft) | Who performed Technical Review and DAMA Review (may be the same identity in a single-author context — see `review_process.md`). | `review_process.md` |
| `creation_date` | Date (ISO 8601) | Yes | Date the question record was first created. | `versioning.md` |
| `last_modified` | Date (ISO 8601) | Yes | Date of the most recent edit, at any version. | `versioning.md` |

## Source Confidence

Distinct from `dama_concept`/`industry_practice_concept` tagging — this field expresses how strongly the question's content is anchored to primary sourcing, per `research/source_map.md`'s priority tiers:

| Value | Meaning |
|---|---|
| **High** | Directly traceable to a `[DAMA]`-tagged claim in an Approved `knowledge_base/` module, itself sourced from DMBOK2 Ch. text. |
| **Medium** | DAMA-consistent and cross-checked, but resting on a paraphrase-only or uncertain-enumeration point the source module itself flagged (e.g., MDM style naming variance in `reference_and_master_data.md`). |
| **Low** | Tests an `[Industry Practice]`-tagged concept — illustrative and realistic, but not itself DMBOK2-authoritative content; used sparingly and never for a Mock Exam's core scoring content. |

## Type-Specific Answer Structures

`answer_choices` and `correct_answer` are shaped differently per `question_type`. This is a conceptual (not implementation-bound) definition of that shape:

| `question_type` | `answer_choices` shape | `correct_answer` shape |
|---|---|---|
| Multiple Choice | List of 3–5 labeled options | The single correct option's label |
| Multiple Select | List of options | The set of correct option labels |
| True/False | Implicit (True, False) | `True` or `False` |
| Scenario-Based | Same as Multiple Choice/Select, presented after the scenario `stem` | Same as Multiple Choice/Select |
| Matching | Two labeled lists (left set, right set) | The correct left→right pairing |
| Ordering | An unordered list of items | The correct sequence |
| Mini Case Study | A list of sub-questions, each with its own `answer_choices` (of any of the above shapes) | A list of correct answers, one per sub-question |

## Illustrative Schema Shape (structure only — not a real question)

The block below shows the *shape* of a question record using placeholder values in every content field. It is not exam content and must not be treated as a starting draft for a real question (`authoring_guidelines.md`, "What Not to Author").

```yaml
question_id: "GOV-000"              # placeholder ID, not assigned
version: "1.0"
knowledge_area: "GOV"
topic: "[topic from taxonomy.md]"
subtopic: "[subtopic from taxonomy.md]"
difficulty: "[Beginner|Intermediate|Advanced|Expert]"
blooms_level: "[Remember|Understand|Apply|Analyze|Evaluate|Create]"
learning_objective: "[one sentence — what correct recall/application demonstrates]"
dama_concept: "[DAMA-tagged concept name, or null]"
industry_practice_concept: "[Industry-Practice-tagged concept name, or null]"
keywords: ["[term]", "[term]"]
estimated_solving_time: 0            # seconds, placeholder
question_type: "[one of the seven types]"
stem: "[question text — placeholder, not a real question]"
answer_choices: []                   # shape depends on question_type
correct_answer: null                 # shape depends on question_type
explanation: "[placeholder]"
why_incorrect: []                    # one entry per distractor
related_knowledge_areas: ["GOV"]
related_flashcards: []
related_exercises: []
references: ["knowledge_base/data_governance.md, Section X"]
source_confidence: "[High|Medium|Low]"
review_status: "Draft"
approval_status: "Pending"
author: "[name]"
reviewer: []
creation_date: "[YYYY-MM-DD]"
last_modified: "[YYYY-MM-DD]"
```

## Versioning-Related Metadata (system-managed, not author-provided)

Two additional fields are maintained automatically by the versioning process described in `versioning.md`, rather than filled in by the author: `supersedes` (the `question_id` + `version` this record replaces, if any) and `superseded_by` (the reverse link, populated once a newer version exists). They are documented here for completeness but are not part of the author-facing schema above — see `versioning.md` for their full behavior.
