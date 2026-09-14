# Limită de Credit pe Partener (localizat la `terrabit_partner_credit_limit/index.md`)

- **Nume Tehnic:** `terrabit_partner_credit_limit`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/terrabit_partner_credit_limit
- **Cale Locală:** `odoo-addons/bitshop/terrabit_partner_credit_limit`
- **Ultima Ingestie:** `2026-09-14`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul implementează un sistem robust de gestionare a limitelor de credit pentru partenerii de afaceri. Permite organizațiilor să stabilească și să aplice limite de credit clienților, ajutând la administrarea riscului financiar și la controlul eficient al creanțelor. Atunci când limita de credit a unui client este depășită, comenzile de vânzare nu mai pot fi confirmate, oferind un control automat asupra expunerii la credit. Modulul este util în special pentru companiile care oferă termene de plată clienților și care doresc să își gestioneze responsabil expunerea pe creanțe.

#### 2. Funcționalități Cheie

- Stabilește o limită de credit pe partener; comenzile de vânzare nu pot fi confirmate dacă limita de credit plus toleranța admisă este depășită.
- Permite marcarea anumitor parteneri pentru a ignora limitele de credit (opțiunea „Allow Over Credit?" de pe partener) și definirea unor „zile de grație" (`Clemency Days`) înainte ca o factură scadentă să conteze drept restantă.
- Introduce grupuri de acces pentru utilizatori:
  - „Manage credit limits" — permite editarea limitei de credit, a „Allow Over Credit?" și a zilelor de grație de pe partener; nu ocolește însă blocajul la confirmarea comenzii.
  - „Can approve sale order over credit limit" — singurul grup care ocolește verificarea la confirmarea comenzii și poate bifa „Allow Over Credit?" direct pe comanda de vânzare.
- Pentru utilizatorii fără grupul „Manage credit limits", la depășirea limitei apare pe comandă butonul „Req. confirm", care deschide o activitate (`mail.activity`) către responsabilul echipei de vânzări, ca flux alternativ de aprobare.
- Permite exceptarea anumitor echipe de vânzări de la verificarea limitei de credit (opțiunea „Ignore credit limits").
- Parametri globali configurabili din **Vânzări → Configurare → Setări**: toleranța admisă (`credit_limit.tolerance`), telefonul departamentului contabil afișat în mesajul de eroare și sărirea verificării pentru termene de plată imediate (`credit_limit.skip_term_immediate`).
- Calcul flexibil al creditului bazat pe parametri de sistem:
  - `credit_limit_from_invoices` — dacă este `False` (implicit), creditul se calculează din liniile de cont (account move lines); dacă este `True`, creditul se calculează din facturi (facturile trebuie să fie plătite).
  - `credit_limit_check_supplier_invoices` (necesită `credit_limit_from_invoices = True`) — dacă este `False` (implicit), creditul se calculează doar din facturile sau notele de credit ale clientului; dacă este `True`, creditul se calculează din toate facturile sau notele de credit.
  - `skip_only_card` — limitează sărirea verificării doar la tranzacțiile plătite altfel decât cu cardul.

Beneficii de afaceri: reducerea riscului financiar prin control automat al creditului, gestionarea mai bună a fluxului de numerar, abordare structurată a creditului clienților, prevenirea expunerii excesive față de clienții cu risc ridicat și fluxuri de aprobare personalizabile pentru depășirea limitelor.

#### 3. Dependențe

- `account_payment`
- `sale_management`
- [terrabit_partner_payable_receivable](../terrabit_partner_payable_receivable/index.md)

#### 4. Componente Cheie

Documentația acestei secțiuni se bazează pe fișierul `readme/DESCRIPTION.md`, care nu detaliază componentele tehnice individuale. Conform fluxului de ingestie, analiza codului pentru Modele, Vizualizări și Acțiuni Automate a fost omisă întrucât Readme-ul este prezent.

#### 5. Conexiuni

- [terrabit_partner_payable_receivable](../terrabit_partner_payable_receivable/index.md): modul înrudit (și dependență) din suita terrabit care stă la baza calculului de plăți/încasări pe partener, folosit de logica de limită de credit.
- `sales_team` (`crm.team`): oferă excepția „Ignore credit limits" pe echipă de vânzări.
- `mail`: susține activitatea de solicitare de aprobare (butonul „Req. confirm").
