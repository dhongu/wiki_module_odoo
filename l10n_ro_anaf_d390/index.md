# Romania - Declarație recapitulativă (D390) (localizat la `l10n_ro_anaf_d390/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d390`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_anaf_d390
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d390`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul care automatizează **Declarația recapitulativă D390 (VIES)** privind livrările, achizițiile și prestările intracomunitare, obligatorie conform art. 325 Cod fiscal și depusă lunar până pe 25 ale lunii următoare. Extinde raportul Enterprise `l10n_ro_reports_d390` cu clasificarea operațiunilor, validări și exporturile ANAF. Fișierul se validează, semnează și depune de utilizator.

#### 2. Funcționalități Cheie

- Extinde modulul Enterprise „Romania - EC Sales List D390 Report" (`l10n_ro_reports_d390`); raportul, declarația și taxa pentru operațiunile triunghiulare sunt accesibile și din **Contabilitate → Declarații ANAF → Declarație 390**.
- **Clasificare automată** pe baza tag-urilor fiscale din `l10n_ro`: L (livrări bunuri), P (prestări servicii), T (triunghiulare), A (achiziții bunuri), S (achiziții servicii); agregare pe partener + tip operație, fără sume zero.
- **XML corect și în fluxul standard** al declarației (validare / depunere): fără secțiunea `<cos>` falsă, achiziții pozitive, totaluri conform regulilor ANAF R13/R16/R21, regularizări negative cu semnul lor.
- **Export XDP (Soft A)** pentru formularul PDF inteligent, cu tip de export configurabil (XDP, ZIP sau PDF cu date), și **XML (Soft J)** conform schemei v3, validat cu `d390_12022021.xsd` (formular OPANAF 705/2020).
- **Validare înainte de export**: cod TVA companie, adresă fiscală completă, cod TVA al partenerilor UE cu prefix de țară.
- **Date declarant** din fereastra declarației, precompletate din „Contact declarant ANAF" din setările companiei; declarația rectificativă este bifată automat dacă declarația a mai fost depusă.
- Pas manual de atașare a XML-ului semnat / recipisei în `account.return`.

Fluxul detaliat este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `l10n_ro_reports_d390`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n_ro.ec.sales.report.handler` (extins, cu `l10n_ro_anaf.report.handler.mixin`): clasifică operațiunile pe categorii D390, grupează partenerii UE și adaugă butoanele de export ANAF.
- `account.return` (extindere): termenul legal de depunere, determinarea exportului inițial/rectificativ și verificările declarației.
- `l10n_ro_reports_d390.generate.ec.sales.report.wizard` (extins): fereastra de validare, cu datele declarantului precompletate și bifa rectificativă.

**Vizualizări**

- `views/account_report_views.xml`: raportul D390 (cod țară, număr TVA, tip operațiune, sumă).
- `views/d390_report_xml_export.xml`: șablonul XML (Soft J), schema `mfp:anaf:dgti:d390:declaratie:v3`.
- `views/d390_report_export.xml`: exportul XDP (Soft A).
- `views/d390_menu.xml`: meniul **Declarație 390**.
- `data/d390_return_checks.xml`: verificarea „Attach D390 (Signed XML / ANAF Receipt)".

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); exportul se declanșează manual din butoanele raportului sau din validarea declarației.*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): infrastructura comună ANAF (mixin handler, butoane export, date declarant).
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): corelarea operațiunilor intracomunitare cu decontul de TVA.
- [l10n_ro_anaf_d394](../l10n_ro_anaf_d394/index.md): reconciliere cu jurnalul TVA (D394 acoperă operațiunile interne, D390 pe cele intracomunitare).
- `l10n_ro_reports_d390`: modulul Enterprise de bază, extins de acest modul.
