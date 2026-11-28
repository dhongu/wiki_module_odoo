# Romania - Impozit pe salarii și deducere personală

- **Nume Tehnic:** `l10n_ro_hr_payroll_enhancement`
- **Versiune:** `20.0.2.20.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_hr_payroll_enhancement
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_hr_payroll_enhancement`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Completează statul de plată românesc din Odoo Enterprise (`l10n_ro_hr_payroll`) cu regulile fiscale care lipsesc și corectează calculul impozitului pe salarii. Regula nativă aplica 10% la brut; modulul aplică impozitul pe baza redusă (brut + tichete − suma neimpozabilă − CAS − CASS − deduceri personale − rețineri deductibile), deci impozitul, netul și declarația D112 ies corecte.

#### 2. Funcționalități Cheie

- Deducerea personală de bază pe grila oficială (Cod fiscal art. 77), cu persoane în întreținere (CNP și perioadă), 100 lei/lună pentru copii sub 18 ani în învățământ, 15% din salariul minim pentru angajații sub 26 de ani; bifa Funcție de bază; scutirea de impozit pentru handicap și cercetare-dezvoltare (art. 60).
- Salariul minim și celelalte valori fiscale în parametri versionați pe dată, deci actualizarea cere o valoare nouă, nu modificare de cod.
- Suma neimpozabilă la salariul minim (OUG 89/2025), proratată cu timpul lucrat, scăzută din baza CAS, CASS, CAM și impozit.
- Rețineri deductibile (cotizație sindicală, pensie facultativă, asigurare de sănătate) cu plafon de 400 EUR pe an.
- Beneficii de la angajator: tichete de masă (valoare pe companie și pe contract), vouchere de vacanță, tichete cadou pe ocazie (300 lei pe persoană), beneficii art. 76 alin. 4^1 cu plafon propriu și plafon lunar comun de 33%; excedentul devine venit impozabil.
- Fluturaș: salariul de încadrare, suma neimpozabilă, salariul impozabil, cost angajator, rotunjire la leu, concediu fără plată, prime în net, avertizări (CNP, persoane în întreținere expirate) și simulator brut ↔ net.
- Concediu de odihnă pe media ultimelor 3 luni (Codul muncii art. 150) și compensarea la încetare.
- Concedii medicale (OUG 158/2005): certificat unic, zilele angajatorului și FNUASS, prima zi neplătită (OUG 91/2025), continuări cu recalcul retroactiv, fișa de calcul și decontarea FNUASS; codurile 10 și 11 nu sunt calculate.
- Limite: valorile sumei neimpozabile se confirmă cu contabilul; vărsământul Legea 448/2006 nu se calculează pe fluturaș; facilitățile fiscale abrogate din 2025 nu sunt incluse.
- Fluxul pas cu pas stă în fișa consultantului.

#### 3. Dependențe

- `l10n_ro_hr_payroll`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.hr.dependent`: persoane în întreținere ale angajatului.
- `l10n.ro.medical.certificate`, `l10n.ro.medical.code`, `l10n.ro.medical.fnuass.report`: certificatul medical, nomenclatorul `D_9` și decontarea FNUASS.
- `l10n.ro.payroll.simulator`, `l10n.ro.payroll.simulator.line`: simulatorul brut ↔ net.
- `hr.payslip`, `hr.payslip.input`, `hr.salary.rule`, `hr.salary.attachment`, `hr.version`, `hr.employee`, `res.company`, `res.config.settings`: extinse cu regulile, intrările și setările fiscale.

**Vizualizări**

- Vizualizările contractului (`hr.version`), ale regulilor salariale, ale reținerilor (`hr.salary.attachment`) și setările de salarizare.
- Simulatorul brut ↔ net, certificatul medical și raportul FNUASS, plus rapoartele PDF ale fluturașului, certificatului și simulatorului.

**Acțiuni Automate / Acțiuni Server**

- Fără cron sau acțiuni server; datele (reguli, parametri, categorii, intrări, coduri medicale, reguli CM și CO) se încarcă la instalare.

#### 5. Conexiuni

- [l10n_ro_hr_payroll_account_enhancement](../l10n_ro_hr_payroll_account_enhancement/index.md): nota contabilă la validarea fluturașului.
- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md) și [l10n_ro_anaf_d112_payroll](../l10n_ro_anaf_d112_payroll/index.md): declarația D112 pe baza fluturașelor.
- [l10n_ro_hr_pontaj_payroll](../l10n_ro_hr_pontaj_payroll/index.md): zilele din pontaj ajung pe fluturaș; valoarea tichetului de masă vine din salarizare.
- `l10n_ro_payroll_statements`, `l10n_ro_payroll_advance`, `l10n_ro_payroll_pack`: statul de plată, avansul de salarii și pachetul care le instalează împreună.
