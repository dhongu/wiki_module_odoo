# Romania - Asistent import e-Factura (verificare față de comandă) (localizat la `l10n_ro_efactura_import_assist/index.md`)

- **Nume Tehnic:** `l10n_ro_efactura_import_assist`
- **Versiune:** `19.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_efactura_import_assist
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_efactura_import_assist`
- **Ultima Ingestie:** `2026-11-25`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă un control intern pentru facturile furnizor importate din SPV: atunci când o factură este legată de o comandă de achiziție, este confruntată linie cu linie cu comanda pe cantitate și preț. Dacă apar diferențe peste toleranțele acceptate, postarea facturii este blocată până când operatorul ia o decizie explicită — acceptă cu ajustare sau refuză, caz în care factura se anulează în Odoo și furnizorul poate fi notificat prin e-mail cu tabelul diferențelor. Modulul nu transmite un refuz în SPV.

#### 2. Funcționalități Cheie

- Verificare automată la import a facturilor SPV legate de o comandă de achiziție: compară **cantitatea** (față de rămasul de facturat — recepționat sau comandat, în funcție de politica de facturare a produsului, minus ce s-a facturat deja) și **prețul unitar** (față de linia din comandă), cu **toleranțe procentuale configurabile pe companie**.
- Toleranțele se setează în **Setări → Facturare**, secțiunea **SPV Import Assistant (PO Discrepancy Check)** (*Quantity Tolerance* și *Price Tolerance*, în procente; implicit 0, deci orice diferență e semnalată).
- Facturile descărcate din SPV (automat sau cu **Sincronizează cu ANAF** din *Facturare → Furnizori → Facturi*) sunt verificate la import.
- La diferențe peste toleranțe, factura intră în starea **„În așteptarea deciziei"**: postarea (manuală sau automată) este blocată cu mesajul „Operație invalidă", apare un banner de avertizare pe factură și o activitate pentru responsabilul facturii; diferențele de tip **Cantitate**, **Preț unitar** și **Linie inexistentă în comandă** sunt listate în fila **„Discrepanțe SPV"**.
- Wizard **Decizie discrepanțe SPV**, accesibil din butonul **Revizuiește discrepanțele**:
  - **Acceptă cu ajustare (permite postarea)** — starea devine *Acceptată cu ajustare* și factura se poate confirma, cu nota contabilă standard a facturii furnizor; se acceptă doar factura așa cum a emis-o furnizorul — pentru acceptare parțială, factura se refuză și se cere furnizorului una corectată;
  - **Refuză (anulează factura și notifică furnizorul)** — factura se anulează, starea devine *Refuzată*, iar cu bifa **Trimite e-mail de notificare furnizorului** furnizorul primește tabelul diferențelor.
- Fila **Discrepanțe SPV** păstrează diferențele acceptate sau refuzate ca evidență.
- Verificare re-rulabilă pe factura ciornă cu diferențe semnalate (**Re-verifică discrepanțele**), de exemplu după o recepție nouă.
- Transportul SPV (trimitere, status, recipisă, import inbound) este nativ în `l10n_ro_edi`; modulul adaugă doar stratul de control.

#### 3. Dependențe

- `l10n_ro_edi`
- `purchase`

#### 4. Componente Cheie

Sumarul și Funcționalitățile Cheie provin din `readme/DESCRIPTION.md` și `readme/USAGE.md`; Componentele Cheie de mai jos sunt doar elementele evidente din structura modulului.

**Modele**

- `l10n.ro.edi.discrepancy`: o diferență semnalată pe o linie a facturii față de comandă (tip, valori comparate, stare).
- `account.move` (extins): starea „în așteptarea deciziei", blocarea postării, verificarea față de comandă și acțiunile de revizuire.
- `l10n.ro.edi.discrepancy.decision` (wizard): decizia de acceptare sau refuz, nota deciziei și opțiunea de e-mail către furnizor.
- `res.company` / `res.config.settings` (extinse): toleranțele de cantitate și preț.

**Vizualizări**

- `view_move_form_l10n_ro_import_assist`: bannerul, butonul și fila *Discrepanțe SPV* pe factura furnizor.
- `view_l10n_ro_edi_discrepancy_decision_form`: formularul wizard-ului de decizie.
- `res_config_settings_view_form_import_assist`: toleranțele în Setări.

**Acțiuni Automate / Acțiuni Server**

- `mail_template_spv_discrepancy_refusal`: șablonul de e-mail către furnizor la refuz (nu e cron; modulul nu definește acțiuni automate).

#### 5. Conexiuni

- [l10n_ro_efactura_dedup](../l10n_ro_efactura_dedup/index.md): modul frate care acoperă
  deduplicarea facturilor SPV cu cheie extinsă (CUI + Serie/Nr + Dată + Valoare); acest
  modul se ocupă exclusiv de verificarea cantitate/preț și decizia de acceptare/refuz.
- `l10n_ro_edi`: asigură transportul SPV (trimitere, status, recipisă, import inbound) pe
  care se bazează acest modul.
