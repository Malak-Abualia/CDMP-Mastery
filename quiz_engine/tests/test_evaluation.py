"""Tests for quiz_engine.scoring.evaluation: single-answer and multi-select grading.

Per quiz_engine/answer_evaluation.md, grading must branch on the SHAPE of
correct_answer, not on question_type -- test_evaluation_uses_answer_shape_
not_question_type_label below deliberately mirrors the real GOV-016 case
documented in research/question_bank_audit.md (a Scenario-Based question
with a multi-select-shaped answer) to prove the engine actually obeys
that rule, not just the label.
"""

from __future__ import annotations

from quiz_engine.loader.yaml_loader import build_question
from quiz_engine.scoring.evaluation import evaluate_answer


def _question(question_dict_factory, **overrides):
    return build_question(question_dict_factory(**overrides), source_path="<test>")


def test_single_answer_correct(question_dict_factory):
    question = _question(question_dict_factory, correct_answer="B")

    result = evaluate_answer(question, "B")

    assert result.correct is True
    assert result.incorrect_reasons == []


def test_single_answer_incorrect_reports_the_specific_distractor_reason(question_dict_factory):
    question = _question(question_dict_factory, correct_answer="B")

    result = evaluate_answer(question, "A")

    assert result.correct is False
    assert len(result.incorrect_reasons) == 1
    assert "Custodian implements" in result.incorrect_reasons[0]


def test_single_answer_is_case_insensitive_and_trims_whitespace(question_dict_factory):
    question = _question(question_dict_factory, correct_answer="B")

    assert evaluate_answer(question, "b").correct is True
    assert evaluate_answer(question, "  B  ").correct is True


def test_multi_select_exact_match_is_correct(question_dict_factory):
    question = _question(
        question_dict_factory,
        question_type="Multiple Select",
        correct_answer=["A", "C"],
        answer_choices=["A) x", "B) y", "C) z", "D) w"],
        why_incorrect=[{"option": "B", "reason": "b is wrong"}, {"option": "D", "reason": "d is wrong"}],
    )

    result = evaluate_answer(question, ["A", "C"])

    assert result.correct is True


def test_multi_select_accepts_space_separated_string_input(question_dict_factory):
    question = _question(
        question_dict_factory,
        question_type="Multiple Select",
        correct_answer=["A", "C"],
    )

    result = evaluate_answer(question, "A C")

    assert result.correct is True


def test_multi_select_partial_match_is_incorrect_all_or_nothing(question_dict_factory):
    question = _question(question_dict_factory, question_type="Multiple Select", correct_answer=["A", "C"])

    result = evaluate_answer(question, ["A"])

    assert result.correct is False


def test_multi_select_extra_option_is_incorrect(question_dict_factory):
    question = _question(question_dict_factory, question_type="Multiple Select", correct_answer=["A", "C"])

    result = evaluate_answer(question, ["A", "C", "D"])

    assert result.correct is False


def test_multi_select_wrong_answer_reports_reasons_for_wrongly_included_and_missed(question_dict_factory):
    question = _question(
        question_dict_factory,
        question_type="Multiple Select",
        correct_answer=["A", "C"],
        why_incorrect=[{"option": "D", "reason": "d is a distractor"}],
    )

    result = evaluate_answer(question, ["A", "D"])

    assert result.correct is False
    joined = " ".join(result.incorrect_reasons)
    assert "D: d is a distractor" in joined
    assert "C: correct option not selected" in joined


def test_evaluation_uses_answer_shape_not_question_type_label(question_dict_factory):
    """Mirrors GOV-016: question_type is Scenario-Based, but correct_answer is a list."""
    question = _question(
        question_dict_factory,
        question_id="GOV-016-LIKE",
        question_type="Scenario-Based",
        correct_answer=["A", "B", "D"],
        answer_choices=["A) x", "B) y", "C) z", "D) w"],
        why_incorrect=[{"option": "C", "reason": "c is wrong"}],
    )

    assert question.is_multi_select is True
    assert evaluate_answer(question, ["A", "B", "D"]).correct is True
    assert evaluate_answer(question, ["A", "B"]).correct is False
