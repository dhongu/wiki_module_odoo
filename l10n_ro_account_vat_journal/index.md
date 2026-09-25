# Romania - Jurnale de TVA (vânzări și cumpărări) (localizat la `l10n_ro_account_vat_journal/index.md`)

- **Nume Tehnic:** `l10n_ro_account_vat_journal`
- **Versiune:** `19.0.1.2.5`
- **Cale:** [https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_account_vat_journal](https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_account_vat_journal)
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_account_vat_journal`
- **Ultima Ingestie:** `2026-09-25`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul aduce Jurnalul de Vânzări și Jurnalul de Cumpărări — registrele lunare de TVA obligatorii cerute de auditorii ANAF — direct în motorul nativ de rapoarte contabile Enterprise al Odoo (`account.report`). Fiecare jurnal listează facturile, avizele de stornare și chitanțele înregistrate în perioadă, cu baza și TVA-ul defalcate pe fiecare cotă, tratează corect TVA la încasare (inclusiv facturile plătite peste mai multe luni) și taxarea inversă, iar datele rezultate stau la baza declarațiilor D300 și D394. Pe lângă jurnalele „clasice" (o coloană per taxă), modulul oferă acum și o pereche de jurnale **pe regimuri fiscale**, cu coloane fixe și configurabile (redenumire, ordonare, ascundere), iar exportul XLSX are aspect tipizat de registru, gata de tipărit și predat la inspecție.

#### 2. Funcționalități Cheie

- Câte un rând pentru fiecare document (număr, dată, partener, cod fiscal, total document cu TVA);
- **Jurnale standard**, cu coloane dinamice **Bază + TVA per cotă** (21% / 11% și cotele istorice 19% / 9% / 5%);
- **Jurnale pe regimuri fiscale** noi — „Jurnal TVA Vânzări/Cumpărări pe regimuri (RO)" — cu coloane fixe per regim (taxabile pe cote, cote anterioare, taxare inversă, livrări/achiziții intracomunitare, export, scutite cu și fără drept de deducere, neimpozabile, autolichidare cu TVA deductibilă și colectată), configurabile în **Contabilitate → Configurare → Contabilitate → Coloane jurnale de TVA (RO)**: redenumire, reordonare, arhivare sau afișare doar dacă au operațiuni în perioadă;
- Clasificarea unei taxe pe coloană urmează, în ordine: taxa aleasă explicit pe coloană, grupul de taxe, grilele D300 (inclusiv grile vechi adăugate manual), cota (pentru cotele istorice fără grile); taxele cu grile D300 neclasificate ajung în coloana „Alte operațiuni", ca nimic să nu dispară din jurnal;
- Tratarea **TVA la încasare** (bază și TVA eligibile / neeligibile), inclusiv **urmărirea peste mai multe luni**: o factură rămâne vizibilă cu valoarea integrală în luna înregistrării, soldul neexigibil se reportează, iar partea exigibilă apare treptat, pe cote, în luna fiecărei plăți, până la stingerea integrală;
- Tratarea operațiunilor de **taxare inversă** (art. 331), inclusiv TVA colectat din autolichidare pe achiziții intracomunitare, într-o coloană dedicată pe jurnalul de cumpărări;
- Rând de totaluri pentru fiecare jurnal, cu valoare calculată (nu doar formulă) pe fiecare coloană;
- Export **XLSX** cu aspect de registru: titlu cu firma, CUI și perioada (format românesc), cap de tabel cu filtre și fundal, sume cu separatori, dată `zz.ll.aaaa`, rândul Total evidențiat, antet fixat la derulare și pregătit de tipărire (peisaj, încadrare pe lățime A4/A3, cap de tabel repetat pe fiecare pagină, numerotare);
- Export **PDF** (nativ `account.report`);
- Modul de sine stătător: instalarea `l10n_ro_anaf_d394` peste el adaugă direct pe aceste rapoarte un buton de export fișier D394.

#### 3. Dependențe

- `l10n_ro`
- `account_reports`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n_ro.vat.journal.column` (`Model`): definește coloanele jurnalelor **pe regimuri** — etichetă, tip de jurnal (vânzări/cumpărări), fel de coloană (`taxable`, `base`, `self_assessed`, `other`) și regulile de clasificare a taxelor (taxe explicite, grup de taxe, grile D300, cotă pentru taxele fără grile); expune `_l10n_ro_map_taxes()`, algoritmul central de încadrare a unei taxe pe coloană.
- `l10n_ro_account_vat_journal.tax.report.handler` (`AbstractModel`, moștenește `account.generic.tax.report.handler` și `l10n_ro_anaf.report.handler.mixin`): logica comună a jurnalului standard — injectează coloanele dinamice Bază/TVA per cotă, interoghează mișcările contabile din perioadă (inclusiv CABA — TVA la încasare, cu soldul neexigibil calculat la data de sfârșit a perioadei, nu la data curentă — și operațiuni de taxare inversă), generează liniile raportului și rândul de total, și construiește exportul XLSX formatat ca registru.
- `l10n_ro_account_vat_journal.purchase.tax.report.handler` / `...sale.tax.report.handler`: handler-e specializate pentru Jurnalul de Cumpărări, respectiv de Vânzări; fixează `journal_type` înaintea logicii comune.
- `l10n_ro_account_vat_journal.regime.report.mixin` (`AbstractModel`): varianta „pe regimuri" a jurnalelor — păstrează interogarea, TVA la încasare, taxarea inversă și totalurile jurnalului standard, dar înlocuiește coloanele per-taxă cu coloanele fixe din `l10n_ro.vat.journal.column`; mai multe taxe cu aceeași încadrare (ex. două taxe de 21% cu denumiri diferite) ajung în aceeași coloană.
- `l10n_ro_account_vat_journal.purchase.regime.report.handler` / `...sale.regime.report.handler`: combină mixin-ul de regim cu handler-ul standard de cumpărări/vânzări pentru cele două jurnale pe regimuri.

