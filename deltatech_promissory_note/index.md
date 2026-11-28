# Bilete la Ordin / CEC (localizat la `deltatech_promissory_note/index.md`)

- **Nume Tehnic:** `deltatech_promissory_note`
- **Versiune:** `20.0.1.0.9`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_promissory_note`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_promissory_note`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul ține evidența biletelor la ordin primite de la clienți și emise către furnizori. Pentru fiecare bilet se înregistrează emitentul, beneficiarul, scadența, valoarea și, opțional, factura la care se referă, iar echipa financiară vede dintr-o privire ce este de încasat, ce a fost încasat și ce a fost anulat. Modulul ține doar registrul: nu generează note contabile și nu reconciliază factura legată.

#### 2. Funcționalități Cheie

- Registru de bilete la ordin pentru clienți și furnizori, listat după scadență, cu totaluri pentru valoare și valoarea încasată (meniul *Promissory Notes* din Contabilitate).
- Datele biletului: serie și număr, emitent și beneficiar cu conturile și băncile lor, valoare și monedă, scadență, acord și, opțional, factura aferentă.
- Tipul biletului completează automat firma pe partea corectă: firma este beneficiarul unui bilet de la client și emitentul unui bilet către furnizor; contul și banca se preiau din primul cont bancar al partenerului (banca este text și poate fi modificată).
- Stări schimbate prin butoane: *Neîncasat* → *Încasat* (cu valoare și dată de încasare), *Neîncasat* (revenire) sau *Anulat*; istoricul stărilor rămâne în chatter.
- Marcajul „Last note" pentru ultimul bilet dintr-un acord: la încasare, utilizatorii din grupul *Primeste atentionari BO* sunt notificați în chatter.
- Fluxul pas-cu-pas este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `promissory.note`: biletul la ordin (serie/număr, tip client/furnizor, scadență, valoare, valoare încasată, emitent, beneficiar, conturi și bănci, factură, acord, stare). Moștenește `mail.thread` și `mail.activity.mixin`.

**Vizualizări**

- Listă cu totaluri pentru `amount` și `cashed_amount`, formular cu bară de stare și butoane de schimbare a stării, căutare după serie, acord, emitent și beneficiar.
- Acțiunea `action_promissory_note`, cu filtru implicit pe biletele neîncasate.
- Rapoarte `Promissory Note Bill` și `Promissory Note Content` (în versiunea curentă tipăresc o pagină goală).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.
- Subtipul de mesaj `mt_state_cashed` și grupul `bo_notifications` („Primeste atentionari BO") servesc notificării la încasarea ultimului bilet dintr-un acord.

#### 5. Conexiuni

- `account`: biletul se leagă opțional de o factură (`account.move`), iar meniul stă în zona de Contabilitate.
