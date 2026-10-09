# Report Layout (Aspecte personalizate pentru rapoarte)

- **Nume Tehnic:** `deltatech_report_layout`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_report_layout
- **Cale Locală:** `odoo-addons/deltatech/deltatech_report_layout`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul adaugă în Odoo aspecte (layout-uri) de document suplimentare, cu un design modern și profesionist, pentru documentele tipărite: facturi, oferte, comenzi de achiziție și altele. Companiile își pot alege dintre ele stilul preferat, astfel încât toate documentele să păstreze o imagine de brand unitară.

#### 2. Funcționalități Cheie

- Două aspecte noi de raport, **Style1** și **Style2**, cu antet, subsol și corp de document diferite față de cele standard Odoo.
- Aspectele apar în configurarea centralizată a layout-ului documentelor, alături de cele standard; alegerea se face din **Setări > Setări generale > Document Layout**, cu previzualizare înainte de salvare.
- După salvare, toate rapoartele care folosesc layout-ul extern (facturi, comenzi de vânzare etc.) preiau stilul ales.
- Stilurile (SCSS) sunt încărcate prin asset-urile standard de raport (`web.report_assets_common`), deci sunt compatibile cu generarea PDF din Odoo.
- Antetul afișează sigla și adresa/detaliile companiei din configurarea companiei.
- Stadiu de dezvoltare: Beta.

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

**Modele**

- `report.layout` (model standard, nu este extins): modulul adaugă două înregistrări de date, `report_layout_style1` (secvența 101) și `report_layout_style2` (secvența 102).

**Vizualizări**

- `external_layout_style1`: șablon QWeb pentru layout-ul Style1 (`views/report_template_style1.xml`).
- `external_layout_style2`: șablon QWeb pentru layout-ul Style2 (`views/report_template_style2.xml`).
- `static/src/scss/report_style1.scss` și `report_style2.scss`: stilurile asociate celor două layout-uri.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `web`: furnizează mecanismul standard de layout de document pe care modulul îl extinde.
