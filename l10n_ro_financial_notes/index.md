# Romania - Note Explicative Situații Financiare (localizat la `l10n_ro_financial_notes/index.md`)

- **Nume Tehnic:** `l10n_ro_financial_notes`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_financial_notes
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_financial_notes`
- **Ultima Ingestie:** 2026-06-01

## 1. Sumar

Modul care generează automat Notele explicative 1–10 la situațiile financiare anuale, conform OMFP 1802/2014. O parte dintre note sunt calculate automat din soldurile contabile (active imobilizate, provizioane, rezultat din exploatare, creanțe și datorii), iar restul oferă câmpuri de completare manuală, totul exportabil într-un singur document PDF gata de atașat la dosarul de situații financiare anuale.

## 2. Funcționalități Cheie

- **Note calculate automat:** Nota 1 (active imobilizate — mișcări și amortizare per categorie), Nota 2 (provizioane per cont 151x), Nota 4 (analiza rezultatului din exploatare 6xx/7xx), Nota 5 (creanțe și datorii cu scadențar din soldurile nereconciliate).
- **Note cu completare manuală:** Nota 3 (repartizarea profitului), Nota 6 (principii și politici contabile — precompletată), Nota 7 (participații și surse de finanțare), Nota 8 (salariați și organe de administrare), Nota 9 (exemple de calcul), Nota 10 (alte informații).
- **Export PDF unic** cu toate cele 10 note, gata de atașat la dosarul de situații financiare anuale.

## 3. Dependențe

- `account`
- `l10n_ro`

## 4. Componente Cheie

### Modele

- Model note explicative: agregă cele 10 note, combinând valorile calculate din soldurile contabile cu câmpurile de completare manuală.

### Vizualizări / Date

- `views/l10n_ro_financial_notes_view.xml`: vizualizările notelor explicative.
- `report/l10n_ro_financial_notes_report.xml`, `report/l10n_ro_financial_notes_template.xml`: raportul PDF unic cu cele 10 note.

### Acțiuni Automate / Acțiuni Server

*Notele calculate automat se generează la cerere din soldurile contabile la data de referință.*

## 5. Conexiuni

- `[[l10n_ro_financial_statements]]`
- `[[l10n_ro_dividends]]`
- `[[l10n_ro_fixed_assets]]`
