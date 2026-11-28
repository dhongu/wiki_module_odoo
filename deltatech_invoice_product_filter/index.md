# Invoice Product Filter (localizat la `deltatech_invoice_product_filter/index.md`)

- **Nume Tehnic:** `deltatech_invoice_product_filter`
- **Versiune:** `20.0.1.2.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_invoice_product_filter
- **Cale Locală:** `odoo-addons/deltatech/deltatech_invoice_product_filter`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite căutarea facturilor după produsul de pe liniile lor sau după furnizorul produsului. În mod standard, lista de facturi se filtrează doar după câmpurile de antet (partener, dată etc.); modulul oferă contabililor o cale rapidă de a găsi toate documentele în care apare un anumit produs sau un produs cumpărat de la un anumit furnizor. Nu conține cod Python, doar o extensie a vizualizării de căutare, deci poate fi folosit și pe Odoo Online.

#### 2. Funcționalități Cheie

- Sugestia **Search Product for: ...** în bara de căutare a facturilor: păstrează facturile care au produsul pe cel puțin o linie; căutarea folosește denumirea, referința internă sau codul de bare.
- Sugestia **Search Vendor for: ...**: păstrează facturile cu produse cumpărate de la furnizorul indicat (din fila **Purchase** a produsului), indiferent de produs.
- Criteriile sunt disponibile în toate listele de facturi (facturi client, note de credit, facturi furnizor, rambursări) și se pot combina între ele și cu filtrele standard.
- Poate fi încărcat pe Odoo Online (plan Custom) din **Apps > Import Module**; nu necesită configurare. Fluxul detaliat este în fișa consultant.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Vizualizări**

- `view_account_invoice_filter`: extinde vizualizarea de căutare a facturilor (`account.view_account_invoice_filter`), adăugând după partener două câmpuri de filtrare pe `line_ids`: produsul și furnizorul produsului (`product_id.seller_ids.partner_id`).

#### 5. Conexiuni

Nu au fost identificate conexiuni cu alte module documentate în wiki.
