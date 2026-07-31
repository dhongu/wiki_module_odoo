# Deltatech Edit Currency Rate (localizat la `deltatech_account_edit_currency_rate/index.md`)

- **Nume Tehnic:** `deltatech_account_edit_currency_rate`
- **Versiune:** `19.0.1.0.0`
- **Cale:** [https://github.com/dhongu/deltatech/tree/19.0/deltatech_account_edit_currency_rate](https://github.com/dhongu/deltatech/tree/19.0/deltatech_account_edit_currency_rate)
- **Cale Locală:** `odoo-addons/deltatech/deltatech_account_edit_currency_rate`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul permite editarea manuală a cursului valutar direct pe documentele de factură (facturi client și facturi furnizor). Este util atunci când o factură în valută trebuie înregistrată la un curs specific, diferit de cursul zilnic standard, asigurând că sumele contabile reflectă exact cursul convenit cu partenerul sau cel din documentul original.

#### 2. Funcționalități Cheie

- Editare manuală a cursului de schimb valutar pe facturile client și facturile furnizor.
- Recalcularea automată a sumelor contabile (în moneda companiei) pe baza cursului introdus de utilizator.
- Suport pentru medii multi-valută în Odoo.
- Asigură consistența între documentul de factură și sumele financiare înregistrate.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.move`: adaugă câmpul `currency_rate_custom` (curs valutar introdus manual) și recalculează liniile facturii la modificarea acestuia.
- `account.move.line`: suprascrie `_compute_currency_rate` și `_inverse_amount_currency` pentru a folosi cursul custom (inversul lui `currency_rate_custom`) în calculul soldului contabil, în locul cursului standard.
- `res.currency`: suprascrie `_convert` pentru a folosi un curs de conversie transmis prin context (`currency_rate`), atunci când este prezent.

**Vizualizări**

- `view_invoice_form_custom_currency_rate`: extinde formularul de factură (`account.view_move_form`), adăugând câmpul `currency_rate_custom` lângă poziția fiscală; vizibil doar când moneda facturii diferă de moneda companiei.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

Nu au fost identificate module funcțional legate (fără dependențe stricte) în cadrul monorepo-ului.
