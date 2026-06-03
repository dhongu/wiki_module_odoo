# Deltatech Purchase UBL (localizat la `deltatech_purchase_ubl/index.md`)

- **Nume Tehnic:** `deltatech_purchase_ubl`
- **Versiune:** `19.0.0.0.7`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_purchase_ubl
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_ubl`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul importă facturi de la furnizori în format UBL XML (Universal Business Language) și le folosește pentru a actualiza fluxurile de achiziție din Odoo. Pe baza fișierului XML, modulul identifică furnizorul și comanda de achiziție, potrivește produsele, actualizează prețurile de la furnizor, poate valida recepția de stoc și poate genera factura de la furnizor. Valoarea de afaceri principală este reducerea muncii manuale și a erorilor la prelucrarea documentelor electronice de achiziție.

#### 2. Funcționalități Cheie

- **Rezolvare automată a furnizorului și a comenzii:** asistentul (wizard) păstrează comanda de achiziție selectată și poate, de asemenea, identifica furnizorul și comanda din XML (`OrderReference`, codul fiscal al furnizorului, numele furnizorului) atunci când contextul nu mai este disponibil.
- **Potrivire automată a produselor:** produsele sunt potrivite după cod de bare (GS1/EAN), cod de furnizor, referință internă sau nume exact.
- **Integrare cu comanda de achiziție:**
    - când comanda are deja linii, importul actualizează doar liniile existente care se potrivesc;
    - liniile noi din XML nu sunt adăugate la o comandă existentă, iar asistentul afișează acest avertisment înainte de import;
    - când nu se rezolvă nicio comandă, asistentul poate totuși identifica furnizorul din XML și actualiza prețurile de la furnizor.
- **Gestionarea prețurilor:** actualizează prețurile de la furnizor în `product.supplierinfo` direct din datele XML.
- **Suport pentru reduceri:** extrage reducerile de pe linii din `AllowanceCharge` (`ChargeIndicator=false`) și le aplică drept reduceri procentuale pe liniile comenzii de achiziție.
- **Verificarea totalului:** compară totalul comenzii cu totalul din XML (`PayableAmount` / `TaxInclusiveAmount`, cu revenire la valoarea fără taxe) și afișează un avertisment când există o diferență.
- **Automatizare de stoc:** validează opțional recepția de stoc asociată, potrivind cantitățile din XML.
- **Contabilitate:** creează și leagă opțional o factură de la furnizor pornind de la comanda de achiziție, când o comandă este rezolvată.
- **Produse lipsă:** opțiune de creare automată a produselor lipsă folosind datele din fișierul UBL.

Modulul suportă namespace-urile standard UBL Invoice și mapările uzuale de coduri de unitate de măsură (C62, KGM, LTR etc.).

#### 3. Dependențe

- `purchase`
- `stock`
- `account`

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, funcționalitatea principală este expusă printr-un asistent (wizard) de import UBL care orchestrează rezolvarea furnizorului/comenzii, potrivirea produselor, actualizarea prețurilor, validarea recepției și crearea facturii de la furnizor. (Detalierea modelelor/vizualizărilor nu a fost extrasă din cod, conform fluxului de ingestie bazat pe Readme.)

#### 5. Conexiuni

- `purchase`: actualizează liniile comenzii de achiziție și prețurile de la furnizor pe baza facturii UBL.
- `stock`: validează opțional recepția de stoc asociată comenzii, potrivind cantitățile din XML.
- `account`: creează și leagă opțional factura de la furnizor pornind de la comanda de achiziție.
