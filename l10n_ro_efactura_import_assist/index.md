# Romania - Asistent import e-Factura (verificare față de comandă) (localizat la `l10n_ro_efactura_import_assist/index.md`)

- **Nume Tehnic:** `l10n_ro_efactura_import_assist`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_efactura_import_assist
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_efactura_import_assist`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă un control intern, cu decizie explicită de acceptare sau refuz, pentru facturile furnizor importate din SPV care prezintă diferențe de cantitate sau preț față de comanda de achiziție. Dacă apar diferențe peste toleranțele acceptate, postarea facturii este blocată până când operatorul decide. Refuzul anulează factura în Odoo și notifică furnizorul pe e-mail; modulul nu transmite un refuz în SPV.

Transportul SPV (trimitere, status, recipisă, import inbound) este nativ în `l10n_ro_edi`, iar maparea contabilă asistată din istoric este nativă în Odoo Enterprise. Acest modul adaugă doar stratul de control.

#### 2. Funcționalități Cheie

- Verificare la import a facturilor SPV legate de o comandă de achiziție: compară linie cu linie **cantitatea** (față de rămasul de facturat, recepționat sau comandat, după politica de facturare a produsului) și **prețul unitar** (față de linia comenzii), cu **toleranțe procentuale configurabile pe companie**.
- Toleranțele se setează în **Setări → Facturare**, secțiunea *SPV Import Assistant (PO Discrepancy Check)* (**Quantity Tolerance** și **Price Tolerance**, implicit 0, deci orice diferență este semnalată).
- La diferențe peste toleranțe, factura primește starea **„În așteptarea deciziei"**: postarea (manuală sau automată) este blocată, apare un banner pe factură și o activitate pentru responsabil; liniile cu probleme apar în fila **Discrepanțe SPV** (tipuri: Cantitate, Preț unitar, Linie inexistentă în comandă).
- Asistent **Decizie discrepanțe SPV**, din butonul **Revizuiește discrepanțele**:
  - **Acceptă cu ajustare** deblochează postarea (starea devine *Acceptată cu ajustare*); se acceptă doar factura așa cum a emis-o furnizorul, altfel se refuză și se cere factura corectată;
  - **Refuză** anulează factura, iar cu bifa de notificare furnizorul primește un e-mail cu tabelul diferențelor.
- Verificare re-rulabilă pe factura ciornă cu diferențe semnalate (**Re-verifică discrepanțele**), de exemplu după o recepție nouă.
- Nota contabilă a facturii acceptate rămâne cea standard a facturii furnizor. Fluxul pas cu pas, cu capturi, este în fișa consultantului.

#### 3. Dependențe

- `l10n_ro_edi`
- `purchase`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.edi.discrepancy`: linia de discrepanță detectată (cantitate, preț unitar, linie inexistentă în comandă) pe factură.
- `l10n.ro.edi.discrepancy.decision`: asistentul (wizard) de decizie, acceptare cu ajustare sau refuz, cu notificare opțională a furnizorului.
- `account.move` (extindere): starea deciziei, verificarea față de comandă, blocarea postării și banner-ul.
- `res.company` / `res.config.settings` (extinderi): toleranțele de cantitate și preț.

**Vizualizări**

- `views/account_move_views.xml`: bannerul, butonul **Revizuiește discrepanțele**, fila **Discrepanțe SPV** pe factura furnizor.
- `wizard/discrepancy_decision_views.xml`: formularul asistentului de decizie.
- `views/res_config_settings_views.xml`: setările de toleranță.

**Acțiuni Automate / Acțiuni Server**

- `data/mail_template.xml`: șablonul de e-mail către furnizor (tabelul diferențelor) la refuz. Nu există `ir.cron`.

#### 5. Conexiuni

- [l10n_ro_efactura_dedup](../l10n_ro_efactura_dedup/index.md): modul frate pentru deduplicarea facturilor SPV cu cheie extinsă (CUI + Serie/Nr + Dată + Valoare); acest modul se ocupă doar de verificarea cantitate/preț și de decizie.
- `l10n_ro_edi`: asigură transportul SPV pe care se bazează modulul.
