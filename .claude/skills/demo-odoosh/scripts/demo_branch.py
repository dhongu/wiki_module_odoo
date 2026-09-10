#!/usr/bin/env python3
"""Branch-uri temporare de demo pe proiectul odoo.sh `terrabit` (repo terrabit-ro/terrabit-erp).

Fiecare client primește propriul branch `demo-<client>-<data>` și propriul build de dev,
cu parola de admin pusă de un modul generat (`terrabit_demo_<client>`): implicit `admin`,
fiindcă build-urile de dev O19 nu acceptă admin/admin de la sine; `--password X` pentru alta,
`--password random` pentru una aleatorie (recomandat când clientul introduce credențiale de terți).
Credențialele pe care le introduce clientul (Kramp, curieri, ANAF) rămân în baza acelui
build și dispar odată cu branch-ul.

Subcomenzi:
  create   <client> <module,...> [--ro | --ro-fiscal] [--name "Nume Client"]
           [--password X|random] [--no-push]
  list                              branch-urile demo-* de pe origin, cu vârsta ultimului commit
  keepalive [--older-than ORE]      push gol pe branch-urile demo-* mai vechi de N ore (implicit 36)
  refresh  <branch>                 regenerează modulul de demo din șablon pe un branch existent
  delete   <branch>                 șterge branch-ul de pe origin (odoo.sh șterge și baza)

Lucrează într-un git worktree separat sub /tmp, ca să nu atingă checkout-ul din proiecte/terrabit-erp.
Merge și fără monorepo-ul odoo19: clonează terrabit-erp în ~/.cache/terrabit-demo și caută
modulele pe GitHub cu `gh` CLI.
"""
import argparse
import ast
import json
import re
import secrets
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEMPLATE_DIR = HERE / "demo_module_template"
PROJECT_REPO = "git@github.com:terrabit-ro/terrabit-erp.git"
ODOOSH_PROJECT = "terrabit"
CACHE_DIR = Path.home() / ".cache" / "terrabit-demo"


def _find_monorepo():
    """Rădăcina monorepo-ului odoo19, dacă scriptul rulează lângă el (opțional)."""
    for cand in [Path.cwd(), *Path.cwd().parents, *HERE.parents]:
        if (cand / "odoo" / "odoo-bin").exists() and (cand / "odoo-addons").exists():
            return cand
    return None


MONOREPO = _find_monorepo()
ADDONS_ROOT = MONOREPO / "odoo-addons" if MONOREPO else None
STANDARD_DIRS = (
    [MONOREPO / "odoo" / "addons", MONOREPO / "odoo" / "odoo" / "addons", MONOREPO / "enterprise"] if MONOREPO else []
)
# Fără monorepo local, modulele se caută pe GitHub (gh CLI) în aceste suite.
KNOWN_SUITES = [
    "terrabit-solutions/bitshop",
    "terrabit-solutions/bitshop_ent",
    "terrabit-solutions/bitshop_vendor",
    "terrabit-solutions/bitshop_delivery",
    "terrabit-solutions/bitshop_marketplace",
    "terrabit-solutions/terrabit",
    "terrabit-solutions/l10n_ro_ent",
    "dhongu/deltatech",
    "dhongu/deltatech_service",
    "dhongu/deltatech_stock_valuation",
    "dhongu/others_addons",
    "dhongu/l10n-romania",
    "OCA/l10n-romania",
]
STANDARD_REPOS = ["odoo/odoo:addons", "odoo/enterprise:"]


def _project_dir():
    if MONOREPO and (MONOREPO / "proiecte" / "terrabit-erp" / ".git").exists():
        return MONOREPO / "proiecte" / "terrabit-erp"
    clone = CACHE_DIR / "terrabit-erp"
    if not (clone / ".git").exists():
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        print(f"clonez {PROJECT_REPO} în {clone} (o singură dată)")
        sh(["git", "clone", "--quiet", "--no-checkout", PROJECT_REPO, str(clone)])
    return clone


PROJECT_DIR = None  # se completează în main(), după ce sh() e definit
PRIVATE_OWNERS = {"terrabit-solutions", "terrabit-ro"}
# Convenția din .gitmodules al proiectului: repo-urile terrabit-solutions stau sub terrabit-ro/.
PATH_OWNER = {"terrabit-solutions": "terrabit-ro"}
# Suite locale al căror remote diferă de ce folosește proiectul.
SUITE_OVERRIDE = {"l10n-romania-oca": "OCA/l10n-romania"}


