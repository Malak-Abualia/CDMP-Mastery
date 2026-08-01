"""Question selection: random, Knowledge-Area-filtered, and difficulty-filtered.

Implements the slice of quiz_engine/question_selection.md needed for v0.1:
filter, then sample. No anti-repetition across sessions, no exam-weighted
sampling, no Weakness Mode -- those depend on persisted session history,
which does not exist yet (see quiz_engine/roadmap.md, Phase B).
"""

from __future__ import annotations

import random
from typing import List, Optional, Sequence

from ..models.question import Question
from ..utils.exceptions import NoQuestionsAvailableError


def select_random(
    questions: Sequence[Question],
    count: int,
    rng: Optional[random.Random] = None,
) -> List[Question]:
    """Pick up to `count` questions at random, with no repeats within the draw."""
    if not questions:
        raise NoQuestionsAvailableError("no questions available to select from")
    generator = rng or random.Random()
    pool = list(questions)
    generator.shuffle(pool)
    return pool[:count]


def filter_by_knowledge_area(questions: Sequence[Question], ka_code: str) -> List[Question]:
    """Filter to questions whose `knowledge_area` matches `ka_code` exactly."""
    return [q for q in questions if q.knowledge_area == ka_code]


def filter_by_difficulty(questions: Sequence[Question], difficulty: str) -> List[Question]:
    """Filter to questions at the given difficulty tier (case-insensitive)."""
    target = difficulty.strip().lower()
    return [q for q in questions if q.difficulty.strip().lower() == target]


def build_quiz(
    questions: Sequence[Question],
    count: int,
    ka_code: Optional[str] = None,
    difficulty: Optional[str] = None,
    rng: Optional[random.Random] = None,
) -> List[Question]:
    """Select a quiz's worth of questions, applying optional KA/difficulty filters.

    Knowledge Area and Difficulty filters are composable -- both may be
    supplied together (quiz_engine/quiz_modes.md's "Composability note").
    Raises NoQuestionsAvailableError, naming the applied filters, if the
    resulting pool is empty.
    """
    pool: Sequence[Question] = questions
    if ka_code:
        pool = filter_by_knowledge_area(pool, ka_code)
    if difficulty:
        pool = filter_by_difficulty(pool, difficulty)

    if not pool:
        applied = []
        if ka_code:
            applied.append(f"knowledge_area={ka_code}")
        if difficulty:
            applied.append(f"difficulty={difficulty}")
        scope = f" matching {', '.join(applied)}" if applied else ""
        raise NoQuestionsAvailableError(f"no questions available{scope}")

    return select_random(pool, count, rng=rng)
