# Bilete la Ordin / CEC (localizat la `deltatech_promissory_note/index.md`)

- **Nume Tehnic:** `deltatech_promissory_note`
- **Versiune:** `19.0.1.0.3`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_promissory_note`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_promissory_note`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul oferă gestionarea biletelor la ordin (BO) și a instrumentelor de tip CEC în Odoo. Permite înregistrarea efectelor de plată emise sau primite, urmărirea scadenței și a stării de încasare a fiecăruia, precum și legarea lor de facturile aferente. Astfel, echipa financiară poate ține o evidență clară a instrumentelor de plată în curs, a celor încasate și a celor anulate, beneficiind de notificări automate atunci când ultimul bilet la ordin dintr-un acord este încasat.

#### 2. Funcționalități Cheie

- Gestionarea biletelor la ordin (BO) și a instrumentelor asociate, atât pentru clienți, cât și pentru furnizori.
- Înregistrarea datelor instrumentului: serie și număr, scadență, valoare, monedă, emitent, beneficiar, conturi și bănci aferente, precum și acordul de referință.
- Urmărirea stării prin flux de stări: Neîncasat, Încasat și Anulat, cu butoane dedicate pentru schimbarea stării.
- Legarea biletului la ordin de o factură (`account.move`) pentru reconciliere și trasabilitate.
- Marcarea unui bilet ca „ultimul" dintr-un acord și notificarea automată a utilizatorilor abilitați la încasarea acestuia.
- Evidențierea valorii și datei efective de încasare, separat de valoarea nominală.
- Istoric și activități prin chatter (mail.thread / mail.activity.mixin), inclusiv subtip de mesaj dedicat la încasare.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `promissory.note`: Modelul principal care reprezintă un bilet la ordin / CEC. Conține seria și numărul, tipul (client/furnizor), scadența, valoarea și valoarea încasată, moneda, emitentul și beneficiarul, conturile și băncile aferente, factura legată, acordul și starea (neîncasat/încasat/anulat). Moștenește `mail.thread` și `mail.activity.mixin` pentru chatter și activități.

**Vizualizări**

- `view_promissory_note_list`: Lista biletelor la ordin, cu însumarea valorilor (`amount`, `cashed_amount`) și afișarea stării.
- `view_promissory_note_form`: Formularul instrumentului, cu bara de stare și butoanele de acțiune (Set Cashed, Set Not Cashed, Cancel) și grupurile de date.
- `view_promissory_note_filter`: Vizualizarea de căutare după serie/număr, acord, emitent și beneficiar.
- `action_promissory_note`: Acțiunea de fereastră care deschide lista/formularul, cu filtrul implicit pe biletele neîncasate; meniul `menu_promissory_note` este atașat sub Contabilitate (`account.menu_finance_entries`).
- `action_report_promissory_note` / `action_report_promissory_note_content`: Acțiuni de raport QWeb-PDF pentru tipărirea biletului la ordin și a conținutului acestuia.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni `ir.actions.server` în acest modul.
- `mt_state_cashed` (`mail.message.subtype`): subtip de mesaj „BO Cashed" folosit pentru notificarea în chatter la încasarea biletului.
- Grup de securitate `bo_notifications` („Primeste atentionari BO"): utilizatorii din acest grup primesc mesaj/notificare la încasarea ultimului bilet la ordin dintr-un acord.

#### 5. Conexiuni

- `account`: instrumentele se leagă de facturi (`account.move`), iar meniul modulului este integrat în zona de Contabilitate.
