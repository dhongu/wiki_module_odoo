# Romania - Mijloace fixe complete (localizat la `l10n_ro_fixed_assets/index.md`)

- **Nume Tehnic:** `l10n_ro_fixed_assets`
- **Versiune:** `20.0.1.17.6`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_fixed_assets
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_fixed_assets`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Extinde modulul Enterprise `account_asset` cu evidența mijloacelor fixe cerută de legislația românească: OMFP 1802/2014, Codul fiscal art. 28, HG 2139/2004, OMFP 2634/2015 și SAF-T D406. Se adresează companiilor din România care țin registrul imobilizărilor în Odoo, calculează amortizarea fiscală separat de cea contabilă și declară activele în D406.

#### 2. Funcționalități Cheie

- **Evidența activului**: număr de inventar (`MF/AAAA/NNNN`, apare ca `<AssetID>` în D406), data punerii în funcțiune distinctă de data achiziției (`<StartUpDate>`; amortizarea lunară începe din prima zi a lunii următoare PIF), catalogul HG 2139/2004 (categoria propune durata normală, codul de clasă și durata fiscală), gestiune și responsabil cu schimbări prin transferuri datate (bon de mișcare).
- **Intrări și preluare**: punere în funcțiune din 231 / 235 printr-un wizard (`Dr 21x = Cr 231`) și import al registrului de imobilizări dintr-un fișier, cu verificare înainte de import, corespondența conturilor, gestiuni create din fișier, amortizare cumulată preluată fără note în balanță și totaluri pe cont pentru comparația cu balanța de deschidere.
- **Amortizare contabilă** cu note pe 281x / 280x; pauza și reluarea lucrează pe luni întregi. În Odoo 20, metoda, durata și jurnalul vin din modelul de amortizare (metoda „Conform planului fiscal (RO)" se alege pe model), iar contul 281x se setează pe contul de imobilizări; durata în luni rămâne pe activ.
- **Plan fiscal lunar**, separat de cel contabil și fără note contabile: liniar, degresiv, accelerat și superaccelerat (2026), plafonul pentru autoturismele M1 și perioadele de conservare; servește la reconcilierea declarației 101.
- **Luna ieșirii**: implicit nu se amortizează; setarea pe companie „Depreciate the Exit Month" o amortizează integral, contabil și fiscal.
- **Reevaluare** prin metoda netă (OMFP 1802/2014 pct. 103 lit. b): `Dr 281x = Cr 21x`, apoi diferența până la valoarea justă pe 105 / 655 / 755; planul se recalculează pe valoarea reevaluată. Din „Modifică" se alege între reevaluare și modernizare (majorare de valoare cu contrapartida 404 / 231).
- **Ieșiri**: casare și cedare (`Dr 281x = Cr 21x`, valoarea neamortizată pe 6583, transferul rezervei 105 → 1175) și vânzare (factură cu liniile pe 7583, creanța trece pe 461 fără a schimba contul de client al partenerului).
- **Documente și rapoarte**: Bon de mișcare, Fișa mijlocului fix, PV de recepție, PV de scoatere din funcțiune, Registrul numerelor de inventar (OMFP 2634/2015) și Decizia de casare; Registrul imobilizărilor ca raport `account.report` la o dată aleasă, cu drill-down pe activ și export PDF / XLSX; pre-validator D406 pentru activele fără număr de inventar sau dată PIF.
- Fluxul pas-cu-pas este în fișa consultant.

#### 3. Dependențe

- `account_asset`
- `account_reports`
- `l10n_ro_saft`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.asset` (extins): câmpurile RO (număr de inventar, dată PIF, gestiune, amortizare fiscală) și override-uri pentru SAF-T și regulile RO de amortizare.
- `account.asset.variant` și `account.depreciation.model` (extinse): în Enterprise 20 starea, planul și notele de amortizare sunt ale variantei principale; regulile RO lucrează pe variantă, iar metoda fiscală se alege pe modelul de amortizare.
- `account.move` / `account.move.line` (extinse): note de amortizare corecte pentru companiile RO și legarea activelor de facturi.
- `asset.modify` (extins): alegerea între reevaluare și modernizare din „Modifică".
- `l10n.ro.asset.fiscal.line` și `l10n.ro.asset.conservation`: planul fiscal lunar și perioadele de conservare.
- `l10n.ro.asset.location` și `l10n.ro.asset.transfer` (cu `l10n.ro.asset.transfer.batch`): gestiuni și transferuri datate (bon de mișcare), individual și în lot.
- `l10n.ro.asset.revaluation` (cu `l10n.ro.asset.revaluation.batch` / `.line` și wizardul `l10n.ro.asset.revaluation.wizard`): reevaluarea mijloacelor fixe, individual și în lot.
- `l10n.ro.asset.closing` (cu `.check` și `.reconciliation`): închiderea lunară a mijloacelor fixe, cu verificări și reconciliere.
- `l10n.ro.asset.commissioning.wizard`: punerea în funcțiune din 231 / 235.
- `l10n.ro.asset.import.saga` (cu linii și mapări de conturi): importul registrului de imobilizări.
- `l10n.ro.asset.inventory.list`: wizard pentru documentele și listele de inventar.
- `account.general.ledger.report.handler` (extins): completează valorile SAF-T D406 și pre-validează activele.
- `res.company` / `res.config.settings` (extinse): setările RO ale mijloacelor fixe (ex. „Depreciate the Exit Month").
- Registrul imobilizărilor: handler `account.report.custom.handler` (`report/asset_register.py`) pe `account.asset`, cu drill-down pe activ.

**Vizualizări**

- `view_account_asset_form_ro_inherit` / `view_account_asset_list_ro_inherit`: câmpurile RO pe mijlocul fix.
- `view_account_depreciation_model_form_ro_inherit`: opțiunile RO pe modelul de amortizare.
- `action_l10n_ro_asset_grid` (`account_asset_grid_views.xml`): grila mijloacelor fixe.
- `view_l10n_ro_asset_closing_form` / `action_l10n_ro_asset_closing`: închiderea lunară.
- `view_l10n_ro_asset_revaluation_form`, `view_l10n_ro_asset_revaluation_wizard_form`: reevaluarea.
- `action_l10n_ro_asset_transfer`, `action_l10n_ro_asset_location`, `action_l10n_ro_asset_transfer_batch`: transferuri și gestiuni.
- `view_l10n_ro_asset_commissioning_wizard_form`, `view_l10n_ro_asset_import_saga_form`, `view_l10n_ro_asset_inventory_list_form`: wizardurile de punere în funcțiune, import și liste de inventar.
- `asset_modify_form_l10n_ro` și `res_config_settings_view_form_l10n_ro_fixed_assets`: „Modifică" și setările.
- `report/report_asset_register.xml`, `report_asset_documents.xml`, `report_asset_closing.xml`, `report_asset_inventory_list.xml`, `report_asset_disposal.xml`: registrul imobilizărilor și documentele PDF; `saft_assets_ro_inherit.xml`: `<AssetID>` și `<StartUpDate>` în D406.
- `data/ir_sequence_data.xml`: secvența numerelor de inventar. Drepturile de acces sunt în `security/ir.access.csv`.

**Acțiuni Automate / Acțiuni Server**

- Acțiunea de server „Revalue Fixed Asset" (`report/report_actions.xml`), în meniul contextual al `account.asset`, deschide wizardul de reevaluare.
- Nu sunt definite `ir.cron`; amortizarea contabilă este cea standard din `account_asset`, iar cea fiscală este doar calculată.

#### 5. Conexiuni

- [l10n_ro_inventory_items](../l10n_ro_inventory_items/index.md): gestiunea fizică a obiectelor de inventar, complementară registrului de mijloace fixe.
- [l10n_ro_financial_notes](../l10n_ro_financial_notes/index.md): notele contabile RO în care se reflectă amortizarea, reevaluarea și casarea mijloacelor fixe.
- [l10n_ro_deferred_entries](../l10n_ro_deferred_entries/index.md): mecanism de note contabile eșalonate, folosit în ecosistemul de contabilitate RO alături de amortizare.
