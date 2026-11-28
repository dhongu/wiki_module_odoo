# Romania - Avans chenzinal pe salarii (localizat la `l10n_ro_payroll_advance/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_advance`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_payroll_advance
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_advance`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Avansul de salarii (chenzinal) se gestionează pe lot, cu nota contabilă a plății, lichidarea pe fluturașul lunii și statul de avansuri semnat de salariați. Nu mai sunt sume trecute de mână în fluturaș și nu rămâne contul 425 nelămurit.

#### 2. Funcționalități Cheie

- **Lotul de avans** (*Stat de plată → Fluturași de salariu → Avansuri de salarii*): companie, lună, data plății, jurnal de plată (bancă sau casă) și o linie pe salariat. Liniile se generează pentru salariații cu contract activ în lună; suma implicită este un procent din salariul de bază (procentul se setează pe companie, implicit 40%) sau o sumă fixă, modificabilă pe linie. Un salariat apare o singură dată pe lot.
- **Plata avansului**: la confirmare, pe jurnal de bancă se creează câte o plată pe salariat cu `Dr 425 = Cr plăți în curs` (reconciliabilă cu extrasul); pe jurnal de numerar se postează direct `Dr 425 = Cr 5311`. Pe metoda de plată de ieșire a jurnalului de bancă trebuie setat contul de plăți în curs.
- **Lichidarea pe fluturaș**: regula salarială *Lichidare avans* (secvența 205, după net) scade avansul din restul de plată și contabilizează `Dr 421 = Cr 425`; brutul, CAS, CASS, impozitul și netul nu se schimbă. La postarea notei fluturașului, linia 425 se reconciliază cu plata avansului.
- **Avans peste net**: se lichidează doar cât acoperă netul, restul de plată nu devine negativ, apare o avertizare pe fluturaș și pe lot, iar diferența rămâne pe 425, de reținut luna următoare.
- **Statul de avansuri**: PDF A4 pe lat, cu coloană de semnătură, și export XLSX.
- Gestionarea necesită grupul *Administrator salarizare*; conturile 425 și 421 se pun automat pe regulă pentru planul de conturi RO.
- Fluxul pas-cu-pas, conturile și verificările sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)
- `l10n_ro_hr_payroll_account_enhancement`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.payroll.advance`: lotul de avans (cu `mail.thread`).
- `l10n.ro.payroll.advance.line`: linia de avans pe salariat.
- `hr.payslip`, `res.company`, `res.config.settings`, `account.move`, `account.chart.template`: extinse pentru lichidare, procentul implicit și conturi.

**Vizualizări**

- `view_l10n_ro_payroll_advance_form` / `_list` / `_search`: lotul de avans.
- `res_config_settings_view_form_payroll_advance`: procentul implicit în Setări.
- `action_report_payroll_advance`: statul de avansuri (PDF).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate; există secvența lotului și regula salarială *Lichidare avans* (date).

#### 5. Conexiuni

- `l10n_ro_payroll_statements`: statul de plată arată avansul lichidat și restul de plată.
- [l10n_ro_payroll_bank_export](../l10n_ro_payroll_bank_export/index.md): fișierul bancar pe fluturași (netul întreg, fără avans în această versiune).
