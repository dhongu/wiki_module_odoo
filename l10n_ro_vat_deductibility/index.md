# Deductibilitate TVA România (localizat la `l10n_ro_vat_deductibility/index.md`)

- **Nume Tehnic:** `l10n_ro_vat_deductibility`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_vat_deductibility
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_vat_deductibility`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

## 1. Sumar

Acest modul gestionează explicit deductibilitatea TVA pentru România: TVA deductibil integral, deductibil parțial (inclusiv pro-rata pe intervale calendaristice) și nedeductibil. Oferă trei metode de lucru — alocare directă per factură, grup de taxe preconfigurate (ex. TVA 50% nedeductibil) și pro-rata cu calcul anual pentru firmele cu regim mixt (operațiuni taxabile + scutite), conform Art. 300 din Codul Fiscal.

## 2. Funcționalități Cheie

- **Alocare directă per factură:** procent deductibil setat pe linia de factură prin câmpul standard `deductible_amount` și modul de deductibilitate pe taxă (`l10n_ro_deductibility_mode`).
- **Grup de taxe preconfigurate:** la instalare se creează automat grupul „TVA 21% (50% Nedeductibil)" (Taxa A + Taxa B).
- **Pro-rata (calcul anual):** pentru activități mixte, cu pro-rata provizorie în cursul anului și regularizare definitivă în ultimul decont, conform Art. 300 Cod Fiscal.
- **Wizard de regularizare pro-rata** pentru ajustarea diferențelor între pro-rata provizorie și cea definitivă.
- Nu necesită modulul OCA `l10n_ro_nondeductible_vat` ca dependență.

## 3. Dependențe

- `l10n_ro_journal_tva`
- `l10n_ro_anaf_d300`
- `l10n_ro_anaf_d394`

## 4. Componente Cheie

Conform `readme/DESCRIPTION.md`:

### Modele

- `account.tax`: Extins cu `l10n_ro_deductibility_mode` (integral / parțial-pro-rata / nedeductibil).
- Model pro-rata pentru gestionarea procentelor deductibile pe intervale calendaristice.

### Vizualizări / Date

- `data/account_tax_tva_50_nedeductibil.xml`: Grupul de taxe „TVA 50% Nedeductibil".
- `views/account_tax_views.xml`: Configurarea modului de deductibilitate pe taxă.
- `views/l10n_ro_vat_prorata_views.xml`: Gestionarea pro-ratei.
- `wizard/l10n_ro_vat_prorata_regularization_views.xml`: Wizardul de regularizare pro-rata.

### Acțiuni Automate / Acțiuni Server

*Nu sunt definite acțiuni automate; regularizarea pro-rata se rulează din wizard.*

## 5. Conexiuni

- `l10n_ro_vat_regularization`
- `l10n_ro_vat_group`
- `l10n_ro_vat_refund`
