# Limită de Credit pe Partener (localizat la `terrabit_partner_credit_limit/index.md`)

- **Nume Tehnic:** `terrabit_partner_credit_limit`
- **Versiune:** `19.0.1.3.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/terrabit_partner_credit_limit
- **Cale Locală:** `odoo-addons/bitshop/terrabit_partner_credit_limit`
- **Ultima Ingestie:** `2026-09-24`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul implementează un sistem robust de gestionare a limitelor de credit pentru partenerii de afaceri. Permite organizațiilor să stabilească și să aplice limite de credit clienților, ajutând la administrarea riscului financiar și la controlul eficient al creanțelor. Depășirea limitei de credit și facturile restante devin **motive de verificare** pe comanda de vânzare (poarta *Înainte de confirmare* din [deltatech_sale_order_review](../deltatech_sale_order_review/index.md)): oferta rămâne ofertă, arată într-un banner motivele, iar un utilizator cu drept de aprobare confirmă printr-un wizard care înregistrează cine și de ce a aprobat derogarea. Modulul este util în special pentru companiile care oferă termene de plată clienților și care doresc să își gestioneze responsabil expunerea pe creanțe.

#### 2. Funcționalități Cheie

- Stabilește o limită de credit pe partener; când soldul de încasat plus comanda curentă depășesc limita plus toleranța admisă, comanda primește motivul de verificare „Limită de credit depășită" și rămâne ofertă (badge „De verificat"), în loc să fie blocată direct la confirmare.
- A doua regulă de verificare, „Facturi restante", se declanșează când clientul are facturi scadente (peste zilele de grație) cu sold neîncasat peste toleranță; se rezolvă automat la următoarea reevaluare, după încasare.
- Permite marcarea anumitor parteneri pentru a ignora limitele de credit (opțiunea „Allow Over Credit?" de pe partener) și definirea unor „zile de grație" (`Clemency Days`) înainte ca o factură scadentă să conteze drept restantă.
- Introduce grupuri de acces pentru utilizatori:
  - „Manage credit limits" — permite editarea limitei de credit, a „Allow Over Credit?" și a zilelor de grație de pe partener; nu ocolește verificarea la confirmarea comenzii și nu vede butonul „Req. confirm".
  - „Can approve sale order over credit limit" — grupul de aprobare al celor două reguli de verificare; la **Confirmă**, wizardul de aprobare din [deltatech_sale_order_review](../deltatech_sale_order_review/index.md) i se deschide lui, aprobarea bifând automat „Allow Over Credit?" pe comandă.
- Pentru utilizatorii fără grupul „Manage credit limits", cât timp există motive deschise pe ofertă, apare butonul „Req. confirm", care deschide o activitate (`mail.activity`) către responsabilul echipei de vânzări, ca flux alternativ de aprobare.
- Permite exceptarea anumitor echipe de vânzări de la verificarea limitei de credit (opțiunea „Ignore credit limits").
- Fluxurile automate (ex. importul din marketplace) interoghează `_review_can_auto_confirm()` și lasă oferta cu motivele vizibile, în loc să eșueze cu `UserError`; `UserError`-ul rămâne ultima gardă la `action_confirm()` pentru un utilizator fără grupul de aprobare care ocolește butonul Confirmă.
- Parametri globali configurabili din **Vânzări → Configurare → Setări**: toleranța admisă (`credit_limit.tolerance`), telefonul departamentului contabil afișat în mesajul de eroare și sărirea verificării pentru termene de plată imediate (`credit_limit.skip_term_immediate`).
- Calcul flexibil al creditului bazat pe parametri de sistem:
  - `credit_limit_from_invoices` — dacă este `False` (implicit), creditul se calculează din liniile de cont (account move lines); dacă este `True`, creditul se calculează din facturi (facturile trebuie să fie plătite).
  - `credit_limit_check_supplier_invoices` (necesită `credit_limit_from_invoices = True`) — dacă este `False` (implicit), creditul se calculează doar din facturile sau notele de credit ale clientului; dacă este `True`, creditul se calculează din toate facturile sau notele de credit.
  - `skip_only_card` — limitează sărirea verificării doar la tranzacțiile plătite altfel decât cu cardul.
- `check_limit()` și `can_skip_credit_limit()` rulează cu `sudo` pe verificările de plăți, ca să nu dea eroare de acces unui vânzător fără drepturi pe `payment.transaction` / `partner.credit`.

Beneficii de afaceri: reducerea riscului financiar prin control automat al creditului, gestionarea mai bună a fluxului de numerar, abordare structurată a creditului clienților, prevenirea expunerii excesive față de clienții cu risc ridicat și fluxuri de aprobare personalizabile pentru depășirea limitelor, integrate în fluxul unic de verificări al comenzilor.

#### 3. Dependențe

- `account_payment`
- `sale_management`
- [terrabit_partner_payable_receivable](../terrabit_partner_payable_receivable/index.md)
- [deltatech_sale_order_review](../deltatech_sale_order_review/index.md)

#### 4. Componente Cheie

Documentația acestei secțiuni se bazează pe fișierul `readme/DESCRIPTION.md` și pe fișa consultant, care nu detaliază componentele tehnice individuale. Conform fluxului de ingestie, analiza codului pentru Modele, Vizualizări și Acțiuni Automate a fost omisă întrucât Readme-ul este prezent. Notă de fapt din `data/review_rule_data.xml`: modulul definește două reguli `sale.order.review.rule` — `rule_credit_limit` (cod `credit_limit`) și `rule_overdue_invoices` (cod `overdue_invoices`), ambele pe poarta `confirm`, tip `manual`, cu grupul de aprobare „Can approve sale order over credit limit".

#### 5. Conexiuni

- [terrabit_partner_payable_receivable](../terrabit_partner_payable_receivable/index.md): modul înrudit (și dependență) din suita terrabit care stă la baza calculului de plăți/încasări pe partener, folosit de logica de limită de credit.
- [deltatech_sale_order_review](../deltatech_sale_order_review/index.md) (dependență): furnizează motorul de motive de verificare pe comandă (banner, badge „De verificat", wizard de aprobare, `_review_can_auto_confirm()`) pe care se bazează cele două reguli ale acestui modul.
- `sales_team` (`crm.team`): oferă excepția „Ignore credit limits" pe echipă de vânzări.
- `mail`: susține activitatea de solicitare de aprobare (butonul „Req. confirm").
- `deltatech_marketplace_sale`: la import, lasă comanda ofertă cu motivele vizibile în loc să eșueze la confirmare, când este instalat.
