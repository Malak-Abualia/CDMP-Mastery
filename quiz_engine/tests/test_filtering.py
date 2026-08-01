"""Tests for quiz_engine.engine.selection: random/KA/difficulty selection and composability."""

from __future__ import annotations

import random

import pytest

from quiz_engine.engine.selection import (
    build_quiz,
    filter_by_difficulty,
    filter_by_knowledge_area,
    select_random,
)
from quiz_engine.loader.yaml_loader import build_question
from quiz_engine.utils.exceptions import NoQuestionsAvailableError


def _question(question_dict_factory, **overrides):
    return build_question(question_dict_factory(**overrides), source_path="<test>")


def test_filter_by_knowledge_area(question_dict_factory):
    gov = _question(question_dict_factory, question_id="G1", knowledge_area="GOV")
    qual = _question(question_dict_factory, question_id="Q1", knowledge_area="QUAL")

    result = filter_by_knowledge_area([gov, qual], "QUAL")

    assert result == [qual]


def test_filter_by_difficulty_is_case_insensitive(question_dict_factory):
    beginner = _question(question_dict_factory, question_id="B1", difficulty="Beginner")
    advanced = _question(question_dict_factory, question_id="A1", difficulty="Advanced")

    result = filter_by_difficulty([beginner, advanced], "beginner")

    assert result == [beginner]


def test_select_random_respects_count_and_has_no_repeats(question_dict_factory):
    questions = [_question(question_dict_factory, question_id=f"Q{i}") for i in range(5)]

    picked = select_random(questions, count=3, rng=random.Random(42))

    assert len(picked) == 3
    assert len({q.question_id for q in picked}) == 3


def test_select_random_returns_whole_pool_if_count_exceeds_pool_size(question_dict_factory):
    questions = [_question(question_dict_factory, question_id=f"Q{i}") for i in range(3)]

    picked = select_random(questions, count=10, rng=random.Random(1))

    assert len(picked) == 3


def test_select_random_raises_when_pool_empty():
    with pytest.raises(NoQuestionsAvailableError):
        select_random([], count=5)


def test_build_quiz_composes_ka_and_difficulty_filters(question_dict_factory):
    match = _question(question_dict_factory, question_id="M1", knowledge_area="GOV", difficulty="Advanced")
    wrong_ka = _question(question_dict_factory, question_id="W1", knowledge_area="QUAL", difficulty="Advanced")
    wrong_difficulty = _question(question_dict_factory, question_id="W2", knowledge_area="GOV", difficulty="Beginner")

    result = build_quiz(
        [match, wrong_ka, wrong_difficulty], count=10, ka_code="GOV", difficulty="Advanced"
    )

    assert result == [match]


def test_build_quiz_raises_clear_error_when_no_match(question_dict_factory):
    question = _question(question_dict_factory, question_id="Q1", knowledge_area="GOV")

    with pytest.raises(NoQuestionsAvailableError, match="knowledge_area=QUAL"):
        build_quiz([question], count=5, ka_code="QUAL")


def test_build_quiz_with_no_filters_draws_from_entire_pool(question_dict_factory):
    questions = [
        _question(question_dict_factory, question_id="A", knowledge_area="GOV"),
        _question(question_dict_factory, question_id="B", knowledge_area="QUAL"),
    ]

    result = build_quiz(questions, count=10)

    assert {q.question_id for q in result} == {"A", "B"}
