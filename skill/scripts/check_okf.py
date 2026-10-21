"""Check a docs/ folder against OKF v0.2 and the house rules of the project-init skill.

Usage:
    python check_okf.py [bundle_dir] [--exclude GLOB ...]

FAIL = breaks OKF v0.2 bundle conformance (or a hard house rule). Exit code 1 if any FAIL.
WARN = a house rule or a likely mistake (missing recommended key, broken link, unlisted document).
Standard library only. Uses PyYAML for a full parse when it is installed.
"""
import argparse
import fnmatch
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote

try:
    import yaml  # optional
except ImportError:
    yaml = None

RESERVED = {"index.md", "log.md"}
STATUS_VALUES = {"draft", "stable", "deprecated"}
RECOMMENDED = ("title", "description", "sources", "generated")
LINK_RE = re.compile(r"\[[^\]]*\]\((<[^>]+>|[^)\s]+)(?:\s+[\"'][^\"']*[\"'])?\s*\)")
DATE_HEADING_RE = re.compile(r"^##\s+(.*?)\s*$")
ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
TOP_KEY_RE = re.compile(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$")
RESOURCE_RE = re.compile(r"^\s*(?:-\s+)?resource\s*:\s*(.+?)\s*$")
URL_RE = re.compile(r"^[a-z][a-z0-9+.-]+:", re.I)  # 2+ letters, so a drive letter (D:) is not a scheme
DRIVE_RE = re.compile(r"^[A-Za-z]:[\\/]")
BULLET_RE = re.compile(r"^[-*]\s")

results = []


def report(level, path, msg):
    results.append((level, path, msg))


def split_frontmatter(text):
    """Return (frontmatter_text, body) or (None, text) when there is no frontmatter."""
    if text.startswith("﻿"):
        text = text[1:]
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i]), "\n".join(lines[i + 1:])
    return None, text


def parse_frontmatter(fm):
    """Return (dict, error). The fallback parser (no PyYAML) is approximate: it reads top-level keys and
    generated.by, and rejects the common error of an unquoted value that holds ': '."""
    if yaml is not None:
        try:
            data = yaml.safe_load(fm) or {}
        except yaml.YAMLError as exc:
            return None, f"frontmatter is not valid YAML: {str(exc).splitlines()[0]}"
        if not isinstance(data, dict):
            return None, "frontmatter is not a YAML mapping"
        return data, None
    data, current = {}, None
    for line in fm.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = TOP_KEY_RE.match(line)
        if m and not line[0].isspace():
            current = m.group(1)
            raw = re.sub(r"\s+#.*$", "", m.group(2)).strip()
            if raw and raw[0] not in "'\"{[|>" and ": " in raw:
                return None, f"frontmatter is not valid YAML: unquoted ': ' in the value of '{current}'"
            value = raw.strip("'\"")
            data[current] = value if value else {}
        elif current == "generated" and isinstance(data.get(current), dict):
            sub = TOP_KEY_RE.match(line.strip())
            if sub:
                data[current][sub.group(1)] = sub.group(2).strip()
    if isinstance(data.get("generated"), str) and data["generated"].startswith("{"):
        inline = data["generated"]
        data["generated"] = {"by": "x"} if re.search(r"\bby\s*:", inline) else {}
    return data, None


