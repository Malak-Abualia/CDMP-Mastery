"""Tests for quiz_engine.scoring.scorer: totals, percentage, Knowledge Area breakdown."""

from __future__ import annotations

from quiz_engine.models.results import AnswerResult
from quiz_engine.scoring.scorer import score_results


def _result(ka: str, correct: bool, qid: str = "Q1") -> AnswerResult:
    return AnswerResult(
        question_id=qid,
        version="1.0",
        knowledge_area=ka,
        correct=correct,
        submitted_answer="A",
        correct_answer="A",
    )


def test_score_results_totals_and_percentage():
    results = [_result("GOV", True), _result("GOV", False), _result("QUAL", True), _result("QUAL", True)]

    report = score_results(results)

    assert report.total_questions == 4
    assert report.correct_answers == 3
    assert report.percentage == 75.0


def test_score_results_ka_breakdown():
    results = [_result("GOV", True), _result("GOV", False), _result("QUAL", True)]

    report = score_results(results)

    assert report.ka_breakdown["GOV"].correct == 1
    assert report.ka_breakdown["GOV"].total == 2
    assert report.ka_breakdown["GOV"].percentage == 50.0
    assert report.ka_breakdown["QUAL"].correct == 1
    assert report.ka_breakdown["QUAL"].total == 1
    assert report.ka_breakdown["QUAL"].percentage == 100.0


def test_score_results_empty_input_does_not_divide_by_zero():
    report = score_results([])

    assert report.total_questions == 0
    assert report.correct_answers == 0
    assert report.percentage == 0.0
    assert report.ka_breakdown == {}


def test_score_results_all_correct_is_100_percent():
    results = [_result("GOV", True), _result("GOV", True)]

    report = score_results(results)

    assert report.percentage == 100.0
