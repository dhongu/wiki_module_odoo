
# `l10n_ro_account_chart`

- **Nume Prietenesc:** Romania - Plan de Conturi Extins (FR-01)
- **Nume Tehnic:** `l10n_ro_account_chart`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_account_chart
- **Ultima Ingestie:** 2026-05-31

## 1. Sumar

Acest modul completează planul de conturi românesc (OMFP 1802/2014) cu trei funcționalități esențiale: blocarea postărilor directe pe conturile sintetice, impunerea analiticului obligatoriu per cont și blocarea inactivării conturilor cu rulaj. Toate aceste mecanisme sunt opționale, configurabile per companie din **Setări → Contabilitate**.

## 2. Funcționalități Cheie

- **Blocare postare pe conturi sintetice:** Conturile marcate ca sintetice nu permit postări directe, cu excepția conturilor de tip `asset_receivable` / `liability_payable` (ex: 401, 411, 421 etc.).
- **Analitic obligatoriu per cont:** Conturile marcate cu „Analitic obligatoriu" impun completarea `analytic_distribution` la postare.
- **Blocaj inactivare cont cu rulaj:** Un cont cu înregistrări contabile nu poate fi marcat `deprecated` sau dezactivat.

## 3. Dependențe

- `account`
- `l10n_ro`

## 4. Componente Cheie

### Modele

- `account.account`: Extinde modelul de bază al conturilor pentru a adăuga câmpuri legate de blocarea postărilor pe conturi sintetice, analitice obligatorii și blocajul inactivării conturilor cu rulaj.
- `account.move`: Extinde modelul de note contabile pentru a aplica regulile de postare bazate pe configurația conturilor.
- `res.company`: Stochează setările specifice companiei pentru activarea/dezactivarea funcționalităților modulului.
- `res.config.settings`: Oferă interfața de utilizator pentru configurarea acestor funcționalități în setările Odoo.

### Vizualizări

- `views/account_account_views.xml`: Modifică vizualizările (formular/listă) ale conturilor pentru a afișa noile câmpuri sau a impune reguli.
- `views/res_config_settings_views.xml`: Adaugă opțiuni de configurare în interfața de setări contabile.

### Acțiuni Automate / Acțiuni Server

*Nu au fost identificate explicit în `__manifest__.py` sau `readme/DESCRIPTION.md`.*

## 5. Conexiuni

- [[l10n_ro_account_fisa_cont/|l10n_ro_account_fisa_cont]]: Modulul „Fișă de Cont” din localizarea românească, care poate beneficia de funcționalitățile acestui modul.
