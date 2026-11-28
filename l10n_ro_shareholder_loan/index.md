# Romania - Împrumuturi de la asociați (contract de creditare, 455) (localizat la `l10n_ro_shareholder_loan/index.md`)

- **Nume Tehnic:** `l10n_ro_shareholder_loan`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_shareholder_loan
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_shareholder_loan`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul ține evidența împrumuturilor primite de societate de la asociați sau acționari, pe baza unui contract de creditare. Încasările de tranșe și rambursările se înregistrează ca de obicei în casă, bancă sau notă contabilă, iar modulul le leagă de contract și arată soldul datorat fiecărui asociat. Contractul se poate tipări în PDF.

#### 2. Funcționalități Cheie

- **Contract de creditare** cu asociatul ales din registrul asociaților, suma convenită, moneda, data, durata în luni, scadența rambursării, dobânda anuală (doar informativă) și destinația împrumutului.
- **Cont implicit după durată:** 45511 pentru împrumuturi de cel mult un an, 45512 pentru cele pe termen mai lung.
- **Stări:** Ciornă → Activ → Închis (sau Anulat); închiderea e permisă doar după rambursarea integrală.
- **Legare automată** a încasărilor (Dr 5311/5121 = Cr 455) și rambursărilor (Dr 455 = Cr 5311/5121) de contractul activ al asociatului, când acesta are un singur contract activ pe contul respectiv.
- **Acțiunea „Contract de creditare”** pe nota contabilă sau linia de extras: leagă operația de un contract existent sau creează contractul direct din ea (cu suma, data și moneda preluate); și butonul **Leagă operații** din contract.
- **Sold pe contract:** primit, restituit, sold datorat și neprimit încă; meniul **Sold pe asociat** arată soldul fiecărui asociat la orice dată.
- **Contract tipărit în PDF**, cu părțile, obiectul, dobânda (sau mențiunea „fără dobândă”), durata, termenul și semnăturile, plus anexa cu sumele primite și restituite.
- Drepturi: Contabil creează și modifică, doar Administratorul contabilității șterge. Fluxul pas cu pas este în fișa consultantului.

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_dividends](../l10n_ro_dividends/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.shareholder.loan`: contractul de creditare cu asociatul (mail.thread, mail.activity.mixin).
- `account.move`, `account.move.line`, `account.bank.statement.line`: extinse cu legătura către contract și acțiunea de legare.
- Wizard `Contract de creditare` (legare de contract existent sau creare din operații).

**Vizualizări**

- `views/l10n_ro_shareholder_loan_views.xml`: listă, formular și meniul Sold pe asociat.
- `views/account_move_views.xml`: legătura cu contractul pe notele contabile.
- `wizard/l10n_ro_shareholder_loan_link_views.xml`: fereastra de legare.
- `report/report_shareholder_loan.xml`: contractul tipărit PDF.

**Acțiuni Automate / Acțiuni Server**

- Secvență `ir.sequence` pentru numerotarea contractelor (`IMPR/an/nr`). Fără cron-uri.

#### 5. Conexiuni

- [l10n_ro_dividends](../l10n_ro_dividends/index.md): registrul asociaților, folosit pentru alegerea împrumutătorului.
