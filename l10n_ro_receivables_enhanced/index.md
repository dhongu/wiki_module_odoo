# Romania - Creanțe și datorii extinse (localizat la `l10n_ro_receivables_enhanced/index.md`)

- **Nume Tehnic:** `l10n_ro_receivables_enhanced`
- **Versiune:** `20.0.1.5.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_receivables_enhanced
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_receivables_enhanced`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde gestiunea creanțelor și datoriilor cu trei elemente cerute în practica contabilă din România: compensarea client-furnizor cu proces-verbal, penalitățile de întârziere conform Legii 72/2013 și parametri de limită de credit per partener. Servește la stingerea soldurilor reciproce și la controlul expunerii pe client.

Pentru un partener care este simultan client și furnizor, contabilul creează o compensare și încarcă dintr-un clic creanțele (411) și datoriile (401) neachitate la data compensării. Modulul propune alocarea FIFO, iar contabilul poate alege suma compensată pe fiecare factură. La confirmare se generează nota contabilă și se reconciliază exact sumele alese, iar procesul-verbal poate fi tipărit în PDF.

#### 2. Funcționalități Cheie

- Document de compensare client-furnizor (Contabilitate → Creanțe → Compensări Client-Furnizor) cu liniile reciproce ale aceluiași partener, inclusiv contactele lui; jurnal de tip Diverse.
- „Încarcă documentele neachitate": creanțe 411x și datorii 401x/404x până la data compensării; avansurile și notele de credit nu se încarcă.
- Suma compensată aleasă pe fiecare factură (între 0 și soldul restant), cu alocare FIFO propusă automat („Alocă FIFO"); diferența dintre creanțe și datorii trebuie să fie 0 la confirmare.
- Notă contabilă cu o linie pe factură și reconciliere parțială exactă pe 411/401.
- Proces-verbal de compensare tipăribil (PDF) cu soldul restant, suma compensată și soldul rămas pe fiecare factură.
- Anulare / readucere în ciornă cu reluarea liniilor.
- Penalități de întârziere pe baza ratei contractuale configurate pe partener (% pe zi), cu factură de penalitate fără TVA pe 7581; dobânda legală penalizatoare nu se calculează automat.
- Limită de credit (cu monedă) per partener, informativă implicit; blocare opțională a postării facturilor de client peste limită, activată per companie în Setări.

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_move_guard](../l10n_ro_move_guard/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.partner.compensation` / `l10n.ro.partner.compensation.line`: Compensarea soldurilor reciproce client-furnizor (linii 411/401, sumă compensată, notă contabilă, PV).
- `l10n.ro.penalty.wizard` / `l10n.ro.penalty.wizard.line`: Wizard pentru calculul penalităților de întârziere și generarea facturii de penalitate.
- `res.partner` (extins): Rata de penalitate, limita de credit și moneda ei (tab „Creanțe RO").
- `res.company` / `res.config.settings` (extinse): Activarea blocării la depășirea limitei de credit și contul de venituri din penalități.
- `account.move` (extins): Verificarea limitei de credit în garda de postare (`_l10n_ro_posting_guard_errors`), activă doar dacă blocarea e bifată pe companie și partenerul are limită pozitivă.

**Vizualizări**

- `views/l10n_ro_compensation_views.xml`: Interfața pentru compensări.
- `views/res_partner_views.xml`: Tab-ul „Creanțe RO" pe fișa partenerului.
- `views/res_config_settings_views.xml`: Setările de limită de credit și cont de penalități.
- `views/menus.xml`: Meniul „Customer-Vendor Offsets" sub Contabilitate → Creanțe.
- `wizard/l10n_ro_penalty_wizard_views.xml`: Wizardul de calcul penalități.
- `report/report_compensation.xml`: Șablonul PDF al procesului-verbal de compensare.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`) în modul.*

#### 5. Conexiuni

- [l10n_ro_move_guard](../l10n_ro_move_guard/index.md): furnizează garda de postare extinsă pentru blocarea peste limita de credit.
- [l10n_ro_partner_ledger_currency](../l10n_ro_partner_ledger_currency/index.md): fișa partenerului în valută, complementară urmăririi creanțelor.
- `account`: liniile contabile (creanțe 411 / datorii 401) și reconcilierea.
