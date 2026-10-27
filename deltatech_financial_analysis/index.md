# Financial Analysis by Period (Analiză financiară pe perioade)

- **Nume Tehnic:** `deltatech_financial_analysis`
- **Versiune:** `19.0.1.2.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_financial_analysis
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_financial_analysis`
- **Ultima Ingestie:** `2026-10-27`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

După închiderea lunii, modulul arată pe o singură pagină cum a decurs perioada și ce s-a schimbat. Citește indicatorii unei luni, ai unui trimestru, ai anului până la data curentă sau ai unui an fiscal din balanța de verificare, îi compară cu perioadele anterioare și listează abaterile importante, împreună cu conturile și partenerii din spatele lor. Spune și dacă perioada este cu adevărat închisă, ca nimeni să nu citească cifre provizorii drept finale.

#### 2. Funcționalități Cheie

- **Indicatori din balanța de verificare**: cifra de afaceri, marja brută, EBITDA, rezultat din exploatare, financiar și net, disponibilități, creanțe, stocuri, datorii comerciale, datorii financiare, capitaluri proprii și fond de rulment, plus rate de marjă, lichiditate, solvabilitate și rotație (DSO, DIO, DPO, ciclul de conversie a banilor).
- **Comparații pe perioade**: luna față de luna precedentă, aceeași lună din anul trecut și cumulat anul trecut; trimestrul față de cel precedent, același trimestru din anul trecut și cumulat, cu trendul ultimelor cinci trimestre; cumulat an față de aceeași perioadă din ultimii doi ani; anul față de ultimii doi ani, cu ponderea fiecărei linii în cifra de afaceri sau în total active.
- **Preț, volum și mix**: abaterea cifrei de afaceri sau a marjei brute se desparte în volum, preț și mix pe categorii de produse, categorii noi și dispărute, cifră de afaceri fără produse și, pentru marjă, costuri. Cauzele însumează abaterea.
- **Doar abateri semnificative**: o abatere apare numai dacă depășește și pragul procentual, și pe cel valoric (procent din cifra de afaceri), setate per companie. Fiecare e marcată favorabilă sau nu și explicată prin conturile și partenerii care o compun în cea mai mare parte.
- **Alerte**: capitaluri proprii negative, capitaluri sub jumătate din capitalul social subscris, lichiditate curentă sub 1 și orice prag setat pe un indicator.
- **Verificarea închiderii perioadei**: cu lista de verificare lunară din `l10n_ro_period_close_enhanced` analiza îi citește starea; fără el caută note în ciornă, linii bancare nelegate, sold în 473 și sold creditor pe disponibilități. O perioadă neînchisă apare ca provizorie (banner).
- **Controale**: rezultatul este verificat cu soldul claselor 6 și 7, se afișează contul de decontări bancare și soldurile inversate ale partenerilor, iar analiza anuală se verifică cu totalul activelor din bilanț (F10).
- **Mapare editabilă**: liniile de bază sunt un raport contabil (*Financial Analysis Base (RO)*) pe planul de conturi românesc, cu drill-down la înregistrări. Contabilul poate schimba conturile unei linii și formulele indicatorilor fără cod (formulele folosesc codurile liniilor, `avg('...')`, `days`, `SALES_INVOICED`, `PURCHASES_INVOICED`, `div(a, b)`).
- **Note de închidere lunară tratate**: nota de închidere a P&L (6/7 → 121) este exclusă din calcul, astfel că o lună închisă pe 121 își arată în continuare cifra de afaceri; închiderea de TVA rămâne în solduri.
- **Fluxul utilizatorului**: *Contabilitate → Raportare → Financial Analysis*, se alege tipul perioadei (lună, trimestru, cumulat an, an) și o zi din perioadă, **Calculează**, apoi file de Indicatori, Abateri (cu comentariu) și Controale, **Validează** (analiza se blochează) și **Tipărește** (PDF).
- **Configurare**: praguri în *Contabilitate → Configurare → Setări → Financial Analysis* (lunar și anual); indicatori în *Contabilitate → Configurare → Financial Analysis Indicators* (formulă, apariție în analiza lunară/anuală, card KPI, praguri de alertă).
- **Instrumente pentru AI și MCP**: metode doar-citire care calculează în memorie și întorc text (indicatori pe perioadă, trend, explicarea abaterii, vechimea creanțelor și datoriilor, starea închiderii), folosite de chatul Plutus și expuse prin serverul MCP (`mcp_fa_indicators`, `mcp_fa_trend`, `mcp_fa_variance_drilldown`, `mcp_fa_aging`, `mcp_fa_close_status`).

#### 3. Dependențe

- `account_reports`
- [deltatech_web_kpi_cards](../deltatech_web_kpi_cards/index.md)

#### 4. Componente Cheie

**Modele**

- `financial.analysis`: analiza unei perioade (cu `mail.thread` și activități); calculează indicatorii, abaterile, controalele și starea închiderii; conține metodele `mcp_fa_*`.
- `financial.analysis.line`: valoarea unui indicator în analiză, cu valorile de comparație.
- `financial.analysis.variance`: abaterea semnificativă, cu cauzele, conturile și partenerii și comentariul utilizatorului.
- `financial.analysis.indicator`: definiția indicatorului (formulă, apariție, card KPI, praguri de alertă).
- `financial.analysis.report.handler` (`account.report.custom.handler`): handler pentru raportul de bază.
- `res.company`, `res.config.settings`: pragurile de materialitate per companie.

**Vizualizări**

- `financial_analysis_view_form`: formularul analizei, cu carduri KPI, banner de provizorat și file Indicatori, Abateri, Controale.
- `financial_analysis_view_list` / `financial_analysis_view_search`: lista și căutarea analizelor.
- `financial_analysis_variance_view_form` / `financial_analysis_variance_view_list`: detaliul abaterilor.
- `financial_analysis_indicator_view_form` / `_list` / `_search`: configurarea indicatorilor.
- `res_config_settings_view_form`: pragurile din Setări.
- `action_financial_analysis_base_report`: deschide raportul de bază.
- Raportul PDF din `report/financial_analysis_report.xml`.

**Acțiuni Automate / Acțiuni Server**

- Niciun `ir.cron` sau acțiune server. Datele includ raportul contabil de bază `financial_analysis_report` și indicatorii impliciți; o migrare (`19.0.1.1.0`) rulează la actualizare.

#### 5. Conexiuni

- [l10n_ro_period_close_enhanced](../l10n_ro_period_close_enhanced/index.md): lista de verificare lunară din care analiza citește starea închiderii (dependență opțională, fără ea se fac verificări proprii).
- [deltatech_mcp_server](../deltatech_mcp_server/index.md): expune metodele `mcp_fa_*` ca instrumente MCP.
- [deltatech_web_kpi_cards](../deltatech_web_kpi_cards/index.md): cardurile KPI din formular.
- [deltatech_ai_financial_analysis](../deltatech_ai_financial_analysis/index.md): agentul Plutus, care comentează analiza și răspunde în chat cu instrumentele de mai sus.
