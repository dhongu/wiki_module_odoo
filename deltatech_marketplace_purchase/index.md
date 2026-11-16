# Marketplace Purchase Orders (localizat la `deltatech_marketplace_purchase/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_purchase`
- **Versiune:** `19.0.1.0.10`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_purchase
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_purchase`
- **Ultima Ingestie:** `2026-11-16`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul este stratul de bază care leagă comenzile de achiziție din Odoo de un backend marketplace din cadrul Deltatech Marketplace. Păstrează evidența comenzilor de achiziție care aparțin unui sistem extern, permite acelui sistem să creeze comenzi de achiziție în Odoo și trimite înapoi, prin conector, modificările făcute în Odoo. Este folosit de conectorul Odoo-to-Odoo (`deltatech_marketplace_odoo`), care trimite comenzile de achiziție confirmate către baza Odoo a furnizorului.

#### 2. Funcționalități Cheie

- Binding-uri pentru comenzile de achiziție: fiecare comandă de achiziție legată de un backend primește o înregistrare de binding cu backend-ul, **External ID**, **External Code** și liniile legate; sunt listate în **Marketplace > Bindings > Purchase Orders**, cu butonul standard **Reimport**.
- Comenzi de achiziție create din exterior: un sistem extern poate crea o comandă de achiziție prin metoda `create_api`, autentificată cu tokenul de securitate al backend-ului; comanda se creează în compania backend-ului și este legată imediat de acesta.
- Import din marketplace: comenzile și liniile primite de la un conector se creează sau se actualizează în Odoo; o comandă existentă se actualizează doar cât timp este încă cerere de ofertă; liniile își găsesc produsul după ID-ul sau codul extern mapat pe backend.
- Modificări trimise înapoi: când o comandă de achiziție legată este modificată în Odoo, modificarea este pusă în coadă ca job pentru backend, la fel ca la comenzile de vânzare, dacă elementul **Purchase Order** al backend-ului este activ la scriere.
- **Purchase Order Days:** câmp nou (implicit 2) în fila *Technical*, grupul *Limits* al formularului backend-ului; conectorul Odoo-to-Odoo trimite doar comenzile de achiziție datate în ultimele zile specificate.
- Limitări: modulul nu are conector propriu și nici import programat — doar conectorii care implementează comenzi de achiziție (în prezent, Odoo-to-Odoo) schimbă astfel de comenzi cu sistemul extern; nu calculează necesarul de achiziții din vânzările marketplace și nu oferă analiză de furnizori sau de marjă.

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- `purchase_stock`

#### 4. Componente Cheie

> Notă: `readme/DESCRIPTION.md` acoperă funcționalitatea, dar nu enumeră componentele tehnice; secțiunea este derivată din codul modulului.

**Modele**

- `marketplace.purchase.order` (model nou, binding): leagă o comandă de achiziție Odoo (`purchase.order`) de o comandă externă din marketplace; gestionează importul comenzilor (`save_from_marketplace`).
- `marketplace.purchase.order.line` (model nou, binding): leagă liniile comenzii de achiziție de liniile externe din marketplace, rezolvând produsele după ID sau cod extern.
- `purchase.order` (extins): adaugă API-ul `create_api` (creare comandă pe baza tokenului de securitate al backend-ului) și propagă scrierile către binding-urile marketplace prin `write` (cu excepția contextului `from_marketplace`).
- `marketplace.backend` (extins): adaugă câmpul `purchase_order_days` (implicit 2 zile).
- `marketplace.backend.item` (extins): adaugă tipul de element `purchase_order`.

**Vizualizări**

- `view_marketplace_purchase_order_form`: formular pentru comanda de achiziție marketplace, cu date externe, comanda Odoo asociată, butonul „Reimport” și liniile importate.
- `view_marketplace_purchase_order_tree`: listă a comenzilor de achiziție marketplace.
- `view_marketplace_purchase_order_search`: căutare după nume, ID/cod extern și comandă Odoo.
- `view_marketplace_backend_form` (moștenită din `deltatech_marketplace`): adaugă câmpul `purchase_order_days` în secțiunea de limite a backend-ului.
- `action_marketplace_purchase_order` și elementul de meniu „Purchase Orders” sub meniul de binding-uri marketplace.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește acțiuni automate sau acțiuni server. Cron-ul `ir_cron_marketplace_get_purchase_order` și hook-ul `on_confirm` au fost eliminate (19.0.1.0.5); trimiterea modificărilor se face prin mecanismul generic `on_write()` al cadrului marketplace, inclusiv la trecerea comenzii în starea `purchase`.

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): modulul de bază al ecosistemului marketplace (backend, binding-uri, item-uri, canal de export prin joburi); acest addon adaugă suportul pentru comenzile de achiziție.
- `deltatech_marketplace_odoo`: conectorul Odoo-to-Odoo, care trimite comenzile de achiziție confirmate către baza Odoo a furnizorului și folosește acest modul (modul fără pagină wiki).
- `purchase_stock`: aprovizionare și legătura achiziție-stoc Odoo, pe care se construiește importul comenzilor de achiziție.
