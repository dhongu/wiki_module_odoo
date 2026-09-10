---
name: demo-odoosh
description: Creează pentru un client o instanță temporară de demo/test cu module Terrabit, ca branch de dezvoltare pe proiectul odoo.sh `terrabit` (repo terrabit-ro/terrabit-erp) — branch per client, login admin/admin pus de un modul generat (sau parolă aleatorie la cerere), lista de module restrânsă la ce se demonstrează, reîmprospătare (keepalive) cât durează testul și ștergere la final. Se declanșează la cereri precum „clientul X vrea să testeze modulul Y", „fă un demo pentru modulul ...", „instanță de test pentru client", „dă-i clientului un link să încerce modulul", „prelungește demo-ul lui X", „șterge demo-ul lui X", „ce demo-uri sunt active".
---

# demo-odoosh — instanțe de demo per client pe odoo.sh

Scop: un client vrea să încerce unul sau mai multe module Terrabit înainte să le cumpere sau să le
implementeze. Îi dăm **propriul build de dev** pe proiectul odoo.sh `terrabit`, cu un URL și o parolă
doar ale lui. Credențialele pe care le introduce el în test (Kramp, curieri, ANAF, marketplace) rămân
în baza acelui build și dispar odată cu branch-ul.

Scriptul `scripts/demo_branch.py` din acest skill face toată partea de git. Rămân două lucruri pe care
le face agentul în browser (odoo.sh nu are API): setarea listei de module pe branch și preluarea URL-ului.

## Cum funcționează (ca să știi ce să aștepți)

- Proiectul odoo.sh `terrabit` are ca submodule toate suitele Terrabit. Un push pe un branch nou
  produce un **build de dev** cu bază proprie și date demo, izolat de producție (`main`).
- Build-urile de dev instalează implicit **toate modulele din rădăcina repo-ului** (inclusiv cele
  interne ale Terrabit) și rulează testele → ~10 minute și teste roșii. De aceea setăm pe branch
  „A specific list of modules” cu **un singur modul**: `terrabit_demo_<client>`, generat de script,
  care trage prin `depends` doar modulele de demonstrat.
- Același modul are un `post_init_hook` care **pune parola admin** (build-urile de dev O19 NU acceptă
  admin/admin de la sine): implicit `admin`, sau aleatorie cu `--password random`. Dezactivează și userul `demo`. Opțional (`--ro`) creează o companie RO cu planul de
  conturi românesc, fiindcă datele demo sunt US/USD.
- Un build de dev **trăiește 24–48 h**. `keepalive` face un push gol → build nou. Datele introduse de
  client NU se păstrează între build-uri; spune-i asta.
- Intrarea noastră în build e prin butonul **Connect** din odoo.sh (`/_odoo/paas/connect`), fără parolă.

## Cerințe

- `git` cu acces SSH la `terrabit-ro/terrabit-erp` (push) și `gh` CLI autentificat (căutarea
  modulelor pe GitHub când nu există monorepo-ul local).
- Browser (claude-in-chrome) logat pe odoo.sh cu drepturi pe proiectul `terrabit`.
- Scriptul merge din orice director: dacă rulează în monorepo-ul odoo19 folosește `proiecte/terrabit-erp`
  și `odoo-addons/`, altfel clonează `terrabit-erp` în `~/.cache/terrabit-demo` și caută modulele pe GitHub.

## Flux: demo nou

### 1. Clarifică cererea (fără să blochezi)
Identificator client (scurt, ex. `agrotrac`), lista de module, dacă are nevoie de context RO
(`--ro` pentru orice modul fiscal, de stoc valorizat sau de facturare). Dacă modulul cere un cont la
un terț (Kramp, Sameday, eMAG...), notează că clientul trebuie să aibă propriile credențiale.

### 2. Rulează scriptul
```bash
python3 <cale-skill>/scripts/demo_branch.py create <client> <modul1,modul2> [--ro] [--name "Nume Client"] [--password random]
```
Alege `--password random` când clientul va introduce credențiale de terți (Kramp, curieri, ANAF):
URL-ul build-ului e public și ghicibil, iar admin/admin l-ar deschide oricui.
Scriptul: verifică că modulele există (local sau pe GitHub), adaugă submodulul suitei dacă lipsește
din proiect, generează `terrabit_demo_<client>` cu parola, face commit pe `demo-<client>-<data>` din
`origin/main` și push. Afișează **branch, modulul de instalat, parola** și pașii rămași.

