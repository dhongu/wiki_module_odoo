# Creanțe și Datorii Extinse România (FR-29) (localizat la `l10n_ro_receivables_enhanced/index.md`)

- **Nume Tehnic:** `l10n_ro_receivables_enhanced`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_receivables_enhanced
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_receivables_enhanced`
- **Ultima Ingestie:** 2026-08-20
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul extinde gestiunea creanțelor și datoriilor cu trei elemente cerute în practica contabilă din România: **compensarea client-furnizor** cu proces-verbal, **penalitățile de întârziere** conform Legii 72/2013 și parametri de **limită de credit** per partener. Servește la stingerea soldurilor reciproce și la controlul expunerii pe client.

Pentru un partener care este simultan client și furnizor, contabilul creează o compensare, selectează liniile de creanță (411) și de datorie (401) deschise, iar modulul calculează suma compensată ca minimul dintre cele două totaluri. La confirmare se generează nota contabilă și se reconciliază liniile, iar procesul-verbal de compensare poate fi tipărit în PDF pentru semnătura părților.

#### 2. Funcționalități Cheie

- Document de compensare client-furnizor (`l10n.ro.partner.compensation`) cu selecția liniilor reciproce ale aceluiași partener.
- Calcul automat al sumei compensate = `min(total creanțe, total datorii)`.
- Generarea notei contabile de compensare și reconcilierea liniilor 411/401.
- Proces-verbal de compensare tipăribil (PDF) cu liniile și suma compensată.
- Anulare / readucere în ciornă cu reluarea liniilor.
- Calcul penalități de întârziere pe baza ratei configurate pe partener (Legea 72/2013), cu wizard de generare a facturii de penalitate.
- Parametri de limită de credit (cu monedă) per partener pentru monitorizarea expunerii.
- Blocare opțională (per companie, în Setări) a postării facturilor de client care depășesc limita de credit a partenerului — implementată prin garda de postare din `l10n_ro_anaf_base`.

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.partner.compensation`: Gestionează operațiunea de compensare a soldurilor reciproce client-furnizor (linii de creanță 411 și datorie 401, sumă compensată, notă contabilă, PV).
- `l10n.ro.penalty.wizard` / `l10n.ro.penalty.wizard.line`: Wizard pentru calculul penalităților de întârziere conform Legii 72/2013 și generarea facturii de penalitate.
- `res.partner`: Extins cu rata de penalitate (% pe zi), limita de credit și moneda limitei de credit (tab „Creanțe RO").
- `res.company` / `res.config.settings`: Câmpul `l10n_ro_credit_limit_enforce` — activează blocarea la postare peste limita de credit.
- `account.move`: Extins cu verificarea limitei de credit în garda de postare (`_l10n_ro_posting_guard_errors`), activă doar dacă blocarea e bifată pe companie și partenerul are limită pozitivă.

**Vizualizări**

- `views/l10n_ro_compensation_views.xml`: Interfața pentru gestionarea compensărilor.
- `views/res_partner_views.xml`: Tab-ul „Creanțe RO" pe formularul partenerului (rată penalitate, limită de credit, monedă).
- `views/res_config_settings_views.xml`: Setarea „Enforce Credit Limit" în blocul de localizare fiscală din Setări Contabilitate.
- `views/menus.xml`: Meniul „Customer-Vendor Offsets" sub Contabilitate → Creanțe.
- `wizard/l10n_ro_penalty_wizard_views.xml`: Vizualizarea wizardului de calcul penalități.
- `report/report_compensation.xml`: Șablonul PDF pentru procesul-verbal de compensare.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`) în modul.*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): furnizează mixinul gărzii de postare (`_l10n_ro_posting_guard_errors`) folosit pentru blocarea peste limita de credit.
- [l10n_ro_partner_ledger_currency](../l10n_ro_partner_ledger_currency/index.md): fișa partenerului în valută, complementară urmăririi creanțelor.
- `account`: liniile contabile (creanțe 411 / datorii 401) și reconcilierea.
