# Expenses Deduction (localizat la `deltatech_expenses/index.md`)

- **Nume Tehnic:** `deltatech_expenses`
- **Versiune:** `20.0.3.8.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_expenses
- **Cale Locală:** `odoo-addons/deltatech/deltatech_expenses`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul gestionează avansurile de trezorerie acordate angajaților și decontarea lor printr-un decont de cheltuieli, așa cum le înregistrează contabilitatea din România. Avansul se înregistrează în contul 542 al angajatului, angajatul aduce bonurile, iar validarea decontului generează chitanțele de achiziție, diurna și diferența de restituit sau de plătit, până când 542 revine la zero pentru angajatul respectiv.

Modulul nu înlocuiește aplicația standard Cheltuieli (`hr_expense`), care rambursează cheltuielile plătite de angajați și nu cunoaște avansul de trezorerie. Cele două pot fi folosite în aceeași bază de date; legătura dintre ele o face modulul-punte `deltatech_expenses_hr_expense`.

#### 2. Funcționalități Cheie

- **Avans în contul 542**: avansul se plătește din jurnalul de numerar și se înregistrează pe 542 al angajatului.
- **Chitanțele ca linii de decont**: fiecare linie este un bon introdus cu TVA inclus; validarea creează chitanțele de achiziție și le decontează din avans. O linie poate fi și o plată către un furnizor făcută din avans (Dr 401 = Cr 542), cu butonul „Bills Paid" pentru alocarea pe facturile furnizorului; partea nealocată este avans către furnizor (Dr 4092 = Cr 401).
- **Diurnă**: sumă zilnică (implicit 42,5) înmulțită cu numărul de zile, înregistrată pe un cont de cheltuieli de deplasare (implicit 625).
- **Diferența decontată**: ce rămâne din avans este restituit de angajat, iar ce s-a cheltuit peste avans se plătește angajatului, prin jurnalul de numerar.
- **Moduri de decontare**: numerar; transfer bancar (card personal), prin contul 5125 „Sume în curs de decontare", potrivit cu extrasul de bancă; card al firmei, fără avans, cu chitanțele decontate Dr 401 = Cr 5125 și doar diurna datorată angajatului.
- **Valută**: un decont pe un jurnal de numerar în valută se ține în acea valută, iar la validare 542 se închide în valută și diferența de curs se înregistrează pe 665/765.
- **Roluri de aprobare**: Angajat, Aprobator și Contabil; aprobatorul validează avansul, doar contabilul postează sau anulează decontul.
- **Fișa angajatului**: buton smart cu deconturile angajatului, buton „Sold 542" cu fișa contului și imprimarea fiecărui decont.
- **Configurare**: jurnalul de cheltuieli are drept cont implicit 542; jurnalul de numerar, jurnalul de diurnă și contul de diurnă se completează pe decont; „Work Contact" al angajatului este partenerul de pe notele contabile.

Fluxul pas-cu-pas este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `l10n_ro`
- `account`
- `product`
- `hr`
- [deltatech_partner_generic](../deltatech_partner_generic/index.md)

#### 4. Componente Cheie

Componentele tehnice nu sunt detaliate în `readme/DESCRIPTION.md`, deci această secțiune nu este dezvoltată (conform fluxului de ingestie).

#### 5. Conexiuni

- [deltatech_expenses_hr_expense](../deltatech_expenses_hr_expense/index.md): modul-punte, auto-instalat, care preia cheltuielile standard `hr.expense` ca linii de decont și previne dubla contabilizare; nu este dependență a `deltatech_expenses`, ci invers.
- [deltatech_partner_generic](../deltatech_partner_generic/index.md): furnizează partenerul generic pentru liniile de decont fără furnizor explicit.
