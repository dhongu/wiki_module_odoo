# Romania - Fișa partenerului în valută (localizat la `l10n_ro_partner_ledger_currency/index.md`)

- **Nume Tehnic:** `l10n_ro_partner_ledger_currency`
- **Versiune:** `19.0.1.4.13`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_partner_ledger_currency
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_partner_ledger_currency`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde raportul Partner Ledger (Fișa Partenerului) din Odoo Enterprise cu coloane în valuta originală a tranzacțiilor, conform OMFP 1802/2014 Pct. 7 alin. (2) — contabilitatea operațiunilor în valută se ține atât în RON, cât și în valută. Pe lângă coloanele standard în RON, afișează Debit, Credit și Sold în valuta efectivă (EUR, USD etc.), fiind util companiilor care vând/cumpără în valută și trebuie să confirme soldul cu parteneri externi, să verifice rulajul valutar per partener și să reconcilieze balanța în RON cu soldul comunicat de partener în valuta sa.

#### 2. Funcționalități Cheie

- Coloane **Debit Valută** și **Credit Valută**: suma debitată/creditată în valuta originală a tranzacției (EUR, USD etc.).
- Coloana **Sold Valută**: sold progresiv acumulat în valuta originală (running balance). Pe linia **Sold Inițial** apare în valuta partenerului (ex. `-199,99 €`), nu în lei. Pe rândul unui partener cu o singură valută străină arată soldul valutar de la început până la sfârșitul perioadei (sold inițial + mișcări), iar coloana **Valută** (mișcările din perioadă) rămâne goală pe rândul partenerului și se citește pe liniile de detaliu; la partenerii cu mai multe valute străine, **Sold Valută** rămâne gol pe rândul partenerului, iar soldurile sunt pe grupurile de valută.
- Netransparent pentru RON: tranzacțiile în RON au coloanele valutare goale, pentru vizibilitate clară a operațiunilor cu valută efectivă.
- Păstrarea coloanelor standard **Debit (RON)**, **Credit (RON)**, **Sold (RON)**.
- Vizibil automat doar pentru companiile cu Țara = România, și doar când baza de date are multi-valută activă (Setări → Contabilitate → Valute).
- Meniu: **Contabilitate → Raportare → Rapoarte parteneri → Fișa Partenerului în Valută**. Pentru ca raportul să apară trebuie activat suportul multi-valută (**Setări → Contabilitate → Valute**, cel puțin o valută străină, cu cursuri disponibile).
- Convenția de semn: **sold pozitiv = sumă de încasat** de companie, **sold negativ = sumă de plătit** (la furnizori soldul apare negativ).
- Moștenește toate funcționalitățile Partner Ledger: sold inițial, export PDF/XLSX, filtre parteneri/jurnale, drill-down, reconciliere.
- Filtrul „Cont" extins doar pe acest raport: conturile de avans **409** (Furnizori-debitori) intră sub **Payable**, **419** (Clienți-creditori) sub **Receivable** — altfel rămâneau invizibile, fiind `liability_current` în planul RO și nu `asset_receivable`/`liability_payable`. Extinderea este aplicată consecvent atât pe antetul partenerului (agregatele calculate de handler), cât și pe liniile desfășurate pe ecran sub fiecare grup de valută — vezi corecția din 19.0.1.4.4 la Componente Cheie.
- Parteneri cu mai multe valute (ex. EUR și USD): raportul inserează automat un sub-nivel de grupare pe valută, fiecare cu propriul sold inițial și sold rulant.
- **Confirmare sold (PDF)**: extras de cont compact per partener, cu o linie per valută (sold inițial / rulaje / sold final, în valută și RON) și text de confirmare conform OMFP 2861/2009, pentru inventarierea anuală a creanțelor și datoriilor. Soldul de **avans (409/419)** apare pe un **rând separat** de soldul comercial al aceleiași valute, necompensat (OMFP 1802/2014 pct. 56); rândul de total al documentului este doar informativ — „Poziție netă totală (RON), cu titlu informativ" — soldul care se confirmă este cel de pe fiecare rând.
- **Fișă în valută (PDF)**: fișă de cont în format clasic, o fișă per (partener, cont, valută), cu antet de sold precedent (*Debit precedent*, *Credit precedent*, *Sold inițial*), linii per document, sold cumulat, *Rulaj total* și *Sold final*. Respectă filtrele raportului (perioadă, partener, cont, jurnal, text din bara de căutare). Un singur PDF poate conține cel mult 100 de fișe (partener × cont × valută); peste această limită exportul este refuzat cu un mesaj care cere selectarea unui partener sau restrângerea perioadei. Funcționează și pe conturile de avans (409/419), prin filtrarea pe cont, iar tranzacțiile în moneda companiei apar ca fișe separate în lei.
- **Export complet pentru arhivare**: butoanele standard **PDF** (landscape) și **XLSX** din antetul raportului includ și coloanele valutare, cu grupurile de valută dacă partenerii sunt desfăcuți.
- Avansurile nu se reevaluează la curs: la un partener cu avans, raportul dintre soldul în lei și cel în valută poate să nu corespundă unui singur curs — nu e o eroare a raportului. Antetul grupului de valută și **Sold Valută** adună și avansul, deci pot diferi de soldul din **Confirmare sold (PDF)**; soldul de confirmat este cel de pe fiecare rând din PDF.

#### 3. Dependențe

- `account_reports`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.partner.currency.report.handler` (`AbstractModel`, moștenește `account.partner.ledger.report.handler`): injectează coloanele valutare (`debit_currency`, `credit_currency`, `balance_currency`) în opțiunile raportului Partner Ledger, extinde query-ul SQL pe `account.move.line` cu sumele brute în valută, calculează soldul inițial și soldul rulant per valută, grupează liniile pe valută sub fiecare partener și expune exporturile PDF „Confirmare sold" și „Fișă în valută". Pentru „Confirmare sold" agregarea soldurilor se face și pe tipul contului (`_l10n_ro_advance_kind_case_sql`, pattern `_ADVANCE_PREFIXES`): soldul comercial (401/4111) și soldul de avans (409/419) sunt calculate și afișate ca rânduri distincte, fără compensare.
- `account.report` (extensie, `account_report.py`): `_get_options_account_type_domain` — extinde domeniul filtrului standard „Cont" (Receivable/Payable) pentru a include și conturile de avans 409%/419% pe acest raport, dar doar dacă raportul curent (`options['report_id']`, nu `self`) este chiar Fișa Partenerului în Valută. Verificarea prin `options['report_id']` este obligatorie: nucleul (`_get_aml_values`, `enterprise/account_reports/models/account_partner_ledger.py`) aduce liniile pentru desfășurarea pe ecran (grupul de valută, sub fiecare partener) pe raportul standard hardcodat (`account_reports.partner_ledger_report`), nu pe raportul curent din context — dacă metoda ar verifica `self`, extinderea 409/419 s-ar aplica corect agregatelor din handler (antetul partenerului, Sold inițial, Confirmare sold PDF), dar NU și liniilor efectiv desfășurate pe ecran, ducând la un total din antet care nu se regăsea în liniile vizibile ale grupului de valută (fix 19.0.1.4.4, tichet #9575).

