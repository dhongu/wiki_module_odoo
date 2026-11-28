# Invoice Storable Products Only from Orders (localizat la `deltatech_invoice_storable_source/index.md`)

- **Nume Tehnic:** `deltatech_invoice_storable_source`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_invoice_storable_source
- **Cale Locală:** `odoo-addons/deltatech/deltatech_invoice_storable_source`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Ține stocul și facturarea în pas: produsele stocabile se facturează doar dintr-o comandă de vânzare și se primesc în factură doar dintr-o comandă de achiziție, astfel încât fiecare linie stocabilă facturată are în spate o comandă, cu livrarea sau recepția ei. Împreună cu politica de facturare *Cantități livrate*, se facturează exact ce a fost livrat.

#### 2. Funcționalități Cheie

- **Facturi de client**: o factură, notă de credit sau chitanță de vânzare cu produs stocabil care nu provine dintr-o comandă de vânzare nu poate fi postată.
- **Facturi de furnizor**: o factură, rambursare sau chitanță de achiziție cu produs stocabil care nu provine dintr-o comandă de achiziție nu poate fi postată.
- **Toate căile de postare**: butonul *Confirmă*, confirmarea în masă din listă și postarea automată programată sunt toate verificate; facturile din Punctul de vânzare nu se verifică.
- **Serviciile trec**: serviciile (transport, manoperă) și bunurile fără *Urmărire inventar* nu sunt verificate.
- **Note de credit din comandă**: o notă de credit care stornează o factură emisă din comandă păstrează legătura cu comanda și se postează normal.
- **Pe companie**: cele două verificări se activează separat în *Facturare > Configurare > Setări*, în secțiunile *Facturi client* și *Facturi furnizor*; la facturile de furnizor, formularul se completează din comanda de achiziție prin câmpul *Completare automată*.
- Pașii ilustrați sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `sale_stock`
- `purchase_stock`

#### 4. Componente Cheie

**Modele**

- `account.move`: verifică la postare liniile cu produse stocabile.
- `res.company`, `res.config.settings`: cele două opțiuni (clienți / furnizori), salvate pe compania curentă.

**Vizualizări**

- `views/res_config_settings_views.xml`: opțiunile din setările de Facturare.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- `sale_stock`, `purchase_stock`: comenzile și livrările/recepțiile de la care provine fiecare linie stocabilă.
