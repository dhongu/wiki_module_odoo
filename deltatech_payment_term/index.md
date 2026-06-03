# Asistent Generare Rate Termen de Plată (localizat la `deltatech_payment_term/index.md`)

- **Nume Tehnic:** `deltatech_payment_term`
- **Versiune:** `19.0.2.0.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_payment_term`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_payment_term`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul simplifică crearea termenilor de plată în rate, eliminând introducerea manuală a fiecărei linii de scadență. Printr-un asistent dedicat, utilizatorul stabilește numărul de rate, eventualul avans și ziua de scadență din lună, iar modulul generează automat liniile termenului de plată cu sumele distribuite proporțional. În plus, facturile, comenzile de vânzare și partenerii primesc indicatori și butoane care evidențiază rapid documentele plătibile în rate.

#### 2. Funcționalități Cheie

- Generarea automată a ratelor (liniilor) unui termen de plată printr-un asistent.
- Definirea avansului și a numărului de rate, cu distribuirea procentuală sau pe sumă fixă a valorilor.
- Configurarea zilei din lună la care devin scadente ratele.
- Indicator pe comanda de vânzare și pe factură care semnalează dacă documentul este plătit în rate.
- Buton statistic „Rates” pe partener și pe factură pentru vizualizarea rapidă a documentelor cu plata în rate.

#### 3. Dependențe

- `account`
- `sale`

#### 4. Componente Cheie

**Modele**

- `account.payment.term.rate.wizard`: Asistent tranzitoriu care construiește liniile termenului de plată (avans + rate) pe baza numărului de rate, a tipului de valoare (procent sau sumă fixă) și a zilei de scadență; poate crea un termen nou sau rescrie liniile unuia existent.
- `account.move` (extins): Adaugă câmpul calculat `in_rates` (factura are termen cu mai multe linii) și acțiunea `view_rate` pentru afișarea documentelor în rate.
- `sale.order` (extins): Adaugă câmpul calculat `sale_in_rates` care indică dacă comanda folosește un termen de plată cu mai multe linii.
- `res.partner` (extins): Adaugă acțiunea `view_rate` pentru vizualizarea facturilor/documentelor în rate ale partenerului.

**Vizualizări**

- `view_account_payment_term_rate_wizard_form`: Formularul asistentului de generare rate (nume, tip, zi din lună, număr rate, avans).
- `view_payment_term_form`: Extinde formularul termenului de plată cu butonul de antet „Create Rate”.
- `view_order_form`: Adaugă indicatorul `sale_in_rates` lângă termenul de plată pe comanda de vânzare.
- `invoice_form1`: Adaugă pe factură indicatorul `in_rates` și butonul statistic „Rates”.
- `view_partner_form`: Adaugă butonul statistic „Rates” pe formularul partenerului.

**Acțiuni Automate / Acțiuni Server**

- `action_sale_payment_term_rate_wizard`: Acțiune contextuală (binding pe `sale.order`) care lansează asistentul de generare rate.
- `action_account_payment_term_rate_wizard`: Acțiune contextuală (binding pe `account.move`) care lansează asistentul de generare rate.

#### 5. Conexiuni

- `account`: modulul extinde termenul de plată și factura, generând liniile termenului de plată standard Odoo.
- `sale`: modulul marchează comenzile de vânzare plătibile în rate.
