# Invoice Numbering Control (localizat la `deltatech_invoice_number/index.md`)

- **Nume Tehnic:** `deltatech_invoice_number`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_invoice_number
- **Cale Locală:** `odoo-addons/deltatech/deltatech_invoice_number`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul păstrează facturile de client în ordine cronologică pe jurnalele unde acest lucru contează și permite unui grup dedicat de utilizatori să corecteze numărul unei facturi.

#### 2. Funcționalități Cheie

- **Date cronologice ale facturilor:** pe un jurnal de vânzări cu opțiunea *Restrict invoice date* activă, o factură sau o notă de credit în ciornă nu poate fi confirmată cu o dată anterioară ultimului document postat de același tip din jurnal. Eroarea indică cea mai veche dată permisă; la alegerea jurnalului pe factura în ciornă apare un avertisment cu aceeași informație.
- **Schimbarea numărului facturii:** utilizatorii din grupul *Allow to change invoice number* primesc acțiunea **Change invoice number** în meniul Acțiuni al facturii. Asistentul propune numărul curent; după **Apply**, noul număr se scrie pe factură și se copiază în referința articolelor contabile (și în *Reference* pentru documentele de client).
- **Configurare:** *Accounting > Configuration > Journals*, jurnal de tip *Sales*, fila **Journal Entries**, secțiunea **Invoice numbering** (*Restrict invoice date*); grupul se acordă din *Settings > Users & Companies > Groups*.
- **Limitări:** câmpul *Journal Sequence* din secțiunea Invoice numbering nu are efect în interfață (nicio acțiune nu apelează metoda de numerotare), iar noul număr se scrie exact cum a fost tastat, fără verificarea formatului jurnalului sau a golurilor.

Fluxul pas-cu-pas se găsește în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.journal` (extins): opțiunea *Restrict invoice date* și câmpul de secvență din secțiunea Invoice numbering.
- `account.move` (extins): verificarea cronologiei datei facturii la confirmare și avertismentul la schimbarea jurnalului.
- `account.invoice.change.number` (model tranzitoriu): asistentul de schimbare a numărului facturii.

**Vizualizări**

- `journal_restrict_date_form`: adaugă secțiunea Invoice numbering pe formularul jurnalului.
- `view_account_invoice_change_number_form`: formularul asistentului Change invoice number.

**Acțiuni Automate / Acțiuni Server**

- `action_account_invoice_change_number_server`: acțiunea de server **Change invoice number** din meniul Acțiuni al facturii (vizibilă pentru grupul dedicat).
- `action_account_invoice_change_number`: acțiunea de fereastră care deschide asistentul.

#### 5. Conexiuni

- `account`: modulul de bază de contabilitate peste care se extinde numerotarea facturilor.
