# Stripe Settlements (localizat la `deltatech_account_bank_statement_import_stripe/index.md`)

- **Nume Tehnic:** `deltatech_account_bank_statement_import_stripe`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_account_bank_statement_import_stripe
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_account_bank_statement_import_stripe`
- **Ultima Ingestie:** `2026-10-12`

#### 1. Sumar

Importă rapoartele de virare (payout) din **Stripe** direct ca extrase de cont: un extras pentru fiecare virare, cu o linie pentru fiecare plată, rambursare sau dispută, legată de client, cu comisioanele Stripe și suma virată în bancă, fără editarea fișierului. Modulul citește doar fișierul încărcat și nu se conectează la Stripe, deci nu trimite date în afara Odoo.

#### 2. Funcționalități Cheie

- **Fișierul așa cum se descarcă:** raportul *Payout reconciliation — itemized* (CSV) din Stripe Dashboard (*Reports > Payout reconciliation*); este citit și exportul mai vechi *Balance history*.
- **Recunoaștere automată:** formatul e recunoscut după coloane, în orice ordine, deci se importă din jurnal ca orice alt extras, fără wizardul de mapare a coloanelor (butonul **Upload** din jurnalul Stripe).
- **Un extras per virare:** un fișier cu mai multe virări produce câte un extras, datat în ziua virării, pentru a se potrivi cu transferul din extrasul băncii.
- **Client identificat din plată:** clientul se ia din plata online Odoo care poartă id-ul de plată Stripe sau referința Odoo, ori din comanda de vânzare menționată în descriere; dacă nu există exact o potrivire, linia rămâne pentru atribuire manuală.
- **Comisioane la alegere:** o linie per virare (implicit), o linie per tranzacție sau deloc (*Settlement Files: Fees*). Serviciile facturate separat (Radar, Billing, Connect) și TVA-ul aplicat de Stripe pe comisioane au linii proprii, din cauza regimului de TVA diferit.
- **Linie de virare, o singură monedă, fără dubluri:** o linie negativă opțională cu suma netă virată echilibrează extrasul (*Settlement Files: Add Payout Line*); un fișier cu mai multe monede este refuzat (un jurnal per monedă); fiecare tranzacție se importă o singură dată, deci reimportul aceluiași fișier este detectat.
- **Configurare jurnal:** jurnal de tip **Bank** în moneda soldului Stripe, cu cont propriu pentru banii ținuți de Stripe până la virare (în planul românesc, subcont 461 de tip Bank and Cash), *Bank Feeds* = *Import*.
- **Reconciliere:** plățile cu facturile clienților, comisioanele cu contul de comisioane (627), linia de virare cu transferul din extrasul băncii prin contul de transfer intern (581). Disputa redeschide creanța clientului (se reconciliază cu clientul, nu cu o notă de credit); sumele reținute de Stripe (rezerve) rămân creanțe.
- **Extrasul nu este factura de comisioane:** factura lunară Stripe se înregistrează ca factură de furnizor (procesarea plăților e scutită de TVA; Radar, Billing, Invoicing, Tax, Connect sunt servicii taxabile cu taxare inversă), iar liniile de comision se reconciliază atunci cu datoria către Stripe (401).

#### 3. Dependențe

- `account_bank_statement_import`
- `account_bank_statement_import_csv`
- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md)

#### 4. Componente Cheie

**Modele**

- `account.journal` (extins): recunoaște și parsează fișierele Stripe (itemized și Balance history) prin constructorul comun de decontări; clasifică rândurile (comisioane de procesare, servicii, TVA, virări) și potrivește clientul.

**Vizualizări**

- Fără vizualizări proprii; opțiunile de comisioane și linia de virare vin din modulul comun, în formularul jurnalului.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md): constructorul comun de extrase de decontare pe care se sprijină importul.
- [deltatech_account_bank_statement_import_euplatesc](../deltatech_account_bank_statement_import_euplatesc/index.md): importator similar pentru procesatorul EuPlatesc.
