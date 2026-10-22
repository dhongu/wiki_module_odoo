# Livrare din factură (Invoice Delivery)

- **Nume Tehnic:** `deltatech_invoice_delivery`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_invoice_delivery
- **Cale Locală:** `odoo-addons/deltatech/deltatech_invoice_delivery`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Modulul permite livrarea mărfii direct din factura de client: la validarea facturii, produsele stocabile sunt trecute într-o comandă de vânzare, comanda este confirmată și livrarea este validată, într-un singur pas și fără ofertă separată. Este util pentru vânzările de la ghișeu sau din magazin, unde marfa pleacă în ziua facturării.

#### 2. Funcționalități Cheie

- **Un singur pas:** validarea facturii creează comanda de vânzare, o confirmă și livrează marfa din stoc; pe factură rămâne o notă cu link către comandă.
- **Activare per jurnal:** fluxul rulează doar pentru jurnalele de vânzări cu opțiunea *Livrare din factură* bifată (*Facturare > Configurare > Jurnale*); facturile emise din comenzi de vânzare păstrează comportamentul standard. Se recomandă un jurnal separat (ex. „Facturi magazin”).
- **Doar ce necesită livrare:** serviciile și liniile deja legate de o comandă de vânzare sunt ignorate.
- **Aceleași valori ca pe factură:** cantitate, unitate de măsură, preț, discount și taxe sunt copiate în linia comenzii, care rămâne legată de linia facturii, astfel încât comanda apare livrată și facturată.
- **Verificare de stoc înainte de validare:** dacă stocul nu e suficient, factura rămâne ciornă, iar mesajul listează fiecare produs cu cantitatea disponibilă și cea cerută.
- **Retururi pe aceeași factură:** o linie cu cantitate negativă readuce marfa în stoc (la costul curent al produsului, nu la cel al livrării inițiale).
- **Data contabilă:** livrarea preia data contabilă a facturii, astfel încât vânzarea (707) și costul mărfii vândute (607) cad în aceeași perioadă (cu `l10n_ro_stock_account_date` instalat).
- **Cerințe și limite:** depozitul trebuie să livreze într-un singur pas (în mai mulți pași livrarea este refuzată cu mesaj clar); se folosește doar când marfa pleacă la data facturii, altfel livrarea anterioară se înregistrează la data ei și se facturează ulterior din livrare.

#### 3. Dependențe

- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `account.move` (extins): `action_post` declanșează crearea comenzii din factură și livrarea (`add_to_sale`, `delivery_form_stock`).
- `sale.order` (extins): câmpul `from_invoice_id` (factura generatoare), verificarea pașilor de livrare și a disponibilității, `delivery_from_stock`.
- `account.journal` (extins): câmpul boolean `invoice_delivery` („Livrare din factură”).

**Vizualizări**

- `view_account_journal_form`: adaugă opțiunea *Livrare din factură* în formularul jurnalului.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_invoice_picking](../deltatech_invoice_picking/index.md): variantă înrudită, legătura dintre facturi și livrări.
- `l10n_ro_stock_account_date`: data contabilă a facturii este preluată de înregistrările de stoc ale livrării.
