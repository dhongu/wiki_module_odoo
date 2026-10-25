#!/usr/bin/env python3
"""Sincronizarea de noapte a wiki-ului cu sursele modulelor.

Rulează din rădăcina unui layout de tip monorepo, cu wiki-ul în
`wiki_module_odoo/` și suitele în `odoo-addons/<suită>/` (ca în odoo19 sau ca
în workflow-ul `wiki-nightly.yml`).

Două comenzi:

  plan      Treapta mecanică, fără AI: aduce `Versiune` la versiunea din
            manifest, resincronizează fișa consultant (cu capturi și sub-fișe)
            și scrie coada pentru reingestia AI (`.wiki-queue.json`), cel mult
            `--limit` module, în ordinea priorității:
              1. dependențele din manifest diferă de cele din pagină;
              2. `readme/DESCRIPTION|USAGE|CONFIGURE.md` modificate după
                 „Ultima Ingestie”;
              3. modul fără DESCRIPTION.md cu modele/view-uri/date modificate;
              4. modul nou, fără pagină.
  finalize  După reingestie: actualizează `index.md` și `log.md` din raportul
            `.wiki-ingest-report.json` scris de agent și reface indexul.

Folosire:
    python3 wiki_module_odoo/scripts/wiki_sync.py plan [--limit 10] [--dry-run]
    python3 wiki_module_odoo/scripts/wiki_sync.py finalize
"""
from __future__ import annotations

import argparse
import ast
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

WIKI = Path(__file__).resolve().parent.parent
ROOT = WIKI.parent
QUEUE = ROOT / ".wiki-queue.json"
SUMMARY = ROOT / ".wiki-sync-summary.json"
REPORT = ROOT / ".wiki-ingest-report.json"
EXCLUDE = WIKI / "scripts" / "wiki_sync_exclude.txt"

# Suitele urmărite, cu repo-ul lor (aceeași mapare ca în documentarist-wiki).
SUITES = {
    "terrabit": "terrabit-solutions/terrabit",
    "l10n_ro_ent": "terrabit-solutions/l10n_ro_ent",
    "bitshop": "terrabit-solutions/bitshop",
    "bitshop_ent": "terrabit-solutions/bitshop_ent",
    "bitshop_delivery": "terrabit-solutions/bitshop_delivery",
    "bitshop_marketplace": "terrabit-solutions/bitshop_marketplace",
    "bitshop_vendor": "terrabit-solutions/bitshop_vendor",
    "deltatech": "dhongu/deltatech",
    "deltatech_service": "dhongu/deltatech_service",
    "deltatech_stock_valuation": "dhongu/deltatech_stock_valuation",
    "l10n-romania": "dhongu/l10n-romania",
    "l10n-romania-oca": "terrabit-ro/l10n-romania",
    "l10n-moldova": "dhongu/l10n-moldova",
}

RE_VERSION = re.compile(r"^(- \*\*Versiune:\*\* `)([^`]+)(`)", re.M)
RE_LOCAL = re.compile(r"^- \*\*Cale Local[ăa]:\*\* `([^`]+)`", re.M)
# Data apare și fără backticks în paginile mai vechi.
RE_INGEST = re.compile(r"^(- \*\*Ultima Ingestie:\*\* `?)(\d{4}-\d{2}-\d{2})(`?.*)$", re.M)
RE_FISA_LINE = "- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)"
RE_IMG = re.compile(r"\]\(((?:\.\./)*)(static/description|screenshots)/([^)]+\.(?:png|jpe?g|gif|svg|webp))\)")
RE_LOCAL_LINK = re.compile(r"\]\(([^)#\s]+\.md)\)")

CODE_PATHS = ("models", "views", "wizard", "wizards", "data", "report")
README_PATHS = ("readme/DESCRIPTION.md", "readme/USAGE.md", "readme/CONFIGURE.md")


def read_manifest(path: Path) -> dict:
    try:
        return ast.literal_eval(path.read_text(encoding="utf-8"))
    except (OSError, ValueError, SyntaxError):
        return {}


def section(text: str, number: int) -> str:
    # Paginile mai vechi au secțiunile cu `##` în loc de `####`.
    m = re.search(rf"^#{{2,4}} {number}\..*?(?=^#{{2,4}} \d|\Z)", text, re.M | re.S)
    return m.group(0) if m else ""


def page_depends(text: str) -> set[str]:
    sec = section(text, 3)
    return set(re.findall(r"^- \[([\w.]+)\]\(", sec, re.M)) | set(re.findall(r"^- `([\w.]+)`", sec, re.M))


