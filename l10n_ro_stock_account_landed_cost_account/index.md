# Romania - Stock Accounting Landed Cost Account (localizat la `l10n_ro_stock_account_landed_cost_account/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_account_landed_cost_account`
- **Versiune:** `19.0.1.1.2`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_stock_account_landed_cost_account
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_stock_account_landed_cost_account`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul stabilește conturile contabile corecte pentru notele generate de costurile suplimentare de achiziție (landed costs) în companiile românești. Contul de stoc este preluat din locațiile de stoc, iar contul de cheltuială/venit al liniei de factură este transferat pe linia costului suplimentar. Opțional, creditarea directă a unui cont din clasa 6 poate fi înlocuită cu un traseu printr-un cont intermediar tehnic, rezultând două note contabile echilibrate și curate.

#### 2. Funcționalități Cheie

- Determinarea contului de valorizare din locația de stoc (sursă sau destinație, după cum mișcarea este de intrare sau de ieșire), în locul contului implicit al categoriei de produs.
- Aplicarea mapării din poziția fiscală a jurnalului costului suplimentar asupra conturilor de debit și credit.
- La crearea costului suplimentar din factura furnizorului, sunt preluate automat recepțiile finalizate din comenzile de achiziție ale facturii (fără cele deja incluse într-un cost suplimentar validat), iar contul fiecărei linii de cost este aliniat la contul liniei de factură corespunzătoare.
- La bifarea „Cost suplimentar" pe o linie de factură cu produs de tip serviciu, contul se completează automat din contul de cheltuială (la achiziții) sau de venit (la vânzări) al produsului.
- Setare per companie „Landed Cost Class 6 Method" (Contabilitate / setări România):
  - **Standard** (implicit): comportamentul nativ Odoo, valorizare stoc = cont clasa 6;
  - **Prin cont intermediar**: creditul spre clasa 6 este rutat printr-un cont intermediar tehnic (ex. 482.99), rezultând două note echilibrate (valorizare stoc = intermediar și intermediar = clasa 6), utile la exportul în programe de contabilitate externe. Contul intermediar apare și este obligatoriu doar pentru această metodă; contul 609 nu este niciodată redirecționat.
- La actualizare, comportamentul rămâne neschimbat (Standard) până la schimbarea explicită a metodei.

#### 3. Dependențe

- `stock_landed_costs`
- `l10n_ro_stock_account`
- `l10n_ro_config`

#### 4. Componente Cheie

**Modele**

- `account.move` (extins): `button_create_landed_costs` atașează recepțiile aferente și aliniază conturile liniilor de cost cu cele din factură (doar pentru înregistrări românești).
- `account.move.line` (extins): onchange pe `is_landed_costs_line` care setează contul din produs pentru serviciile marcate ca cost suplimentar.
- `stock.valuation.adjustment.lines` (extins): `_create_account_move_line` determină conturile din locații și poziția fiscală; `_l10n_ro_route_class6_through_intermediary` redirecționează creditele clasa 6 (fără 609) prin contul intermediar.
- `res.company` (extins): câmpurile `l10n_ro_landed_cost_method` și `l10n_ro_landed_cost_intermediary_account_id`.
- `res.config.settings` (extins): câmpuri related către cele două setări ale companiei.

**Vizualizări**

- `res_config_settings_view_form`: extinde formularul de setări `l10n_ro_config` cu selectorul metodei și contul intermediar (vizibil doar pentru metoda „intermediary").

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `l10n_ro_stock_account`: logica de valorizare a stocului pe locații, completată aici pentru costurile suplimentare.
- `l10n_ro_config`: setările de contabilitate România în care apare opțiunea.
