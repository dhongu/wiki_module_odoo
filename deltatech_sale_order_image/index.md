# Imagini pe Liniile Comenzii de Vânzare (localizat la `deltatech_sale_order_image/index.md`)

- **Nume Tehnic:** `deltatech_sale_order_image`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_order_image
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_order_image`
- **Ultima Ingestie:** `2026-11-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă imaginea produsului pe liniile ofertei și ale comenzii de vânzare în documentul PDF. Clientul vede imediat despre ce articole este vorba, iar oferta arată mai profesionist. Afișarea se poate dezactiva separat pentru fiecare companie.

#### 2. Funcționalități Cheie

- Imaginea produsului (sau a variantei, când există) se tipărește într-o coloană proprie, înaintea descrierii, cu lățime de cel mult 50 px.
- Același PDF este folosit la tipărire, la trimiterea prin email și la factura proformă, care afișează tot imaginea.
- Liniile fără imagine păstrează o celulă goală, iar rândurile de secțiune, notă și combo ocupă tot tabelul, deci aliniamentul rămâne corect.
- Opțiunea **Include image** se află în *Vânzări > Configurare > Setări > Oferte și comenzi*, este activă implicit și se setează per companie.
- Imaginea apare doar în documentul tipărit, nu și în formularul ofertei.
- Imaginea se încarcă pe produs din *Vânzări > Produse > Produse*.

#### 3. Dependențe

- `sale`

#### 4. Componente Cheie

**Modele**

- `res.company` (extins): câmpul boolean `include_image_line` (implicit activ).
- `res.config.settings` (extins): câmpul `include_image_line`, legat de companie, editabil din Setări.

**Vizualizări**

- `res_config_settings_view_form`: adaugă opțiunea **Include image** în blocul Oferte și comenzi din setările Vânzărilor.
- `report_saleorder_document`: extinde șablonul `sale.report_saleorder_document` cu coloana de imagine și ajustarea rândurilor de secțiune.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `sale`: modulul extinde raportul standard al ofertei și al comenzii de vânzare.
