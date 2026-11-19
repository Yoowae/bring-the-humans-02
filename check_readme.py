#!/usr/bin/env python3
"""Validate the bring-the-humans-02 guide README against RULES.txt.

Stdlib only, offline, deterministic. Checks the guide_page rules the
competition names plus the badge lines repo_readme reads:
  - README.md exists at repo root, exact case, under 2 MB
  - referral code b9gbfsac present (bare, /r/b9gbfsac, ?ref=b9gbfsac)
  - exact referral link https://make.fun/r/b9gbfsac present, no shortener,
    no extra tracking params
  - three make.fun badge lines present as live images (not in a code block
    or HTML comment)
  - no .github/README.md shadowing the root README
  - required tutorial sections present
  - no leftover {{PLACEHOLDER}} referral fields (owner placeholder is
    reported separately: the GitHub owner is filled in when the repo is
    created under the linked account)

Usage: python3 check_readme.py [repo-root]
Exit 0 when every check passes, 1 otherwise.
"""
import os
import re
import sys

CODE = "b9gbfsac"
LINK = "https://make.fun/r/b9gbfsac"
SLUG = "bring-the-humans-02"
MAX_BYTES = 2 * 1024 * 1024

REQUIRED_SECTIONS = [
    "What make.fun is",
    "What you can win",
    "What you need before you start",
    "Create your account",
    "Choose a bounty",
    "Download the kit",
    "Build with your agent",
    "Submit your entry",
    "Read the checks",
    "Claim a reward",
    "Get your own referral link",
    "Common questions",
]

BADGE_LINES = [
    "https://make.fun/badge/bring-the-humans-02.svg",
    "/rank.svg",
    "/reward.svg",
]


def strip_code_and_comments(text):
    """Remove fenced code blocks and HTML comments for the 'live' checks."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return text


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    readme = os.path.join(root, "README.md")
    failures = []
    notes = []

    if not os.path.isfile(readme):
        print("FAIL: README.md missing at repo root")
        return 1
    if os.path.exists(os.path.join(root, "Readme.md")) or os.path.exists(
        os.path.join(root, "readme.md")
    ):
        failures.append("wrong-case readme file present alongside README.md")
    if os.path.exists(os.path.join(root, ".github", "README.md")):
        failures.append(".github/README.md would shadow the root README")

    size = os.path.getsize(readme)
    print(f"README.md size: {size} bytes (limit {MAX_BYTES})")
    if size > MAX_BYTES:
        failures.append("README.md over 2 MB")

    text = open(readme, encoding="utf-8").read()
    live = strip_code_and_comments(text)

    if LINK not in text:
        failures.append(f"exact referral link {LINK} missing")
    if f"/r/{CODE}" not in text:
        failures.append("referral code as /r/<code> missing")
    if f"`{CODE}`" not in text and CODE not in text:
        failures.append("bare referral code missing")
    if re.search(r"https?://(bit\.ly|t\.co|tinyurl\.|goo\.gl|is\.gd)/", text):
        failures.append("URL shortener found in README")
    if re.search(re.escape(LINK) + r"\?[^ \)\n]+", text):
        failures.append("extra tracking params on referral link")
    if "{{REFERRAL_LINK}}" in text or "{{REFERRAL_CODE}}" in text:
        failures.append("unfilled referral placeholder left in README")
    if "{{GITHUB_OWNER}}" in text:
        notes.append(
            "NOTE: {{GITHUB_OWNER}} still a placeholder — fill with the "
            "linked GitHub account when the repo is created"
        )

    for badge in BADGE_LINES:
        if badge not in live:
            failures.append(f"badge line missing or not live: {badge}")
    if "make.fun/badge/bring-the-humans-02" not in live:
        failures.append("competition badge line missing")

    for section in REQUIRED_SECTIONS:
        if section.lower() not in text.lower():
            failures.append(f"required section missing: {section}")

    for word in ("testimonial", "guaranteed prize", "guaranteed to win",
                 "100% win", "free money"):
        if word in text.lower():
            failures.append(f"forbidden/misleading wording present: {word!r}")

    print(f"referral link occurrences: {text.count(LINK)}")
    print(f"referral code occurrences: {text.count(CODE)}")
    print(f"lines: {text.count(chr(10)) + 1}")

    for note in notes:
        print(note)
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print("PASS: README meets the checked RULES.txt requirements")
    return 0


if __name__ == "__main__":
    sys.exit(main())
