# Marketplace Purchase Order addon (localizat la `deltatech_marketplace_purchase/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_purchase`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_purchase
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_purchase`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul extinde ecosistemul marketplace prin integrarea proceselor de aprovizionare cu vânzările din marketplace, permițând decizii de achiziție bazate pe date. Din perspectivă de afaceri, el face legătura între cererea de vânzări externă și gestionarea internă a lanțului de aprovizionare, asigurând că vânzările din marketplace sunt susținute de achiziții oportune și corecte. Practic, comenzile de achiziție sunt aliniate la cererea reală din marketplace, iar achizițiile destinate vânzărilor din marketplace sunt corelate automat cu înregistrările de stoc și de vânzări din Odoo.

#### 2. Funcționalități Cheie

- Achiziții orientate spre cerere: aliniază comenzile de achiziție la performanța reală a vânzărilor din marketplace și la cererea previzionată.
- Gestionarea furnizorilor: urmărește performanța și costurile furnizorilor pentru produsele destinate vânzării în marketplace.
- Flux de numerar îmbunătățit: optimizează nivelurile de stoc și frecvența achizițiilor pentru a se potrivi mai bine cu ciclurile de vânzare din marketplace.
- Analiză precisă a marjei: combină costurile de achiziție cu datele de vânzare din marketplace pentru o imagine completă a profitabilității produselor.
- Operațiuni eficientizate: corelează automat achizițiile legate de marketplace cu înregistrările corespunzătoare de stoc și de vânzări din Odoo.

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- `purchase_stock`

#### 4. Componente Cheie

> Notă: secțiunea este derivată din `__manifest__.py` și din structura tehnică a modulului, deoarece `readme/DESCRIPTION.md` nu acoperă componentele tehnice.

**Modele**

- `marketplace.purchase.order` (model nou, binding): leagă o comandă de achiziție Odoo (`purchase.order`) de o comandă externă din marketplace; gestionează importul comenzilor (`save_from_marketplace`) și exportul la confirmare (`on_confirm`), acum cu `identity_key` pe job-ul de export pentru a deduplica reconfirmările repetate în loc să pună în coadă job-uri duplicate.
- `marketplace.purchase.order.line` (model nou, binding): leagă liniile de comandă de achiziție de liniile externe din marketplace, rezolvând produsele după ID sau cod extern.
- `purchase.order` (extins): adaugă API-ul `create_api` (creare comandă pe baza unui token de securitate al backend-ului) și propagă scrierile către binding-urile marketplace prin `write` (cu excepția contextului `from_marketplace`).
- `marketplace.backend` (extins): adaugă câmpul `purchase_order_days` (implicit 2 zile).
- `marketplace.backend.item` (extins): adaugă tipul de element `purchase_order` și pictograma asociată (`fa-shopping-cart`).

**Vizualizări**

- `view_marketplace_purchase_order_form`: formular pentru comanda de achiziție marketplace, cu date externe, comanda Odoo asociată, buton „Reimport" și liniile importate.
- `view_marketplace_purchase_order_tree`: listă a comenzilor de achiziție marketplace.
- `view_marketplace_purchase_order_search`: vizualizare de căutare după nume, ID/cod extern și comandă Odoo.
- `view_marketplace_backend_form` (moștenită din `deltatech_marketplace`): adaugă câmpul `purchase_order_days` în secțiunea de limite a backend-ului.
- `menu_marketplace_purchase_order`: element de meniu „Purchase Orders" sub meniul de binding-uri marketplace.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_marketplace_get_purchase_order` (`ir.cron`): „Marketplace: Get Purchase Orders" — configurat să ruleze la interval de 1 oră; este **inactiv** implicit (`active = False`). Notă tehnică: metoda pe care o apela (`cron_import_purchase_orders`) a fost eliminată din `models/backend.py` odată cu versiunea 19.0.1.0.3 (marcată drept „stub mort" în `HISTORY.md`), dar înregistrarea `ir.cron` din `data/ir_cron_data.xml` nu a fost curățată — rămâne inactivă și nefolosită, fără efect cât timp nu e activată manual.

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): modulul de bază al ecosistemului marketplace (backend, binding-uri, item-uri, canal de export prin joburi `with_delay`); acest addon adaugă suportul pentru comenzile de achiziție.
- `purchase_stock`: aprovizionare și legătura achiziție-stoc Odoo, pe care se construiește importul comenzilor de achiziție.
