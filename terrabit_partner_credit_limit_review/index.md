# Partner Credit Limit - Sale Order Review

- **Nume Tehnic:** `terrabit_partner_credit_limit_review`
- **Versiune:** `20.0.0.2.8`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/terrabit_partner_credit_limit_review
- **Cale Locală:** `odoo-addons/bitshop/terrabit_partner_credit_limit_review`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Afișează verificările de limită de credit din [terrabit_partner_credit_limit](../terrabit_partner_credit_limit/index.md) ca motive de revizuire a comenzii de vânzare ([deltatech_sale_order_review](../deltatech_sale_order_review/index.md)), în loc de o eroare la apăsarea butonului Confirm. Se instalează explicit, unde se dorește revizuirea; cele două reguli livrate sunt **inactive**. Fără acest modul, `terrabit_partner_credit_limit` funcționează singur și refuză confirmarea cu mesajul de limită de credit.

#### 2. Funcționalități Cheie

- **Credit limit exceeded** și **Overdue invoices** devin motive pe poarta *înainte de confirmare*: oferta arată de ce este oprită, în banner și în coada *To Review*.
- Butonul **Confirm** deschide wizardul de aprobare pentru utilizatorii grupului *Can approve sale order over credit limit* și refuză ceilalți utilizatori, afișând lista motivelor. Aprobarea setează *Allow Over Credit?* pe comandă, derogarea existentă în modulul de limită de credit.
- Fluxurile automate (import marketplace) întreabă `_review_can_auto_confirm()` și lasă comanda ofertă cu motivele vizibile, în loc să eșueze cu eroarea de limită.
- Excepțiile modulului de limită rămân: echipă de vânzări cu *Ignore credit limits*, partener cu *Allow Over Credit?*, comenzi cu tranzacție de plată (care contează depinde de setarea *Orders with a Payment Transaction*).
- Configurare: *Sales → Configuration → Order Review Rules*, activarea regulilor; grupul de aprobare e implicit *Can approve sale order over credit limit*, schimbabil pe regulă.
- Modulul este plătit în Odoo Apps (40 EUR).

#### 3. Dependențe

- [terrabit_partner_credit_limit](../terrabit_partner_credit_limit/index.md)
- [deltatech_sale_order_review](../deltatech_sale_order_review/index.md)

#### 4. Componente Cheie

**Modele**

- `sale.order.review.reason`: extins cu motivele de limită de credit și facturi restante.
- `sale.order`: Confirm trece prin revizuire; `_review_can_auto_confirm()` pentru fluxurile automate.

**Vizualizări**

- Nu are vizualizări proprii.

**Acțiuni Automate / Acțiuni Server**

- `data/review_rule_data.xml`: regulile `rule_credit_limit` și `rule_overdue_invoices` (poartă *confirm*, tip manual, inactive la instalare).

#### 5. Conexiuni

- [terrabit_partner_credit_limit](../terrabit_partner_credit_limit/index.md): sursa verificărilor.
- [deltatech_sale_order_review](../deltatech_sale_order_review/index.md): mecanismul de revizuire.
