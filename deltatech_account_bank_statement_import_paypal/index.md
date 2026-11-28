# PayPal Settlements (localizat la `deltatech_account_bank_statement_import_paypal/index.md`)

- **Nume Tehnic:** `deltatech_account_bank_statement_import_paypal`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_account_bank_statement_import_paypal
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_account_bank_statement_import_paypal`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul importă raportul de activitate **PayPal** direct ca extras de cont: o linie pentru fiecare plată, rambursare, conversie valutară și retragere către bancă, legată de client, plus comisioanele PayPal, fără să editați fișierul. Contabilul încarcă CSV-ul așa cum îl produce PayPal, iar reconcilierea cu facturile și cu extrasul bancar real devine rapidă. Modulul nu se conectează la PayPal, ci citește doar fișierul încărcat; nu trimite date în afara Odoo.

#### 2. Funcționalități Cheie

- **Fișierul așa cum se descarcă**: raportul *Activity download* (CSV, tranzacții care afectează soldul), cu antetul în engleză, fără mapare de coloane; formatul e recunoscut după coloane.
- **O monedă pe jurnal**: PayPal ține câte un sold pe monedă; se importă doar rândurile în moneda jurnalului, iar o plată în altă monedă intră prin conversia ei, la suma efectiv creditată, netă de comision.
- **Doar ce mișcă soldul**: autorizările, blocările și rândurile informative (*Memo*) sunt omise.
- **Clientul găsit după plată**: din plata online Odoo cu id-ul tranzacției PayPal sau cu referința Odoo (*Invoice Number*), ori din comanda de vânzare cu acea referință; dacă nu există exact o potrivire, linia rămâne de completat de operator.
- **Comisioane după preferință**: o linie agregată, o linie pe tranzacție sau deloc (setarea **Settlement Files: Fees** pe jurnal); comisioanele returnate la rambursări reduc cheltuiala.
- **Date în ambele formate**: zi-lună (Europa) și lună-zi (SUA).
- **Fără dubluri**: fiecare tranzacție se importă o singură dată, deci perioadele se pot suprapune.
- **Configurare**: jurnal de tip **Bank** pentru fiecare monedă PayPal (*Contabilitate > Configurare > Jurnale*), cu **Bank Feeds = Import**; import prin butonul **Upload** al jurnalului. Soldul extrasului este soldul rămas în PayPal, nu zero.
- **Reconciliere**: plățile cu facturile clienților, comisionul pe contul de comisioane (627), retragerile pe contul de transfer intern (581); regulile pentru conversii depind de existența unui jurnal PayPal în moneda plății (detalii în fișa consultantului și în USAGE).

#### 3. Dependențe

- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md)
- `account_bank_statement_import`
- `account_bank_statement_import_csv`

#### 4. Componente Cheie

Secțiunea nu este detaliată: documentația se bazează pe `readme/DESCRIPTION.md`, care nu solicită explicit analiza componentelor tehnice (modele, vizualizări, acțiuni automate).

#### 5. Conexiuni

- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md): constructorul comun de extrase de decontare (parsare sume/date, comisioane, potrivirea clientului).
- [deltatech_account_bank_statement_import_stripe](../deltatech_account_bank_statement_import_stripe/index.md): același mecanism de import, pentru rapoartele Stripe.
