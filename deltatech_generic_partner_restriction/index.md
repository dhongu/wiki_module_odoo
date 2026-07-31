# Restricție Jurnale pentru Partenerul Generic (localizat la `deltatech_generic_partner_restriction/index.md`)

- **Nume Tehnic:** `deltatech_generic_partner_restriction`
- **Versiune:** `19.0.2.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_generic_partner_restriction
- **Cale Locală:** `odoo-addons/deltatech/deltatech_generic_partner_restriction`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul restricționează, la înregistrarea plăților, jurnalele bancare și de casă disponibile atunci când partenerul selectat este "partenerul generic" configurat pe companie. Practic, permite excluderea anumitor conturi/case de marcat din lista de jurnale afișate pentru încasările/plățile efectuate pe acest partener generic (folosit de obicei pentru vânzări cu amănuntul sau clienți neidentificați), evitând astfel utilizarea greșită a unor jurnale rezervate altor fluxuri.

#### 2. Funcționalități Cheie

- Adaugă pe jurnalul contabil (`account.journal`) o bifă "Restricție Generic" care marchează jurnalul ca fiind interzis pentru partenerul generic.
- La deschiderea unei plăți (`account.payment`) pentru partenerul generic al companiei, lista de jurnale disponibile exclude automat jurnalele bancare/casă marcate cu restricție.
- Pentru orice alt partener (diferit de cel generic), toate jurnalele rămân disponibile ca de obicei.
- Câmpul de restricție este vizibil (opțional, ascuns implicit) în vizualizarea listă a jurnalelor și în formularul jurnalului.

#### 3. Dependențe

- `account`
- [deltatech_partner_generic](../deltatech_partner_generic/index.md)

#### 4. Componente Cheie

**Modele**

- `account.payment` (extins): suprascrie `_compute_available_journal_ids` pentru a filtra, în cazul partenerului generic al companiei, jurnalele bancare/casă marcate cu `restriction`.
- `account.journal` (extins): adaugă câmpul boolean `restriction` ("Generic Restriction") care marchează jurnalul ca restricționat pentru partenerul generic.

**Vizualizări**

- `account_journal_view_list` (extinde `account.view_account_journal_tree`): adaugă coloana `restriction` (ascunsă implicit) înainte de câmpul `type`.
- `account_journal_view_form` (extinde `account.view_account_journal_form`): adaugă câmpul `restriction` în formularul jurnalului, înainte de câmpul `type`.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

- [deltatech_partner_generic](../deltatech_partner_generic/index.md): furnizează câmpul `generic_partner_id` pe companie, folosit de acest modul pentru a identifica partenerul generic ale cărui plăți sunt restricționate.
