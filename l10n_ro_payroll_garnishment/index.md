# Romania - Popriri pe salarii (localizat la `l10n_ro_payroll_garnishment/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_garnishment`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_payroll_garnishment
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_garnishment`
- **Ultima Ingestie:** `2026-10-12`

#### 1. Sumar

Modulul face ca reținerile din deciziile primite de angajator (pensie de întreținere, poprire, cesiune) să se oprească pe fluturaș la plafonul legal din venitul net al angajatului, nu la suma din decizie. Fluturașul avertizează când suma cerută depășește ce se poate reține, iar restul rămâne datorat pe ajustarea salarială. Astfel, contabilul de salarii respectă CPC art. 728 și Codul muncii art. 169 fără calcule manuale.

#### 2. Funcționalități Cheie

- Plafoane legale aplicate automat pe venitul net:
  - pensia de întreținere: cel mult 1/2 din venitul net (CPC art. 728 alin. 1 lit. a);
  - poprirea pentru alte datorii: cel mult 1/3 din venitul net (lit. b);
  - toate reținerile la un loc: cel mult 1/2 din venitul net (CPC art. 728 alin. 2; Codul muncii art. 169 alin. 4).
- Ordinea priorităților: întreținere, poprire, cesiune (Codul muncii art. 169 alin. 3); toate regulile se raportează la același net, indiferent de ordinea calculului.
- Sumele reținute se rotunjesc în jos la 0,01.
- Avertizare pe fluturaș când suma cerută depășește ce se poate reține; restul rămâne datorat pe ajustarea salarială cu sumă totală (acțiune directă spre „Ajustări salariale").
- Pe ajustarea salarială se țin numărul dosarului de executare, executorul sau beneficiarul și contul de virare (urmărite în chatter).
- Parametru `salariu_minim_net` (implicit 0 = protecția nu se aplică): sub acest net se poate reține doar partea care depășește jumătate din el; se adaugă o valoare nouă, cu altă dată, la fiecare modificare a salariului minim.
- Neacoperit în versiunea curentă: indemnizațiile de concediu medical (art. 728 alin. 4–5) și veniturile neurmăribile (alin. 7). Statusul modulului: Alpha.

#### 3. Dependențe

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)

#### 4. Componente Cheie

**Modele**

- `hr.salary.attachment` (extins): adaugă numărul dosarului de executare (`l10n_ro_case_number`), executorul/creditorul (`l10n_ro_creditor_id`) și contul de virare (`l10n_ro_creditor_bank_id`, filtrat după creditor).
- `hr.payslip` (extins): calculează netul de referință, împarte sumele cerute/permise pe cele trei tipuri de reținere (`CHILD_SUPPORT`, `ATTACH_SALARY`, `ASSIG_SALARY`) și adaugă avertizările de pe fluturaș.
- `hr.rule.parameter` `l10n_ro_garnishment_params`: parametru pe țară (RO), valabil din 2026-01-01, cu cheia `salariu_minim_net`.

**Vizualizări**

- `hr_salary_attachment_view_form_l10n_ro_garnishment`: moștenește formularul ajustării salariale și adaugă dosarul, creditorul și contul acestuia (vizibil doar cu creditor ales).

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau acțiuni server. Modulul suprascrie prin date regulile salariale din `l10n_ro_hr_payroll` pentru pensia de întreținere, poprire și cesiune, ca să folosească plafonul.

#### 5. Conexiuni

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md): furnizează baza de salarizare și mecanismul de avertizări pe fluturaș.
- `l10n_ro_hr_payroll`: structura salarială și regulile suprascrise.
- `hr_payroll`: ajustările salariale (`hr.salary.attachment`) și fluturașul.
