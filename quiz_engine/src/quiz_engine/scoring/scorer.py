"""Aggregates AnswerResults into a ScoreReport: totals, percentage, KA breakdown.

Implements quiz_engine/scoring_engine.md sections 1-3 (Raw Score,
Percentage, Knowledge Area Score). Sections 4-5 (Difficulty Adjustment,
Readiness Indicator) are deferred to quiz_engine/roadmap.md Phase B, since
they depend on persisted session history this v0.1 does not yet have.
"""

from __future__ import annotations

from typing import Dict, Sequence

from ..models.results import AnswerResult, KAScore, ScoreReport


def score_results(results: Sequence[AnswerResult]) -> ScoreReport:
    """Compute a session's Raw Score, Percentage, and Knowledge Area breakdown."""
    total = len(results)
    correct = sum(1 for r in results if r.correct)
    percentage = round((correct / total) * 100, 1) if total else 0.0

    ka_breakdown: Dict[str, KAScore] = {}
    for result in results:
        ka_score = ka_breakdown.setdefault(
            result.knowledge_area,
            KAScore(knowledge_area=result.knowledge_area, correct=0, total=0),
        )
        ka_score.total += 1
        if result.correct:
            ka_score.correct += 1

    return ScoreReport(
        total_questions=total,
        correct_answers=correct,
        percentage=percentage,
        ka_breakdown=ka_breakdown,
    )
