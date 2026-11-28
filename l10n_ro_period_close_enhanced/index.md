# Romania - Checklist de închidere de perioadă (localizat la `l10n_ro_period_close_enhanced/index.md`)

- **Nume Tehnic:** `l10n_ro_period_close_enhanced`
- **Versiune:** `20.0.1.15.0`
- **Cale:** [https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_period_close_enhanced](https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_period_close_enhanced)
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_period_close_enhanced`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă un checklist lunar de închidere a perioadei contabile, construit pe infrastructura Enterprise `account.return.type` din `account_reports` și conform OMFP 1802/2014. Înlocuiește lista de control ținută ad-hoc cu o fișă pe lună, cu stare, termen și 32 de verificări automate (documente, confruntări de solduri, depuneri ANAF, controale operaționale), la care se adaugă verificări manuale și cele ale modulelor opționale. Fiecare verificare duce la înregistrările vinovate, iar la final se obțin procesul-verbal de pre-închidere și arhiva cu situațiile lunare. Se adresează contabililor care fac închiderea lunară.

#### 2. Funcționalități Cheie

- **Checklist interactiv de tip `audit`**, creat pentru fiecare lună (**Contabilitate → Closing → Închidere Perioadă (RO)**). Pe Odoo 20 fluxul este „(fără stare) → Reviewed → Submit"; starea inițială „New" din 19.0 nu mai există. Termenul implicit este de 5 zile după sfârșitul lunii, configurabil pe tipul de return din **Contabilitate → Configurare → Return Types**.
- **32 de verificări** pe patru familii; cele ale modulelor opționale apar doar cu modulul instalat. Rezultatele sunt Verificat, Anomalie sau În așteptare, iar butonul „De revizuit" marchează manual o verificare:
  - **Documente și reconcilieri:** facturi/avize în Schiță, extrase bancare nereconciliate.
  - **Confruntări de solduri** (mesajul arată ambele sume și diferența): casă 531x, jurnale de TVA vs. 4426/4427, TVA neexigibilă 4428, balanță echilibrată, amortizare 681x vs. registrul mijloacelor fixe, registru vs. 21x/28x, viramente interne 581, clasele 6 și 7 fără sold după închiderea în 121, repartizări lunare 471/472.
  - **Depuneri ANAF:** D300, D390, D394, D112 și recipise fără erori.
  - **Controale operaționale:** stoc negativ, recepții pe aviz nefacturate (408), valorizare stoc vs. 3xx, mesaje SPV neprelucrate, facturi emise nevalidate în e-Factura, avansuri nejustificate (409/419).
- **Termen legal pe periodicitatea reală a companiei:** o declarație lipsă înainte de termen e sarcină, nu anomalie; termenul lunar e pe 25, iar la TVA trimestrial se calculează de la sfârșitul trimestrului.
- **D390** se cere doar când perioada are operațiuni intracomunitare, după tag-urile fiscale ale declarației.
- **Regularizarea TVA (4426/4427 → 44231/4424)** se verifică pe nota de închidere generată de returnul D300 la depunere.
- **Verificări condiționale:** Coeficient K, CMP periodic, reevaluare valutară (665/765), WIP producție, provizioane de stoc, închidere de inventar. **Verificări manuale:** registru de casă, inventar stocuri, reconciliere clienți/furnizori.
- **Conturi de control configurabile pe companie**, ca prefixe în **Contabilitate → Configurare → Setări**; un prefix golit scoate verificarea din checklist.
- **Blocări:** la validarea lunii decembrie se avansează `fiscalyear_lock_date` (niciodată retras); fiecare jurnal poate avea și o **Dată blocare jurnal** proprie, care respinge postările datate la sau înainte de ea.
- **Proces-verbal de pre-închidere (PDF)**, generat la validare și retipăribil.
- **Situații lunare (ZIP):** asistent din meniul ⋮ al cardului lunii; generează în PDF și/sau XLSX balanța de verificare, jurnalele de vânzări și cumpărări, registrul-jurnal, registrul de casă, jurnalul de bancă și fișele de cont, atașate pe checklist. Setul implicit și generarea automată la validare se configurează în Setări.
- **Reguli de reconciliere pentru plățile la buget** (TVA 4423, profit 4411, micro 4418, CAS 4315, CASS 4316, CAM 436, impozit salarii 444, alte impozite 446), create pentru companiile cu plan RO la instalare, la upgrade și pentru companii noi. Detaliile pas-cu-pas sunt în fișa consultantului.

#### 3. Dependențe

- `account_reports`
- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.return` (extins, pe mai multe fișiere): motorul checklistului RO.
  - `account_return.py`: verificările condiționale de closing, verificarea D300, blocarea exercițiului la validarea din decembrie și generarea procesului-verbal.
  - `account_return_balance.py`: infrastructura de confruntare sold operațional vs. rulaj și verificările de casă, TVA, balanță, amortizare și mijloace fixe.
  - `account_return_declarations.py`: verificarea de depunere a declarațiilor (cu termen pe periodicitate), D390, D394, D112 și recipisele ANAF.
  - `account_return_operations.py`: stoc negativ, recepții pe aviz vs. 408, valorizare stoc, mesaje SPV, facturi nevalidate în e-Factura, avansuri 409/419.
  - `account_return_monthly_reports.py`: situațiile lunare atașate pe checklist.
