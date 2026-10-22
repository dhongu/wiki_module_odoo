# Romania - Pachet salarizare (localizat la `l10n_ro_payroll_pack/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_pack`
- **Versiune:** `19.0.1.2.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_payroll_pack
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_pack`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Salarizarea unei firme din România, completă și la zi cu legislația 2026, direct în Odoo: fluturașul calculat corect, nota contabilă, statul de plată semnat și declarația D112, toate din aceiași fluturași validați. Pachetul instalează cele cinci module de salarizare Terrabit dintr-o singură mișcare și aduce doar o mică punte de cod pentru istoricul lunilor dinainte de Odoo. Prețul simbolic (1 EUR) este completat de prețul modulelor incluse; nu există cost pe salariat, fluturaș sau declarație.

#### 2. Funcționalități Cheie

- **Salarii calculate ca la carte:** CAS, CASS, impozit și CAM pe bazele legale, rotunjite la leu; deducere personală pe grila oficială (tranșe de 50 lei), persoane în întreținere, deducere pentru tineri și pentru copii în învățământ.
- **Excepții din practică:** suma neimpozabilă la salariul minim cu pragul ei de venit, tichete de masă, vouchere de vacanță, tichete cadou, pensii și asigurări suportate de angajator (plafon 400 EUR), cotizație sindicală ca procent, prime cerute în net.
- **Concedii calculate:** concediu medical din certificat (partea angajatorului și FNUASS, continuări, decontare), concediu de odihnă pe media ultimelor 3 luni, concediu fără plată.
- **Notă contabilă la validare:** conturi românești pe fiecare regulă salarială, cu salariatul ca partener pe 421, gata de reconciliat cu plata.
- **Stat de plată:** statul semnat, recapitulația pe reguli și centralizatorul de sporuri și rețineri, în PDF sau XLSX, pe lună, lot, departament sau punct de lucru.
- **D112 din fluturași:** linii nominale preluate din fluturașii validați (concedii medicale, tichete, beneficii), bază minimă CAS/CASS la normă parțială cu excepțiile ei, CAS suplimentar pentru condiții deosebite/speciale, validări blocante (CNP greșit/duplicat, date lipsă), previzualizarea obligațiilor, reconcilierea cu conturile 4315/4316/436/444, declarația rectificativă, ordine de plată către trezorerie și XML validat cu schema ANAF. Depunerea se face prin SPV sau cu semnătură electronică.
- **Fluturașul pe e-mail:** PDF-ul fluturașului (tichete pe număr × valoare) se trimite automat salariaților, momentul alegându-se în setările de salarizare.
- **Simulator brut ↔ net** pentru oferte, fără a crea fluturași; calcul invers net → brut pentru prime.
- **Multi-companie:** fiecare companie cu salariații, parametrii, conturile și declarațiile ei.
- **Legislație versionată pe dată:** salariul minim, suma neimpozabilă, plafoanele și valoarea tichetului sunt parametri cu dată de început (*Stat de plată → Configurare → Salariu → Regulă Parametri*, fila Istoric).
- **Luni dinainte de Odoo, din D112 importat:** pe primul fluturaș, mediile concediului medical și de odihnă și tichetele pe luna anterioară se iau din declarația D112 importată (venit = baza CAM plus indemnizația FNUASS; concediul de odihnă pe salariul de bază proratat cu zilele lucrate). D112 nu desparte concediul de odihnă de zilele lucrate și nici primele de salariu, deci propunerea se verifică pe primul fluturaș.
- **Configurare minimă:** companie cu țara fiscală România și planul de conturi românesc; pe angajat, grupul *Salarizare România* (funcție de bază, persoane în întreținere cu CNP, tichete, scutiri); pentru D112, pe companie CAEN, județul și persoana de contact ANAF.
- **Cerințe:** Odoo 19 Enterprise (se bazează pe `hr_payroll`), Odoo.sh sau on-premise; nu rulează pe Odoo Online.
- **Module opționale** (nu sunt incluse): sporuri și ore suplimentare, avans chenzinal, fișiere de plată bancare, adeverințe, REGES-Online, zilieri, drepturi de autor, pontaj, diurne.

#### 3. Dependențe

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)
- [l10n_ro_hr_payroll_account_enhancement](../l10n_ro_hr_payroll_account_enhancement/index.md)
- [l10n_ro_payroll_statements](../l10n_ro_payroll_statements/index.md)
- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md)
- [l10n_ro_anaf_d112_payroll](../l10n_ro_anaf_d112_payroll/index.md)

#### 4. Componente Cheie

**Modele**

Modulul are cod minim; restul vine din modulele dependente.

- `hr.employee` (extins, `models/hr_employee.py`): suprascrie `_l10n_ro_external_month_history`; dacă lunii nu i se găsește istoric din fluturași, îl construiește din linia angajatului din declarația D112 importată (`l10n.ro.d112.employee.line`): `cm_income`, `cm_days`, `co_amount`, `co_days`, `worked_days`.

Testele din `tests/` confruntă salarizarea cu declarații D112 de referință (helper `tests/d112_reference.py`, scenarii sintetice, istoric din D112 importat, baza minimă CAS/CASS la normă parțială, simulatorul).

**Vizualizări**

Nu are (nici date).

**Acțiuni Automate / Acțiuni Server**

Nu are.

#### 5. Conexiuni

- [l10n_ro_payroll_allowances](../l10n_ro_payroll_allowances/index.md): sporuri, ore suplimentare, muncă de noapte, sărbători.
- [l10n_ro_payroll_advance](../l10n_ro_payroll_advance/index.md): avans chenzinal cu lichidare pe fluturaș.
- [l10n_ro_payroll_bank_export](../l10n_ro_payroll_bank_export/index.md): fișiere de plată a salariilor pentru bănci.
- [l10n_ro_payroll_certificates](../l10n_ro_payroll_certificates/index.md): adeverințe salariale, de șomaj, creștere copil.
- [l10n_ro_payroll_day_labourers](../l10n_ro_payroll_day_labourers/index.md): registrul și statul de plată al zilierilor.
- [l10n_ro_payroll_copyright](../l10n_ro_payroll_copyright/index.md): contracte și state de plată pentru drepturi de autor.
- [l10n_ro_hr_pontaj](../l10n_ro_hr_pontaj/index.md) și [l10n_ro_hr_pontaj_payroll](../l10n_ro_hr_pontaj_payroll/index.md): foaia colectivă de prezență, cu zilele trecute în fluturaș.
- [l10n_ro_expense_allowance_payroll](../l10n_ro_expense_allowance_payroll/index.md): diurna în fluturaș.
- [l10n_ro_reges](../l10n_ro_reges/index.md): transmiterea salariaților și contractelor în REGES-Online.
- [l10n_ro_expense_allowance](../l10n_ro_expense_allowance/index.md): diurne și deplasări.
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): bază pentru declarațiile ANAF (adusă prin D112).
