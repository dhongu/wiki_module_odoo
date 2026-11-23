# Plată Ramburs / la Livrare (COD) (localizat la `deltatech_payment_on_delivery/index.md`)

- **Nume Tehnic:** `deltatech_payment_on_delivery`
- **Versiune:** `19.0.4.1.13`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_payment_on_delivery
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_on_delivery`
- **Ultima Ingestie:** `2026-11-18`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă o metodă de plată „Ramburs la livrare" (Cash On Delivery – COD) pentru magazinele online care expediază prin curieri ce încasează suma la livrare. Comanda plătită ramburs este validată de un operator, iar banii încasați de curier sunt reconciliați pe baza decontărilor primite de la aceștia. Astfel se reduce riscul coletelor refuzate și se simplifică închiderea contabilă a încasărilor.

#### 2. Funcționalități Cheie

Odoo 19 standard (modulul `delivery`) oferă deja un ramburs de bază: furnizor `custom` în modul *Cash On Delivery*, opțiunea „Cash on Delivery" pe metoda de livrare, confirmarea automată a comenzii și o sumă maximă. Nu tratează însă riscul coletelor refuzate, restricția pe produs sau reconcilierea sumelor încasate de curier. Modulul adaugă:

- **Confirmare manuală a comenzii:** cu opțiunea *In pending*, o comandă plătită ramburs nu se confirmă automat; oferta este marcată ca trimisă și așteaptă confirmarea unui operator.
- **Stare configurabilă a tranzacției:** „Pending" (confirmare manuală) sau „Authorized" (comanda se confirmă automat, ca la COD-ul standard).
- **Sumă minimă:** COD este oferit doar peste un prag, convertit în moneda companiei (Odoo standard are doar sumă maximă).
- **Restricție pe categorie de produs:** categoriile de website marcate „No Cash On Delivery" ascund opțiunea COD pentru comenzile care conțin produsele lor.
- **Fără COD după un link de plată:** dacă pentru o comandă s-a generat un link de plată, COD nu mai este oferit, ca suma să nu fie încasată de două ori.
- **Protecția integrității:** o tranzacție COD nu poate fi trecută manual în „Done"; se închide doar prin wizard-ul de import.
- **Wizard de import al plăților COD:** importă decontările curierilor (Excel), potrivește tranzacțiile după referință sau număr de tracking și le închide.
- **Referință de plată pe factură:** factura unei comenzi COD folosește AWB-ul (referința de tracking) ca referință de plată, ceea ce ușurează reconcilierea bancară a decontării curierului.
- **Fără e-mail „plată reușită"** pentru comenzile COD, deoarece nimic nu a fost încă plătit.
- **Integrare cu Deltatech Delivery și conectorii de marketplace:** modulele de livrare, de revizuire a comenzilor și de marketplace (eMAG, PrestaShop) recunosc comenzile COD după furnizorul acestui modul.

**Notă:** modulul folosește propriul furnizor (cod `on_delivery`). Furnizorul standard *Cash On Delivery* trebuie păstrat dezactivat, altfel clienții văd două opțiuni COD la checkout, iar cea standard confirmă comenzile automat, ocolind validarea manuală.

#### 3. Dependențe

- `payment`
- `sale`
- `delivery`
- `payment_custom`
- `account`
- `stock_delivery`
- `website_sale`

Dependență externă Python: `openpyxl`.

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile de componente sunt omise deoarece `readme/DESCRIPTION.md` este prezent și acoperă Sumarul și Funcționalitățile Cheie. (Din manifest reies: un furnizor și o metodă de plată COD definite în `data/`, un wizard de import al plăților, extinderi pe categoria de produs și pe furnizorul de plată, plus un script JS pentru checkout-ul website.)

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): recunoaște tranzacțiile cu furnizorul `on_delivery` (legătura se face la rulare; modulul nu îl declară în dependențe, linia fiind comentată în manifest).
- [deltatech_marketplace_emag](../deltatech_marketplace_emag/index.md): tratează comenzile COD importate din eMAG.
- [deltatech_marketplace_prestashop](../deltatech_marketplace_prestashop/index.md): tratează comenzile COD importate din PrestaShop.
- [deltatech_marketplace_review](../deltatech_marketplace_review/index.md): revizuirea comenzilor de marketplace ține cont de comenzile COD.
