# Romania - Cont corespondent (localizat la `l10n_ro_account_correspondence/index.md`)

- **Nume Tehnic:** `l10n_ro_account_correspondence`
- **Nume anterior:** `l10n_ro_account_counterpart` (redenumit pe 23.09.2026: numele vechi e ocupat pe Odoo Apps de alt furnizor)
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_account_correspondence
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_account_correspondence`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă pe fiecare poziție contabilă (`account.move.line`) contul corespondent (cont contrapartidă, conform OMFP 1802/2014), util pentru fișele de cont, registrul-jurnal și verificarea notelor contabile. Informația este afișată direct în lista pozițiilor contabile și nu modifică monografia.

#### 2. Funcționalități Cheie

- Dacă pe partea opusă (debit ↔ credit) a notei există un singur cont distinct, se completează acel cont și codul lui.
- Dacă există mai multe conturi distincte pe partea opusă, se afișează eticheta „Diverși" (*Various*).
- Liniile fără mișcare (secțiuni, note fără sumă) rămân fără corespondent.
- Câmpurile sunt stocate și calculate (recalculate automat la modificarea liniilor notei), deci pot fi folosite la grupare, filtrare și în rapoarte.
- Coloana **Cont corespondent** apare automat în **Contabilitate → Contabilitate → Poziții contabile**; contul complet este o coloană opțională, ascunsă implicit.
- Nu necesită configurare; utilizatorul are nevoie doar de acces la Contabilitate.
- Complementar modulului [l10n_ro_journal_reports](../l10n_ro_journal_reports/index.md), care afișează contul corespondent ca o coloană în Cartea Mare (Grand Livre) — acest modul îl persistă la nivel de linie.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.move.line` (extindere): adaugă câmpurile calculate și stocate `l10n_ro_counterpart_account_id` (contul corespondent, populat doar când există un singur cont distinct pe partea opusă) și `l10n_ro_counterpart_code` (codul contului corespondent sau eticheta „Various" pentru conturi multiple).

**Vizualizări**

- `view_move_line_tree_counterpart`: extinde lista standard de poziții contabile adăugând după coloana `account_id` coloana `l10n_ro_counterpart_code` (vizibilă implicit) și `l10n_ro_counterpart_account_id` (opțională, ascunsă implicit).

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

- [l10n_ro_journal_reports](../l10n_ro_journal_reports/index.md): afișează contul corespondent calculat dinamic în Cartea Mare (Grand Livre); modulul de față persistă aceeași informație la nivel de linie, permițând filtrare/grupare/raportare fără recalcul.
