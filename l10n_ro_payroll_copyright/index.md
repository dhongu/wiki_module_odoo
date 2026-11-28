# Romania - Drepturi de autor (localizat la `l10n_ro_payroll_copyright/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_copyright`
- **Versiune:** `20.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_payroll_copyright
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_copyright`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Contracte și plată pentru drepturile de proprietate intelectuală (art. 70–73 Cod fiscal), cu nota contabilă și preluarea automată în D112. Plătitorul reține la sursă impozitul de 10% pe venitul net (brut minus cheltuieli forfetare de 40%, cu excepțiile din lege), iar CAS și CASS se rețin doar când sunt atinse pragurile și contractul o prevede.

#### 2. Funcționalități Cheie

- **Contractul de drepturi de autor** (*Contabilitate → Contabilitate → Drepturi de autor → Contracte*): autor (persoană fizică cu CNP), dată, opera sau dreptul cedat, regim (cu sau fără cotă forfetară), cont de cheltuieli (implicit 621; 205 pentru imobilizări necorporale).
- **Contribuții la sursă**, opțional pe contract: CAS pe venitul ales (12 sau 24 de salarii minime) și CASS pe baza anuală de 6, 12 sau 24 de salarii minime, după venitul net anual estimat; pragurile se verifică la salvare.
- **Statul de plată** de trei tipuri: *Plată*, *Avans* și *Lichidare*. Calculează brut, cheltuieli forfetare, venit net, impozit, contribuții și rest de plată (sume rotunjite la leu, ca în D112); se tipărește cu coloană de semnătură.
- **Nota contabilă** la contabilizare: `621 = 401` brutul, `401 = 444` impozit, `401 = 4315` CAS, `401 = 4316` CASS (cont modificabil). Pentru imobilizări (20x) contrapartida este 404. Restul de plată se achită cu butonul *Plătește*, integral sau în tranșe.
- **Avans și lichidare**: avansul se contabilizează pe 4092/4094 cu rețineri la plată; lichidarea recunoaște cheltuiala și deduce avansurile, reținerile fiind doar pe diferență.
- **D112**: la *Calculează*, declarația lunii preia autorii din statele contabilizate (secțiunea C, tip asigurat 17, creanțele 611, 451, 461), câte o linie pe autor.
- Configurare în *Contabilitate → Configurare → Setări → Declarații ANAF* (cont de cheltuieli, jurnal, cont CASS, cont furnizori de imobilizări, cont de avansuri). Autorii au nevoie de CNP valid.

#### 3. Dependențe

- `account`
- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md)
- `l10n_ro_partner_cnp`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.copyright.contract`: contractul de drepturi de autor.
- `l10n.ro.copyright.payroll` / `l10n.ro.copyright.payroll.line`: statul de plată și liniile pe autor.
- `l10n.ro.d112`, `l10n.ro.d112.employee.line`, `res.company`, `res.config.settings`: extinse pentru D112 și setări.

**Vizualizări**

- `view_copyright_contract_form` / `_list`: contractele.
- `view_copyright_payroll_form` / `_list`: statele de plată.
- `res_config_settings_view_form_copyright`: setările de conturi.
- `action_report_copyright_payroll`: statul tipărit.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate; există secvențe pentru contracte și state.

#### 5. Conexiuni

- [l10n_ro_payroll_day_labourers](../l10n_ro_payroll_day_labourers/index.md): modul soră pentru zilieri, cu același mecanism de stat, notă contabilă și D112.
- [l10n_ro_anaf_d112_payroll](../l10n_ro_anaf_d112_payroll/index.md): D112 pentru salariați; un salariat cu drepturi de autor apare o singură dată în declarație.
