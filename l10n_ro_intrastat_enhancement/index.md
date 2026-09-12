# Romania - Declarație Intrastat (localizat la `l10n_ro_intrastat_enhancement/index.md`)

- **Nume Tehnic:** `l10n_ro_intrastat_enhancement`
- **Versiune:** `19.0.1.5.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_intrastat_enhancement
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_intrastat_enhancement`
- **Ultima Ingestie:** `2026-09-12`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde declarația Intrastat din Odoo Enterprise pentru piața din România, adaptând-o la cerințele Institutului Național de Statistică (INS). Adaugă în raportul standard de Intrastat un buton de export al declarației în format XML conform structurii cerute de portalul INS (intrastat.ro), atât pentru sosiri, cât și pentru expedieri, plus un buton de verificare a erorilor care semnalează dinainte câmpurile obligatorii lipsă ce ar duce la respingerea declarației. Ajută firma să își monitorizeze obligația de raportare: calculează automat volumul tranzacțiilor cu parteneri din Uniunea Europeană, îl compară cu pragurile anuale stabilite de INS și afișează direct în antetul raportului Intrastat un banner de alertă cu statusul față de prag (sub prag / atenție / depășit / declarat obligatoriu), fără să fie nevoie de niciun wizard separat. Atunci când este instalat și modulul de declarație recapitulativă D390, adaugă și o reconciliere automată între valorile Intrastat și cele din D390, ca verificare încrucișată înainte de depunere. Nomenclatorul codurilor Intrastat (coduri de marfă NC8 și coduri de tranzacție) este disponibil integral și în limba română, terminologie oficială preluată din Regulamentul UE 2020/1197 și din nomenclatorul INS. Scopul este să reducă munca manuală și riscul de amenzi prin nedeclarare, depunere întârziată sau respingere de către INS.

#### 2. Funcționalități Cheie

