# Romania - Șabloane note contabile

- **Nume Tehnic:** `l10n_ro_move_template`
- **Versiune:** `20.0.1.0.5`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_move_template
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_move_template`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Contabilul definește o singură dată șabloane de note contabile și generează apoi notele dintr-un asistent, introducând doar data și sumele de bază. Odoo standard permite doar duplicarea unei note existente și modificarea fiecărei linii; aici restul liniilor se calculează, iar nota iese echilibrată. Modulul livrează și zece șabloane românești gata de folosit (salarii, chirie, amortizare, comodat, TVA la încasare).

#### 2. Funcționalități Cheie

- Șablon cu jurnal, referință implicită, instrucțiuni pentru operator și linii cu cont, etichetă, partener opțional, distribuție analitică, taxe sau grile de taxe și sens (debit sau credit).
- Fiecare linie are un cod (de ex. `GROSS`; `L1`, `L2`... se completează automat) și un tip de sumă: **Introdusă** (cu valoare propusă, fixă sau formulă, înlocuibilă de operator), **Fixă**, **Procent**, **Formulă** (expresie Python cu `round`, `abs`, `min`, `max`) și **Sold** (închide nota, inclusiv taxele).
- Liniile fără cont sunt parametri de calcul (o sumă cu TVA, o cotă): se folosesc în formule, dar nu se înregistrează.
- Ordinea de calcul urmează formulele; codurile necunoscute sau duplicate, buclele, mai multe linii de sold și formulele invalide sunt refuzate la salvarea șablonului.
- Taxele pe linie funcționează ca pe o notă manuală (liniile de TVA cu grilele lor, deci nota intră în decontul de TVA); suma negativă trece pe partea opusă, iar liniile cu sumă zero sunt omise.
- Asistentul **Notă din șablon** (**Facturare → Contabilitate → Tranzacții**, sau butonul **Generează nota** pe șablon) cere șablonul, data, referința, eventual partenerul și opțiunea **Validează nota** pentru postare directă.
- Nota rămâne legată de șablon: filtrul **Din șablon** pe notele contabile și butonul **Note** pe șablon.
- Butonul **Încarcă șabloanele românești** creează zece șabloane pe planul RO (refuzat pe companiile fără România ca țară fiscală; nu dublează șabloanele existente, iar cele cu cont lipsă sunt raportate ca „Omise”).
- Șabloanele de TVA la încasare livrate nu au grile fiscale, deci nu intră în D300 decât dacă se completează grilele înainte de generare; șablonul de amortizare nu se folosește pentru imobilizările gestionate cu modulul de active.

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_off_balance](../l10n_ro_off_balance/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.move.template`: șablonul de notă contabilă (jurnal, referință, instrucțiuni, linii); extins în `ro_templates.py` cu șabloanele românești.
- `l10n.ro.move.template.line`: linia de șablon (cod, cont, sens, tip sumă, formulă, taxe, analitic).
- `l10n.ro.move.template.run` și `l10n.ro.move.template.run.line`: asistentul de generare și sumele introduse.
- `account.move` (extins): câmpul `l10n_ro_move_template_id` („Șablon notă”).

**Vizualizări**

- `view_l10n_ro_move_template_list` / `view_l10n_ro_move_template_form` / `view_l10n_ro_move_template_search`: lista, formularul și căutarea șabloanelor.
- `view_l10n_ro_move_template_run_form`: asistentul Notă din șablon.
- `view_move_form` / `view_account_move_filter`: câmpul și filtrul **Din șablon** pe notele contabile.

**Acțiuni Automate / Acțiuni Server**

- `action_l10n_ro_move_template` și `action_l10n_ro_move_template_run`: acțiunile de fereastră ale șabloanelor și ale asistentului (cu meniurile aferente). Nu are cron-uri.

#### 5. Conexiuni

- [l10n_ro_off_balance](../l10n_ro_off_balance/index.md): contrapartida tehnică 803999 și jurnalul EXTR pentru șabloanele de comodat.
