"""Schema validation for raw question dictionaries.

Mirrors the required fields and controlled-value ("enum") fields defined
in question_bank/metadata_schema.md. Validation failures are collected
and returned as a list rather than raised one at a time, so a caller can
report every problem with a record in a single pass -- consistent with
quiz_engine/data_loading.md's "Schema Validation" step, which is meant to
reject a bad record with a specific, complete reason, not a first-error-only
message.
"""

from __future__ import annotations

from typing import Any, Dict, List

# Fields that must always be present with a non-empty/meaningful value.
REQUIRED_FIELDS = [
    "question_id",
    "version",
    "knowledge_area",
    "topic",
    "subtopic",
    "difficulty",
    "blooms_level",
    "learning_objective",
    "keywords",
    "estimated_solving_time",
    "question_type",
    "stem",
    "answer_choices",
    "correct_answer",
    "explanation",
    "why_incorrect",
    "related_knowledge_areas",
    "references",
    "source_confidence",
    "review_status",
    "approval_status",
    "author",
    "creation_date",
    "last_modified",
]

# Fields that must be present as a key, but may legitimately hold null
# (dama_concept / industry_practice_concept: exactly one is often null by
# design, per question_bank/metadata_schema.md) or an empty list.
NULLABLE_FIELDS = ["dama_concept", "industry_practice_concept", "reviewer"]
OPTIONAL_LIST_FIELDS = ["related_flashcards", "related_exercises"]

VALID_DIFFICULTIES = {"Beginner", "Intermediate", "Advanced", "Expert"}
VALID_BLOOMS_LEVELS = {"Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create"}
VALID_QUESTION_TYPES = {
    "Multiple Choice",
    "Multiple Select",
    "True/False",
    "Scenario-Based",
    "Matching",
    "Ordering",
    "Mini Case Study",
}
VALID_SOURCE_CONFIDENCE = {"High", "Medium", "Low"}
VALID_REVIEW_STATUS = {
    "Draft",
    "TechnicalReview",
    "DAMAReview",
    "Approval",
    "Published",
    "Retired",
}
VALID_APPROVAL_STATUS = {"Pending", "Approved", "Rejected"}


def validate_question_dict(data: Dict[str, Any]) -> List[str]:
    """Validate a raw parsed-YAML question record.

    Returns a list of human-readable error strings; an empty list means
    the record is valid.
    """
    errors: List[str] = []

    for field_name in REQUIRED_FIELDS:
        if field_name not in data:
            errors.append(f"missing required field '{field_name}'")

    for field_name in NULLABLE_FIELDS + OPTIONAL_LIST_FIELDS:
        if field_name not in data:
            errors.append(f"missing required field '{field_name}' (key must exist, value may be null/empty)")

    if errors:
        # Shape/enum checks below assume the fields they inspect exist.
        return errors

    if data["difficulty"] not in VALID_DIFFICULTIES:
        errors.append(f"invalid difficulty '{data['difficulty']}'")
    if data["blooms_level"] not in VALID_BLOOMS_LEVELS:
        errors.append(f"invalid blooms_level '{data['blooms_level']}'")
    if data["question_type"] not in VALID_QUESTION_TYPES:
        errors.append(f"invalid question_type '{data['question_type']}'")
    if data["source_confidence"] not in VALID_SOURCE_CONFIDENCE:
        errors.append(f"invalid source_confidence '{data['source_confidence']}'")
    if data["review_status"] not in VALID_REVIEW_STATUS:
        errors.append(f"invalid review_status '{data['review_status']}'")
    if data["approval_status"] not in VALID_APPROVAL_STATUS:
        errors.append(f"invalid approval_status '{data['approval_status']}'")

    if not isinstance(data["answer_choices"], list) or not data["answer_choices"]:
        errors.append("'answer_choices' must be a non-empty list")

    correct_answer = data["correct_answer"]
    if not isinstance(correct_answer, (str, list)):
        errors.append("'correct_answer' must be a string or a list of strings")
    elif isinstance(correct_answer, list):
        if not correct_answer or not all(isinstance(x, str) for x in correct_answer):
            errors.append("'correct_answer' list must be non-empty and contain only strings")

    if not isinstance(data["why_incorrect"], list):
        errors.append("'why_incorrect' must be a list")
    else:
        for entry in data["why_incorrect"]:
            if not isinstance(entry, dict) or "option" not in entry or "reason" not in entry:
                errors.append("each 'why_incorrect' entry must be a mapping with 'option' and 'reason'")
                break

    if not isinstance(data["keywords"], list):
        errors.append("'keywords' must be a list")

    if not isinstance(data["estimated_solving_time"], int):
        errors.append("'estimated_solving_time' must be an integer (seconds)")

    return errors
