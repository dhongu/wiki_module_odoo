# Romania - Checklist de închidere de perioadă (localizat la `l10n_ro_period_close_enhanced/index.md`)

- **Nume Tehnic:** `l10n_ro_period_close_enhanced`
- **Versiune:** `19.0.1.12.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_period_close_enhanced
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_period_close_enhanced`
- **Ultima Ingestie:** 2026-09-12
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul de localizare românească care implementează un checklist lunar de închidere a perioadei contabile, folosind infrastructura Enterprise `account.return.type` din modulul `account_reports`. Se adresează contabililor care efectuează închiderea lunară și doresc un flux structurat, cu verificări automate ale rulajelor și soldurilor, conform cerințelor OMFP 1802/2014, care înlocuiește verificarea manuală ad-hoc a „listei de control" lunare.

#### 2. Funcționalități Cheie

- Checklist interactiv de tip `audit` cu flux **New → Review → Submit**, creat automat pentru fiecare lună (**Contabilitate → Closing → RO – Checklist Închidere Perioadă**).
- **Verificări automate** evaluate direct din date: facturi/avize în stare Schiță datate în perioadă; extrase bancare nereconciliate.
- **Confruntări de sold** (sursă operațională vs. rulaj contabil, cu diferența afișată explicit în mesaj): registru de casă vs. conturi 531x; jurnalul de TVA vs. conturile 4426/4427; TVA la încasare vs. contul 4428 (comparație unidirecțională — un sold 4428 mai mare e normal, fiindcă include și 408/418); balanța de verificare echilibrată (rulaj și cumulat); cheltuiala cu amortizarea vs. conturile 681x; registrul mijloacelor fixe vs. conturile 21x/28x (valoare brută și amortizare cumulată).
- **Verificări operaționale de completitudine**: nicio cantitate negativă pe gestiune (`stock.quant`); soldul 408 (marfă recepționată nefacturată) justificat de recepții pe aviz deschise, cu comparație pe sume dacă `l10n_ro_rni_report` e instalat; valorizarea de stoc vs. conturile de stoc 3xx (rulează raportul `stock.accounting.check` din `l10n_ro_stock_account_check`, dacă e instalat); mesajele SPV (e-Factura) fără vreunul rămas neprocesat; avansurile 409/419 fără sume decontate dar nereconciliate.
- **Verificări condiționale**, active doar dacă modulul opțional e instalat: Coeficient K (`l10n_ro_stock_k_coefficient`), CMP Periodic (`l10n_ro_stock_cmp_periodic`), Reevaluare Valutară 665/765 (`l10n_ro_currency_revaluation`), Regularizare TVA 4426/4427 → 44231/4424 (`l10n_ro_vat_regularization`), WIP producție 331/711 (`l10n_ro_wip_closing`), provizioane stocuri slow-moving 39x (`l10n_ro_stock_provision`), contabilizare completă a inventarelor de stoc (`l10n_ro_inventory_closing`).
- **Depunerea declarațiilor lunare/trimestriale la ANAF**: D300 (TVA), D390 (recapitulativă UE — doar dacă perioada are operațiuni intracomunitare), D394 și D112, fiecare raportată `todo` până la termenul legal (25 ale lunii următoare) și `anomaly` după, plus o verificare finală că toate depunerile perioadei au recipisă ANAF fără erori (fără rămase respinse/în eroare din `l10n.ro.anaf.submission`).
- **Verificări manuale** confirmate prin bifare de contabil: registru de casă verificat față de numerar fizic, inventar stocuri regularizat, reconciliere conturi clienți/furnizori 411x/401x.
- Conturile de control folosite în confruntările de sold (casă, TVA deductibilă/colectată/amânată, amortizare, mijloace fixe, marfă nefacturată, avansuri) sunt configurabile pe companie, ca prefixe de cont, din **Contabilitate → Configurare → Setări → Period Closing Control Accounts (RO)**; un prefix golit dezactivează verificarea care depinde de el.
- **Blocare perioadă la validare**: la închiderea lunii decembrie se setează automat data de blocare a exercițiului financiar (`fiscalyear_lock_date`), avansând doar (nu retrage o blocare existentă mai recentă).
- **Blocare per-jurnal** (`l10n_ro_lock_date` pe `account.journal`): permite blocarea jurnalelor TVA/vânzări după depunerea D300, ținând alte jurnale (ex. salarii) deschise; postarea unei note contabile datate în perioada blocată a jurnalului ei este respinsă.
- **Raport unic de pre-închidere (PDF)**: proces-verbal cu toate verificările (verificate / anomalii / în așteptare), observații și semnături — generat automat la validare și atașat la chatter, retipăribil oricând (`action_print_preclose_report`).
- Termen implicit de 5 zile după sfârșitul perioadei de raportare (lunară sau trimestrială, după periodicitatea companiei), configurabil pe tipul de return (`RO – Checklist Închidere Perioadă`).
- **Reguli de reconciliere** pentru plățile lunare la buget (TVA 4423, impozit profit 4411, micro 4418, CAS 4315, CASS 4316, CAM 436, impozit salarii 444, alte impozite 446) — livrate ca șablon `account.reconcile.model` la instalare/upgrade și pentru companii noi, cu propunere automată a contrapartidei pe baza narațiunii extrasului bancar (potrivire pe cuvânt-cheie sau regex pentru CAS/CASS/CAM); activare opt-in a reconcilierii complet automate din **Contabilitate → Configurare → Setări → Budget Payments Reconciliation (RO)** (`res.company.l10n_ro_budget_auto_reconcile`), cu buton de sincronizare a regulilor existente.
- Integrare nativă cu checklistele de closing din celelalte module RO — checklistul e recomandat ca ultimul pas, după rularea operațiilor de closing dedicate (K, CMP, reevaluare, regularizare TVA, WIP, D300).

