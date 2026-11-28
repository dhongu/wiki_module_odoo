# Financial Analysis by Period

- **Nume Tehnic:** `deltatech_financial_analysis`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_financial_analysis
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_financial_analysis`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

După închiderea lunii, arată într-o singură pagină cum a mers și ce s-a schimbat. Citește indicatorii unei luni, ai unui trimestru, ai anului până la zi sau ai unui an fiscal din balanța de verificare, îi compară cu perioadele anterioare și listează abaterile importante, cu conturile și partenerii din spate. Spune și dacă perioada este cu adevărat închisă, ca cifrele provizorii să nu fie citite drept finale.

#### 2. Funcționalități Cheie

- **Indicatori din balanță**: cifră de afaceri, marjă brută, EBITDA, rezultat operațional, financiar și net, numerar, creanțe, stocuri, datorii, datorie financiară, capitaluri proprii, capital de lucru, plus marje, lichiditate, solvabilitate și rotații (DSO, DIO, DPO, ciclul de conversie a numerarului).
- **Comparații pe perioade**: luna față de luna anterioară, aceeași lună din anul trecut și cumulat anul trecut; trimestrul față de cel anterior și de același trimestru anul trecut, cu trendul ultimelor cinci trimestre; anul curent față de doi ani anteriori.
- **Preț, volum și mix**: abaterea cifrei de afaceri sau a marjei se descompune în volum, preț și mix pe categorii de produse, categorii noi/dispărute și costuri; cauzele însumează abaterea.
- **Doar abateri materiale**: se raportează abaterea care depășește atât un prag procentual, cât și unul valoric (parte din cifra de afaceri), setate pe companie; fiecare e marcată favorabilă sau nu și explicată prin conturile și partenerii principali.
- **Alerte**: capitaluri proprii negative sau sub jumătate din capitalul subscris, lichiditate curentă sub 1 și praguri proprii pe indicator.
- **Verificarea închiderii perioadei**: citește statusul din lista de închidere lunară din [l10n_ro_period_close_enhanced](../l10n_ro_period_close_enhanced/index.md) sau, în lipsa ei, caută note în ciornă, linii bancare nereconciliate, sold pe 473 și sold creditor la casă. O perioadă neînchisă apare ca provizorie.
- **Controale**: rezultatul este verificat față de soldul claselor 6 și 7, se afișează contul de suspensie bancar și soldurile partenerilor inversate; analiza anuală se verifică față de total active (F10).
- **Mapare editabilă**: liniile de bază sunt un raport contabil (*Financial Analysis Base (RO)*) pe planul de conturi românesc, cu drill-down; contabilul poate schimba conturile și formulele fără cod.
- **Închiderile lunare tratate**: închiderea contului de profit și pierdere (6/7 → 121) este lăsată deoparte; închiderea TVA rămâne în solduri.
- **Unelte pentru AI și MCP**: metode doar-citire (indicatori, trend, explicarea abaterii, vechimea creanțelor/datoriilor, statusul închiderii), declarabile pentru serverul MCP (`mcp_fa_indicators`, `mcp_fa_trend`, `mcp_fa_variance_drilldown`, `mcp_fa_aging`, `mcp_fa_close_status`).
- **Validare și tipărire**: analiza validată se blochează; raportul PDF conține indicatorii, abaterile și controalele.
- Utilizare: **Accounting → Reporting → Financial Analysis** (tip perioadă Month/Quarter/Year to Date/Year, apoi **Compute**, **Validate**, **Print**); praguri în **Accounting → Configuration → Settings → Financial Analysis**; indicatori în **Accounting → Configuration → Financial Analysis Indicators**.
- Fluxul detaliat este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account_reports`
- `deltatech_web_kpi_cards`

#### 4. Componente Cheie

**Modele**

- `financial.analysis`: analiza unei perioade (cu chatter și activități), calculată și validată.
- `financial.analysis.line`: valorile indicatorilor pe perioadă și comparații.
- `financial.analysis.variance`: abaterile materiale, cu cauze, conturi și parteneri.
- `financial.analysis.indicator`: definiția indicatorului (formulă, praguri, afișare ca KPI).
- `financial.analysis.lock.mixin`: blochează modificarea după validare.
- `financial.analysis.report.handler` (`account.report.custom.handler`): handler pentru raportul de bază.
- `res.company`, `res.config.settings` (extinse): pragurile de materialitate.

**Vizualizări**

- `financial_analysis_view_form` / `financial_analysis_view_list` / `financial_analysis_view_search`: analizele.
- `financial_analysis_variance_view_form` / `financial_analysis_variance_view_list`: abaterile.
- `financial_analysis_indicator_view_form` / `financial_analysis_indicator_view_list`: indicatorii.
- `res_config_settings_view_form`: pragurile.
- `action_financial_analysis_base_report`: raportul de bază *Financial Analysis Base (RO)*.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_ro_period_close_enhanced](../l10n_ro_period_close_enhanced/index.md): lista de închidere lunară citită pentru statusul perioadei.
- `deltatech_mcp_server`: serverul MCP pe care se declară metodele doar-citire.
