# Card Payment Method

- **Nume Tehnic:** `deltatech_card_payment`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_card_payment
- **Cale Locală:** odoo-addons/deltatech/deltatech_card_payment
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Adaugă în contabilitate o metodă de plată generică „Card Payment”, care permite distingerea încasărilor prin card de celelalte plăți primite. Ajută la clasificarea mai bună a plăților și simplifică reconcilierea bancară pentru firmele cu multe tranzacții cu cardul.

#### 2. Funcționalități Cheie

- Creează automat metoda „Card Payment” (cod `card_payment`, tip încasare) între metodele de plată Odoo.
- Distinge clar plățile cu cardul de celelalte încasări.
- Metoda este disponibilă doar pe jurnale de tip bancă și este adăugată implicit la metodele de încasare ale jurnalelor noi.
- Se alege la înregistrarea plăților de la clienți sau la configurarea jurnalelor contabile, util în comerț și servicii.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.payment.method` (extins): înregistrează metoda `card_payment` ca metodă „multi”, limitată la jurnalele de tip bancă.
- `account.journal` (extins): adaugă metoda Card Payment la metodele de încasare implicite.

**Vizualizări**

- Nu are vizualizări.

**Acțiuni Automate / Acțiuni Server**

- `account_payment_method_card_in` (date): înregistrarea metodei de plată „Card Payment”.

#### 5. Conexiuni

- Nu are conexiuni funcționale verificate cu alte module cu pagină wiki.
