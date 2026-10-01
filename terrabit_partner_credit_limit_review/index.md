# Partner Credit Limit - Sale Order Review (localizat la `terrabit_partner_credit_limit_review/index.md`)

- **Nume Tehnic:** `terrabit_partner_credit_limit_review`
- **Versiune:** `19.0.0.1.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/terrabit_partner_credit_limit_review
- **Cale Locală:** `odoo-addons/bitshop/terrabit_partner_credit_limit_review`
- **Ultima Ingestie:** `2026-10-01`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul transformă verificările de limită de credit din `terrabit_partner_credit_limit` în motive de revizuire pe comanda de vânzare, în loc de o eroare afișată la apăsarea butonului Confirmă. O ofertă care depășește limita de credit a clientului sau care are facturi restante rămâne ofertă, iar motivul apare vizibil pe comandă. Un utilizator cu drept de aprobare o confirmă printr-un wizard, care păstrează cine a aprobat și de ce. Se instalează explicit, acolo unde se dorește fluxul de revizuire; cele două reguli livrate sunt inactive implicit.

#### 2. Funcționalități Cheie

- **Motive de revizuire pe poarta „înainte de confirmare":** *Credit limit exceeded* și *Overdue invoices*. Oferta afișează bannerul „Held for review", butonul inteligent *Reviews* și insigna *To Review* în lista de comenzi.
- **Confirmare controlată:** butonul **Confirm** deschide wizardul de aprobare pentru utilizatorii din grupul *Can approve sale order over credit limit*; ceilalți primesc un refuz cu lista motivelor, iar oferta rămâne neatinsă. Wizardul afișează motivele cu sumele și un câmp **Note**, care ajunge în chatter.
- **Derogarea existentă:** aprobarea bifează automat *Allow Over Credit?* pe comandă (fila *Other Info*); o comandă cu bifa activă nu mai primește motive de credit. Aprobatorii pot bifa câmpul și direct pe ofertă.
- **Reevaluare:** dacă valoarea comenzii crește după aprobare, motivul se redeschide; motivul pentru facturi restante se rezolvă singur după plata facturii.
- **Fluxuri automate** (ex. import marketplace): comanda rămâne ofertă cu motivele vizibile, în loc să pice pe eroarea de limită de credit (prin `_review_can_auto_confirm()`).
- **Excepții păstrate din modulul de bază:** echipă de vânzări cu *Ignore credit limits*, partener cu *Allow Over Credit?*, comenzi plătite.
- **Configurare:** regulile se activează din *Sales → Configuration → Order Review Rules*; grupul de aprobare al ambelor reguli este implicit *Can approve sale order over credit limit* și poate fi schimbat pe regulă. Limita, toleranța, zilele de clemență și modul de calcul al soldului se setează conform modulului `terrabit_partner_credit_limit` (partener, *Sales → Configuration → Settings*, echipă de vânzări).
- Utilizatorii din afara grupului de gestiune a limitelor văd și butonul **Req. confirm**, care creează o activitate pentru liderul echipei de vânzări.
- Fără acest modul, `terrabit_partner_credit_limit` funcționează independent, refuzând confirmarea cu mesajul de limită de credit.
- Flux pas-cu-pas, cu capturi: vezi [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- [terrabit_partner_credit_limit](../terrabit_partner_credit_limit/index.md)
- [deltatech_sale_order_review](../deltatech_sale_order_review/index.md)

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): `_review_check_credit_limit` și `_review_check_overdue_invoices` sunt verificările apelate de regulile de revizuire; folosesc `check_limit()` și `get_overdue_invoices()` din modulul de bază, respectă `can_skip_credit_limit()` și rulează cu `sudo()` pentru că soldul clientului nu e lizibil pentru vânzător.
- `sale.order.review.reason` (extins): `action_approve` bifează `allow_overcredit` pe comandă după aprobarea unui motiv `credit_limit` sau `overdue_invoices`.

**Vizualizări**

- Modulul nu definește vizualizări proprii; folosește bannerul, butonul *Reviews* și wizardul de aprobare din `deltatech_sale_order_review`.

**Acțiuni Automate / Acțiuni Server**

- Nu are cron-uri sau acțiuni server. Livrează două înregistrări `sale.order.review.rule` (`rule_credit_limit`, `rule_overdue_invoices`; poarta `confirm`, tip `manual`, secvențe 80 și 81), **inactive** implicit.

#### 5. Conexiuni

- [terrabit_partner_credit_limit_website](../terrabit_partner_credit_limit_website/index.md): extinde același modul de bază către website; nu interacționează direct cu acest modul.
