# Romania - Decont de TVA (D300) (localizat la `l10n_ro_anaf_d300/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d300`
- **Versiune:** `20.0.0.0.35`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_anaf_d300
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d300`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul destinat departamentelor financiar-contabile din România care depun Decontul de TVA (Declarația 300) la ANAF. Generează și exportă D300 direct din Odoo, în două formate acceptate oficial, fără reintroducerea manuală a datelor. Fișierul se descarcă din Odoo și se validează, semnează și depune de utilizator; modulul nu transmite nimic automat către ANAF. Necesită Odoo Enterprise (`account_reports`).

#### 2. Funcționalități Cheie

- **Mapare automată a rândurilor**: codurile liniilor din raportul de taxe (`tax_ro_baza_rdX` / `tax_ro_tva_rdX`) se mapează pe rândurile R1–R44; raportul pe două coloane (Bază și TVA) se deschide din **Contabilitate → Raportare → Declarații ANAF → Declarație 300**, iar raportul clasic rămâne în **Raport TVA**.
- **Sold reportat preluat automat**: rd. 38 din 4423 (minus plățile din perioadă), rd. 41 din 4424 (fără sumele cerute la rambursare); când rămân ambele solduri se raportează diferența.
- **Cerere de rambursare**: bifa „Solicit rambursarea TVA" și contul bancar se aleg pe perioadă, în verificarea „Opțiuni decont D300"; exportul se oprește pentru sold negativ sub 5.000 lei.
- **Bifele art. 331** (cereale, telefoane mobile, circuite integrate, console / tablete / laptopuri): recunoscute după codul NC al produsului sau bifate manual.
- **TVA la încasare (CABA)**: baza și TVA neexigibil din facturile neîncasate la sfârșitul perioadei, raportate separat.
- **Tip decont detectat din interval**: lunar (L), trimestrial (T), semestrial (S), anual (A), cu numărul de evidență al plății conform ANAF; un interval nestandard oprește exportul cu eroare.
- **Export XDP (Soft A)** și **XML (Soft J)** ca butoane în bara raportului, cu validare a datelor companiei și a XML-ului față de XSD înainte de descărcare (formular v12.0.2, OPANAF 174/2026, schema `d300_v12.xsd`).
- **Corecturi față de TVA-ul standard RO**: totaluri rd. 19 / 30 ca în validatorul ANAF, TVA nededusă (art. 298), servicii intracomunitare (rd. 3.1), servicii de la prestatori din afara UE (rd. 7 și 22), import (art. 326), cotele anterioare 19% / 9% / 5% (rd. 16 / 33).
- **Integrare `account.return`**: verificările „Generează D300 (TVA)", „Atașează D300 (XML semnat)" și „Opțiuni decont D300" în checklistul perioadei.
- **Setări companie** (Setări → Contabilitate → Declarații ANAF): depus de reprezentant, bifă operațiuni interne, temei legal (0 sau art. 324 alin. (14)).

Fluxul detaliat și exemplele de facturi sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `l10n_ro`
- `account_reports`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md)
- `l10n_ro_reports`

#### 4. Componente Cheie

**Modele**

- `account.report` / `l10n_ro_anaf_d300.tax.report.handler` (extins): maparea rândurilor raportului de taxe pe D300 și generarea fișierelor XDP/XML, cu validarea companiei.
- `l10n_ro_anaf_d300.grid.tax.report.handler`: handlerul raportului pe grilă, cu coloanele Bază și TVA.
- `account.chart.template` (extins, inclusiv variantele pentru grile): completează CAEN-ul demo și definește taxele/etichetele necesare grilei.
- `account.return` / `account.return.check` (extinse): verificările D300 din fluxul de închidere, inclusiv opțiunile de rambursare și bifele art. 331.
- `res.company` / `res.config.settings` (extinse): setările D300 la nivel de companie.

**Vizualizări**

- `data/d300_grid_report.xml`: grila raportului D300 pe secțiuni (I. TVA colectată, II. TVA deductibilă, III. Regularizări).
- `data/d300_menu.xml`: intrarea de meniu D300.
- `data/return_checks.xml`: verificările D300 din `account.return`.
- `data/l10n_ro_tax_report_fix.xml`: corecturi ale raportului de TVA standard pentru România.
- `views/account_return_views.xml`: opțiunile de decont în declarație.
- `views/tax_report_xdp_export.xml`, `views/tax_report_xml_export.xml`: exporturile Soft A și Soft J.
- `views/res_config_settings_views.xml`: setările D300.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); exportul se declanșează manual din raport sau din checklistul `account.return`.*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): mapări comune ANAF (județ, reprezentant legal) pentru datele de identificare.
- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md): date ANAF ale partenerului (inclusiv CAEN) folosite la export.
- [l10n_ro_anaf_d394](../l10n_ro_anaf_d394/index.md): declarația informativă; codul NC al produsului este folosit în ambele pentru bifele art. 331.
- [l10n_ro_anaf_d390](../l10n_ro_anaf_d390/index.md): declarația recapitulativă a operațiunilor intracomunitare, din aceeași suită.
- [l10n_ro_anaf_d398](../l10n_ro_anaf_d398/index.md): altă declarație ANAF din aceeași suită.
- [l10n_ro_anaf_d100](../l10n_ro_anaf_d100/index.md): altă declarație ANAF din aceeași suită.
