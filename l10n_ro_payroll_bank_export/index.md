# Romania - Fișiere de plată salarii pentru bănci (localizat la `l10n_ro_payroll_bank_export/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_bank_export`
- **Versiune:** `20.0.1.1.5`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_payroll_bank_export
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_bank_export`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Generează fișierul de plată a salariilor în formatul băncii angajaților, direct din lotul de fluturași închis, fără retastarea IBAN-urilor și a sumelor în aplicația băncii.

#### 2. Funcționalități Cheie

- Formatul se alege în fereastra **Raport de plată** a lotului (butonul existent din Salarizare), alături de formatele standard (CSV, SEPA).
- Formate: Banca Transilvania (BT GO sau CSV simplu), BRD@ffice (CSV), BCR (CSV cu `|`), ING (OneCSV sau MT TXT), CEC Bank (CSV), Raiffeisen (DBF), UniCredit (CSV), OTP Bank (TXT), Alpha Bank (ALPHAClick TXT).
- Fișierul conține plățile din **restul de plată** al fluturașilor validați, câte una pe fiecare cont bancar al angajatului (inclusiv repartizarea pe mai multe conturi).
- Implicit intră doar conturile deschise la banca formatului (codul băncii din IBAN); bifa *Doar angajații acestei bănci* o dezactivează, iar un rezumat arată plățile incluse, totalul și conturile rămase în afară.
- Numele se scriu cu majuscule, fără diacritice; explicația plății (implicit *Salarii LL/AAAA*) se poate edita. Câmpul *Contul plătitor* este obligatoriu la BCR și opțional la BRD și CEC.
- Fișierul se arhivează pe lot și pe fluturași. Fiecare angajat are nevoie de IBAN pe fișă și de CNP.
- Limite: First Bank, Banca Românească și MT100 (ROI) nu sunt incluse. Fluxul detaliat e în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `l10n_ro_hr_payroll`

#### 4. Componente Cheie

**Modele**

- `hr.payroll.payment.report.wizard` (extins): adaugă formatele bancare românești în asistentul Raport de plată.

**Vizualizări**

- `hr_payroll_payment_report_view_form`: formularul extins al asistentului.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- [l10n_ro_payroll_advance](../l10n_ro_payroll_advance/index.md): avansul chenzinal; fișierul bancar nu scade încă avansul din net.
