#!/usr/bin/env python3
"""Validate QUESTION_BANK.md structure and required fields."""
from __future__ import annotations

import re
import sys
from pathlib import Path

BANK_PATH = Path("QUESTION_BANK.md")
ALLOWED_DIFFICULTY = {"Easy", "Medium", "Hard"}
QUESTION_HEADER = re.compile(r"^### Q: .+")
REQUIRED_SECTIONS = [
    "Foundations of LLMs",
    "Training & Alignment",
    "Inference & Systems Engineering",
    "Retrieval, Agents & Tool Use",
    "Evaluation & Safety",
    "Real-World Engineering & Debugging",
    "System Design Scenarios",
]

FIELD_PATTERNS = {
    "difficulty": re.compile(r"^\*\*Difficulty:\*\*\s*(Easy|Medium|Hard)\s{2}$"),
    "tags": re.compile(r"^\*\*Tags:\*\*\s*(.+?)\s{2}$"),
    "question": re.compile(r"^\*\*Question:\*\*\s*(.+?)\s{2}$"),
    "strong": re.compile(r"^\*\*What a strong answer includes:\*\*$"),
    "pitfalls": re.compile(r"^\*\*Common pitfalls:\*\*$"),
}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


def validate_question_block(lines: list[str], start: int) -> int:
    i = start
    if not QUESTION_HEADER.match(lines[i]):
        fail(f"Line {i+1}: Question header must match '### Q: <title>'.")

    expected_order = ["difficulty", "tags", "question", "strong"]
    i += 1
    if i >= len(lines) or lines[i] != "":
        fail(f"Line {i+1}: Expected blank line after question header.")
    i += 1

    for field in expected_order:
        if i >= len(lines) or not FIELD_PATTERNS[field].match(lines[i]):
            fail(f"Line {i+1}: Invalid or missing {field} field.")
        if field == "difficulty":
            difficulty = FIELD_PATTERNS['difficulty'].match(lines[i]).group(1)
            if difficulty not in ALLOWED_DIFFICULTY:
                fail(f"Line {i+1}: Difficulty must be one of {sorted(ALLOWED_DIFFICULTY)}.")
        if field == "tags":
            tags = FIELD_PATTERNS['tags'].match(lines[i]).group(1).strip()
            if not tags or all(not t.strip() for t in tags.split(",")):
                fail(f"Line {i+1}: Tags must be non-empty comma-separated values.")
        i += 1

    if i < len(lines) and lines[i] == "":
        i += 1

    for bullet_idx in range(3):
        if i >= len(lines) or not lines[i].startswith("- "):
            fail(f"Line {i+1}: Missing bullet {bullet_idx+1} under strong answer section.")
        i += 1

    if i >= len(lines) or not FIELD_PATTERNS["pitfalls"].match(lines[i]):
        fail(f"Line {i+1}: Missing 'Common pitfalls' section.")
    i += 1

    if i < len(lines) and lines[i] == "":
        i += 1

    for bullet_idx in range(2):
        if i >= len(lines) or not lines[i].startswith("- "):
            fail(f"Line {i+1}: Missing bullet {bullet_idx+1} under common pitfalls section.")
        i += 1

    if i < len(lines) and lines[i] != "":
        fail(f"Line {i+1}: Expected blank line after question block.")
    return i


def main() -> None:
    if not BANK_PATH.exists():
        fail("QUESTION_BANK.md does not exist.")

    lines = BANK_PATH.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "# LLM Interview Question Bank":
        fail("QUESTION_BANK.md must start with '# LLM Interview Question Bank'.")

    # ensure required top-level sections exist
    for section in REQUIRED_SECTIONS:
        if f"## {section}" not in lines:
            fail(f"Missing required section: {section}")

    question_count = 0
    seen_titles: set[str] = set()
    i = 0
    while i < len(lines):
        if QUESTION_HEADER.match(lines[i]):
            question_count += 1
            title = lines[i][7:].strip().lower()
            if title in seen_titles:
                fail(f"Duplicate question title detected at line {i+1}: {lines[i][7:].strip()}")
            seen_titles.add(title)
            i = validate_question_block(lines, i)
        i += 1

    if question_count < 80 or question_count > 120:
        fail(f"Question count must be between 80 and 120; found {question_count}.")

    print(f"Validation successful: {question_count} questions found.")


if __name__ == "__main__":
    main()
