# Schemă pentru Wiki Module Odoo

Acest document definește structura și convențiile pentru documentarea modulelor Odoo în cadrul acestui wiki. Asistentul LLM va urma aceste reguli în timpul operației de `ingestie`.

## Structura Paginii Modulului

Fiecare modul Odoo va avea propriul director markdown în directorul `wiki_module_odoo/`, numit `[module_name]/`. Documentația principală pentru modul va fi într-un fișier `index.md` în cadrul acelui director.

# [Nume Prietenesc Modul] (localizat la `[module_name]/index.md`)

- **Nume Tehnic:** `[module_name]`
- **Versiune:** `[VERSION]`
- **Cale:** URL-ul complet GitHub către directorul modulului (ex: `https://github.com/OWNER/REPO/tree/BRANCH/path/to/module`)
- **Cale Locală:** Calea relativă către directorul modulului din rădăcina monorepo-ului Odoo (ex: `odoo-addons/l10n_ro_ent/nume_modul`)
- **Ultima Ingestie:** `[AAAA-LL-ZZ]`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md) — *linie opțională, prezentă DOAR dacă modulul are `readme/FISA_CONSULTANT.md` (copiată în directorul wiki al modulului, vezi Fluxul de Ingestie).*

#### 1. Sumar

Un sumar concis, dintr-un singur paragraf, scris într-un limbaj simplu. Acesta ar trebui să explice scopul principal și valoarea de afaceri a modulului. Evitați jargonul tehnic.

#### 2. Funcționalități Cheie

O listă cu principalele funcționalități pe care modulul le oferă utilizatorului final.

- Funcționalitate A...
- Funcționalitate B...
- ...

#### 3. Dependențe

O listă cu alte module Odoo de care depinde direct acest modul. Aceasta ar trebui să provină din fișierul `__manifest__.py`. Fiecare dependență al cărei pagină wiki există deja trebuie să fie un **link Markdown activ** relativ către pagina sa (ex: `[account](../account/index.md)`). Modulele care **nu** au încă pagină wiki rămân ca text `cod` (ex: `account`, `l10n_ro`, `mail`).

- [dependency1](../dependency1/index.md)
- `dependency2`

#### 4. Componente Cheie

Această secțiune detaliază cele mai importante componente tehnice ale modulului.

**Modele**

O listă cu cele mai semnificative modele Odoo definite sau extinse de acest modul. Pentru fiecare model, furnizați o scurtă descriere a rolului său.

- `model.name` (ex: `account.asset`): Descrierea modelului.
- ...

**Vizualizări**

O listă cu vizualizările cheie (formulare, liste, kanban-uri) care oferă principalele interfețe de utilizator pentru acest modul.

- `view_xml_id`: Scurtă descriere a scopului vizualizării.
- ...

**Acțiuni Automate / Acțiuni Server**

O listă cu orice sarcini `ir.cron`, reguli `base.automation` sau înregistrări `ir.actions.server` definite în modul.

- `action_name`: Ce face și când rulează.
- ...

#### 5. Conexiuni

O listă de **link-uri Markdown active** către alte pagini de module care sunt funcțional legate de acesta, dar nu sunt dependențe stricte. Acest lucru ajută la înțelegerea ecosistemului mai larg. Folosiți căi relative către `index.md`-ul modulului țintă. Modulele fără pagină wiki rămân ca text `cod`.

- [related_module_a](../related_module_a/index.md): scurtă descriere a legăturii.
- [related_module_b](../related_module_b/index.md): scurtă descriere a legăturii.

---

## Flux de Ingestie

1.  **Prioritizarea Readme:** În primul rând, se caută un fișier `readme/DESCRIPTION.md` în directorul modulului.
    - Dacă este găsit:
        - Conținutul său este utilizat pentru secțiunile 'Sumar' și 'Funcționalități Cheie' ale paginii wiki.
        - **Se omite analiza suplimentară a codului pentru 'Componente Cheie' (Modele, Vizualizări, Acțiuni Automate / Acțiuni Server) cu excepția cazului în care este menționat explicit în Readme.**
    - Dacă nu este găsit, 'Sumarul' și 'Funcționalitățile Cheie' sunt sintetizate prin analiza descrierii din `__manifest__.py` și a codului modulului (modele, vizualizări).
    - **Sursă secundară — `readme/USAGE.md` / `readme/CONFIGURE.md`:** dacă există, se citesc și se folosesc pentru a **îmbogăți** secțiunea 'Funcționalități Cheie' cu detalii operaționale pe care `DESCRIPTION.md` de regulă nu le are — căi reale de meniu, semnificația câmpurilor dintr-un wizard, tipurile/valorile unei opțiuni, ordinea pașilor unui flux, formatul unui fișier generat. Nu se copiază fraze întregi din USAGE/CONFIGURE; se sintetizează la nivel de bullet, ca restul secțiunii.
      - Dacă modulul are deja `readme/FISA_CONSULTANT.md` (copiată integral la pasul 5), fluxul detaliat pas-cu-pas rămâne **acolo** — 'Funcționalități Cheie' preia doar esențialul (ex. valorile unei opțiuni-cheie), nu reface fișa. Evitați dublarea.
      - Dacă modulul **nu** are fișă consultant, USAGE/CONFIGURE devin sursa principală pentru orice detaliu operațional care altfel ar lipsi din pagină (ex. ce alege operatorul într-un wizard, ce meniu accesează).
2.  **Fișier Manifest:** Se citește fișierul `__manifest__.py` pentru a obține numele prietenesc, numele tehnic, dependențele și calea.
3.  **Analiza Codului (pentru componente - DOAR dacă Readme-ul nu este prezent sau nu acoperă aceste secțiuni):**
    - Se scanează directorul `models/` pentru a identifica modelele cheie pentru secțiunea 'Componente Cheie'.
    - Se scanează directorul `views/` pentru a identifica vizualizările cheie pentru secțiunea 'Componente Cheie'.
    - Se scanează fișierele de date (`data/*.xml`) pentru acțiuni automate și acțiuni server pentru secțiunea 'Componente Cheie'.
4.  **Crearea Paginii:** Se sintetizează toate informațiile colectate pentru a popula o nouă pagină conform structurii de mai sus.
5.  **Copierea Fișei Consultant (dacă există):** Dacă modulul are `readme/FISA_CONSULTANT.md`:
    - Se copiază fișa în `[module_name]/FISA_CONSULTANT.md` (copie fidelă, fără modificări de conținut).
    - Se copiază integral directorul `readme/screenshots/` în `[module_name]/screenshots/` — pozele sunt referite relativ din fișă (`screenshots/*.png`), deci link-urile rămân funcționale după copiere.
    - Se adaugă în pagina modulului linia de metadate `- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)`.
    - La re-ingestie, copia din wiki se suprascrie cu versiunea curentă din modul (fișa din `readme/` e sursa de adevăr).
6.  **Actualizarea Indexului:** Se adaugă noua pagină la `index.md`.
7.  **Actualizarea Jurnalului:** Se adaugă o înregistrare a ingestiei la `log.md`.
