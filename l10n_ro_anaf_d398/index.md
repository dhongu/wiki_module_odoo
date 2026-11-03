# Romania - Declarația D398 ANAF (TVA OSS) (localizat la `l10n_ro_anaf_d398/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d398`
- **Versiune:** `19.0.0.0.13`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d398
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d398`
- **Ultima Ingestie:** `2026-11-03`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite generarea Declarației Speciale de TVA (D398) direct din Odoo, conform formatului solicitat de ANAF pentru regimul special One Stop Shop (OSS). Este destinat companiilor din România care efectuează livrări de bunuri sau prestări de servicii către consumatori finali (B2C) din alte state membre UE și sunt înregistrate în regimul OSS. Modulul **nu adaugă un ecran propriu**: extinde raportul standard OSS din Enterprise, adăugând butoanele de export ANAF (XML Soft J / XDP Soft A) și coloane de control în EUR, la cursul BCE. Contabilitatea rămâne în RON; conversia în EUR este doar pentru raportarea declarației OSS.

#### 2. Funcționalități Cheie

- **Raport Declarație 398**, la **Contabilitate → Raportare → Declarații ANAF → Declarație 398**: liniile sunt grupate pe stat membru de consum (MSCON), tip livrare (bunuri/servicii) și cotă TVA a statului de consum. Apar doar dacă în perioadă există facturi B2C intra-UE cu poziția fiscală OSS; butoanele de export rămân vizibile și când raportul e gol.
- **Perioade:** regimul UE (OSS) se declară trimestrial, iar regimul de import (IOSS) lunar; exportul se oprește cu mesaj explicit dacă perioada nu corespunde regimului, fiindcă validatorul ANAF ar respinge declarația.
- **Export XML D398 (Soft J)** — fișier validat automat față de schema XSD oficială ANAF (`d398_20211101.xsd`, structura v1.0.11), pentru DUKIntegrator (validare și semnare); sumele sunt convertite în EUR. Opțional se pot exporta PDF sau XLSX pentru arhivă.
- **Export XDP D398 (Soft A)** — fișier de date pentru formularul PDF inteligent ANAF (versiunea 1.0.11+), importat cu *Import Date*; disponibil și ca ZIP cu PDF inclus.
- **Conversie în EUR la cursul BCE** din ultima zi a perioadei, fără a afecta furnizorul de cursuri BNR al restului contabilității. Cursul se descarcă o singură dată pe zi de sfârșit de perioadă și se păstrează în **Contabilitate → Configurare → Cursuri de schimb BCE**, cu ziua publicării; dacă BCE nu poate fi accesată, cursul se introduce manual (cel din ziua de sfârșit sau, dacă nu s-a publicat, din următoarea zi publicată). Fără curs BCE, exportul este refuzat, iar raportul afișează un avertisment și folosește temporar cursul din Odoo.
- **Coloane în raportul OSS:** „Net (EUR)" și „Tax (EUR)", lângă „Amount excl. VAT" și „VAT" în RON; pe subtotalurile pe stat membru coloana Net (EUR) apare goală, ca în raportul OSS standard.
- **Configurare:** bifa **Interfață electronică** în **Contabilitate → Configurare → Setări → Declarații ANAF** (ajunge în atributul `e_int` pentru regimul UE), **Numărul IOSS** pe companie pentru regimul de import (fără el exportul se oprește), CUI și adresa companiei (altfel exportul este respins), plus pozițiile fiscale și taxele OSS ale statelor membre.
- **Limitări:** modulul nu generează note contabile (contabilitatea OSS rămâne cea din `l10n_eu_oss`), nu depune declarația și nu generează referința de plată; avertizarea pentru pragul de 10.000 EUR/an nu e implementată aici (se folosește [l10n_ro_oss_threshold](../l10n_ro_oss_threshold/index.md)).

#### 3. Dependențe

- `l10n_ro`
- `account_reports`
- `l10n_eu_oss_reports`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n_eu_oss.tax.report.handler`: handler-ul de raport OSS extins de modul; moștenește handler-ul OSS Enterprise împreună cu `l10n_ro_anaf.report.handler.mixin`, adăugând butoanele de export ANAF D398 (XML Soft J / XDP Soft A) și coloanele în EUR.
- `l10n_ro.ecb.rate`: cursul BCE (RON pentru 1 EUR) pe ziua de sfârșit de perioadă, cu data publicării și sursa (`ecb` sau `manual`).
- `account.report`, `res.company`, `res.config.settings` (extinse): `res.company` și setările primesc `l10n_ro_oss_electronic_interface` (interfață electronică).

**Date / Vizualizări**

- `data/account_reports.xml`: extinde raportul standard OSS (`l10n_eu_oss_reports.oss_sales_report`) cu butoanele și coloanele D398.
- `data/d398_menu.xml`: acțiunea `l10n_ro_anaf_d398_report_action` și meniul „Declarație 398" sub „Declarații ANAF".
- `views/report_export_templates.xml`: șabloanele de export XML/XDP.
- `l10n_ro_ecb_rate_view_list`, `l10n_ro_ecb_rate_view_search`, `l10n_ro_ecb_rate_action`: lista și acțiunea pentru cursurile BCE.
- `res_config_settings_view_form`: setarea „Interfață electronică".

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); exportul se declanșează manual din raport, iar cursul BCE se descarcă la prima nevoie.*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): infrastructura comună ANAF (validări, butoane XML/XDP, date companie, registru de declarații).
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): D398 este o declarație separată de decontul intern de TVA (D300), dar se reconciliază ca proces TVA.
- [l10n_ro_anaf_d318](../l10n_ro_anaf_d318/index.md): altă declarație ANAF din aceeași suită Enterprise.
- [l10n_ro_oss_threshold](../l10n_ro_oss_threshold/index.md): avertizarea pentru pragul OSS de 10.000 EUR, neacoperită de acest modul.
- `l10n_eu_oss`: pozițiile fiscale și taxele OSS pe state membre, sursa datelor de TVA OSS.
- `l10n_eu_oss_reports`: raportul OSS Enterprise pe care se bazează exportul D398.
