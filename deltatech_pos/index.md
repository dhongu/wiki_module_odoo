# Print to ECR from POS (localizat la `deltatech_pos/index.md`)

- **Nume Tehnic:** `deltatech_pos`
- **Versiune:** `19.0.2.8.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_pos
- **Cale Locală:** `odoo-addons/bitshop/deltatech_pos`
- **Ultima Ingestie:** `2026-09-04`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul Deltatech POS ECR asigură o integrare eficientă între punctul de vânzare (Point of Sale) din Odoo și diverse case de marcat fiscale (ECR — Electronic Cash Register), permițând generarea automată a bonurilor fiscale și o gestionare completă a numerarului. În practică, modulul creează o punte între POS-ul Odoo și casa de marcat configurată: generează un fișier în formatul potrivit, care este apoi preluat și tipărit de casa de marcat în modul Conexiune PC (este nevoie de un driver de comunicare specific modelului). Astfel, operatorul nu mai lucrează din utilitarul instalat al casei de marcat, ci direct din Odoo — poate tipări bonuri fiscale, introduce sau scoate bani din casă, emite rapoarte X și Z și urmărește vânzările pe TVA direct dintr-un raport dedicat.

#### 2. Funcționalități Cheie

- Generare fișier pentru programul de tipărit Bon Fiscal din POS.
- Suport pentru tipărirea notelor de pe liniile de comandă (note client și note interne).
- Suport pentru tipărirea notei generale a comenzii, după liniile de produse.
- Suport pentru tipărirea numărului comenzii sub formă de cod de bare pe bon (opțional).
- Căutare în POS după codul fiscal (tax ID).
- Gestionare Cash In / Cash Out: efectuare de încasări și plăți de numerar direct din interfața POS.
- Tipărirea documentelor de plată/încasare (dispoziții de plată) pe casa de marcat.
- Opțiune pentru tipărirea duplicatului dispoziției de plată.
- Tipărirea rapoartelor X și Z direct din Odoo.
- Posibilitatea de a configura departamentul implicit pentru liniile de pe bon.
- Output compatibil ASCII pentru driverele ECR: elimină diacriticele și convertește exponenții uzuali (ex.: m² → m2, m³ → m3); orice alt caracter non-ASCII este înlocuit cu spațiu.
- **Raportul „Vânzări TVA pe casă de marcat"** (nou, PR #2795): **Punct de vânzare → Reporting → VAT Sales by Fiscal Device** — vedere pivot/listă peste comenzile POS plătite sau postate, grupată implicit pe punct de lucru (casă de marcat) și cotă TVA, cu bază, TVA și total pentru orice interval de dată; filtrul implicit „Fiscal Receipt Printed" arată doar liniile al căror bon a fost efectiv tipărit, iar vederea listă oferă detalierea pe comandă. Citește direct `pos.order.line`, fără migrare/backfill — e un punct de plecare pentru reconciliere, nu o citire a arhivei electronice a aparatului fiscal, și nu acoperă fluxul separat `deltatech_sale_store` (facturare la bon fiscal, fără POS).

**Case de marcat compatibile:**

- Datecs — variantele noi (2018), cu driverele FiscalWire, FiscalNet și DxPrint.
- Optima — cu driverul QComm.
- Incotex Succes — cu driverul FiscalPrinterDevice.
- Daisy — cu driver corespunzător (folosind protocolul Daisy).

**Configurare și utilizare (din `readme/USAGE.md`):**

- Codul ECR se setează per metodă de plată (Punct de vânzare > Configurare > Metode de plată).
- Comportamentul specific ECR (cod de bare pe bon, Cash In/Out, Cash In/Out către ECR, duplicat dispoziție de plată, departament implicit) se configurează în Setările Punctului de Vânzare, secțiunea ECR.
- Rapoartele X și Z se tipăresc din sesiunea POS activă (Punct de vânzare > Comenzi > Sesiuni).

#### 3. Dependențe

- `point_of_sale`
- [deltatech_pos_base](../deltatech_pos_base/index.md)
- [deltatech_ecr_connect](../deltatech_ecr_connect/index.md)
- `deltatech_ecr_fiscal`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile de Componente Cheie sunt în principiu omise deoarece modulul include un fișier `readme/DESCRIPTION.md`, folosit pentru Sumar și Funcționalități Cheie. Excepție: modelul nou adăugat pentru raportul de vânzări TVA, prea tehnic pentru a fi acoperit exclusiv de readme.

**Modele**

- `deltatech.pos.vat.report` (`models/deltatech_pos_vat_report.py`): model nestocat (`_auto = False`), definit direct ca vedere SQL peste `pos.order.line` (join cu `pos_order`, `res_company` și taxele procentuale ale liniei). Nu are migrare/backfill — se recreează la fiecare pornire a modulului. Agregă vânzările POS pe dată fiscală (`report_date`, din `date_order`), punct de vânzare (`config_id`), cotă TVA (`vat_rate`, prima taxă procentuală a liniei) și stare (`paid`/`done`), expunând bază, TVA și total. Include și `receipt_print`, pentru filtrarea pe bonuri efectiv tipărite.

**Vizualizări**

- `view_deltatech_pos_vat_report_search`: căutare/filtre pe punct de vânzare, cotă TVA și dată fiscală, cu grupare rapidă pe punct de vânzare/cotă/dată și filtrul „Fiscal Receipt Printed".
- `view_deltatech_pos_vat_report_pivot`: vedere implicită a raportului — rânduri pe punct de vânzare și cotă TVA, coloane pe lună, măsuri Bază/TVA/Total.
- `view_deltatech_pos_vat_report_list`: vedere listă needitabilă (`create="0" edit="0" delete="0"`) pentru detalierea pe comandă individuală.
- `action_deltatech_pos_vat_report` + `menu_deltatech_pos_vat_report`: acțiunea și intrarea de meniu **Point of Sale → Reporting → VAT Sales by Fiscal Device**, cu grupare implicită pe punct de vânzare și cotă TVA și filtrul „Fiscal Receipt Printed" activ din context.

#### 5. Conexiuni

- [deltatech_pos_base](../deltatech_pos_base/index.md): modul de bază POS Deltatech pe care se construiește integrarea ECR (dependență directă).
- [deltatech_ecr_connect](../deltatech_ecr_connect/index.md): componenta partajată de conectare/comunicare cu casele de marcat, folosită de `deltatech_pos` pentru generarea fișierelor ECR (dependență directă).
- `l10n_ro_anaf_d394_pos`: preia bonurile POS pentru declarația D394 (menționat în fișa consultant ca modul complementar, nu dependență directă).
- `deltatech_sale_store` / `deltatech_sale_store_report`: fluxul separat de facturare la bon fiscal, fără POS — nu e acoperit de noul raport „VAT Sales by Fiscal Device" (limitare notată explicit în fișa consultant).
