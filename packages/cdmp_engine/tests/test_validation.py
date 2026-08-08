"""Tests for cdmp_engine.validation: schema validation and the file/field/reason error shape."""

from __future__ import annotations

from cdmp_content_schema import Question
from cdmp_engine.validation import validate_question_record


def test_valid_record_passes_and_parses(question_dict_factory):
    result = validate_question_record(question_dict_factory(), "some/path.yaml")

    assert result.passed is True
    assert result.errors == ()
    assert isinstance(result.question, Question)
    assert result.question.question_id == "TEST-001"


def test_missing_required_field_is_rejected_with_specific_field(question_dict_factory):
    data = question_dict_factory()
    del data["explanation"]

    result = validate_question_record(data, "some/path.yaml")

    assert result.passed is False
    assert result.question is None
    assert any(err.field == "explanation" for err in result.errors)


def test_invalid_enum_value_is_rejected_with_specific_field(question_dict_factory):
    result = validate_question_record(question_dict_factory(difficulty="Impossible"), "some/path.yaml")

    assert result.passed is False
    assert any(err.field == "difficulty" for err in result.errors)


def test_correct_answer_not_among_choices_is_rejected(question_dict_factory):
    result = validate_question_record(question_dict_factory(correct_answer="Z"), "some/path.yaml")

    assert result.passed is False
    assert any("not among" in err.reason for err in result.errors)


def test_multi_select_shape_is_accepted_regardless_of_question_type_label(question_dict_factory):
    """GOV-016's known case: a Scenario-Based-labeled question that is Multiple-Select-shaped."""
    result = validate_question_record(
        question_dict_factory(
            question_type="Scenario-Based",
            correct_answer=["B", "C"],
            why_incorrect=[
                {"option": "A", "reason": "Not a correct option."},
                {"option": "D", "reason": "Not a correct option."},
            ],
        ),
        "some/path.yaml",
    )

    assert result.passed is True
    assert result.question.is_multi_select is True


def test_why_incorrect_option_matching_correct_answer_is_rejected(question_dict_factory):
    result = validate_question_record(
        question_dict_factory(why_incorrect=[{"option": "B", "reason": "This is actually correct."}]),
        "some/path.yaml",
    )

    assert result.passed is False
    assert any("distractor" in err.reason for err in result.errors)


def test_related_knowledge_areas_not_listing_primary_first_is_rejected(question_dict_factory):
    result = validate_question_record(
        question_dict_factory(knowledge_area="GOV", related_knowledge_areas=["META", "GOV"]),
        "some/path.yaml",
    )

    assert result.passed is False
    assert any("related_knowledge_areas" in err.reason for err in result.errors)


def test_reviewer_required_once_past_draft(question_dict_factory):
    result = validate_question_record(
        question_dict_factory(review_status="TechnicalReview", reviewer=[]),
        "some/path.yaml",
    )

    assert result.passed is False
    assert any("reviewer" in err.reason for err in result.errors)


def test_draft_status_does_not_require_reviewer(question_dict_factory):
    result = validate_question_record(
        question_dict_factory(review_status="Draft", approval_status="Pending", reviewer=[]),
        "some/path.yaml",
    )

    assert result.passed is True


def test_last_modified_before_creation_date_is_rejected(question_dict_factory):
    result = validate_question_record(
        question_dict_factory(creation_date="2026-08-01", last_modified="2026-07-01"),
        "some/path.yaml",
    )

    assert result.passed is False
    assert any("last_modified" in err.reason for err in result.errors)


def test_warns_when_neither_dama_nor_industry_concept_populated(question_dict_factory):
    result = validate_question_record(
        question_dict_factory(dama_concept=None, industry_practice_concept=None),
        "some/path.yaml",
    )

    assert result.passed is True
    assert any("dama_concept" in warning for warning in result.warnings)


def test_valid_record_has_no_warnings_by_default(question_dict_factory):
    result = validate_question_record(question_dict_factory(), "some/path.yaml")

    assert result.warnings == ()
