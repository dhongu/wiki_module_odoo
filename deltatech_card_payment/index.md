# Deltatech Payment Method Card

- **Nume Tehnic:** `deltatech_card_payment`
- **Versiune:** `19.0.1.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_card_payment
- **Cale Locală:** `odoo-addons/deltatech/deltatech_card_payment`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul adaugă în configurarea contabilă o metodă de plată generică „Card Payment”, pentru încasări. Astfel plățile făcute cu cardul pot fi clasificate și urmărite separat de celelalte încasări, iar reconcilierea bancară este simplificată pentru firmele care procesează multe tranzacții cu cardul (retail, servicii).

#### 2. Funcționalități Cheie

- Creează automat metoda de plată „Card Payment” (cod `card_payment`), de tip încasare (inbound).
- Permite distingerea clară a încasărilor cu cardul de celelalte tipuri de încasări.
- Metoda este disponibilă doar pe jurnale de tip bancă, în mod „multi” (poate fi folosită pe mai multe jurnale).
- Jurnalele noi primesc implicit metoda „Card Payment” printre metodele de încasare.
- Metoda poate fi selectată la înregistrarea plăților clienților sau în configurarea jurnalelor.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.payment.method` (extins): înregistrează metoda `card_payment` (mod `multi`, domeniu: jurnale de tip `bank`).
- `account.journal` (extins): `_default_inbound_payment_methods` adaugă metoda „Card Payment” la valorile implicite.

**Vizualizări**

- Modulul nu definește vizualizări.

**Acțiuni Automate / Acțiuni Server**

- Nu există. Modulul încarcă doar înregistrarea `account_payment_method_card_in` (`data/account_data.xml`).

#### 5. Conexiuni

- [deltatech_payment_card_dummy](../deltatech_payment_card_dummy/index.md): modul înrudit tematic (plăți cu cardul); fără dependență în cod.
- `terrabit_ridacon`: modul client (proiecte/ridacon) care depinde de acest modul.
