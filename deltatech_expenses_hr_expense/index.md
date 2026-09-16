# Expenses Deduction - HR Expense Bridge (localizat la `deltatech_expenses_hr_expense/index.md`)

- **Nume Tehnic:** `deltatech_expenses_hr_expense`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_expenses_hr_expense
- **Cale Locală:** `odoo-addons/deltatech/deltatech_expenses_hr_expense`
- **Ultima Ingestie:** `2026-09-16`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul este o punte între cheltuielile standard de angajați (`hr_expense`) și Decontul de cheltuieli
din avans de trezorerie (`deltatech_expenses`, cont 542), pentru companiile care folosesc ambele
fluxuri și vor să evite dubla contabilizare a acelorași cheltuieli. Se instalează automat, fără
intervenție manuală, doar atunci când ambele module de bază sunt deja prezente în baza de date —
companiile care nu folosesc modulul standard de cheltuieli nu îl primesc și nu văd elemente
suplimentare aduse de `hr_expense`.

#### 2. Funcționalități Cheie

- Buton **„Preia cheltuieli HR"** pe formularul Decontului (vizibil doar în stările Ciornă/Avans):
  deschide un wizard preîncărcat cu cheltuielile `hr.expense` eligibile ale angajatului (aprobate sau
  depuse, fără notă contabilă proprie, nelegate încă de alt decont) și le adaugă ca linii de decont.
- Acțiune contextuală pe lista de cheltuieli standard, „Adaugă în decont de cheltuieli": permite
  selectarea mai multor cheltuieli ale aceluiași angajat și trimiterea lor către un decont ales
  dintr-o listă filtrată (doar deconturile angajatului respectiv, în stare Ciornă sau Avans).
- Cheltuielile `hr.expense` legate de un decont (câmpul `expenses_deduction_id`) nu se mai
  postează prin `action_post` standard — contabilizarea se face exclusiv prin Decont, evitând
  dublarea; formularul cheltuielii arată un banner informativ și ascunde butoanele de postare
  standard cât timp cheltuiala rămâne legată.
- La invalidarea unui decont, liniile importate din `hr.expense` se șterg automat, iar cheltuielile
  respective sunt eliberate — redevin disponibile pentru fluxul standard sau pentru o nouă preluare;
  liniile introduse manual în decont nu sunt afectate.
- Preluarea revalidează explicit eligibilitatea (angajat, companie, stare, absența unei note
  contabile) pe orice set de cheltuieli primit, indiferent de filtrul afișat în wizard, ca protecție
  împotriva unor apeluri directe sau a unor deconturi finalizate/anulate.
- Nu necesită configurare suplimentară — funcționează imediat ce ambele module sunt instalate.

#### 3. Dependențe

- [deltatech_expenses](../deltatech_expenses/index.md)
- `hr_expense`

#### 4. Componente Cheie

**Modele**

- `hr.expense` (extindere): adaugă `expenses_deduction_id` (decontul care preia cheltuiala) și
  suprascrie `action_post` pentru a sări postarea standard a cheltuielilor legate de un decont.
- `deltatech.expenses.deduction` (extindere): adaugă `_eligible_hr_expenses()` (cheltuielile
  eligibile ale angajatului), `_import_hr_expenses()` (creează linii de decont din cheltuieli
  `hr.expense` și le leagă de decont, cu revalidare strictă a eligibilității), acțiunea
  `action_open_import_hr_expenses` (deschide wizard-ul) și suprascrie `_release_imported_lines()`
  pentru a elibera la invalidare cheltuielile preluate din `hr.expense`.
- `deltatech.expenses.deduction.line` (extindere): adaugă `hr_expense_id` (cheltuiala sursă) și
  suprascrie `unlink()` pentru a dezlega automat cheltuiala `hr.expense` de decont la ștergerea
  liniei.
- `deltatech.expenses.import.hr` (wizard, tranzitoriu): pregătește lista de cheltuieli eligibile fie
  pornind dintr-un decont (preîncărcare automată), fie pornind din selecția de pe lista de cheltuieli
  standard (decontul se alege manual), și expune acțiunea de import.

**Vizualizări**

- `view_deltatech_expenses_deduction_form_inherit_hr_expense`: adaugă butonul „Preia cheltuieli HR"
  pe formularul Decontului, vizibil doar în stările Ciornă/Avans.
- `hr_expense_view_form_deduction`: adaugă bannerul informativ pe formularul cheltuielii standard
  când aceasta e legată de un decont și ascunde butoanele de postare standard în acest caz.
- `view_expenses_import_hr_form`: formularul wizard-ului de preluare, cu angajatul (needitabil),
  decontul țintă (filtrat pe angajat și stare) și lista de cheltuieli eligibile de selectat.

**Acțiuni Automate / Acțiuni Server**

- `action_add_expenses_to_deduction`: acțiune contextuală (`binding_model_id` pe `hr.expense`,
  vizibilă în listă) care deschide wizard-ul de import pornind de la cheltuielile selectate de
  utilizator.

#### 5. Conexiuni

- [deltatech_expenses](../deltatech_expenses/index.md): modulul de bază al Decontului de cheltuieli
  (cont 542) — această punte adaugă exclusiv legătura cu cheltuielile standard `hr.expense`.
