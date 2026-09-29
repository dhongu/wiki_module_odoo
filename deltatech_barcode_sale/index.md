# Barcode Sale (localizat la `deltatech_barcode_sale/index.md`)

- **Nume Tehnic:** `deltatech_barcode_sale`
- **Versiune:** `19.0.2.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_barcode_sale
- **Cale Locală:** `odoo-addons/bitshop/deltatech_barcode_sale`
- **Ultima Ingestie:** `2026-09-29`

#### 1. Sumar

Acest modul optimizează procesul de vânzare permițând scanarea directă a codurilor de bare în interfața comenzii de vânzare, astfel încât reprezentanții de vânzări pot construi rapid și precis ofertele și comenzile clienților. Din perspectivă de business, funcționalitatea accelerează ciclul de tranzacționare, reduce riscul de erori în comenzi și oferă o experiență mai profesională clientului, fiind utilă mai ales în medii de tip retail.

#### 2. Funcționalități Cheie

- **Introducere accelerată a comenzilor:** adăugarea rapidă a produselor pe comenzile de vânzare prin scanarea codurilor de bare, reducând semnificativ timpul de așteptare al clientului.
- **Reducerea erorilor în comenzi:** eliminarea greșelilor de tastare manuală, asigurând că produsele și variantele corecte sunt întotdeauna adăugate pe comandă.
- **Control îmbunătățit al stocului:** identificarea produselor în timp real prin coduri de bare ajută la menținerea unor evidențe corecte de stoc în timpul vânzării.
- **Eficiență sporită a vânzărilor:** personalul se poate concentra pe servirea clientului și pe cross-selling în loc de introducerea laborioasă a datelor.
- **Mesaje clare la scanare:** scanarea unui cod de bare al unui ambalaj (`product.uom`) afișează un mesaj care numește produsul, iar scanarea unui produs nevandabil (`sale_ok = False`) afișează un mesaj dedicat „produsul nu poate fi vândut”, în loc de eroarea generică „produs negăsit”.
- **Scanare sigură în multi-company:** căutarea produsului după codul de bare este limitată la compania comenzii (sau la produse fără companie) și la un singur rezultat, astfel că un cod de bare duplicat între companii nu mai produce eroarea „Expected singleton”.
- **Serviciu profesional:** o experiență de finalizare a comenzii modernă și eficientă pentru clienți, care crește încrederea și satisfacția.

#### 3. Dependențe

- `sale`
- `barcodes`

#### 4. Componente Cheie

Informațiile provin din `readme/DESCRIPTION.md` și `readme/HISTORY.md`; codul nu a fost analizat în detaliu. Pe scurt, modulul extinde modelul de comandă de vânzare (`sale.order`) și interfața acestuia (`views/sale_views.xml`) pentru a integra scanarea codurilor de bare la adăugarea liniilor de comandă.

#### 5. Conexiuni

- `sale`: modulul de bază al comenzilor de vânzare, peste care se adaugă funcționalitatea de scanare.
- `barcodes`: motorul Odoo de scanare a codurilor de bare folosit pentru identificarea produselor.
