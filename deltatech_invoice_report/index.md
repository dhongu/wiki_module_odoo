# Invoice Report (localizat la `deltatech_invoice_report/index.md`)

- **Nume Tehnic:** `deltatech_invoice_report`
- **Versiune:** `19.0.1.0.11`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_invoice_report
- **Cale Locală:** `odoo-addons/deltatech/deltatech_invoice_report`
- **Ultima Ingestie:** `2026-11-09`

#### 1. Sumar

Modulul extinde raportul standard de analiză a facturilor din Odoo și fișa produsului cu istoricul
cantităților cumpărate și vândute, astfel încât echipele de achiziții și vânzări văd rapid, direct
pe fișa produsului, câtă cantitate a fost intrată sau ieșită pe facturi în fiecare an, fără să mai
ruleze un raport dedicat.

#### 2. Funcționalități Cheie

- Adaugă câmpurile **Regiune** (județul/starea partenerului) și **Furnizor Implicit** pe raportul
  `account.invoice.report`, pentru a putea grupa sau filtra analiza facturilor după regiunea
  clientului/furnizorului sau după furnizorul principal al produsului.
- Adaugă o filă **History** pe formularul produsului (accesibil din Inventar, Vânzări sau Achiziții), cu un rând pe an: **Qty In** (facturi de achiziție) și **Qty Out** (facturi de vânzare).
- Buton **Refresh** (săgeată circulară) pe fila History, care recalculează istoricul la cerere pentru produsul curent din toate facturile postate, folosind o interogare SQL optimizată.
- O sarcină `ir.cron` zilnică (**Update Product Invoice History by Year**) care reconstruiește tabelul de istoric pentru toate produsele; este activă implicit și apare în *Setări > Tehnic > Automatizare > Acțiuni programate*, unde se pot schimba frecvența (**Interval** / **Interval Unit**) sau se poate dezactiva (reîmprospătarea manuală pe produs rămâne posibilă).
- Populare inițială: tabelul se umple la prima rulare a cron-ului; pentru date imediat după instalare, sarcina se rulează manual cu **Run Manually**.
- Buton **View Invoices** pe fișa șablonului de produs și pe varianta de produs, care deschide raportul Invoice Analysis (*Contabilitate > Raportare > Invoice Analysis*) pre-filtrat pe produs și grupat pe an, cu tipul documentului ca grup de coloane.
- În raportul Invoice Analysis, filtrul de grupare **Region** agregă facturile după județul/starea partenerului, iar coloana **Default Supplier** e disponibilă în vizualizările pivot/grafic.
- Tabelul de istoric (`product.invoice.history`) este un cache materializat; sursa de adevăr rămân înregistrările `account.move` postate.

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
