# Pay Transparency (EU Directive 2023/970) (localizat la `deltatech_hr_pay_transparency/index.md`)

- **Nume Tehnic:** `deltatech_hr_pay_transparency`
- **Versiune:** `20.0.0.1.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_hr_pay_transparency
- **Cale Locală:** `odoo-addons/bitshop/deltatech_hr_pay_transparency`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul sprijină conformarea cu Directiva (UE) 2023/970 privind transparența salarială, pe care statele membre trebuiau s-o transpună până la 7 iunie 2026. Primele rapoarte privind diferența de remunerare între femei și bărbați sunt scadente la 7 iunie 2027, pentru salariile din 2026, la angajatorii cu cel puțin 150 de lucrători (cei cu 100-149 raportează din 2031). Funcționează pe Odoo Community, pornind de la angajați și contractele lor; cu `deltatech_hr_pay_transparency_payroll` (instalat automat cu Payroll) cifrele provin din fluturașii validați.

#### 2. Funcționalități Cheie

- **Categorii de lucrători** de valoare egală, punctate pe cele patru criterii ale directivei (competențe, efort, responsabilitate, condiții de muncă; art. 4). Categoria se setează pe funcție și se păstrează pe fiecare versiune de contract, deci raportul unui an trecut folosește categoria de atunci.
- **Criterii salariale** publicate per categorie (art. 6) și intervalul salarial al categoriei (art. 5).
- **Raportul privind diferența salarială** (art. 9), ca instantaneu aprobat: diferențe medii și mediane, aceleași pe componentele complementare/variabile, ponderea femeilor și bărbaților care le primesc, cuartile salariale și diferențele pe categorii, separat pentru salariul de bază și componentele variabile, calculate anual și orar.
- **Aprobare de conducere** (art. 9(6)), data transmiterii și o perioadă de remediere de șase luni pentru categoriile cu diferență de 5% sau mai mare; fiecare categorie roșie se marchează *Justified* (cu motiv) sau *Remedied*.
- **Evaluare comună a remunerării** (art. 10), deschisă automat când perioada de remediere s-a încheiat și diferența rămâne nejustificată, cu secțiunile (a)-(g) ale directivei.
- **Cereri de informații** (art. 7): înregistrate de HR sau făcute de lucrător din aplicația Employees (*My Requests*), cu termen legal, activitate pentru responsabil și răspuns scris (e-mail și PDF) cu nivelul salarial propriu și mediile pe sexe ale categoriei; cererile primite prin reprezentanți sau organismul de egalitate primesc cifrele complete.
- **Notificare anuală** către toți lucrătorii privind dreptul de a cere informații (art. 7(3)).
- **Export pentru autoritate** (Excel, fără mascare) și PDF cu diferențele pe categorii pentru lucrători.
- **Confidențialitate**: grupuri de securitate dedicate (*Officer* și *Administrator*), cifre individuale vizibile doar administratorilor, medii ascunse pe documentele lucrătorilor când un grup are mai puțini lucrători de un sex decât minimul configurat.
- **Profiluri de țară**: termen de răspuns, praguri și date de raportare, prag de evaluare, dimensiune minimă de grup și organism de monitorizare, pentru UE (implicit) și România.
- **Linii de salarii** importate dintr-un payroll extern, pentru firmele care nu rulează salarizarea în Odoo; fără ele, calculul folosește salariul din contract.
- Fluxul în 10 pași, cu capturi, este în [fișa consultantului](FISA_CONSULTANT.md). Raportul refuză calculul dacă lipsește sexul legal al angajaților (opțiunea *Compute Without Sex* îi exclude); tipurile de angajați fără relație de muncă se marchează *Outside Pay Transparency*.

#### 3. Dependențe

- `hr`
- `mail`
- Dependență externă Python: `xlsxwriter` (exportul Excel)

#### 4. Componente Cheie

**Modele**

- `deltatech.pay.transparency.profile`: profilul de țară (termene, praguri, organism de monitorizare).
- `deltatech.pay.transparency.criterion`, `.category`, `.category.score`: criteriile, categoriile de lucrători și punctajele lor.
- `deltatech.pay.transparency.pay.line`: linii de salariu importate dintr-un payroll extern.
- `deltatech.pay.transparency.report` cu `.report.indicator`, `.report.quartile`, `.report.category`, `.report.employee`: raportul de diferențe și detaliile lui.
- `deltatech.pay.transparency.assessment`: evaluarea comună a remunerării.
- `deltatech.pay.transparency.request`: cererile de informații.
- `hr.employee`, `hr.employee.type`, `hr.job`, `hr.version`, `res.company`, `res.config.settings`: extinse cu categoria, excluderea și setările.

**Vizualizări**

- `views/pay_transparency_report_views.xml`, `..._assessment_views.xml`, `..._request_views.xml`: raportul, evaluarea comună și cererile.
- `views/pay_transparency_category_views.xml`, `..._profile_views.xml`, `..._pay_line_views.xml`: configurarea.
- `views/hr_views.xml`, `views/res_config_settings_views.xml`, `views/menus.xml`: integrarea în *Employees > Pay Transparency*.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_joint_assessment`: deschide automat evaluarea comună la expirarea perioadei de remediere, pentru rapoartele obligatorii.
- `ir_cron_annual_notice`: trimite notificarea anuală către lucrători (dacă este activată în setări).

#### 5. Conexiuni

- `deltatech_hr_pay_transparency_payroll`: extensia care citește cifrele din fluturașii validați (instalată automat cu Payroll; fără pagină wiki).
