# Transfer Product Images (localizat la `deltatech_stock_picking_image/index.md`)

- **Nume Tehnic:** `deltatech_stock_picking_image`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_stock_picking_image
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_picking_image`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaugă imaginea produsului pe transferurile de stoc: pe liniile formularului, pe avizul de livrare și pe raportul de operațiuni de picking. Echipa din depozit recunoaște mai ușor produsele, iar documentele tipărite se pot emite și fără imagini, printr-o setare pe companie.

#### 2. Funcționalități Cheie

- Coloana opțională **Imagine** pe liniile transferului (tab-ul Operații), afișată implicit.
- Imaginea (maximum 48 px) la începutul celulei de produs de pe avizul de livrare, înainte și după validare, cu sau fără loturi/serii sau pachete și pe liniile grupate pe produs.
- Imaginea lângă fiecare produs pe raportul **Picking Operations**.
- Opțiunea **Hide Product Images on Transfer PDFs** (Inventar > Configurare > Setări, secțiunea Operații, per companie) scoate imaginile din PDF-uri; pe ecran rămân.

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

**Modele**

- `stock.move`: câmpul `product_image`, preluat din produs.
- `res.company` și `res.config.settings`: câmpul `hide_picking_image_pdf`.

**Vizualizări**

- `view_picking_form`: coloana Imagine pe liniile transferului.
- `res_config_settings_view_form`: opțiunea de ascundere a imaginilor în PDF.
- `report_delivery_document` și `report_picking`: moștenesc rapoartele standard `stock` pentru a insera imaginea.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- Fără conexiuni funcționale directe verificate în cod.