#### 3. Dependențe

- `account_reports`
- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.return` (extins, pe 4 fișiere): motorul checklist-ului RO de închidere lunară.
  - `account_return.py`: verificările condiționale de operații de closing (K, CMP, reevaluare valutară, regularizare TVA, WIP, provizioane stoc, contabilizare inventar), verificarea D300, blocarea exercițiului la validarea din decembrie (`_l10n_ro_apply_period_lock`) și generarea raportului de pre-închidere (`_l10n_ro_generate_preclose_report`, `action_print_preclose_report`).
  - `account_return_balance.py`: infrastructura comună de confruntare sold operațional vs. rulaj contabil (`_l10n_ro_control_accounts`, `_l10n_ro_balance_of`) și verificările de casă, TVA (jurnale/amânată), balanță de verificare, amortizare și registru de mijloace fixe.
  - `account_return_declarations.py`: verificarea generică de depunere a declarațiilor lunare (`_check_ro_declaration_submitted`, cu logică de termen pe periodicitate) și verificările specifice D390, D394, D112 și „recipise ANAF fără erori".
  - `account_return_operations.py`: verificările de completitudine operațională — stoc negativ, recepții pe aviz vs. cont 408, valorizare stoc vs. conturi 3xx, mesaje SPV neprocesate, avansuri 409/419 nejustificate.
- `account.chart.template` (extins): livrează șablonul de reguli de reconciliere `account.reconcile.model` pentru plățile bugetare RO (`_get_ro_budget_reconcile_model`), pe baza mapării `RO_BUDGET_RECO_RULES`/`RO_BUDGET_RECO_NAMES`.
- `account.journal` (extins): câmpul `l10n_ro_lock_date` pentru blocare de postare per-jurnal.
- `account.move` (extins): respinge postarea (`_post`) unei note contabile datate în perioada blocată a jurnalului ei, pentru companiile cu țara fiscală RO.
- `res.company` (extins): conturile de control ale confruntărilor de sold (`l10n_ro_close_*_prefix`, cu prefixe implicite conform OMFP 1802/2014), flag-ul de reconciliere automată a plăților bugetare (`l10n_ro_budget_auto_reconcile`) și sincronizarea regulilor (`action_l10n_ro_sync_budget_reconcile`).
- `res.config.settings` (extins): expune setările de mai sus în ecranul de configurare Contabilitate.

**Vizualizări / Date**

- `data/period_close_return_type.xml`: definește tipul de return `return_type_ro_period_close` (categorie `audit`, flux `generic_state_review_submit`, periodicitate lunară, termen 5 zile) și cele 20 de șabloane de verificare (`account.return.check.template`) — de la facturi în ciornă și extrase nereconciliate, până la confruntările de sold, declarațiile ANAF și verificările manuale.
- `data/menu.xml`: acțiunea și intrarea de meniu **Contabilitate → Closing → Period Closing (RO)**, pe view-ul kanban de audit standard din `account_reports`.
- `report/report_period_close.xml`: raportul PDF de pre-închidere (proces-verbal cu situația fiecărei verificări și semnături).
- `views/res_config_settings_views.xml`: setările de reconciliere bugetară automată și conturile de control ale confruntărilor de sold.
- `views/account_journal_views.xml`: câmpul de blocare per-jurnal pe formularul de jurnal contabil.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook` (`_l10n_ro_period_close_post_init`): rulează la instalare pentru inițializarea regulilor/datelor specifice RO.
- Verificările (model+domeniu și cele Python condiționate/de confruntare) sunt evaluate la refresh/review, prin `_run_checks()` / `_check_suite_ro_period_close()` suprascris pe `account.return`, compus din cele 4 fișiere de model.
- La `action_validate()` pe checklist se declanșează automat blocarea exercițiului (decembrie) și generarea/atașarea raportului PDF de pre-închidere.
- La postarea unei note contabile (`account.move._post`), se verifică blocarea per-jurnal (`l10n_ro_lock_date`) pentru companiile RO.

