# SmartBill Interface

- **Nume Tehnic:** `deltatech_smartbill`
- **Versiune:** `20.0.1.0.5`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_smartbill
- **Cale Locală:** `odoo-addons/bitshop/deltatech_smartbill`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Trimite facturile către clienți din Odoo în **SmartBill**, programul românesc de facturare, astfel încât factura să fie emisă în SmartBill sub propria serie și propriul număr, iar contabilitatea să rămână în Odoo. Seria facturii este codul jurnalului, iar numărul primit de la SmartBill se păstrează pe factura din Odoo.

#### 2. Funcționalități Cheie

- **Trimitere din factură**: facturile și notele de credit către clienți, netrimise încă (inclusiv cele în ciornă), au butonul **Send to SmartBill**; butonul dispare după trimitere sau la anulare.
- **Numărul SmartBill pe factură**: numărul primit se salvează pe factură. O ciornă este postată imediat după trimitere; la cerere, ea preia și numărul SmartBill (codul jurnalului + numărul SmartBill), iar o factură deja postată își păstrează numărul din Odoo.
- **Trimitere zilnică**: o acțiune programată trimite o dată pe zi facturile netrimise, după o întârziere configurabilă față de data facturii, fiecare în compania sa; o factură respinsă de SmartBill este înregistrată în jurnal și nu oprește restul.
- **Note de credit ca stornare**: o notă de credit care stornează integral o factură trimisă în SmartBill este emisă acolo ca stornare, una parțială ca factură cu cantități negative; nota de credit pentru o factură netrimisă în SmartBill este refuzată.
- **Linii ca în Odoo**: fiecare linie pleacă cu cod, denumire și descriere, unitate de măsură, cantitate, preț și cota de TVA; prețurile se trimit cu sau fără TVA, după taxa liniei; discountul de pe linie devine linie de discount procentual, iar moneda facturii este trimisă împreună cu factura.
- **Client plătitor de TVA doar când este**: clientul este declarat plătitor de TVA numai dacă este companie cu cod de TVA având prefix de țară (RO…); persoanele fizice și simplele coduri fiscale sunt trimise ca neplătitori.
- **Configurare** (*Contabilitate > Configurare > Setări*, secțiunea **SmartBill**): utilizator (e-mailul SmartBill) și parolă (token-ul API), opțiunea **Use Invoice Number from Smartbill**, întârzierea în zile (0 = de la data facturii); fiecare jurnal de vânzări primește un **Prefix de secvență** egal cu seria din SmartBill.
- **Date trimise către SmartBill**: CUI-ul companiei, codul jurnalului ca serie, data și moneda, numele, CUI-ul, adresa și e-mailul clientului, plus liniile. Clientul și produsele nu se salvează în baza de date SmartBill.
- **Cerințe**: cont SmartBill cu acces API și, în SmartBill, o serie de factură pentru fiecare jurnal Odoo care trimite facturi.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.move` (extins): câmpul `smartbill_number`, trimiterea facturii (`create_invoice_in_smartbill`), construirea payload-ului și metoda cron `_cron_smartbill_auto_send`.
- `account.move.line` (extins): pregătirea liniilor pentru SmartBill (cod, denumire, TVA, discount).
- `res.config.settings` (extins): utilizator, parolă, numărul SmartBill și întârzierea.

**Vizualizări**

- `view_move_form` (`account.move`): butonul **Send to SmartBill** și numărul SmartBill.
- `res_config_settings_view_form`: secțiunea **SmartBill** din setările de contabilitate.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_smartbill_auto_send` (*SmartBill: Send Invoice*): rulează zilnic și trimite facturile netrimise, după întârzierea configurată.

#### 5. Conexiuni

Nu există legături funcționale cu alte module wiki; modulul depinde doar de `account`.
