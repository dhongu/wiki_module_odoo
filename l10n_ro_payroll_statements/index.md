# Romania - Stat de plată și recapitulații (`l10n_ro_payroll_statements`)

- **Nume Tehnic:** `l10n_ro_payroll_statements`
- **Versiune:** `20.0.1.1.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_payroll_statements
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_statements`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Tipăriri centralizate pe lotul de fluturași sau pe lună, cu filtre și export XLSX, fără să adunați de mână sumele din fluturași: statul de plată, recapitulația pe reguli și centralizatorul de sporuri și rețineri.

#### 2. Funcționalități Cheie

- Acces din *Stat de plată → Raportare → Stat de plată (RO)*, cu alegerea tipului de raport.
- **Stat de plată**: o linie pe salariat, cu brut, CAS, CASS, CM FNUASS, deducere personală, impozit, alte rețineri, net, avans și rest de plată, totaluri pe coloană și coloană de semnătură.
- **Recapitulație pe reguli**: totalul fiecărei reguli salariale, cu numărul de salariați.
- **Centralizator de sporuri și rețineri**: matrice salariați × reguli din categoriile ALW și DED, cu totaluri.
- Filtre pe lotul de fluturași sau lună, departamente și puncte de lucru; implicit fluturașii validați și plătiți, cu opțiunea *Include fluturașii în ciornă*.
- Ieșire PDF (A4 pe lat) sau XLSX.
- Cu `l10n_ro_payroll_advance`, statul are coloanele *Avans* și *Rest de plată*.
- Limită: nu se filtrează pe analitic. Pașii detaliați sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.payroll.statement` (wizard): alegerea raportului și a filtrelor, generarea PDF și XLSX.

**Vizualizări**

- `view_l10n_ro_payroll_statement_form`: fereastra raportului, cu tipul și filtrele.
- `report_payroll_statement`: șablonul QWeb al rapoartelor PDF.

**Acțiuni Automate / Acțiuni Server**

- `action_l10n_ro_payroll_statement`: deschide wizardul din meniul de raportare.
- `action_report_payroll_statement`: raportul PDF, pe format de hârtie dedicat (`paperformat_payroll_statement`).

#### 5. Conexiuni

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md): sursa fluturașilor.
- [l10n_ro_payroll_pack](../l10n_ro_payroll_pack/index.md): pachetul care îl include.
- `l10n_ro_payroll_advance`: adaugă coloanele de avans.