#### 5. Conexiuni

- [l10n_ro_stock_k_coefficient](../l10n_ro_stock_k_coefficient/index.md): verificare condiționată — coeficientul K postat pentru luna curentă.
- [l10n_ro_stock_cmp_periodic](../l10n_ro_stock_cmp_periodic/index.md): verificare condiționată — nota de corecție CMP periodic postată.
- [l10n_ro_currency_revaluation](../l10n_ro_currency_revaluation/index.md): verificare condiționată — reevaluarea valutară postată.
- [l10n_ro_vat_regularization](../l10n_ro_vat_regularization/index.md): verificare condiționată — regularizarea lunară a TVA (4426/4427 → 44231/4424) postată.
- [l10n_ro_wip_closing](../l10n_ro_wip_closing/index.md): verificare condiționată — WIP-ul de producție finalizat în perioadă.
- [l10n_ro_stock_provision](../l10n_ro_stock_provision/index.md): verificare condiționată — provizioanele de stoc slow-moving confirmate.
- [l10n_ro_inventory_closing](../l10n_ro_inventory_closing/index.md): verificare condiționată — inventarele de stoc complet contabilizate.
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): tipul de return de TVA (`ro_tax_return_type`) pe care se bazează verificarea de depunere D300.
- [l10n_ro_anaf_d390](../l10n_ro_anaf_d390/index.md): tipul de return al declarației recapitulative UE (`d390_return_type`), pentru verificarea de depunere D390.
- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md): tipul de return al declarației de contribuții (`d112_return_type`), pentru verificarea de depunere D112.
- [l10n_ro_anaf_submission](../l10n_ro_anaf_submission/index.md): registrul de depuneri ANAF (`l10n.ro.anaf.submission`), sursă pentru verificarea D394 și pentru „recipise ANAF fără erori".
- [l10n_ro_message_spv_purchase](../l10n_ro_message_spv_purchase/index.md): mesajele SPV e-Factura (`l10n.ro.message.spv`), verificate ca fiind procesate integral în perioadă.
- [l10n_ro_account_return_pl_closing](../l10n_ro_account_return_pl_closing/index.md): checklist complementar de închidere P&L, în același ecosistem de closing bazat pe `account.return`.
- `l10n_ro_anaf_d394`: declarația informativă D394, verificată prin registrul de depuneri (fără tip propriu de return).
- `l10n_ro_stock_account_check`: raportul `stock.accounting.check`, rulat de verificarea de valorizare a stocului (3xx) dacă e instalat.
- [l10n_ro_rni_report](../l10n_ro_rni_report/index.md): raportul dedicat de recepții fără factură, folosit (dacă e instalat) pentru confruntarea pe sume a soldului 408, în loc de simpla verificare de prezență.

---

**Notă din re-ingestie (2026-09-12):** `readme/DESCRIPTION.md` și `readme/USAGE.md` documentează doar un subset (8 verificări) din checklist-ul real; între timp modulul a ajuns la 20 de șabloane de verificare (`data/period_close_return_type.xml`) — confruntări de sold (casă, TVA, balanță, amortizare, mijloace fixe), depuneri de declarații ANAF (D300/D390/D394/D112 + recipise) și verificări operaționale (stoc negativ, recepții pe aviz, valorizare stoc, mesaje SPV, avansuri). Secțiunea 2 de mai sus a fost completată direct din cod (`models/account_return*.py` + `data/period_close_return_type.xml`) pentru a reflecta versiunea curentă 19.0.1.12.0.
