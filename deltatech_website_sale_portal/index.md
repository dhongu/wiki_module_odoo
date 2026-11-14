# Portal Order Search (localizat la `deltatech_website_sale_portal/index.md`)

- **Nume Tehnic:** `deltatech_website_sale_portal`
- **Versiune:** `19.0.1.0.6`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_sale_portal
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_sale_portal`
- **Ultima Ingestie:** `2026-11-14`

#### 1. Sumar

Clienții care comandă des își țin propria referință pe fiecare comandă, dar portalul îi lasă să caute ofertele și comenzile doar după numărul Odoo. Modulul adaugă în aceste două liste o coloană de referință și o casetă de căutare, astfel încât clientul să găsească un document după numărul pe care îl cunoaște.

#### 2. Funcționalități Cheie

- **Coloană de referință:** *Customer Reference* (`client_order_ref`) apare imediat după numărul comenzii, atât în lista *Quotations*, cât și în *Orders*.
- **Casetă de căutare:** clientul alege unde caută: în numele comenzii, în referința clientului sau în ambele (implicit).
- **Potriviri parțiale:** căutarea găsește părți din text și ignoră majusculele, deci câteva cifre din referință sunt suficiente.
- **Sortare suplimentară:** listele pot fi sortate și după numele comenzii sau după referința clientului.
- **Căutare păstrată între pagini:** căutarea rămâne activă la trecerea pe pagina următoare, iar textul căutat rămâne vizibil în casetă.
- **Doar ofertele și comenzile:** facturile și celelalte documente din portal rămân neschimbate.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

Modulul nu definește și nu extinde modele Python; logica se află în controllerul `CustomerPortal` (extinde `sale.controllers.portal.CustomerPortal`):

- `_get_sale_searchbar_sortings`: adaugă sortările „Order Name" și „Client Reference".
- `_prepare_quotations_domain` / `_prepare_orders_domain`: aplică filtrul `ilike` pe `name`, `client_order_ref` sau ambele, după parametrii `search` și `search_in`.
- `_prepare_sale_portal_rendering_values`: păstrează căutarea în link-urile paginatorului.
- `portal_my_quotes` / `portal_my_orders`: suprascrise pentru a injecta opțiunile din bara de căutare (`searchbar_inputs`, `search_in`).

**Vizualizări**

- `portal_my_quotations` (extinde `sale.portal_my_quotations`): adaugă coloana „Reference" cu `client_order_ref` în tabelul ofertelor din portal.
- `portal_my_orders` (extinde `sale.portal_my_orders`): adaugă coloana „Reference" cu `client_order_ref` în tabelul comenzilor din portal.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite acțiuni automate, sarcini cron sau acțiuni server.

#### 5. Conexiuni

- `sale`: portalul de vânzări standard, ale cărui liste de oferte și comenzi sunt extinse.
