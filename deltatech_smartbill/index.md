# SmartBill Interface (localizat la `deltatech_smartbill/index.md`)

- **Nume Tehnic:** `deltatech_smartbill`
- **Versiune:** `19.0.1.0.7`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_smartbill
- **Cale Locală:** `odoo-addons/bitshop/deltatech_smartbill`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Modulul trimite facturile de client din Odoo către **SmartBill**, programul românesc de facturare, astfel încât factura să fie emisă în SmartBill cu propria serie și propriul număr, în timp ce contabilitatea rămâne în Odoo. Trimiterea se poate face manual, din factură, sau automat, o dată pe zi.

#### 2. Funcționalități Cheie

- **Trimitere din factură:** o factură sau o notă de credit netrimisă are butonul **Send to SmartBill** (inclusiv ciornele); butonul dispare după trimitere sau la anulare.
- **Numărul SmartBill pe factură:** numărul primit se salvează pe factură. Ciorna este postată imediat după trimitere; opțional preia și numărul SmartBill (cod jurnal + număr SmartBill), iar o factură deja postată își păstrează numărul Odoo.
- **Trimitere zilnică:** o acțiune programată trimite zilnic facturile netrimise, după o întârziere configurabilă față de data facturii, fiecare în compania sa; o factură respinsă de SmartBill este înregistrată în log și nu oprește celelalte.
- **Note de credit ca stornare:** nota de credit care inversează integral o factură trimisă în SmartBill se emite ca stornare, cea parțială ca factură cu cantități negative; nota de credit pentru o factură netrimisă în SmartBill este refuzată.
- **Linii ca în Odoo:** fiecare linie pleacă cu cod, denumire și descriere, unitate de măsură, cantitate, preț și cotă TVA; prețurile se trimit cu sau fără TVA în funcție de taxa liniei, discountul liniei devine linie de discount procentual, iar moneda facturii se trimite odată cu factura.
- **Client plătitor de TVA doar când este cazul:** clientul este declarat plătitor de TVA doar dacă este companie cu cod de TVA cu prefix de țară (RO…); persoanele fizice și codurile fiscale fără prefix se trimit ca neplătitori.
- **Date trimise:** CUI-ul companiei, codul jurnalului ca serie, data și moneda, datele clientului (nume, cod TVA, adresă, e-mail) și liniile. Clientul și produsele nu se salvează în baza de date SmartBill.
- **Configurare:** în *Contabilitate > Configurare > Setări*, secțiunea **SmartBill**: **Username** (e-mailul SmartBill), **Password** (token-ul API), bifa **Use Invoice Number from Smartbill** și **Delay** în zile (0 = de la data facturii). Fiecare jurnal de vânzări primește **Prefix secvență** egal cu seria din SmartBill.
- **Erori:** mesajul de refuz al SmartBill este afișat (sau logat, la acțiunea programată); se corectează factura și se retrimite.
- **Cerințe:** cont SmartBill cu acces API (e-mail utilizator și token) și, în SmartBill, o serie de facturare pentru fiecare jurnal Odoo care trimite facturi.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.move` (extins): câmpul `smartbill_number` și logica de trimitere/stornare către SmartBill.
- `account.move.line` (extins): pregătirea liniilor (nume, descriere, taxă, discount) pentru SmartBill.
- `res.config.settings` (extins): utilizator, token, opțiunea de număr SmartBill și întârzierea de trimitere.

**Vizualizări**

- `view_move_form`: butonul **Send to SmartBill** și numărul SmartBill pe factură.
- `res_config_settings_view_form`: secțiunea SmartBill din setările de contabilitate.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_smartbill_auto_send` (*SmartBill: Send Invoice*): rulează zilnic și trimite facturile netrimise după întârzierea configurată.

#### 5. Conexiuni

- `account`: facturile de client și jurnalele de vânzări de la care pornește trimiterea.
