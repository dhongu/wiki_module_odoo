# Tablou de bord vânzări (Sales Dashboard)

- **Nume Tehnic:** `deltatech_sale_dashboard`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_sale_dashboard
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_sale_dashboard`
- **Ultima Ingestie:** `2026-10-06`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Un singur ecran în aplicația Vânzări, care răspunde la două întrebări: ce așteaptă acum echipa de vânzări și cum a mers perioada. Agentul vede dintr-o privire ofertele de urmărit, comenzile de livrat sau de facturat și rezultatele ultimelor zile, fără să caute prin liste. Un clic pe orice card deschide lista exactă a înregistrărilor numărate.

#### 2. Funcționalități Cheie

- **Banda „De făcut acum”** (indiferent de dată): oferte deschise, oferte expirate, oferte de urmărit (trimise de mai mult de 7 zile, încă valabile și fără răspuns), comenzi de livrat, livrări întârziate (programate înainte de azi) și comenzi de facturat.
- **Banda „Rezultate”** pe ultimele 7, 30, 90 sau 365 de zile, fiecare față de perioada anterioară de aceeași lungime, cu linie de evoluție: oferte emise, comenzi confirmate, vânzări fără TVA (în moneda companiei), rata de conversie (cu variația în puncte) și facturat fără TVA (notele de credit se scad).
- **Sume doar pentru manageri:** valorile și cardurile de sume (vânzări, facturat) sunt vizibile doar pentru **Vânzări: Administrator**; agentul vede numărătorile, variațiile și rata de conversie.
- **Domeniu de vizualizare:** „Vânzările mele”, „Echipa mea” (echipele din care utilizatorul face parte sau pe care le conduce) sau „Toată compania”, ultimele două doar pentru cine are dreptul. Datele se citesc cu drepturile utilizatorului (reguli de înregistrare și companii selectate).
- **De la număr la listă:** cardul deschide lista în vizualizările standard (oferte, comenzi, facturi, retururi), fără filtrele implicite, astfel încât numărul de pe card egalează numărul de rânduri.
- **Configurare:** numărul de zile după care o ofertă trimisă se urmărește este parametrul de sistem `deltatech_sale_dashboard.follow_up_days` (implicit 7). Meniul: **Vânzări ▸ Dashboard**.
- Cardurile sunt cele din `deltatech_web_kpi_cards` și respectă modul luminos/întunecat.
- Cu modulele punte instalate, apar automat carduri pentru retururi și colete (vezi Conexiuni). Fluxul detaliat este în fișa consultant.

#### 3. Dependențe

- `sale_stock`
- [deltatech_web_kpi_cards](../deltatech_web_kpi_cards/index.md)

#### 4. Componente Cheie

**Modele**

- `deltatech.sale.dashboard` (model abstract): calculează indicatorii („de făcut” și pe perioadă), tendința, domeniile pentru deschiderea listelor și regulile de acces la sume; expune `get_dashboard_data` și `dashboard_open_kpi`.

**Vizualizări**

- `action_sale_dashboard`: acțiune client (`deltatech_sale_dashboard.dashboard`), implementată în OWL (`static/src/dashboard/`).
- `menu_sale_dashboard`: meniul **Dashboard** sub Vânzări, pentru grupul `sales_team.group_sale_salesman`.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_sale_dashboard_rma](../deltatech_sale_dashboard_rma/index.md): punte care adaugă cardurile de retururi (de aprobat, în curs, cererile perioadei) când este instalat [deltatech_rma](../deltatech_rma/index.md).
- [deltatech_sale_dashboard_delivery](../deltatech_sale_dashboard_delivery/index.md): punte care adaugă cardurile de colete (de pregătit, de ridicat de curier, în drum) când este instalat [deltatech_delivery_status](../deltatech_delivery_status/index.md).