**Vizualizări**

- `view_l10n_ro_vat_journal_column_list` / `..._form` / `..._search`: interfața de configurare a coloanelor jurnalelor pe regimuri — listă cu ordonare prin drag (`sequence`, widget `handle`), grupare/filtrare pe tip de jurnal, formular cu secțiunile „Column" (etichetă, tip, fel, ordine, activ) și „Classification" (taxe explicite, referințe plan de conturi RO, grupuri de taxe, grile D300, cotă, prioritate de potrivire).
- Restul interfeței (jurnalele standard și cele pe regimuri) este generată de motorul nativ `account.report` (rapoarte Enterprise, randate prin acțiunea client `account_report`); modulul nu adaugă vizualizări de formular/listă clasice pentru rapoarte.

**Acțiuni Automate / Acțiuni Server**

- `action_l10n_ro_purchase_tax_report` / `action_l10n_ro_sale_tax_report` (`ir.actions.client`, tag `account_report`): deschid Jurnalul de Cumpărări, respectiv de Vânzări (standard), din meniul Contabilitate → Rapoarte → Taxe (sequence 31/32).
- `action_l10n_ro_purchase_regime_report` / `action_l10n_ro_sale_regime_report` (`ir.actions.client`, tag `account_report`): deschid Jurnalul de Cumpărări, respectiv de Vânzări **pe regimuri**, din același meniu (sequence 33/34).
- `action_l10n_ro_vat_journal_column` (`ir.actions.act_window`): deschide configurarea coloanelor jurnalelor pe regimuri, din meniul Contabilitate → Configurare → Contabilitate → Coloane jurnale de TVA (RO), grupat implicit pe tip de jurnal; vizibilă doar pentru grupul de administrare contabilă.
- Toate cele patru rapoarte (`l10n_ro_purchase_tax_report`, `l10n_ro_sale_tax_report`, `l10n_ro_purchase_regime_report`, `l10n_ro_sale_regime_report`) sunt definite ca înregistrări `account.report` cu `default_opening_date_filter = previous_month` (perioada implicită e luna închisă anterioară) și `only_tax_exigible = True`.
- `pre_init_hook` (`hooks.py`): migrare, nu inițializare generică — pe instalările existente care aveau aceste rapoarte create anterior de `l10n_ro_anaf_d394`, rulează înaintea încărcării datelor noului modul, re-atribuie xml_id-urile (rapoarte, coloane, acțiuni, meniuri), redenumește modelele de handler și curăță metadatele orfane, astfel încât loaderul să actualizeze înregistrările existente în loc să creeze duplicate. Pe instalări noi, UPDATE-urile ating 0 rânduri.

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): furnizează mixin-ul `l10n_ro_anaf.report.handler.mixin` folosit de toate handler-ele de raport.
- [l10n_ro_anaf_d394](../l10n_ro_anaf_d394/index.md): fost proprietar al rapoartelor standard (înainte de extragere); instalat peste acest modul, adaugă un buton de export fișier D394 direct pe jurnale.
- `account_reports`: motorul nativ Enterprise de rapoarte contabile pe care se bazează întreaga arhitectură a modulului.
