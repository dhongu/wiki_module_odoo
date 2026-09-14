# Romania - Mijloace fixe complete (FR-19) (localizat la `l10n_ro_fixed_assets/index.md`)

- **Nume Tehnic:** `l10n_ro_fixed_assets`
- **Versiune:** `19.0.1.2.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_fixed_assets
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_fixed_assets`
- **Ultima Ingestie:** 2026-09-14
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Extinde modulul `account_asset` (Enterprise) cu câmpurile și funcționalitățile obligatorii pentru mijloacele fixe conform legislației românești (OMFP 1802/2014, HG 2139/2004, Cod Fiscal art. 28, SAF-T D406). Acoperă gap-urile față de Odoo standard: numărul de inventar în SAF-T, data punerii în funcțiune, amortizarea fiscală vs. contabilă, reevaluarea pe contul 105, monografia corectă de casare și rapoartele PDF aferente.

#### 2. Funcționalități Cheie

- **Nr. Inventar** (`l10n_ro_inventory_number`): generabil automat din secvența `MF/AAAA/NNNN`; suprascrie `<AssetID>` în SAF-T D406 cu identificatorul din registrul imobilizărilor fizic.
- **Data PIF** (`l10n_ro_date_in_service`): data punerii în funcțiune, distinctă de data achiziției; override `<StartUpDate>` în SAF-T; amortizarea contabilă și fiscală pornesc din **prima zi a lunii următoare** PIF, nu din PIF însuși (fix de conformitate cu art. 28 alin. (12) lit. a) Legea 227/2015 și OMFP 1802/2014 pct. 238 — vezi secțiunea 12 din fișa consultant).
- **Responsabil Custodie** și **Locație**: câmpuri pentru registrul imobilizărilor; **DNU Catalog HG 2139/2004** informativ.
- **Amortizare fiscală vs. contabilă**: urmărire separată conform Cod Fiscal art. 28, calcul automat fără note contabile, exclusiv pentru reconcilierea Declarației 101; cumulatul și amortizarea anului curent folosesc acum aceeași convenție de start (luna următoare PIF), corectând o incoerență în care cumulatul putea ieși mai mic decât amortizarea anului curent pentru un activ pus în funcțiune în anul curent. Baza de amortizare fiscală este acum câmpul nou `l10n_ro_fiscal_original_value`, înghețat la valoarea de intrare din momentul creării activului — un surplus dintr-o reevaluare ulterioară (care majorează `original_value`, dar nu e deductibil fiscal conform Cod Fiscal art. 28) nu mai umflă cifra de amortizare fiscală afișată.
- **Vânzare/casare fără prorata pe luna cedării**: la vânzarea sau casarea unui activ în cursul lunii, luna cedării nu se mai amortizează proporțional cu zilele scurse — ultima lună amortizată este cea anterioară vânzării, simetric cu regula de start.
- **Blocare legare manuală a câmpului tehnic „Asset"**: o notă contabilă (ex. de reevaluare) nu mai poate fi legată manual la activ fără data de început a amortizării completată; anterior acest lucru bloca ulterior orice calcul de valoare reziduală (inclusiv din wizard-ul „Modifică") cu `TypeError`.
- **Reevaluare la valoare justă**: model dedicat `l10n.ro.asset.revaluation` cu wizard; generează automat nota Dr 21x = Cr 105 (surplus) sau Dr 105/6813 = Cr 21x (depreciere); recalculează planul de amortizare după reevaluare.
- **Casare cu monografie RO corectă**: override `set_to_close()` generează Dr 281x = Cr 21x și Dr 6583 = Cr 21x (valoare reziduală); transfer automat 105 → 1175 dacă există rezervă din reevaluare.
- **Vânzare mijloc fix**: diferența dintre valoarea neamortizată și prețul de vânzare se închide pe 7583 (`gain_account_id`, câștig) sau 6583 (`loss_account_id`, pierdere); necesită **Contare Storno** (`account_storno`) activat pe compania RO pentru a evita un rulaj suplimentar pe contul de venit.
- **Decizie de Casare PDF**: raport QWeb cu comisie, motiv, valori inventar/amortizare/reziduală.
- **Registrul Imobilizărilor PDF**: raport tabelar cu toate activele.
- **Pre-validator SAF-T D406**: raportează erori la active fără număr de inventar sau fără dată PIF.

#### 3. Dependențe

- `account_asset`
- `l10n_ro_saft`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.asset`: extins cu câmpurile RO (nr. inventar, dată PIF, custodie, locație, DNU, amortizare fiscală, `l10n_ro_fiscal_original_value` înghețat la creare) și override-uri SAF-T, `set_to_close()`, `prorata_date` (start amortizare din luna următoare PIF) și calculul amortizării fiscale cumulate/an curent pe baza valorii fiscale de intrare (nu a valorii curente, care poate include un surplus de reevaluare).
- `l10n.ro.asset.revaluation`: modelul de reevaluare a mijloacelor fixe (cont 105), cu monografie completă și recalcularea planului de amortizare.
- `account.general.ledger.report.handler` (extindere): completează valorile SAF-T D406 (`asset_inventory_number`, `l10n_ro_date_in_service`, custodie, locație) și pre-validează activele fără număr de inventar sau dată PIF.
- `account.move` (extindere): `_get_asset_depreciation_line()` exclude contul de amortizare cumulată (281x) din latura de cheltuială pentru companiile RO, ca nota de amortizare Dr 6811 / Cr 281x să nu se anuleze reciproc; adaugă o constrângere care respinge legarea manuală a câmpului tehnic „Asset" fără `asset_depreciation_beginning_date` completat.

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
