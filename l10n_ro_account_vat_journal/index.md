# Romania - VAT Journals (Sales & Purchase) (localizat la `l10n_ro_account_vat_journal/index.md`)

- **Nume Tehnic:** `l10n_ro_account_vat_journal`
- **Versiune:** `19.0.1.0.0`
- **Cale:** [https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_account_vat_journal](https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_account_vat_journal)
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_account_vat_journal`
- **Ultima Ingestie:** `2026-07-02`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul aduce Jurnalul de Vânzări și Jurnalul de Cumpărări — registrele lunare de TVA obligatorii cerute de auditorii ANAF — direct în motorul nativ de rapoarte contabile Enterprise al Odoo (`account.report`). Fiecare jurnal listează facturile, avizele de stornare și chitanțele înregistrate în perioadă, cu baza și TVA-ul defalcate pe fiecare cotă, tratează corect TVA la încasare și taxarea inversă, iar datele rezultate stau la baza declarațiilor D300 și D394.

#### 2. Funcționalități Cheie

- Câte un rând pentru fiecare document (număr, dată, partener, cod fiscal, total document);
- Coloane dinamice **Bază + TVA per cotă** (21% / 11% și cotele istorice 19% / 9% / 5%);
- Tratarea **TVA la încasare** (bază și TVA eligibile / neeligibile);
- Tratarea operațiunilor de **taxare inversă** (art. 331);
- Rând de totaluri pentru fiecare jurnal;
- Export XLSX (aspect tipizat) și PDF (nativ `account.report`);
- Modul de sine stătător: instalarea `l10n_ro_anaf_d394` peste el adaugă direct pe aceste rapoarte un buton de export fișier D394.

#### 3. Dependențe

- `l10n_ro`
- `account_reports`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n_ro_account_vat_journal.tax.report.handler` (`AbstractModel`, moștenește `account.generic.tax.report.handler` și `l10n_ro_anaf.report.handler.mixin`): logica comună de construire a liniilor jurnalului de TVA — interogare mișcări contabile, defalcare bază/TVA per cotă, tratare TVA la încasare și taxare inversă.
- `l10n_ro_account_vat_journal.purchase.tax.report.handler`: handler specializat pentru Jurnalul de Cumpărări, moștenește handler-ul comun.
- `l10n_ro_account_vat_journal.sale.tax.report.handler`: handler specializat pentru Jurnalul de Vânzări, moștenește handler-ul comun.

**Vizualizări**

Modulul nu adaugă vizualizări de formular/listă clasice; interfața este generată de motorul nativ `account.report` (raport de tip Enterprise, randat prin acțiunea client `account_report`).

**Acțiuni Automate / Acțiuni Server**

- `action_l10n_ro_purchase_tax_report` (`ir.actions.client`, tag `account_report`): deschide raportul „VAT Purchase Journal” (Jurnal de Cumpărări RO), accesibil din meniul Contabilitate → Rapoarte → Taxe.
- `action_l10n_ro_sale_tax_report` (`ir.actions.client`, tag `account_report`): deschide raportul „VAT Sales Journal” (Jurnal de Vânzări RO), din același meniu.
- Ambele rapoarte (`l10n_ro_purchase_tax_report`, `l10n_ro_sale_tax_report`) sunt definite ca înregistrări `account.report` cu `default_opening_date_filter = previous_month` (perioada implicită este luna închisă anterioară) și `only_tax_exigible = True`.
- `pre_init_hook` (`hooks.py`): rulează la instalare, înainte de încărcarea datelor modulului.

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): furnizează mixin-ul `l10n_ro_anaf.report.handler.mixin` folosit de handler-ele de raport.
- [l10n_ro_anaf_d394](../l10n_ro_anaf_d394/index.md): instalat peste acest modul, adaugă un buton de export fișier D394 direct pe cele două jurnale.
- `account_reports`: motorul nativ Enterprise de rapoarte contabile pe care se bazează întreaga arhitectură a modulului.
