# Romania - Declarație Intrastat (localizat la `l10n_ro_intrastat_enhancement/index.md`)

- **Nume Tehnic:** `l10n_ro_intrastat_enhancement`
- **Versiune:** `19.0.1.8.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_intrastat_enhancement
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_intrastat_enhancement`
- **Ultima Ingestie:** `2026-09-16`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Extinde declarația Intrastat românească din Odoo Enterprise cu tot ce este necesar pentru depunerea efectivă a declarației statistice la Institutul Național de Statistică (INS): export XML în formatul oficial INS, monitorizare praguri anuale cu avertizări automate și mecanism de actualizare a codurilor CN (Nomenclatură Combinată) publicate de INS. Modulul se instalează automat (`auto_install`) când sunt prezente atât raportul Intrastat de bază (`l10n_ro_intrastat`) cât și gestionarea livrărilor (`stock_delivery`).

#### 2. Funcționalități Cheie

- **Export XML INS** — buton „XML" în bara de instrumente a raportului Intrastat standard (vizibil doar pentru companiile românești); generează declarația lunară în structura XML oficială INS, cu layout-uri separate pentru sosiri și expedieri; aplică validări de perioadă (o singură lună calendaristică) și de direcție (una singură per fișier); normalizează codul TVA al partenerului și aplică CUI-ul companiei în forma cerută de INS; toate versiunile nomenclatoarelor (CN, transport, termeni de livrare, țări, județ, localitate, unitate de măsură) se stochează în `ir.config_parameter` pentru actualizare anuală fără modificări de cod.
- **Parteneri fără cod de TVA (ex. persoane fizice)** — sunt recunoscuți automat (placeholder-ul standard Enterprise `QN999999999999`/`QV999999999999`) și exportați cu codul special de țară `QV` pe partener, singura formă acceptată de aplicația offline INS pentru un cod de TVA neidentificat, fără nicio acțiune manuală; țara de destinație a mărfii rămâne cea reală, doar partenerul comercial devine „neprecizat".
- **Monitorizare praguri anuale** — configurare per companie a pragurilor INS (valori implicite 2025: 1.000.000 RON expedieri / 900.000 RON sosiri) cu procent de avertizare configurabil (implicit 80%) și flag „declarat obligatoriu"; calculează volumul Intrastat anual din facturile și stornările postate către parteneri UE (exclus România) ale căror produse au cod Intrastat, convertind fiecare sumă în RON.
- **Status prag la cerere, din meniul ⚙ al raportului** — buton discret „Intrastat Threshold" (fără `always_show`, deci nu apare ca banner permanent deasupra raportului) deschide statusul de prag pentru anul perioadei deschise în raport: volumul calculat, pragul INS configurat, procentul atins și starea (sub prag / atenție / depășit / declarat obligatoriu), pentru ambele direcții. Aceeași fereastră rămâne disponibilă și prin acțiunea tehnică `action_l10n_ro_intrastat_check`, pentru un recalcul punctual pe un an anume.
- **Verificare erori INS (INS Validation)** — buton „INS Validation" în bara raportului Intrastat, care rulează aceeași interogare ca exportul XML și listează liniile cu câmpuri obligatorii lipsă: cod NC8, valoare, masă netă/unități suplimentare, natura tranzacției, cod TVA partener la expedieri, țară de origine la sosiri, termeni de livrare (Incoterm), plus mod de transport/regiune la declarația extinsă — cauzele tipice de respingere la INS.
- **Validare formală a codului de TVA partener** — port fidel al bibliotecii Java `vat-validator` folosite de aplicația oficială INS (regex de format + cifră de control, pe țară); un cod care nu trece verificarea e semnalat de „INS Validation" înainte de export, nu abia la deschiderea declarației în aplicația offline INS. Placeholder-ul standard `QN`/`QV999999999999` e exclus din această verificare (e tratat separat, nu ca eroare de format).
- **Remindere automate** — o acțiune programată lunară verifică fiecare companie românească față de pragurile sale și creează activități de avertizare când se atinge procentul de alertă sau se depășește pragul (deduplicare — o singură activitate deschisă per direcție), plus un reminder de depunere înainte de data de 15 a lunii cu link către portalul INS (https://intrastat.ro).
- **Actualizare nomenclator CN** — lista de coduri Intrastat (`account.intrastat.code`) poate fi actualizată direct din XML-ul oficial INS (`CN_<versiune>.xml`), din **Contabilitate → Configurare → Coduri Intrastat**, butonul „Refresh"; menține Nomenclatura Combinată sincronizată cu anul configurat.
- **Versiunile nomenclatoarelor, mutate în Setări** — începând cu 19.0.1.7.0, cele 10 versiuni de nomenclator INS (CN8, țări, țări UE, mod de transport, termeni de livrare, natura tranzacției A/B, județe, localități, unități suplimentare) se editează direct din **Contabilitate → Configurare → Setări**, secțiunea „Intrastat — INS Romania Nomenclature Versions" (vizibilă doar pentru companii românești), nu doar din Tehnic → Parametri de sistem; rămân parametri globali de instanță (`ir.config_parameter`, `l10n_ro_intrastat.*`), nu per companie.
- **Reconciliere cu D390** — buton „D390 Reconciliation" în raportul Intrastat (vizibil doar dacă modulul `l10n_ro_anaf_d390` este instalat) care compară, pentru aceeași perioadă, valoarea bunurilor din Intrastat cu declarația recapitulativă D390: sosirile Intrastat față de achizițiile intracomunitare de bunuri (cod „A") și expedierile Intrastat față de livrările + operațiunile triunghiulare (coduri „L"+„T"). Afișează diferența absolută, procentuală și un status (concordant / diferență minoră / de verificat).
- **Terminologie românească oficială** pentru codurile de marfă (NC8) și codurile de tranzacție Intrastat, preluată din Regulamentul UE 2020/1197 și din nomenclatorul INS.

