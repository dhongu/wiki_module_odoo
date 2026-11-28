# Import fișiere extras bancar

- **Nume Tehnic:** `account_statement_import_file`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/dhongu/others_addons/tree/20.0/account_statement_import_file
- **Cale Locală:** `odoo-addons/others_addons/account_statement_import_file`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Oferă cadrul tehnic pentru importul extraselor bancare din fișiere. Este succesorul modulului `account_bank_statement_import`, care a făcut parte din Odoo Community până la v13 și a trecut în Enterprise din v14; a fost redenumit pentru a evita conflictul cu versiunea Enterprise. Formatele concrete (de exemplu OFX) se adaugă prin module separate specifice fiecărui format.

#### 2. Funcționalități Cheie

- Suport pentru fișiere de extras multi-cont (se creează mai multe extrase dintr-un singur fișier).
- Atașarea fișierului importat la extrasul bancar, pentru diagnosticare în caz de probleme.
- Mesaje de eroare îmbunătățite.
- Import din dashboard-ul Contabilitate: pe jurnalul bancar apare un buton de import; wizard-ul listează formatele de fișier suportate, iar butonul **Import** creează extrasul (sau extrasele).
- Tranzacțiile deja importate nu se creează a doua oară.
- Dacă fișierul conține contul bancar al contrapartidei și acesta există pe un partener din Odoo, partenerul este completat automat pe linia de extras (doar pentru formatele care oferă această informație).
- Modulul oferă doar cadrul: pentru formatele băncilor trebuie instalate module dedicate (ex. `account_statement_import_ofx`).

#### 3. Dependențe

- `account_statement_import_base`

#### 4. Componente Cheie

**Modele**

- `account.statement.import` (wizard): importă fișierul de extras și creează extrasele.
- `account.journal` (extins): acțiunea de import de pe dashboard.

**Vizualizări**

- `account_statement_import_form`: formularul wizard-ului de import.
- `journal_dashboard_view_inherit`: butonul de import pe jurnalul bancar din dashboard.

**Acțiuni Automate / Acțiuni Server**

- `account_statement_import_action` și meniul `account_statement_import_menu`: deschid wizard-ul de import.

#### 5. Conexiuni

- `account_statement_import_base`: cod comun al importului de extrase.
- `account_statement_import_ofx`: exemplu de modul de format specific (modul separat, fără pagină wiki).
