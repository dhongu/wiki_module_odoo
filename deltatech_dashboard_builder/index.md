# Dashboard Builder

- **Nume Tehnic:** `deltatech_dashboard_builder`
- **Versiune:** `20.0.1.3.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_dashboard_builder
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_dashboard_builder`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Permite construirea fără cod de tablouri de bord cu KPI-uri și grafice pe orice model Odoo. Un tablou este un set de widgeturi care numără, însumează sau fac media înregistrărilor unui model, afișate ca număr, indicator, grafic sau tabel. Fiecare utilizator vede doar datele la care are dreptul.

#### 2. Funcționalități Cheie

- **Mereu datele utilizatorului**: widgeturile se calculează cu drepturile și companiile celui care privește tabloul (citiri grupate); un widget pe un model necitibil este golit, nu expus.
- **De la număr la înregistrări**: click pe un KPI, o bară sau un rând de tabel deschide lista înregistrărilor din spate.
- **Aceleași carduri peste tot**: KPI-urile folosesc cardurile din `deltatech_web_kpi_cards` (numere compacte, variație, progres, trend, mod luminos/întunecat).
- **KPI din KPI**: formule între KPI-urile tabloului (ex. „companii / parteneri * 100"), comparate cu perioada anterioară.
- **Fără goluri în timp**: graficele pe lună/săptămână/zi arată perioadele fără înregistrări ca zero.
- **Altă reprezentare**: orice grafic sau tabel poate fi redesenat ca alt tip din antet, doar cât timp e deschis tabloul.
- **Perioade**: un selector unic (luna aceasta, trimestrul trecut, ultimele 12 luni etc.) se aplică widgeturilor cu câmp de perioadă; KPI-ul arată variația față de perioada anterioară.
- **Ținte, instantanee și alerte**: țintă cu bară de progres, instantaneu zilnic pentru trend și alerte la depășirea unui prag (notifică o singură dată, se rearmează la revenire).
- **Mod editare**: constructorii îl activează din bara de instrumente și modifică widgeturile direct unde sunt desenate (tragere, redimensionare, meniul *Size*).
- **Partajare și prezentare**: vizibilitate pe grupuri, intrare proprie de meniu (**Add to menu**), ecran complet, export PNG sau CSV.
- Meniu: **KPI Dashboards ▸ Configuration ▸ Dashboards**. Grupurile *Dashboards / Builder* (creează) și *Viewer* (doar vizualizează); alertele se calculează cu drepturile utilizatorului din **Computed as**.
- Fluxul detaliat este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `web`
- `mail`
- `deltatech_web_kpi_cards`

#### 4. Componente Cheie

**Modele**

- `deltatech.dashboard`: tabloul de bord (nume, perioadă implicită, grupuri; cu chatter).
- `deltatech.dashboard.item`: widgetul (model, agregare, măsură, grupare, domeniu, țintă).
- `deltatech.dashboard.alert`: alerta de prag a unui KPI.
- `deltatech.dashboard.snapshot`: instantaneul zilnic al unui KPI.

**Vizualizări**

- `view_deltatech_dashboard_form` / `view_deltatech_dashboard_list`: tablourile.
- `view_deltatech_dashboard_item_form` / `view_deltatech_dashboard_item_list`: widgeturile.
- `view_deltatech_dashboard_alert_form` / `view_deltatech_dashboard_alert_list`: alertele.
- `action_dashboard_client`: acțiunea client care afișează tabloul.

**Acțiuni Automate / Acțiuni Server**

- `cron_dashboard_snapshots`: instantaneele zilnice ale KPI-urilor.
- `cron_dashboard_alerts`: verificarea orară a alertelor de prag.

#### 5. Conexiuni

- [deltatech_dashboard_builder_ai](../deltatech_dashboard_builder_ai/index.md): asistent AI care creează și modifică tablourile.
- `deltatech_web_kpi_cards`: cardurile KPI comune tablourilor Terrabit.
