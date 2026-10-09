# Romania - Avans chenzinal pe salarii (localizat la `l10n_ro_payroll_advance/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_advance`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_payroll_advance
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_advance`
- **Ultima Ingestie:** `2026-10-09`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Firmele care plătesc salariul în două tranșe dau salariaților un avans la jumătatea lunii. Modulul ține acest avans într-un lot, cu plata contabilizată pe contul 425, îl scade automat din restul de plată al fluturașului lunii și tipărește statul de avansuri cu semnături. Astfel, nu mai există sume trecute de mână în fluturaș, iar contul 425 se lămurește pe fiecare salariat.

#### 2. Funcționalități Cheie

- **Lot de avans** (*Salarizare → Fluturași → Avansuri de salarii*): companie, luna, data plății, jurnalul de plată (bancă sau casă) și o linie pe salariat. Liniile se generează pentru salariații cu contract activ în lună; un salariat apare o singură dată într-un lot. Suma implicită este un procent din salariul de bază (procentul se setează pe companie, implicit 40%) sau o sumă fixă, și se poate modifica pe fiecare linie. Când avansul depășește netul estimat, linia este marcată și lotul afișează o avertizare.
- **Plata avansului**: la confirmare se postează `Dr 425 Avansuri acordate personalului = Cr 5121 / 5311` (contul implicit al jurnalului), cu câte o pereche de linii pe salariat, pe contactul de muncă al acestuia.
- **Lichidare pe fluturaș**: regula salarială *Lichidare avans* (cod `AVANS`, secvența 205, după net) scade avansul din restul de plată. La validarea fluturașului se contabilizează `Dr 421 Personal - salarii datorate = Cr 425`. La postarea notei fluturașului, linia `Cr 425` se reconciliază automat cu plata avansului (parțial, dacă sumele diferă), astfel încât butonul de plată al fluturașului acoperă doar restul (net - avans). La invalidarea sau anularea fluturașului reconcilierea se desface, iar avansul revine la *Nelichidat*.
- **Fără efect fiscal asupra fluturașului**: regula are categorie proprie, în afara brutului, CAS, CASS, impozitului și netului; avansul nu modifică baza de calcul a contribuțiilor și nu apare în D112.
- **Avans mai mare decât netul**: se scade doar cât acoperă netul, restul de plată nu devine negativ, iar pe fluturaș și pe lot apare o avertizare. Diferența rămâne pe 425 (linia lotului este *Parțial lichidat*) și se reține manual pe statul lunii următoare.
- **Stat de avansuri**: raport PDF A4 pe lat, cu coloană de semnătură, și export XLSX.
- **Anulare**: lotul *Plătit* se anulează cu stornarea notei plății; un lot lichidat pe un fluturaș validat nu se anulează înainte de anularea fluturașului.
- **Configurare**: procentul implicit în *Setări → Salarizare → Avans de salarii*; conturile 425 și 421 se completează automat pe regulă la planul de conturi RO (pe alte planuri se completează manual); jurnalul de plată are nevoie de cont implicit (5121 sau 5311). Gestionarea avansurilor cere grupul *Salarizare / Administrator*.
- **Limite**: nu există fișier bancar pentru avans (fișierul de plată a salariilor lucrează pe fluturași și conține netul întreg); recuperarea automată a diferenței din salariul lunii următoare nu este implementată; regula *Lichidare avans* este legată doar de structura salarială RO, deci pe alte structuri avansul rămâne *Nelichidat*; statul de plată semnat din `l10n_ro_payroll_statements` rămâne fără coloană de avans.

#### 3. Dependențe

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)
- [l10n_ro_hr_payroll_account_enhancement](../l10n_ro_hr_payroll_account_enhancement/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.payroll.advance`: lotul de avans (companie, lună, data plății, jurnal, stare, nota plății), cu `mail.thread`.
- `l10n.ro.payroll.advance.line`: linia pe salariat, cu suma, starea lichidării (*Nelichidat*, *Parțial lichidat*, *Lichidat*) și legătura cu fluturașul.
- `hr.payslip` (extins): calculul liniei de lichidare, avertizarea peste net și legătura cu loturile.
- `account.move` (extins): reconcilierea liniei `Cr 425` cu plata avansului la postarea notei fluturașului și desfacerea ei la anulare.
- `res.company` / `res.config.settings` (extinse): procentul implicit al avansului.
- `account.chart.template` (extins): completarea conturilor 425 și 421 pe regula de lichidare la planul RO.

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
- [l10n_ro_payroll_bank_export](../l10n_ro_payroll_bank_export/index.md): fișierul bancar al fluturașului conține netul întreg, fără avans; pentru avansurile plătite prin bancă, plata se face din extras sau manual.
