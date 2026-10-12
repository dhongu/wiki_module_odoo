# Romania - Transparență salarială (Directiva UE 2023/970)

- **Nume Tehnic:** `l10n_ro_hr_pay_transparency`
- **Versiune:** `19.0.0.1.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_hr_pay_transparency
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_hr_pay_transparency`
- **Ultima Ingestie:** `2026-10-12`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Puntea dintre modulul de transparență salarială ([deltatech_hr_pay_transparency](../deltatech_hr_pay_transparency/index.md), Directiva (UE) 2023/970) și salarizarea românească. Directiva numără ca remunerație salariul de bază și orice componentă complementară sau variabilă, în bani sau în natură. Fără această punte, maparea generică ar strica cifrele pentru România: indemnizația de concediu de odihnă ar umfla componenta variabilă, beneficiile s-ar număra de două ori, iar rambursările și diurna ar intra ca remunerație. Modulul mapează fiecare componentă a salarizării RO o singură dată și propune categorii de lucrători pornind de la codul COR.

#### 2. Funcționalități Cheie

- **Maparea componentelor salarizării RO, fiecare o singură dată:**
  - remunerație de bază: salariul de bază (zile lucrate) și indemnizația de concediu de odihnă (`CO_IND`);
  - componentă variabilă: sporuri permanente, ore suplimentare, noapte, sărbători, repaus, prime (`PRIMA`, `PRIMA_NET`), compensarea CO la încetare, concediul medical plătit de angajator (`CM_FS`) și din FNUASS;
  - în natură: tichete de masă, vouchere de vacanță, pensii facultative și ocupaționale, asigurări de sănătate, tichete cadou plătite de angajator (totalul, o singură dată);
  - nu e remunerație: partea neimpozabilă a beneficiilor, excedentul impozabil (`AVANTAJ_ANG`, `CADOU_IMP`), rambursările, diurna (`REIMBURSEMENT`, `DIURNA_IMP`, `DIURNA_NEIMP`), bazele de calcul, contribuțiile, impozitul, avansul, rețineri, netul.
- **Mapare la instalare și pe regulile create ulterior** (de exemplu diurna, după instalarea `l10n_ro_expense_allowance_payroll`), doar unde nu există deja o alegere; o mapare făcută manual rămâne neschimbată.
- **Verificarea mapării** în *Stat de plată → Configurare → Salariu → Categorii de reguli* (coloana *Transparență salarială*) și pe regulile salariale.
- **Asistentul *Categorii din COR*** (*Angajați → Configurare → Transparență salarială → Categorii din COR* sau butonul din lista categoriilor de lucrători): propune câte o categorie pentru fiecare cod COR de pe contractele în curs fără categorie, cu denumirea ocupației din nomenclatorul REGES; operatorul debifează codurile nedorite, poate schimba denumirile și apasă *Creare categorii*, iar categoria se completează pe contracte. Funcția primește categoria doar când toate contractele ei au același cod COR.
- **Flux după creare:** categoriile se evaluează pe cele patru criterii (competențe, efort, responsabilitate, condiții de muncă), apoi se unesc cele cu muncă de aceeași valoare; raportul privind diferențele de remunerare și răspunsurile la cereri iau sumele din fluturașii validați.
- **Limite:** legea română de transpunere nu era adoptată la 11.10.2026 (proiectul L445/2026); profilul *România* din modulul de bază urmează directiva și proiectul, iar termenul de răspuns și formatul raportului către ANES se ajustează la publicarea legii. Tichetele de masă intră în natură, ca în directivă; maparea categoriei *Tichete de masă* se poate schimba din configurare.
- Detaliile pas-cu-pas și capturile sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_hr_pay_transparency_payroll](../deltatech_hr_pay_transparency_payroll/index.md)
- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)
- [l10n_ro_payroll_allowances](../l10n_ro_payroll_allowances/index.md)
- [l10n_ro_reges](../l10n_ro_reges/index.md)

#### 4. Componente Cheie

**Modele**

- `hr.salary.rule.category` (extins): aplică la creare maparea componentei de transparență pe categoriile RO (`TICHETE`, `BENANG`, `BENANG_NI`, `CMFN`), doar unde câmpul e gol.
- `hr.salary.rule` (extins): aplică maparea pe regulile cu cod specific (`CO_IND`, `REIMBURSEMENT`, `DIURNA_*`, `AVANTAJ_ANG*`, `CADOU_IMP*`).
- `l10n.ro.pay.transparency.cor.wizard` și `l10n.ro.pay.transparency.cor.wizard.line` (wizard): propun și creează categorii de lucrători din codurile COR ale contractelor.

**Vizualizări**

- `view_l10n_ro_pay_transparency_cor_wizard_form`: formularul asistentului *Categorii din COR*.
- `view_pay_transparency_category_list`: extinde lista categoriilor de lucrători cu butonul *Categorii din COR*.
- `menu_l10n_ro_pay_transparency_cor_wizard`: intrarea de meniu a asistentului.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: la instalare mapează regulile și categoriile salariale RO existente. Nu există cron-uri sau acțiuni server.

#### 5. Conexiuni

- [deltatech_hr_pay_transparency](../deltatech_hr_pay_transparency/index.md): modulul de bază (raport, cereri, categorii de lucrători), prin dependența `deltatech_hr_pay_transparency_payroll`.
- [l10n_ro_expense_allowance_payroll](../l10n_ro_expense_allowance_payroll/index.md): regulile de diurnă create de el primesc maparea (exclusă din remunerație).
