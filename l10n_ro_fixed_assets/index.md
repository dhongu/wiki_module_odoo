# Romania - Mijloace fixe complete (FR-19) (localizat la `l10n_ro_fixed_assets/index.md`)

- **Nume Tehnic:** `l10n_ro_fixed_assets`
- **Versiune:** `19.0.1.9.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_fixed_assets
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_fixed_assets`
- **Ultima Ingestie:** 2026-10-04
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Extinde modulul `account_asset` (Enterprise) cu tot ce cere legislația românească pentru mijloacele fixe (OMFP 1802/2014, OMFP 2634/2015, HG 2139/2004, Codul fiscal art. 28, SAF-T D406): număr de inventar, dată de punere în funcțiune, gestiuni și transferuri, reevaluare la valoare justă, plan de amortizare fiscală separat de cel contabil, casare și vânzare cu monografie corectă, documente tipizate și Registrul imobilizărilor. Include și preluarea registrului de imobilizări din programul anterior, pentru companiile care trec pe Odoo în cursul exercițiului.

#### 2. Funcționalități Cheie

- **Identificare și SAF-T D406**: număr de inventar (`l10n_ro_inventory_number`, secvența `MF/AAAA/NNNN`) și data punerii în funcțiune (`l10n_ro_date_in_service`) înlocuiesc `<AssetID>` și `<StartUpDate>` din D406 (inclusiv în AssetTransactions); pre-validatorul semnalează activele fără număr sau fără dată, cu link către lista lor. Data PIF nu poate fi anterioară datei de achiziție.
- **Început de amortizare**: contabil și fiscal, din prima zi a lunii următoare punerii în funcțiune; pauza și reluarea lucrează pe luni întregi. Opțiunea „Depreciate the Exit Month" de pe companie decide dacă luna vânzării/casării se amortizează integral (implicit nu).
- **Creare din factură sau din 231**: la postarea facturii de furnizor pe un cont de imobilizări cu „Automatizează activul", activul se creează în ciornă (contrapartidă recomandată 404). Wizardul „Commissioning from 231" face `Dr 21x = Cr 231` din costurile de investiție alese și creează activul în ciornă; costurile puse în funcțiune nu mai pot fi alese a doua oară.
- **Catalog HG 2139/2004**: categoria SAF-T propune durata minimă, codul de clasă și durata fiscală, iar contul 21x/20x propune contul de amortizare 281x/280x.
- **Gestiuni și transferuri**: gestiunea este nomenclator (`l10n.ro.asset.location`); la confirmare se creează transferul inițial, iar la activele în funcțiune gestiunea și responsabilul se schimbă doar prin transfer datat (secvența `BM/AAAA/`, se anulează doar ultimul). Registrul arată gestiunea de la data raportului.
- **Amortizare fiscală**: plan lunar separat (`l10n.ro.asset.fiscal.line`), fără note contabile, regenerat la confirmare, reevaluare, modernizare, conservare și ieșire; servește la reconcilierea Declarației 101. Regimuri: liniar, degresiv (coeficienți 1,5/2,0/2,5), accelerat (max. 50 % în primul an) și superaccelerat 2026 (max. 65 %), cu restricții pe clase și tipuri de imobilizări necorporale. Baza fiscală = costul istoric plus diferențele din reevaluările confirmate, cu costul ca minim. Include regula pentru autoturisme M1 (limita de 1.500 lei lunar și plafonul la ieșire) și conservarea (perioade cu amortizare fiscală zero, fără scăderea duratei).
- **Reevaluare la valoare justă (metoda netă)**: wizard din butonul „Reevaluare" (și din „Modifică", unde se alege Reevaluare sau Modernizare). Nota elimină întâi amortizarea cumulată (`Dr 281x = Cr 21x`), apoi diferența merge pe 105 (surplus), 655 (diminuare peste rezervă) sau 755 (creștere care compensează o diminuare anterioară); brutul devine valoarea justă. Nota e datată la sfârșitul lunii, cu avertisment dacă nu e sfârșit de exercițiu; planul se recalculează din luna următoare. Se pot reevalua și activele complet amortizate; activele cu modernizări separate sunt refuzate deocamdată.
- **Casare și vânzare**: casarea generează `Dr 281x = Cr 21x` și `Dr 6583` pentru valoarea reziduală, plus transfer 105 → 1175 dacă există rezervă. La vânzare, valoarea neamortizată merge integral pe 6583, fără compensare cu venitul din factură; creanța trece pe 461 „Debitori diverși" (facturile cu toate liniile pe 7583), iar contul de client al partenerului rămâne neschimbat.
- **Documente tipizate OMFP 2634/2015**: Bon de mișcare, Fișa mijlocului fix, PV de recepție (cu număr `PVR/AAAA/`), PV de scoatere din funcțiune (`PVS/AAAA/`), Registrul numerelor de inventar, plus Decizia de casare (PDF cu comisie, motiv și valori).
- **Registrul imobilizărilor**: raport nativ `account.report`, în **Contabilitate → Raportare → Statement Reports → Fixed Assets Register (RO)**; filtru „As of Date", grupare pe cont cu subtotaluri, drill-down pe activ, export PDF/XLSX. Amortizarea cumulată vine din notele postate până la data de referință.
- **Preluarea registrului existent**: meniul „Import from SAGA" (Contabilitate → Configurare → Mijloace fixe) importă fișierul Excel „Registrul imobilizărilor" / „Lista imobilizărilor", în pașii Verifică → Importă (corespondența conturilor, gestiuni create din fișier, avertizări pe rând, totaluri pe cont pentru comparația cu balanța). Importul nu face note în balanță: activele în funcțiune intră cu o notă de deschidere cu sume zero, care poartă amortizarea până la data situației, iar amortizarea continuă din luna următoare; rezerva 105 preluată se transferă la 1175 la ieșire.
- **Configurare necesară**: jurnal de active fixe, conturile 21x/28x/105/1175/655/755/6583, „Cont Pierdere Casare" (6583) pe companie și secvența numerelor de inventar. Pașii de operare, exemplele numerice și verificările sunt în fișa consultantului.

