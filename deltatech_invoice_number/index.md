# Invoice Number (localizat la `deltatech_invoice_number/index.md`)

- **Nume Tehnic:** `deltatech_invoice_number`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_invoice_number
- **Cale Locală:** `odoo-addons/deltatech/deltatech_invoice_number`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul asigură renumerotarea și controlul secvenței facturilor de vânzare, garantând că facturile sunt validate în ordine cronologică și oferind utilizatorilor autorizați posibilitatea de a corecta manual numărul unei facturi sau de a atribui un număr dintr-o secvență dedicată a jurnalului, direct din starea de ciornă.

#### 2. Funcționalități Cheie

- Validează ordinea cronologică a facturilor emise (nu permite validarea unei facturi cu dată anterioară ultimei facturi confirmate pe același jurnal).
- Permite modificarea numărului unei facturi pentru un grup dedicat de utilizatori.
- Permite numerotarea unei facturi aflate în starea de ciornă, folosind o secvență configurată la nivel de jurnal.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.move` (extindere): adaugă verificarea ordinii cronologice (`check_data`), acțiunea `action_get_number` pentru alocarea unui număr din secvența jurnalului pe o factură în ciornă și `action_number` pentru sincronizarea referinței (`ref`) facturii și a liniilor sale după o renumerotare manuală; suprascrie `action_post` pentru a bloca postarea facturilor de client în afara ordinii cronologice dacă jurnalul are bifat `restrict_date`.
- `account.journal` (extindere): adaugă câmpurile `journal_sequence_id` (secvența folosită pentru numerotarea facturilor) și `restrict_date` (activează restricția de ordine cronologică).
- `account.invoice.change.number` (model tranzitoriu — wizard): permite introducerea manuală a unui nou număr de factură și sincronizarea acestuia prin `do_change_number`.

**Vizualizări**

- `journal_restrict_date_form`: extinde formularul jurnalului contabil (`account.view_account_journal_form`) cu grupul „Invoice numbering", vizibil doar pentru jurnalele de vânzare, unde se configurează `journal_sequence_id` și `restrict_date`.
- `view_account_invoice_change_number_form`: formular wizard pentru introducerea noului număr de factură, cu butoane „Apply" și „Cancel".

**Acțiuni Automate / Acțiuni Server**

- `action_account_invoice_change_number_server`: acțiune de server legată de formularul facturii (`account.move`), vizibilă doar grupului `group_change_invoice_number`, care deschide wizard-ul de schimbare a numărului de factură.

#### 5. Conexiuni

- `account`: modulul de bază contabilitate peste care se extinde numerotarea facturilor.

---
