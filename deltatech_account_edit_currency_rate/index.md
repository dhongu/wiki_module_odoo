# Custom Invoice Exchange Rate (localizat la `deltatech_account_edit_currency_rate/index.md`)

- **Nume Tehnic:** `deltatech_account_edit_currency_rate`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_account_edit_currency_rate
- **Cale Locală:** `odoo-addons/deltatech/deltatech_account_edit_currency_rate`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite editarea cursului valutar direct pe factură. Este util pentru facturile în valută cu un curs specific, diferit de cursul zilnic standard: utilizatorul introduce cursul dorit, iar sumele în moneda companiei se recalculează în consecință, păstrând coerența dintre documentul de factură și valorile contabile înregistrate.

#### 2. Funcționalități Cheie

- Editarea manuală a cursului valutar pe facturile de client și furnizor, cât timp factura este în ciornă; câmpul apare doar când moneda facturii diferă de moneda companiei.
- Recalcularea automată a sumelor contabile pe baza cursului introdus.
- Funcționare în medii multi-valută.
- Coerență între documentul facturii și sumele contabile înregistrate.

Fluxul detaliat și verificările pentru consultant sunt în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.move`: adaugă `currency_rate_custom` (curs introdus manual) și recalculează liniile facturii la modificarea lui.
- `account.move.line`: suprascrie `_compute_currency_rate` și `_inverse_amount_currency` pentru a folosi cursul custom în calculul soldului.
- `res.currency`: suprascrie `_convert` pentru a folosi un curs transmis prin context (`currency_rate`), când este prezent.

**Vizualizări**

- `view_invoice_form_custom_currency_rate`: extinde formularul de factură cu `currency_rate_custom`, lângă poziția fiscală.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale către alte module cu pagină în wiki.
