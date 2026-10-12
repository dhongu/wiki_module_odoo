# Transparență salarială (Directiva UE 2023/970)

- **Nume Tehnic:** `deltatech_hr_pay_transparency`
- **Versiune:** `19.0.0.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_hr_pay_transparency
- **Cale Locală:** `odoo-addons/bitshop/deltatech_hr_pay_transparency`
- **Ultima Ingestie:** `2026-10-12`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul ajută angajatorii din Uniunea Europeană să respecte Directiva (UE) 2023/970 privind transparența salarială. Statele membre trebuiau să o transpună până la 7 iunie 2026; primele rapoarte, pentru salariile din 2026, sunt datorate la 7 iunie 2027 de angajatorii cu cel puțin 150 de lucrători (cei cu 100–149 de lucrători raportează din 2031). Modulul pornește de la angajați și contractele lor, funcționează pe Odoo Community și produce raportul privind diferența de remunerare între femei și bărbați, răspunsurile la cererile de informații ale lucrătorilor și evaluarea comună a remunerării.

#### 2. Funcționalități Cheie

- **Categorii de lucrători** cu valoare egală, notate pe cele patru criterii ale directivei (competențe, efort, responsabilitate, condiții de muncă, art. 4). Categoria se setează pe funcție și se păstrează pe fiecare versiune de contract, astfel încât raportul unui an trecut folosește categoria valabilă atunci.
- **Criterii de remunerare** publicate pe categorie: cum se stabilește și cum progresează salariul (art. 6), plus intervalul salarial al categoriei (art. 5). Ponderile celor patru criterii se pot ajusta sau se pot adăuga criterii proprii.
- **Raport privind diferența de remunerare** (art. 9), ca instantaneu aprobat: diferențe medii și mediane, aceleași pe componentele complementare/variabile, proporția femeilor și bărbaților care le primesc, cuartile salariale și diferențe pe categorii (bază și variabil). Toate cifrele sunt calculate pe salariul anual și pe cel orar; indicatorii (a)–(e) și (g) apar în filele Indicatori, Cuartile, Categorii și Lucrători.
- **Aprobarea de către conducere** (art. 9(6)), data transmiterii și o perioadă de remediere de șase luni pentru categoriile cu diferență de 5% sau mai mare (rânduri roșii; se pot marca *Justificat* cu motiv sau *Remediat*).
- **Evaluare comună a remunerării** (art. 10), deschisă automat la expirarea perioadei de remediere dacă diferența rămâne nejustificată (doar pentru rapoartele obligatorii), cu secțiunile (a)–(g) ale directivei.
- **Cereri de informații** (art. 7): înregistrate de HR sau create de lucrător din aplicația Angajați (*Cererile mele*), cu termen legal de răspuns, activitate pentru responsabil și răspuns scris (e-mail și PDF) cu nivelul propriu de remunerare și nivelurile medii pe sexe ale categoriei. Canale: lucrătorul, e-mail, reprezentanți, organismul pentru egalitate; pentru ultimele două răspunsul conține cifrele complete și nu se trimite lucrătorului.
- **Notificare anuală** către toți lucrătorii privind dreptul de a cere informații (art. 7(3)).
- **Export pentru organismul de monitorizare** (Excel, cifre nemascate) și PDF cu diferențele pe categorii pentru lucrători.
- **Confidențialitate**: grupuri de securitate dedicate (Responsabil / Administrator), cifre individuale vizibile doar administratorilor și medii ascunse în documentele pentru lucrători când un grup are mai puțini lucrători de un sex decât minimul configurabil.
- **Profile de țară**: termen de răspuns (luni, zile calendaristice sau lucrătoare), praguri și date de raportare, prag de evaluare comună, perioadă de remediere, dimensiune minimă de grup și organism de monitorizare; implicit profil UE și profil România.
- **Linii de remunerare** importate dintr-un sistem de salarizare extern (bază, variabil, în natură, ore plătite), pentru firmele care nu rulează salarizarea în Odoo; fără linii, se folosește salariul din contract.
- **Configurare**: Setări Angajați, secțiunea *Pay Transparency* (profil de țară, responsabil, notificare anuală); sexul legal al fiecărui angajat trebuie completat, altfel raportul nu se calculează (decât cu *Compute Without Sex*).

#### 3. Dependențe

- `hr`
- `mail`
- Dependență Python externă: `xlsxwriter`

#### 4. Componente Cheie

**Modele**

- `deltatech.pay.transparency.report`: raportul anual privind diferența de remunerare (cu `.indicator`, `.quartile`, `.category`, `.employee` pentru liniile detaliate).
- `deltatech.pay.transparency.category`: categoria de lucrători, cu intervalul salarial și criteriile de remunerare (`.score` pentru notele pe criterii).
- `deltatech.pay.transparency.criterion`: criteriile de evaluare cu pondere.
- `deltatech.pay.transparency.request`: cererea de informații a unui lucrător, cu termen și răspuns.
- `deltatech.pay.transparency.assessment`: evaluarea comună a remunerării (art. 10).
- `deltatech.pay.transparency.profile`: profilul de țară (termene, praguri, organism).
- `deltatech.pay.transparency.pay.line`: linii de remunerare importate din salarizare externă.
- Extensii: `hr.job`, `hr.version` (categoria de lucrători), `hr.employee`, `res.company`, `res.config.settings`.

**Vizualizări**

- Vizualizări de formular și listă pentru profil, categorie, linii de remunerare, raport, evaluare comună și cerere (`views/*.xml`), plus extinderi pe funcție/angajat și în setări.
- Meniul *Angajați → Pay Transparency* (rapoarte, evaluări comune, cereri, cererile mele, linii de remunerare) și configurarea în *Angajați → Configurare*.
- Rapoarte: PDF cu diferențele pe categorii pentru lucrători, PDF de răspuns la cerere, export Excel.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_joint_assessment`: deschide evaluările comune la expirarea perioadei de remediere.
- `ir_cron_annual_notice`: trimite notificarea anuală către lucrători.
- Șabloane de e-mail pentru răspunsul la cerere și notificarea anuală; secvență pentru cereri.

#### 5. Conexiuni

- `deltatech_hr_pay_transparency_payroll` (suita `bitshop_ent`): puntea cu Payroll, instalată automat; cifrele provin din fluturașii validați.
