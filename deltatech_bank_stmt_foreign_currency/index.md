# Bank Statement Foreign Currency (localizat la `deltatech_bank_stmt_foreign_currency/index.md`)

- **Nume Tehnic:** `deltatech_bank_stmt_foreign_currency`
- **Versiune:** `19.0.0.0.7`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_bank_stmt_foreign_currency
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_bank_stmt_foreign_currency`
- **Ultima Ingestie:** `2026-11-02`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul extinde importul extraselor bancare pentru tranzacțiile efectuate în valută. Când extrasul conține sume într-o monedă diferită de cea a jurnalului (sau a companiei), modulul le convertește automat pe baza cursului de schimb de la data tranzacției. Astfel, contabilii importă fără efort suplimentar extrase cu operațiuni multi-valutare, iar sumele sunt aduse corect în moneda de lucru. Este în uz la clienți de mult timp și are statutul de dezvoltare Production/Stable.

#### 2. Funcționalități Cheie

- **Conversie valutară automată**: convertește sumele din valută străină în moneda jurnalului (sau a companiei) pe baza cursului de schimb de la data tranzacției.
- **Suport multi-valutar**: permite importul fișierelor cu tranzacții în monede diferite, prin maparea câmpurilor `foreign_currency_id` (moneda tranzacției) și `amount_currency` (suma în acea monedă); suma convertită se completează în coloana `amount`.
- **Doar pentru importurile care au nevoie**: sunt pre-procesate numai importurile de extrase bancare din CSV, cu o coloană de monedă străină mapată; orice alt import (importuri obișnuite, extrase cu debit/credit sau doar cu sumă) folosește parsarea standard, deci datele, numerele localizate și valorile relaționale sunt normalizate ca fără modul.
- **Detectare îmbunătățită a partenerilor**: moștenește identificarea automată a partenerului (după nume sau după referința comenzii de vânzare) din modulul de bază.

#### 3. Dependențe

- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md)

#### 4. Componente Cheie

**Modele**

- `base_import.import`: extins (în `wizard/account_bank_statement_import_csv.py`) cu pre-procesarea datelor importate: pentru liniile cu monedă străină, convertește `amount_currency` în moneda jurnalului sau a companiei, la cursul de la data liniei, și completează `amount`.

**Vizualizări**

- Modulul nu definește vizualizări; lucrează prin ecranul standard de import al extraselor bancare.

**Acțiuni Automate / Acțiuni Server**

- Nu există acțiuni `ir.cron`, `base.automation` sau `ir.actions.server` definite în acest modul.

#### 5. Conexiuni

- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md): modulul de bază pe care îl extinde, oferind importul propriu-zis al extraselor bancare și detectarea automată a partenerilor.
