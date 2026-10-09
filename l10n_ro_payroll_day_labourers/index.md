# Romania - Zilieri (localizat la `l10n_ro_payroll_day_labourers/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_day_labourers`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_payroll_day_labourers
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_day_labourers`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul ține evidența și plata **zilierilor** conform Legii 52/2011 (activități cu caracter ocazional): registrul zilierilor, statul de plată cu calculul reținerilor, nota contabilă și preluarea automată în declarația D112. Remunerația zilierului este venit asimilat salariilor: beneficiarul reține CAS 25% din brut și impozit 10% pe brut minus CAS; nu se datorează CASS, CAM sau contribuția de șomaj.

#### 2. Funcționalități Cheie

- **Registrul zilierilor** (*Contabilitate → Contabilitate → Zilieri → Registrul zilierilor*): o poziție pe zilier și zi, cu orele lucrate, tariful orar brut (implicit salariul minim pe oră), domeniul de activitate (art. 13), locul activității și bifa *Transmis în registrul ITM* (filtru *Netransmis la ITM*). CNP-ul se completează direct din registru.
- **Verificări din lege**, la salvare:
  - tariful orar cel puțin egal cu salariul minim brut pe oră (24,496 lei; 25,949 lei din iulie 2026);
  - cel mult 12 ore pe zi; plata se face pentru minimum 8 ore;
  - cel mult 25 de zile calendaristice continuu la același beneficiar;
  - cel mult 90 de zile pe an la același beneficiar, respectiv 180 de zile în agricultură, silvicultură, pescuit, material săditor și creșterea animalelor;
  - un zilier o singură dată pe zi.
- **Statul de plată** (*Zilieri → State de plată*): perioadă din aceeași lună și dată de plată; butonul *Calculează din registru* preia zilele neplătite și calculează pe zilier zilele, brutul, CAS-ul, baza de impozitare, impozitul și restul de plată. Fluxul: Calculează, Confirmă (CNP valid obligatoriu), Tipărește (cu coloană de semnătură, ține loc de dovadă a plății), Contabilizează. Rotunjirea la leu se face o singură dată, pe luna întreagă, în D112.
- **Nota contabilă** la contabilizare (OMFP 1802/2014): `621 = 401` brut, `401 = 4315` CAS, `401 = 444` impozit. Restul de plată rămâne în 401, pe zilier, și se stinge la plata din casă sau bancă.
- **Configurare** (*Contabilitate → Configurare → Setări*, secțiunea Declarații ANAF): contul de cheltuieli (implicit `621`), jurnalul notelor contabile (implicit primul jurnal de operațiuni diverse); conturile de CAS și impozit sunt cele din setările D112.
- **D112**: butonul *Calculează* adaugă zilierii din statele contabilizate, câte o linie pe persoană (secțiunea A, tip asigurat 3, natura venitului *Zilier*); un stat anulat dispare la următorul calcul.
- **Rămâne manual:** transmiterea în registrul electronic ITM și verificarea plafonului de 120 de zile pe an la toți beneficiarii.

#### 3. Dependențe

- `account`
- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md)
- `l10n_ro_partner_cnp`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.day.labourer.work`: poziția din registrul zilierilor (zilier, zi, ore, tarif, verificările legale).
- `l10n.ro.day.labourer.payroll`: statul de plată (cu `mail.thread`, secvență proprie), cu calcul, confirmare și contabilizare.
- `l10n.ro.day.labourer.payroll.line`: linia statului, pe zilier.
- `l10n.ro.d112` / `l10n.ro.d112.employee.line` (extinse): preluarea zilierilor în D112.
- `res.company` / `res.config.settings` (extinse): contul de cheltuieli și jurnalul zilierilor.

**Vizualizări**

- `view_day_labourer_work_list` / `view_day_labourer_work_search`: registrul zilierilor.
- `view_day_labourer_payroll_form` / `view_day_labourer_payroll_list`: statul de plată.
- `res_config_settings_view_form_day_labourers`: setările zilierilor.
- `action_report_day_labourer_payroll`: raportul tipărit al statului de plată.

**Acțiuni Automate / Acțiuni Server**

- Niciuna (doar secvența `seq_day_labourer_payroll` pentru numerotarea statelor).

#### 5. Conexiuni

- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md): declarația D112 care preia zilierii din statele contabilizate.
- `l10n_ro_partner_cnp`: CNP-ul partenerului zilier.
