# SAGA Export for Odoo Online (localizat la `deltatech_saga_online/index.md`)

- **Nume Tehnic:** `deltatech_saga_online`
- **Versiune:** `19.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_saga_online
- **Cale Locală:** `odoo-addons/bitshop/deltatech_saga_online`
- **Ultima Ingestie:** `2026-11-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul exportă facturile de client ale unei perioade sub formă de fișiere XML de import pentru SAGA, inclusiv pe Odoo Online. Nu conține cod Python și se importă ca arhivă zip; fișierele sunt construite de serviciul SAGA Terrabit, iar arhiva revine atașată exportului. Contabilul primește astfel, dintr-un singur export lunar, tot ce are de importat în SAGA. Modulul este în stadiul Alpha.

#### 2. Funcționalități Cheie

- **Un export pe perioadă**: *Contabilitate > Raportare > SAGA Export*; perioada (implicit luna precedentă) și, opțional, jurnalele de vânzări. Butonul *Export* trimite facturile, notele de credit și bonurile de client postate din perioadă. Perioada este cea contabilă (data contabilă), iar în fișier ajunge data facturii.
- **Fișierele din arhivă**: clienții (`CLI`), facturile în RON (`IE`, un fișier pe jurnal, bonurile cu `C`) și facturile în valută sau ale clienților din străinătate (`IEV`, pe jurnal și monedă). Se exportă pe valoare: contul de venit al fiecărei linii, cota de TVA, notele de credit cu cantități negative, cursul facturii. Facturile din Punct de Vânzare sunt marcate cu bon fiscal.
- **Tip document**: tipul SAGA al poziției fiscale (T, X etc.), T pentru taxare inversă internă (taxele grupului RO „TVA Taxare Inversă”), TVA la încasare din poziția fiscală sau pentru toate facturile. O factură cu linii mixte (taxare inversă și normale) este lăsată pe dinafară, exportată cu T sau fără tip, după opțiune, cu mesaj.
- **Cod client**: codul fiscal (implicit) sau codul SAGA al partenerului, completat cu zerouri dacă se dorește (*Lungime cod client*).
- **Perioade lungi**: facturile pleacă în cereri de cel mult 100 de facturi (configurabil), iar serverul le reunește într-un singur fișier de fiecare tip. Progresul (cereri răspunse, facturi exportate, credite folosite) și mesajele sunt pe export; o cerere fără răspuns se retrimite după 10 minute.
- **Reexport**: *Export Again* retrimite o perioadă după corecții; facturile exportate în ultimele 30 de zile nu se taxează din nou.
- **Mai puține date personale**: telefonul și emailul clienților nu se trimit decât la alegere; datele facturilor dintr-o cerere se golesc după răspuns. Serverul Terrabit nu păstrează facturile și șterge arhiva după trimitere; mesajele răspunsurilor rămân în jurnalul cererilor 30 de zile, un export neterminat cel mult o zi.
- **Credite**: fiecare factură exportată se taxează din contul Terrabit; creditele se văd și se cumpără din *Setări > Credite Terrabit*.
- **Tokenul serviciului rămâne la administratori**: utilizatorii de facturare exportă fără acces la serviciul SAGA; cererile sunt create de export în numele lor.
- **Configurare**: în *Setări > Credite Terrabit > Servicii și Credite*, serviciul **SAGA Export** se activează (administrator), apoi se aleg *Cod client = cod fiscal*, *TVA la încasare pentru toate facturile*, tratamentul facturilor mixte, *Un fișier pe tip*, trimiterea telefonului/emailului, formatul datei și numărul de facturi pe cerere. Pe pozițiile fiscale se completează *Tip SAGA* și *TVA la încasare (SAGA)*, iar pe clienți *Cod client SAGA* când nu se folosește codul fiscal.

#### 3. Dependențe

- [deltatech_iap_online](../deltatech_iap_online/index.md)
- `account`

#### 4. Componente Cheie

**Modele**

- `x_saga_export`: exportul unei perioade, cu starea, cererile trimise, facturile exportate, creditele folosite, mesajele și arhiva SAGA (model definit în date, fără cod Python, pentru import pe Odoo Online).
- `x_iap_online_service` (extins): serviciul SAGA Export, cu câmpurile de configurare `x_saga*` (cod client, TVA la încasare, facturi mixte, dimensiunea cererii).
- `account.fiscal.position` (extins): `x_saga_code` (Tip SAGA) și `x_saga_vat_on_payment`.
- `res.partner` (extins): `x_saga_customer_code` (dependent de companie).

**Vizualizări**

- `view_x_saga_export_list` / `view_x_saga_export_form`: lista și formularul exporturilor, sub *Contabilitate > Raportare*.
- `view_x_iap_online_service_form`: grupul de setări SAGA din serviciul Terrabit.
- `view_account_position_form`: Tip SAGA și TVA la încasare pe poziția fiscală.
- `view_partner_form`: Cod client SAGA pe partener.

**Acțiuni Automate / Acțiuni Server**

- `action_saga_export_send` („Export to SAGA”): butonul exportului; limitat la grupul de facturare, citește facturile postate din perioadă, construiește cererile și le trimite serviciului Terrabit.
- `iap_online_service_saga` (date): înregistrarea serviciului SAGA Export în serviciile Terrabit.

#### 5. Conexiuni

- [deltatech_iap_online](../deltatech_iap_online/index.md): oferă serviciile, tokenul, cererile și creditele Terrabit pe care se sprijină exportul.
