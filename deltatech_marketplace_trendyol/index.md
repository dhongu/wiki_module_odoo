# Conector Trendyol Marketplace (localizat la `deltatech_marketplace_trendyol/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_trendyol`
- **Versiune:** `20.0.1.5.0`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_marketplace/tree/20.0/deltatech_marketplace_trendyol`
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_trendyol`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Un magazin Trendyol ținut lângă Odoo fără conector înseamnă stoc, preț și comenzi actualizate manual în două locuri: cantitatea și prețul se repetă în panoul de seller după fiecare modificare din Odoo, fiecare comandă se reintroduce, iar numerele de tracking se urmăresc separat. Conectorul Trendyol Marketplace închide acest gol: produsele, comenzile, stocul, prețul și facturile circulă între Odoo și Trendyol prin API-ul V2 și prin endpoint-urile asincrone de tip batch ale Trendyol, iar pentru că se leagă de același cadru `deltatech_marketplace` folosit de conectorii Shopify, eMAG și ceilalți, adăugarea Trendyol lângă un canal deja folosit nu înseamnă învățarea unui al doilea sistem.

#### 2. Funcționalități Cheie

- Import de produse (oferte) existente din Trendyol, potrivite automat după cod de bare, cu status de aprobare, preț de vânzare/listă și stoc; **Map Products** leagă produsele deja existente în Odoo de ofertele Trendyol (după cod de bare și referință internă) fără a importa nimic.
- Creare și actualizare de produse pe Trendyol (Product V2 API), cu categorie, atribute, cod de bare, TVA din taxa produsului, imagini și țară de origine (obligatorie pe Trendyol din 23.10.2026); un produs fără cod de bare sau fără țară de origine nu se poate crea.
- Export asincron de preț și stoc prin API-ul batch `price-and-inventory`, cu verificarea automată a rezultatului după circa un minut; articolele respinse sunt înregistrate cu motivul dat de Trendyol, iar erorile temporare (429, 5xx) sunt reluate de coada de joburi.
- Import de comenzi (pachete de expediție, Order V2) cu client, adrese, linii potrivite după cod de bare și plată marcată printr-o metodă „Trendyol”; fereastra de import e dată de „Sale Order Days” (1–30 de zile). Comenzile se importă doar în stările Created, Picking sau Invoiced; pachetele Cancelled/UnSupplied anulează comanda Odoo dacă nu există livrare finalizată, altfel lasă o notă.
- Notificări de comenzi în timp real printr-un webhook Trendyol, pe lângă importul programat.
- Numărul de tracking (AWB) se trimite automat la validarea livrării, iar starea pachetului este actualizată în Odoo la fiecare import; actualizarea explicită a stării pachetului pe Trendyol (Picking/Invoiced) rămâne disponibilă doar ca apel de dezvoltator.
- Import de retururi (claims) în registrul generic **Marketplace > Return Requests**, cu stările Trendyol mapate; conectorul doar citește (acceptarea sau respingerea rămâne în panoul Trendyol), iar pentru un claim în WaitingInAction se creează o activitate To Do înainte de acceptarea automată de la 48 de ore.
- Import al arborelui complet de categorii Trendyol dintr-o singură trecere; atributele obligatorii și valorile permise ale unei categorii frunză se aduc la prima referire.
- Trimiterea automată a link-ului PDF al facturii către Trendyol după postarea facturii Odoo (opțiunea „Push invoice to marketplace” de pe backend).
- Configurare pe backend: Seller ID, API Key/Secret, Storefront Code; comutatorul de producție/stage schimbă gateway-ul (stage cere IP-uri whitelistate). Butonul **Test connection** validează credențialele printr-un apel real.
- Acțiunile programate `Trendyol: Import Orders` și `Trendyol: Export Stock` sunt dezactivate implicit.
- Flux pas-cu-pas, cu capturi, în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `sale`
- `delivery`
- `stock_delivery`
- [deltatech_marketplace](../deltatech_marketplace/index.md)
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md)
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md)

#### 4. Componente Cheie

Sumarul și funcționalitățile provin din `readme/DESCRIPTION.md`, `readme/USAGE.md` și `readme/CONFIGURE.md`; componentele de mai jos rezultă din cod și din fișierele de date.

**Modele**

- `marketplace.backend` (extins): credențialele și setările Trendyol, testul de conexiune, importul de categorii, exportul de preț/stoc și verificarea batch-urilor.
- `marketplace.product` (extins): legătura produsului cu oferta Trendyol (cod de bare ca `external_id`, cod de stoc, preț tăiat, stare aprobat/în vânzare), import și export V2.
- `marketplace.product.category` (extins): maparea categoriilor Trendyol, cu atribute și valori permise.
- `marketplace.sale.order` (extins): importul pachetelor de expediție, starea Trendyol, tracking-ul AWB (`trendyol_after_send_to_shipper`) și anularea comenzii.
- `marketplace.return.request` (extins): importul claim-urilor Trendyol, maparea stărilor și activitatea de așteptare a acceptării automate.

**Vizualizări**

- `view_marketplace_backend_form` (extinsă): câmpurile specifice Trendyol pe formularul backend-ului.
- `view_marketplace_sale_order_form` (extinsă): starea Trendyol și tracking-ul pe comanda din marketplace.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_trendyol_import_orders`: „Trendyol: Import Orders”, la fiecare 30 de minute, dezactivată implicit.
- `ir_cron_trendyol_export_stock`: „Trendyol: Export Stock”, la fiecare oră, dezactivată implicit.

#### 5. Conexiuni

- [deltatech_marketplace_emag](../deltatech_marketplace_emag/index.md): conector analog pentru eMAG, pe același cadru.
- [deltatech_marketplace_shopify](../deltatech_marketplace_shopify/index.md): conector analog pentru Shopify, cu același mecanism de tracking la expediere.
- [deltatech_rma_marketplace](../deltatech_rma_marketplace/index.md): punte RMA; motivele de retur Trendyol se mapează pe backend.