#### 3. Dependențe

- `l10n_ro_intrastat`
- `stock_delivery`

#### 4. Componente Cheie

**Modele**

- `account.intrastat.report.handler` (extins): adaugă în raportul Intrastat butoanele „XML" (export), „INS Validation" și, condiționat, „D390 Reconciliation" — toate cu `always_show: True` pentru a apărea în bara principală, plus butonul „Intrastat Threshold" fără `always_show` (doar în meniul ⚙); implementează `ro_intrastat_export_to_xml`, `ro_intrastat_validate`, `ro_intrastat_reconcile_d390` și `ro_intrastat_threshold_status`, toate pe baza aceleiași interogări comune `_l10n_ro_intrastat_query_res`.
- `l10n.ro.intrastat.vat_validator` (`models/l10n_ro_intrastat_vat_validator.py`, funcții modul, nu model ORM): port Python fidel al bibliotecii Java `vat-validator` folosite de aplicația offline INS — regexuri de format (`_REGEX_ARRAYS`) și algoritmi de cifră de control (`_DIGIT_VALIDATORS`) pentru fiecare țară acceptată; funcția publică `validate_formal_vat(country_code, vat_number)` e folosită de `ro_intrastat_validate` pentru a semnala codurile de TVA partener invalide înainte de export.
- `account.intrastat.code` (extins): câmpul `description` devine traductibil (`translate=True`), permițând terminologia românească oficială fără să suprascrie varianta engleză; `_compute_display_name` capătă `@api.depends_context("lang")`; metodele `refresh` / `load_xml` descarcă nomenclatorul CN din XML-ul INS, restrâng căutarea la `type = "commodity"` și scriu denumirile românești ca traducere a `description`.
- `res.company` (extins): câmpuri pentru praguri (expedieri/sosiri), procent de avertizare și status „declarat obligatoriu"; metoda `_l10n_ro_get_intrastat_volume()` calculează volumul Intrastat pe an/direcție din liniile de factură postate cu parteneri UE și produse cu cod Intrastat, convertit în RON; `_l10n_ro_intrastat_threshold_status()` combină volumele cu pragurile și întoarce statusul (`ok`/`warning`/`exceeded`/`registered`) pentru ambele direcții — folosită de wizard-ul tehnic, de acțiunea `ro_intrastat_threshold_status` din raport și de cron-ul lunar; `_cron_check_intrastat_threshold()` creează activitățile de avertizare/reminder.
- `res.config.settings` (extins): expune pragurile, procentul de avertizare și statusul de înregistrare (câmpuri `related` pe `res.company`), plus cele 10 câmpuri `config_parameter` pentru versiunile de nomenclatoare INS (scriu/citesc direct `ir.config_parameter`, cheile `l10n_ro_intrastat.*` rămân neschimbate).
- `l10n.ro.intrastat.check` (TransientModel): wizard tehnic (fără meniu) care calculează și afișează la cerere volumul, pragul, procentul și statusul Intrastat pentru sosiri și expedieri, pe an/companie; folosit atât din acțiunea tehnică `action_l10n_ro_intrastat_check` cât și din butonul „Intrastat Threshold" al raportului.
- `l10n.ro.intrastat.error.line` (TransientModel): liniile de eroare rezultate din verificarea „INS Validation" (flux, cod NC8, TVA partener, țară origine, valoare, greutate, descrierea problemelor — inclusiv codurile de TVA partener care nu trec verificarea formală).
- `l10n.ro.intrastat.d390.reconcile` (TransientModel): rezultatul reconcilierii Intrastat ↔ D390, cu valorile pe cele două fluxuri, diferența absolută/procentuală și statusul calculat (`_compute_reconcile`).

