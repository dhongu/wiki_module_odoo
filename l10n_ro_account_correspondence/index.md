# Romania - Cont corespondent (localizat la `l10n_ro_account_correspondence/index.md`)

- **Nume Tehnic:** `l10n_ro_account_correspondence`
- **Nume anterior:** `l10n_ro_account_counterpart` (redenumit pe 23.09.2026: numele vechi e ocupat pe Odoo Apps de alt furnizor)
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_account_correspondence
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_account_correspondence`
- **Ultima Ingestie:** `2026-11-26`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă pe fiecare poziție contabilă (`account.move.line`) contul corespondent
(cont contrapartidă, conform OMFP 1802/2014), util pentru fișele de cont, registrul-jurnal
și verificarea notelor contabile.

#### 2. Funcționalități Cheie

- Pentru fiecare linie de notă contabilă: dacă pe partea opusă (debit ↔ credit) există un
  singur cont distinct, se completează acel cont și codul lui.
- Dacă există mai multe conturi distincte pe partea opusă, se afișează eticheta „Diverși"
  (*Various*).
- Liniile fără mișcare (secțiuni, note fără sumă) rămân fără corespondent.
- Câmpurile sunt stocate și calculate (recalculate automat la modificarea liniilor notei),
  deci pot fi folosite la grupare, filtrare și în rapoarte.
- Nu necesită configurare: coloana **Cont corespondent** apare automat în Contabilitate → Contabilitate → Poziții contabile (lângă contul liniei) și în tabelul de linii al unei note contabile postate; este informativă, nu schimbă monografia. Câmpurile se calculează la postarea sau modificarea notelor; utilizatorul are nevoie de acces la Contabilitate (grupul „Contabil”).
- Pe o notă cu două linii, linia de debit arată codul contului de credit și invers (de exemplu, la 5121 debit și 4111 credit, linia 5121 arată 4111, iar linia 4111 arată 5121), așa că perechea contabilă se verifică direct din listă; „Diverși” indică o corespondență „unul-la-mai-mulți” (de exemplu o linie de bancă față de mai multe conturi de cheltuială).
- Filtrare și grupare: câmpurile stocate pot fi folosite la filtrare (de exemplu „Cont corespondent = 401”), la grupare în vizualizările pivot sau grafic și în rapoarte (Cartea Mare sau registrul-jurnal din `l10n_ro_journal_reports`). Contul corespondent complet (un singur cont) e în aceeași listă, ascuns implicit, în meniul de coloane opționale.
- Redenumit din `l10n_ro_account_counterpart` (19.0.1.0.1): numele vechi e folosit pe Odoo Apps de alt furnizor; modelele, câmpurile și funcționalitatea au rămas neschimbate. Pe o bază cu modulul vechi instalat, `ir_module_module`, `ir_module_module_dependency` și `ir_model_data` trebuie redenumite prin SQL înainte de actualizare (pașii exacți sunt în `readme/HISTORY.md`), apoi `-u l10n_ro_account_correspondence`.
- Complementar modulului [l10n_ro_journal_reports](../l10n_ro_journal_reports/index.md), care
  afișează contul corespondent ca o coloană în Cartea Mare (Grand Livre) — acest modul îl
  persistă la nivel de linie.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.move.line` (extindere): adaugă câmpurile calculate și stocate
  `l10n_ro_counterpart_account_id` (contul corespondent, populat doar când există un singur
  cont distinct pe partea opusă) și `l10n_ro_counterpart_code` (codul contului corespondent
  sau eticheta „Various" pentru conturi multiple), calculate prin `_compute_l10n_ro_counterpart`
  pe baza metodei `_l10n_ro_get_counterpart`.

**Vizualizări**

- `view_move_line_tree_counterpart`: extinde lista standard de poziții contabile
  (`account.view_move_line_tree`) adăugând după coloana `account_id` coloana
  `l10n_ro_counterpart_code` (vizibilă implicit) și `l10n_ro_counterpart_account_id`
  (opțională, ascunsă implicit).

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

- [l10n_ro_journal_reports](../l10n_ro_journal_reports/index.md): afișează contul corespondent
  calculat dinamic în Cartea Mare (Grand Livre); modulul de față persistă aceeași informație
  la nivel de linie (`account.move.line`), permițând filtrare/grupare/raportare fără recalcul.