def sh(cmd, cwd=None, check=True, capture=True):
    res = subprocess.run(cmd, cwd=cwd, check=False, text=True, capture_output=capture)
    if check and res.returncode:
        sys.exit(f"eroare: {' '.join(cmd)}\n{res.stderr or res.stdout}")
    return (res.stdout or "").strip()


def slugify(text):
    slug = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    if not slug:
        sys.exit("eroare: numele clientului nu produce un identificator valid")
    return slug


def _gh_exists(owner_repo, path):
    res = subprocess.run(
        ["gh", "api", f"repos/{owner_repo}/contents/{path}?ref=19.0", "--silent"],
        capture_output=True, text=True,
    )
    return res.returncode == 0


def find_module(name):
    """Întoarce ('standard', None) sau ('suite', 'owner/repo') sau iese cu eroare.

    Cu monorepo local caută pe disc; altfel întreabă GitHub prin `gh` pentru fiecare suită cunoscută.
    """
    if MONOREPO:
        for d in STANDARD_DIRS:
            if (d / name / "__manifest__.py").exists():
                return "standard", None
        hits = [p.parent.parent for p in ADDONS_ROOT.glob(f"*/{name}/__manifest__.py")]
        if not hits:
            sys.exit(f"eroare: modulul '{name}' nu există nici în standard, nici în odoo-addons/*")
        if len(hits) > 1:
            print(f"atenție: '{name}' există în mai multe suite {[h.name for h in hits]}, o folosesc pe prima")
        return "suite", suite_owner_repo(hits[0])
    if shutil.which("gh") is None:
        sys.exit("eroare: fără monorepo local am nevoie de `gh` CLI autentificat ca să găsesc modulele")
    for spec in STANDARD_REPOS:
        repo, sub = spec.split(":")
        if _gh_exists(repo, f"{sub + '/' if sub else ''}{name}/__manifest__.py"):
            return "standard", None
    for suite in KNOWN_SUITES:
        if _gh_exists(suite, f"{name}/__manifest__.py"):
            return "suite", suite
    sys.exit(f"eroare: modulul '{name}' nu e în standard și nu l-am găsit în suitele cunoscute {KNOWN_SUITES}")


def suite_owner_repo(suite_dir):
    if suite_dir.name in SUITE_OVERRIDE:
        return SUITE_OVERRIDE[suite_dir.name]
    remote = sh(["git", "-C", str(suite_dir), "remote", "get-url", "origin"])
    m = re.search(r"github\.com[:/]([^/]+)/([^/.]+?)(?:\.git)?$", remote)
    if not m:
        sys.exit(f"eroare: nu recunosc remote-ul suitei {suite_dir}: {remote}")
    return f"{m.group(1)}/{m.group(2)}"


def suite_submodule(owner_repo):
    """(cale în proiect, url) pentru suita `owner/repo`, după convenția proiectului."""
    owner, repo = owner_repo.split("/")
    path = f"{PATH_OWNER.get(owner, owner)}/{repo}"
    if owner in PRIVATE_OWNERS:
        url = f"git@github.com:{owner}/{repo}.git"
    else:
        url = f"https://github.com/{owner}/{repo}.git"
    return path, url


def existing_submodules(worktree):
    out = sh(["git", "config", "-f", ".gitmodules", "--get-regexp", r"submodule\..*\.url"], cwd=worktree, check=False)
    result = {}
    for line in out.splitlines():
        key, url = line.split(" ", 1)
        name = key[len("submodule.") : -len(".url")]
        path = sh(["git", "config", "-f", ".gitmodules", f"submodule.{name}.path"], cwd=worktree)
        result[repo_key(url)] = path
    return result


def repo_key(url):
    m = re.search(r"github\.com[:/]([^/]+)/([^/.]+)", url)
    return m.group(2).lower() if m else url


def odoosh_key_registered(repo_name):
    keys = PROJECT_DIR / "odoosh-keys.json"
    if not keys.exists():
        return True  # fără registru local nu putem ști; nu alarmăm degeaba
    return any(k.split("/")[-1].lower() == repo_name.lower() for k in json.load(open(keys)))


