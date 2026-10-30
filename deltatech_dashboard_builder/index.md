# Dashboard Builder (localizat la `deltatech_dashboard_builder/index.md`)

- **Nume Tehnic:** `deltatech_dashboard_builder`
- **Versiune:** `19.0.1.3.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_dashboard_builder
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_dashboard_builder`
- **Ultima Ingestie:** `2026-10-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Permite construirea, fără cod, a tablourilor de bord cu indicatori (KPI) și grafice pe orice model Odoo. Un tablou este un set de widget-uri; fiecare numără, însumează sau face media înregistrărilor unui model, opțional grupate după un câmp, și se afișează ca număr, indicator semicircular (gauge), grafic (bare, linii, arii, bare cu linie, pâlnie, plăcintă) sau tabel. Utilizatorii văd mereu doar datele la care au dreptul, iar managerii pot urmări ținte, tendințe și alerte pe praguri.

#### 2. Funcționalități Cheie

- **Datele utilizatorului curent:** widget-urile se calculează cu drepturile și companiile celui care privește tabloul (citiri grupate Odoo); regulile de înregistrare și multi-company se aplică, iar un widget pe un model necitibil este golit, nu expus.
- **De la număr la înregistrări:** un clic pe un KPI, o bară sau un rând de tabel deschide lista înregistrărilor din spate.
- **Aceleași carduri peste tot:** KPI-urile folosesc cardurile din [deltatech_web_kpi_cards](../deltatech_web_kpi_cards/index.md) (numere compacte, variație, progres, linie de tendință, mod luminos/întunecat).
- **KPI-uri din alte KPI-uri:** un KPI sau un gauge poate fi o formulă pe celelalte KPI-uri ale tabloului (ex. „companii / parteneri * 100"), identificate prin cod scurt și combinate cu + - * / și paranteze; se calculează cu drepturile celui care privește, se compară cu perioada anterioară, iar formula e validată la salvare (cod necunoscut, autoreferință).
- **Tipuri de widget:** număr (KPI), gauge (semicerc umplut până la țintă), grafic cu bare, linii, arii, bare cu linie (a doua agregare pe axă proprie), pâlnie, plăcintă, plus tabel. Graficele, gauge-urile și tabelele au înălțime (mică, medie, mare).
- **Fără goluri în timp:** un grafic grupat pe lună, săptămână sau zi arată perioadele fără înregistrări ca zero (opțiunea „Show periods without records", implicit activă), pe toată perioada aleasă; plăcintele și pâlniile nu se completează.
- **Comutator de tip:** orice grafic sau tabel poate fi redesenat ca alt tip din antetul său, cât timp tabloul e deschis, fără a-l modifica pentru ceilalți.
- **Mod de editare:** managerii cu drept de scriere activează din bara de unelte (creionul) modul de editare: fiecare widget arată butoanele de unelte, „Configure" îl deschide într-un dialog; widget-urile și benzile de KPI-uri se mută cu mânerul din antet, lățimea se schimbă din marginea dreaptă (1/4, 1/3, 1/2, 2/3, lățime întreagă) sau din meniul „Size"; aranjarea se salvează imediat. Sub 992px nu se trage, dimensiunea se setează din „Size". Alte module pot adăuga butoane prin categoria de registru `deltatech_dashboard_builder.item_tools`.
- **Perioade:** un singur selector (luna aceasta, trimestrul trecut, ultimele 12 luni etc.) se aplică tuturor widget-urilor cu câmp de perioadă; KPI-ul arată variația față de perioada anterioară.
- **Ținte, instantanee și alerte:** un KPI poate avea țintă cu bară de progres, instantaneu zilnic (opțiunea „Keep daily snapshots") pentru tendință și alerte pe prag, care notifică o singură dată la depășire și se rearmează la revenire.
- **Partajare și prezentare:** tablourile sunt vizibile pentru grupuri alese, pot primi intrare proprie în meniu („Add to menu"), se deschid pe tot ecranul, iar graficele și tabelele se exportă în PNG sau CSV.
- **Configurare:** în **KPI Dashboards ▸ Configuration ▸ Dashboards** se definesc numele, perioada implicită și grupurile; pentru fiecare widget se aleg modelul, agregarea (count, sum, average etc.), măsura, câmpul de grupare și domeniul. Instantaneele zilnice se calculează cu drepturile creatorului widget-ului. Grupul **Builder** creează tablouri, **Viewer** doar le vizualizează; tabloul fără grupuri este vizibil oricărui viewer. Alertele se calculează cu drepturile utilizatorului din „Computed as". Fluxul detaliat este în fișa consultant.

#### 3. Dependențe

- `web`
- `mail`
- [deltatech_web_kpi_cards](../deltatech_web_kpi_cards/index.md)

#### 4. Componente Cheie

**Modele**

- `deltatech.dashboard`: tabloul de bord (nume, perioadă implicită, grupuri, intrare de meniu); moștenește `mail.thread`.
- `deltatech.dashboard.item`: widget-ul (tip, model, agregare, măsură, grupare, domeniu, formulă și cod scurt, țintă, lățime, înălțime).
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
