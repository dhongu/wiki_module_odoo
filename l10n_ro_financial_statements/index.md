# Romania - Situații Financiare Anuale ANAF (FR-31) (localizat la `l10n_ro_financial_statements/index.md`)

- **Nume Tehnic:** `l10n_ro_financial_statements`
- **Versiune:** `19.0.1.3.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_financial_statements
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_financial_statements`
- **Ultima Ingestie:** 2026-08-20
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Extinde rapoartele financiare native românești din Odoo Enterprise (`l10n_ro_reports`) cu funcționalități de depunere a situațiilor financiare anuale conform OMFP 1802/2014. Adaugă un buton „Export XML ANAF" direct în headerul rapoartelor Formular 10 (Bilanț) și Formular 20 (Cont de Profit și Pierdere), cu validare de echilibru al bilanțului înainte de export, și introduce două rapoarte custom noi în framework-ul Enterprise: Formularul 40 (Situația activelor imobilizate), calculat automat din clasele de conturi 20x/21x/26x/28x/29x, și Formularul 30 (Date informative), care combină rânduri calculate din contabilitate cu rânduri completate manual (ex. număr de salariați, structura capitalului social) și exportă XML-ul aferent. Se adresează contabililor și directorilor financiari din companiile românești care depun anual situațiile financiare la ANAF și Registrul Comerțului.

#### 2. Funcționalități Cheie

- **Buton „Export XML ANAF"** în headerul rapoartelor „Cod 10 - Bilanț" și „Cod 20 - Cont de Profit și Pierdere"; butonul este `always_show`, deci apare indiferent de varianta de raport auto-selectată.
- **Formularul 10 (Bilanț):** XML cu rândurile 01–51 extrase din raportul Enterprise prin pattern `| NN`, cu atribut `tip="BL"`.
- **Formularul 20 (CPP):** XML cu rândurile 01–68 extrase din raportul Enterprise (`tip="CPP"`); butonul este atașat pe **toate variantele** de cont de profit și pierdere (smle / micro-entitate / internațional).
- **Validare bilanț echilibrat:** blocare export dacă Total Activ (rd.04+11+12) ≠ Total Pasiv (rd.15+18+19+20+51), cu toleranță 1 RON; validarea rulează doar pentru bilanț (F10).
- **Formularul 40 — Situația activelor imobilizate:** raport Enterprise nou, cu coloane Sold inițial / Creșteri / Reduceri / Sold final, calculat automat pe categorii (imobilizări necorporale, corporale, financiare, amortizare, ajustări de depreciere) din rulajele conturilor 20x/21x/23x/26x/28x/29x.
- **Formularul 30 — Date informative:** raport Enterprise nou care combină rânduri derivate din contabilitate (rezultat profit/pierdere, plăți restante furnizori/buget/credite, dobânzi, creanțe/datorii pe scadențe) cu rânduri introduse manual (număr mediu de salariați, structura capitalului social, cheltuieli de cercetare-dezvoltare) prin modelul persistent `l10n.ro.f30.manual.value`; include buton „Fill manual rows" pentru pre-completarea rândurilor pe companie/perioadă și buton „Export XML ANAF" care exportă doar rândurile cu număr oficial confirmat (`anaf_nr`).
- **Implementat integral ca handlere `account.report.custom.handler`** — trei handlere (`l10n.ro.fs.handler` pentru F10/F20, `l10n.ro.f40.handler`, `l10n.ro.f30.handler`), integrate nativ în frameworkul Enterprise de rapoarte, fără ecrane proprii de introducere a datelor contabile.

#### 3. Dependențe

- `l10n_ro_reports`
- `account`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.fs.handler` (`account.report.custom.handler`): handler ce adaugă butonul „Export XML ANAF" și logica de generare a XML-ului pentru F10 (Bilanț) și F20 (CPP), inclusiv validarea de echilibru a bilanțului.
- `l10n.ro.f40.handler` (`account.report.custom.handler`): calculează Situația activelor imobilizate (F40) pe categorii de conturi (necorporale, corporale, financiare, amortizare, ajustări), cu solduri inițiale/finale și creșteri/reduceri pe perioadă.
- `l10n.ro.f30.handler` (`account.report.custom.handler`): calculează rândurile Formularului 30 (rezultat, plăți restante, dobânzi/dividende, creanțe/datorii pe scadențe), gestionează butoanele „Fill manual rows" și „Export XML ANAF" și construiește XML-ul final doar cu rândurile al căror număr oficial ANAF (`anaf_nr`) e confirmat.
- `l10n.ro.f30.manual.value`: stochează valorile introduse manual pentru rândurile statistice ale Formularului 30 (număr salariați, structura capitalului social, cheltuieli C&D pe surse), cheie unică pe companie + perioadă + cod de rând.

**Vizualizări / Date**

- `data/l10n_ro_fs_report_setup.xml`: leagă handlerul `l10n.ro.fs.handler` de raportul F10 Bilanț (`l10n_ro_reports.account_financial_report_ro_bs_smle`) și de variantele F20 CPP (`account_financial_report_ro_pnl_smle`, `..._micro`, `..._internat`).
- `data/l10n_ro_f40_report.xml`: definește raportul Enterprise „Cod 40 - Statement of Fixed Assets" (coloane Sold inițial/Creșteri/Reduceri/Sold final), acțiunea client și intrarea de meniu în Rapoartele contabile.
- `data/l10n_ro_f30_report.xml`: definește raportul Enterprise „Cod 30 - Informative Data (auto-fill)", acțiunea client și intrarea de meniu în Rapoartele contabile.
- `views/l10n_ro_f30_manual_views.xml`: vizualizarea listă `view_l10n_ro_f30_manual_value_list` pentru editarea rândurilor manuale ale Formularului 30, deschisă din butonul „Fill manual rows".

**Acțiuni Automate / Acțiuni Server**

- Acțiunea de export XML ANAF, declanșată din butonul `always_show` din headerul rapoartelor F10/F20/F30.
- Acțiunea „Fill manual rows" (F30), care seedează idempotent câte un rând manual pe companie/perioadă și deschide lista editabilă.

#### 5. Conexiuni

- [l10n_ro_financial_notes](../l10n_ro_financial_notes/index.md): note explicative la bilanț, complementare situațiilor financiare.
- [l10n_ro_inventory_register](../l10n_ro_inventory_register/index.md): document suport pentru patrimoniu.
- [l10n_ro_account_return_pl_closing](../l10n_ro_account_return_pl_closing/index.md): rezultatul exercițiului în contul 121.
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): infrastructură ANAF în ecosistemul de declarații.
- [l10n_ro_account_chart](../l10n_ro_account_chart/index.md): planul de conturi RO pe care se construiesc formularele.
