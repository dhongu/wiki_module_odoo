# Romania - Cont corespondent în Cartea mare (localizat la `l10n_ro_journal_reports/index.md`)

- **Nume Tehnic:** `l10n_ro_journal_reports`
- **Versiune:** `19.0.2.0.6`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_journal_reports
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_journal_reports`
- **Ultima Ingestie:** `2026-10-26`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul completează Cartea Mare standard din Odoo Enterprise (General Ledger din `account_reports`) cu coloana **Cont Corespondent**, cerută de OMFP 1802/2014 (art. 7 și art. 9). Acoperă exclusiv acest decalaj real față de reglementarea românească, lăsând Registrul Jurnal și Cartea Mare de bază pe seama rapoartelor standard Odoo, fără a duplica funcționalitate.

#### 2. Funcționalități Cheie

- Coloana "Cont Corespondent" apare automat în Cartea Mare (**Contabilitate → Raportare → Cartea Mare**), imediat după coloana Credit; la nivel de cont este goală, iar pe liniile de mișcare se completează.
- Pentru o linie debitoare, corespondentul este contul creditor din aceeași notă contabilă, și invers. Pentru un singur cont corespondent afișează codul acestuia (codul complet la conturi analitice); pentru conturi multiple afișează "Diverși", conform standardului OMFP 1802.
- Coloana este pur informativă: nu modifică solduri sau înregistrări.
- Calcul SQL în batch pe toate liniile vizibile, evitând interogările N+1.
- Funcționează atât la desfășurarea (unfold) interactivă, cât și la exportul PDF/XLSX.
- Nu necesită configurare; utilizatorul trebuie să aibă acces la rapoartele contabile (grupul Contabilitate: Contabil sau Utilizator financiar).
- Temei legal: OMFP 1802/2014, art. 7 (Registrul-jurnal) și art. 9 (Cartea mare).

#### 3. Dependențe

- `account_reports`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.general.ledger.report.handler` (extins în `models/l10n_ro_general_ledger.py`, clasa `L10nRoGeneralLedgerReportHandler`): injectează coloana Cont Corespondent în raportul General Ledger și calculează codurile conturilor corespondente în batch.

**Vizualizări**

*Modulul nu adaugă fișiere de date noi (`data` este gol); coloana este injectată programatic în raportul standard.*

**Acțiuni Automate / Acțiuni Server**

*Nu există acțiuni automate.*

#### 5. Conexiuni

- [l10n_ro_anaf_d394](../l10n_ro_anaf_d394/index.md): jurnalele de TVA vânzări/cumpărări (cu coloane pe cote) sunt acum aici; au înlocuit fostul `l10n_ro_journal_tva`, eliminat.
- [l10n_ro_partner_ledger_currency](../l10n_ro_partner_ledger_currency/index.md): raport complementar pentru fișa partenerului în valută.
