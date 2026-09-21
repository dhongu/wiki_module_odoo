# Romania - Mijloace fixe complete (FR-19) (localizat la `l10n_ro_fixed_assets/index.md`)

- **Nume Tehnic:** `l10n_ro_fixed_assets`
- **Versiune:** `19.0.1.3.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_fixed_assets
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_fixed_assets`
- **Ultima Ingestie:** 2026-09-19
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Extinde modulul `account_asset` (Enterprise) cu câmpurile și funcționalitățile obligatorii pentru mijloacele fixe conform legislației românești (OMFP 1802/2014, HG 2139/2004, Cod Fiscal art. 28, SAF-T D406). Acoperă gap-urile față de Odoo standard: numărul de inventar în SAF-T, data punerii în funcțiune, amortizarea fiscală vs. contabilă, reevaluarea pe contul 105, monografia corectă de casare și Registrul Imobilizărilor, disponibil ca raport nativ `account.report`.

#### 2. Funcționalități Cheie

- **Generare automată la achiziție**: un mijloc fix nu se creează manual din lista de active — flux standard **Comandă de achiziție → Recepție → Factură furnizor**, iar activul se generează automat, în ciornă, la postarea facturii, dacă linia e pe un cont de imobilizări configurat cu tab-ul **„Automatizare"** → **„Automatizează activul"** (`create_asset` = „Nu" / „Creează în stadiu de proiect" / „Creează și validează"); conturile de amortizare/cheltuială rămân de completat manual înainte de confirmare. Nota contabilă a facturii de furnizor trebuie să folosească **404 „Furnizori de imobilizări"** ca și contrapartidă, nu 401 „Furnizori" (rezervat aprovizionărilor din exploatare) — pentru asta, furnizorul de mijloace fixe trebuie să aibă setat pe fișa de partener contul de plată „Furnizori de imobilizări" (`property_account_payable_id`), altfel Odoo folosește implicit 401.
- **Nr. Inventar** (`l10n_ro_inventory_number`): generabil automat din secvența `MF/AAAA/NNNN`; suprascrie `<AssetID>` în SAF-T D406 cu identificatorul din registrul imobilizărilor fizic.
- **Data PIF** (`l10n_ro_date_in_service`): data punerii în funcțiune, distinctă de data achiziției; override `<StartUpDate>` în SAF-T; amortizarea contabilă și fiscală pornesc din **prima zi a lunii următoare** PIF, nu din PIF însuși (fix de conformitate cu art. 28 alin. (12) lit. a) Legea 227/2015 și OMFP 1802/2014 pct. 238 — vezi secțiunea 12 din fișa consultant). Sistemul blochează salvarea dacă data PIF e anterioară datei de achiziție.
- **Responsabil Custodie** și **Locație**: câmpuri pentru registrul imobilizărilor; **DNU Catalog HG 2139/2004** informativ.
- **Amortizare fiscală vs. contabilă**: urmărire separată conform Cod Fiscal art. 28, calcul automat fără note contabile, exclusiv pentru reconcilierea Declarației 101; cumulatul și amortizarea anului curent folosesc acum aceeași convenție de start (luna următoare PIF), corectând o incoerență în care cumulatul putea ieși mai mic decât amortizarea anului curent pentru un activ pus în funcțiune în anul curent. Baza de amortizare fiscală (`l10n_ro_fiscal_original_value`) este acum un `compute` = `max(l10n_ro_acquisition_value, original_value)` (fix 19.0.1.3.4) — urmărește CREȘTERILE din reevaluare (L227/2015 art. 7 pct. 44 lit. c): surplusul intră în valoarea fiscală și se amortizează, cu impozitarea concomitentă a rezervei 105, art. 26 alin. (6)), dar nu coboară sub costul istoric de achiziție (`l10n_ro_acquisition_value`, înghețat la creare) la o diminuare. Versiunea anterioară (19.0.1.2.2-19.0.1.3.3) îngheța complet baza la costul de intrare, subestimând amortizarea fiscală deductibilă după o reevaluare în creștere — confirmat greșit printr-un audit `pacioli`.
- **Rezerva 105 afișată pe activ** (`l10n_ro_revaluation_reserve`) se calculează acum din soldul REAL al liniilor contului 105 din notele de reevaluare postate (fix 19.0.1.3.4), nu din suma algebrică a tuturor reevaluărilor — anterior putea arăta o valoare falsă (ex. -2.000 deși 105 nu fusese atins deloc, dacă o diminuare depășise soldul și mersese integral pe 655) și permitea unei a doua diminuări succesive să consume din 105 mai mult decât soldul real rămas. O creștere care compensează o diminuare anterioară recunoscută pe 655 trece acum întâi prin cont nou **755** „Venituri din reevaluare" (OMFP 1802/2014 pct. 111 alin. (1), liniuța a doua), abia restul intrând în 105.
- **Vânzare/casare fără prorata pe luna cedării**: la vânzarea sau casarea unui activ în cursul lunii, luna cedării nu se mai amortizează proporțional cu zilele scurse — ultima lună amortizată este cea anterioară vânzării, simetric cu regula de start.
- **Blocare legare manuală a câmpului tehnic „Asset"**: o notă contabilă (ex. de reevaluare) nu mai poate fi legată manual la activ fără data de început a amortizării completată; anterior acest lucru bloca ulterior orice calcul de valoare reziduală (inclusiv din wizard-ul „Modifică") cu `TypeError`.
- **Reevaluare la valoare justă**: model dedicat `l10n.ro.asset.revaluation` cu wizard, accesibil din butonul „Reevaluare" al formularului activului; generează automat nota Dr 21x = Cr 105 (surplus) sau Dr 105/655 (depreciere — cont 655 „Cheltuieli din reevaluarea imobilizărilor", OMFP 1802/2014 pct. 111 alin. (3); corectat în 19.0.1.3.2, anterior folosea greșit 6813, un cont de ajustări pentru depreciere/provizioane); recalculează corect planul de amortizare de la data reevaluării încolo, pentru surplus și pentru depreciere deopotrivă (fix 19.0.1.3.1 — `action_post()` apela direct `_recompute_board()`, care doar calculează noile valori fără să șteargă liniile draft vechi și fără să creeze cele noi, astfel încât amortizarea viitoare continua tăcut la suma dinaintea reevaluării; acum apelează `compute_depreciation_board(date=...)`, care regenerează efectiv planul). Recalculul pornește din prima zi a lunii **următoare** reevaluării (fix 19.0.1.3.2 — anterior pornea din data exactă a reevaluării, ceea ce genera o notă suplimentară pro-rata pe zile pentru restul lunii, pe lângă cea deja calculată la vechea valoare, dublând amortizarea acelei luni; amortizarea RO e strict lunară, OMFP 1802/2014 pct. 238). Câmpurile de cont (`account_reserve_id`/`account_expense_id`, fostele `account_105_id`/`account_6813_id`) nu mai includ codul de cont în numele tehnic.
- **Casare cu monografie RO corectă**: override `set_to_close()` generează Dr 281x = Cr 21x și Dr 6583 = Cr 21x (valoare reziduală); transfer automat 105 → 1175 dacă există rezervă din reevaluare.
- **Vânzare mijloc fix — fără compensare venit/cheltuială** (fix 19.0.1.3.3): nota de cedare înregistrează întreaga valoare neamortizată pe 6583 (`loss_account_id`), independent de prețul de vânzare — identic cu monografia de la casare fără vânzare. Anterior, motorul standard relua linia de venit din factură (Dr 7583, ca stornare) și înregistra doar diferența netă pe 6583/7583 — o compensare venituri/cheltuieli interzisă de OMFP 1802/2014 pct. 56 alin. (1), care subevalua rulajele celor două conturi cu exact valoarea vânzării (rezultatul net total ieșea totuși corect). Contrapartida creanței la vânzare este de regulă **461** „Debitori diverși" (funcțiunea contului, Cap. 16), nu 411/4111 (fix 19.0.1.3.4 — exemplul din fișă folosea greșit 4111). Confirmat printr-o consultare explicită `pacioli` (tichet 9452).
- **Decizie de Casare PDF**: raport QWeb cu comisie, motiv, valori inventar/amortizare/reziduală.
- **Registrul Imobilizărilor**: raport nativ `account.report` (Enterprise), accesibil din **Contabilitate → Raportare → Statement Reports → Fixed Assets Register (RO)** — filtru **„As of Date"** (situație la o dată aleasă, implicit ziua curentă), grupare pe cont de imobilizări cu subtotaluri și total general, drill-down pe fiecare activ (click pe linie deschide fișa) și export PDF/XLSX din bara de instrumente a raportului. Amortizarea cumulată se calculează exclusiv din notele de amortizare postate până la data de referință, ca o fotografie fidelă la acea dată — nu valoarea contabilă curentă. Migrat de la vechiul wizard + raport QWeb PDF în versiunea 19.0.1.3.0 (2026-09-15); wizard-ul (`l10n.ro.asset.register.wizard`) și raportul QWeb au fost eliminate.
- **Pre-validator SAF-T D406**: raportează erori la active fără număr de inventar sau fără dată PIF, cu link direct la lista activelor afectate.

