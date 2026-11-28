# Marketplace Purchase Orders (localizat la `deltatech_marketplace_purchase/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_purchase`
- **Versiune:** `20.0.1.0.9`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/20.0/deltatech_marketplace_purchase
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_purchase`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Strat de bază care leagă comenzile de achiziție Odoo de un backend al cadrului Marketplace. Înregistrează ce comenzi aparțin unui sistem extern, permite acelui sistem să creeze comenzi de achiziție în Odoo și trimite înapoi, prin conector, modificările făcute în Odoo. Este folosit de conectorul Odoo-către-Odoo, care trimite comenzile confirmate către baza de date a furnizorului.

#### 2. Funcționalități Cheie

- Legătură (binding) pentru fiecare comandă de achiziție asociată unui backend, cu **External ID**, **External Code** și liniile legate; lista este în **Marketplace > Bindings > Purchase Orders**, cu butonul standard **Reimport**.
- Comenzi create din exterior prin metoda `create_api`, autentificată cu tokenul de securitate al backend-ului; comanda se creează în compania backend-ului.
- Import din marketplace: comenzile și liniile primite de la conector se creează sau se actualizează; o comandă existentă se actualizează doar cât timp este cerere de ofertă; produsele se găsesc după ID-ul sau codul extern.
- Modificările unei comenzi legate se pun în coadă ca job pentru backend, dacă elementul **Purchase Order** este activ la scriere (**Active On Write**).
- Câmpul **Purchase Order Days** (implicit 2) în fila **Technical**, grupul **Limits**: conectorul Odoo-către-Odoo trimite doar comenzile din ultimele zile indicate.
- Limite: fără conector propriu și fără import programat; nu calculează necesar de achiziție din vânzările marketplace și nu oferă analiză de furnizor sau marjă.

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- `purchase_stock`

#### 4. Componente Cheie

**Modele**

- `marketplace.purchase.order` (binding): leagă `purchase.order` de comanda externă; import (`save_from_marketplace`) și export la confirmare (`on_confirm`).
- `marketplace.purchase.order.line` (binding): leagă liniile comenzii de liniile externe.
- `purchase.order` (extins): API-ul `create_api` și propagarea scrierilor către binding-uri.
- `marketplace.backend` (extins): câmpul `purchase_order_days`.
- `marketplace.backend.item` (extins): tipul de element `purchase_order`.

**Vizualizări**

- `view_marketplace_purchase_order_form`, `view_marketplace_purchase_order_tree`, `view_marketplace_purchase_order_search` (acțiunea `action_marketplace_purchase_order`): binding-urile comenzilor de achiziție.
- `views/backend_views.xml`, `views/purchase_order_view.xml`: `purchase_order_days` pe backend și legătura marketplace pe comanda de achiziție.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu mai definește sarcini `ir.cron` pe 20.0 (fișierul de date cu cron-ul inactiv a dispărut).

#### 5. Conexiuni

- [deltatech_marketplace_odoo](../deltatech_marketplace_odoo/index.md): conectorul Odoo-către-Odoo, singurul care implementează schimbul de comenzi de achiziție.