#### 3. Dependențe

- `account_asset`
- `account_reports`
- `l10n_ro_saft`
- `l10n_ro`
- Python: `openpyxl` (importul registrului)

#### 4. Componente Cheie

**Modele**

- `account.asset` (extins): câmpurile RO (inventar, PIF, gestiune, responsabil, categorie SAF-T/HG, date de preluare), suprascrieri pentru SAF-T, start de amortizare, casare/vânzare și baza fiscală.
- `l10n.ro.asset.revaluation` și `l10n.ro.asset.revaluation.wizard`: reevaluarea prin metoda netă, cu monografia 281x/105/655/755.
- `l10n.ro.asset.fiscal.line`: planul lunar de amortizare fiscală; calculul regimurilor e în `models/fiscal_board.py`.
- `l10n.ro.asset.conservation`: perioadele de conservare ale activului.
- `l10n.ro.asset.location` și `l10n.ro.asset.transfer`: gestiunile (nomenclator) și transferurile datate, cu bonul de mișcare.
- `l10n.ro.asset.commissioning.wizard`: punerea în funcțiune din 231.
- `l10n.ro.asset.import.saga`, `.line`, `.account`: importul registrului de imobilizări (verificare, corespondența conturilor, creare).
- `l10n.ro.asset.register.report.handler` (în `report/asset_register.py`): handlerul Registrului imobilizărilor.
- `account.move`, `account.move.line`, `asset.modify`, `res.company`, `res.config.settings`, `account.general.ledger.report.handler` (extinse): note de amortizare/cedare/deschidere, alegerea Reevaluare vs. Modernizare, setarea pentru luna ieșirii și completarea D406.

**Vizualizări**

- `views/account_asset_views.xml`: câmpurile RO, butoanele Reevaluare, Transfer, Casare.
- `views/l10n_ro_asset_revaluation_views.xml`, `views/asset_modify_views.xml`: reevaluarea și fereastra „Modifică".
- `views/l10n_ro_asset_location_views.xml`: gestiunile.
- `views/res_config_settings_views.xml`: setările RO pe companie.
- `wizard/*_views.xml`: reevaluare, punere în funcțiune din 231, import registru.
- `report/report_asset_register.xml`, `report_asset_disposal.xml`, `report_asset_documents.xml`, `saft_assets_ro_inherit.xml`: registrul, decizia de casare, documentele OMFP 2634/2015 și suprascrierile D406.

**Acțiuni Automate / Acțiuni Server**

- „Revalue Fixed Asset" (meniul contextual al listei `account.asset`): deschide wizardul de reevaluare.
- `data/ir_sequence_data.xml`: secvențele de inventar (`MF/`), transferuri (`BM/`) și PV (`PVR/`, `PVS/`).
- Fără `ir.cron`; amortizarea contabilă rămâne mecanismul standard `account_asset`.

#### 5. Conexiuni

- [l10n_ro_inventory_items](../l10n_ro_inventory_items/index.md): obiectele de inventar, complementare registrului de mijloace fixe.
- [l10n_ro_inventory_register](../l10n_ro_inventory_register/index.md): registrul-inventar (14-1-2) preia mijloacele fixe, cu detalierea pe activ după numărul de inventar RO, modernizări incluse.
- [l10n_ro_saft_validator](../l10n_ro_saft_validator/index.md): verificările declarației anuale D406 Active (număr de inventar, PIF, durata față de catalog, perioada).
- `l10n_ro_inventory_items_hr`: darea în folosință a obiectelor de inventar pe salariat (fără pagină wiki încă).
- [l10n_ro_inventory_closing](../l10n_ro_inventory_closing/index.md): închiderea inventarierii, care include și mijloacele fixe.
- [l10n_ro_financial_notes](../l10n_ro_financial_notes/index.md): notele explicative, cu datele despre imobilizări și amortizare.
- [l10n_ro_grants](../l10n_ro_grants/index.md): subvenții pentru active, corelate cu amortizarea activului finanțat.
- [l10n_ro_deferred_entries](../l10n_ro_deferred_entries/index.md): note eșalonate, în același ecosistem de contabilitate RO.
- [l10n_ro_saft_fix](../l10n_ro_saft_fix/index.md): corecția de instalare a lui `l10n_ro_saft`, de care depinde acest modul.
