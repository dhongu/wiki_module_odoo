# Romania - Închiderea conturilor de venituri și cheltuieli (121) (localizat la `l10n_ro_account_return_pl_closing/index.md`)

- **Nume Tehnic:** `l10n_ro_account_return_pl_closing`
- **Versiune:** `19.0.1.0.11`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_account_return_pl_closing
- **Cale Locală:** odoo-addons/l10n_ro_ent/l10n_ro_account_return_pl_closing
- **Ultima Ingestie:** `2026-11-24`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul pentru închiderea lunară a conturilor de venituri (clasa 7) și cheltuieli (clasa 6) prin transferul soldului în contul 121 – Profit și pierdere, conform OMFP 1802/2014. Folosește framework-ul standard Enterprise `account.return` din `account_reports` (Odoo 19), oferind un flux structurat cu audit trail, similar cu cel de închidere TVA.

#### 2. Funcționalități Cheie

- Generare automată a notei contabile de închidere 6xx/7xx → 121 la apăsarea butonului **Mark as Reviewed**; fiecare cont cu sold are linia proprie de închidere, iar contul 121 primește contrapartida fiecărui transfer; conturile cu sold zero sunt ignorate. Nota este datată la ultima zi a perioadei.
- Flux cu stări Review → Submit, cu audit trail complet prin chatter; la **Submit** se verifică existența notei postate și se afișează rezultatul (profit/pierdere/echilibru) în istoric. Denumirile butoanelor (**Mark as Reviewed**, **Submit**, **Reset**, **View Entry**) vin din Enterprise și pot apărea în engleză.
- Accesare: **Contabilitate → Contabilitate → Închidere → Rulați închiderea P&L** (kanban filtrat pe tipul „RO – Închidere P&L (Venituri/Cheltuieli)"); se creează cu **Nou** (tipul, perioada — de la prima până la ultima zi a lunii — și compania). Înainte de rulare, toate documentele lunii (facturi, note manuale, note de stoc, preț mediu ponderat, coeficient K, reevaluări valutare) trebuie să fie postate, nu ciornă.
- Suport pentru conturi cu sold pe ambele părți: 609, 709, 711 etc. (`pl_bypass_account_ids`).
- Calcul profit/pierdere estimat înainte de generarea notei (fără a crea înregistrări), disponibil ca verificare „Estimated Profit / Loss” în panoul de checks al return-ului. Verificarea este informativă: pierderea sau echilibrul nu sunt anomalii, iar verificarea apare revizuită în toate cazurile, fără a cere „Validate” forțat.
- Badge profit/pierdere vizibil direct în vizualizarea Kanban pe fiecare return lunar.
- Buton „View Entry” pentru deschiderea directă a notei generate.
- **Reset complet**: **Reset** (pe închidere sau din meniul ⋮ al cardului din kanban) șterge sau stornează nota de închidere și readuce return-ul în starea nouă; apoi se postează documentele corective și se reia verificarea și generarea (util pentru corectarea unei închideri greșite fără note duplicate). O închidere poate avea o singură notă activă; pentru o a doua rulare se apasă întâi **Reset** (șterge definitiv nota — exportați-o dacă aveți nevoie de o copie).
- **O închidere cu notă nu poate fi ștearsă**: apare mesajul „Resetați închiderea înainte de ștergere.”; astfel nota nu rămâne postată, fără legătură cu închiderea, cu conturile 6xx/7xx închise în 121.
- **Fără distribuție analitică pe nota de închidere**: liniile ei nu primesc distribuția din modelele definite pe cont (ex. 628 → Subcontractori), ca rapoartele analitice ale lunii închise să nu arate sume fără cost real.
- **Nu intră sub blocarea declarației fiscale** (TVA/D300): nota nu are TVA, deci rămâne datată la sfârșitul perioadei și poate fi resetată chiar dacă o lună ulterioară are TVA validat; celelalte blocări (exercițiu financiar, blocarea definitivă) se aplică în continuare.
- Fallback multi-companie: dacă jurnalul sau contul 121 sunt configurate doar pentru altă companie, se folosesc echivalentele din compania return-ului — contul cu același cod, apoi cu aceleași prime 3 cifre; jurnalul cu același cod, apoi primul jurnal general al companiei. Același cont 121 se folosește la profitul afișat și la mesajul de la Submit. În formularul tipului de return se oferă doar înregistrările companiei curente.
- Include toate conturile de tip `income`, `income_other` (ex. 758) și `expense` din planul companiei.
- Cont 121 unic: același cont se creditează la profit și se debitează la pierdere; dacă planul folosește 1211 și 1212 separat, se alege unul dintre ele.
- Verificare în balanță: după generare, 6xx/7xx ale perioadei au sold zero, iar 121 are rezultatul perioadei; linia standard „Result Brought Forward” este tehnică, de raportare, nu nota generată. Repartizarea lui 121 în 117 se face printr-o notă separată, nu prin acest modul.
- Periodicitate lunară cu termen de 25 de zile, configurabilă pe tipul de return.
- Configurare per tip de return, în grupul „P&L Closing Configuration (RO)”: jurnalul de închidere (**Contabilitate → Configurare → Jurnale**, tip `Diverse`), contul 121 și lista de conturi cu bypass la verificarea sensului soldului — recomandate suplimentar față de 609/709/711: 712, 722, 723 (variații de stocuri/producție de imobilizări cu sold posibil invers).
- Integrare cu `l10n_ro_period_close_enhanced` (dacă e instalat): checklist-ul de închidere de perioadă verifică automat existența documentelor draft înainte de rulare.
- Integrare cu `l10n_ro_reports_fix`: opțiunea „Raw trial balance” din balanța de verificare permite reconcilierea corectă cu soldurile reale (linia standard Odoo „Result Brought Forward” e doar de raportare, nu reflectă nota generată).
- Regulă de migrare: modulul nu trebuie rulat pentru perioade la care s-a importat deja o balanță finală cu conturile 6/7 închise și rezultatul reportat în 121, pentru a evita dublarea închiderii.

#### 3. Dependențe

- `account_reports`
- `account`
- `l10n_ro`
- `l10n_ro_reports`

#### 4. Componente Cheie

**Modele**

- `account.return.type` (extins): adaugă configurația implicită pentru închiderea P&L pe tipul de return — `pl_journal_id` (jurnalul de închidere), `pl_account_id` (contul 121), `pl_bypass_account_ids` (conturi închise pe sold net, indiferent de parte) și câmpul calculat `is_pl_closing_return_type` (identifică dacă tipul de return se bazează pe un raport P&L românesc). Include și `_demo_setup()` pentru configurarea datelor demo.
- `account.return` (extins): adaugă `pl_profit_amount`/`pl_show_profit` (rezultatul calculat din nota de închidere postată) și `is_pl_closing_return` (related pe tipul de return). Suprascrie `_run_checks()` pentru a injecta verificarea „Estimated Profit/Loss”, `action_validate()` și `_proceed_with_locking()` pentru a genera nota de închidere la validare, și `_on_post_submission_event()` pentru a afișa rezultatul (profit/pierdere) și nota generată după Submit; `action_mark_uncompleted()` (Reset din meniul cardului) face resetul complet, iar o ștergere cu notă existentă este blocată (`@api.ondelete`). Metoda centrală `_generate_pl_closing_entries()` calculează soldurile conturilor de tip `income`/`income_other`/`expense` pe perioada return-ului (doar mișcări postate) și creează + postează nota contabilă de închidere, legată de return prin `closing_return_id`, fără distribuție analitică. `action_compute_estimated_profit()` expune calculul preliminar din verificarea de check.
- `account.move.line` (extins): `_affect_tax_report()` exclude nota de închidere P&L din blocarea declarației fiscale (păstrează doar criteriile standard: taxe, linii de taxă, etichete de taxă).
- `account.move`: nota generată este legată de return prin câmpul standard `closing_return_id` din `account_reports` (nu e extins de acest modul), ceea ce o face vizibilă în `closing_move_ids` și gestionată automat la reset.

**Vizualizări**

- `data/account_return_pl_closing.xml`: definește tipul de return „RO – Închidere venituri/cheltuieli (P&L)” și verificările (checks) asociate.
- `views/account_return_type_views.xml`: extinde vizualizarea formularului tipului de return pentru a expune câmpurile `pl_journal_id`, `pl_account_id`, `pl_bypass_account_ids`.
- `data/menu.xml`: adaugă opțiunea de meniu **Run P&L Closing** (**Închidere** în română) în meniul de închidere din Contabilitate, cu un kanban de audit filtrat pe tipul P&L.

**Acțiuni Automate / Acțiuni Server**

- Verificare „Estimated Profit / Loss” (`_check_template_pl_estimated_profit`): injectată în `_run_checks()`, calculează și afișează ca notificare profitul/pierderea estimat(ă) înainte de generarea notei finale, prin `action_compute_estimated_profit()`.

#### 5. Conexiuni

- [l10n_ro_account_chart](../l10n_ro_account_chart/index.md): modulul de plan de conturi românesc extins, fundamental pentru structura contabilă (contul 121 și conturile de clasă 6/7).
- [l10n_ro_account_fisa_cont](../l10n_ro_account_fisa_cont/index.md): raportul „Fișă de Cont”, complementar pentru verificarea soldurilor conturilor 6xx/7xx/121 înainte și după închidere.
- [l10n_ro_period_close_enhanced](../l10n_ro_period_close_enhanced/index.md): checklist-ul de închidere de perioadă include automat verificarea facturilor/notelor draft înainte de rularea acestui modul.
- [l10n_ro_reports_fix](../l10n_ro_reports_fix/index.md): furnizează opțiunea „Raw trial balance”, necesară pentru reconcilierea balanței cu soldurile reale după rularea închiderii P&L.
- `account_reports`: framework-ul standard Odoo Enterprise pentru rapoarte financiare și return-uri (`account.return`), pe care se bazează întregul flux al modulului.
- `l10n_ro_reports`: furnizează rapoartele financiare P&L românești (micro/SMLE/internațional) folosite pentru a identifica tipurile de return relevante prin `is_pl_closing_return_type`.
- `l10n_ro_account_period_close` (OCA): modul alternativ cu funcționalitate similară de închidere a exercițiului/perioadei, dar cu arhitectură diferită (fără framework-ul `account.return`); menționat în documentație ca punct de comparație.
