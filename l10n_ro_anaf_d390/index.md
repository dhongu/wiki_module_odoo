# ANAF D390 (localizat la `l10n_ro_anaf_d390/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d390`
- **Versiune:** `19.0.0.0.5`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d390
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d390`
- **Ultima Ingestie:** 2026-08-20
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul automatizează generarea Declarației recapitulative D390 (VIES) privind livrările, achizițiile și prestările intracomunitare, pentru companiile înregistrate în scopuri de TVA în România care efectuează operațiuni intracomunitare. Declarația este obligatorie conform Art. 325 din Codul Fiscal și se depune lunar, până pe 25 ale lunii următoare. Modulul construiește un raport în stil contabil pe baza listei standard Odoo „Listă Vânzări/Achiziții CE", clasifică automat operațiunile pe baza tag-urilor fiscale românești din `l10n_ro`, produce fișierele de depunere către ANAF și integrează D390 în lista declarațiilor fiscale (`account.return`), cu termen legal calculat și verificări proprii, eliminând completarea manuală pe fiecare partener UE.

#### 2. Funcționalități Cheie

- Raport „Listă vânzări/achiziții CE" adaptat pentru România, accesibil din meniul **Contabilitate → Declarații ANAF → Declarație 390**.
- Clasificare automată a operațiunilor în categoriile D390 pe baza tag-urilor fiscale românești: **L** (livrări bunuri), **P** (prestări servicii), **T** (triunghiulare), **A** (achiziții bunuri) și **S** (achiziții servicii).
- Export **XDP (Soft A)** — fișier Adobe XDP gata de importat în formularul PDF inteligent de pe portalul ANAF.
- Export **XML (Soft J)** — fișier XML conform schemei oficiale ANAF v3 (2021+), validat automat împotriva schemei XSD înainte de descărcare și compatibil cu DUKIntegrator.
- Butoanele de export (XML / XDP) sunt afișate permanent în bara de sus a raportului.
- Validare automată înainte de export: cod TVA companie, adresă fiscală completă, cod TVA al partenerilor UE cu prefix de țară corect.
- Date declarant preluate automat din câmpul de contact ANAF configurat în setările companiei (funcție — fallback „CONTABIL" —, prenume, nume).
- Agregare pe perechea partener + tip operație, cu eliminarea automată a sumelor zero.
- D390 apare în lista declarațiilor fiscale (`account.return`), cu termenul legal calculat automat (ziua 25 a lunii următoare perioadei) și cu două verificări proprii: operațiunile intracomunitare ale perioadei (cu acțiune directă către raport) și partenerii fără cod de TVA sau fără țară, care altfel ar bloca exportul.
- Suport pentru **declarație rectificativă**: caracterul rectificativ se deduce automat din istoric (dacă declarația a fost deja depusă pentru perioadă), fără bifă manuală și fără dialog suplimentar.
- Categoria de comerț triunghiular (cod `T`) este funcțională: tag fiscal dedicat (`01T - TAX BASE`) și taxă de vânzare `0% EU T`, creată automat la instalare inclusiv pe companiile RO care au deja planul de conturi instalat.

#### 3. Dependențe

- `account`
- `l10n_ro`
- `account_reports`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n_ro_anaf_d390.tax.report.handler`: handlerul raportului D390. Moștenește handlerul standard Odoo `account.ec.sales.report.handler` și mixin-ul `l10n_ro_anaf.report.handler.mixin` din `l10n_ro_anaf_base`. Atașat raportului `l10n_ro_d390_report` (cu rădăcina `account_reports.generic_ec_sales_report`), clasifică operațiunile pe categorii D390 după numele tag-urilor fiscale (nu prin expresiile raportului de TVA, pentru a evita o capcană tăcută de filtrare pe motor `tax_tags`), grupează partenerii UE pe tip de operațiune și adaugă butoanele de export ANAF.
- `account.return` (extindere, `models/account_return.py`): integrează D390 în fluxul standard de declarații fiscale — calculează termenul legal de depunere, deduce declarația care acoperă perioada raportată (pentru a decide dacă exportul este inițial sau rectificativ) și rulează verificările proprii ale declarației.
- `account.chart.template` (extindere, `models/account_chart_template.py`): definește taxa de vânzare `0% EU T` (referință `tvati_intrat`) pentru comerțul triunghiular intracomunitar, cu linie de repartiție purtătoare a tag-ului `01T - TAX BASE`; taxa nu este atașată la poziții fiscale, fiind aleasă explicit pe factura de livrare triunghiulară.
- `hooks.py` (`post_init_hook`): creează taxa de comerț triunghiular și pe companiile RO care au deja planul de conturi instalat, caz neacoperit de încărcarea standard prin `@template`.

**Vizualizări**

- `l10n_ro_d390_report` (`views/account_report_views.xml`): definirea raportului `account.report` D390, cu coloanele cod țară, număr TVA, tip operațiune și sumă.
- `d390_report_xml_template` (`views/d390_report_xml_export.xml`): template-ul QWeb pentru exportul XML (Soft J), conform schemei `mfp:anaf:dgti:d390:declaratie:v3`.
- `views/d390_report_export.xml`: template-ul de export XDP (Soft A).
- `views/d390_menu.xml`: intrarea de meniu **Declarație 390**.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate sarcini `ir.cron`; exportul fișierelor se declanșează manual din butoanele raportului, iar generarea nu este legată de validarea declarației (validarea nu ar putea trece niciodată de propriul fișier atașat prin șablonul de verificare).*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): infrastructura comună pentru declarațiile ANAF (mixin handler, butoane export, date declarant).
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): corelarea operațiunilor intracomunitare cu decontul de TVA, fără dublarea sumelor.
- [l10n_ro_anaf_d394](../l10n_ro_anaf_d394/index.md): reconciliere cu jurnalul TVA (D394 acoperă operațiunile interne, D390 pe cele intracomunitare).
- [l10n_ro_doc_screenshots](../l10n_ro_doc_screenshots/index.md): mixinul `ScreenshotCase` folosit pentru generarea automată a capturilor din fișa modulului.
