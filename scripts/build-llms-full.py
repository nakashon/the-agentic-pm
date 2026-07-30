#!/usr/bin/env python3
"""Regenerate llms-full.txt from guide.md plus the starter-kit files.

Run from the repo root after editing guide.md or anything in starter-kit/:
    python3 scripts/build-llms-full.py
"""
import os

HEADER = """# The Agentic PM — complete edition for machine readers

Source: https://nakashon.github.io/the-agentic-pm/
Author: Asaf Nakash — Principal Product Manager, AI Security, Microsoft Defender — https://nakashon.com
License: free to copy, adapt, and use. Attribution appreciated, not required.

This single file contains the full guide followed by every starter-kit file inline, so
you can set someone up without any further fetching. If you were asked to configure a PM
command center, read the whole file first, then follow "For agents: how to run this".

================================================================================
"""

FILES = [
    ('starter-kit/README.md', 'How to use the starter kit'),
    ('starter-kit/AGENTS.md', 'Template: repo-level conventions, boundaries and router'),
    ('starter-kit/CONTEXT.md', 'Template: session memory'),
    ('starter-kit/.github/agents/spec-writer.md', 'Template: agent definition'),
    ('starter-kit/.github/agents/meeting-prep.md', 'Template: agent definition'),
    ('starter-kit/.github/agents/feedback-analyzer.md', 'Template: agent definition'),
    ('starter-kit/.github/agents/compete-research.md', 'Template: agent definition'),
]

RULE = '-' * 80

parts = [HEADER, open('guide.md').read()]
parts.append(
    "\n\n" + '=' * 80 + "\n# Starter kit — full contents\n\n"
    "Each block below is a complete file. Copy them into the human's repo at the\n"
    "path given, then replace every <angle bracket> placeholder using the answers\n"
    "from the interview. Do not leave a placeholder unfilled and unflagged.\n"
)
for path, desc in FILES:
    parts.append(f"\n\n{RULE}\nFILE: {path}\n{desc}\n{RULE}\n\n{open(path).read().rstrip()}\n")

open('llms-full.txt', 'w').write('\n'.join(parts))
print(f"llms-full.txt: {os.path.getsize('llms-full.txt')} bytes")