⚠️ Dacă afișează „submodule private fără cheie înregistrată în odoo.sh”, oprește-te și rulează
skill-ul `odoosh-chei-subrepo` pentru acel repo (Settings → Submodules → Add + deploy key pe GitHub),
altfel build-ul pică la clone.

### 3. Setează lista de module pe branch (browser)
Deschide `https://www.odoo.sh/project/terrabit/branches/<branch>/settings` și:
1. debifează „Use default development branch settings”;
2. alege „A specific list of modules” și scrie exact `terrabit_demo_<client>`;
3. alege „Disable the test suite”; lasă „Install demo data” bifat.
Setările se salvează automat („Changes saved”). Verifică starea cu JS, nu după coordonate — pagina se
re-randează:
```js
JSON.stringify([...document.querySelectorAll('input[type=radio],input[type=checkbox]')].map(i=>({l:i.parentElement.textContent.trim().slice(0,40),c:i.checked})))
```
Capcană: pe pagina de Settings a proiectului există două butoane „Add”; pe pagina branch-ului
iconița rotundă de pe cardul build-ului e link spre commitul GitHub, NU rebuild.

### 4. Pornește build-ul corect
Primul build (declanșat de push) a plecat cu setările implicite. Declanșează unul nou:
```bash
python3 <cale-skill>/scripts/demo_branch.py keepalive --branch <branch>
```
Build-ul durează ~3–5 minute pentru un modul obișnuit. Urmărește la
`https://www.odoo.sh/project/terrabit/builds/<branch>`; starea „warning” e normală pe dev.

### 5. Verifică și ia URL-ul
Din pagina Builds ia linkul Connect al **build-ului cel mai nou** (id mai mare):
```js
JSON.stringify([...document.querySelectorAll('a[href*="dev.odoo.com"]')].map(a=>a.href))
```
URL-ul clientului e `https://terrabit-<branch>-<id>.dev.odoo.com`. Intră prin Connect și verifică
prin RPC din pagină că modulele sunt `installed` și că `deltatech_terrabit` NU e:
```js
const r=await fetch('/web/dataset/call_kw',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({jsonrpc:'2.0',id:1,params:{model:'ir.module.module',method:'search_read',args:[[['name','in',['<modul>','deltatech_terrabit']]]],kwargs:{fields:['name','state']}}})});(await r.json()).result
```
Nu seta și nu citi parole prin RPC — parola e cea afișată de script (implicit `admin`).

### 6. Mesajul către client
Scurt, fără nume în salut (convenția Terrabit), pe două canale separate: URL-ul într-un mesaj, parola
în altul. Include obligatoriu:
- login `admin` + parola; cu admin/admin, cere-i explicit să o schimbe la prima intrare dacă introduce
  credențiale proprii;
- unde e funcționalitatea (meniul), în 1–2 rânduri;
- mediul e temporar: se reface la ~2 zile și **datele introduse nu se păstrează**; fără date reale;
- până când e disponibil și pe cine să întrebe.

## Flux: întreținere și închidere

```bash
python3 <cale-skill>/scripts/demo_branch.py list                   # demo-urile active, vârsta ultimului commit
python3 <cale-skill>/scripts/demo_branch.py keepalive              # push gol pe cele mai vechi de 36 h
python3 <cale-skill>/scripts/demo_branch.py delete <branch>        # șterge branch-ul → odoo.sh șterge baza
```
După `keepalive` URL-ul se schimbă (alt id de build) — trimite-l din nou clientului. La `delete`
dispar și modulul cu parola, și baza cu credențialele lui.

## Ce NU face acest skill
- Nu atinge `main`/`staging`/producția: lucrează într-un worktree temporar și împinge doar `demo-*`.
- Nu pune chei de deploy (vezi `odoosh-chei-subrepo`) și nu se conectează la bazele clienților
  (vezi `conectare-agent-claudiu`).
- Nu oferă demo permanent: pentru un mediu care trebuie să țină săptămâni, discută un server demo
  propriu sau un branch de staging.
