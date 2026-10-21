"""Run check_okf.py on real bundles, an edge-case fixture and a bundle made from the templates.

Usage: python tests/test_check_okf.py [skill_dir]   (default: ../skills/project-init next to this file)
Read the output: the expected results are in docs/skill/Skill-Overview.md section 5.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
SK = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "skills" / "project-init"
CHECK = SK / "scripts" / "check_okf.py"
STUDIES = Path(r"D:\Users\ShaoWenChooi\YTL\Digital Engineering (SPYTL) - Repository\Studies")
NO_YAML = "import sys,runpy; sys.modules['yaml']=None; s=sys.argv[1]; sys.argv=['x', sys.argv[2]]; runpy.run_path(s, run_name='__main__')"


def run(bundle, yaml=True):
    cmd = [sys.executable, str(CHECK), str(bundle)] if yaml else [sys.executable, "-c", NO_YAML, str(CHECK), str(bundle)]
    out = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    return out.stdout.strip()


def write(root, rel, text):
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


print("=== real bundles: last line with PyYAML / without")
for name in ["(2026.10.21) SW - Worksheet Improvements - App", "(2026.10.06) Voon - Water Engineering"]:
    b = STUDIES / name / "docs"
    print(name, "|", run(b).splitlines()[-1], "|", run(b, yaml=False).splitlines()[-1])

tmp = Path(tempfile.mkdtemp(prefix="okf-test-"))
fx = tmp / "fixture" / "docs"
write(fx, "index.md", '---\nokf_version: "0.2"\n---\n# X\n* [line/](line/) - line\n')
write(fx, "line/index.md", '# Line\n* [A.md](A.md "titled link") - a\n* [B.md](B.md) - b\n* [Missing](Gone.md "t") - broken titled link\n')
write(fx, "line/A.md", "---\ntype: overview\ntitle: Worksheet: KPI\n---\nbody\n")
write(fx, "line/B.md", "---\ntype: overview\ntitle: B\ndescription: d\nsources:\n  - title: no resource here\n"
      "  - resource: D:\\nowhere\\book.xlsx\n  - resource: \\\\server\\share\\book.xlsx\n"
      "generated: { by: claude-code/x }\nverified:\n  - at: 2026-10-21T00:00:00+08:00\n---\n[bad](/line/nope.md)\n")
write(fx, "log.md", "# Log\n\nIntro prose.\n\n## 2026-10-21\n\n* **Update** \u2014 star bullet with no owner\n"
      "- **Update** \u2014 dash bullet\nactor:claude-code/x \u00b7 owner:human:SW \u00b7 reason: flush-left continuation\n\n## Notes\n")
print("\n=== fixture, PyYAML\n" + run(fx))
print("\n=== fixture, no PyYAML\n" + run(fx, yaml=False))

tp = tmp / "tpl" / "docs"


def fill(src, dst, extra=()):
    text = re.sub(r"\{\{[^}]*\}\}", "x", (SK / "templates" / src).read_text(encoding="utf-8"))
    for a, b in extra:
        text = text.replace(a, b)
    write(tp, dst, text)


fill("docs-index.md", "index.md", [("](x/)", "](line-one/)")])
fill("docs-log.md", "log.md", [("## x\n", "## 2026-10-21\n")])
fill("line-index.md", "line-one/index.md", [("x-Overview", "L-Overview"), ("x-Open-Items", "L-Open-Items")])
fill("Overview.md", "line-one/L-Overview.md")
fill("Open-Items.md", "line-one/L-Open-Items.md")
fill("Decision.md", "line-one/decisions/L-Decision.md")
fill("Project-Setup.md", "Project-Setup.md")
STALE = "stale_after: {{YYYY-MM-DDTHH:MM:SS+08:00, 14 days after generated.at}}"
src = (SK / "templates" / "Current-State.md").read_text(encoding="utf-8")
assert STALE in src, "stale_after placeholder changed"
for name, when in [("Current-State.md", "2026-01-01T00:00:00+08:00"), ("Current-State-Future.md", "2099-01-01T00:00:00+08:00")]:
    write(tp, name, re.sub(r"\{\{[^}]*\}\}", "x", src.replace(STALE, f"stale_after: {when}")))
print("\n=== template bundle (placeholders replaced with 'x')\n" + run(tp))
print("\nfixtures in", tmp)
