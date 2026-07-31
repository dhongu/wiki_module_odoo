# Corecție Rapoarte Contabile RO (localizat la `l10n_ro_reports_fix/index.md`)

- **Nume Tehnic:** `l10n_ro_reports_fix`
- **Versiune:** `19.0.0.0.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_reports_fix
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_reports_fix`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

## 1. Sumar

Acest modul corectează raportul **Balanță de verificare cu 5 coloane** din `l10n_ro_reports` pentru a calcula corect soldul final (debitor/creditor) al conturilor contabile, conform naturii fiecărui cont din planul de conturi românesc. În plus, adaugă opțiunea **Raw trial balance** care afișează balanța fără linia tehnică Odoo „Result Brought Forward", utilă la migrarea soldurilor sau la compararea cu o balanță primită de la contabil.

## 2. Funcționalități Cheie

- **Corectarea soldului final:** Soldul final se calculează ca diferență debit-credit; dacă `l10n_ro_usage` este instalat, conturile active afișează soldul pe debit, iar cele pasive pe credit.
- **Recalcularea grupurilor:** Valorile corectate se propagă corect în ierarhia de grupuri de conturi, la fiecare nivel.
- **Recalcularea totalului general** pe baza soldurilor finale corectate.
- **Afișare brută (Raw trial balance):** Elimină linia dinamică „Result Brought Forward", afișând soldurile reale din `account.move.line`, ideală pentru verificări de migrare și comparații cu balanțe externe.
- Respectă cele patru egalități ale balanței românești și permite agregarea sintetică/analitică pe clase și niveluri de cont.

## 3. Dependențe

- `l10n_ro_reports`

## 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, modulul corectează logica raportului de balanță și adaugă opțiunea „Raw trial balance".

**Assets**

- `static/src/components/account_report/filters/filters.esm.js`: Componentă frontend (OWL) care adaugă filtrul/bifa pentru afișarea brută în interfața raportului.

### Acțiuni Automate / Acțiuni Server

*Nu sunt definite acțiuni automate; modulul intervine pe motorul de raportare și pe interfața raportului.*

## 5. Conexiuni

- `[[l10n_ro_account_chart]]`
- `[[l10n_ro_account_fisa_cont]]`
