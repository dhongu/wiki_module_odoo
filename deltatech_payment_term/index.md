# Payment Term Rate Wizard (localizat la `deltatech_payment_term/index.md`)

- **Nume Tehnic:** `deltatech_payment_term`
- **Versiune:** `20.0.2.0.6`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_payment_term
- **Cale Locală:** `odoo-addons/deltatech/deltatech_payment_term`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul ajută echipele de finanțe și de vânzări să genereze rapid termene de plată în rate, fără a crea manual fiecare linie. Utilizatorul completează un wizard simplu, iar sistemul generează termenul complet, cu avansul, numărul de rate și scadențele corecte.

#### 2. Funcționalități Cheie

- Wizard de generare a ratelor: nume, tip, avans (sumă sau procent), număr de rate și ziua din lună produc un `account.payment.term` complet.
- Moduri procentual și sumă fixă; ultima linie e mereu de tip „sold”, ca să absoarbă rotunjirile. Pentru suma fixă se completează și valoarea ratei.
- Indicatorul calculat **In Rates** pe `account.move` marchează facturile al căror termen are mai multe linii; indicatorul **Sale in Rates** face același lucru pe `sale.order`.
- Butonul **Rates** pe facturi și pe fișa partenerului deschide înregistrările contabile legate de plata în rate.
- Wizardul se lansează din *Accounting > Configuration > Payment Terms* (butonul **Create Rate**, cu înlocuirea liniilor existente) sau din meniul Acțiuni al comenzilor de vânzare și al facturilor (**Payment Term Rate Wizard**).

#### 3. Dependențe

- `account`
- `sale`

#### 4. Componente Cheie

Secțiunea e omisă: `readme/DESCRIPTION.md` nu cere explicit analiza componentelor tehnice.

#### 5. Conexiuni

- `account`: modulul extinde termenul de plată și factura.
- `sale`: modulul marchează comenzile de vânzare plătibile în rate.
