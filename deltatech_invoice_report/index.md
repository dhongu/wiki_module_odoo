# Invoice Report (localizat la `deltatech_invoice_report/index.md`)

- **Nume Tehnic:** `deltatech_invoice_report`
- **Versiune:** `19.0.1.0.8`
- **Cale:** [https://github.com/dhongu/deltatech/tree/19.0/deltatech_invoice_report](https://github.com/dhongu/deltatech/tree/19.0/deltatech_invoice_report)
- **Cale Locală:** `odoo-addons/deltatech/deltatech_invoice_report`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul extinde raportul standard de analiză a facturilor din Odoo și fișa produsului cu istoricul
cantităților cumpărate și vândute, astfel încât echipele de achiziții și vânzări văd rapid, direct
pe fișa produsului, câtă cantitate a fost intrată sau ieșită pe facturi în fiecare an, fără să mai
ruleze un raport dedicat.

#### 2. Funcționalități Cheie

- Adaugă câmpurile **Regiune** (județul/starea partenerului) și **Furnizor Implicit** pe raportul
  `account.invoice.report`, pentru a putea grupa sau filtra analiza facturilor după regiunea
  clientului/furnizorului sau după furnizorul principal al produsului.
- Adaugă o filă **Istoric** pe formularul produsului, cu cantitățile facturate pe fiecare an
  (cantitate intrată din facturi de achiziție, cantitate ieșită din facturi de vânzare).
- Buton **Refresh** pe fila Istoric, care recalculează istoricul la cerere pentru produsul curent,
  folosind o interogare SQL optimizată.
- O sarcină `ir.cron` zilnică (**Update Product Invoice History by Year**) care actualizează automat
  tabelul de istoric pentru toate produsele.
- Buton **View Invoices** pe fișa șablonului de produs și pe varianta de produs, care deschide
  raportul Invoice Analysis pre-filtrat pe produs și grupat pe an și tip de document.

#### 3. Dependențe

- `account`
- `product`

#### 4. Componente Cheie

Documentația pentru Sumar și Funcționalități Cheie a fost generată din fișierul
`readme/DESCRIPTION.md`. Conform fluxului de ingestie, analiza detaliată a codului pentru această
secțiune a fost omisă, întrucât Readme-ul nu cere explicit o astfel de analiză. Pentru detalii
despre modele, vizualizări și acțiuni, consultați direct codul sursă al modulului (`models/`,
`views/`, `report/`, `data/ir_cron_data.xml`).

#### 5. Conexiuni

- `account`: modulul se bazează pe `account.move` / `account.invoice.report` (facturile de vânzare
  și achiziție) pentru a calcula istoricul cantităților și pentru a extinde raportul de analiză.
- `product`: extinde fișa produsului (șablon și variantă) cu fila de istoric și butonul de acces la
  raportul de analiză a facturilor.
