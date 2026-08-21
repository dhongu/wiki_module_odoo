# Fișa Partenerului în Valută (localizat la `l10n_ro_partner_ledger_currency/index.md`)

- **Nume Tehnic:** `l10n_ro_partner_ledger_currency`
- **Versiune:** `19.0.1.4.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_partner_ledger_currency
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_partner_ledger_currency`
- **Ultima Ingestie:** 2026-08-20
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde raportul Partner Ledger (Fișa Partenerului) din Odoo Enterprise cu coloane în valuta originală a tranzacțiilor, conform OMFP 1802/2014 Pct. 7 alin. (2) — contabilitatea operațiunilor în valută se ține atât în RON, cât și în valută. Pe lângă coloanele standard în RON, afișează Debit, Credit și Sold în valuta efectivă (EUR, USD etc.), fiind util companiilor care vând/cumpără în valută și trebuie să confirme soldul cu parteneri externi, să verifice rulajul valutar per partener și să reconcilieze balanța în RON cu soldul comunicat de partener în valuta sa.

#### 2. Funcționalități Cheie

- Coloane **Debit Valută** și **Credit Valută**: suma debitată/creditată în valuta originală a tranzacției (EUR, USD etc.).
- Coloana **Sold Valută**: sold progresiv acumulat în valuta originală (running balance).
- Netransparent pentru RON: tranzacțiile în RON au coloanele valutare goale, pentru vizibilitate clară a operațiunilor cu valută efectivă.
- Păstrarea coloanelor standard **Debit (RON)**, **Credit (RON)**, **Sold (RON)**.
- Vizibil automat doar pentru companiile cu Țara = România.
- Moștenește toate funcționalitățile Partner Ledger: sold inițial, export PDF/XLSX, filtre parteneri/jurnale, drill-down, reconciliere.
- Parteneri cu mai multe valute (ex. EUR și USD): raportul inserează automat un sub-nivel de grupare pe valută, fiecare cu propriul sold inițial și sold rulant.
- **Confirmare sold (PDF)**: extras de cont compact per partener, cu o linie per valută (sold inițial / rulaje / sold final, în valută și RON) și text de confirmare conform OMFP 2861/2009, pentru inventarierea anuală a creanțelor și datoriilor.
- **Fișă în valută (PDF)**: fișă de cont în format clasic, o fișă per (partener, cont, valută), cu antet de sold precedent, linii per document și sold cumulat.

#### 3. Dependențe

- `account_reports`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.partner.currency.report.handler` (`AbstractModel`, moștenește `account.partner.ledger.report.handler`): injectează coloanele valutare (`debit_currency`, `credit_currency`, `balance_currency`) în opțiunile raportului Partner Ledger, extinde query-ul SQL pe `account.move.line` cu sumele brute în valută, calculează soldul inițial și soldul rulant per valută, grupează liniile pe valută sub fiecare partener și expune exporturile PDF „Confirmare sold" și „Fișă în valută".

**Vizualizări / Date**

- `data/l10n_ro_partner_currency_report.xml`: definește raportul `account.report` „Fișa Partenerului în Valută" (vizibil doar pentru `country_id = base.ro`), coloanele standard RON + `amount_currency`, filtrul `filter_aml_ir_filters` pentru izolarea unei singure valute, acțiunea client și meniul (Contabilitate → Raportare → Parteneri).
- `data/confirmare_sold_pdf.xml`: șablon QWeb `confirmare_sold_pdf` — extras de cont compact, o pagină per partener, cu tabel per valută (sold inițial/rulaje/sold final, în valută și RON) și text legal OMFP 2861/2009.
- `data/fisa_cont_valuta_pdf.xml`: acțiune `ir.actions.report` + șablon QWeb `fisa_cont_valuta_pdf` — fișă de cont clasică per (partener, cont, valută), randată cu `web.external_layout`.
- `security/ir.model.access.csv`: acces în citire pentru `account.group_account_readonly` pe handlerul raportului.

**Acțiuni Automate / Acțiuni Server**

*Nu există acțiuni automate (`ir.cron`) sau reguli `base.automation`.* Modulul expune două butoane de export în antetul raportului („Confirmare sold (PDF)" și „Fișă în valută (PDF)"), executate la cerere de utilizator, nu programat.

#### 5. Conexiuni

- `account_reports`: modulul de bază Enterprise ale cărui componente (handler-ul Partner Ledger, motorul de raportare) sunt extinse.
- `l10n_ro`: localizarea românească; raportul este activ doar pentru companii cu `country_id = base.ro`.
