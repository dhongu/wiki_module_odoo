# Invoice Receipt Confirmation (localizat la `deltatech_invoice_receipt_confirmation/index.md`)

- **Nume Tehnic:** `deltatech_invoice_receipt_confirmation`
- **Versiune:** `20.0.0.1.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_invoice_receipt_confirmation
- **Cale Locală:** `odoo-addons/bitshop/deltatech_invoice_receipt_confirmation`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul le permite clienților să confirme că au primit factura trimisă pe e-mail și în SPV (e-Factura) și că este corectă. E-mailul care poartă factura conține un link către o pagină publică, protejată cu token, unde clientul bifează cum a primit factura și apasă „Totul e în regulă" sau semnalează o problemă, cu motiv și comentariu. Confirmarea este declarativă: ANAF nu anunță emitentul că destinatarul a văzut factura în SPV, deci „primită în SPV" este ceea ce declară clientul.

#### 2. Funcționalități Cheie

- **Activare pe companie**: *Invoicing > Configuration > Settings*, secțiunea *Invoice receipt confirmation*: opțiunea *Ask for invoice receipt confirmation* și *Reminder after (days)* (zero dezactivează reminderul).
- **Link în e-mail**: la trimiterea unei facturi client sau a unei note de credit postate (*Send*), mesajul se încheie cu o cerere scurtă și butonul *Confirm receipt*, iar factura trece în *Awaiting confirmation*.
- **Pagina clientului**, fără autentificare: clientul vede numărul și suma facturii, bifează canalul (e-mail, SPV / e-Factura), opțional își trece numele și e-mailul, apoi confirmă sau raportează problema cu un motiv (date client/factură greșite, sumă greșită, produse sau cantități greșite, altele). Linkul acceptă un singur răspuns.
- **Starea pe factură**: *Confirmed*, *Awaiting confirmation* sau *Disputed*, lângă data facturii; butonul *Confirmations* deschide jurnalul răspunsurilor facturii.
- **Jurnal al confirmărilor**: *Invoicing > Customers > Receipt confirmations*, cu data, factura, clientul, rezultatul, canalele bifate, motivul, comentariul, e-mailul și IP-ul; respectă regula multi-companie.
- **Activități pentru vânzător**: o factură contestată creează imediat activitatea *Invoice disputed by the customer*; un cron zilnic creează, o singură dată per factură, activitatea *Invoice receipt not confirmed* după numărul de zile din setări. Reminderul este intern, modulul nu retrimite e-mailul clientului.
- **Filtre pe facturi**: *Receipt not confirmed*, *Receipt confirmed*, *Receipt disputed* și grupare după *Receipt confirmation*.
- Limită: linkul funcționează doar dacă parametrul `web.base.url` este adresa publică a instanței. Fluxul cu capturi este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `portal`
- `mail`

#### 4. Componente Cheie

**Modele**

- `account.move.receipt.confirmation`: un răspuns al clientului (dată, contact, IP, canale, rezultat, motiv, comentariu).
- `account.move`: extins cu starea confirmării, tokenul și butonul *Confirmations*.
- `account.move.send`: adaugă cererea și butonul *Confirm receipt* în mesajul trimis.
- `res.company`, `res.config.settings`: setările de activare și reminder.

**Vizualizări**

- `views/account_move_views.xml`: starea, butonul și filtrele de pe factură.
- `views/receipt_confirmation_views.xml`: lista și formularul jurnalului.
- `views/receipt_templates.xml`: pagina publică a clientului și pagina de mulțumire (controller în `controllers/`).
- `views/res_config_settings_views.xml`: setările.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_receipt_reminder`: rulează zilnic și creează activitatea de reminder pentru vânzător la facturile neconfirmate.

#### 5. Conexiuni

- [deltatech_invoice_receipt](../deltatech_invoice_receipt/index.md): nume asemănător, dar fără legătură funcțională (acela generează comenzi de achiziție și recepții din facturile de furnizor).
