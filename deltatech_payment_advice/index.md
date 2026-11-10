# Payment Advice (localizat la `deltatech_payment_advice/index.md`)

- **Nume Tehnic:** `deltatech_payment_advice`
- **Versiune:** `19.0.1.0.6`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_payment_advice
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_payment_advice`
- **Ultima Ingestie:** `2026-11-10`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă un raport de tip **aviz de plată** (remittance advice) pe plata în lot din Odoo — documentul pe care plătitorul îl trimite furnizorilor pentru a-i notifica ce facturi le-au fost achitate printr-un ordin de plată bancar. Pornind de la o plată în lot, modulul grupează plățile pe furnizor și produce câte un aviz per furnizor, cu lista facturilor achitate și suma alocată fiecăreia; avizul poate fi tipărit ca PDF sau trimis direct pe e-mail furnizorului, eliminând nevoia de a comunica manual detaliile decontării.

#### 2. Funcționalități Cheie

- Adaugă un raport PDF de **Payment Advice** (aviz de plată) pe `account.batch.payment`.
- Grupează plățile din lot pe furnizor — se produce câte un document de aviz per furnizor.
- Listează facturile furnizor achitate (număr, dată, scadență) cu suma alocată fiecăreia: preluată din reconcilierea plății, când există; altfel, suma plății se repartizează pe facturile furnizorului în ordinea scadenței, fiecare factură primind cel mult restul ei de plată (astfel avizul poate fi emis înainte ca plata să fie reconciliată, iar o plată parțială apare cu suma efectiv plătită, nu cu totalul facturii). Un eventual excedent (avans) nu apare în aviz.
- Buton **Send Payment Advice** (Trimite avizul de plată) care trimite pe e-mail fiecărui furnizor propriul PDF de aviz, printr-un șablon de e-mail, omițând (și raportând) furnizorii fără adresă de e-mail.
- Randează și traduce avizul fiecărui furnizor — atât PDF-ul, cât și e-mailul — în limba respectivului furnizor.
- Antetul documentului este compania plătitoare.
- Cerințe: necesită `account_batch_payment` (plăți în lot, Odoo Enterprise); facturile listate sunt cele pentru care s-a înregistrat plata (de exemplu plăți create din facturile furnizor); reconcilierea nu este necesară pentru emiterea avizului.

#### 3. Dependențe

- `account_batch_payment`

#### 4. Componente Cheie

Sumar și Funcționalități Cheie provin din `readme/DESCRIPTION.md`; componentele de mai jos sunt doar un reper minim pentru navigare tehnică, verificat în `models/`, `views/`, `report/` și `data/`.

**Modele**

- `account.batch.payment` (extindere): `_get_advice_data()` grupează plățile lotului pe furnizor și calculează sumele alocate; `action_send_payment_advice()` generează PDF-ul per furnizor și îl trimite pe e-mail, raportând furnizorii fără adresă de e-mail.
- `account.payment` (extindere): `_deltatech_advice_bills()` identifică facturile furnizor (`in_invoice` / `in_refund`) la care se aplică plata; `_deltatech_advice_amounts()` calculează suma alocată fiecărei facturi (în moneda companiei); `_deltatech_allocated_amount()` o determină din reconcilierile parțiale ale plății.

**Vizualizări**

- `view_batch_payment_form_advice`: extinde formularul plății în lot (`account_batch_payment.view_batch_payment_form`) cu butonul „Send Payment Advice", vizibil doar pentru loturi de ieșire (`outbound`) cu plăți adăugate.
- `report_payment_advice` / `report_payment_advice_document`: șabloanele QWeb ale avizului de plată.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`. Modulul include raportul `action_report_payment_advice` și șablonul de e-mail `mail_template_payment_advice`, ambele declanșate manual (tipărire, respectiv butonul de trimitere).

#### 5. Conexiuni

- `account_batch_payment`: modulul de bază peste care se construiește avizul (dependență directă, listată și la secțiunea 3).
