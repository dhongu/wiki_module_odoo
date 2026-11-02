# Romania - Repartizarea cheltuielilor indirecte pe centre de cost (localizat la `l10n_ro_cost_centers/index.md`)

- **Nume Tehnic:** `l10n_ro_cost_centers`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_cost_centers
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_cost_centers`
- **Ultima Ingestie:** `2026-11-02`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul automatizează repartizarea cheltuielilor indirecte pe centre de cost (conturi analitice), conform contabilității de gestiune din România (OMFP 1802/2014). Costurile colectate pe un centru comun sau indirect se redistribuie pe centrele productive printr-o notă contabilă cu impact financiar zero pe contul de cheltuială (creditul 6xx de pe centrul comun este egal cu debitele 6xx de pe centrele țintă): costul se mută doar pe dimensiunea analitică, fără a folosi obligatoriu conturile din clasa 9. Este un instrument de control de gestiune, neutru financiar, care nu modifică balanța contabilă. Este un modul nou în 19.0.

#### 2. Funcționalități Cheie

- Repartizarea cheltuielilor indirecte de pe un centru de cost sursă (comun/indirect) pe mai multe centre țintă (productive).
- Cheie de repartizare configurabilă: **manual** (procente fixe, care trebuie să însumeze 100%), **suprafață** (m²), **nr. angajați** sau **cifră de afaceri** (rulajul creditor al conturilor de venituri 7xx de pe fiecare centru țintă, în perioadă).
- Câmpuri proprii pe centrul de cost (cont analitic): **Suprafață (m²)** și **Nr. angajați**, folosite ca baze de repartizare.
- Flux de lucru, în *Contabilitate → Contabilitate → Repartizare costuri indirecte*:
  - se completează centrul sursă, conturile de cheltuieli 6xx repartizate, jurnalul de tip Diverse (obligatoriu), perioada, cheia de repartizare și centrele țintă;
  - **Calculează** colectează totalul de pe centrul sursă în perioadă (**Total de repartizat**) și calculează procentele și sumele pe fiecare centru țintă;
  - **Postează nota** generează, pentru fiecare cont de cheltuială, o notă de redistribuire analitică echilibrată: o linie scoate costul de pe centrul comun, iar câte o linie îl încarcă pe fiecare centru țintă, cu distribuție analitică 100%;
  - **Anulează** readuce repartizarea în ciornă și anulează nota generată; **Resetare la ciornă** permite reluarea.
- Utilizatorul care postează repartizările are nevoie de grupul **Contabilitate / Contabil**; cheltuielile de repartizat trebuie să fie deja postate pe centrul sursă, cu distribuție analitică.
- Rezultatul se vede în rapoartele analitice native (profit și pierdere pe centre de cost). Planurile analitice ierarhice, distribuția analitică obligatorie la postare, bugetele pe centre și rapoartele P&L pe dimensiuni rămân acoperite de baza nativă Odoo (analytic + Enterprise `account_budget` / `account_reports`).
- Pașii detaliați, cu capturi de ecran, sunt în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `analytic`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.cost.allocation`: repartizarea (sursă, conturi, perioadă, cheie, stare, notă contabilă generată); conține acțiunile de calcul, postare, anulare și resetare.
- `l10n.ro.cost.allocation.line`: linia unui centru țintă, cu valoarea bazei, procentul și suma repartizată.
- `account.analytic.account`: extins cu `l10n_ro_surface_m2` (suprafață) și `l10n_ro_headcount` (număr de angajați).

**Vizualizări**

- `view_l10n_ro_cost_allocation_form` / `view_l10n_ro_cost_allocation_list`: formularul și lista repartizărilor, cu meniul și acțiunea `action_l10n_ro_cost_allocation`.
- `view_account_analytic_account_form_ro_cc`: adaugă suprafața și numărul de angajați pe centrul de cost.

**Acțiuni Automate / Acțiuni Server**

- Nu există acțiuni `ir.cron`, `base.automation` sau `ir.actions.server`; modulul definește doar secvența `seq_l10n_ro_cost_allocation` pentru numerotarea repartizărilor.

#### 5. Conexiuni

- `account_budget` (Enterprise): bugete pe centre de cost — nativ, opțional, necuplat de modul.
- `account_reports` (Enterprise): rapoarte P&L pe dimensiuni analitice — nativ, opțional.
