# Deltatech Purchase UBL (localizat la `deltatech_purchase_ubl/index.md`)

- **Nume Tehnic:** `deltatech_purchase_ubl`
- **Versiune:** `19.0.1.2.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_purchase_ubl
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_ubl`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul importă facturi de la furnizori în format UBL XML (Universal Business Language) și le folosește pentru a actualiza fluxurile de achiziție din Odoo. Pe baza fișierului XML, modulul identifică furnizorul și comanda de achiziție, potrivește produsele, actualizează prețurile de la furnizor, poate valida recepția de stoc și poate genera factura de la furnizor. Valoarea de afaceri principală este reducerea muncii manuale și a erorilor la prelucrarea documentelor electronice de achiziție.

#### 2. Funcționalități Cheie

- **Rezolvare automată a furnizorului și a comenzii:** asistentul (wizard) păstrează comanda de achiziție selectată și poate, de asemenea, identifica furnizorul și comanda din XML (`OrderReference`, codul fiscal al furnizorului, numele furnizorului) atunci când contextul nu mai este disponibil.
- **Potrivire automată a produselor:** produsele sunt potrivite după cod de bare (GS1/EAN), cod de furnizor, referință internă sau nume exact.
- **Integrare cu comanda de achiziție:**
    - când comanda are deja linii, importul actualizează doar liniile existente care se potrivesc;
    - liniile noi din XML nu sunt adăugate la o comandă existentă cu linii, iar asistentul afișează acest avertisment înainte de import;
    - liniile noi neconsumate (produse care nu erau pe comanda originală, ex. o linie de „Ecovaloare" adăugată de furnizor) sunt totuși adăugate ca linii noi pe comandă;
    - când nu se rezolvă nicio comandă, asistentul poate totuși identifica furnizorul din XML și actualiza prețurile de la furnizor.
- **Gestionarea prețurilor:** actualizează prețurile de la furnizor în `product.supplierinfo` direct din datele XML.
- **Suport pentru reduceri:** extrage reducerile de pe linii din `AllowanceCharge` (`ChargeIndicator=false`) și le aplică drept reduceri procentuale pe liniile comenzii de achiziție.
- **Verificarea totalului:** compară totalul comenzii cu totalul din XML (`PayableAmount` / `TaxInclusiveAmount`, cu revenire la valoarea fără taxe) și afișează un avertisment când există o diferență.
- **Automatizare de stoc:** validează opțional recepția de stoc asociată, potrivind cantitățile din XML; liniile de servicii cu politică de facturare „la recepție" (ex. taxele de eco-tax) sunt marcate manual ca recepționate, deoarece nu au mișcări de stoc.
- **Contabilitate:** creează și leagă opțional o factură de la furnizor pornind de la comanda de achiziție. Factura se creează automat când documentul sursă identifică un număr de factură, dar numai dacă înainte comanda a fost confirmată (`state` în `purchase`/`done`) — pentru a evita generarea unor facturi „fantomă" cu cantități zero pe comenzi neconfirmate.
- **Produse lipsă:** opțiune de creare automată a produselor lipsă folosind datele din fișierul UBL.

Modulul suportă namespace-urile standard UBL Invoice și mapările uzuale de coduri de unitate de măsură (C62, KGM, LTR etc.).

Logica de potrivire produse/preț/recepție/facturare este extrasă într-un mixin comun (`purchase.invoice.import.mixin`), reutilizabil și de alte asistente de import facturi (ex. PDF pentru Marso, Delta, Sigemo, Procar); acest wizard păstrează doar partea specifică UBL-XML (parsare XML, detecție format, unități de măsură).

#### 3. Dependențe

- `purchase_stock`
- `account`

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, funcționalitatea principală este expusă printr-un asistent (wizard) de import UBL (`purchase.ubl.import.wizard`) care orchestrează rezolvarea furnizorului/comenzii, potrivirea produselor, actualizarea prețurilor, validarea recepției și crearea facturii de la furnizor, pe baza logicii comune din mixin-ul `purchase.invoice.import.mixin`. (Detalierea modelelor/vizualizărilor nu a fost extrasă din cod, conform fluxului de ingestie bazat pe Readme.)

#### 5. Conexiuni

- `purchase_stock`: actualizează liniile comenzii de achiziție, prețurile de la furnizor și validează recepția de stoc asociată, potrivind cantitățile din XML.
- `account`: creează și leagă opțional factura de la furnizor pornind de la comanda de achiziție.
