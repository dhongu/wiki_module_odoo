# Romania - Situații Financiare Anuale ANAF (FR-31) (localizat la `l10n_ro_financial_statements/index.md`)

- **Nume Tehnic:** `l10n_ro_financial_statements`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_financial_statements
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_financial_statements`
- **Ultima Ingestie:** 2026-06-09
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Extinde rapoartele financiare native românești din Odoo Enterprise (`l10n_ro_reports`) cu un buton „Export XML ANAF", direct în headerul rapoartelor Formular 10 (Bilanț) și Formular 20 (Cont de Profit și Pierdere). Modulul **nu adaugă un ecran propriu** — generează fișierul XML în formatul de depunere ANAF (`tip=BL` pentru bilanț, `tip=CPP` pentru CPP), prin același mecanism ca exportul D300/SAF-T, și validează că bilanțul este echilibrat înainte de export. Se adresează contabililor și directorilor financiari din companiile românești care depun situațiile financiare anuale conform OMFP 1802/2014.

#### 2. Funcționalități Cheie

- **Buton „Export XML ANAF"** în headerul rapoartelor „Cod 10 - Bilanț" și „Cod 20 - Cont de Profit și Pierdere"; butonul este `always_show`, deci apare indiferent de varianta de raport auto-selectată.
- **Formularul 10 (Bilanț):** XML cu rândurile 01–51 extrase din raportul Enterprise prin pattern `| NN`.
- **Formularul 20 (CPP):** XML cu rândurile 01–68 extrase din raportul Enterprise; butonul este atașat pe **toate variantele** de cont de profit și pierdere (smle / micro-entitate / internațional).
- **Validare bilanț echilibrat:** blocare export dacă Total Activ (rd.04+11+12) ≠ Total Pasiv (rd.15+18+19+20+51), cu toleranță 1 RON; validarea rulează doar pentru bilanț (F10).
- **Implementat ca `account.report.custom.handler`** — un singur handler `l10n.ro.fs.handler` legat de raportul F10 și de variantele F20, integrat nativ în frameworkul Enterprise de rapoarte.

#### 3. Dependențe

- `l10n_ro_reports`
- `account`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.fs.handler` (`account.report.custom.handler`): handler unic ce adaugă butonul „Export XML ANAF" și logica de generare a XML-ului ANAF (validarea echilibrului bilanțului se aplică doar la F10).

**Vizualizări / Date**

- `data/l10n_ro_fs_report_setup.xml`: leagă handlerul `l10n.ro.fs.handler` de raportul F10 Bilanț (`l10n_ro_reports.account_financial_report_ro_bs_smle`) și de variantele F20 CPP (`account_financial_report_ro_pnl_smle`, `..._micro`, `..._internat`).

**Acțiuni Automate / Acțiuni Server**

- Acțiunea de export XML ANAF, declanșată din butonul `always_show` din headerul rapoartelor F10/F20.

#### 5. Conexiuni

- [l10n_ro_financial_notes](../l10n_ro_financial_notes/index.md): note explicative la bilanț, complementare situațiilor financiare.
- [l10n_ro_inventory_register](../l10n_ro_inventory_register/index.md): document suport pentru patrimoniu.
- [l10n_ro_account_return_pl_closing](../l10n_ro_account_return_pl_closing/index.md): rezultatul exercițiului în contul 121.
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): infrastructură ANAF în ecosistemul de declarații.
- [l10n_ro_account_chart](../l10n_ro_account_chart/index.md): planul de conturi RO pe care se construiesc formularele.
