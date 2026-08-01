"""Path resolution helpers."""

from __future__ import annotations

from pathlib import Path


def default_question_bank_path() -> Path:
    """Best-effort resolution of question_bank/questions/.

    Walks up from this file's location looking for a `question_bank/questions`
    directory, so the CLI works whether invoked from the repo root, from
    inside quiz_engine/, or after the package is installed elsewhere
    alongside the project. Falls back to a path relative to the current
    working directory if no match is found while walking up.
    """
    here = Path(__file__).resolve()
    for parent in here.parents:
        candidate = parent / "question_bank" / "questions"
        if candidate.is_dir():
            return candidate
    return Path.cwd() / "question_bank" / "questions"
