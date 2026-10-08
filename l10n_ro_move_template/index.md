# Romania - Șabloane note contabile (localizat la `l10n_ro_move_template/index.md`)

- **Nume Tehnic:** `l10n_ro_move_template`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_move_template
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_move_template`
- **Ultima Ingestie:** `2026-10-08`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite contabilului să definească o singură dată șabloane de note contabile și să genereze apoi notele dintr-un asistent, introducând doar sumele de bază și data. În Odoo standard se poate doar duplica o notă existentă și modifica fiecare linie. Modulul vine și cu zece șabloane românești gata făcute (salarii, chirie, amortizare, comodat, TVA la încasare), validate pe planul de conturi RO.

#### 2. Funcționalități Cheie

- Un șablon are jurnal, referință implicită, instrucțiuni pentru operator și linii cu cont, etichetă, partener opțional, distribuție analitică, taxe sau grile de taxe și sens (debit sau credit).
- Fiecare linie are un cod (de ex. `GROSS`; dacă rămâne gol se completează automat `L1`, `L2`...) și un tip de sumă:
  - **Introdusă**: se completează la generare; valoarea propusă poate fi o sumă fixă sau o formulă (de ex. `GROSS * 0.25`), pe care operatorul o poate înlocui (dezactivând **Propusă** în asistent);
  - **Fixă**: întotdeauna aceeași sumă;
  - **Procent**: un procent dintr-o altă linie (**Codul de bază**);
  - **Formulă**: expresie Python pe codurile celorlalte linii, cu `round`, `abs`, `min`, `max`;
  - **Sold**: suma care închide nota, inclusiv taxele (cel mult o linie pe șablon).
- Liniile fără cont sunt parametri de calcul (o sumă cu TVA, o cotă): se introduc sau se calculează, dar nu se înregistrează.
- Ordinea de calcul urmează formulele, nu ordinea liniilor; codurile necunoscute, buclele între formule și formulele care folosesc linia de sold sunt refuzate la salvarea șablonului.
- Taxele de pe o linie funcționează ca pe o notă manuală: Odoo adaugă liniile de TVA cu grilele lor, deci nota intră în decontul de TVA, iar linia de sold include taxa.
- O sumă negativă trece pe partea cealaltă a contului; liniile cu sumă zero sunt omise.
- Generarea se face din **Facturare → Contabilitate → Tranzacții → Notă din șablon** sau cu butonul **Generează nota** de pe șablon; se aleg șablonul, data, referința și partenerul (pus pe liniile fără partener), apoi nota se poate lăsa în ciornă sau valida imediat (**Validează nota**).
- Nota generată rămâne legată de șablon: filtrul **Din șablon** pe notele contabile și butonul **Note** pe șablon.
- Șabloanele se administrează din **Configurare → Contabilitate → Șabloane note contabile**; butonul **Încarcă șabloanele românești** creează cele zece șabloane: chirie la chiriaș și la locator, amortizare manuală (corporale și necorporale), bunuri primite în folosință (comodat sau chirie, în afara bilanțului; la nevoie se creează contul tehnic de contrapartidă 800000), salarii dintr-un stat de plată extern, tichete de masă și exigibilizarea / deducerea TVA la încasare. Șabloanele pentru care lipsește un cont din plan sunt omise, iar o nouă încărcare nu creează dubluri.
- Fluxul pas-cu-pas, cu capturi de ecran, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.move.template`: șablonul de notă contabilă (nume unic per companie, jurnal, referință, instrucțiuni, linii); validează codurile, buclele și formulele la salvare. Extins în `models/ro_templates.py` cu încărcarea șabloanelor românești.
- `l10n.ro.move.template.line`: linia șablonului (cont, sens, tip sumă, cod, formulă, taxe/grile, distribuție analitică prin `analytic.mixin`).
- `l10n.ro.move.template.run` / `l10n.ro.move.template.run.line`: asistentul tranzitoriu care primește sumele, calculează liniile și generează nota.
- `account.move` (extins): legătura notei cu șablonul de origine.

**Vizualizări**

- `view_l10n_ro_move_template_list` / `_form` / `_search`: lista, formularul și căutarea șabloanelor.
- `view_l10n_ro_move_template_run_form`: asistentul „Notă din șablon”.
- `view_move_form` / `view_account_move_filter`: câmpul și filtrul **Din șablon** pe notele contabile.

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau acțiuni server; singurele acțiuni sunt cele de fereastră (`action_l10n_ro_move_template`, `action_l10n_ro_move_template_run`).

#### 5. Conexiuni

- [l10n_ro_payroll_import](../l10n_ro_payroll_import/index.md): importul fișierului de notă salarii (FR-13); șablonul de salarii din acest modul este varianta cu sume introduse manual din statul de plată extern.
- [l10n_ro_deferred_entries](../l10n_ro_deferred_entries/index.md): înregistrările 471/472 se generează automat acolo; șabloanele de aici acoperă cazurile manuale.
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): grilele de taxe puse pe liniile șablonului (TVA la încasare) ajung în decontul D300.
- [l10n_ro_stock_consignment](../l10n_ro_stock_consignment/index.md): alte contrapartide tehnice în afara bilanțului (8039).
- [l10n_ro_inventory_items](../l10n_ro_inventory_items/index.md): alte contrapartide tehnice în afara bilanțului (8035C), alături de contul 800000 din șabloanele de comodat.
- `account_move_template` (OCA): modul similar; modelele de aici sunt `l10n.ro.move.template*`, deci cele două pot coexista.
