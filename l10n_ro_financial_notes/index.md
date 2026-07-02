# Romania - Note Explicative Situații Financiare (localizat la `l10n_ro_financial_notes/index.md`)

- **Nume Tehnic:** `l10n_ro_financial_notes`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_financial_notes
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_financial_notes`
- **Ultima Ingestie:** 2026-06-09
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul care generează Notele explicative 1–10 la situațiile financiare anuale, conform OMFP 1802/2014. Este adresat contabililor și directorilor financiari care trebuie să atașeze notele explicative la bilanțul anual depus la ANAF. O parte dintre note sunt calculate automat din înregistrările contabile la data de referință (active imobilizate, provizioane, analiza rezultatului din exploatare, scadențarul creanțelor și datoriilor), iar restul oferă câmpuri de completare manuală. Toate cele 10 note se exportă într-un singur document PDF gata de atașat la dosarul de situații financiare anuale.

#### 2. Funcționalități Cheie

- **Note calculate automat din contabilitate:**
  - **Nota 1** — Active imobilizate: mișcări (intrări, ieșiri) și amortizare per categorie (necorporale `20x`/`280x`, corporale `21x`/`281x`, financiare `26x`/`296x`).
  - **Nota 2** — Provizioane: constituiri, utilizări și anulări per cont `151x`.
  - **Nota 4** — Analiza rezultatului din exploatare: venituri și cheltuieli pe categorii (`6xx`/`7xx`).
  - **Nota 5** — Creanțe și datorii: scadențar (sub 1 an / 1–5 ani / peste 5 ani) din soldurile nereconciliate la data de referință.
- **Note cu completare manuală:**
  - **Nota 3** — Repartizarea profitului (câmpuri numerice).
  - **Nota 6** — Principii și politici contabile (text — precompletat cu text standard OMFP 1802).
  - **Nota 7** — Participații și surse de finanțare (câmpuri numerice).
  - **Nota 8** — Salariați și organe de administrare (câmpuri numerice).
  - **Nota 9** — Exemple de calcul (text liber).
  - **Nota 10** — Alte informații (text liber).
- **Export PDF unic** cu toate cele 10 note, gata de atașat la dosarul de situații financiare anuale.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.financial.notes`: modelul principal care agregă cele 10 note, combinând valorile calculate din soldurile contabile cu câmpurile de completare manuală. Moștenește `mail.thread` și `mail.activity.mixin` (chatter și activități în formular).
- `l10n.ro.financial.notes.asset.line`: liniile mișcării activelor imobilizate (Nota 1).
- `l10n.ro.financial.notes.provision.line`: liniile provizioanelor (Nota 2).
- `l10n.ro.financial.notes.aging.line`: liniile scadențarului creanțelor și datoriilor (Nota 5).

**Vizualizări**

- `views/l10n_ro_financial_notes_view.xml`: vizualizările (listă, formular cu chatter) ale notelor explicative.

**Acțiuni Automate / Acțiuni Server**

- `report/l10n_ro_financial_notes_report.xml`, `report/l10n_ro_financial_notes_template.xml`: raportul PDF unic cu cele 10 note. Notele calculate automat se generează la cerere din soldurile contabile la data de referință.

#### 5. Conexiuni

- [l10n_ro_financial_statements](../l10n_ro_financial_statements/index.md): situațiile financiare anuale pe care notele explicative le însoțesc.
- [l10n_ro_fixed_assets](../l10n_ro_fixed_assets/index.md): date despre imobilizări și amortizare, corelate cu Nota 1.
- [l10n_ro_provisions](../l10n_ro_provisions/index.md): date privind provizioanele, corelate cu Nota 2.
- [l10n_ro_dividends](../l10n_ro_dividends/index.md): repartizarea profitului, corelată cu Nota 3.
