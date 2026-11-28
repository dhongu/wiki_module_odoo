# Marketplace Order Stages (localizat la `deltatech_marketplace_sale_stage/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_sale_stage`
- **Versiune:** `20.0.1.2.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/20.0/deltatech_marketplace_sale_stage
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_sale_stage`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul leagă statusurile comenzilor din marketplace de fazele de vânzare definite în [deltatech_sale_stage](../deltatech_sale_stage/index.md), astfel încât comenzile importate să urmeze același flux de faze ca restul comenzilor. Echipele văd pe fiecare comandă faza în care se află și pot urmări trecerea dintre faze în chatter. Fazele propriu-zise și fluxul lor vin din `deltatech_sale_stage`; modulul nu calculează durate pe etape și nu oferă un raport separat.

#### 2. Funcționalități Cheie

- **Mapare de statusuri:** pentru fiecare marketplace se asociază fiecare status de comandă cu o fază de vânzare Odoo (backend → tab *Objects*, element *Sale Stage*).
- **Faza la import:** conectorii care folosesc maparea (de exemplu Doraly și Marketplace Extended) setează faza mapată pe comenzile importate.
- **Sărirea fazelor:** statusurile fără relevanță pentru fluxul comenzii se marchează *Skip Order*.
- **Istoric:** schimbările de fază se urmăresc în chatter-ul comenzii.
- Fluxul de configurare pas-cu-pas se află în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_sale_stage](../deltatech_sale_stage/index.md)

#### 4. Componente Cheie

**Modele**

- `marketplace.sale.phase` (`binding_sale_stage.py`): binding între faza marketplace (`external_id`) și `sale.order.phase` (`_inherits`), cu câmpul `skip_order`; `save_from_marketplace()` leagă faza după nume sau o creează.
- `marketplace.backend.item` (extindere): tipul de element nou `sale_stage` (*Sale Stage*), cu modelul de binding `marketplace.sale.phase`.

**Vizualizări**

- `view_marketplace_sale_phase_form` / `view_marketplace_sale_phase_tree` (`binding_sale_stage_view.xml`): formularul și lista binding-urilor de fază.
- `view_marketplace_sale_order_form` (`sale_order_view.xml`): extinde formularul comenzii marketplace cu faza.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): modulul de bază pentru comenzile din marketplace, peste care acest addon adaugă fazele.
- [deltatech_marketplace](../deltatech_marketplace/index.md): cadrul marketplace din care face parte.
- [deltatech_marketplace_sale_type](../deltatech_marketplace_sale_type/index.md): modul soră, care adaugă tipuri pentru comenzile de marketplace.
- [deltatech_marketplace_review](../deltatech_marketplace_review/index.md): folosește statusurile aduse de acest modul pentru regula „status nepermis pentru confirmare automată".
- [deltatech_marketplace_shopify](../deltatech_marketplace_shopify/index.md): mapează etichetele comenzii Shopify pe aceste faze.
