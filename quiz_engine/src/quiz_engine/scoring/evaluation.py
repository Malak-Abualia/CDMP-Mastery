"""Answer evaluation: grades a submitted answer against a Question's correct_answer.

Core rule (quiz_engine/answer_evaluation.md, "Evaluate by Shape, Not by
Label"): grading branches on whether `question.correct_answer` is a
string or a list -- never on `question_type`. This matters concretely:
research/question_bank_audit.md documents that GOV-016 is labeled
`question_type: "Scenario-Based"` but carries a list-shaped
`correct_answer`. Branching on the label instead of the shape would
silently misgrade it and any future question authored the same way.
"""

from __future__ import annotations

from typing import List, Sequence, Set, Union

from ..models.question import Question
from ..models.results import AnswerResult

Answer = Union[str, Sequence[str]]


def _to_letter_set(value: Answer) -> Set[str]:
    if isinstance(value, str):
        return {part.strip().upper() for part in value.replace(",", " ").split() if part.strip()}
    return {str(part).strip().upper() for part in value}


def _reasons_for(question: Question, wrongly_included: Set[str], missed: Set[str]) -> List[str]:
    by_option = {w.option.strip().upper(): w.reason for w in question.why_incorrect}
    reasons: List[str] = []
    for letter in sorted(wrongly_included):
        if letter in by_option:
            reasons.append(f"{letter}: {by_option[letter]}")
    for letter in sorted(missed):
        reasons.append(f"{letter}: correct option not selected")
    return reasons


def evaluate_answer(question: Question, submitted: Answer) -> AnswerResult:
    """Grade one submitted answer against `question`.

    `submitted` may be a single letter string (e.g. "B"), a
    space/comma-separated string of letters (e.g. "A C"), or a list of
    letters -- accepted uniformly for both single-answer and
    multiple-select questions.
    """
    if question.is_multi_select:
        correct_set = _to_letter_set(question.correct_answer)
        submitted_set = _to_letter_set(submitted)
        is_correct = submitted_set == correct_set
        incorrect_reasons = (
            []
            if is_correct
            else _reasons_for(
                question,
                wrongly_included=submitted_set - correct_set,
                missed=correct_set - submitted_set,
            )
        )
        submitted_repr: Union[str, List[str]] = sorted(submitted_set)
    else:
        correct_letter = str(question.correct_answer).strip().upper()
        submitted_letters = _to_letter_set(submitted)
        submitted_letter = next(iter(submitted_letters)) if submitted_letters else ""
        is_correct = submitted_letter == correct_letter
        incorrect_reasons = (
            []
            if is_correct
            else _reasons_for(question, wrongly_included={submitted_letter}, missed=set())
        )
        submitted_repr = submitted_letter

    return AnswerResult(
        question_id=question.question_id,
        version=question.version,
        knowledge_area=question.knowledge_area,
        correct=is_correct,
        submitted_answer=submitted_repr,
        correct_answer=question.correct_answer,
        incorrect_reasons=incorrect_reasons,
    )
