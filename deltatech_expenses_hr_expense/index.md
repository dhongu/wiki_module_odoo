# Expenses Deduction - HR Expense Bridge (localizat la `deltatech_expenses_hr_expense/index.md`)

- **Nume Tehnic:** `deltatech_expenses_hr_expense`
- **Versiune:** `20.0.1.1.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_expenses_hr_expense
- **Cale Locală:** `odoo-addons/deltatech/deltatech_expenses_hr_expense`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul face legătura dintre aplicația standard Cheltuieli (`hr_expense`) și decontul de cheltuieli din avans de trezorerie (`deltatech_expenses`, cont 542), pentru companiile care le folosesc pe amândouă și vor să evite înregistrarea de două ori a aceleiași cheltuieli.

#### 2. Funcționalități Cheie

- **Preluarea cheltuielilor HR în decont**: butonul „Preia cheltuieli HR" din decont adaugă ca linii cheltuielile trimise sau aprobate ale angajatului, nepostate și nelegate de alt decont; fiecare linie păstrează suma, taxele, furnizorul, contul și distribuția analitică.
- **Trimitere din lista de cheltuieli**: acțiunea „Adaugă în decont de cheltuieli" trimite mai multe cheltuieli ale aceluiași angajat într-un decont ales, dintr-un singur pas.
- **Fără dublă contabilizare**: o cheltuială legată de un decont se postează doar prin decont; aprobarea ei nu mai creează nota contabilă standard.
- **Eliberare la anulare**: la anularea decontului, liniile importate sunt șterse, iar cheltuielile redevin disponibile.
- **Instalare automată**: modulul se instalează singur când sunt prezente `deltatech_expenses` și `hr_expense`; nu necesită configurare.

Fluxul pas-cu-pas este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_expenses](../deltatech_expenses/index.md)
- `hr_expense`

#### 4. Componente Cheie

Componentele tehnice nu sunt detaliate în `readme/DESCRIPTION.md`, deci această secțiune nu este dezvoltată (conform fluxului de ingestie).

#### 5. Conexiuni

- [deltatech_expenses](../deltatech_expenses/index.md): decontul de cheltuieli din avans (cont 542) în care se importă cheltuielile HR.
