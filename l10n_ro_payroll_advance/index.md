# Romania - Avans chenzinal pe salarii (localizat la `l10n_ro_payroll_advance/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_advance`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_payroll_advance
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_advance`
- **Ultima Ingestie:** `2026-10-09`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Firmele care plătesc salariul în două tranșe dau salariaților un avans la jumătatea lunii. Modulul ține acest avans într-un lot, cu plata contabilizată pe contul 425, îl scade automat din restul de plată al fluturașului lunii și tipărește statul de avansuri cu semnături. Astfel, nu mai există sume trecute de mână în fluturaș, iar contul 425 se lămurește pe fiecare salariat.

#### 2. Funcționalități Cheie

- **Lot de avans** (*Stat de plată → Fluturași de salariu → Avansuri de salarii*): companie, luna, data plății, jurnalul de plată (bancă sau casă) și o linie pe salariat. Liniile se generează pentru salariații cu contract activ în lună; un salariat apare o singură dată într-un lot. Suma implicită este un procent din salariul de bază (procentul se setează pe companie, implicit 40%) sau o sumă fixă, și se poate modifica pe fiecare linie; *Recalculează sumele* reia sumele din tipul ales. Când avansul depășește netul estimat (fluturașul lunii, dacă e calculat, altfel o estimare din salariul de bază), linia este marcată și lotul afișează o avertizare. Lista liniilor are coloana *Rest pe 425*.
- **Plata prin bancă**: la *Confirmă plata* se creează câte o plată de ieșire (`account.payment`) pe salariat, cu partener contactul de muncă, cu `425 Avansuri acordate personalului` drept cont de destinație, iar creditul rămâne pe contul de plăți în curs până la reconcilierea extrasului bancar. Linia de extras importat se reconciliază cu plata, fără dublă contabilizare pe 5121; nu contabilizați manual linia de extras pe 425 și 5121.
- **Plata în numerar**: pe un jurnal de numerar se postează direct nota `Dr 425 = Cr 5311` (contul implicit al jurnalului), cu câte o pereche de linii pe salariat, pe contactul de muncă.
- **Configurarea cerută pentru banca**: metoda de plată de ieșire a jurnalului trebuie să aibă cont de plăți în curs (*Contabilitate → Configurare → Jurnale → Plăți Efectuate*; contul reconciliabil, de tip *Active circulante*, de exemplu 512103). Dacă lipsește, modulul refuză plata cu o eroare explicită, înainte de orice postare: lotul rămâne în ciornă și nu se postează nicio plată (cu aplicația Contabilitate, o plată fără acest cont s-ar posta fără notă contabilă). Planul RO nu îl setează automat. Butonul inteligent *Plăți / Notă* deschide plățile (bancă) sau nota (numerar); totalul pe 425 este totalul lotului.
- **Lichidare pe fluturaș**: regula salarială *Lichidare avans* (cod `AVANS`, secvența 205, după net) scade avansul din restul de plată. La validarea fluturașului se contabilizează `Dr 421 Personal - salarii datorate = Cr 425`. La postarea notei fluturașului, linia `Cr 425` se reconciliază automat cu liniile `Dr 425` ale plăților avansului (parțial, dacă sumele diferă), astfel încât în nota fluturașului rămân deschise doar 421 și contul de plată. La anularea fluturașului reconcilierea se desface, iar avansul revine la *Nelichidat*. Un al doilea fluturaș al lunii (corecție) nu scade din nou avansul deja lichidat; mai multe loturi pe aceeași lună se lichidează împreună.
- **Fără efect fiscal asupra fluturașului**: regula are categorie proprie, în afara brutului, CAS, CASS, impozitului și netului; avansul nu modifică baza de calcul a contribuțiilor și nu apare în D112.
- **Avans mai mare decât netul**: se scade doar cât acoperă netul, restul de plată nu devine negativ, iar pe fluturaș și pe lot apare o avertizare. Diferența rămâne pe 425 (linia lotului este *Parțial lichidat*) și se reține manual pe statul lunii următoare (reținerile cumulate nu pot depăși jumătate din net, Codul muncii art. 169 alin. 4).
- **Stat de avansuri**: raport PDF A4 pe lat, cu coloană de semnătură (*Tipărește statul*), și export XLSX (*Exportă XLSX*).
- **Anulare**: butonul *Anulează* al unui lot *Plătit* șterge, anulează sau stornează plățile (bancă) sau nota directă (numerar), după blocarea perioadei și audit trail (`_unlink_or_reverse`). Anularea este blocată dacă o plată este reconciliată cu un extras bancar (se desface mai întâi reconcilierea), dacă lotul e lichidat pe un fluturaș validat (se anulează mai întâi fluturașul) sau dacă o ciornă de fluturaș deduce deja avansul.
- **Protecții pe fluturaș**: acțiunea *Setează ca ciornă* este blocată pe un fluturaș validat care a lichidat un avans (se folosește *Anulează*, apoi *Setează ca ciornă* pe formular); fluturașul afișează o avertizare când este activă opțiunea *Batch Account Move Lines* (*Setări → Stat de plată*), care scoate salariatul de pe liniile notei și împiedică reconcilierea automată pe 425 (opțiunea trebuie dezactivată).
- **Configurare**: procentul implicit în *Setări → Stat de plată → Avans de salarii*; conturile 425 și 421 se completează automat pe regulă la planul de conturi RO (pe alte planuri se completează manual pe regulă); jurnalul de plată are nevoie de cont implicit (5121 sau 5311). Gestionarea avansurilor cere grupul *Salarizare / Administrator*. Modulul nu impune data sau mărimea avansului (ține de contractul de muncă / regulamentul intern, Codul muncii art. 166).
- **Limite**: butonul nativ *Plătește* al fluturașului poate da eroarea „Contul de credit din regula salariului NET nu este reconciliabil” în configurarea RO (provine din `hr_payroll_account`, nu din acest modul; verificați în baza dumneavoastră); nu există fișier bancar pentru avans (fișierul de plată a salariilor lucrează pe fluturași și conține netul întreg); recuperarea automată a diferenței din salariul lunii următoare nu este implementată; regula *Lichidare avans* este legată doar de structura salarială RO, deci pe alte structuri avansul rămâne *Nelichidat*; statul de plată semnat din `l10n_ro_payroll_statements` rămâne fără coloană de avans.
- **Fișa de consultant** are 10 capturi de ecran (setarea procentului, lotul în ciornă și plătit, nota plății, statul de avansuri, fluturașul cu lichidarea, notele fluturașului, avansul peste net, lotul lichidat).

#### 3. Dependențe

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)
- [l10n_ro_hr_payroll_account_enhancement](../l10n_ro_hr_payroll_account_enhancement/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.payroll.advance`: lotul de avans (companie, lună, data plății, jurnal, stare, nota plății pentru numerar, plățile pentru bancă), cu `mail.thread`; conține confirmarea (`_create_payments` pe bancă, notă directă pe numerar, cu verificarea contului de plăți în curs), anularea și statul PDF/XLSX.
- `l10n.ro.payroll.advance.line`: linia pe salariat, cu suma, plata (`account.payment`) a salariatului, starea lichidării (*Nelichidat*, *Parțial lichidat*, *Lichidat*), restul rămas pe 425 și estimarea netului.
- `account.payment` (folosit, nu extins): plata de ieșire pe salariat, cu 425 drept cont de destinație.
- `hr.payslip` (extins): calculul avansului de lichidat (plafonat la net, fără dublare pe fluturași de corecție), reconcilierea `Cr 425` cu liniile `Dr 425` ale plăților, desfacerea ei la `action_payslip_cancel`, blocarea `action_payslip_draft` pe fluturaș cu avans lichidat și avertizările (avans peste net, *Batch Account Move Lines*).
- `account.move` (extins): `_post` declanșează reconcilierea pe 425 a fluturașilor ale căror note tocmai s-au postat.
- `res.company` / `res.config.settings` (extinse): câmpul `l10n_ro_advance_percent` (procentul implicit al avansului, 40%) și expunerea lui în setări.
- `account.chart.template` (extins): completarea conturilor 425 și 421 pe regula de lichidare la configurarea contabilă a salarizării pe planul RO (regulile configurate manual nu se modifică).