#### 3. Dependențe

- `account_asset`
- `account_reports`
- `l10n_ro_saft`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.asset`: extins cu câmpurile RO (nr. inventar, dată PIF, custodie, locație, DNU, amortizare fiscală, `l10n_ro_fiscal_original_value` înghețat la creare) și override-uri SAF-T, `set_to_close()`, `prorata_date` (start amortizare din luna următoare PIF) și calculul amortizării fiscale cumulate/an curent pe baza valorii fiscale de intrare (nu a valorii curente, care poate include un surplus de reevaluare).
- `l10n.ro.asset.revaluation`: modelul de reevaluare a mijloacelor fixe (conturi 105/655), cu monografie completă; `action_post()` recalculează planul de amortizare apelând `asset.compute_depreciation_board(date=...)`, cu data mutată la prima zi a lunii următoare reevaluării pentru companiile cu amortizare lunară (fix 19.0.1.3.1/19.0.1.3.2 — anterior apela `_recompute_board()`, care nu regenera efectiv liniile, iar apoi `compute_depreciation_board(date=self.date)` genera un split pro-rata pe zile pentru luna reevaluării).
- `l10n.ro.asset.register.report.handler`: handler `account.report.custom.handler` pentru Registrul Imobilizărilor — grupare pe două niveluri (`asset_account` → `asset_line`), motor `_report_custom_engine_asset_register` pe `account.asset` (nu pe `account.move.line`), drill-down (caret option „Fixed Asset") și etichetare a activelor după nr. de inventar. Înlocuiește vechiul wizard `l10n.ro.asset.register.wizard`, eliminat în 19.0.1.3.0.
- `account.general.ledger.report.handler` (extindere): completează valorile SAF-T D406 (`asset_inventory_number`, `l10n_ro_date_in_service`, custodie, locație) și pre-validează activele fără număr de inventar sau dată PIF.
- `account.move` (extindere): `_get_asset_depreciation_line()` exclude contul de amortizare cumulată (281x) din latura de cheltuială pentru companiile RO, ca nota de amortizare Dr 6811 / Cr 281x să nu se anuleze reciproc; adaugă o constrângere care respinge legarea manuală a câmpului tehnic „Asset" fără `asset_depreciation_beginning_date` completat.

**Vizualizări**

- `views/account_asset_views.xml`: câmpurile RO pe mijlocul fix.
- `views/l10n_ro_asset_revaluation_views.xml`, `wizard/asset_revaluation_wizard_views.xml`: reevaluarea și wizardul aferent.
- `report/report_asset_register.xml`: definiția raportului nativ `account.report` „Fixed Assets Register" — coloane (nr. inventar, dată achiziție, document, clasă, valoare de intrare, durată, îmbunătățiri, valoare inventar, valoare netă, durată rămasă, amortizare lunară/cumulată, dată casare), acțiunea de client `account_report` și intrarea de meniu sub **Statement Reports**.
- `report/report_asset_disposal.xml`: raportul QWeb al Deciziei de Casare.
- `report/saft_assets_ro_inherit.xml`: override-urile SAF-T D406 pentru `<AssetID>` și `<StartUpDate>`.
- `data/ir_sequence_data.xml`: secvența numerelor de inventar.

**Acțiuni Automate / Acțiuni Server**

- Acțiunea de server „Revalue Fixed Asset" din meniul contextual al listei `account.asset` apelează `action_l10n_ro_revalue()` pentru deschiderea wizardului de reevaluare (`report/report_actions.xml`). Corectată în 19.0.1.1.1 — anterior apela o metodă inexistentă pe wizard și genera `AttributeError`.
- Amortizarea contabilă este gestionată de mecanismul standard `account_asset`; amortizarea fiscală este doar calculată (fără note contabile).

#### 5. Conexiuni

- [l10n_ro_inventory_items](../l10n_ro_inventory_items/index.md): gestiunea fizică a obiectelor de inventar, complementară registrului de mijloace fixe.
- [l10n_ro_financial_notes](../l10n_ro_financial_notes/index.md): notele contabile RO în care se reflectă amortizarea, reevaluarea și casarea mijloacelor fixe.
- [l10n_ro_deferred_entries](../l10n_ro_deferred_entries/index.md): mecanism de note contabile eșalonate, folosit în ecosistemul de contabilitate RO alături de amortizare.
