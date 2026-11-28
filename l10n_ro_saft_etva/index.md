# Romania - Reconciliere e-TVA (decont precompletat ANAF) (localizat la `l10n_ro_saft_etva/index.md`)

- **Nume Tehnic:** `l10n_ro_saft_etva`
- **Versiune:** `20.0.1.0.7`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_saft_etva
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_saft_etva`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul reconciliază automat **decontul precompletat RO e-TVA** (OUG 70/2024) cu Decontul de TVA (D300) calculat intern în Odoo. ANAF generează lunar un decont precompletat din datele e-Factura, e-Transport, SAF-T și caselor de marcat, transmis prin SPV. Modulul importă fișierul XML primit, îl compară rând cu rând cu D300-ul intern și evidențiază diferențele înainte de depunere, gradate pe severitate. Diferențele critice nejustificate blochează închiderea perioadei de TVA, ca discrepanțele să fie explicate înainte de transmiterea D300. Modulul nu generează și nu transmite D300 (aceasta rămâne în [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md)) și nu acoperă pre-validarea SAF-T D406.

#### 2. Funcționalități Cheie

- Import manual al fișierului XML „Decont precompletat de TVA", descărcat din SPV; modulul nu se conectează la ANAF. Meniu: **Contabilitate → Raportare → e-TVA → Reconciliere decont precompletat** (se poate deschide și din verificarea „Reconciliere e-TVA" a checklistului de închidere).
- Reconciliere rând cu rând, nu doar pe total, cu butonul **Reconciliază cu D300**: pentru fiecare rând, baza și TVA-ul ANAF, baza și TVA-ul intern, diferența și severitatea. Rândurile apar cu numărul din formularul D300 în vigoare, inclusiv subrândurile (3.1, 5.1, 12.1, 20.1 etc.).
- Severități: **Coincide** (diferență sub 1 leu, din rotunjire), **Avertisment** (cel puțin 1 leu, sub praguri) și **Eroare critică** (peste ambele praguri).
- Praguri configurabile pe companie, în **Contabilitate → Configurare → Setări**: valoric (implicit 1.000 RON) și procentual (implicit 20%); o diferență devine eroare critică doar dacă le depășește pe amândouă.
- Justificare pe fiecare linie critică; apoi **Marchează justificat** și **Închide**. Cât timp există erori critice nejustificate, un banner avertizează, iar verificarea e-TVA din checklistul de închidere a perioadei de TVA rămâne blocată.
- Raport PDF de reconciliere.
- Fluxul pas-cu-pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `mail`
- `l10n_ro`
- `l10n_ro_reports`
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.etva.decont`: decontul e-TVA importat (perioadă, fișier, stare, contoare de diferențe și de erori critice, indicator de blocare); cu `mail.thread` și activități.
- `l10n.ro.etva.line`: linia de reconciliere pe rând D300 (valori ANAF și interne, diferențe, severitate, justificare).
- `account.return.check` (extindere): verificarea e-TVA din checklistul de închidere, cu `_l10n_ro_open_etva_decont`, bazată pe ciclul de audit al `account_reports`.
- `res.company` / `res.config.settings` (extinderi): pragurile valoric și procentual ale erorii critice.

**Vizualizări**

- `view_l10n_ro_etva_decont_form` / `view_l10n_ro_etva_decont_list`: formularul și lista deconturilor e-TVA.
- `res_config_settings_view_form_etva`: pragurile de severitate în setările contabilității.
- `report_etva_reconciliation_document`: șablonul raportului PDF de reconciliere.

**Acțiuni Automate / Acțiuni Server**

- `check_template_etva_reconcile`: șablonul verificării de închidere „Reconciliere e-TVA".
- `action_l10n_ro_etva_decont` și meniurile `menu_l10n_ro_etva_root` / `menu_l10n_ro_etva_decont`.
- `seq_l10n_ro_etva_decont`: secvența referinței; `security/ir.access.csv` acordă citire grupului contabil și acces complet managerului, cu restricție globală multi-company.

#### 5. Conexiuni

- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): sursa valorilor D300 interne cu care se face reconcilierea; valorile nu se recalculează aici.
- `l10n_ro_reports`: furnizează tipul de return TVA (`account.return`) pe al cărui checklist se adaugă verificarea blocantă.
- [l10n_ro_saft_validator](../l10n_ro_saft_validator/index.md): pre-validarea SAF-T D406, tratată separat.
- [l10n_ro_doc_screenshots](../l10n_ro_doc_screenshots/index.md): generarea automată a capturilor din fișa consultant.
