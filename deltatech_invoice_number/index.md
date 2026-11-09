# Invoice Numbering Control (localizat la `deltatech_invoice_number/index.md`)

- **Nume Tehnic:** `deltatech_invoice_number`
- **Versiune:** `19.0.1.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_invoice_number
- **Cale Locală:** `odoo-addons/deltatech/deltatech_invoice_number`
- **Ultima Ingestie:** `2026-11-09`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul păstrează facturile de client în ordine cronologică pe jurnalele unde acest lucru contează și oferă unui grup dedicat de utilizatori posibilitatea de a corecta numărul unei facturi. Astfel se evită facturile cu dată anterioară ultimei facturi emise și se pot remedia numerele greșite fără intervenții în baza de date.

#### 2. Funcționalități Cheie

- **Date cronologice:** pe un jurnal de vânzări cu **Restrict invoice date** bifat, o factură sau notă de credit în ciornă nu poate fi confirmată cu dată anterioară ultimului document postat de același tip din jurnal. Eroarea indică cea mai veche dată permisă, iar la alegerea jurnalului pe o factură în ciornă apare un avertisment cu aceeași informație.
- **Schimbarea numărului facturii:** utilizatorii din grupul **Allow to change invoice number** primesc acțiunea **Change invoice number** în meniul Acțiuni (roata dințată) din formularul facturii. Wizardul propune numărul curent; după **Apply**, noul număr se scrie pe factură și se copiază în referința liniilor sale contabile (și în **Reference** pentru documentele de client).
- **Configurare:** *Contabilitate > Configurare > Jurnale*, jurnal de tip Vânzări, fila **Journal Entries**, secțiunea **Invoice numbering** (bifa **Restrict invoice date**); utilizatorii se adaugă în grup din *Setări > Utilizatori și companii > Grupuri*.
- **Limitări:** câmpul **Journal Sequence** din secțiunea **Invoice numbering** nu are efect în interfață — există o metodă care numerotează o factură în ciornă din această secvență, dar niciun buton sau meniu nu o apelează (versiunile anterioare ale paginii o prezentau ca funcționalitate). Noul număr se scrie exact cum e tastat: wizardul nu îl verifică față de formatul de numerotare al jurnalului și nici față de goluri.
- Pașii detaliați sunt în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.move` (extindere): verificarea ordinii cronologice (`check_data`), `action_get_number` (alocare număr din secvența jurnalului pe o factură în ciornă, neapelată din interfață) și `action_number` pentru sincronizarea referinței (`ref`) facturii și a liniilor după o renumerotare manuală; suprascrie `action_post` pentru a bloca postarea facturilor de client în afara ordinii cronologice dacă jurnalul are bifat `restrict_date`.
- `account.journal` (extindere): câmpurile `journal_sequence_id` (secvența de numerotare, fără efect în interfață) și `restrict_date` (activează restricția de ordine cronologică).
- `account.invoice.change.number` (model tranzitoriu — wizard): introducerea manuală a unui nou număr de factură și sincronizarea lui prin `do_change_number`.

**Vizualizări**

- `journal_restrict_date_form`: extinde formularul jurnalului contabil (`account.view_account_journal_form`) cu grupul „Invoice numbering", vizibil doar pentru jurnalele de vânzare, unde se află `journal_sequence_id` și `restrict_date`.
- `view_account_invoice_change_number_form`: formularul wizardului pentru noul număr de factură, cu butoanele „Apply" și „Cancel".

**Acțiuni Automate / Acțiuni Server**

- `action_account_invoice_change_number_server`: acțiune de server legată de formularul facturii (`account.move`), vizibilă doar grupului `group_change_invoice_number`, care deschide wizardul de schimbare a numărului.

#### 5. Conexiuni

- `account`: modulul de bază de contabilitate peste care se extinde numerotarea facturilor.
