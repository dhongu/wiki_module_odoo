# Expenses Deduction (localizat la `deltatech_expenses/index.md`)

- **Nume Tehnic:** `deltatech_expenses`
- **Versiune:** `19.0.3.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_expenses
- **Cale Locală:** `odoo-addons/deltatech/deltatech_expenses`
- **Ultima Ingestie:** `2026-06-01`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul gestionează decontarea cheltuielilor efectuate de angajați pe baza avansurilor primite. Permite introducerea unui decont de cheltuieli într-un document distinct, care generează automat chitanțele de achiziție aferente, iar la validare produce notele contabile de avans și înregistrează plățile. Astfel, soldul avansurilor de decontat (cont 542) se închide corect, calculându-se automat diferența de restituit sau de încasat între avansul acordat și cheltuielile justificate, inclusiv TVA-ul deductibil.

> **Notă — diferența față de `hr_expense`:** Acest modul **nu** înlocuiește modulul standard `hr_expense` și poate coexista cu el. `deltatech_expenses` acoperă fluxul contabil românesc *avans de trezorerie (cont 542) → decont → diurnă → închidere 542*. Începând cu versiunea `19.0.3.0.0` angajatul este un `hr.employee` (la fel ca în standard), iar partenerul contabil derivă din `work_contact_id`; un script de migrare convertește datele vechi (`res.partner` → `hr.employee`). În schimb, `hr_expense` acoperă fluxul generic HR *angajatul plătește din buzunar → firma rambursează*, bazat pe `hr.expense` / `hr.expense.sheet`, fără noțiunea de avans 542 sau diurnă.

#### 2. Funcționalități Cheie

- Introducerea decontului de cheltuieli într-un document distinct care generează automat chitanțe de achiziție.
- Validarea documentului duce la generarea notelor contabile de avans și înregistrarea plăților.
- Calculul automat al diferenței dintre avansul acordat și totalul cheltuielilor (restituire sau încasare).
- Calculul corect al TVA-ului deductibil aferent cheltuielilor.
- Generarea documentului de încasare (Chitanță / Dispoziție de Încasare) pentru restituirea soldului de către angajat.
- Închiderea automată a contului de avansuri de decontat (542) la contabilizarea finală.

> **Configurare:** În registrul de numerar trebuie completat câmpul "Cash advances" cu contul 542.

#### 3. Dependențe

- `l10n_ro`
- `account`
- `product`
- `hr`
- `hr_expense`
- `deltatech_partner_generic`

#### 4. Componente Cheie

Informațiile pentru Componente Cheie nu sunt acoperite de `readme/DESCRIPTION.md`, iar conform fluxului de ingestie analiza suplimentară a codului se omite atunci când Sumarul și Funcționalitățile Cheie sunt preluate din Readme.

#### 5. Conexiuni

Nu au fost identificate conexiuni către alte module cu pagină wiki existentă.
