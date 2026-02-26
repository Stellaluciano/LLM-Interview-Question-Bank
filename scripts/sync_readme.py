#!/usr/bin/env python3
"""Generate README.md from QUESTION_BANK.md with project introduction."""
from pathlib import Path

INTRO = """# LLM Interview Question Bank

An original, community-driven repository of interview questions for modern LLM engineering.
It is designed for realistic hiring loops and technical screen preparation.
The source of truth is `QUESTION_BANK.md`, while `README.md` is generated for discoverability.
Questions emphasize tradeoffs, debugging strategy, production constraints, and safety thinking.
Contributors are expected to add fully original content using the required strict template.
Automated checks in CI enforce formatting consistency and structural correctness.

"""

bank_path = Path("QUESTION_BANK.md")
readme_path = Path("README.md")

bank_lines = bank_path.read_text(encoding="utf-8").splitlines()
if bank_lines and bank_lines[0].startswith("# "):
    bank_lines = bank_lines[2:] if len(bank_lines) > 1 and bank_lines[1] == "" else bank_lines[1:]

content = INTRO + "\n".join(bank_lines).lstrip("\n") + "\n"
readme_path.write_text(content, encoding="utf-8")
print("README.md synced from QUESTION_BANK.md")
