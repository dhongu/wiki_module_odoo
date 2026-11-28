# Romania - Corecții rapoarte contabile (localizat la `l10n_ro_reports_fix/index.md`)

- **Nume Tehnic:** `l10n_ro_reports_fix`
- **Versiune:** `20.0.0.0.11`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_reports_fix
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_reports_fix`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul corectează raportul Balanța de verificare cu 4 și 5 coloane (`l10n_ro_reports`), astfel încât soldul final al fiecărui cont să apară pe coloana corectă (debit sau credit), conform contabilității românești (OMFP 1802/2014). Raportul standard poate plasa soldul unui cont pe coloana greșită, ceea ce face balanța inacceptabilă pentru auditori sau ANAF. Se adresează contabililor care pregătesc balanța pentru situațiile financiare sau pentru audit, inclusiv firmelor cu conturi bifuncționale.

#### 2. Funcționalități Cheie

- Corectarea soldului inițial și final: o singură coloană pe cont; cu `l10n_ro_storno_enhancement` instalat se ține cont de natura contului (activ doar Debit, pasiv doar Credit), altfel soldul net merge pe coloana corespunzătoare.
- Recalcularea totalului general pe baza soldurilor corectate.
- Opțiunea „Balanță brută" (Raw trial balance): scoate linia tehnică „Result Brought Forward" și folosește doar soldurile conturilor reale.
- Conturile extrabilanțiere, în trei variante din meniul Opțiuni: implicit (clasa 8 în total, cu contrapartida 803999, pentru reconciliere); „Ascunde conturile extrabilanțiere" (clasele 8 și 9 scoase); „Conturile extrabilanțiere în bloc separat" (grupa 80 sub totalul general, cu subtotal propriu, partidă simplă). Dacă sunt bifate ambele, prevalează „Ascunde".
- Funcționează identic pe balanța sintetică și pe cea analitică; export PDF/XLSX. Fluxul detaliat, cu exemple, este în fișa consultant.

#### 3. Dependențe

- `l10n_ro_reports`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.trial.balance.5.column.report.handler` (extins): Handlerul raportului de balanță cu 5 coloane, cu soldurile finale corectate, totalul recalculat și opțiunile pentru clasa 8.

**Vizualizări**

*Nu există vizualizări proprii; opțiunile se adaugă în meniul Opțiuni al raportului.*

**Acțiuni Automate / Acțiuni Server**

*Nu există acțiuni automate sau acțiuni server.*

#### 5. Conexiuni

- [l10n_ro_storno_enhancement](../l10n_ro_storno_enhancement/index.md): câmpul `l10n_ro_usage` (natura contului) folosit opțional la reclasificarea soldurilor.
- `account_reports`: framework-ul Enterprise de raportare pe care se sprijină balanța.
