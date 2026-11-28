# Bank Statement Foreign Currency (localizat la `deltatech_bank_stmt_foreign_currency/index.md`)

- **Nume Tehnic:** `deltatech_bank_stmt_foreign_currency`
- **Versiune:** `20.0.0.0.7`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_bank_stmt_foreign_currency
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_bank_stmt_foreign_currency`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul extinde importul extraselor bancare pentru a gestiona tranzacțiile efectuate în valută. Atunci când fișierul conține sume într-o monedă diferită de cea a jurnalului (sau a companiei), modulul realizează automat conversia pe baza cursului de schimb valabil la data tranzacției. Astfel, contabilii pot importa fără efort suplimentar extrase cu operațiuni multi-valutare, sumele fiind aduse corect în moneda de lucru.

#### 2. Funcționalități Cheie

- **Conversie valutară automată:** convertește sumele dintr-o valută străină în moneda jurnalului (sau a companiei) pe baza cursului de la data tranzacției; cursul trebuie să existe în Odoo pentru fiecare dată.
- **Suport multi-valutar:** permite importul fișierelor cu tranzacții în monede diferite, prin maparea câmpurilor `foreign_currency_id` (codul valutei) și `amount_currency` (suma în valuta originală, negativă pentru plăți).
- **Detectare îmbunătățită a partenerilor:** moștenește identificarea automată a partenerului (după nume sau după referința comenzii de vânzare) din modulul de bază.
- **Flux de import:** din tabloul de bord Contabilitate, meniul cardului jurnalului bancar → **Import File**; după maparea coloanelor, **Test** și **Import**. Jurnalul trebuie să aibă *Bank Feeds* pe importul manual.
- **Diferențe de curs:** la reconcilierea cu o factură emisă la alt curs, Odoo înregistrează automat diferența de curs.
- **Limitări:** se folosește cursul din Odoo, nu cel aplicat efectiv de bancă (soldul poate diferi); rândurile cu cod de valută necunoscut sau inactiv sunt sărite fără mesaj, iar coloana valutei nu poate fi prima; rândurile în moneda jurnalului cu valută externă identică sunt refuzate.

Fluxul pas cu pas, cu capturi, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md)

#### 4. Componente Cheie

Conform fișierului `readme/DESCRIPTION.md`, această secțiune nu a fost detaliată separat: descrierea acoperă scopul și funcționalitățile modulului fără a impune analiza componentelor tehnice. Modulul extinde mecanismul de import (`base_import.import`) din modulul de bază, logica fiind în directorul `wizard/`.

#### 5. Conexiuni

- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md): modulul de bază pe care îl extinde, oferind importul propriu-zis al extraselor bancare și detectarea automată a partenerilor.
