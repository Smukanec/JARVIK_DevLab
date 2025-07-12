"""Utility helpers for the DevLab package."""

from __future__ import annotations

import re


def detect_language(prompt: str) -> str:
    """Very small heuristic to guess the programming language in *prompt*.

    The function looks for common keywords or code fragments and returns one
    of ``"python"``, ``"html"``, ``"php"``, ``"json"``, ``"c"``, ``"sql`` or
    ``"text"`` (default).
    """
    if not prompt:
        return "text"
    lowered = prompt.lower()
    if "<?php" in lowered or re.search(r"\bphp\b", lowered):
        return "php"
    if "<html" in lowered or "</html>" in lowered:
        return "html"
    if re.search(r"\bjson\b", lowered) or lowered.strip().startswith("{"):
        return "json"
    if "python" in lowered or re.search(r"\bdef\b", lowered) or "import " in lowered:
        return "python"
    if "sql" in lowered:
        return "sql"
    if re.search(r"\b#include\b|int main", lowered):
        return "c"
    return "text"