**Vizualizări**

- `view_l10n_ro_intrastat_check_form` / `action_l10n_ro_intrastat_check`: formularul și acțiunea (fără meniu) ale wizardului tehnic de verificare a pragului Intrastat; deschis atât tehnic, cât și din butonul „Intrastat Threshold" al raportului.
- `view_l10n_ro_intrastat_error_line_list` / `action_l10n_ro_intrastat_error_line`: lista (needit/nedelete) cu liniile de eroare afișate după rularea „INS Validation".
- `view_l10n_ro_intrastat_d390_reconcile_form`: formularul de reconciliere Intrastat ↔ D390, cu insigne de status colorate (verde/albastru/portocaliu) per flux.
- `res_config_settings_view_form_intrastat_ro` (`res_config_settings_views.xml`): două secțiuni noi în **Contabilitate → Configurare → Setări** (vizibile doar pentru companii RO) — „Intrastat — INS Romania Thresholds" (praguri, % avertizare, „declarat obligatoriu", Incoterm implicit) și „Intrastat — INS Romania Nomenclature Versions" (cele 10 versiuni de nomenclator, mutate aici din Tehnic → Parametri de sistem începând cu 19.0.1.7.0).
- `product_template_hs_code`: ascunde câmpul `hs_code` din formularul produsului (moștenit din `stock_delivery`).
- `account_intrastat_code_view.xml`: vizualizarea codurilor Intrastat, cu acțiunea de reîmprospătare a nomenclatorului („Refresh").

**Acțiuni Automate / Acțiuni Server**

- `cron_l10n_ro_intrastat_threshold`: sarcină `ir.cron` lunară care apelează `_cron_check_intrastat_threshold()` pe `res.company`; generează activități de avertizare la apropierea/depășirea pragului și memento pentru termenul de depunere (înainte de 15 ale lunii).

**Șabloane**

- `intrastat_report_arrivals_xml` / `intrastat_report_dispatches_xml` (în `data/intrastat_export.xml`): șabloanele QWeb care produc structura XML a declarației pentru sosiri, respectiv expedieri, conform formatului INS.

**Traduceri**

- `i18n_extra/ro.po`: traducerile românești ale descrierilor codurilor de tranzacție și ale codurilor speciale din capitolul 99 — stau într-un director separat de `i18n/` special ca să nu fie fuzionate (și marcate obsolete) la citirea `.pot`-ului standard.

#### 5. Conexiuni

- `l10n_ro_intrastat`: modulul de bază al declarației Intrastat pe România, pe care acest modul îl extinde cu exportul XML, verificarea de erori, statusul de prag, traducerile românești și logica de reconciliere.
- `stock_delivery`: sursa câmpurilor de livrare și a codului HS (`hs_code`) ajustate de modul.
- [l10n_ro_anaf_d390](../l10n_ro_anaf_d390/index.md): dacă este instalat, activează butonul de reconciliere Intrastat ↔ D390 (comparație bunuri intracomunitare); nu este o dependență strictă (verificare la runtime prin `_l10n_ro_d390_available`).
