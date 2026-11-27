# Romania - Decont de TVA (D300) (localizat la `l10n_ro_anaf_d300/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d300`
- **Versiune:** `19.0.0.0.40`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d300
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d300`
- **Ultima Ingestie:** `2026-11-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul destinat departamentelor financiar-contabile din România care au obligația depunerii Decontului de TVA (Declarația 300) la ANAF. Permite generarea și exportul D300 direct din Odoo, în două formate acceptate oficial (XDP și XML), pornind din jurnalele de TVA ale perioadei, fără re-introducerea manuală a datelor. Fișierul generat se descarcă din Odoo și se depune de utilizator pe portalul e-guvernare.ro; modulul nu transmite nimic automat către ANAF. Necesită Odoo Enterprise (motorul `account_reports`).

#### 2. Funcționalități Cheie

- **Fără re-introducere de date**: codurile liniilor din raportul de taxe (`tax_ro_baza_rdX` / `tax_ro_tva_rdX`) se mapează automat pe rândurile R1–R44 ale declarației, din jurnalele de vânzări și cumpărări.
- **Raport D300 pe două coloane (Bază și TVA)**: în **Contabilitate → Raportare → Declarații ANAF → Declarație 300**, grupat pe secțiuni (I. TVA colectată, II. TVA deductibilă, III. Regularizări); raportul clasic rămâne în **Raport TVA**.
- **Două formate, un singur flux**: XDP (Soft A, import în formularul PDF inteligent ANAF) și XML (Soft J, pentru DUKIntegrator), ambele din același raport.
- **Validare XSD înainte de descărcare**: structura XML se verifică față de schema oficială (`d300_v12.xsd`); datele companiei (CUI, județ, adresă, reprezentant) se validează înainte de export, iar o eroare oprește generarea.
- **Tip decont detectat din interval**: lunar (L, 301), trimestrial (T, 302), semestrial (S, 303), anual (A, 304), cu numărul de evidență al plății generat conform algoritmului ANAF; un interval nestandard oprește exportul cu eroare.
- **Sold reportat preluat automat**: rd. 38 din TVA-ul de plată rămas neachitat (cont 4423, minus plățile din perioadă), rd. 41 din soldul negativ reportat (cont 4424), fără sumele cerute la rambursare.
- **Cerere de rambursare din închiderea de TVA**: bifa „Solicit rambursarea TVA" și contul bancar se aleg pe perioadă; declarația primește banca și IBAN-ul, iar exportul se oprește (eroarea R24) dacă soldul negativ (rd. 45) este sub 5.000 lei.
- **Bife art. 331 (taxare inversă)**: cereale, telefoane mobile, circuite integrate, console / tablete / laptopuri, recunoscute după codul NC al produsului (ca în D394) sau bifate pe închiderea de TVA.
- **TVA la încasare (CABA)**: baza și TVA neexigibil din facturile neîncasate la sfârșitul perioadei sunt raportate distinct de TVA exigibil.
- **Integrare cu `account.return`**: în lista de verificări a declarației apar „Generează D300 (TVA)", „Atașează D300 (XML semnat)" și „Opțiuni decont D300"; accesibilă și din **Contabilitate → Contabilitate → Perioade fiscale**.
- **Setări la nivel de companie** (**Contabilitate → Configurare → Setări**, secțiunea Declarații ANAF): „Depus de reprezentant", „Bifă operațiuni interne" și „Temei legal" (0 = standard, 2 = art. 324 alin. (14) Cod fiscal).
- **Totaluri ca în validatorul ANAF**: rd. 19 și rd. 30 sunt suma rândurilor rotunjite, iar rd. 30 nu include achizițiile scutite de la rd. 29.
- **TVA nededusă (art. 298, OPANAF 174/2026)**: rd. 24 / 25 și rd. 30 au TVA-ul brut, rd. 31 doar TVA-ul efectiv dedus, rotunjit o singură dată; se recunosc taxele cu repartiție parțială (ex. „21% ND 50%") și „Deductibilitate" pe linie.
- **Corecturi pe planul RO**: servicii intracomunitare pe rd. 3 / 3.1; servicii de la prestatori din afara UE autolichidate pe rd. 7 și 22 (art. 307 alin. (2)); factura furnizorului extern la import nu se mai declară a doua oară lângă DVI; import cu TVA amânată la plată în vamă („21% IMP AM" / „11% IMP AM", art. 326 alin. (5)); cotele anterioare (19%, 9%, 5%) apar pe rd. 16 / 33. Planurile existente se corectează la instalare/actualizare.
- **Versiune formular acceptată**: v12.0.2, OPANAF 174/2026 (în vigoare de la 01.01.2026); verificat cu DUKIntegrator (soft J 12.0.1) la 12.09.2026.

#### 3. Dependențe

- `account`
- `l10n_ro`
- `account_reports`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md)
- `l10n_ro_reports`

#### 4. Componente Cheie

**Modele**

- `l10n_ro_anaf_d300.tax.report.handler`: handlerul raportului D300 (extinde `account.tax.report.handler` și mixinul ANAF din `l10n_ro_anaf_base`); mapează rândurile, calculează soldurile reportate și generează exporturile XDP / XML.
- `account.report`, `account.return`: extinse pentru raportul pe grile și pentru verificările și opțiunile D300 pe declarația perioadei (rambursare, bife art. 331).
- `res.company`, `res.config.settings`: parametrii D300 (depus de reprezentant, bifă operațiuni interne, temei legal).
- `account.chart.template`: extins pentru corectarea taxelor și grilelor D300 pe planul RO.

**Vizualizări**

- `views/account_return_views.xml`: opțiunile decontului pe declarația perioadei.
- `views/res_config_settings_views.xml`: setările D300 din configurarea contabilității.
- `views/tax_report_xdp_export.xml`, `views/tax_report_xml_export.xml`: șabloanele fișierelor XDP și XML.
- `data/d300_grid_report.xml`, `data/d300_menu.xml`: raportul pe două coloane și meniul „Declarație 300".

**Acțiuni Automate / Acțiuni Server**

- Nu există `ir.cron` sau acțiuni server. `data/return_checks.xml` definește verificările adăugate în lista declarației, iar `post_init_hook` corectează taxele și grilele planurilor existente.

#### 5. Conexiuni

- [l10n_ro_anaf_d394](../l10n_ro_anaf_d394/index.md): reconciliere cu jurnalele de TVA din D394 (rapoartele jurnalelor de vânzări și cumpărări) și aceeași recunoaștere a codurilor NC.
- [l10n_ro_vat_deductibility](../l10n_ro_vat_deductibility/index.md): metoda de calcul al TVA nededus poate fi suprascrisă pentru pro-rata pe perioade.