- Export al declarației Intrastat în fișier XML, în formatul cerut de portalul INS România, direct din raportul standard de Intrastat (buton dedicat „XML").
- Generare separată a declarației pentru sosiri (arrivals) sau pentru expedieri (dispatches), cu validări care impun selectarea unui interval lunar corect și a unei singure direcții.
- Verificare erori INS (buton „Verificare INS") — rulează aceeași interogare ca exportul XML și listează liniile cu câmpuri obligatorii lipsă (cod NC8, valoare, masă netă/unități suplimentare, natura tranzacției, cod TVA partener la expedieri, țară de origine la sosiri, mod de transport/regiune la declarația extinsă), exact cauzele tipice de respingere la INS.
- Reconciliere Intrastat ↔ D390 (buton „Reconciliere D390", vizibil doar dacă `l10n_ro_anaf_d390` este instalat) — compară, pentru aceeași perioadă, sosirile Intrastat cu achizițiile intracomunitare de bunuri D390 (cod „A") și expedierile Intrastat cu livrările + operațiunile triunghiulare D390 (coduri „L"+„T"), afișând diferența absolută, procentuală și un status (concordant / diferență minoră / de verificat).
- Butoanele XML, Verificare INS și Reconciliere D390 apar direct în bara principală de instrumente a raportului (nu doar în meniul-rotiță de opțiuni) — construite cu `always_show: True`, ca orice buton propriu de raport în Odoo 19.
- Calcul automat al volumului anual al tranzacțiilor cu parteneri din UE (pe facturi/storno emise și primite), cu conversie în RON.
- **Status prag direct în antetul raportului Intrastat**: la deschiderea raportului (companii românești), apare automat — fără niciun click suplimentar — un banner de alertă cu volumul calculat, pragul INS configurat, procentul atins și starea, pentru ambele direcții (sosiri și expedieri), pentru anul perioadei deschise în raport. Culoarea reflectă cea mai gravă dintre cele două stări.
- Wizard-ul de verificare a pragului (`l10n.ro.intrastat.check`) rămâne disponibil doar ca **acțiune tehnică** (`action_l10n_ro_intrastat_check`), fără meniu propriu — util pentru un recalcul punctual pe un an anume, în afara raportului; calculul de fond folosește aceeași metodă `res.company._l10n_ro_intrastat_threshold_status()` ca banner-ul.
- Avertizări automate lunare (activități în Odoo) când volumul atinge un procent configurabil din prag (implicit 80%) sau când pragul a fost depășit, plus memento pentru termenul de depunere (15 ale lunii).
- Configurarea pragurilor, a procentului de avertizare și a statusului „declarat obligatoriu" din **Contabilitate → Configurare → Setări**, secțiunea „Intrastat — Praguri INS România", per companie; implicit 2025: 1.000.000 RON expedieri / 900.000 RON sosiri, avertizare la 80%.
- Versiuni de nomenclatoare (țară, CN, mod de transport, condiții de livrare etc.) configurabile prin parametri de sistem (ex. `l10n_ro_intrastat.cn_ver`, implicit 2026), incluse în antetul declarației XML — se actualizează anual, fără modificări de cod.
- Actualizarea denumirilor codurilor Intrastat (nomenclatorul CN) din **Contabilitate → Configurare → Coduri Intrastat** prin butonul „Refresh", care descarcă direct XML-ul oficial publicat de INS.
- **Terminologie românească oficială pentru toate codurile Intrastat**: descrierile codurilor de marfă (NC8) și ale codurilor de tranzacție sunt traduse integral în română — cele 28 de coduri de tranzacție (19 în vigoare + 9 expirate la 01.01.2022, păstrate pentru declarații istorice), codurile de marfă preluate din nomenclatorul INS la actualizare, plus cele 4 coduri speciale din capitolul 99 (reparații/întreținere, tranzacții de valoare mică, note de credit, note de debit), care nu au poziție tarifară și au fost traduse manual. Denumirile românești se scriu ca traducere a câmpului `description` (devenit traductibil în modul), fără să afecteze varianta engleză a Odoo standard.

#### 3. Dependențe

- `l10n_ro_intrastat`
- `stock_delivery`

#### 4. Componente Cheie

**Modele**

- `account.intrastat.report.handler` (extins): adaugă în raportul Intrastat butoanele „XML" (export), „Verificare INS" și, condiționat, „Reconciliere D390" — toate cu `always_show: True` pentru a apărea în bara principală; implementează `ro_intrastat_export_to_xml`, `ro_intrastat_validate` și `ro_intrastat_reconcile_d390`, toate pe baza aceleiași interogări comune `_l10n_ro_intrastat_query_res`; prin `_customize_warnings` construiește banner-ul de status prag afișat automat în antetul raportului (`warnings["l10n_ro_intrastat_enhancement.threshold_status"]`).
- `account.intrastat.code` (extins): câmpul `description` devine traductibil (`translate=True`), permițând terminologia românească oficială fără să suprascrie varianta engleză; `_compute_display_name` capătă `@api.depends_context("lang")` ca numele afișat să nu rămână blocat în cache pe prima limbă calculată; metodele `refresh` / `load_xml` descarcă nomenclatorul CN din XML-ul INS, restrâng căutarea la `type = "commodity"` (codurile de tranzacție/transport au aceeași numerotare pe două cifre și s-ar potrivi accidental cu capitolele nomenclatorului) și scriu denumirile românești ca traducere a `description`, cu verificare prealabilă că limba română e instalată.
- `res.company` (extins): câmpuri pentru praguri (expedieri/sosiri), procent de avertizare și status „declarat obligatoriu"; metoda `_l10n_ro_intrastat_threshold_status()` calculează volumul Intrastat și statusul față de praguri, folosită atât de banner-ul din raport, cât și de wizard-ul tehnic și de cron-ul lunar de avertizare/memento.
- `res.config.settings` (extins): expune pragurile, procentul de avertizare și statusul de înregistrare în ecranul de Setări.
- `l10n.ro.intrastat.check` (TransientModel): wizard tehnic (fără meniu) care calculează și afișează la cerere volumul, pragul, procentul și statusul Intrastat pentru sosiri și expedieri, pe an/companie.
- `l10n.ro.intrastat.error.line` (TransientModel): liniile de eroare rezultate din verificarea INS Validation (flux, cod NC8, TVA partener, țară origine, valoare, greutate, descrierea problemelor).
- `l10n.ro.intrastat.d390.reconcile` (TransientModel): rezultatul reconcilierii Intrastat ↔ D390, cu valorile pe cele două fluxuri, diferența absolută/procentuală și statusul calculat (`_compute_reconcile`).

**Vizualizări**

- `view_l10n_ro_intrastat_check_form` / `action_l10n_ro_intrastat_check`: formularul și acțiunea (fără meniu) ale wizardului tehnic de verificare a pragului Intrastat.
- `view_l10n_ro_intrastat_error_line_list` / `action_l10n_ro_intrastat_error_line`: lista (needit/nedelete) cu liniile de eroare afișate după rularea „Verificare INS".
- `view_l10n_ro_intrastat_d390_reconcile_form`: formularul de reconciliere Intrastat ↔ D390, cu insigne de status colorate (verde/albastru/portocaliu) per flux.
- `res_config_settings_views.xml`: secțiunea de configurare a pragurilor și avertizărilor Intrastat în Setări.
- `intrastat_threshold_warning.xml` (asset `web.assets_backend`): componenta OWL care randează banner-ul de status prag în antetul raportului `account.report` standard.
- `product_template_hs_code`: ascunde câmpul `hs_code` din formularul produsului (moștenit din `stock_delivery`).
- `account_intrastat_code_view.xml`: vizualizarea codurilor Intrastat, cu acțiunea de reîmprospătare a nomenclatorului.

**Acțiuni Automate / Acțiuni Server**

- `cron_l10n_ro_intrastat_threshold`: sarcină `ir.cron` lunară care apelează `_cron_check_intrastat_threshold()` pe `res.company`; generează activități de avertizare la apropierea/depășirea pragului și memento pentru termenul de depunere (înainte de 15 ale lunii).

**Șabloane**

- `intrastat_report_arrivals_xml` / `intrastat_report_dispatches_xml` (în `data/intrastat_export.xml`): șabloanele QWeb care produc structura XML a declarației pentru sosiri, respectiv expedieri, conform formatului INS.

**Traduceri**

- `i18n_extra/ro.po`: traducerile românești ale descrierilor codurilor de tranzacție și ale celor 4 coduri speciale din capitolul 99 — stau într-un director separat de `i18n/` special ca să nu fie fuzionate (și marcate obsolete) la citirea `.pot`-ului standard, care nu poate include un model cu `_translate = False` precum `account.intrastat.code`.

#### 5. Conexiuni

- `l10n_ro_intrastat`: modulul de bază al declarației Intrastat pe România, pe care acest modul îl extinde cu exportul XML, verificarea de erori, banner-ul de prag, traducerile românești și logica de reconciliere.
- `stock_delivery`: sursa câmpurilor de livrare și a codului HS (`hs_code`) ajustate de modul.
- [l10n_ro_anaf_d390](../l10n_ro_anaf_d390/index.md): dacă este instalat, activează butonul de reconciliere Intrastat ↔ D390 (comparație bunuri intracomunitare); nu este o dependență strictă (verificare la runtime prin `_l10n_ro_d390_available`).