def git_changed_since(suite_dir: Path, module: str, since: str, paths: tuple[str, ...]) -> bool:
    """True dacă vreun commit de după `since` atinge una din căile modulului."""
    specs = [f"{module}/{p}" for p in paths]
    try:
        out = subprocess.run(
            ["git", "-C", str(suite_dir), "log", f"--since={since}T23:59:59", "--format=%H", "--", *specs],
            capture_output=True, text=True, check=True,
        ).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False
    return bool(out.strip())


def write_if_changed(path: Path, data: bytes) -> bool:
    if path.exists() and path.read_bytes() == data:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return True


def rewrite_images(md: str, depth: int, src_md_dir: Path, readme: Path, shots: Path) -> tuple[str, bool]:
    """Copiază pozele referite și rescrie căile la `<../ x depth>screenshots/`."""
    changed = False
    module_dir = readme.parent

    def repl(m: re.Match) -> str:
        nonlocal changed
        ups, kind, name = m.groups()
        src = (src_md_dir / ups / kind / name).resolve()
        for cand in (src, module_dir / "static/description" / name, readme / "screenshots" / name):
            if cand.is_file():
                changed |= write_if_changed(shots / name, cand.read_bytes())
                break
        return f"]({'../' * depth}screenshots/{name})"

    return RE_IMG.sub(repl, md), changed


def sync_fisa(src: Path, dst: Path) -> bool:
    """Copia fidelă a fișei consultant, ca la pasul 5–7 din documentarist-wiki."""
    readme = src / "readme"
    fisa = readme / "FISA_CONSULTANT.md"
    if not fisa.is_file():
        return False
    shots = dst / "screenshots"
    text, changed = rewrite_images(fisa.read_text(encoding="utf-8"), 0, readme, readme, shots)
    changed |= write_if_changed(dst / "FISA_CONSULTANT.md", text.encode("utf-8"))
    # Sub-fișe legate din fișă: un director din readme/ se copiază întreg,
    # un .md aflat direct în readme/ se copiază ca fișier.
    seen = set()
    for target in RE_LOCAL_LINK.findall(text):
        if target.startswith(("http", "screenshots/", "../")) or target in seen:
            continue
        seen.add(target)
        tpath = readme / target
        if not tpath.is_file():
            continue
        parts = Path(target).parts
        files = sorted((readme / parts[0]).rglob("*.md")) if len(parts) > 1 else [tpath]
        for f in files:
            rel = f.relative_to(readme)
            md, ch = rewrite_images(f.read_text(encoding="utf-8"), len(rel.parts) - 1, f.parent, readme, shots)
            changed |= ch | write_if_changed(dst / rel, md.encode("utf-8"))
    return changed


def plan(limit: int, dry_run: bool) -> None:
    today = dt.date.today().isoformat()
    excluded = set()
    if EXCLUDE.exists():
        excluded = {ln.strip() for ln in EXCLUDE.read_text().splitlines() if ln.strip() and not ln.startswith("#")}
    summary = {"date": today, "version": [], "fisa": [], "missing_source": [], "queued": []}
    candidates: list[tuple[int, str, dict]] = []
    known = set()

    for idx in sorted(WIKI.glob("*/index.md")):
        module = idx.parent.name
        known.add(module)
        text = idx.read_text(encoding="utf-8")
        local = RE_LOCAL.search(text)
        if not local:
            continue
        src = ROOT / local.group(1)
        suite = local.group(1).split("/")[1] if local.group(1).startswith("odoo-addons/") else None
        if suite not in SUITES:
            continue
        manifest = read_manifest(src / "__manifest__.py")
        if not manifest:
            if (ROOT / "odoo-addons" / suite).is_dir():
                summary["missing_source"].append(module)
            continue

        new_text = text
        version = manifest.get("version")
        cur = RE_VERSION.search(text)
        if version and cur and cur.group(2) != version:
            new_text = RE_VERSION.sub(lambda m: m.group(1) + version + m.group(3), new_text, count=1)
            summary["version"].append(f"{module} {cur.group(2)} → {version}")
        if not dry_run and sync_fisa(src, idx.parent):
            summary["fisa"].append(module)
            if RE_FISA_LINE not in new_text:
                new_text = RE_INGEST.sub(lambda m: m.group(0) + "\n" + RE_FISA_LINE, new_text, count=1)
        if new_text != text and not dry_run:
            idx.write_text(new_text, encoding="utf-8")

        if module in excluded:
            continue
        ingest = RE_INGEST.search(text)
        since = ingest.group(2) if ingest else "2000-01-01"
        suite_dir = ROOT / "odoo-addons" / suite
        has_desc = (src / "readme/DESCRIPTION.md").is_file()
        reason = None
        if set(manifest.get("depends", [])) != page_depends(text):
            reason, prio = "dependențele din manifest diferă de pagină", 1
        elif git_changed_since(suite_dir, module, since, README_PATHS):
            reason, prio = "readme modificat după ultima ingestie", 2
        elif not has_desc and git_changed_since(suite_dir, module, since, CODE_PATHS):
            reason, prio = "cod modificat, modul fără DESCRIPTION.md", 3
        if reason:
            candidates.append((prio, since, {"module": module, "path": local.group(1), "reason": reason}))

    for suite in SUITES:
        for manifest_path in sorted((ROOT / "odoo-addons" / suite).glob("*/__manifest__.py")):
            module = manifest_path.parent.name
            if module in known or module in excluded or module.startswith("test_"):
                continue
            if read_manifest(manifest_path).get("installable", True) is False:
                continue
            candidates.append((4, "", {"module": module, "path": f"odoo-addons/{suite}/{module}", "reason": "modul nou"}))

    candidates.sort(key=lambda c: (c[0], c[1], c[2]["module"]))
    queue = [c[2] for c in candidates[:limit]]
    summary["queued"] = queue
    summary["backlog"] = len(candidates)
    QUEUE.write_text(json.dumps(queue, ensure_ascii=False, indent=2), encoding="utf-8")
    SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"versiuni: {len(summary['version'])}, fișe: {len(summary['fisa'])}, "
          f"fără sursă: {len(summary['missing_source'])}, coadă AI: {len(queue)} din {len(candidates)}")