# Dependența adusă de fiecare mod RO: modul „fiscal" trage l10n_ro_anaf_base, ale cărui date
# demo pun cazurile fiscale (taxare inversă, intracomunitar, TVA la încasare) pe compania demo RO.
RO_MODE_DEPEND = {"own": "l10n_ro", "fiscal": "l10n_ro_anaf_base"}


def render_template(dst, client_slug, client_name, modules, password, ro_company, ro_mode=None):
    depends = list(dict.fromkeys(modules))  # ordine stabilă, fără dubluri
    ro_depend = RO_MODE_DEPEND.get(ro_mode)
    if ro_depend and ro_depend not in depends:
        depends.insert(0, ro_depend)
    repl = {
        "__CLIENT_NAME__": client_name,
        "__MODULES_HUMAN__": ", ".join(modules),
        "__DEPENDS__": json.dumps(depends),
        "__ADMIN_PASSWORD__": password,
        "__RO_MODE__": json.dumps(ro_mode) if ro_mode else "None",
        "__RO_COMPANY_NAME__": json.dumps(ro_company) if ro_company else "None",
    }
    repl["__MODULE__"] = dst.name
    for src in TEMPLATE_DIR.rglob("*"):
        if src.is_dir() or "__pycache__" in src.parts:
            continue
        text = src.read_text()
        for k, v in repl.items():
            text = text.replace(k, v)
        out = dst / src.relative_to(TEMPLATE_DIR)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text)


def gen_password():
    alphabet = "abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    return "Demo-" + "".join(secrets.choice(alphabet) for _ in range(14))


def with_worktree(branch, start_point, fn):
    sh(["git", "fetch", "origin", "--quiet"], cwd=PROJECT_DIR)
    tmp = Path(tempfile.mkdtemp(prefix="demo-branch-"))
    wt = tmp / "wt"
    try:
        sh(["git", "worktree", "add", "-b", branch, str(wt), start_point], cwd=PROJECT_DIR)
        return fn(wt)
    finally:
        sh(["git", "worktree", "remove", "--force", str(wt)], cwd=PROJECT_DIR, check=False)
        sh(["git", "branch", "-D", branch], cwd=PROJECT_DIR, check=False)
        shutil.rmtree(tmp, ignore_errors=True)


