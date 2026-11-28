# Romania - Pachet salarizare (`l10n_ro_payroll_pack`)

- **Nume Tehnic:** `l10n_ro_payroll_pack`
- **Versiune:** `20.0.1.2.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_payroll_pack
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_pack`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Salarizarea unei firme din România, completă și la zi cu legislația 2026: fluturașul calculat corect, nota contabilă, statul de plată și declarația D112, toate din aceiași fluturași validați. Pachetul instalează dintr-o singură mișcare modulele de salarizare Terrabit și nu are cod propriu. Necesită Odoo 20 Enterprise (`hr_payroll`).

#### 2. Funcționalități Cheie

- Calcul pe bazele legale: CAS, CASS, impozit, CAM, deducere personală, persoane în întreținere, deducerea pentru tineri.
- Excepții din practică: suma neimpozabilă la salariul minim, tichete de masă, vouchere de vacanță, cadou, plafonul de 400 EUR, cotizația sindicală, prime cerute în net.
- Concedii calculate: medical din certificat, de odihnă pe media ultimelor 3 luni, fără plată.
- Nota contabilă generată la validare, cu salariatul partener pe 421.
- Stat de plată, recapitulație și centralizator, în PDF sau XLSX.
- D112 din fluturașii validați, cu validări, reconciliere (4315 / 4316 / 436 / 444), rectificativă, ordine de plată și XML validat cu schema ANAF.
- Trimiterea fluturașului pe e-mail, simulator brut ↔ net, multi-companie, parametri legali versionați pe dată.
- Configurare: țara fiscală România cu planul de conturi românesc; verificarea parametrului *Romania Salary Parameters* (*Stat de plată → Configurare → Salariu → Regulă Parametri*); date pe angajat (grupul *Salarizare România*) și, pentru D112, CAEN, județ și persoana de contact ANAF pe companie.
- Module opționale: sporuri, avans, export bancar, adeverințe, REGES, zilieri, drepturi de autor, pontaj, diurne.

#### 3. Dependențe

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)
- `l10n_ro_hr_payroll_account_enhancement`
- [l10n_ro_payroll_statements](../l10n_ro_payroll_statements/index.md)
- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md)
- [l10n_ro_anaf_d112_payroll](../l10n_ro_anaf_d112_payroll/index.md)

#### 4. Componente Cheie

**Modele**

- `hr.employee` (extins, `models/hr_employee.py`): singurul cod propriu al pachetului; furnizează istoricul lunii din D112 importat (salarizare ținută anterior în alt program) pentru media concediilor și propunerea de tichete.

**Vizualizări**

- Fără vizualizări proprii.

**Acțiuni Automate / Acțiuni Server**

- Fără.

#### 5. Conexiuni

- [l10n_ro_payroll_garnishment](../l10n_ro_payroll_garnishment/index.md): popriri și pensie de întreținere cu plafon legal (opțional).
- [l10n_ro_payroll_tax_redirect](../l10n_ro_payroll_tax_redirect/index.md): redirecționarea a 3,5% din impozit (opțional).
- `l10n_ro_anaf_base`, `l10n_ro_payroll_advance`, `l10n_ro_payroll_allowances`, `l10n_ro_payroll_bank_export`, `l10n_ro_reges`: module complementare.
