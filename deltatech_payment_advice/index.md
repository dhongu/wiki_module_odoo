# Payment Advice (localizat la `deltatech_payment_advice/index.md`)

- **Nume Tehnic:** `deltatech_payment_advice`
- **Versiune:** `20.0.1.0.5`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_payment_advice
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_payment_advice`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă un raport de tip **aviz de plată** (remittance advice) pe plata în lot din Odoo, adică documentul pe care plătitorul îl trimite furnizorilor ca să le comunice ce facturi le-au fost achitate printr-un ordin de plată bancar. Pornind de la o plată în lot, modulul grupează plățile pe furnizor și produce câte un aviz per furnizor, cu facturile achitate și suma alocată fiecăreia. Avizul poate fi tipărit ca PDF sau trimis direct pe e-mail furnizorului.

#### 2. Funcționalități Cheie

- Raport PDF **Aviz de plată** pe `account.batch.payment`, cu câte un document per furnizor.
- Listează facturile furnizor achitate (număr, dată, scadență) cu suma alocată fiecăreia: din reconcilierea plății, când există; altfel suma plății este distribuită pe facturile furnizorului în ordinea scadenței, fiecare primind cel mult restul de plată, deci avizul se poate emite înainte de reconciliere.
- Butonul **Trimite avizul de plată** trimite pe e-mail fiecărui furnizor propriul PDF, printr-un șablon de e-mail, omițând (și raportând) furnizorii fără adresă de e-mail.
- Avizul (PDF și e-mail) este randat și tradus în limba fiecărui furnizor.
- Antetul documentului este compania plătitoare.
- Facturile listate sunt cele pentru care s-a înregistrat plata (de exemplu plăți create din facturile furnizor); reconcilierea nu este obligatorie.

Fluxul pas-cu-pas, cu capturi, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account_batch_payment`

#### 4. Componente Cheie

*Notă: conform priorității Readme, componentele nu au fost analizate exhaustiv în cod; mai jos sunt doar repere de navigare.*

**Modele**

- `account.batch.payment` (extins): `_get_advice_data()` grupează plățile pe furnizor și calculează sumele alocate; `action_send_payment_advice()` generează PDF-ul per furnizor și îl trimite pe e-mail.
- `account.payment` (extins): `_deltatech_advice_bills()`, `_deltatech_advice_amounts()` și `_deltatech_allocated_amount()` identifică facturile achitate și suma alocată fiecăreia.

**Vizualizări**

- `view_batch_payment_form_advice`: adaugă butonul „Send Payment Advice" pe formularul plății în lot.
- `report_payment_advice` / `report_payment_advice_document`: șabloanele QWeb ale avizului.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`. Modulul include raportul `action_report_payment_advice` și șablonul de e-mail `mail_template_payment_advice`, declanșate manual (tipărire, respectiv butonul de trimitere).

#### 5. Conexiuni

- `account_batch_payment`: plata în lot din Enterprise, peste care se construiește avizul (dependență directă).