**Vizualizări**

- `view_l10n_ro_payroll_advance_form`, `view_l10n_ro_payroll_advance_list`, `view_l10n_ro_payroll_advance_search`: formularul, lista și căutarea loturilor.
- `res_config_settings_view_form_payroll_advance`: setarea procentului implicit.
- `report_payroll_advance`: șablonul statului de avansuri (PDF A4 pe lat).

**Acțiuni Automate / Acțiuni Server**

- `action_l10n_ro_payroll_advance`: acțiunea de meniu pentru loturile de avans.
- `action_report_payroll_advance`: raportul PDF al statului de avansuri.
- `l10n_ro_employee_salary_advance`: regula salarială *Lichidare avans* (categoria `l10n_ro_advance_category`).
- `seq_l10n_ro_payroll_advance`: secvența loturilor.
- Nu există acțiuni cron.

#### 5. Conexiuni

- [l10n_ro_payroll_statements](../l10n_ro_payroll_statements/index.md): statul de plată semnat conține doar NET, fără coloană de avans; statul de avansuri este un raport separat, al acestui modul.
- [l10n_ro_payroll_bank_export](../l10n_ro_payroll_bank_export/index.md): fișierul bancar al fluturașului conține netul întreg, fără avans; avansurile plătite prin bancă se plătesc cu plățile din modul, nu din fișierul bancar al fluturașului.
