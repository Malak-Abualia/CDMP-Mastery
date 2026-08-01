"""Command-line entry point: `python -m quiz_engine`.

Implements v0.1 of quiz_engine/cli_design.md: a thin client that loads
questions, starts a quiz (random / Knowledge-Area-filtered /
difficulty-filtered), presents questions in the terminal, collects
answers, evaluates them immediately, and prints an end-of-session score
report. Read-only with respect to question_bank/ -- this module never
writes to it.
"""

from __future__ import annotations

import argparse
import random
import sys
from pathlib import Path
from typing import List, Optional

from ..engine.selection import build_quiz
from ..loader.yaml_loader import DEFAULT_ALLOWED_STATUSES, load_questions
from ..models.question import Question
from ..scoring.evaluation import evaluate_answer
from ..scoring.scorer import score_results
from ..utils.exceptions import NoQuestionsAvailableError
from ..utils.ka_mapping import CODE_TO_FOLDER, FOLDER_TO_CODE, resolve_ka_code
from ..utils.paths import default_question_bank_path

DEV_WARNING = "[DEV/UNREVIEWED CONTENT -- not validated study material]"


def _ensure_utf8_console() -> None:
    """Best-effort: avoid mangled output (e.g. em dashes) on Windows consoles.

    Windows terminals commonly default stdout/stderr to a legacy codepage
    (e.g. cp1252), which cannot represent characters question text may
    contain (em dashes, curly quotes). `reconfigure` is only available on
    real text streams (Python 3.7+); this is a no-op if stdout/stderr has
    already been redirected to something that doesn't support it.
    """
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            try:
                reconfigure(encoding="utf-8")
            except (ValueError, OSError):
                pass


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="quiz_engine",
        description=(
            "CDMP Mastery Quiz Engine (v0.1) -- a terminal practice quiz over "
            "question_bank/questions/."
        ),
    )
    parser.add_argument(
        "--ka",
        dest="knowledge_area",
        default=None,
        help="Filter to one Knowledge Area, by folder name (e.g. data_quality) or code (e.g. QUAL).",
    )
    parser.add_argument(
        "--difficulty",
        dest="difficulty",
        default=None,
        choices=["Beginner", "Intermediate", "Advanced", "Expert"],
        help="Filter to one difficulty tier.",
    )
    parser.add_argument(
        "--count",
        dest="count",
        type=int,
        default=10,
        help="Number of questions to include (default: 10).",
    )
    parser.add_argument(
        "--questions-path",
        dest="questions_path",
        default=None,
        help="Override path to question_bank/questions/ (default: auto-detected).",
    )
    parser.add_argument(
        "--seed",
        dest="seed",
        type=int,
        default=None,
        help="Random seed for reproducible question selection (mainly for testing).",
    )
    parser.add_argument(
        "--dev-unreviewed",
        dest="dev_unreviewed",
        action="store_true",
        help=(
            "Include unreviewed ('Draft') questions. NOT for real study use -- "
            "see quiz_engine/data_loading.md, 'Lifecycle Filter'. Every question "
            "and the session summary will be marked as unreviewed content."
        ),
    )
    return parser


def _valid_letters(question: Question) -> List[str]:
    """The option letters actually on offer, parsed from `answer_choices`

    e.g. "A) Custodian" -> "A". Used to reject a letter that isn't a real
    option, per quiz_engine/cli_design.md's "Answer Input Conventions".
    """
    return [choice.strip()[0].upper() for choice in question.answer_choices if choice.strip()]


