# Deltatech Payment Advice (localizat la `deltatech_payment_advice/index.md`)

- **Nume Tehnic:** `deltatech_payment_advice`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/bitshop_ent/tree/19.0/deltatech_payment_advice
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_payment_advice`
- **Ultima Ingestie:** `2026-07-31`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă un raport de tip **aviz de plată** (remittance advice) pe plata în lot din Odoo — documentul pe care plătitorul îl trimite furnizorilor pentru a-i notifica ce facturi le-au fost achitate printr-un ordin de plată bancar. Pornind de la o plată în lot, modulul grupează plățile pe furnizor și produce câte un aviz per furnizor, cu lista facturilor achitate și suma alocată fiecăreia; avizul poate fi tipărit ca PDF sau trimis direct pe e-mail furnizorului, eliminând nevoia de a comunica manual detaliile decontării.

#### 2. Funcționalități Cheie

- Adaugă un raport PDF de **Aviz de plată** pe `account.batch.payment`.
- Grupează plățile din lot pe furnizor — se produce câte un document de aviz per furnizor.
- Listează facturile furnizor achitate (număr, dată, scadență) cu suma efectiv alocată fiecăreia, calculată din reconcilierea plății atunci când este disponibilă, altfel din valoarea brută a facturii (astfel avizul poate fi emis chiar înainte ca plata să fie complet reconciliată).
- Buton **Trimite avizul de plată** care trimite pe e-mail fiecărui furnizor propriul PDF de aviz, printr-un șablon de e-mail, omițând (și raportând) furnizorii fără adresă de e-mail.
- Randează și traduce avizul fiecărui furnizor — atât PDF-ul, cât și e-mailul — în limba respectivului furnizor.
- Antetul documentului este compania plătitoare.

#### 3. Dependențe

- `account_batch_payment`

#### 4. Componente Cheie

*Notă: conform priorității Readme, componentele tehnice nu au fost extrase din cod pentru această pagină; secțiunea de mai jos oferă doar un reper minim util pentru navigare tehnică.*

**Modele**

- `account.batch.payment` (extindere): metoda `_get_advice_data()` grupează plățile lotului pe furnizor și calculează sumele alocate; `action_send_payment_advice()` generează PDF-ul per furnizor și îl trimite pe e-mail, raportând furnizorii fără adresă de e-mail.
- `account.payment` (extindere): `_deltatech_advice_bills()` identifică facturile furnizor stinse de plată; `_deltatech_allocated_amount()` calculează suma efectiv alocată unei facturi din reconcilierile parțiale ale plății.

**Vizualizări**

- `view_batch_payment_form_advice`: extinde formularul plății în lot (`account_batch_payment.view_batch_payment_form`) cu butonul „Send Payment Advice", vizibil doar pentru loturi de ieșire (`outbound`) cu plăți adăugate.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul. Modulul include un raport (`action_report_payment_advice`) și un șablon de e-mail (`mail_template_payment_advice`), ambele declanșate manual de utilizator (tipărire, respectiv butonul de trimitere).

#### 5. Conexiuni

- `account_batch_payment`: modulul de bază peste care se construiește avizul (dependență directă, listată și la secțiunea 3).
- `terrabit_inedit`: modulul de proiect al clientului Inedit Venture, la a cărui cerere a fost dezvoltat `deltatech_payment_advice`; `terrabit_inedit` are acest modul în propriile dependențe.
