# Report Layout (localizat la `deltatech_report_layout/index.md`)

- **Nume Tehnic:** `deltatech_report_layout`
- **Versiune:** `20.0.1.3.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_report_layout
- **Cale Locală:** `odoo-addons/deltatech/deltatech_report_layout`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaugă opt machete suplimentare pentru documentele tipărite (facturi, oferte, comenzi de achiziție, avize) cu un aspect mai modern și mai profesionist. Machetele se aleg per companie, din dialogul standard Odoo de configurare a layout-ului documentelor, astfel încât toate documentele companiei să aibă o identitate vizuală unitară.

#### 2. Funcționalități Cheie

- Opt machete noi: Grid, Inline, Band, Modern, Title Box, Dense, Minimal și Accent, fiecare cu propriul antet, subsol și stil de tabel.
- Culorile urmează culorile primară și secundară ale companiei (cu excepția machetei Minimal, alb-negru, economică la tipărit).
- Alegerea se face din **Setări > Setări generale > Companii > Configurare layout document**; machetele apar după cele standard. Opțiunea **Tabele** (Light, Boxed, Bold...) se aplică doar machetelor standard, nu și celor noi.
- Dense folosește font mic și margini reduse, potrivit documentelor cu multe linii.
- Modulul nu conține cod Python (doar vizualizări, șabloane de raport și stiluri), deci poate fi importat și pe Odoo Online (plan Custom) din **Aplicații > Import modul**.
- Fluxul pas cu pas, cu capturi, este în fișa consultantului.

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

**Modele**

- Modulul nu definește modele Python.

**Vizualizări**

- `external_layout_style1` ... `external_layout_style8`: șabloanele QWeb ale celor opt machete (Grid, Inline, Band, Modern, Title Box, Dense, Minimal, Accent), fiecare cu un șablon CSS asociat (`*_css`).

**Acțiuni Automate / Acțiuni Server**

- `report_layout_style1` ... `report_layout_style8`: înregistrări `report.layout` care fac machetele disponibile în dialogul de configurare a documentului.

#### 5. Conexiuni

- `base`: dialogul **Configure Document Layout** și culorile companiei sunt cele standard.
