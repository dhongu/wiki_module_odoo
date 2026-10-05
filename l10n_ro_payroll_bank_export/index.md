# Romania - Fișiere de plată salarii pentru bănci (localizat la `l10n_ro_payroll_bank_export/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_bank_export`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_payroll_bank_export
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_bank_export`
- **Ultima Ingestie:** `2026-10-05`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul generează fișierul de plată a salariilor în formatul băncii angajaților, direct din lotul de fluturași închis, fără retastarea IBAN-urilor și a sumelor în aplicația băncii. Formatul se alege în fereastra *Raport de plată* a lotului, alături de formatele standard (CSV, SEPA), iar fișierul rezultat se arhivează pe lot și pe fluturași.

#### 2. Funcționalități Cheie

- **Formate disponibile:**
    - **Banca Transilvania:** BT GO (CSV) sau CSV simplu;
    - **BRD:** BRD@ffice (CSV), aliniat la specificația băncii (suma cu virgulă și două zecimale, coloana *Data* goală, nume și detalii până la 35 de caractere);
    - **BCR:** Click 24 / George, plăți salariale (CSV cu `|`), după instrucțiunile publice ale băncii: antet cu IBAN-ul plătitorului, apoi o plată pe linie;
    - **ING:** OneCSV (CSV) sau MT (TXT);
    - **CEC Bank:** CSV;
    - **Raiffeisen:** DBF (dBase III);
    - **UniCredit:** CSV;
    - **OTP Bank:** TXT;
    - **Alpha Bank:** ALPHAClick (TXT).
- **Conținutul fișierului:** plățile din **restul de plată** al fluturașilor validați, câte una pe fiecare cont bancar al angajatului, inclusiv repartizarea pe mai multe conturi.
- **Filtru pe bancă:** implicit intră doar conturile deschise la banca formatului (codul băncii din IBAN); bifa *Doar angajații acestei bănci* îl dezactivează. Un rezumat din formular arată câte plăți intră, totalul și câte conturi rămân în afară (alte bănci sau fără cont).
- **Explicația plății** editabilă (implicit *Salarii LL/AAAA*) și data plății, alese în fereastră.
- **Date plătitor:** numele și CUI-ul se iau din companie; câmpul *Contul plătitor* (cont bancar al companiei) e obligatoriu la BCR, unde fișierul începe cu IBAN-ul lui, și se scrie și la BRD și CEC; la celelalte bănci IBAN-ul plătitorului rămâne gol, banca îl completează la import.
- **Normalizare:** numele se scriu cu majuscule, fără diacritice și fără separatori, așa cum cer băncile.
- **Flux:** *Stat de plată → Fluturași de salariu → Pay Runs* → lot cu fluturașii validați → *Raport de plată* → format, dată, explicație → rezumat → *Generează*; pentru angajații altor bănci se repetă cu formatul băncii lor (pașii detaliați, în fișa consultant).
- **Configurare:** fiecare angajat are IBAN pe fișă (*tab Personal → Cont bancar*) și CNP completat; pe companie se completează denumirea, CUI-ul, strada și orașul. Grupurile necesare sunt *Administrator salarizare* sau *Utilizator salarizare*, ca la raportul de plată standard.
- **Limite:**
    - formatele First Bank (integrată în Intesa Sanpaolo Bank România), Banca Românească (integrată în Exim Banca Românească) și MT100 lipsesc: nu există specificații publice accesibile, formatul trebuie cerut băncii; CEC rămâne după fișierul de referință (specificația băncii nu a putut fi consultată);
    - fișierele nu au fost verificate încă prin import în aplicațiile băncilor (Internet Banking, BRD@ffice, BT GO etc.), deci se recomandă un test cu o plată mică la prima utilizare;
    - la formatele fără zecimale (CEC, UniCredit, OTP) suma se scrie întreagă, dar un net cu bani se scrie cu două zecimale;
    - diacriticele sunt eliminate din toate numele și explicațiile.

#### 3. Dependențe

- `l10n_ro_hr_payroll`

#### 4. Componente Cheie

**Modele**

- `hr.payroll.payment.report.wizard` (extins, model tranzitoriu): adaugă în `export_format` formatele băncilor (la dezinstalare revin la CSV), plus câmpurile `l10n_ro_payment_details` (explicația plății), `l10n_ro_only_bank` (filtrul pe banca din IBAN) și `l10n_ro_bank_summary` (rezumat calculat). Metodele `_l10n_ro_payment_lines`, `_l10n_ro_payment_context`, `_perform_checks` și `generate_payment_report` colectează plățile, validează și generează fișierul.
- Biblioteci fără model (`tools/`): `bank_formats.py` (câte o funcție de scriere pentru fiecare format, curățarea textului, a IBAN-ului și a sumelor) și `dbf.py` (scriere/citire dBase III pentru Raiffeisen).

**Vizualizări**

- `hr_payroll_payment_report_view_form`: moștenește formularul `hr_payroll.hr_payroll_payment_report_view_form` și adaugă în grupul de raport formatele, explicația, filtrul pe bancă și rezumatul.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- `hr_payroll`: sursa lotului de fluturași și a ferestrei *Raport de plată* pe care modulul o extinde.
