"""
Smoke tests for the book's chapter scripts.

A "smoke test" checks that a program runs from start to finish without
crashing. It does not check that every number in the output is correct.
That kind of detailed check would need a separate test for each chapter.
A smoke test is the right first step because it catches the most common
problems automatically: a broken import, a missing data file, a typo in
the code, or a dependency that silently stopped working.

How this file works:
1. It looks inside code/python/ and finds every chapter script.
2. For each script, it runs that script in a fresh Python process,
   the same way a reader would run it from the command line.
3. It checks that the script exits with code 0, which is the standard
   signal that a program finished without an error.

If a script fails, pytest prints that script's own error message, so you
can see exactly what went wrong without needing to run it by hand.
"""
import subprocess
import sys
from pathlib import Path

import pytest

# Path to the repository root.
# __file__ is this test file. .parents[1] goes up one folder, from
# tests/ to the repository root.
REPO_ROOT = Path(__file__).resolve().parents[1]

# Folder that holds the chapter scripts.
PYTHON_DIR = REPO_ROOT / "code" / "python"

# Find every chapter script automatically, so new chapters get tested
# without needing to edit this file. Sorted so test output stays in
# a predictable, readable order (ch01, ch02, ch03, ...).
CHAPTER_SCRIPTS = sorted(PYTHON_DIR.glob("ch*.py"))


@pytest.mark.parametrize("script", CHAPTER_SCRIPTS, ids=lambda p: p.name)
def test_chapter_script_runs(script):
    """Each chapter script should run to completion without raising an error."""
    result = subprocess.run(
        [sys.executable, str(script)],  # run "python <script>"
        cwd=REPO_ROOT,                  # run from the repo root, like a reader would
        capture_output=True,            # collect stdout and stderr for the error message
        text=True,                      # return output as text, not bytes
        timeout=180,                    # fail rather than hang forever
    )

    assert result.returncode == 0, (
        f"{script.name} exited with code {result.returncode}\n"
        f"--- stdout ---\n{result.stdout}\n"
        f"--- stderr ---\n{result.stderr}"
    )
