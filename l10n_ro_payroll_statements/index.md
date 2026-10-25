# Romania - Stat de plată și recapitulații (localizat la `l10n_ro_payroll_statements/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_statements`
- **Versiune:** `19.0.1.1.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_payroll_statements
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_statements`
- **Ultima Ingestie:** `2026-10-12`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Tipăriri centralizate pe lotul de fluturași sau pe lună, cu filtre și export XLSX, fără să adunați de mână sumele din fluturași. Se deschid din *Stat de plată → Raportare → Stat de plată (RO)*.

#### 2. Funcționalități Cheie

- **Stat de plată:** o linie pe salariat, cu brut, CAS, CASS, CM FNUASS, deducere personală, impozit, alte rețineri și net, totaluri pe coloană și coloană de semnătură; concediul medical intră în CAS, CASS și impozit prin rândurile lui de contribuții.
- **Avans (cu `l10n_ro_payroll_advance`):** statul de plată are, după *Net*, coloanele *Avans* (avansul lichidat pe fluturaș) și *Rest de plată* (net − avans), în PDF și XLSX; fără modulul de avans, avansul e 0 și restul de plată este netul. Statul de avansuri se tipărește din modulul de avans.
- **Recapitulație pe reguli:** totalul fiecărei reguli salariale (cod, denumire, categorie), cu numărul de salariați și suma pe toți fluturașii.
- **Centralizator de sporuri și rețineri:** matrice salariați × reguli din categoriile sporuri (ALW) și rețineri (DED), cu totaluri.
- **Filtre:** lotul de fluturași sau luna, departamentele și punctele de lucru; implicit se iau fluturașii validați și plătiți (bifa *Include fluturașii în ciornă* adaugă ciornele).
- **Ieșiri:** PDF (A4 pe lat) sau XLSX.
- **Limite:** nu se filtrează pe analitic (fluturașii nu au analitic); modulul nu generează note contabile și nu transmite date în D112.

#### 3. Dependențe

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.payroll.statement` (wizard): alege tipul de raport, filtrele și formatul (PDF / XLSX).

**Vizualizări**

- `views/l10n_ro_payroll_statement_views.xml`: fereastra wizardului și meniul.
- `report/report_payroll_statement.xml`: șabloanele PDF ale celor trei rapoarte.

**Acțiuni Automate / Acțiuni Server**

Nu are `ir.cron` sau acțiuni server.

#### 5. Conexiuni

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md): fluturașii și regulile din care se agregă.
- [l10n_ro_payroll_advance](../l10n_ro_payroll_advance/index.md): sursa coloanelor *Avans* și *Rest de plată* (regula `AVANS`); dependență opțională.
- [l10n_ro_payroll_bank_export](../l10n_ro_payroll_bank_export/index.md): plata efectivă a netului din stat.
