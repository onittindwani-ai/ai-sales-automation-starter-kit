#!/usr/bin/env python3
"""Checks the AI Sales Automation Starter Kit for broken links and unsafe content.

Run from anywhere:

    python3 tests/check_kit.py

Checks:
1. Every required file exists.
2. Every relative Markdown link points to a file or folder that exists.
3. No long dash characters (em dash, en dash and similar) in any text file.
4. No secrets, API keys, tokens or private keys.
5. No email addresses.
6. No private identifiers (kept as SHA-256 hashes so this file does not reveal them).
7. Every prompt file has the required sections and at least one code block.
8. The README has the board placeholder and the credits line.

Exit code 0 means every check passed. Exit code 1 means at least one failed.
No third party packages needed. Works on Python 3.9 and newer.
"""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "README.md",
    "01-THE-8-STEP-PATH.md",
    "02-OUR-TOOL-STACK.md",
    "03-SYSTEM-MAP.md",
    "04-GLOSSARY.md",
    "05-COMPLIANCE-BASICS.md",
    "LICENSE",
    "CHANGELOG.md",
    ".github/workflows/check.yml",
    "prompts/README.md",
    "prompts/00-LEARN-THE-BASICS.md",
    "prompts/01-FIND-YOUR-MONEY-PROBLEM.md",
    "prompts/02-DOCUMENT-YOUR-MANUAL-PROCESS.md",
    "prompts/03-SET-UP-A-PROJECT-IN-CLAUDE-CODE.md",
    "prompts/04-AI-VOICE-CALLER-SYSTEM-PROMPT.md",
    "prompts/05-POST-CALL-ANALYSIS.md",
    "prompts/06-CLAUDE-CODE-BUILD-SPEC.md",
    "prompts/07-MULTI-CHANNEL-FOLLOW-UP.md",
    "prompts/08-PRODUCTION-CHECKLIST-AND-TEST-PLAN.md",
    "templates/README.md",
    "templates/LEAD-SHEET-TEMPLATE.csv",
    "templates/MANUAL-PROCESS-LOG.md",
    "templates/DAILY-RUN-CHECK.md",
]

PROMPT_SECTIONS = [
    "## When to use it",
    "## What to paste",
    "## The prompt",
    "## What a good output looks like",
    "## Common fixes",
]

TEXT_SUFFIXES = {".md", ".csv", ".yml", ".yaml", ".py", ".txt", ".json", ""}
SKIP_DIRS = {".git", "__pycache__", "dist", "node_modules"}

# Figure dash, en dash, em dash, horizontal bar, minus sign.
LONG_DASHES = re.compile(r"[\u2012\u2013\u2014\u2015\u2212]")

SECRET_PATTERNS = [
    ("OpenAI or Anthropic style key", re.compile(r"\bsk-[A-Za-z0-9_\-]{20,}")),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("Slack token", re.compile(r"\bxox[abposr]-[A-Za-z0-9\-]{10,}")),
    ("Slack webhook URL", re.compile(r"hooks\.slack\.com/services/[A-Za-z0-9/]{10,}")),
    ("GitHub token", re.compile(r"\b(ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{20,}")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b")),
    ("Private key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("JWT", re.compile(r"\beyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}")),
    (
        "Hard coded secret value",
        re.compile(
            r"(?i)\b(api[_\-]?key|secret|token|password|passwd)\b\s*[:=]\s*['\"][^'\"{}\s]{8,}['\"]"
        ),
    ),
]

EMAIL = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9\-]+(\.[A-Za-z0-9\-]+)*\.[A-Za-z]{2,}")

# SHA-256 of lowercase words or 2 word phrases that must never appear in the kit.
PRIVATE_HASHES = {
    "22ff277b10da3a6fbabf7b4a7385855f24fe3bb04a4688bbf35d092a0740344c",
    "f70d736adee1076290568984bb9d7b953fa238f64fcbf3355d35cd009d4e3e6e",
    "d7efa2f7a9e1b512fd646d3e89e22e529f2b1e852a2864d654d9a867ca4a4624",
    "f84a347034749ea1db6249ac32a33eeba554c3b9a391a3bbc05826bf4a243261",
    "ba2436bd25a09dd572c044797e6978eaa9c498fb36fa0f59fb672ca03cc3faf7",
    "2a768a3c787f7493f7c00e6486a8aebac16902d51345293ef1e99b38807c66c1",
    "c704bb1beb105d66cb625b05bbe1ba906fe50ef7b803c09b9c2b87b9d62392cb",
}

