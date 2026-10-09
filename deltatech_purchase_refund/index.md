# Refund Purchase (Notă de credit furnizor)

- **Nume Tehnic:** `deltatech_purchase_refund`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_purchase_refund
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_refund`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul tratează situația în care o comandă de achiziție are cantități negative de facturat (de exemplu, s-a facturat mai mult decât s-a primit sau comandat). În loc de o factură de furnizor obișnuită, Odoo deschide direct o notă de credit de la furnizor, cu cantități pozitive și cu valoarea corect recalculată în moneda companiei.

#### 2. Funcționalități Cheie

- Detectarea cantităților negative de facturat pe comanda de achiziție (în funcție de metoda de control a produsului: cantitate comandată sau cantitate recepționată, minus cantitatea deja facturată).
- Deschiderea facturii ca notă de credit de la furnizor (`in_refund`) în locul facturii obișnuite.
- Pe linia notei de credit se postează cantități pozitive, iar soldul liniei este recalculat în moneda companiei, pe baza prețului unitar cu discount.
- Selectarea comenzii de achiziție de origine direct pe formularul notei de credit (câmp vizibil doar în ciornă, pentru nota de credit furnizor; filtrat după companie și partener).
- Data facturii implicită se preia din data planificată a comenzii; dacă există picking-uri cu aviz (`l10n_ro_notice`), indicatorul de aviz este propagat în contextul acțiunii.

#### 3. Dependențe

- `base`
- `account`
- `purchase_stock`
- `stock`

#### 4. Componente Cheie

**Modele**

- `purchase.order` (extins): `action_view_invoice` determină tipul facturii (`in_invoice` / `in_refund`) și completează contextul acțiunii.
- `purchase.order.line` (extins): `_prepare_account_move_line` calculează cantitatea pozitivă pentru nota de credit și recalculează `balance`.

**Vizualizări**

- `view_move_form`: moștenește `account.view_move_form` și adaugă câmpul `purchase_id` după `invoice_vendor_bill_id`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- Câmpul `l10n_ro_notice` de pe `stock.picking` (din localizarea română), dacă există, indicatorul de aviz este preluat în contextul acțiunii (legătură opțională, fără dependență).
