# Bilete la Ordin / CEC (localizat la `deltatech_promissory_note/index.md`)

- **Nume Tehnic:** `deltatech_promissory_note`
- **Versiune:** `19.0.1.0.9`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_promissory_note
- **Cale Locală:** `odoo-addons/deltatech/deltatech_promissory_note`
- **Ultima Ingestie:** `2026-11-05`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul ține un registru al biletelor la ordin primite de la clienți și emise către furnizori. Pentru fiecare bilet se urmăresc scadența și starea de încasare, iar echipa financiară are o evidență clară a biletelor neîncasate, încasate și anulate. Modulul ține doar registrul: nu generează note contabile și nu reconciliază factura legată.

#### 2. Funcționalități Cheie

- **Date înregistrate pentru fiecare bilet**: serie și număr, emitent și beneficiar cu conturile bancare și băncile lor, valoare și monedă, scadență, acord și, opțional, factura de care aparține. Tipul biletului completează automat firma: este beneficiarul unui bilet de client și emitentul unui bilet de furnizor.
- **Lista** este ordonată după scadență, cu totaluri pentru valoare și valoarea încasată, și are filtru implicit pe biletele neîncasate.
- **Flux de stări** prin butoane: *Not Cashed* → *Cashed* sau *Cancelled*. **Set Cashed** cere completarea **Cashed Amount** și **Cashed Date**; **Set Not Cashed** reface un bilet încasat; **Cancel** anulează un bilet neîncasat. Istoricul stărilor rămâne în chatter.
- **Bilet client**: se păstrează **Type** = **Customer**, firma devine **Beneficiary**, iar clientul se alege ca **Issuer**; contul și banca emitentului se iau din primul cont bancar al clientului.
- **Bilet furnizor**: **Type** = **Vendor**, firma devine **Issuer**, furnizorul se alege ca **Beneficiary**, cu contul și banca completate la fel.
- **Ultimul bilet dintr-un acord**: dacă la încasare este bifat **Last note**, utilizatorii din grupul *Primeste atentionari BO* primesc mesaj în chatter.
- **Meniu**: *Invoicing > Accounting > Promissory Notes* (cu Odoo Enterprise: *Accounting > Accounting > Promissory Notes*).
- **Rapoarte**: cele două rapoarte din meniul **Print** (*Promissory Note Bill*, *Promissory Note Content*) tipăresc, în această versiune, o pagină goală.
- Fluxul pas cu pas, cu capturi, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

Sumarul și Funcționalitățile Cheie provin din `readme/DESCRIPTION.md` și `readme/USAGE.md`. Elementele de mai jos au fost păstrate din ingestia anterioară și confirmate parțial în `views/promissory_note_view.xml`.

**Modele**

- `promissory.note`: modelul principal, un bilet la ordin. Conține seria și numărul, tipul (client/furnizor), scadența, valoarea și valoarea încasată, moneda, emitentul și beneficiarul, conturile și băncile, factura legată, acordul și starea. Moștenește `mail.thread` și `mail.activity.mixin`.

**Vizualizări**

- `view_promissory_note_list`: lista biletelor, cu însumarea valorilor și afișarea stării.
- `view_promissory_note_form`: formularul biletului, cu bara de stare și butoanele Set Cashed, Set Not Cashed și Cancel.
- `view_promissory_note_filter`: căutare după serie/număr, acord, emitent și beneficiar.
- `action_promissory_note`: acțiunea de fereastră cu filtrul implicit pe biletele neîncasate; meniul `menu_promissory_note` este sub Contabilitate.
- `action_report_promissory_note` / `action_report_promissory_note_content`: acțiunile de raport QWeb-PDF (pagină goală în această versiune).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni `ir.actions.server`.
- `mt_state_cashed` (`mail.message.subtype`): subtipul de mesaj „BO Cashed", folosit la notificarea în chatter la încasare.
- Grupul de securitate `bo_notifications` („Primeste atentionari BO"): membrii lui sunt notificați la încasarea ultimului bilet dintr-un acord.

#### 5. Conexiuni

- `account`: biletul poate fi legat de o factură (`account.move`), iar meniul modulului este în zona de Contabilitate; fără note contabile și fără reconciliere.
