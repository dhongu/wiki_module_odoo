# Sale Order Line Images (localizat la `deltatech_sale_order_image/index.md`)

- **Nume Tehnic:** `deltatech_sale_order_image`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_order_image
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_order_image`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă imaginea produsului (sau a variantei) pe liniile ofertei și ale comenzii de vânzare în PDF. Imaginea apare într-o coloană proprie, înaintea descrierii, ceea ce face documentul trimis clientului mai ușor de parcurs vizual.

#### 2. Funcționalități Cheie

- Imaginea produsului sau a variantei se tipărește pe fiecare linie de produs, în prima coloană (lățime maximă 50 px); liniile fără imagine păstrează o celulă goală.
- Rândurile de tip secțiune, notă și combo ocupă întreaga lățime a tabelului, deci tabelul rămâne aliniat.
- Același PDF este folosit la trimiterea prin email, iar factura proformă afișează și ea imaginea.
- Opțiunea **Include image** se setează per companie în *Vânzări > Configurare > Setări > Oferte și comenzi* și este activă implicit.
- Imaginea apare doar pe documentul tipărit, nu și pe formularul ofertei.
- Atenție: Odoo 20 are propria opțiune **Display Product Images** (aceeași pagină de setări); nu le activa pe amândouă, altfel imaginea se tipărește de două ori.
- Fluxul pas cu pas este în fișa consultantului.

#### 3. Dependențe

- `sale`

#### 4. Componente Cheie

**Modele**

- `res.company`: câmpul boolean `include_image_line` (Include image), activ implicit.
- `res.config.settings`: expune opțiunea în setările de vânzări.

**Vizualizări**

- `views/res_config_view.xml`: opțiunea Include image în setările de vânzări.
- `report_saleorder_document` (`views/sale_order_report.xml`): moștenește șablonul `sale.report_saleorder_document` și adaugă coloana cu imagine.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- Nu există legături funcționale cu alte module wiki.
