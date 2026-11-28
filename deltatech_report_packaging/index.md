# Report Packaging (localizat la `deltatech_report_packaging/index.md`)

- **Nume Tehnic:** `deltatech_report_packaging`
- **Versiune:** `20.0.1.3.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_report_packaging
- **Cale Locală:** `odoo-addons/deltatech/deltatech_report_packaging`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul calculează cantitățile de materiale de ambalare folosite pentru produsele facturate și oferă, din lista de facturi, un raport agregat al acestora. Fiecare material se configurează cu o cantitate de achiziție și una de vânzare, pentru produsele ambalate într-un fel de furnizor și în alt fel la expediere: facturile de furnizor folosesc prima cantitate, cele către clienți pe a doua.

#### 2. Funcționalități Cheie

- Configurarea materialelor de ambalare (tip material, cantitate de achiziție și cantitate de vânzare, per unitate) în secțiunea **Packaging materials** a fișei produsului; un material folosit într-o singură direcție are cealaltă cantitate pe zero.
- Configurare implicită pe categoria de produs: un produs fără materiale proprii le folosește pe cele ale categoriei sale sau ale celei mai apropiate categorii părinte care are configurare. Nu se copiază nimic pe produs, deci o modificare pe categorie se aplică imediat produselor ei.
- Opțiunea **No packaging material** pe produs oprește moștenirea pentru produsele care nu folosesc deloc ambalaj; un produs cu materiale proprii și le păstrează.
- Fila **Packaging materials** pe factură: cantitatea fiecărui material = cantitatea facturată înmulțită cu cantitatea configurată (de achiziție pe facturi/retururi de furnizor, de vânzare pe facturi/note de credit către clienți); materialele cu cantitate zero în direcția respectivă nu apar.
- Recalcularea cantităților la postarea facturii, atât timp cât factura este în actualizare automată.
- Corecție manuală: editarea sau ștergerea unei cantități scoate factura din actualizarea automată (comutatorul **Auto-update packaging materials**), astfel încât corecția supraviețuiește validării; butonul **Refresh** recalculează cantitățile și repune factura în actualizare automată.
- Raport agregat: din lista de facturi, selectând mai multe facturi, se rulează acțiunea de raport al materialelor de ambalare.

#### 3. Dependențe

- `account`
- `product`

#### 4. Componente Cheie

**Modele**

- `packaging.product.material`: linie de configurare (tip material, cantitate de achiziție, cantitate de vânzare) legată de un produs sau de o categorie de produs.
- `product.template` (extindere): `packaging_material_ids`, indicatorul `packaging_material_no_inherit` și lista calculată a materialelor moștenite de la categorie.
- `product.category` (extindere): `packaging_material_ids`, materialele implicite pentru produsele categoriei.
- `account.move` (extindere): `packaging_material_ids`, comutatorul de actualizare automată și recalcularea materialelor la postare.
- `packaging.invoice.material`: cantitatea unui tip de material calculată pentru o factură.
- `packaging.report.material` și `packaging.report.material.line` (tranzitorii): wizardul raportului agregat și liniile sale de rezultat.

**Vizualizări**

- `product_template_form_view`, `product_category_form_view`: secțiunea **Packaging materials** pe produs și pe categorie.
- `account_move_form_view`: fila **Packaging materials** și butonul **Refresh** pe factură.
- `invoice_packaging_material_form`: formularul wizardului de raport agregat.

**Acțiuni Automate / Acțiuni Server**

- `action_packaging_wizard`: acțiune de fereastră legată de lista de facturi (`account.move`), care deschide raportul materialelor de ambalare.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale suplimentare, în afara dependențelor directe.