def _prompt_for_answer(question: Question) -> str:
    """Prompt until a syntactically valid answer is given; never guess on bad input.

    Per quiz_engine/cli_design.md, "Answer Input Conventions": invalid
    input (an unrecognized letter, or more than one letter for a
    single-answer question) is rejected with a re-prompt, never silently
    interpreted -- e.g. never arbitrarily picking one letter out of several
    typed by mistake for a single-answer question.
    """
    is_multi = question.is_multi_select
    valid = set(_valid_letters(question))
    prompt = (
        "Your answer (letters, space-separated, e.g. 'A C'): " if is_multi else "Your answer: "
    )
    while True:
        raw = input(prompt).strip()
        if not raw:
            print("Please enter an answer.")
            continue

        letters = [tok.strip().upper() for tok in raw.replace(",", " ").split()]
        if not is_multi and len(letters) > 1:
            print(f"This question has a single correct answer -- enter one letter (e.g. {sorted(valid)[0]}).")
            continue
        unknown = [letter for letter in letters if letter not in valid]
        if unknown:
            print(f"'{', '.join(unknown)}' is not one of the available options ({', '.join(sorted(valid))}).")
            continue

        return raw


def run_quiz(questions: List[Question], dev_unreviewed: bool) -> int:
    """Run an interactive session over `questions`; returns the number correct."""
    results = []
    for index, question in enumerate(questions, start=1):
        print(f"\nQuestion {index} of {len(questions)}  [{question.knowledge_area} | {question.difficulty}]")
        if dev_unreviewed:
            print(DEV_WARNING)
        print(question.stem)
        for choice in question.answer_choices:
            print(f"  {choice}")

        submitted = _prompt_for_answer(question)
        result = evaluate_answer(question, submitted)
        results.append(result)

        print("Correct!" if result.correct else "Incorrect.")
        print(f"Explanation: {question.explanation}")
        if not result.correct and result.incorrect_reasons:
            for reason in result.incorrect_reasons:
                print(f"  - {reason}")
        if question.related_flashcards:
            print(f"Related flashcards: {', '.join(question.related_flashcards)}")
        if question.references:
            print(f"Recommended revision: {question.references[0]}")

    report = score_results(results)
    print("\n" + "=" * 40)
    print("Session Summary")
    print("=" * 40)
    print(f"Score: {report.correct_answers}/{report.total_questions} ({report.percentage}%)")
    print("Knowledge Area breakdown:")
    for ka in sorted(report.ka_breakdown):
        ka_score = report.ka_breakdown[ka]
        print(f"  {ka}: {ka_score.correct}/{ka_score.total} ({ka_score.percentage}%)")
    if dev_unreviewed:
        print(f"\n{DEV_WARNING}")

    return report.correct_answers


def main(argv: Optional[List[str]] = None) -> int:
    _ensure_utf8_console()
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    questions_path = (
        Path(args.questions_path) if args.questions_path else default_question_bank_path()
    )
    allowed_statuses = (
        ("Draft", *DEFAULT_ALLOWED_STATUSES) if args.dev_unreviewed else DEFAULT_ALLOWED_STATUSES
    )

    load_result = load_questions(questions_path, allowed_statuses=allowed_statuses)
    for error in load_result.errors:
        print(f"[load error] {error.path}: {error.reason}", file=sys.stderr)

    if not load_result.questions:
        if not args.dev_unreviewed:
            print(
                "No Published questions found. Phase 1 content is currently all "
                "'Draft' (see research/question_bank_phase1_validation.md) -- pass "
                "--dev-unreviewed to practice with it anyway (unreviewed content, "
                "not yet DAMA-reviewed).",
                file=sys.stderr,
            )
        else:
            print(f"No questions found under {questions_path}.", file=sys.stderr)
        return 1

    ka_code: Optional[str] = None
    if args.knowledge_area:
        try:
            ka_code = resolve_ka_code(args.knowledge_area)
        except KeyError:
            valid = sorted(FOLDER_TO_CODE) + sorted(CODE_TO_FOLDER)
            print(f"Error: unrecognized Knowledge Area '{args.knowledge_area}'.", file=sys.stderr)
            print(f"Valid values: {', '.join(valid)}", file=sys.stderr)
            return 1

    rng = random.Random(args.seed) if args.seed is not None else None

    try:
        quiz_questions = build_quiz(
            load_result.questions,
            count=args.count,
            ka_code=ka_code,
            difficulty=args.difficulty,
            rng=rng,
        )
    except NoQuestionsAvailableError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    run_quiz(quiz_questions, dev_unreviewed=args.dev_unreviewed)
    return 0


if __name__ == "__main__":
    sys.exit(main())