def update_index(entries: dict[str, str]) -> None:
    path = WIKI / "index.md"
    text = path.read_text(encoding="utf-8")
    head, _, body = text.partition("## Module\n")
    lines = [ln for ln in body.splitlines() if ln.strip()]
    items = {}
    for ln in lines:
        m = re.match(r"- \[([\w.]+)\]\(", ln)
        if m:
            items[m.group(1)] = ln
    for module, line in entries.items():
        items[module] = f"- [{module}]({module}/index.md): {line.strip()}"
    path.write_text(head + "## Module\n\n" + "\n".join(items[k] for k in sorted(items)) + "\n", encoding="utf-8")


def finalize() -> None:
    summary = json.loads(SUMMARY.read_text(encoding="utf-8")) if SUMMARY.exists() else {}
    report = json.loads(REPORT.read_text(encoding="utf-8")) if REPORT.exists() else []
    done = [r for r in report if (WIKI / r.get("module", "") / "index.md").is_file()]
    if done:
        update_index({r["module"]: r["line"] for r in done if r.get("line")})

    today = summary.get("date") or dt.date.today().isoformat()

    def listing(items: list[str], cap: int = 30) -> str:
        shown = ", ".join(f"`{i}`" for i in items[:cap])
        return shown + (f" și încă {len(items) - cap}" if len(items) > cap else "") + "."

    bullets = []
    if summary.get("version"):
        bullets.append(f"- **Versiuni aduse la zi** ({len(summary['version'])}): " + listing(summary["version"]))
    if summary.get("fisa"):
        bullets.append(f"- **Fișe consultant resincronizate** ({len(summary['fisa'])}): " + listing(summary["fisa"]))
    for r in done:
        note = f" {r['notes'].strip()}" if r.get("notes") else ""
        bullets.append(f"- **Reingestie AI:** [{r['module']}]({r['module']}/index.md) ({r.get('reason', '')}).{note}")
    failed = sorted({q["module"] for q in summary.get("queued", [])} - {r["module"] for r in done})
    if failed:
        bullets.append("- **Din coadă, neprocesate:** " + ", ".join(f"`{m}`" for m in failed) + ".")
    if summary.get("missing_source"):
        bullets.append("- **Pagini fără sursă (de verificat):** "
                       + ", ".join(f"`{m}`" for m in summary["missing_source"]) + ".")
    if summary.get("backlog") is not None:
        bullets.append(f"- **Rămase pentru nopțile următoare:** {max(summary['backlog'] - len(done), 0)}.")
    if not bullets:
        print("nimic de jurnalizat")
    else:
        log = WIKI / "log.md"
        text = log.read_text(encoding="utf-8")
        entry = f"## [{today}] Sincronizare automată de noapte\n\n" + "\n".join(bullets) + "\n\n"
        head, sep, rest = text.partition("---\n\n")
        log.write_text(head + sep + entry + rest if sep else text + "\n" + entry, encoding="utf-8")
    subprocess.run([sys.executable, str(WIKI / "scripts" / "wiki_index.py")], check=True)
    for tmp in (QUEUE, SUMMARY, REPORT):
        tmp.unlink(missing_ok=True)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("plan")
    p.add_argument("--limit", type=int, default=10)
    p.add_argument("--dry-run", action="store_true")
    sub.add_parser("finalize")
    args = ap.parse_args()
    if args.cmd == "plan":
        plan(args.limit, args.dry_run)
    else:
        finalize()


if __name__ == "__main__":
    main()
