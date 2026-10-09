# Print to ECR from POS (localizat la `deltatech_pos/index.md`)

- **Nume Tehnic:** `deltatech_pos`
- **Versiune:** `19.0.2.10.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_pos
- **Cale Locală:** `odoo-addons/bitshop/deltatech_pos`
- **Ultima Ingestie:** `2026-10-09`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul Deltatech POS ECR asigură o integrare eficientă între punctul de vânzare (Point of Sale) din Odoo și diverse case de marcat fiscale (ECR — Electronic Cash Register), permițând generarea automată a bonurilor fiscale și o gestionare completă a numerarului. În practică, modulul creează o punte între POS-ul Odoo și casa de marcat configurată: generează un fișier în formatul potrivit, care este apoi preluat și tipărit de casa de marcat în modul Conexiune PC (este nevoie de un driver de comunicare specific modelului). Astfel, operatorul nu mai lucrează din utilitarul instalat al casei de marcat, ci direct din Odoo — poate tipări bonuri fiscale, introduce sau scoate bani din casă, emite rapoarte X și Z și urmărește vânzările pe TVA (pe casă de marcat și pe taxă) direct dintr-un raport dedicat.

#### 2. Funcționalități Cheie

- Generare fișier pentru programul de tipărit Bon Fiscal din POS.
- Suport pentru tipărirea notelor de pe liniile de comandă (note client și note interne).
- Suport pentru tipărirea notei generale a comenzii, după liniile de produse.
- Suport pentru tipărirea numărului comenzii sub formă de cod de bare pe bon (opțional).
- **Scanare după referința internă**: dacă un cod scanat nu corespunde niciunui cod de bare al produsului sau al ambalajului, POS-ul caută produsul după **referința internă** (`default_code`), întâi printre produsele încărcate, apoi pe server (produse vandabile și disponibile în POS); la produse cu variante se adaugă varianta cu acea referință.
- Gestionare Cash In / Cash Out: efectuare de încasări și plăți de numerar direct din interfața POS.
- Tipărirea documentelor de plată/încasare (dispoziții de plată) pe casa de marcat.
- Opțiune pentru tipărirea duplicatului dispoziției de plată.
- Tipărirea rapoartelor X și Z direct din Odoo.
- Opțiunea **Force total = Price \* Quantity** (total bon = preț × cantitate); la facturarea unei comenzi POS, prețul unitar de pe factură urmează convenția taxei liniei (brut pentru taxe incluse, net pentru taxe excluse), astfel încât totalul facturii să coincidă cu bonul.
- Output compatibil ASCII pentru driverele ECR: elimină diacriticele și convertește exponenții uzuali (ex.: m² → m2, m³ → m3); orice alt caracter non-ASCII este înlocuit cu spațiu.
- **Tipărirea CIF-ului clientului pe bon** (factură simplificată, Cod fiscal art. 319 alin. (12) lit. a)): opțiunea **Print customer VAT on receipt**, sub plafonul configurat în **VAT print limit** (implicit 490 lei); peste plafon, vânzarea trebuie facturată normal.
- **Raportul „Vânzări TVA pe casă de marcat"** (**Punct de vânzare → Reporting → VAT Sales by Fiscal Device**): vedere pivot/listă peste liniile comenzilor POS plătite sau postate, grupată implicit pe punct de vânzare (casă de marcat) și **numele real al taxei efective** (taxele produsului mapate prin poziția fiscală a comenzii, ca `map_tax`; `tax_name`, ex. „TVA colectat 21% Bunuri", „TVA Taxare Inversa"), cu bază, TVA și total pentru orice interval de dată. Gruparea pe `tax_name` (nu pe cota numerică `vat_rate`, păstrată doar pentru compatibilitate) evită cumularea tăcută a taxelor diferite care au aceeași cotă 0% (SGR, taxare inversă, scutiri). Câmpul `vat_mismatch` (filtrul **VAT Differs from Tax Rate (to check)**, coloană vizibilă implicit în listă) semnalează liniile la care TVA-ul stocat la vânzare nu corespunde cotei taxei efective de azi (o poziție fiscală sau o cotă modificată după vânzare mută linia pe taxa nouă, dar sumele rămân cele de pe bon). Câmpul `vat_mismatch` (filtrul **VAT Differs from Tax Rate (to check)**, coloană vizibilă implicit în listă) semnalează liniile la care TVA-ul stocat la vânzare nu corespunde cotei taxei efective de azi (o poziție fiscală sau o cotă modificată după vânzare mută linia pe taxa nouă, dar sumele rămân cele de pe bon). Câmpul `multi_tax` semnalează liniile cu **două taxe procentuale simultan** pe aceeași linie de comandă — o configurare de verificat, nu un comportament normal (caz real găsit la un client: 21% Bunuri + TVA Taxare Inversă pe aceeași linie). Filtrul „Fiscal Receipt Printed"/„ECR Receipt Text" NU e activ implicit, ca să nu ascundă vânzări reale din perioadele fără integrare ECR activă. Citește direct `pos.order.line`, fără migrare/backfill — e un punct de plecare pentru reconciliere, nu o citire a arhivei electronice a aparatului fiscal, și nu acoperă fluxul separat `deltatech_sale_store` (facturare la bon fiscal, fără POS).

**Case de marcat compatibile:**

- Datecs — variantele noi (2018), cu driverele FiscalWire, FiscalNet și DxPrint.
- Optima — cu driverul QComm.
- Incotex Succes — cu driverul FiscalPrinterDevice.
- Daisy — cu driver corespunzător (folosind protocolul Daisy).
- Succes și alte modele care folosesc aceeași sintaxă de comenzi. Modulul este testat extins cu driverele certificate FiscalWire și FiscalNet.

**Configurare și utilizare (din `readme/USAGE.md`):**

- Codul ECR (**Cod ECR**) se setează per metodă de plată (Punct de vânzare > Configurare > Metode de plată; de regulă 1 numerar, 2 card) și, dacă aparatul lucrează cu categorii de TVA în loc de cote, și pe taxe.
- Tipul casei de marcat și modul în care bonul ajunge la aparat (fișier descărcat preluat de driver sau agentul local **Terrabit Connect**), plus opțiunile ECR (cod de bare pe bon, Cash In/Out, Cash In/Out către ECR, duplicat dispoziție de plată, Force total, CIF pe bon și plafonul lui) se configurează în Punct de vânzare > Configurare > Setări, secțiunea ECR.
- Rapoartele X și Z se tipăresc din sesiunea POS activă (Punct de vânzare > Comenzi > Sesiuni).
- Fluxul pas-cu-pas complet (inclusiv reimprimarea din backoffice, plafonul CIF-ului pe bon și limitările raportului TVA) e detaliat în fișa consultant.

#### 3. Dependențe

- `point_of_sale`
- [deltatech_pos_base](../deltatech_pos_base/index.md)
- [deltatech_ecr_connect](../deltatech_ecr_connect/index.md)
- [deltatech_ecr_fiscal](../deltatech_ecr_fiscal/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile de Componente Cheie sunt în principiu omise deoarece modulul include un fișier `readme/DESCRIPTION.md`, folosit pentru Sumar și Funcționalități Cheie. Excepție: modelul raportului de vânzări TVA (inclusiv logica de mapare a taxei prin poziția fiscală și semnalarea `vat_mismatch`), prea tehnic pentru a fi acoperit exclusiv de readme.

**Modele**

- `deltatech.pos.vat.report` (`models/deltatech_pos_vat_report.py`): model nestocat (`_auto = False`), definit direct ca vedere SQL peste `pos.order.line` (join cu `pos_order`, `res_company` și taxele procentuale ale liniei, via `account_tax_pos_order_line_rel`). Nu are migrare/backfill — se recreează la fiecare pornire a modulului. Taxa raportată e cea **efectivă**: echivalentul SQL al `map_tax` (taxele liniei înlocuite cu cele din poziția fiscală a comenzii, via `account_fiscal_position_account_tax_rel` și `account_tax_alternatives`). Agregă vânzările POS pe dată fiscală (`report_date`, din `date_order`), punct de vânzare (`config_id`) și stare (`paid`/`done`), expunând bază, TVA și total. `tax_name` e numele real al taxei (sau al taxelor concatenate cu „ + ", când sunt mai multe), preluat cu `string_agg` peste taxele procentuale ale liniei; liniile fără nicio taxă procentuală apar cu `tax_name = "Fără taxă TVA"`. `vat_rate` rămâne cota primei taxe procentuale, doar pentru compatibilitate. `vat_mismatch` e `true` când TVA-ul stocat diferă de cel rezultat din cota taxei efective peste o toleranță de rotunjire (max(0,02; 0,01 × cantitate)). `multi_tax` e `true` când linia are mai mult de o taxă procentuală simultan — caz de configurare de verificat. `receipt_print`, pentru filtrarea pe bonuri efectiv tipărite.

**Vizualizări**

- `view_deltatech_pos_vat_report_search`: căutare/filtre pe punct de vânzare, taxă (`tax_name`) și cotă TVA, cu grupare rapidă pe punct de vânzare/taxă/cotă/dată, filtrul „ECR Receipt Text" (`receipt_print`, neactiv implicit) și filtrul „Multiple Taxes (to check)" (`multi_tax`).
- `view_deltatech_pos_vat_report_pivot`: vedere implicită a raportului — rânduri pe punct de vânzare și taxă (`tax_name`), coloane pe lună, măsuri Bază/TVA/Total.
- `view_deltatech_pos_vat_report_list`: vedere listă needitabilă (`create="0" edit="0" delete="0"`) pentru detalierea pe comandă individuală, cu `multi_tax` și `receipt_print` ascunse opțional (`optional="hide"`).
- `action_deltatech_pos_vat_report` + `menu_deltatech_pos_vat_report`: acțiunea și intrarea de meniu **Point of Sale → Reporting → VAT Sales by Fiscal Device**, cu grupare implicită pe punct de vânzare și taxă din context.

#### 5. Conexiuni

- [deltatech_pos_base](../deltatech_pos_base/index.md): modul de bază POS Deltatech pe care se construiește integrarea ECR (dependență directă).
- [deltatech_ecr_connect](../deltatech_ecr_connect/index.md): componenta partajată de conectare/comunicare cu casele de marcat, folosită de `deltatech_pos` pentru generarea fișierelor ECR (dependență directă).
- [l10n_ro_anaf_d394_pos](../l10n_ro_anaf_d394_pos/index.md): raportează bonurile fiscale POS în declarația D394 (modul complementar, nu dependență directă).
- [l10n_ro_pos_fiscal_compliance_ecr](../l10n_ro_pos_fiscal_compliance_ecr/index.md) / [l10n_ro_pos_fiscal_compliance](../l10n_ro_pos_fiscal_compliance/index.md): preiau răspunsul casei de marcat în starea de conformitate AMEF (bon fiscal, reconciliere raport Z).
- [l10n_ro_pos_returns](../l10n_ro_pos_returns/index.md): factură de retur și linie de casă separată pentru fiecare retur POS.
- [deltatech_pos_fix](../deltatech_pos_fix/index.md), [deltatech_pos_stock](../deltatech_pos_stock/index.md), [deltatech_pos_price_sync](../deltatech_pos_price_sync/index.md): module complementare din suita Terrabit pentru POS (corecție total la poziție fiscală cu taxă inclusă, stoc în POS, sincronizare prețuri).
- [deltatech_sale_store](../deltatech_sale_store/index.md) / [deltatech_sale_store_report](../deltatech_sale_store_report/index.md): fluxul separat de facturare la bon fiscal, fără POS — nu e acoperit de raportul „VAT Sales by Fiscal Device" (limitare notată explicit în fișa consultant).
