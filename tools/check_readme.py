#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Lightweight README validator for qqq-readme-test.

Checks: README exists, local images/links resolve, no banned stale-claim
phrases, no placeholder text, size threshold, expected headings, hero and
social assets present.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
MAX_BYTES = 35 * 1024

BANNED = [
    "412 rps", "18 ms p99", "27 ACTIVE", "274/587", "microseconds",
    "KB-scale", "~10-100 ms", "No other runtime", "cannot do this",
    "nothing drops", "nobody reconnects", "bit for bit",
    "production-ready", "YOUR_TEXT", "INSERT_IMAGE", "TBD", "FIXME",
    "lorem ipsum",
]

EXPECTED_HEADINGS = [
    "# QQQ",
    "# RUN ANYTHING. TRUST NOTHING.",
    "## WHY QQQ",
    "## INSTALL",
    "## ZERO AUTHORITY BY DEFAULT",
    "ONE RUNTIME. MULTIPLE LANGUAGES. ONE COMPONENT GRAPH.",
    "## SOFTWARE IS CHANGING.",
    "## THE RUNTIME HAS TO CHANGE TOO.",
    "## A DIFFERENT EXECUTION MODEL",
    "## PERFORMANCE",
    "## OPERATIONAL VISIBILITY",
    "## DETERMINISTIC EXECUTION",
    "## AOT",
    "## HOT SWAP",
    "## WHERE QQQ LOSES",
    "## STATUS",
    "## DOCUMENTATION",
    "## CONTRIBUTING",
    "## SECURITY",
]

failures = []


def fail(msg):
    failures.append(msg)


def main():
    if not README.exists():
        fail("README.md missing")
        return 1
    text = README.read_text(encoding="utf-8")

    if len(text.encode("utf-8")) > MAX_BYTES:
        fail("README exceeds %d bytes" % MAX_BYTES)

    for h in EXPECTED_HEADINGS:
        if h not in text:
            fail("missing heading: %s" % h)

    for phrase in BANNED:
        if phrase in text:
            fail("banned stale-claim phrase present: %r" % phrase)

    if "```" in text and "TODO" in text:
        fail("TODO left in README")

    for m in re.finditer(r"<img\s+[^>]*>", text):
        tag = m.group(0)
        sm = re.search(r'src="([^"]+)"', tag)
        am = re.search(r'alt="([^"]*)"', tag)
        src = sm.group(1) if sm else ""
        if src.startswith("./"):
            p = ROOT / src[2:]
            if not p.exists():
                fail("missing image: %s" % src)
            elif p.stat().st_size == 0:
                fail("empty image: %s" % src)
        alt = am.group(1) if am else ""
        if src.startswith("./"):
            if not alt.strip() or len(alt) < 8:
                fail("local image without meaningful alt text: %s" % src)
        elif not alt.strip():
            fail("badge without alt text: %s" % src)

    for m in re.finditer(r'\[.+?\]\((\./[^)]+)\)', text):
        p = ROOT / m.group(1)[2:].split("#")[0]
        if not p.exists():
            fail("broken local link: %s" % m.group(1))

    for asset in ("assets/qqq-hero.jpg", "assets/qqq-social-preview.png"):
        p = ROOT / asset
        if not p.exists():
            fail("missing asset: %s" % asset)
        elif p.stat().st_size >= 1024 * 1024:
            fail("asset over 1 MB: %s" % asset)
    for svg in (
        "assets/qqq-runtime-model.svg", "assets/qqq-capability-wall.svg",
        "assets/qqq-language-graph.svg", "assets/qqq-ai-agent-runtime.svg",
        "assets/qqq-execution-model.svg", "assets/qqq-aot.svg",
        "assets/qqq-hot-swap.svg",
    ):
        p = ROOT / svg
        if not p.exists():
            fail("missing asset: %s" % svg)
        elif p.stat().st_size >= 250 * 1024:
            fail("svg over 250 KB: %s" % svg)

    if failures:
        print("README CHECK FAILED:")
        for f in failures:
            print(" -", f)
        return 1
    print("README CHECK OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
