# Romania - Înregistrări în Avans (471/472) (localizat la `l10n_ro_deferred_entries/index.md`)

- **Nume Tehnic:** `l10n_ro_deferred_entries`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_deferred_entries
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_deferred_entries`
- **Ultima Ingestie:** 2026-06-01

## 1. Sumar

Modulul implementează recunoașterea automată a cheltuielilor și veniturilor înregistrate în avans (conturile 471 și 472) conform OMFP 1802/2014 pct. 233-237. La postarea unei facturi cu linie pe contul 471 sau 472, dacă utilizatorul completează intervalul de recunoaștere, modulul creează automat un plan de recunoaștere bazat pe `account.asset` (Enterprise), care generează și postează notele lunare la scadență.

## 2. Funcționalități Cheie

- **Planuri automate de recunoaștere 471/472:** la postarea facturii cu linie pe 471/472 și completarea câmpurilor „Avans: de la" și „Avans: până la", se creează automat un plan de recunoaștere bazat pe `account.asset`.
- **Monografii contabile RO:** cheltuieli în avans (Dr 471 = Cr 401; lunar Dr 6xx = Cr 471) și venituri în avans (Dr 4111 = Cr 472; lunar Dr 472 = Cr 7xx).
- **Flux de lucru:** factura creează planul în stare Draft; după verificarea contului-țintă și confirmare, Enterprise generează automat notele lunare.
- **Modele preconfigurate** „Model 471" și „Model 472" cu cont cheltuială/venit țintă configurabil (ex. 613 asigurări, 706 chirii).

## 3. Dependențe

- `account_asset`
- `l10n_ro`

## 4. Componente Cheie

### Modele

- `account.asset`: reutilizat ca plan de recunoaștere 471/472, cu modele dedicate preconfigurate.
- `account.move` / `account.move.line`: extinse cu câmpurile „Avans: de la" / „Avans: până la" și logica de generare automată a planului la postare.

### Vizualizări / Date

- `views/account_move_views.xml`: câmpurile de interval avans pe linia de factură și smart button către plan.
- `data/account_asset_data.xml`: modelele preconfigurate „Model 471" și „Model 472".

### Acțiuni Automate / Acțiuni Server

- Recunoașterea lunară este realizată de mecanismul standard `account.asset` (Enterprise), care postează notele la scadență.

## 5. Conexiuni

- `[[l10n_ro_fixed_assets]]`
- `[[l10n_ro_financial_notes]]`
