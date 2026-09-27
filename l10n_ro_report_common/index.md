# Romania - Report Common (localizat la `l10n_ro_report_common/index.md`)

- **Nume Tehnic:** `l10n_ro_report_common`
- **Versiune:** `20.0.1.1.0`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_report_common
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_report_common`
- **Ultima Ingestie:** `2026-09-27`

#### 1. Sumar

Modulul oferă blocurile QWeb comune folosite de rapoartele tipărite românești
(factură, comandă de vânzare, aviz de expediție, confirmare de sold): antetul
de identificare a companiei și lista conturilor bancare de afișat. În plus,
rescrie modul în care Odoo scrie sumele în litere pentru moneda RON, astfel
încât textul de pe o chitanță sau factură să respecte uzanța contabilă
românească (ex. „opt mii trei sute optzeci și doi de lei și douăzeci și cinci
de bani"), în loc de formularea standard Odoo, nefirească în română.

#### 2. Funcționalități Cheie

- Șablon QWeb `l10n_ro_report_common.banks` — tipărește până la 3 conturi
  bancare ale partenerului marcate *Print in Report*, în moneda documentului
  (cu fallback pe moneda companiei); moneda unui cont bancar este cea a
  jurnalului bancar asociat, iar conturile fără jurnal sunt considerate în
  moneda companiei.
- Șablon QWeb `l10n_ro_report_common.report_address_company` — blocul de
  identificare a companiei pe rapoarte: denumire, adresă, conturi bancare,
  CUI, Nr. Reg. Com. și capital social.
- Suprascrie `res.currency.amount_to_text` pentru RON: numeralul *unu* devine
  *un* înaintea substantivului (*un leu*), substantivul se acordă la plural,
  particula *de* se leagă când ultima grupă a numeralului e 20 sau peste ori
  numeralul se termină într-o sută/mie întreagă (*cinci sute de lei*, dar *o
  sută unu lei*, *nouăsprezece lei*), suma se rotunjește după precizia monedei,
  iar formularea în lei rămâne în română indiferent de limba de tipărire a
  documentului (ex. pe o factură în engleză). Pentru orice altă monedă se
  păstrează comportamentul standard Odoo.
- Necesită biblioteca Python `num2words` (`>=0.5.12`); dacă lipsește, se revine
  automat la formularea implicită Odoo.
- Adaugă câmpul *Print in Report* (`l10n_ro_print_report`) pe conturile
  bancare ale partenerilor și câmpul *Share Capital* (`l10n_ro_share_capital`)
  pe companie — vizibile în formularele standard (`res.partner.bank`,
  `res.company`).
- Numele acestor două câmpuri sunt identice cu cele istorice din modulul OCA
  `l10n_ro_config`, astfel încât clienții care migrează de pe stack-ul OCA își
  păstrează configurarea fără migrare de date; cele două module pot fi
  instalate simultan.

#### 3. Dependențe

- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `res.company` (extindere): adaugă `l10n_ro_share_capital` (capitalul social,
  tipărit în antetul rapoartelor românești).
- `res.partner.bank` (extindere): adaugă `l10n_ro_print_report` (bifă pentru
  includerea contului bancar pe rapoarte).
- `res.currency` (extindere): suprascrie `amount_to_text` pentru a genera
  formularea în litere specifică limbii române pentru moneda RON.

**Vizualizări**

- `view_partner_bank_form` / `view_partner_bank_tree`: expun câmpul *Print in
  Report* pe formularul și lista conturilor bancare ale partenerilor.
- `view_company_form`: expune câmpul *Share Capital* pe formularul companiei.
- Șabloane QWeb `banks` și `report_address_company`
  (`l10n_ro_report_common.banks` / `l10n_ro_report_common.report_address_company`):
  blocuri reutilizabile incluse de rapoartele Odoo pentru afișarea conturilor
  bancare, respectiv a antetului de identificare a companiei.

**Acțiuni Automate / Acțiuni Server**

- Nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- `l10n_ro`: localizarea românească de bază, dependința directă a modulului.
