# Romania - Mijloace Fixe Complete (FR-19) (localizat la `l10n_ro_fixed_assets/index.md`)

- **Nume Tehnic:** `l10n_ro_fixed_assets`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_fixed_assets
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_fixed_assets`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

## 1. Sumar

Extinde modulul `account_asset` (Enterprise) cu câmpurile și funcționalitățile obligatorii pentru mijloacele fixe conform legislației românești (OMFP 1802/2014, HG 2139/2004, Cod Fiscal art. 28, SAF-T D406). Acoperă gap-urile față de Odoo standard: numărul de inventar în SAF-T, data punerii în funcțiune, amortizarea fiscală vs. contabilă, reevaluarea pe contul 105, monografia corectă de casare și rapoartele PDF aferente.

## 2. Funcționalități Cheie

- **Câmpuri suplimentare pe mijlocul fix:** Nr. Inventar (`l10n_ro_inventory_number`, secvență `MF/AAAA/NNNN`, override `<AssetID>` în SAF-T), Data PIF (`l10n_ro_date_in_service`, override `<StartUpDate>`), responsabil custodie, locație, DNU catalog HG 2139/2004.
- **Amortizare fiscală vs. contabilă:** câmpuri separate (`l10n_ro_fiscal_method`, `l10n_ro_fiscal_method_number`), fără generare `account.move`, pentru reconcilierea Declarației 101.
- **Reevaluare mijloace fixe (cont 105):** model `l10n.ro.asset.revaluation` (OMFP 1802 pct. 97–106) cu surplus (Dr 21x = Cr 105), depreciere fără/ cu sold 105 și recalcularea planului de amortizare.
- **Casare cu monografie RO corectă:** transfer `Dr 105 = Cr 1175` la casarea unui activ cu sold 105.
- **Rapoarte PDF:** Decizie de Casare și Registrul Imobilizărilor.
- **Pre-validator SAF-T D406:** raportează active fără număr de inventar sau fără dată PIF.

## 3. Dependențe

- `account_asset`
- `l10n_ro_saft`
- `l10n_ro`

## 4. Componente Cheie

### Modele

- `account.asset`: extins cu câmpurile RO (nr. inventar, dată PIF, custodie, locație, DNU, amortizare fiscală) și override-uri SAF-T și `set_to_close()`.
- `l10n.ro.asset.revaluation`: modelul de reevaluare a mijloacelor fixe (cont 105) cu monografie completă și recalcularea planului de amortizare.

### Vizualizări / Date

- `views/account_asset_views.xml`: câmpurile RO pe mijlocul fix.
- `views/l10n_ro_asset_revaluation_views.xml`, `wizard/asset_revaluation_wizard_views.xml`: reevaluarea și wizardul aferent.
- `report/report_asset_disposal.xml`, `report/report_asset_register.xml`: Decizia de Casare și Registrul Imobilizărilor.
- `report/saft_assets_ro_inherit.xml`: override-urile SAF-T D406 pentru `<AssetID>` și `<StartUpDate>`.
- `data/ir_sequence_data.xml`: secvența numerelor de inventar.

### Acțiuni Automate / Acțiuni Server

*Amortizarea contabilă este gestionată de mecanismul standard `account_asset`; amortizarea fiscală este doar calculată (fără note contabile).*

## 5. Conexiuni

- `[[l10n_ro_inventory_items]]`
- `[[l10n_ro_financial_notes]]`
- `[[l10n_ro_deferred_entries]]`
