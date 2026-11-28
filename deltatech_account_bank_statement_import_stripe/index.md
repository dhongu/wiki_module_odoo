# Stripe Settlements (localizat la `deltatech_account_bank_statement_import_stripe/index.md`)

- **Nume Tehnic:** `deltatech_account_bank_statement_import_stripe`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_account_bank_statement_import_stripe
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_account_bank_statement_import_stripe`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul importă rapoartele de plată (payout) **Stripe** direct ca extrase de cont: un extras pentru fiecare payout, câte o linie pentru fiecare plată, rambursare sau dispută, legată de client, comisioanele Stripe și suma virată în bancă, fără editarea fișierului. Reduce munca de reconciliere dintre încasările cu cardul, facturi și extrasul bancar. Modulul nu se conectează la Stripe, ci citește doar fișierul încărcat; nu trimite date în afara Odoo.

#### 2. Funcționalități Cheie

- **Fișierul așa cum se descarcă**: raportul *Payout reconciliation, Itemized* (CSV) din Stripe Dashboard (*Reports > Payout reconciliation*); exportul mai vechi *Balance history* este citit și el. Formatul e recunoscut după coloane, fără mapare.
- **Un extras pe payout**: un fișier cu mai multe payout-uri dă câte un extras, datat în ziua virării, ca să corespundă transferului din extrasul bancar; soldurile inițial și final sunt 0,00.
- **Clientul găsit după plată**: din plata online Odoo cu id-ul plății Stripe sau cu referința Odoo, ori din comanda de vânzare din descriere; fără potrivire unică, linia rămâne de completat.
- **Comisioane după preferință**: o linie pe payout, o linie pe tranzacție sau deloc; serviciile facturate separat (Radar, Billing) și TVA-ul aplicat de Stripe pe comisioane au linii proprii, fiindcă regimul de TVA diferă.
- **Linia de payout opțională**: o linie negativă cu suma netă virată echilibrează extrasul (**Settlement Files: Add Payout Line**).
- **O monedă pe jurnal, fără dubluri**: un fișier cu mai multe monede este refuzat; reimportul aceluiași fișier este detectat.
- **Configurare**: jurnal de tip **Bank** în moneda soldului Stripe, cu **Bank Feeds = Import**; import prin **Upload** din jurnal.
- **Reconciliere**: plățile cu facturile, comisioanele cu contul 627 (sau cu furnizorul Stripe, 401, la înregistrarea facturii), payout-ul cu transferul din bancă prin 581; disputa redeschide creanța clientului.

#### 3. Dependențe

- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md)
- `account_bank_statement_import`
- `account_bank_statement_import_csv`

#### 4. Componente Cheie

Secțiunea nu este detaliată: documentația se bazează pe `readme/DESCRIPTION.md`, care nu solicită explicit analiza componentelor tehnice (modele, vizualizări, acțiuni automate).

#### 5. Conexiuni

- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md): constructorul comun de extrase de decontare.
- [deltatech_account_bank_statement_import_paypal](../deltatech_account_bank_statement_import_paypal/index.md): același mecanism de import, pentru raportul PayPal.
