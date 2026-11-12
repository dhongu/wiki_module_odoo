# Custom Invoice Exchange Rate (localizat la `deltatech_account_edit_currency_rate/index.md`)

- **Nume Tehnic:** `deltatech_account_edit_currency_rate`
- **Versiune:** `19.0.1.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_account_edit_currency_rate
- **Cale Locală:** `odoo-addons/deltatech/deltatech_account_edit_currency_rate`
- **Ultima Ingestie:** `2026-11-08`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite introducerea unui curs valutar propriu direct pe factura client sau furnizor în valută. Este util atunci când factura trebuie înregistrată la alt curs decât cel oficial din ziua facturii: cursul BCE în loc de cel BNR, cursul băncii prin care se face decontarea sau cursul din factura furnizorului. Cât timp câmpul este completat, toate valorile în lei (liniile, TVA-ul, totalurile, nota contabilă) se calculează la acel curs; dacă este golit, factura revine la cursul oficial.

#### 2. Funcționalități Cheie

- Câmpul **Curs valutar** (`currency_rate_custom`) apare pe formularul facturii, în tabul **Alte informații**, grupul **Contabilitate**, după **Poziție fiscală**, și doar dacă moneda facturii diferă de cea a companiei.
- Cursul se introduce ca **lei pentru o unitate de valută** (ex. `5,0000`), cu până la 4 zecimale.
- Recalcularea se face și pe server, nu doar în formular: la creare sau modificare prin RPC, import sau ORM se recalculează cursurile liniilor, soldurile în moneda companiei și taxele, ca la editarea din formular.
- Golirea câmpului readuce factura la cursul oficial.
- Pe factura confirmată câmpul este needitabil, iar modificarea este blocată și la scriere; pentru corecție, factura se readuce în ciornă (**Resetare la ciornă**), se schimbă cursul și se confirmă din nou.
- La **duplicarea** facturii cursul propriu nu se copiază; **nota de credit** păstrează cursul facturii originale, ca stornarea să se facă la aceleași valori în lei.
- Diferențele de curs de la încasare sau plată se calculează față de valorile în lei ale facturii (deci față de cursul propriu); baza și TVA-ul în lei ajung în jurnalele de TVA și declarații (D300, D394, SAF-T) cu valorile de la cursul propriu.
- Textul de ajutor al câmpului trimite la art. 290 din Codul fiscal; modulul nu validează cursul ales, răspunderea alegerii rămâne a contabilului.
- Nu adaugă grupuri sau drepturi și nu are setări proprii. Pentru detalii pas cu pas și monografii, vezi [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.move`: adaugă câmpul `currency_rate_custom` (nu se copiază la duplicare), îl folosește în `_compute_invoice_currency_rate` ca să determine cursul nativ al facturii (`invoice_currency_rate`), blochează modificarea lui pe mișcarea postată (`write`) și îl păstrează la stornare (`_reverse_moves`). Pentru înregistrările contabile care nu sunt facturi, `onchange` păstrează recalcularea interactivă a soldurilor.
- `account.move.line`: suprascrie `_compute_currency_rate` și `_inverse_amount_currency` pentru a folosi inversul cursului propriu la calculul soldului în moneda companiei.
- `res.currency`: suprascrie `_convert` pentru a folosi un curs transmis prin contextul `currency_rate`, atunci când este prezent.

**Vizualizări**

- `view_invoice_form_custom_currency_rate`: extinde formularul de factură (`account.view_move_form`) cu câmpul `currency_rate_custom` după poziția fiscală; invizibil când moneda facturii este cea a companiei, readonly când factura este postată.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

Nu au fost identificate module funcțional legate (fără dependențe stricte) în cadrul monorepo-ului.
