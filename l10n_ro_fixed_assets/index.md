# Romania - Mijloace Fixe Complete (FR-19) (localizat la `l10n_ro_fixed_assets/index.md`)

- **Nume Tehnic:** `l10n_ro_fixed_assets`
- **Versiune:** `19.0.1.1.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_fixed_assets
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_fixed_assets`
- **Ultima Ingestie:** 2026-08-20
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Extinde modulul `account_asset` (Enterprise) cu câmpurile și funcționalitățile obligatorii pentru mijloacele fixe conform legislației românești (OMFP 1802/2014, HG 2139/2004, Cod Fiscal art. 28, SAF-T D406). Acoperă gap-urile față de Odoo standard: numărul de inventar în SAF-T, data punerii în funcțiune, amortizarea fiscală vs. contabilă, reevaluarea pe contul 105, monografia corectă de casare și rapoartele PDF aferente.

#### 2. Funcționalități Cheie

- **Nr. Inventar** (`l10n_ro_inventory_number`): generabil automat din secvența `MF/AAAA/NNNN`; suprascrie `<AssetID>` în SAF-T D406 cu identificatorul din registrul imobilizărilor fizic.
- **Data PIF** (`l10n_ro_date_in_service`): data punerii în funcțiune, distinctă de data achiziției; override `<StartUpDate>` în SAF-T; amortizarea începe la data PIF.
- **Responsabil Custodie** și **Locație**: câmpuri pentru registrul imobilizărilor; **DNU Catalog HG 2139/2004** informativ.
- **Amortizare fiscală vs. contabilă**: urmărire separată conform Cod Fiscal art. 28, calcul automat fără note contabile, exclusiv pentru reconcilierea Declarației 101.
- **Reevaluare la valoare justă**: model dedicat `l10n.ro.asset.revaluation` cu wizard; generează automat nota Dr 21x = Cr 105 (surplus) sau Dr 105/6813 = Cr 21x (depreciere); recalculează planul de amortizare după reevaluare.
- **Casare cu monografie RO corectă**: override `set_to_close()` generează Dr 281x = Cr 21x și Dr 6583 = Cr 21x (valoare reziduală); transfer automat 105 → 1175 dacă există rezervă din reevaluare.
- **Decizie de Casare PDF**: raport QWeb cu comisie, motiv, valori inventar/amortizare/reziduală.
- **Registrul Imobilizărilor PDF**: raport tabelar cu toate activele.
- **Pre-validator SAF-T D406**: raportează erori la active fără număr de inventar sau fără dată PIF.

#### 3. Dependențe

- `account_asset`
- [l10n_ro_saft](../l10n_ro_saft/index.md)
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.asset`: extins cu câmpurile RO (nr. inventar, dată PIF, custodie, locație, DNU, amortizare fiscală) și override-uri SAF-T și `set_to_close()`.
- `l10n.ro.asset.revaluation`: modelul de reevaluare a mijloacelor fixe (cont 105), cu monografie completă și recalcularea planului de amortizare.
- `account.general.ledger.report.handler` (extindere): completează valorile SAF-T D406 (`asset_inventory_number`, `l10n_ro_date_in_service`, custodie, locație) și pre-validează activele fără număr de inventar sau dată PIF.
- `account.move` (extindere): `_get_asset_depreciation_line()` exclude contul de amortizare cumulată (281x) din latura de cheltuială pentru companiile RO, ca nota de amortizare Dr 6811 / Cr 281x să nu se anuleze reciproc.

**Vizualizări**

- `views/account_asset_views.xml`: câmpurile RO pe mijlocul fix.
- `views/l10n_ro_asset_revaluation_views.xml`, `wizard/asset_revaluation_wizard_views.xml`: reevaluarea și wizardul aferent.
- `wizard/asset_register_wizard_views.xml`: wizardul de generare a registrului imobilizărilor.
- `report/report_asset_disposal.xml`, `report/report_asset_register.xml`: Decizia de Casare și Registrul Imobilizărilor.
- `report/saft_assets_ro_inherit.xml`: override-urile SAF-T D406 pentru `<AssetID>` și `<StartUpDate>`.
- `data/ir_sequence_data.xml`: secvența numerelor de inventar.

**Acțiuni Automate / Acțiuni Server**

- Acțiunea de server „Revalue Fixed Asset" din meniul contextual al listei `account.asset` apelează `action_l10n_ro_revalue()` pentru deschiderea wizardului de reevaluare (`report/report_actions.xml`). Corectată în 19.0.1.1.1 — anterior apela o metodă inexistentă pe wizard și genera `AttributeError`.
- Amortizarea contabilă este gestionată de mecanismul standard `account_asset`; amortizarea fiscală este doar calculată (fără note contabile).

#### 5. Conexiuni

- [l10n_ro_inventory_items](../l10n_ro_inventory_items/index.md): gestiunea fizică a obiectelor de inventar, complementară registrului de mijloace fixe.
- [l10n_ro_financial_notes](../l10n_ro_financial_notes/index.md): notele contabile RO în care se reflectă amortizarea, reevaluarea și casarea mijloacelor fixe.
- [l10n_ro_deferred_entries](../l10n_ro_deferred_entries/index.md): mecanism de note contabile eșalonate, folosit în ecosistemul de contabilitate RO alături de amortizare.
