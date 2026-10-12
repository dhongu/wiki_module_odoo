# Romania - Drepturi de autor (localizat la `l10n_ro_payroll_copyright/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_copyright`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_payroll_copyright
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_copyright`
- **Ultima Ingestie:** `2026-10-12`

#### 1. Sumar

Modulul gestionează contractele și plata **drepturilor de proprietate intelectuală** (drepturi de autor și conexe, art. 70–73 din Codul fiscal). Plătitorul reține la sursă impozitul de 10% pe venitul net (brut minus cheltuielile forfetare de 40%, unde se aplică), iar CAS și CASS se rețin doar când sunt îndeplinite pragurile legale și contractul o prevede. Modulul generează statul de plată (de plată, avans sau lichidare), nota contabilă, plata din casă sau bancă și preia automat autorii în declarația D112.

#### 2. Funcționalități Cheie

- **Contractul de drepturi de autor**: autorul (persoană fizică cu CNP), data, opera sau dreptul cedat, regimul (cu sau fără cotă forfetară) și contul de cheltuieli (implicit 621; de exemplu 205 când dreptul se recunoaște ca imobilizare necorporală). Contractul se pornește cu **Începe**; doar contractele în curs pot fi plătite.
- **Contribuții reținute la sursă**, opțional pe contract:
  - CAS pe venitul ales (cel puțin 12 salarii minime, respectiv 24 când venitul net estimat atinge 24);
  - CASS pe baza anuală de 6, 12 sau 24 de salarii minime, după venitul net estimat;
  - salariul minim este cel de la 1 ianuarie al anului (4.050 lei în 2026);
  - verificarea pragurilor la salvare, cu atenționare la plătitor unic, unde reținerea este obligatorie.
- **Statul de plată** (*Drepturi de autor → State de plată*), de trei tipuri: *Plată* (venitul se recunoaște și se plătește odată), *Avans* și *Lichidare*. Pe data plății: brut, cheltuieli forfetare, venit net, impozit, baze și contribuții (tranșe lunare de 1/12 din baza anuală, ajustabile; un avans și o lichidare în aceeași lună rețin două tranșe), rest de plată; sume rotunjite la leu ca în D112. Flux: **Confirmă**, **Tipărește** (cu coloană de semnătură), **Contabilizează**, **Plătește**.
- **Nota contabilă** (OMFP 1802/2014): `621 = 401` (brut), `401 = 444` (impozit), `401 = 4315` (CAS), `401 = 4316` (CASS, schimbabil, de ex. 4318). Reținerile se sting în 401 cu brutul din aceeași notă, deci rămâne deschis doar restul de plată. Pentru imobilizări necorporale (20x) contrapartida este `404`. Statul nu se confirmă dacă reținerile depășesc brutul.
- **Plata statului**: butonul *Plătește* (pe stat sau pe linia autorului), din jurnal de casă sau bancă, integral sau în tranșe; coloanele *Plătit* și *Rest de plată* arată situația. Plătiți tranșele în luna statului (impozitul se declară pe luna reținerii; o plată ulterioară se face pe un stat nou). Pentru casă, jurnalul de numerar trebuie să aibă contul de plăți în curs setat la contul casei (5311). Un stat cu plăți nu se mai poate anula.
- **Avans și lichidare**: avansul reține impozitul și contribuțiile la plată și se înregistrează `4092 = 401` (`4094 = 404` pentru imobilizări), cu reținerile `401 = 444 / 4315 / 4316`. Lichidarea recunoaște cheltuiala pe venitul total al operei (`621 = 401`), deduce avansurile contractului (propuse automat din cele contabilizate și nededuse; `401 = 4092`, reconciliat) și reține doar pe diferență. Nu se confirmă dacă venitul total e sub avansuri; un avans dedus nu se anulează cât timp lichidarea există.
- **D112**: la *Calculează*, declarația lunii preia drepturile de autor din statele contabilizate, câte o linie pe autor, în secțiunea C (tip asigurat 17), cu creanțele 611, 451 și 461. Avansul intră pe luna lui, iar lichidarea doar cu diferența de venit. Un salariat cu drepturi de autor apare o singură dată, cu ambele venituri. Veniturile din drepturi de autor nu se mai declară în D205.
- **Configurare** (*Contabilitate → Configurare → Setări*, secțiunea Declarații ANAF): cont de cheltuieli, jurnal, cont CASS, cont furnizori de imobilizări, cont de avansuri (implicit 4092, respectiv 4094 pentru 20x); conturile de impozit (444) și CAS (4315) vin din setările D112.

#### 3. Dependențe

- `account`
- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md)
- `l10n_ro_partner_cnp`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.copyright.contract`: contractul de drepturi de autor (cu `mail.thread`).
- `l10n.ro.copyright.payroll`: statul de plată (plată/avans/lichidare) pe data plății, cu notă contabilă și plăți.
- `l10n.ro.copyright.payroll.line`: linia statului, câte una pe contract.
- `l10n.ro.d112` și `l10n.ro.d112.employee.line` (extinse): preiau autorii din state în D112.
- `res.company`, `res.config.settings` (extinse): conturile și jurnalul pentru drepturi de autor.

**Vizualizări**

- `view_copyright_contract_form` / `view_copyright_contract_list`: contractele.
- `view_copyright_payroll_form` / `view_copyright_payroll_list`: statele de plată.
- `res_config_settings_view_form_copyright`: setările în Contabilitate.
- `action_report_copyright_payroll`: raportul tipărit al statului de plată.
- Meniu: `menu_copyright` (Drepturi de autor), cu Contracte și State de plată.

**Acțiuni Automate / Acțiuni Server**

- Nu are `ir.cron` sau acțiuni server; doar secvența pentru numerotarea statelor (`data/ir_sequence_data.xml`).

#### 5. Conexiuni

- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md): declarația în care se preiau autorii (secțiunea C).