def strip_code(body):
    body = re.sub(r"```.*?```|<!--.*?-->", "", body, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", body)


def link_targets(body):
    for m in LINK_RE.finditer(strip_code(body)):
        target = m.group(1)
        if target.startswith("<"):
            target = target[1:-1]
        target = target.split("#", 1)[0].strip()
        if not target or URL_RE.match(target):
            continue  # anchor only, or a URL / mailto
        yield unquote(target)


def resolve(target, base_dir, bundle):
    """A /-rooted path is bundle-absolute (OKF). A drive path is absolute. Others are relative."""
    if DRIVE_RE.match(target):
        return [Path(target)]
    if target.startswith("/"):
        return [bundle / target.lstrip("/")]
    return [base_dir / target]


def check_links(path, rel, body, bundle):
    for target in link_targets(body):
        if not any(p.exists() for p in resolve(target, path.parent, bundle)):
            report("WARN", rel, f"link target not found: {target}")


def check_stale(rel, data):
    """stale_after must be an ISO 8601 instant with an offset; WARN when it has passed."""
    value = data.get("stale_after")
    if value is None or value == {}:
        if str(data.get("type")).strip() == "status":
            report("WARN", rel, "type 'status' has no 'stale_after'")
        return
    if isinstance(value, datetime):
        when = value
    else:
        try:
            when = datetime.fromisoformat(str(value).strip().strip("'\"").replace("Z", "+00:00"))
        except ValueError:
            report("FAIL", rel, f"stale_after is not an ISO 8601 date-time: {value}")
            return
    if when.tzinfo is None:
        report("WARN", rel, "stale_after has no UTC offset")
        when = when.replace(tzinfo=timezone.utc)
    if datetime.now(timezone.utc) >= when:
        report("WARN", rel, f"stale since {when.isoformat()} - rewrite it, then move stale_after ahead")


def check_lists(rel, data):
    """Shape checks that need a full YAML parse: sources[].resource and verified[].by."""
    sources = data.get("sources")
    if sources is not None:
        if not isinstance(sources, list):
            report("FAIL", rel, "'sources' must be a list")
        else:
            for i, s in enumerate(sources):
                if not (isinstance(s, dict) and s.get("resource")):
                    report("FAIL", rel, f"sources[{i}] has no 'resource'")
    verified = data.get("verified")
    if verified is None or verified == []:
        return
    entries = [verified] if isinstance(verified, dict) else verified
    if not isinstance(entries, list):
        report("FAIL", rel, "'verified' must be a list or a mapping")
        return
    for i, v in enumerate(entries):
        if not (isinstance(v, dict) and v.get("by")):
            report("FAIL", rel, f"verified[{i}] has no 'by'")
        elif not v.get("at"):
            report("WARN", rel, f"verified[{i}] has no 'at'")


def check_concept(path, rel, text, bundle):
    fm, body = split_frontmatter(text)
    if fm is None:
        report("FAIL", rel, "no frontmatter (every non-reserved .md file needs a --- block with type)")
        check_links(path, rel, body, bundle)
        return
    data, err = parse_frontmatter(fm)
    if err:
        report("FAIL", rel, err)
        check_links(path, rel, body, bundle)
        return
    if not str(data.get("type") or "").strip():
        report("FAIL", rel, "frontmatter has no non-empty 'type'")
    for key in RECOMMENDED:
        if key not in data:
            report("WARN", rel, f"recommended key missing: {key}")
    gen = data.get("generated")
    if gen is not None and not (isinstance(gen, dict) and gen.get("by")):
        report("FAIL", rel, "'generated' must have 'by'")
    status = str(data.get("status") or "").strip()
    if status and status not in STATUS_VALUES:
        report("FAIL", rel, f"status '{status}' is not draft, stable or deprecated")
    if re.search(r"^verified\s*:\s*\[\s*\]", fm, re.M):
        report("WARN", rel, "'verified: []' - omit the key when there is no verification")
    if str(data.get("type")).strip() == "Attested Computation" and "runtime" not in data:
        report("FAIL", rel, "type 'Attested Computation' needs 'runtime'")
    check_stale(rel, data)
    if yaml is not None:
        check_lists(rel, data)
    for line in fm.splitlines():
        m = RESOURCE_RE.match(line)
        if not m:
            continue
        value = re.sub(r"\s+#.*$", "", m.group(1)).strip().strip("'\"")
        if URL_RE.match(value) or value.startswith("\\\\"):
            continue  # URL or network share: outside what this check can see
        if " " in value and "/" not in value and "\\" not in value:
            continue  # scope descriptor, not a path
        if not any(p.exists() for p in resolve(unquote(value), path.parent, bundle)):
            report("WARN", rel, f"resource path not found: {value}")
    check_links(path, rel, body, bundle)


def check_index(path, rel, text, bundle, is_root):
    fm, body = split_frontmatter(text)
    if is_root:
        if fm is None:
            report("WARN", rel, "root index.md has no frontmatter with okf_version: \"0.2\"")
        else:
            data, err = parse_frontmatter(fm)
            if err:
                report("FAIL", rel, err)
            else:
                extra = set(data) - {"okf_version"}
                if extra:
                    report("FAIL", rel, f"root index frontmatter may hold only okf_version (found {sorted(extra)})")
                if str(data.get("okf_version", "")).strip("'\"") != "0.2":
                    report("WARN", rel, "okf_version is not \"0.2\"")
    elif fm is not None:
        report("FAIL", rel, "a non-root index.md must not have frontmatter")
    check_links(path, rel, body, bundle)
    listed = set()
    for target in link_targets(body):
        for p in resolve(target, path.parent, bundle):
            listed.add(p.resolve())
    return listed


def check_log(path, rel, text, bundle):
    fm, body = split_frontmatter(text)
    if fm is not None:
        report("FAIL", rel, "log.md must not have frontmatter")
    check_links(path, rel, body, bundle)
    dates, entry, entries = [], None, []
    for line in body.splitlines():
        m = DATE_HEADING_RE.match(line)
        if m:
            if not ISO_DATE_RE.match(m.group(1)):
                report("FAIL", rel, f"every '##' heading in a log must be a date 'YYYY-MM-DD': {line.strip()}")
            else:
                dates.append(m.group(1))
            entry = None
            continue
        if not dates:
            continue  # prose above the first date heading
        if BULLET_RE.match(line):
            entry = [line]
            entries.append(entry)
        elif entry is not None and line.strip() and not line.startswith("#"):
            entry.append(line)
        else:
            entry = None
    if dates != sorted(dates, reverse=True):
        report("FAIL", rel, "date headings are not newest first")
    if len(dates) != len(set(dates)):
        report("WARN", rel, "a date heading appears more than once")
    for e in entries:
        joined = " ".join(e)
        if "owner:" not in joined:
            report("WARN", rel, f"entry has no 'owner:' tag: {e[0][:70]}...")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("bundle", nargs="?", default="docs")
    ap.add_argument("--exclude", action="append", default=[], help="glob relative to the bundle, e.g. 'archive/**'")
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass

    bundle = Path(args.bundle).resolve()
    if not bundle.is_dir():
        print(f"FAIL {args.bundle}: not a folder")
        return 1

    files = []
    for p in sorted(bundle.rglob("*.md")):
        rel = p.relative_to(bundle).as_posix()
        if any(part.startswith(".") or part == "node_modules" for part in p.relative_to(bundle).parts):
            continue
        if any(fnmatch.fnmatch(rel, g) for g in args.exclude):
            continue
        files.append((p, rel))

    listed, concepts = set(), []
    for p, rel in files:
        text = p.read_text(encoding="utf-8", errors="replace")
        name = p.name
        if name.lower() in RESERVED and name not in RESERVED:
            report("WARN", rel, f"use lowercase '{name.lower()}' (reserved name)")
        if name.lower() == "index.md":
            listed |= check_index(p, rel, text, bundle, is_root=(p.parent == bundle))
        elif name.lower() == "log.md":
            check_log(p, rel, text, bundle)
        else:
            concepts.append(p)
            check_concept(p, rel, text, bundle)

    if not (bundle / "index.md").exists():
        report("WARN", ".", "no root index.md")
    for p in concepts:
        if p.resolve() not in listed:
            report("WARN", p.relative_to(bundle).as_posix(), "not listed in any index.md")

    order = {"FAIL": 0, "WARN": 1}
    for level, rel, msg in sorted(results, key=lambda r: (order[r[0]], r[1])):
        print(f"{level} {rel}: {msg}")
    fails = sum(1 for r in results if r[0] == "FAIL")
    warns = len(results) - fails
    parser = "PyYAML" if yaml else "built-in parser"
    print(f"{'PASS' if not fails else 'FAIL'}: {len(concepts)} concepts, {fails} FAIL, {warns} WARN ({parser})")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
