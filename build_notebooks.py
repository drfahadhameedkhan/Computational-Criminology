"""
Build one Colab notebook per chapter from the verified Python code and the
exercise prompts. Run from the repository root:

    python build_notebooks.py

Each notebook clones the repository, installs what the chapter needs, builds
the synthetic data, then runs the chapter's code. Replace drfahadhameedkhan with
your GitHub username (the README explains how, or edit REPO below once).
"""
import re
from pathlib import Path
import nbformat as nbf

ROOT = Path(__file__).resolve().parent
REPO = "https://github.com/drfahadhameedkhan/computational-criminology.git"
REPO_DIR = "computational-criminology"

# chapter -> (filename stem, title, pip extras beyond the base install)
CHAPTERS = {
    1:  ("ch01_first_session",      "The shape of computational criminology", ""),
    2:  ("ch02_sampling_bias",      "Designing a computational study", ""),
    3:  ("ch03_recording_pipeline", "Theory, measurement, and crime data", ""),
    4:  ("ch04_fetching_api",       "Sources and collection of data", "requests"),
    5:  ("ch05_cleaning",           "Cleaning, structuring, and managing data", ""),
    6:  ("ch06_k_anonymity",        "Ethics, privacy, and law", ""),
    7:  ("ch07_counts_poisson",     "Statistical foundations", "statsmodels"),
    8:  ("ch08_prediction",         "Machine learning for prediction", "scikit-learn"),
    9:  ("ch09_spatial",            "Spatial analysis and crime mapping",
         "geopandas libpysal esda shapely"),
    10: ("ch10_networks",           "Network analysis of co-offending", "networkx"),
    11: ("ch11_abm",                "Agent-based modelling and simulation", ""),
    12: ("ch12_text",               "Text as data", ""),
    13: ("ch13_did",                "Causal inference with observational data", "statsmodels"),
    14: ("ch14_fairness",           "Validation, fairness, and accountability", "scikit-learn"),
    15: ("ch15_reproducibility",    "Reproducibility and open science", ""),
    16: ("ch16_bootstrap",          "Writing and publishing", ""),
}

def load_exercises(chap):
    """Read the exercise prompts from the committed per-chapter markdown file,
    stripping the heading and the trailing how-to-run note."""
    p = ROOT / "exercises" / f"ch{chap:02d}_exercises.md"
    if not p.exists():
        return ""
    text = p.read_text(encoding="utf-8")
    body = text.split("\n", 3)[-1] if text.count("\n") >= 3 else text
    body = body.split("\n---\n")[0]
    return body.strip()


def chapter_code(stem):
    """Read the .py file, strip the __file__-based path setup, and rewrite
    data paths to be relative to the repo root (the notebook cwd)."""
    src = (ROOT / "code" / "python" / f"{stem}.py").read_text()
    # drop the module docstring (first triple-quoted block)
    src = re.sub(r'^""".*?"""\n', "", src, count=1, flags=re.S)
    # rewrite the Path(__file__)... data locator to a plain relative path
    src = re.sub(
        r'Path\(__file__\)\.resolve\(\)\.parents\[2\]\s*/\s*"data"\s*/\s*"synthetic"\s*/\s*"([^"]+)"',
        r'Path("data/synthetic/\1")', src)
    src = re.sub(
        r'Path\(__file__\)\.resolve\(\)\.parents\[2\]\s*/\s*"figures"\s*/\s*"output"',
        r'Path("figures/output")', src)
    # the ch11 guard would suppress output in a notebook; unwrap it
    src = src.replace(
        'if __name__ == "__main__":\n    print("few guardians:'
        ' ", run(0.02), " many:", run(0.35))',
        'print("few guardians:", run(0.02), " many:", run(0.35))')
    return src.strip()


def build(chap):
    stem, title, extras = CHAPTERS[chap]
    nb = nbf.v4.new_notebook()
    cells = []

    cells.append(nbf.v4.new_markdown_cell(
        f"# Chapter {chap}. {title}\n\n"
        "*Companion notebook to* **Computational Criminology: Research Methods, "
        "Ethics, and Reproducible Practice with R and Python** *by Dr Fahad "
        "Hameed Khan.*\n\n"
        "Run the setup cell once, then run the code cell. Everything uses "
        "synthetic data, so nothing here describes a real person. The R version "
        f"of this chapter is in `code/r/{stem}.R`."))

    base = "numpy pandas matplotlib"
    pip = (base + " " + extras).strip()
    setup = (
        "# Setup: fetch the repository, install what this chapter needs,\n"
        "# and build the synthetic data. Safe to run more than once.\n"
        "import os\n"
        f"if not os.path.exists('{REPO_DIR}'):\n"
        f"    !git clone -q {REPO}\n"
        f"%cd -q {REPO_DIR}\n"
        f"!pip install -q {pip}\n"
        "!python data/synthetic/make_synthetic_data.py")
    cells.append(nbf.v4.new_code_cell(setup))

    cells.append(nbf.v4.new_code_cell(chapter_code(stem)))

    ex = load_exercises(chap)
    if ex:
        cells.append(nbf.v4.new_markdown_cell("## Exercises\n\n" + ex))

    nb["cells"] = cells
    nb["metadata"] = {
        "colab": {"name": f"{stem}.ipynb", "provenance": []},
        "kernelspec": {"name": "python3", "display_name": "Python 3"},
        "language_info": {"name": "python"},
    }
    out = ROOT / "notebooks" / f"{stem}.ipynb"
    nbf.write(nb, out)
    return out.name


if __name__ == "__main__":
    for c in sorted(CHAPTERS):
        print("built", build(c))
    print("\nAll notebooks written to notebooks/")