def cmd_create(args):
    client_slug = slugify(args.client)
    client_name = args.name or args.client
    modules = [m.strip() for m in args.modules.split(",") if m.strip()]
    if not modules:
        sys.exit("eroare: lista de module e goală")
    branch = f"demo-{client_slug.replace('_', '-')}-{datetime.now():%Y%m%d}"
    glue = f"terrabit_demo_{client_slug}"
    password = gen_password() if args.password == "random" else args.password
    ro_mode = "fiscal" if args.ro_fiscal else ("own" if args.ro else None)
    ro_company = f"{client_name} Demo SRL" if ro_mode else None

    needed = {}
    for mod in modules:
        kind, owner_repo = find_module(mod)
        if kind == "suite":
            needed[owner_repo] = suite_submodule(owner_repo)

    def work(wt):
        present = existing_submodules(wt)
        missing_keys = []
        for suite, (path, url) in needed.items():
            key = repo_key(url)
            if key in present:
                continue
            print(f"+ submodul nou {path} <- {url}")
            sh(["git", "submodule", "add", "-b", "19.0", url, path], cwd=wt)
            if url.startswith("git@") and not odoosh_key_registered(key):
                missing_keys.append(url)
        if (wt / glue).exists():
            sys.exit(f"eroare: {glue} există deja pe main; șterge-l sau alege alt client")
        render_template(wt / glue, client_slug, client_name, modules, password, ro_company, ro_mode)
        sh(["git", "add", "-A"], cwd=wt)
        msg = (
            f"[DEMO] {branch}: {', '.join(modules)}\n\n"
            f"Branch temporar de demo pentru {client_name}. Modulul {glue} pune parola admin\n"
            f"și restrânge instalarea la modulele cerute. Se șterge după test.\n\n"
            f"Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
        )
        sh(["git", "commit", "--quiet", "-m", msg], cwd=wt)
        if args.no_push:
            print(f"(fără push) commit pregătit pe {branch} în worktree-ul temporar; se pierde la ieșire")
        else:
            sh(["git", "push", "--quiet", "-u", "origin", branch], cwd=wt)
        return missing_keys

    missing_keys = with_worktree(branch, "origin/main", work)

    print("\n" + "=" * 72)
    print(f"Branch:            {branch}")
    print(f"Modul de instalat: {glue}   (pune EXACT acesta în lista de module a branch-ului)")
    print(f"Parola admin:      {password}   (login: admin)")
    if password == "admin":
        print("                   URL-ul e public și ghicibil: dacă clientul introduce credențiale de terți,")
        print("                   cere-i să schimbe parola la prima intrare sau refă cu --password random.")
    if ro_mode == "fiscal":
        print("Companie RO:       RO Company (demo standard) + cazurile fiscale din l10n_ro_anaf_base")
        print("                   21%/11%, taxare inversă, IC bunuri/servicii, TVA la încasare, plus seed comercial")
    elif ro_mode == "own":
        print(f"Companie RO:       {ro_company} (plan de conturi ro, RON) + seed comercial")
    print(f"Setări branch:     https://www.odoo.sh/project/{ODOOSH_PROJECT}/branches/{branch}/settings")
    print(f"Build-uri:         https://www.odoo.sh/project/{ODOOSH_PROJECT}/builds/{branch}")
    print("=" * 72)
    print(
        "Pași rămași pe odoo.sh:\n"
        "  1. Branch → Settings → debifează „Use default development branch settings”,\n"
        f"     alege „A specific list of modules” și scrie: {glue}; dezactivează testele.\n"
        "  2. Primul build (pornit la push) folosește setările implicite; după pasul 1 rulează\n"
        f"     `{Path(__file__).name} keepalive --branch {branch}` ca să pornești build-ul corect.\n"
        "  3. Așteaptă ~1–2 min după „done”: odoo.sh rescrie parola admin, cronul modulului o reimpune.\n"
        "  4. Trimite clientului URL-ul build-ului (Connect → adresa) și parola, pe canale separate.\n"
        "  Build-ul de dev trăiește 24–48h: `keepalive` îl reîmprospătează cât durează testul."
    )
    if missing_keys:
        print("\nATENȚIE: submodule private fără cheie înregistrată în odoo.sh (build-ul va pica la clone):")
        for url in missing_keys:
            print(f"  - {url}  → Settings → Submodules → Add, apoi skill `odoosh-chei-subrepo`")


def cmd_refresh(args):
    """Regenerează modulul de demo pe un branch existent (după o schimbare de șablon), fără să
    atingă setările branch-ului din odoo.sh."""
    branch = args.branch

    def work(wt):
        glue = next((p.parent for p in wt.glob("terrabit_demo_*/demo_config.py")), None)
        if not glue:
            sys.exit(f"eroare: pe {branch} nu există un modul terrabit_demo_*")
        ns = {}
        exec(glue.joinpath("demo_config.py").read_text(), ns)  # noqa: S102 — fișier generat de noi
        manifest = ast.literal_eval(glue.joinpath("__manifest__.py").read_text().split("\n", 1)[1])
        client_slug = glue.name[len("terrabit_demo_"):]
        client_name = manifest["name"].split(" - ", 1)[-1]
        # Compatibil cu branch-urile generate înainte de RO_MODE: prezența numelui de companie
        # însemna pe atunci modul „own".
        ro_mode = ns.get("RO_MODE") or ("own" if ns.get("RO_COMPANY_NAME") else None)
        ro_depend = RO_MODE_DEPEND.get(ro_mode)
        modules = [d for d in manifest["depends"] if d != ro_depend]
        shutil.rmtree(glue)
        render_template(
            glue, client_slug, client_name, modules, ns["ADMIN_PASSWORD"], ns.get("RO_COMPANY_NAME"), ro_mode
        )
        sh(["git", "add", "-A"], cwd=wt)
        if not sh(["git", "status", "--porcelain"], cwd=wt):
            print("modulul e deja la zi; nimic de împins")
            return
        sh(["git", "commit", "--quiet", "-m",
            f"[DEMO] {branch}: regenerare {glue.name} din șablon\n\n"
            "Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"], cwd=wt)
        sh(["git", "push", "--quiet", "origin", f"HEAD:{branch}"], cwd=wt)
        print(f"{glue.name} regenerat și împins pe {branch} → build nou")

    with_worktree(f"_rf_{branch}", f"origin/{branch}", work)


