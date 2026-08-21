# Romania Intrastat Declaration (localizat la `l10n_ro_intrastat_enhancement/index.md`)

- **Nume Tehnic:** `l10n_ro_intrastat_enhancement`
- **Versiune:** `19.0.1.2.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_intrastat_enhancement
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_intrastat_enhancement`
- **Ultima Ingestie:** `2026-08-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde declarația Intrastat din Odoo Enterprise pentru piața din România, adaptând-o la cerințele Institutului Național de Statistică (INS). Adaugă în raportul standard de Intrastat un buton de export al declarației în format XML conform structurii cerute de portalul INS (intrastat.ro), atât pentru sosiri, cât și pentru expedieri, plus un buton de verificare a erorilor care semnalează dinainte câmpurile obligatorii lipsă ce ar duce la respingerea declarației. Ajută firma să își monitorizeze obligația de raportare: calculează automat volumul tranzacțiilor cu parteneri din Uniunea Europeană, îl compară cu pragurile anuale stabilite de INS și avertizează responsabilul atunci când compania se apropie de prag, l-a depășit sau se apropie termenul lunar de depunere. Atunci când este instalat și modulul de declarație recapitulativă D390, adaugă și o reconciliere automată între valorile Intrastat și cele din D390, ca verificare încrucișată înainte de depunere. Scopul este să reducă munca manuală și riscul de amenzi prin nedeclarare, depunere întârziată sau respingere de către INS.

#### 2. Funcționalități Cheie

- Export al declarației Intrastat în fișier XML, în formatul cerut de portalul INS România, direct din raportul standard de Intrastat (buton dedicat „XML").
- Generare separată a declarației pentru sosiri (arrivals) sau pentru expedieri (dispatches), cu validări care impun selectarea unui interval lunar corect și a unei singure direcții.
- Verificare erori INS (buton „INS Validation") — rulează aceeași interogare ca exportul XML și listează liniile cu câmpuri obligatorii lipsă (cod NC8, valoare, masă netă/unități suplimentare, natura tranzacției, cod TVA partener la expedieri, țară de origine la sosiri, mod de transport/regiune la declarația extinsă), exact cauzele tipice de respingere la INS.
- Reconciliere Intrastat ↔ D390 (buton „D390 Reconciliation", vizibil doar dacă `l10n_ro_anaf_d390` este instalat) — compară, pentru aceeași perioadă, sosirile Intrastat cu achizițiile intracomunitare de bunuri D390 (cod „A") și expedierile Intrastat cu livrările + operațiunile triunghiulare D390 (coduri „L"+„T"), afișând diferența absolută, procentuală și un status (concordant / diferență minoră / de verificat).
- Calcul automat al volumului anual al tranzacțiilor cu parteneri din UE (pe facturi/storno emise și primite), cu conversie în RON.
- Compararea volumului cu pragurile anuale INS (implicit 1.000.000 RON expedieri și 900.000 RON sosiri) și determinarea unui status: sub prag, atenție, depășit sau declarat obligatoriu.
- Avertizări automate lunare (activități în Odoo) când volumul atinge un procent configurabil din prag (implicit 80%) sau când pragul a fost depășit, plus memento pentru termenul de depunere (15 ale lunii).
- Wizard de verificare a pragului Intrastat la cerere, pe an și companie, care afișează volumul, pragul, procentul și statusul pentru sosiri și expedieri.
- Configurarea pragurilor, a procentului de avertizare și a statusului „declarat obligatoriu" din Setări, per companie.
- Actualizarea denumirilor codurilor Intrastat (nomenclatorul CN) prin descărcare directă din fișierul XML publicat de INS.
- Versiuni de nomenclatoare (țară, CN, mod de transport, condiții de livrare etc.) configurabile prin parametri de sistem, incluse în antetul declarației XML.

#### 3. Dependențe

- `l10n_ro_intrastat`
- `stock_delivery`

#### 4. Componente Cheie

**Modele**

- `account.intrastat.report.handler` (extins): adaugă în raportul Intrastat butoanele „XML" (export), „INS Validation" (verificare erori) și, condiționat, „D390 Reconciliation"; implementează `ro_intrastat_export_to_xml`, `ro_intrastat_validate` și `ro_intrastat_reconcile_d390`, toate pe baza aceleiași interogări comune `_l10n_ro_intrastat_query_res`.
- `account.intrastat.code` (extins): metodele `refresh` / `load_xml` descarcă nomenclatorul CN din fișierul XML al INS și actualizează denumirile codurilor.
- `res.company` (extins): câmpuri pentru praguri (expedieri/sosiri), procent de avertizare și status „declarat obligatoriu"; metode pentru calculul volumului Intrastat, evaluarea statusului față de praguri și cron-ul lunar de avertizare/memento.
- `res.config.settings` (extins): expune pragurile, procentul de avertizare și statusul de înregistrare în ecranul de Setări.
- `l10n.ro.intrastat.check` (TransientModel): wizard care calculează și afișează la cerere volumul, pragul, procentul și statusul Intrastat pentru sosiri și expedieri.
- `l10n.ro.intrastat.error.line` (TransientModel): liniile de eroare rezultate din verificarea INS Validation (flux, cod NC8, TVA partener, țară origine, valoare, greutate, descrierea problemelor).
- `l10n.ro.intrastat.d390.reconcile` (TransientModel): rezultatul reconcilierii Intrastat ↔ D390, cu valorile pe cele două fluxuri, diferența absolută/procentuală și statusul calculat (`_compute_reconcile`).

**Vizualizări**

- `view_l10n_ro_intrastat_check_form` / `action_l10n_ro_intrastat_check`: formularul și acțiunea wizardului de verificare a pragului Intrastat.
- `view_l10n_ro_intrastat_error_line_list` / `action_l10n_ro_intrastat_error_line`: lista (needit/nedelete) cu liniile de eroare afișate după rularea „INS Validation".
- `view_l10n_ro_intrastat_d390_reconcile_form`: formularul de reconciliere Intrastat ↔ D390, cu insigne de status colorate (verde/albastru/portocaliu) per flux.
- `res_config_settings_views.xml`: secțiunea de configurare a pragurilor și avertizărilor Intrastat în Setări.
- `product_template_hs_code`: ascunde câmpul `hs_code` din formularul produsului (moștenit din `stock_delivery`).
- `account_intrastat_code_view.xml`: vizualizarea codurilor Intrastat, cu acțiunea de reîmprospătare a nomenclatorului.

**Acțiuni Automate / Acțiuni Server**

- `cron_l10n_ro_intrastat_threshold`: sarcină `ir.cron` lunară care apelează `_cron_check_intrastat_threshold()` pe `res.company`; generează activități de avertizare la apropierea/depășirea pragului și memento pentru termenul de depunere (înainte de 15 ale lunii).

**Șabloane**

- `intrastat_report_arrivals_xml` / `intrastat_report_dispatches_xml` (în `data/intrastat_export.xml`): șabloanele QWeb care produc structura XML a declarației pentru sosiri, respectiv expedieri, conform formatului INS.

#### 5. Conexiuni

- `l10n_ro_intrastat`: modulul de bază al declarației Intrastat pe România, pe care acest modul îl extinde cu exportul XML, verificarea de erori și logica de praguri.
- `stock_delivery`: sursa câmpurilor de livrare și a codului HS (`hs_code`) ajustate de modul.
- [l10n_ro_anaf_d390](../l10n_ro_anaf_d390/index.md): dacă este instalat, activează butonul și wizard-ul de reconciliere Intrastat ↔ D390 (comparație bunuri intracomunitare); nu este o dependență strictă (verificare la runtime prin `_l10n_ro_d390_available`).
