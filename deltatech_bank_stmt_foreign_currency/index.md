# Bank Statement Foreign Currency (localizat la `deltatech_bank_stmt_foreign_currency/index.md`)

- **Nume Tehnic:** `deltatech_bank_stmt_foreign_currency`
- **Versiune:** `19.0.0.0.2`
- **Cale:** https://github.com/terrabit-ro/bitshop_ent/tree/19.0/deltatech_bank_stmt_foreign_currency
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_bank_stmt_foreign_currency`
- **Ultima Ingestie:** `2026-06-09`

#### 1. Sumar

Acest modul extinde funcționalitatea de import al extraselor bancare pentru a gestiona tranzacțiile efectuate în valută. Atunci când extrasul conține sume într-o monedă diferită de cea a jurnalului (sau a companiei), modulul realizează automat conversia pe baza cursului de schimb valabil la data tranzacției. Astfel, contabilii pot importa fără efort suplimentar extrase cu operațiuni multi-valutare, sumele fiind aduse corect în moneda de lucru.

#### 2. Funcționalități Cheie

- **Conversie valutară automată:** convertește sumele dintr-o valută străină în moneda jurnalului (sau a companiei) pe baza cursului de schimb de la data tranzacției.
- **Suport multi-valutar:** permite importul fișierelor care conțin tranzacții în monede diferite, prin maparea câmpurilor `foreign_currency_id` și `amount_currency`.
- **Detectare îmbunătățită a partenerilor:** moștenește identificarea automată a partenerului (după nume sau după referința comenzii de vânzare) din modulul de bază.

#### 3. Dependențe

- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md)

#### 4. Componente Cheie

Conform fișierului `readme/DESCRIPTION.md`, această secțiune nu a fost detaliată separat: descrierea acoperă scopul și funcționalitățile modulului fără a impune analiza componentelor tehnice. Modulul extinde mecanismul de import al extraselor bancare din modulul de bază (logica fiind localizată în directorul `wizard/`).

#### 5. Conexiuni

- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md): modulul de bază pe care îl extinde, oferind importul propriu-zis al extraselor bancare și detectarea automată a partenerilor.
