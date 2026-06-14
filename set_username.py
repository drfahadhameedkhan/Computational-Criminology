"""
Replace the YOUR-USERNAME placeholder across the repository with your GitHub
username, so the Colab badges, clone commands, and notebook setup cells point
at your copy.

Usage, from the repository root:
    python set_username.py your-github-username
"""
import sys
from pathlib import Path

if len(sys.argv) != 2:
    print("usage: python set_username.py <your-github-username>")
    raise SystemExit(1)

user = sys.argv[1].strip().strip("/")
root = Path(__file__).resolve().parent
exts = {".md", ".ipynb", ".yml", ".yaml", ".cff", ".py"}
changed = 0
for p in root.rglob("*"):
    if p.is_file() and p.suffix in exts and p.name != "set_username.py":
        text = p.read_text(encoding="utf-8")
        if "YOUR-USERNAME" in text:
            p.write_text(text.replace("YOUR-USERNAME", user), encoding="utf-8")
            changed += 1
            print("updated", p.relative_to(root))
print(f"\nReplaced YOUR-USERNAME with '{user}' in {changed} files.")
print("Review the changes, then commit and push.")