- `account.report` (extins): suportul rapoartelor folosite de situațiile lunare.
- `account.chart.template` (extins): livrează regulile de reconciliere `account.reconcile.model` pentru plățile bugetare RO.
- `account.journal` (extins): câmpul `l10n_ro_lock_date`, blocarea postării pe jurnal.
- `account.move` (extins): respinge postarea unei note datate în perioada blocată a jurnalului, pentru companiile cu țara fiscală RO.
- `res.company` / `res.config.settings` (extinse): prefixele conturilor de control, reconcilierea automată a plăților bugetare și setările situațiilor lunare.
- `l10n.ro.period.close.reports.wizard`: asistentul „Situații lunare" (rapoarte, conturi pentru fișe, format PDF/XLSX).

**Vizualizări**

- `data/period_close_return_type.xml`: tipul de return `return_type_ro_period_close` (categorie `audit`, periodicitate lunară, termen 5 zile) și cele 32 de șabloane de verificare.
- `data/menu.xml`: intrarea **Contabilitate → Closing → Închidere Perioadă (RO)**, pe vizualizarea kanban de audit din `account_reports`.
- `report/report_period_close.xml`: raportul PDF de pre-închidere (proces-verbal cu semnături).
- `views/res_config_settings_views.xml`: conturile de control, reconcilierea bugetară și situațiile lunare.
- `views/account_journal_views.xml`: data de blocare pe jurnal.
- `wizard/period_close_reports_wizard_views.xml`: formularul asistentului de situații lunare.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook` (`_l10n_ro_period_close_post_init`): inițializează la instalare regulile și datele specifice RO.
- Migrări post-update (`20.0.1.12.1`, `20.0.1.14.0`): aduc checklisturile create pe 19.0 la ciclurile și verificările din 20.0.
- Verificările se evaluează la reîmprospătarea checklistului; la `action_validate()` se aplică blocarea exercițiului (decembrie), se generează procesul-verbal și, dacă e bifat în Setări, arhiva situațiilor lunare. Nu sunt definite `ir.cron`.

#### 5. Conexiuni

- [l10n_ro_stock_k_coefficient](../l10n_ro_stock_k_coefficient/index.md): verificare condiționată — coeficientul K postat.
- [l10n_ro_stock_cmp_periodic](../l10n_ro_stock_cmp_periodic/index.md): verificare condiționată — corecția CMP periodic postată.
- [l10n_ro_currency_revaluation](../l10n_ro_currency_revaluation/index.md): verificare condiționată — reevaluarea valutară postată.
- [l10n_ro_wip_closing](../l10n_ro_wip_closing/index.md): verificare condiționată — WIP-ul de producție finalizat.
- [l10n_ro_stock_provision](../l10n_ro_stock_provision/index.md): verificare condiționată — provizioanele de stoc confirmate.
- [l10n_ro_inventory_closing](../l10n_ro_inventory_closing/index.md): verificare condiționată — inventarele contabilizate.
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): returnul de TVA pe care se bazează verificarea D300 și nota de regularizare a TVA.
- [l10n_ro_anaf_d390](../l10n_ro_anaf_d390/index.md): returnul recapitulativ UE, pentru verificarea D390 și tag-urile intracomunitare.
- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md): returnul declarației de contribuții, pentru verificarea D112.
- [l10n_ro_anaf_d394](../l10n_ro_anaf_d394/index.md): declarația informativă D394, verificată prin registrul de depuneri.
- [l10n_ro_anaf_submission](../l10n_ro_anaf_submission/index.md): registrul de depuneri ANAF, sursă pentru D394 și „recipise ANAF fără erori".
- [l10n_ro_message_spv](../l10n_ro_message_spv/index.md): mesajele SPV verificate ca fiind prelucrate în perioadă.
- [l10n_ro_account_return_pl_closing](../l10n_ro_account_return_pl_closing/index.md): checklist complementar de închidere P&L, lansabil din checklist.
- [l10n_ro_rni_report](../l10n_ro_rni_report/index.md): raportul de recepții fără factură, folosit la confruntarea pe sume a soldului 408.
- `l10n_ro_stock_account_check`: raportul de valorizare a stocului față de conturile 3xx, rulat dacă e instalat.
