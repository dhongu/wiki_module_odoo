# Romania - Zilieri (localizat la `l10n_ro_payroll_day_labourers/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_day_labourers`
- **Versiune:** `20.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_payroll_day_labourers
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_day_labourers`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Evidența și plata zilierilor (Legea 52/2011), cu nota contabilă și preluarea automată în D112. Remunerația zilierului este venit asimilat salariilor: beneficiarul reține CAS 25% din brut și impozit 10% pe brut minus CAS; nu se datorează CASS, CAM sau contribuția de șomaj.

#### 2. Funcționalități Cheie

- **Registrul zilierilor**: o poziție pe zilier și zi, cu ore lucrate, tarif orar brut (implicit salariul minim pe oră), domeniul de activitate, locul, bifa *Transmis în registrul ITM* și codul de confirmare din aplicația ITM.
- **Verificări din lege** la salvare: tarif minim pe oră, cel mult 12 ore pe zi (plată minim 8 ore), cel mult 25 de zile continuu, 90 de zile pe an la același beneficiar (180 în agricultură și domenii asimilate), un zilier o singură dată pe zi.
- **Statul de plată** (*Zilieri → State de plată*): *Calculează din registru* preia zilele neplătite din perioadă; calculează brut, CAS, impozit și rest de plată; *Confirmă* cere CNP valid; *Tipărește* scoate statul pentru semnătură.
- **Nota contabilă** la *Contabilizează*: `621 = 401` brutul, `401 = 4315` CAS, `401 = 444` impozit.
- **Plata integrală sau în tranșe**: butonul *Plătește* pe stat sau pe linia zilierului (casă sau bancă); *Tipărește plățile* scoate lista cu semnături. Statul cu plăți nu se anulează până nu se anulează plățile.
- **Aplicația ITM**: export al zilierilor selectați în CSV-ul de contacte (5 coloane) și import al CSV-ului din aplicație, potrivit pe CNP, cu raport de diferențe și creare de parteneri lipsă (cetățenii străini se creează manual).
- **D112**: *Calculează* preia zilierii din statele contabilizate (secțiunea A, tip asigurat 3), câte o linie pe persoană.
- Rămâne manuală transmiterea zilnică în aplicația ITM și verificarea plafonului de 120 de zile pe an.

#### 3. Dependențe

- `account`
- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md)
- `l10n_ro_partner_cnp`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.day.labourer.work`: poziția din registru (zilier și zi).
- `l10n.ro.day.labourer.payroll` / `l10n.ro.day.labourer.payroll.line`: statul de plată și liniile pe zilier.
- `l10n.ro.day.labourer.itm.export`: asistent de export CSV pentru aplicația ITM.
- `l10n.ro.day.labourer.itm.import` / `l10n.ro.day.labourer.itm.import.line`: asistent de import și verificare a contactelor ITM.
- `l10n.ro.d112`, `l10n.ro.d112.employee.line`, `res.company`, `res.config.settings`: extinse.

**Vizualizări**

- `view_day_labourer_work_list` / `_search`: registrul zilierilor.
- `view_day_labourer_payroll_form` / `_list`: statele de plată.
- `view_day_labourer_itm_export_form`, `view_day_labourer_itm_import_form`: asistenții ITM.
- `action_report_day_labourer_payroll`, `action_report_day_labourer_payments`: rapoartele PDF.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate; există secvențe pentru state.

#### 5. Conexiuni

- [l10n_ro_payroll_copyright](../l10n_ro_payroll_copyright/index.md): modul soră pentru drepturi de autor, cu același mecanism de stat și D112.
- [l10n_ro_anaf_d112_payroll](../l10n_ro_anaf_d112_payroll/index.md): D112 pentru salariați.
