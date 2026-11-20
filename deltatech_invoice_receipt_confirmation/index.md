# Invoice Receipt Confirmation (localizat la `deltatech_invoice_receipt_confirmation/index.md`)

- **Nume Tehnic:** `deltatech_invoice_receipt_confirmation`
- **Versiune:** `19.0.0.1.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_invoice_receipt_confirmation
- **Cale Locală:** `odoo-addons/bitshop/deltatech_invoice_receipt_confirmation`
- **Ultima Ingestie:** `2026-11-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite clienților să confirme, de la un link din e-mailul care conține factura, că au primit factura prin e-mail și în SPV (e-Factura) și că aceasta este corectă. Clientul deschide o pagină publică, protejată cu token, bifează modul de primire și apasă „Everything is OK” sau semnalează o problemă, cu motiv și comentariu. Factura afișează starea confirmării, iar emitentul are un jurnal al răspunsurilor și remindere automate pentru facturile neconfirmate.

Confirmarea este declarativă: ANAF nu comunică emitentului că factura a fost văzută în SPV, deci „primită în SPV” reprezintă declarația clientului.

#### 2. Funcționalități Cheie

- Activare per companie din **Facturare → Configurare → Setări** (secțiunea *Invoice receipt confirmation*), cu **Reminder after (days)** pentru amintire (zero dezactivează reminderul).
- La trimiterea facturii (facturi și note de credit client postate), mesajul către client primește o cerere scurtă și butonul **Confirm receipt**, iar factura trece în starea *Awaiting confirmation*.
- Pagină publică fără autentificare: număr și sumă factură, canale bifabile (e-mail, SPV), nume și e-mail opționale, butoanele *Everything is OK* / *I have a problem*; la problemă se alege un motiv (date client/factură greșite, sumă greșită, produse sau cantități greșite, altul) și un comentariu.
- Un link primește un singur răspuns; după folosire, pagina arată doar că factura a fost deja confirmată.
- Link invalidat dacă factura este anulată sau revine în ciornă, ori funcția este dezactivată: se afișează doar compania și mesajul „This confirmation request is no longer valid”, fără date și fără înregistrare. Linkul redevine valid la repostare sau la reactivare.
- Stare pe factură (*Confirmed*, *Awaiting confirmation*, *Disputed*) lângă data facturii, buton **Confirmations** și filtre/grupare după confirmare în lista facturilor.
- O factură contestată creează imediat o activitate pentru vânzător, cu motivul și comentariul.
- Acțiune programată zilnică: activitate „Invoice receipt not confirmed” pentru vânzător, o singură dată per factură, după numărul de zile setat. Reminderul este intern; e-mailul nu se retrimite clientului.
- Jurnal în **Facturare → Clienți → Receipt confirmations**: data, factura, clientul, rezultatul, canalele, persoana, motivul, comentariul, e-mailul și IP-ul. Respectă regulile multi-companie.
- Limită: linkul funcționează corect doar dacă `web.base.url` este adresa publică a instanței.

#### 3. Dependențe

- `account`
- `portal`
- `mail`

#### 4. Componente Cheie

**Modele**

- `account.move.receipt.confirmation`: jurnalul răspunsurilor (factură, dată, rezultat, canale e-mail/SPV, motiv, comentariu, contact, IP).
- `account.move` (extins): token, stare, dată cerere, confirmări, contor și logica reminderului.
- `account.move.send` (extins): adaugă cererea și linkul în mesajul de trimitere a facturii.
- `res.company` / `res.config.settings` (extinse): activare și zile de reminder.

**Vizualizări**

- `view_move_form_receipt`, `view_account_invoice_filter_receipt`: stare, buton și filtre pe factură.
- `view_receipt_confirmation_list`, `view_receipt_confirmation_form`: jurnalul confirmărilor.
- `res_config_settings_view_form_receipt`: setările per companie.
- `receipt_templates.xml`: pagina publică de confirmare (controller `controllers/main.py`).

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_receipt_reminder`: zilnic, rulează `_cron_receipt_reminder()` pe `account.move`.

#### 5. Conexiuni

- `account`: facturile și trimiterea lor (`account.move.send`) sunt extinse direct (dependență, fără pagină wiki).
