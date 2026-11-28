# Sales Dashboard

- **Nume Tehnic:** `deltatech_sale_dashboard`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_sale_dashboard
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_sale_dashboard`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Un singur ecran în aplicația Sales care răspunde la două întrebări: ce ne așteaptă acum și cum a mers perioada. Cardurile sunt cele din `deltatech_web_kpi_cards` și respectă modul luminos și întunecat al Odoo.

#### 2. Funcționalități Cheie

- Banda **To Do Now**: oferte deschise, oferte expirate, oferte de urmărit (trimise de mai mult de 7 zile, configurabil), comenzi de livrat, livrări întârziate, comenzi de facturat.
- Banda **Results** pe ultimele 7, 30, 90 sau 365 de zile, comparate cu perioada anterioară, cu linie de tendință: oferte emise, comenzi confirmate, vânzări fără taxe, rată de conversie, facturat fără taxe (note de credit scăzute).
- Alegerea sferei: **My Sales**, **My Team** sau **Whole Company** (ultimele două doar cui are voie); cifrele se citesc cu drepturile utilizatorului, deci se aplică regulile Sales și companiile selectate.
- Sumele sunt vizibile doar managerilor de vânzări (**Sales: Administrator**); agentul vede numărătorile, variațiile și conversia.
- Click pe card deschide lista înregistrărilor numărate (fără filtrele implicite), în vizualizările standard.
- Extensii automate: `deltatech_sale_dashboard_rma` (retururi) cu `deltatech_rma` și [deltatech_sale_dashboard_delivery](../deltatech_sale_dashboard_delivery/index.md) (colete) cu `deltatech_delivery_status`.
- Configurare: parametrul de sistem `deltatech_sale_dashboard.follow_up_days` (implicit 7); *My Team* folosește echipele din **Sales ▸ Configuration ▸ Sales Teams**.
- Flux ilustrat în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `sale_stock`
- `deltatech_web_kpi_cards`

#### 4. Componente Cheie

**Modele**

- `deltatech.sale.dashboard`: modelul care calculează cardurile și perioadele.

**Vizualizări**

- `views/sale_dashboard_views.xml`: ecranul **Sales ▸ Dashboard**.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- [deltatech_sale_dashboard_delivery](../deltatech_sale_dashboard_delivery/index.md): adaugă cardurile de colete.
- [deltatech_rma](../deltatech_rma/index.md): retururile apar pe bord prin `deltatech_sale_dashboard_rma`.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): sursa statusului coletelor.
