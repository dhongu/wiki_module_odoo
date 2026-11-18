# Report Layout (Aspecte personalizate pentru rapoarte)

- **Nume Tehnic:** `deltatech_report_layout`
- **Versiune:** `19.0.1.3.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_report_layout
- **Cale Locală:** `odoo-addons/deltatech/deltatech_report_layout`
- **Ultima Ingestie:** `2026-11-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă în Odoo opt aspecte (layout-uri) de document suplimentare, cu un design modern și profesionist, pentru documentele tipărite: facturi, oferte, comenzi de achiziție și altele. Companiile își pot alege dintre ele stilul preferat, astfel încât toate documentele să păstreze o imagine de brand unitară.

#### 2. Funcționalități Cheie

- Opt aspecte noi de raport: **Style1**, **Style2**, **Band**, **Modern**, **Title Box**, **Compact**, **Minimal** și **Accent**, fiecare cu antet, subsol și tabel proprii, diferite de cele standard Odoo.
- Aspectele apar în configurarea centralizată a layout-ului documentelor, alături de cele standard; alegerea se face din **Setări > Setări generale**, secțiunea **Companii**, butonul **Configurare Document Layout**, cu previzualizare înainte de salvare.
- Style1: sigla în stânga, adresa companiei aliniată la dreapta. Style2: adresa lângă siglă, antetul tabelului și totalul în culoarea primară a companiei.
- Band: titlul documentului și numele companiei pe o bandă colorată pe toată lățimea, subsol sub formă de bandă colorată. Modern: sigla în stânga, titlul și datele companiei în dreapta, bară colorată pentru total. Title Box: titlul într-un chenar centrat, antetul tabelului colorat.
- Compact: font mic, margini strânse și antet pe o singură linie, potrivit pentru documente cu multe linii. Minimal: alb-negru, fără fundaluri colorate, ieftin la tipărit (ignoră culorile companiei). Accent: bară colorată verticală pe marginea stângă a conținutului, titlu colorat.
- Culorile urmează culoarea primară și secundară a companiei (mai puțin Minimal), modificabile în același dialog.
- După salvare, toate rapoartele care folosesc layout-ul extern (facturi, comenzi de vânzare etc.) preiau stilul ales.
- Stilurile (SCSS) sunt încărcate prin asset-urile standard de raport (`web.report_assets_common`), listate explicit în manifest (fără wildcard, cerință pentru import pe Odoo Online), deci sunt compatibile cu generarea PDF din Odoo.
- Modul exclusiv de date (fără cod Python): poate fi instalat și pe Odoo Online (plan Custom), ca arhivă zip din **Aplicații > Import Module**, nu doar pe Odoo.sh sau on-premise.
- Stadiu de dezvoltare: Production/Stable (folosit de mult timp la clienți).

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

**Modele**

- `report.layout` (model standard, nu este extins): modulul adaugă opt înregistrări de date, `report_layout_style1` ... `report_layout_style8` (secvențele 101-108), cu numele Style1, Style2, Band, Modern, Title Box, Compact, Minimal, Accent.

**Vizualizări**

- `external_layout_style1` ... `external_layout_style8`: șabloane QWeb pentru cele opt layout-uri (`views/report_template_style1.xml` ... `style8.xml`), fiecare cu un șablon `_css` asociat.
- `static/src/scss/report_style1.scss` ... `report_style8.scss`: stilurile asociate layout-urilor.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `web`: furnizează mecanismul standard de layout de document pe care modulul îl extinde.
