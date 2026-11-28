# Sale Payment (localizat la `deltatech_sale_payment/index.md`)

- **Nume Tehnic:** `deltatech_sale_payment`
- **Versiune:** `20.0.1.3.5`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_payment`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_payment`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Echipa de vânzări vede direct din comandă dacă clientul a plătit. Modulul adaugă pe comenzile de vânzare suma încasată și o stare a plății, și permite agentului de vânzări să înregistreze o plată fără drepturi de facturare.

#### 2. Funcționalități Cheie

- Pe formular apar **Payment** (suma încasată), **Provider** și **Payment Status**.
- Șapte stări: *Without*, *Initiated*, *Pending*, *Authorized*, *Partial*, *Done*, *Cancelled*; vizibile implicit în listele de oferte și comenzi, cu filtre și grupare.
- Acțiunea **Confirm Payment** a comenzii deschide o fereastră pornind de la ultima tranzacție în ciornă sau în așteptare, ori de la suma rămasă; se alege furnizorul, metoda, suma și **Payment Date**.
- **Confirm** marchează tranzacția ca finalizată și reține data pe comandă (Odoo poate apoi confirma oferta); **Add** doar înregistrează o tranzacție în așteptare.
- Protecții: fereastra cere drept de scriere pe comandă (nu drepturi de facturare) și refuză suma negativă, plata autorizată, tranzacția altei comenzi, furnizorul altei companii și metoda neoferită de furnizor.
- Un furnizor al cărui jurnal nu are metodă de plată (ex. transfer bancar) nu generează plată contabilă; o înregistrează contabilul.

#### 3. Dependențe

- `sale`
- `payment`
- `account_payment`

#### 4. Componente Cheie

**Modele**

- `sale.order`: câmpurile calculate `provider_id`, `payment_amount`, `payment_status` (`_compute_payment`) și `action_payment_link`.
- `sale.confirm.payment` (tranzitoriu): asistentul de confirmare cu `do_add_payment` și `do_confirm`.
- `payment.transaction`: `_should_create_payment` și `_create_payment` adaptate.

**Vizualizări**

- `view_order_form`: câmpurile de plată pe comandă.
- `view_quotation_tree` / `view_order_tree`: coloanele furnizor și stare plată.
- `view_sales_order_filter`: filtre după starea plății.
- `view_sale_confirm_payment_form`: formularul asistentului.

**Acțiuni Automate / Acțiuni Server**

- `action_sale_confirm_payment`: acțiune contextuală pe `sale.order` care deschide fereastra „Confirm Payment".

#### 5. Conexiuni

- `payment`: folosește `payment.provider`, `payment.transaction` și `payment.method`.
- `account_payment`: legătura cu plata contabilă.
- `sale`: comanda este documentul pe care se urmărește plata.
