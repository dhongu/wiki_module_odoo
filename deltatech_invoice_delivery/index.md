# Invoice Delivery (localizat la `deltatech_invoice_delivery/index.md`)

- **Nume Tehnic:** `deltatech_invoice_delivery`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_invoice_delivery
- **Cale Locală:** `odoo-addons/deltatech/deltatech_invoice_delivery`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Livrarea mărfii direct din factura de client: la postarea facturii, produsele stocabile sunt adăugate pe o comandă de vânzare, comanda este confirmată și livrarea este validată, într-un singur pas și fără ofertă separată. Util la vânzarea din magazin sau de la tejghea, unde marfa pleacă în momentul facturării.

#### 2. Funcționalități Cheie

- **Un singur pas**: postarea facturii creează comanda de vânzare, o confirmă și livrează marfa din stoc.
- **Activat pe jurnal**: doar jurnalele de vânzări cu **Livrare din factură** bifat folosesc fluxul; facturile emise din comenzi rămân pe fluxul standard. Se recomandă un jurnal separat (ex. *Facturi magazin*).
- **Doar ce are nevoie de livrare**: serviciile și liniile deja legate de o comandă rămân neatinse.
- **Aceleași valori ca factura**: cantitatea, unitatea, prețul, discountul și taxele se copiază pe linia comenzii, care rămâne legată de linia facturii, deci comanda apare livrată și facturată.
- **Verificarea stocului înainte de postare**: dacă stocul nu ajunge, factura nu se postează, iar mesajul listează fiecare produs cu cantitatea disponibilă și cea cerută.
- **Retururi pe aceeași factură**: o linie cu cantitate negativă readuce marfa în stoc; linia trebuie să se refere la factura inițială, iar marfa intră la costul curent al produsului, nu la cel al livrării originale (pentru anulare exactă de cost se folosește returul din livrarea inițială și nota de credit).
- **Contabilitate stoc**: cu `l10n_ro_stock_account_date` instalat, notele contabile de stoc ale livrării iau data contabilă a facturii, deci vânzarea (707) și costul mărfii vândute (607) cad în aceeași perioadă.
- **Configurare**: *Facturare > Configurare > Jurnale* (bifa **Livrare din factură**); depozitul comenzii generate trebuie să livreze într-un pas (*Inventar > Configurare > Depozite*, *Livrare directă*).
- **Limite**: se folosește doar când marfa pleacă la data facturii; marfa livrată mai devreme, mai ales într-o lună anterioară, se înregistrează la data livrării (418) și se facturează ulterior din livrare.

#### 3. Dependențe

- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `account.journal`: câmpul **Livrare din factură**.
- `account.move`: la postare creează comanda de vânzare, o confirmă și validează livrarea.

**Vizualizări**

- `views/account_journal_view.xml`: bifa pe formularul jurnalului.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- `l10n_ro_stock_account_date`: aliniază data contabilă a notelor de stoc la data facturii.
