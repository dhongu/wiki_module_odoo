# Cont Corespondent în Grand Livre (localizat la `l10n_ro_journal_reports/index.md`)

- **Nume Tehnic:** `l10n_ro_journal_reports`
- **Versiune:** `19.0.2.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_journal_reports
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_journal_reports`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul completează Cartea Mare standard din Odoo Enterprise (General Ledger din `account_reports`) cu coloana **Cont Corespondent**, cerută de OMFP 1802/2014 (art. 7 și art. 9). Acoperă exclusiv acest decalaj real față de reglementarea românească, lăsând Registrul Jurnal și Cartea Mare de bază pe seama rapoartelor standard Odoo, fără a duplica funcționalitate.

#### 2. Funcționalități Cheie

- Coloana "Cont Corespondent" apare automat în Cartea Mare, imediat după coloana Credit.
- Pentru un singur cont corespondent afișează codul acestuia; pentru conturi multiple afișează "Diverși", conform standardului OMFP 1802.
- Calcul SQL în batch pe toate liniile vizibile, evitând interogările N+1.
- Funcționează atât la desfășurarea (unfold) interactivă, cât și la exportul PDF/XLSX.
- Temei legal: OMFP 1802/2014, art. 7 (Registrul-jurnal) și art. 9 (Cartea mare).

#### 3. Dependențe

- `account_reports`
- `[[l10n_ro]]`

#### 4. Componente Cheie

**Modele**

- Extinde handlerul raportului General Ledger din `account_reports` pentru a injecta și calcula coloana Cont Corespondent.

**Vizualizări / Date**

*Modulul nu adaugă fișiere de date noi; coloana este injectată programatic în raportul standard.*

**Acțiuni Automate / Acțiuni Server**

*Nu există acțiuni automate.*

#### 5. Conexiuni

- `[[l10n_ro_journal_tva]]`
- `[[l10n_ro_partner_ledger_currency]]`