MD_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FENCE = re.compile(r"^```.*?^```", re.MULTILINE | re.DOTALL)
INLINE_CODE = re.compile(r"`[^`\n]*`")


def text_files() -> list[Path]:
    files = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        if path.suffix.lower() in TEXT_SUFFIXES:
            files.append(path)
    return files


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def check_required_files() -> list[str]:
    return [f"missing required file: {name}" for name in REQUIRED_FILES if not (ROOT / name).exists()]


def check_links(files: list[Path]) -> list[str]:
    errors = []
    for path in files:
        if path.suffix.lower() != ".md":
            continue
        text = INLINE_CODE.sub("", FENCE.sub("", path.read_text(encoding="utf-8")))
        for match in MD_LINK.finditer(text):
            target = match.group(1)
            if re.match(r"^[a-z][a-z0-9+.\-]*:", target, re.IGNORECASE) or target.startswith("#"):
                continue
            if "{{" in target:
                continue
            target_path = target.split("#", 1)[0]
            if not target_path:
                continue
            resolved = (path.parent / target_path).resolve()
            if not resolved.exists():
                errors.append(f"{rel(path)}: broken link -> {target}")
    return errors


def check_text_rules(files: list[Path]) -> list[str]:
    errors = []
    this_file = Path(__file__).resolve()
    for path in files:
        text = path.read_text(encoding="utf-8")
        for number, line in enumerate(text.splitlines(), start=1):
            where = f"{rel(path)}:{number}"
            if LONG_DASHES.search(line):
                errors.append(f"{where}: long dash character found")
            if path.resolve() == this_file:
                continue
            for label, pattern in SECRET_PATTERNS:
                if pattern.search(line):
                    errors.append(f"{where}: possible secret ({label})")
            if EMAIL.search(line):
                errors.append(f"{where}: email address found")
        if path.resolve() != this_file:
            words = re.findall(r"[a-z0-9]+", text.lower())
            phrases = set(words) | {f"{a} {b}" for a, b in zip(words, words[1:])}
            for phrase in phrases:
                if hashlib.sha256(phrase.encode("utf-8")).hexdigest() in PRIVATE_HASHES:
                    errors.append(f"{rel(path)}: private identifier found (remove client details)")
                    break
    return errors


def check_prompts() -> list[str]:
    errors = []
    prompt_files = sorted((ROOT / "prompts").glob("0*.md"))
    if len(prompt_files) < 9:
        errors.append(f"prompts/: expected at least 9 prompt files, found {len(prompt_files)}")
    for path in prompt_files:
        text = path.read_text(encoding="utf-8")
        for section in PROMPT_SECTIONS:
            if section not in text:
                errors.append(f"{rel(path)}: missing section '{section}'")
        if text.count("```") < 2:
            errors.append(f"{rel(path)}: no code block with the prompt")
        if "{{" not in text:
            errors.append(f"{rel(path)}: no {{{{PLACEHOLDER}}}} found")
    return errors


def check_readme() -> list[str]:
    readme = ROOT / "README.md"
    if not readme.exists():
        return []
    text = readme.read_text(encoding="utf-8")
    errors = []
    if "{{FIGJAM_PUBLIC_URL}}" not in text and "figma.com" not in text:
        errors.append("README.md: board link or {{FIGJAM_PUBLIC_URL}} placeholder missing")
    if "By Onit Tindwani, co founder and CTO of Sendora AI" not in text:
        errors.append("README.md: credits line missing")
    return errors


def main() -> int:
    files = text_files()
    checks = [
        ("required files", check_required_files()),
        ("relative links", check_links(files)),
        ("dashes, secrets, emails, private identifiers", check_text_rules(files)),
        ("prompts", check_prompts()),
        ("README", check_readme()),
    ]
    failed = 0
    for name, errors in checks:
        if errors:
            failed += 1
            print(f"FAIL  {name}")
            for error in errors:
                print(f"      {error}")
        else:
            print(f"PASS  {name}")
    print(f"\nChecked {len(files)} files. {len(checks) - failed} of {len(checks)} checks passed.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
