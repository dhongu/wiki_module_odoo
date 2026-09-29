# Limită de Credit pe Partener (localizat la `terrabit_partner_credit_limit/index.md`)

- **Nume Tehnic:** `terrabit_partner_credit_limit`
- **Versiune:** `19.0.1.4.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/terrabit_partner_credit_limit
- **Cale Locală:** `odoo-addons/bitshop/terrabit_partner_credit_limit`
- **Ultima Ingestie:** `2026-09-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul implementează un sistem de gestionare a limitelor de credit pentru partenerii de afaceri. Permite stabilirea și aplicarea limitelor de credit clienților, ajutând la administrarea riscului financiar și la controlul creanțelor. La confirmarea unei comenzi de vânzare care depășește limita (plus toleranța admisă), confirmarea este refuzată cu mesajul limitei de credit; un utilizator cu drept de aprobare poate acorda derogarea bifând „Allow Over Credit?" pe comandă. Integrarea cu fluxul de verificări al comenzii (motive de verificare, banner, wizard de aprobare din `deltatech_sale_order_review`) a fost mutată în modulul separat `terrabit_partner_credit_limit_review`, care se instalează explicit. Modulul este util companiilor care oferă termene de plată clienților și doresc să își gestioneze expunerea pe creanțe.

#### 2. Funcționalități Cheie

- Stabilește o limită de credit pe partener; când soldul de încasat plus comanda curentă depășesc limita plus toleranța admisă, confirmarea comenzii este refuzată cu mesajul limitei de credit (`UserError`, cu telefonul departamentului contabil).
- Permite marcarea anumitor parteneri pentru a ignora limitele de credit („Allow Over Credit?" pe partener) și definirea unor „zile de grație" (`Clemency Days`) înainte ca o factură scadentă să conteze drept restantă.
- Introduce grupuri de acces pentru utilizatori:
  - „Manage credit limits" — permite editarea limitei de credit, a „Allow Over Credit?" și a zilelor de grație de pe partener; nu ocolește verificarea la confirmarea comenzii și nu vede butonul „Req. confirm".
  - „Can approve sale order over credit limit" — permite derogarea prin bifarea „Allow Over Credit?" (fila Other Info) pe comanda de vânzare.
- Pentru utilizatorii fără grupul „Manage credit limits", pe ofertă apare butonul „Req. confirm", care deschide o activitate (`mail.activity`) către responsabilul echipei de vânzări, ca flux alternativ de aprobare.
- Permite exceptarea anumitor echipe de vânzări de la verificarea limitei de credit (opțiunea „Ignore credit limits").
- Parametri globali configurabili din **Vânzări → Configurare → Setări**: toleranța admisă (`credit_limit.tolerance`), telefonul departamentului contabil afișat în mesajul de eroare și sărirea verificării pentru termene de plată imediate (`credit_limit.skip_term_immediate`).
- Calcul flexibil al creditului bazat pe parametri de sistem:
  - `credit_limit_from_invoices` — dacă este `False` (implicit), creditul se calculează din liniile de cont (account move lines); dacă este `True`, creditul se calculează din facturi (facturile trebuie să fie plătite).
  - `credit_limit_check_supplier_invoices` (necesită `credit_limit_from_invoices = True`) — dacă este `False` (implicit), creditul se calculează doar din facturile sau notele de credit ale clientului; dacă este `True`, din toate facturile sau notele de credit.
  - `skip_only_card` — limitează sărirea verificării doar la tranzacțiile plătite altfel decât cu cardul.
- `can_skip_credit_limit()` și `action_confirm()` (prin `check_limit()`) rulează cu `sudo`, ca să nu dea eroare de acces unui vânzător fără drepturi pe `payment.transaction` / `partner.credit`.
- Fluxul cu motive de verificare pe comandă (regulile „Limită de credit depășită" și „Facturi restante", banner, wizard de aprobare, integrarea cu importul din marketplace) nu mai face parte din acest modul: este oferit de `terrabit_partner_credit_limit_review`, instalat explicit. Migrarea predă cele două reguli (`rule_credit_limit`, `rule_overdue_invoices`) către xml id-urile punții, fără ștergere sau duplicare.

Beneficii de afaceri: reducerea riscului financiar prin control automat al creditului, gestionarea mai bună a fluxului de numerar, abordare structurată a creditului clienților, prevenirea expunerii excesive față de clienții cu risc ridicat și fluxuri de aprobare personalizabile pentru depășirea limitelor.

#### 3. Dependențe

- `account_payment`
- `sale_management`
- [terrabit_partner_payable_receivable](../terrabit_partner_payable_receivable/index.md)

#### 4. Componente Cheie

Documentația acestei secțiuni se bazează pe `readme/DESCRIPTION.md` și pe fișa consultant, care nu detaliază componentele tehnice individuale; analiza codului a fost omisă conform fluxului de ingestie. Notă de fapt: `data/ir.config_parameter.xml` definește parametrii `credit_limit.skip_term_immediate`, `credit_limit.accounting_phone` și `credit_limit.tolerance`. Începând cu 19.0.1.4.0 modulul nu mai definește reguli `sale.order.review.rule`; acestea aparțin punții `terrabit_partner_credit_limit_review`.

#### 5. Conexiuni

- [terrabit_partner_payable_receivable](../terrabit_partner_payable_receivable/index.md): modul înrudit (și dependență) din suita terrabit care stă la baza calculului de plăți/încasări pe partener, folosit de logica de limită de credit.
- `terrabit_partner_credit_limit_review`: punte separată (instalată explicit) care integrează limita de credit și facturile restante ca motive de verificare în [deltatech_sale_order_review](../deltatech_sale_order_review/index.md); a preluat regulile și fișa consultant bazată pe verificări.
- `sales_team` (`crm.team`): oferă excepția „Ignore credit limits" pe echipă de vânzări.
- `mail`: susține activitatea de solicitare de aprobare (butonul „Req. confirm").
