# Limită de Credit pe Partener (localizat la `terrabit_partner_credit_limit/index.md`)

- **Nume Tehnic:** `terrabit_partner_credit_limit`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/terrabit_partner_credit_limit
- **Cale Locală:** `odoo-addons/bitshop/terrabit_partner_credit_limit`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul implementează un sistem robust de gestionare a limitelor de credit pentru partenerii de afaceri. Permite organizațiilor să stabilească și să aplice limite de credit clienților, ajutând la administrarea riscului financiar și la controlul eficient al creanțelor. Atunci când limita de credit a unui client este depășită, comenzile de vânzare nu mai pot fi confirmate, oferind un control automat asupra expunerii la credit. Modulul este util în special pentru companiile care oferă termene de plată clienților și care doresc să își gestioneze responsabil expunerea pe creanțe.

#### 2. Funcționalități Cheie

- Stabilește o limită de credit pe partener; comenzile de vânzare nu pot fi confirmate dacă limita de credit este depășită.
- Permite marcarea anumitor parteneri pentru a ignora limitele de credit.
- Introduce grupuri de acces pentru utilizatori:
  - „Manage credit limits" — permite utilizatorilor să modifice limitele de credit ale partenerilor.
  - „Can approve sale order over credit limit" — permite utilizatorilor autorizați să depășească restricția de credit (prin bifarea opțiunii „Allow Over Credit?" din tab-ul Other Info al comenzii de vânzare).
- Permite exceptarea anumitor echipe de vânzări de la verificarea limitei de credit.
- Calcul flexibil al creditului bazat pe parametri de sistem:
  - Parametrul `credit_limit_from_invoices` — dacă este `False` (implicit), creditul se calculează din liniile de cont (account move lines); dacă este `True`, creditul se calculează din facturi (facturile trebuie să fie plătite).
  - Parametrul `credit_limit_check_supplier_invoices` (necesită `credit_limit_from_invoices = True`) — dacă este `False` (implicit), creditul se calculează doar din facturile sau notele de credit ale clientului; dacă este `True`, creditul se calculează din toate facturile sau notele de credit.

Beneficii de afaceri: reducerea riscului financiar prin control automat al creditului, gestionarea mai bună a fluxului de numerar, abordare structurată a creditului clienților, prevenirea expunerii excesive față de clienții cu risc ridicat și fluxuri de aprobare personalizabile pentru depășirea limitelor.

#### 3. Dependențe

- `account_payment`
- `sale_management`
- [terrabit_partner_payable_receivable](../terrabit_partner_payable_receivable/index.md)

#### 4. Componente Cheie

Documentația acestei secțiuni se bazează pe fișierul `readme/DESCRIPTION.md`, care nu detaliază componentele tehnice individuale. Conform fluxului de ingestie, analiza codului pentru Modele, Vizualizări și Acțiuni Automate a fost omisă întrucât Readme-ul este prezent.

#### 5. Conexiuni

- [terrabit_partner_payable_receivable](../terrabit_partner_payable_receivable/index.md): modul înrudit (și dependență) din suita terrabit care stă la baza calculului de plăți/încasări pe partener, folosit de logica de limită de credit.
