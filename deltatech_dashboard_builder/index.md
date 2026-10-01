# Dashboard Builder (localizat la `deltatech_dashboard_builder/index.md`)

- **Nume Tehnic:** `deltatech_dashboard_builder`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_dashboard_builder
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_dashboard_builder`
- **Ultima Ingestie:** `2026-10-01`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Permite construirea, fără cod, a tablourilor de bord cu indicatori (KPI) și grafice pe orice model Odoo. Un tablou este un set de widget-uri; fiecare numără, însumează sau face media înregistrărilor unui model, opțional grupate după un câmp, și se afișează ca număr, grafic sau tabel. Utilizatorii văd mereu doar datele la care au dreptul, iar managerii pot urmări ținte, tendințe și alerte pe praguri.

#### 2. Funcționalități Cheie

- **Datele utilizatorului curent:** widget-urile se calculează cu drepturile și companiile celui care privește tabloul (citiri grupate Odoo); regulile de înregistrare și multi-company se aplică, iar un widget pe un model necitibil este golit, nu expus.
- **De la număr la înregistrări:** un clic pe un KPI, o bară sau un rând de tabel deschide lista înregistrărilor din spate.
- **Aceleași carduri peste tot:** KPI-urile folosesc cardurile din [deltatech_web_kpi_cards](../deltatech_web_kpi_cards/index.md) (numere compacte, variație, progres, linie de tendință, mod luminos/întunecat).
- **Perioade:** un singur selector (luna aceasta, trimestrul trecut, ultimele 12 luni etc.) se aplică tuturor widget-urilor cu câmp de perioadă; KPI-ul arată variația față de perioada anterioară.
- **Ținte, instantanee și alerte:** un KPI poate avea țintă cu bară de progres, instantaneu zilnic (opțiunea „Keep daily snapshots") pentru tendință și alerte pe prag, care notifică o singură dată la depășire și se rearmează la revenire.
- **Partajare și prezentare:** tablourile sunt vizibile pentru grupuri alese, pot primi intrare proprie în meniu („Add to menu"), se deschid pe tot ecranul, iar graficele și tabelele se exportă în PNG sau CSV.
- **Configurare:** în **KPI Dashboards ▸ Configuration ▸ Dashboards** se definesc numele, perioada implicită și grupurile; pentru fiecare widget se aleg modelul, agregarea (count, sum, average etc.), măsura, câmpul de grupare și domeniul. Grupul **Builder** creează tablouri, **Viewer** doar le vizualizează; tabloul fără grupuri este vizibil oricărui viewer. Alertele se calculează cu drepturile utilizatorului din „Computed as". Fluxul detaliat este în fișa consultant.

#### 3. Dependențe

- `web`
- `mail`
- [deltatech_web_kpi_cards](../deltatech_web_kpi_cards/index.md)

#### 4. Componente Cheie

**Modele**

- `deltatech.dashboard`: tabloul de bord (nume, perioadă implicită, grupuri, intrare de meniu); moștenește `mail.thread`.
- `deltatech.dashboard.item`: widget-ul (model, agregare, măsură, grupare, domeniu, țintă, lățime).
- `deltatech.dashboard.alert`: alertă pe prag asociată unui KPI.
- `deltatech.dashboard.snapshot`: valoarea zilnică păstrată pentru tendința unui KPI.

**Vizualizări**

- `view_deltatech_dashboard_form` / `view_deltatech_dashboard_list`: definirea tablourilor.
- `view_deltatech_dashboard_item_form` / `view_deltatech_dashboard_item_list`: definirea widget-urilor.
- `view_deltatech_dashboard_alert_form` / `view_deltatech_dashboard_alert_list`: alertele.
- `action_dashboard_client`: acțiune client (componentă OWL) care afișează tabloul.

**Acțiuni Automate / Acțiuni Server**

- `cron_dashboard_snapshots`: salvează zilnic instantaneele KPI-urilor.
- `cron_dashboard_alerts`: verifică din oră în oră pragurile alertelor.

Securitate: grupurile `group_dashboard_viewer` și `group_dashboard_builder`, plus reguli de înregistrare (companie, viewer, builder) pe tablouri, widget-uri și instantanee.

#### 5. Conexiuni

- [deltatech_web_kpi_cards](../deltatech_web_kpi_cards/index.md): cardurile KPI comune folosite și de celelalte tablouri Terrabit.
