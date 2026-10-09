# Deltatech Cash Statement Extension (localizat la `deltatech_cash_statement/index.md`)

- **Nume Tehnic:** `deltatech_cash_statement`
- **Versiune:** `19.0.3.1.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_cash_statement
- **Cale Locală:** `odoo-addons/deltatech/deltatech_cash_statement`
- **Ultima Ingestie:** `2026-10-09`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul păstrează soldurile extraselor de casă în acord cu contabilitatea și înregistrează o diferență de numerar constatată la inventar ca o operațiune datată și documentată, în loc să suprascrie tăcut un sold. Este util responsabililor de contabilitate și casierilor, pentru că orice diferență între numerarul numărat și soldul contului de casă rămâne vizibilă și justificată printr-o notă contabilă, iar soldurile se reportează automat de la un extras la următorul.

#### 2. Funcționalități Cheie

- **Asistent pe lista extraselor**: se deschide din lista extraselor bancare/de casă, prin **Acțiune → Cash Update Balances**, pe unul sau mai multe extrase selectate. Extrasele trebuie să aparțină unui singur jurnal, altfel asistentul refuză operațiunea.
- **Mod „Aliniere cu soldul contabil”** (implicit): soldul inițial al primului extras selectat devine soldul contului de casă din notele postate, datate înaintea extrasului, iar fiecare extras următor pornește de la soldul final real al celui dinainte. Extrasele se actualizează în ordine cronologică; nu se creează nicio notă contabilă.
- **Mod „Înregistrare diferență de casă”**: operatorul introduce **soldul numărat** (numerarul efectiv la începutul zilei), iar asistentul calculează diferența față de soldul contabil și adaugă pe extras o linie datată la data inventarului, cu nota contabilă deja postată. Apoi soldurile se aliniază.
  - Contul de contrapartidă: la o firmă din România, implicit 7588 pentru plus și 6588 pentru minus; în alte țări, conturile de diferență de casă ale jurnalului (profit/pierdere). Contul poate fi schimbat, de exemplu pe 4282 când lipsa se imputează casierului.
  - Dacă lipsa se imputează (cont de creanță sau 428x), este obligatorie **persoana responsabilă**, astfel încât creanța să fie urmărită pe acel partener.
  - Data diferenței nu poate fi anterioară extrasului (ar fi numărată de două ori), iar eticheta liniei este editabilă.
- **Fără suprascriere arbitrară a soldului**: o diferență reală nu se mai poate ascunde prin tastarea unui sold; se corectează doar printr-o înregistrare datată. Asta respectă regula că orice operațiune de casă are document justificativ și reportarea automată a soldurilor.
- **Notă fiscală**: o lipsă neimputată (6588) este, de regulă, cheltuială nedeductibilă la impozitul pe profit; se verifică cu contabilul.
- **Fișă consultant** (în română) cu pașii de aliniere a registrelor de casă și de înregistrare a unei diferențe la inventar, cu capturi de ecran.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.cash.update.balances` (model tranzitoriu): asistentul. Câmpuri principale: `mode` (align / difference), `balance_start`, `accounting_balance` (calculat prin SQL din liniile postate ale contului implicit al jurnalului, datate înainte de extras, în moneda jurnalului dacă e străină), `counted_balance`, `difference`, `date`, `counterpart_account_id` (calculat, editabil), `partner_id`, `label`. Metoda `do_update_balance` creează, dacă e cazul, linia de diferență (pe `account.bank.statement.line`) și realiniază lanțul de solduri.

**Vizualizări**

- `view_account_cash_update_balances_form`: formularul asistentului, cu alegerea modului, soldurile și, în modul diferență, soldul numărat, diferența, data, contul, persoana responsabilă și eticheta.
- `action_account_cash_update_balances`: acțiune de fereastră legată (binding) de `account.bank.statement`, doar pe vizualizarea listă, afișată în meniul **Acțiune**.

**Acțiuni Automate / Acțiuni Server**

- Nu există acțiuni automate sau acțiuni server.

#### 5. Conexiuni

Nu au fost identificate conexiuni către alte module documentate în wiki. Singura dependență este modulul standard `account`.
