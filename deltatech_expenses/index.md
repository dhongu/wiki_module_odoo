# Expenses Deduction (localizat la `deltatech_expenses/index.md`)

- **Nume Tehnic:** `deltatech_expenses`
- **Versiune:** `19.0.3.3.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_expenses
- **Cale Locală:** `odoo-addons/deltatech/deltatech_expenses`
- **Ultima Ingestie:** `2026-09-16`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul gestionează decontarea cheltuielilor efectuate de angajați pe baza avansurilor de trezorerie primite, un flux specific contabilității din România. Permite introducerea unui decont de cheltuieli într-un document distinct, care generează automat chitanțele de achiziție aferente, iar la validare produce notele contabile de avans, de decontare și de diurnă, închizând corect soldul contului de avansuri de decontat (542). Se calculează automat diferența de restituit sau de încasat între avansul acordat și cheltuielile justificate, inclusiv TVA-ul deductibil.

> **Notă — nu mai depinde de `hr_expense`.** Modulul a fost restructurat: nucleul `deltatech_expenses` este acum independent de modulul standard `hr_expense` și nu îl mai include ca dependență. Preluarea cheltuielilor `hr.expense` într-un decont (fostul wizard „Preia cheltuieli HR", câmpul `hr_expense_id` și override-ul pe `hr.expense.action_post`) a fost mutată într-un modul-punte separat, `deltatech_expenses_hr_expense` (auto-instalabil, activ doar dacă ambele module coexistă). Cele două module acoperă procese distincte care pot coexista fără dublă contabilizare: `deltatech_expenses` tratează fluxul românesc *avans de trezorerie (542) → decont → diurnă → închidere 542* cu model central propriu (`deltatech.expenses.deduction`), iar `hr_expense` tratează fluxul generic *angajatul/firma plătește → (eventual) rambursare*.

#### 2. Funcționalități Cheie

- Introducerea decontului de cheltuieli într-un document distinct care generează automat chitanțe de achiziție.
- Validarea documentului duce la generarea notelor contabile de avans, de decontare din avans și de diurnă, și la înregistrarea plăților.
- Calculul automat al diferenței dintre avansul acordat și totalul cheltuielilor (restituire sau încasare de către angajat).
- Calculul corect al TVA-ului deductibil aferent cheltuielilor, cu sume introduse TVA inclus.
- Linii de cheltuieli de două tipuri: „Cheltuieli" (justificată cu bon/factură, generează chitanță de achiziție `in_receipt`) și „Plată furnizor" (angajatul achită direct o datorie a firmei, generează doar nota `Dr 401 = Cr 542`, reconciliată cu facturile furnizor deschise).
- Calcul diurnă (câmp `diem`, implicit 42,5 lei/zi) și `total_diem`, cu notă contabilă proprie (`Dr 625 = Cr 542`).
- Închiderea automată a contului de avansuri de decontat (542) la contabilizarea finală, prin nota de diferență (`5311/5121` ↔ `542`).
- Buton smart „Deconturi" pe fișa angajatului (`hr.employee`), cu numărul deconturilor și listă filtrată.
- Angajatul este un `hr.employee`; partenerul contabil folosit pe notele contabile derivă din câmpul „Work Contact" (`work_contact_id`) — dacă acesta lipsește, notele se generează fără partener (înregistrări interne), validarea funcționând în ambele cazuri.

> **Configurare:** jurnalul de cheltuieli folosit pe decont trebuie să aibă drept cont implicit contul 542 („Cash advances"); jurnalul de numerar (Casă) trebuie să aibă contul 5311 configurat.

#### 3. Dependențe

- `l10n_ro`
- `account`
- `product`
- `hr`
- [deltatech_partner_generic](../deltatech_partner_generic/index.md)

#### 4. Componente Cheie

Informațiile pentru Componente Cheie nu sunt acoperite de `readme/DESCRIPTION.md`, iar conform fluxului de ingestie analiza suplimentară a codului se omite atunci când Sumarul și Funcționalitățile Cheie sunt preluate din Readme.

#### 5. Conexiuni

- `deltatech_expenses_hr_expense`: modul-punte (fără pagină wiki proprie momentan) care preia cheltuielile standard `hr.expense` ca linii de decont și previne dubla contabilizare la postare; nu este dependență a `deltatech_expenses`, ci invers.
- [deltatech_partner_generic](../deltatech_partner_generic/index.md): furnizează partenerul generic pentru liniile de decont fără furnizor explicit.