**Vizualizări / Date**

- `data/l10n_ro_partner_currency_report.xml`: definește raportul `account.report` „Fișa Partenerului în Valută" (vizibil doar pentru `country_id = base.ro`), coloanele standard RON + `amount_currency`, filtrul `filter_aml_ir_filters` pentru izolarea unei singure valute, acțiunea client și meniul (Contabilitate → Raportare → Rapoarte parteneri).
- `data/confirmare_sold_pdf.xml`: șablon QWeb `confirmare_sold_pdf` — extras de cont compact, o pagină per partener, cu tabel per valută și tip de sold (comercial vs. avans, pe rânduri separate), în valută și RON, plus text legal OMFP 2861/2009.
- `data/fisa_cont_valuta_pdf.xml`: acțiune `ir.actions.report` + șablon QWeb `fisa_cont_valuta_pdf` — fișă de cont clasică per (partener, cont, valută), randată cu `web.external_layout`.
- `security/ir.model.access.csv`: acces în citire pentru `account.group_account_readonly` pe handlerul raportului.

**Acțiuni Automate / Acțiuni Server**

*Nu există acțiuni automate (`ir.cron`) sau reguli `base.automation`.* Modulul expune două butoane de export în antetul raportului („Confirmare sold (PDF)" și „Fișă în valută (PDF)"), executate la cerere de utilizator, nu programat.

#### 5. Conexiuni

- `account_reports`: modulul de bază Enterprise ale cărui componente (handler-ul Partner Ledger, motorul de raportare) sunt extinse.
- `l10n_ro`: localizarea românească; raportul este activ doar pentru companii cu `country_id = base.ro`.
- [l10n_ro_balance_confirmation](../l10n_ro_balance_confirmation/index.md): confirmarea de sold în RON pentru toți partenerii; modulul de față oferă echivalentul în valută, cu logica de separare a avansurilor (409/419) preluată de acolo (`_ADVANCE_PREFIXES`).
- [l10n_ro_currency_revaluation](../l10n_ro_currency_revaluation/index.md): reevaluarea lunară la cursul BNR a soldurilor în valută — complementar; avansurile (409/419) sunt elemente nemonetare și nu se reevaluează.
- `currency_rate_live`: opțional, pentru actualizarea automată a cursurilor valutare folosite la afișarea soldurilor.
- [l10n_ro_partner_trial_balance](../l10n_ro_partner_trial_balance/index.md): extinde aceeași metodă de domeniu a filtrului „Cont” (`_get_options_account_type_domain`) cu intrările Avansuri (409, 419) și Alte conturi de terți, pentru balanța pe parteneri și, opțional, pentru Partner Ledger standard; cele două extensii coexistă (testate împreună).
