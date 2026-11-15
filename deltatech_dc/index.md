# Declaration of Conformity (localizat la `deltatech_dc/index.md`)

- **Nume Tehnic:** `deltatech_dc`
- **Versiune:** `19.0.1.0.15`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_dc
- **Cale Locală:** `odoo-addons/deltatech/deltatech_dc`
- **Ultima Ingestie:** `2026-11-15`

#### 1. Sumar

Clienții cer adesea furnizorilor o declarație că bunurile livrate respectă standardele tehnice. Modulul păstrează pe fiecare produs referințele de calitate și tipărește o Declarație de Conformitate numerotată pentru loturi, facturi și livrări, ajutând compania să documenteze conformitatea produselor livrate.

#### 2. Funcționalități Cheie

- **Referințe de calitate**: un tab *Quality Control* pe produs conține *Standard of Company*, *Data Sheet*, *Technical Specification* și *Standards*, tipărite în declarație când sunt completate.
- **Evidența declarațiilor**: lista *Declaration of Conformity* (meniul catalogului de produse din Vânzări) arată *Number*, *Date of Declaration*, *Product* și *Lot*. La tipărire declarațiile sunt numerotate din secvența `DC/`; la creare manuală numărul se introduce de mână.
- **Tipărire cu creare automată**: acțiunea de tipărire de pe un lot, o factură postată sau o livrare creează declarațiile lipsă și le tipărește: câte una per lot, sau per produs și dată pentru produsele fără lot. Serviciile sunt omise.
- **Data producției**: câmpul *Production Date* al lotului datează declarația (data de azi dacă e gol) și apare ca dată a planului de calitate pentru loturile cu dată de expirare.
- **Al doilea formular de livrare**: *Declaration of Conformity 2* pe o livrare tipărește o singură declarație pentru toate liniile (produs, cantitate, lot, dată de utilizare, condiții de depozitare) și nu creează înregistrări.
- **Limitări**: textul declarației este fix în șabloane; al doilea formular citește un câmp *NRC* al partenerului pe care acest modul nu îl adaugă. Utilizatorii interni pot edita declarațiile companiilor lor. Formatul tipărit a fost curățat în 19.0 (structură și stil).

#### 3. Dependențe

- `base`
- `product`
- `sale`
- `mrp`
- `product_expiry`
- `stock_account`

#### 4. Componente Cheie

Secțiunea este acoperită de `readme/DESCRIPTION.md`; analiza codului a servit doar la verificarea comportamentului descris.

**Modele**

- `deltatech.dc`: declarația de conformitate (număr, dată, produs, lot, companie); numărul vine din secvența `declaration.conformity` (prefix `DC/`); câmpurile de calitate sunt preluate din produs.
- `product.template` (extins): `company_standard`, `data_sheet`, `technical_specification`, `standards`.
- `stock.lot` (extins): `production_date`, folosită la calculul datelor de expirare, utilizare, scoatere și alertă.
- `report.deltatech_dc.report_dc_lot`, `report.deltatech_dc.report_dc_invoice`, `report.deltatech_dc.report_dc_picking`: modele abstracte de raport care găsesc sau creează declarațiile pentru loturi, facturi și livrări.

**Vizualizări**

- `view_deltatech_dc_type_form` și `view_deltatech_dc_type_tree`: formularul și lista declarațiilor, accesibile din meniul `menu_deltatech_dc`.
- `product_template_form_view`: tabul *Quality Control* pe produs.
- `view_move_form_expiry`: câmpul de dată a producției pe formularul lotului.
- Rapoarte QWeb: `action_report_dc`, `action_report_dc_lot`, `action_report_dc_invoice`, `action_report_dc_picking` și `action_report_dc_picking_form_2`, plus șablonul `report_dc_warranty_certificate`.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește acțiuni automate sau acțiuni server. Secvența `DC/` (`sequence_dc`) și regula multi-companie `dc_comp_rule` sunt definite în date, ambele `noupdate`.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale către alte module cu pagină wiki existentă.