def remote_demo_branches():
    out = sh(["git", "ls-remote", "--heads", "origin", "refs/heads/demo-*"], cwd=PROJECT_DIR)
    return [line.split("refs/heads/")[1] for line in out.splitlines() if line.strip()]


def branch_age_hours(branch):
    sh(["git", "fetch", "origin", "--quiet", branch], cwd=PROJECT_DIR)
    ts = int(sh(["git", "log", "-1", "--format=%ct", f"origin/{branch}"], cwd=PROJECT_DIR))
    return (datetime.now(timezone.utc).timestamp() - ts) / 3600


def cmd_list(args):
    sh(["git", "fetch", "origin", "--quiet"], cwd=PROJECT_DIR)
    branches = remote_demo_branches()
    if not branches:
        print("niciun branch demo-* pe origin")
        return
    for b in branches:
        print(f"{b:45s} ultimul commit: {branch_age_hours(b):6.1f} h")


def keepalive_branch(branch):
    def work(wt):
        sh(
            [
                "git", "commit", "--quiet", "--allow-empty", "-m",
                f"[KEEPALIVE] {branch}: build nou pentru demo\n\n"
                "Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>",
            ],
            cwd=wt,
        )
        sh(["git", "push", "--quiet", "origin", f"HEAD:{branch}"], cwd=wt)

    with_worktree(f"_ka_{branch}", f"origin/{branch}", work)
    print(f"push gol pe {branch} → build nou")


def cmd_keepalive(args):
    sh(["git", "fetch", "origin", "--quiet"], cwd=PROJECT_DIR)
    if args.branch:
        targets = [args.branch]
    else:
        targets = [b for b in remote_demo_branches() if branch_age_hours(b) >= args.older_than]
    if not targets:
        print(f"nimic de reîmprospătat (niciun demo-* mai vechi de {args.older_than} h)")
    for b in targets:
        keepalive_branch(b)


def cmd_delete(args):
    if not args.branch.startswith("demo-"):
        sys.exit("eroare: șterg doar branch-uri demo-*")
    sh(["git", "push", "--quiet", "origin", "--delete", args.branch], cwd=PROJECT_DIR)
    print(f"{args.branch} șters de pe origin; odoo.sh elimină branch-ul și baza build-ului")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("create", help="branch de demo nou pentru un client")
    c.add_argument("client", help="identificator client, ex. agrotrac")
    c.add_argument("modules", help="module de demonstrat, separate prin virgulă")
    c.add_argument("--name", help="numele afișat al clientului (implicit = identificatorul)")
    ro = c.add_mutually_exclusive_group()
    ro.add_argument("--ro", action="store_true", help="companie RO proprie cu planul de conturi românesc + seed comercial")
    ro.add_argument(
        "--ro-fiscal",
        action="store_true",
        help="compania demo RO standard cu cazurile fiscale din l10n_ro_anaf_base (taxare inversă, IC, TVA la încasare) + seed comercial",
    )
    c.add_argument("--password", default="admin", help="parola admin: implicit 'admin'; 'random' pentru una aleatorie")
    c.add_argument("--no-push", action="store_true", help="pregătește commit-ul fără push (test)")
    c.set_defaults(fn=cmd_create)
    sub.add_parser("list", help="branch-urile demo-* de pe origin").set_defaults(fn=cmd_list)
    k = sub.add_parser("keepalive", help="push gol pe branch-urile demo-* vechi")
    k.add_argument("--older-than", type=float, default=36, help="ore (implicit 36)")
    k.add_argument("--branch", help="doar acest branch, indiferent de vârstă")
    k.set_defaults(fn=cmd_keepalive)
    rf = sub.add_parser("refresh", help="regenerează modulul de demo pe un branch existent (șablon nou)")
    rf.add_argument("branch")
    rf.set_defaults(fn=cmd_refresh)
    d = sub.add_parser("delete", help="șterge un branch demo-* de pe origin")
    d.add_argument("branch")
    d.set_defaults(fn=cmd_delete)
    args = p.parse_args()
    global PROJECT_DIR
    PROJECT_DIR = _project_dir()
    args.fn(args)


if __name__ == "__main__":
    main()
