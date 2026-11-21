# Romania - Import extrase bancare (XLSX) (localizat la `l10n_ro_account_bank_statement_import_xlsx/index.md`)

- **Nume Tehnic:** `l10n_ro_account_bank_statement_import_xlsx`
- **Versiune:** `19.0.2.1.7`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_account_bank_statement_import_xlsx
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_account_bank_statement_import_xlsx`
- **Ultima Ingestie:** `2026-11-21`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul completează importul extraselor de cont din fișiere Excel (XLSX) cu identificarea automată a partenerului. Fișierul se încarcă în jurnalul de bancă, iar coloanele lui se asociază cu câmpurile liniei de extras în asistentul de import Odoo (asocierea este reținută pentru importurile următoare). Este util pentru băncile care nu oferă export MT940 sau CAMT, iar contabilii preiau extrasele direct din Excel, fără conversii manuale.

#### 2. Funcționalități Cheie

- **Identificarea partenerului după nume:** valoarea din coloana asociată cu *Nume partener* se caută printre partenerii din Odoo, după denumirea identică (fără să conteze majusculele); partenerul găsit se completează pe linie.
- **Identificarea partenerului după comanda de vânzare:** dacă linia nu are partener și detaliile plății (*Eticheta*) conțin exact numărul unei comenzi de vânzare, se completează clientul de facturare al comenzii (necesită aplicația Vânzări instalată). Liniile fără detalii primesc eticheta „N/A”.
- **Parsere XLSX dedicate:** dacă fișierul este recunoscut de un parser dedicat instalat (de exemplu un borderou de curier), importul trece direct pe acel parser, fără asistentul de mapare.
- **Cum se importă:**
  - fișierul XLSX are un rând de antet și rândurile ordonate după dată;
  - din *Contabilitate → Tablou de bord*, pe cardul jurnalului de bancă, se apasă **Încărcare** (sau **⋮** → **Importă fișier**);
  - în asistentul **Importă extras cont bancar** se asociază data → *Dată*, detaliile → *Eticheta*, numele → *Nume partener*, suma → *Valoare* (sau *Debit* și *Credit*), soldul → *Cumulative Balance* (opțional, pentru soldurile extrasului), apoi **Test** și **Importă**;
  - se verifică liniile (cele fără partener se completează manual înainte de reconciliere) și soldurile extrasului; fișierul importat rămâne atașat extrasului.
- **Restricții:** se poate selecta un singur fișier XLSX o dată și nu se pot amesteca fișiere XLSX cu alte formate.

#### 3. Dependențe

- `l10n_ro`
- `account_bank_statement_import_csv`

#### 4. Componente Cheie

**Modele**

- `base_import.import` (extindere, TransientModel): la `_parse_import_data` completează coloana `partner_id/.id` căutând partenerul după nume (`partner_name`, potrivire `=ilike`) sau, dacă lipsește, după referința comenzii de vânzare din `payment_ref` (căutare exactă în `sale.order`, cu partenerul comercial de facturare); pentru linii fără `payment_ref` pune „N/A”.
- `account.journal` (extindere): adaugă `XLSX` la formatele de import (dacă nu există deja) și suprascrie `_import_bank_statement`: validează restricțiile de mai sus; dacă un parser dedicat recunoaște fișierul, urmează fluxul standard de import; altfel deschide asistentul de mapare (`base_import.import`) prin acțiunea client `import_bank_stmt`, cu atașamentul (`attachment_ids`) transmis în context.

**Vizualizări**

Modulul nu adaugă vizualizări proprii; se bazează pe asistentul standard de import (`base_import.import`) din Odoo.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

- [l10n_ro_account_bank_statement_import_ing_csv](../l10n_ro_account_bank_statement_import_ing_csv/index.md): modul soră pentru importul fișierului CSV „Istoric conturi” ING Business, fără asistent de mapare.
- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md): parsere dedicate pentru fișiere de decontare XLSX/CSV; un fișier recunoscut de ele sare peste asistentul de mapare al acestui modul.
