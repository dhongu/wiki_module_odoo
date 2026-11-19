# Romania - Creanțe și datorii extinse (localizat la `l10n_ro_receivables_enhanced/index.md`)

- **Nume Tehnic:** `l10n_ro_receivables_enhanced`
- **Versiune:** `19.0.1.5.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_receivables_enhanced
- **Cale Locală:** odoo-addons/l10n_ro_ent/l10n_ro_receivables_enhanced
- **Ultima Ingestie:** `2026-11-19`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul extinde gestiunea creanțelor și datoriilor cu trei elemente cerute în practica contabilă din România: **compensarea client-furnizor** cu proces-verbal, **penalitățile de întârziere** calculate pe baza ratei contractuale a partenerului și un parametru de **limită de credit** per partener. Servește la stingerea soldurilor reciproce și la controlul expunerii pe client.

Pentru un partener care este simultan client și furnizor, contabilul creează o compensare și încarcă dintr-un clic creanțele (411) și datoriile (401) neachitate la data compensării. Modulul propune alocarea FIFO, iar contabilul poate alege suma compensată pe fiecare factură. La confirmare se generează nota contabilă și se reconciliază exact sumele alese, iar procesul-verbal de compensare poate fi tipărit în PDF pentru semnătura părților.

#### 2. Funcționalități Cheie

- Document de compensare client-furnizor (`l10n.ro.partner.compensation`), creat din Contabilitate → Clienți → Compensări client-furnizor, cu liniile reciproce ale aceluiași partener (inclusiv contactele lui).
- Încărcarea creanțelor (tab-ul Receivables 411) și a datoriilor (tab-ul Payables 401/404) neachitate la data compensării; sunt folosite doar conturile comerciale, avansurile și notele de credit rămase pe aceste conturi nu se încarcă.
- Suma compensată aleasă pe fiecare factură (între 0 și soldul inițial; linia cu 0 e omisă), cu alocare FIFO propusă automat și buton de realocare.
- Notă contabilă (Dr 401 = Cr 411) cu o linie pe factură și reconciliere parțială exactă pe 411/401; confirmarea cere reîncărcarea dacă între timp o factură a fost plătită.
- Proces-verbal de compensare tipăribil (PDF) cu soldul inițial, suma compensată și soldul rămas pe fiecare factură.
- Anulare (drept de administrator contabil) și readucere în ciornă cu reluarea liniilor.
- Calcul penalități de întârziere (Contabilitate → Clienți → Calcul penalități): penalitate = sold restant × rată / 100 × zile de întârziere, pe baza ratei contractuale din fișa partenerului (în % pe zi, ex. `0.05` pentru 0,05%/zi). Dobânda legală penalizatoare (Legea 72/2013, OG 13/2011) nu se calculează automat.
- Factură de penalitate generată din wizard, fără TVA, pe contul 7581 (sau pe contul din Setări → Creanțe (RO) → Cont de venituri din penalități): Dr 4111 = Cr 7581; fiecare click creează o factură nouă.
- Limită de credit RO (cu monedă) per partener, în tab-ul „Creanțe RO”; câmp separat de limita de credit standard Odoo, `0` = fără limită.
- Blocare opțională (per companie, Setări → Creanțe (RO) → Aplică limita de credit) a postării facturilor de client care ar depăși limita de credit RO a partenerului.

#### 3. Dependențe

- `account`
- `l10n_ro`
- `l10n_ro_move_guard`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.partner.compensation` / `l10n.ro.partner.compensation.line`: Operațiunea de compensare a soldurilor reciproce client-furnizor (linii de creanță 411 și datorie 401, sumă compensată pe factură, notă contabilă, PV).
- `l10n.ro.penalty.wizard` / `l10n.ro.penalty.wizard.line`: Wizard pentru calculul penalităților de întârziere și generarea facturii de penalitate.
- `res.partner`: Extins cu rata de penalitate (% pe zi), limita de credit RO și moneda limitei (tab „Creanțe RO”).
- `res.company` / `res.config.settings`: Setările de blocare la limita de credit (`l10n_ro_credit_limit_enforce`) și contul de venituri din penalități.
- `account.move`: Extins cu verificarea limitei de credit în garda de postare (`_l10n_ro_posting_guard_errors`), activă doar dacă blocarea e bifată pe companie, factura e de client și partenerul are limită pozitivă.

**Vizualizări**

- `view_l10n_ro_compensation_form` / `view_l10n_ro_compensation_list`: Interfața pentru gestionarea compensărilor (acțiunea `action_l10n_ro_compensation`).
- `view_partner_form_l10n_ro_receivables`: Tab-ul „Creanțe RO” pe formularul partenerului (rată penalitate, limită de credit, monedă).
- `res_config_settings_view_form_receivables`: Secțiunea „Creanțe (RO)” din Setări (aplicare limită de credit, cont de venituri din penalități).
- `view_l10n_ro_penalty_wizard_form`: Wizardul de calcul penalități (acțiunea `action_l10n_ro_penalty_wizard`).
- `report/report_compensation.xml`: Șablonul PDF pentru procesul-verbal de compensare.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`) în modul.*

#### 5. Conexiuni

- [l10n_ro_partner_ledger_currency](../l10n_ro_partner_ledger_currency/index.md): fișa partenerului în valută, complementară urmăririi creanțelor.
- `l10n_ro_move_guard`: furnizează mixinul gărzii de postare (`_l10n_ro_posting_guard_errors`) folosit pentru blocarea peste limita de credit; modulul nu mai depinde de `l10n_ro_anaf_base`, unde se afla anterior garda.
- `account`: liniile contabile (creanțe 411 / datorii 401) și reconcilierea.
