# Romania - ANAF D398 Declaration (VAT OSS) (localizat la `l10n_ro_anaf_d398/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d398`
- **Versiune:** `19.0.0.0.2`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d398
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d398`
- **Ultima Ingestie:** 2026-06-09

#### 1. Sumar

Modulul permite generarea Declarației Speciale de TVA (D398) direct din Odoo, conform formatului solicitat de ANAF pentru regimul special One Stop Shop (OSS). Este destinat companiilor din România care efectuează livrări de bunuri sau prestări de servicii către consumatori finali (B2C) din alte state membre UE și sunt înregistrate în regimul OSS. Modulul **nu adaugă un ecran propriu**: extinde raportul standard OSS din Enterprise, adăugând butoanele de export ANAF (XML Soft J / XDP Soft A) și coloane de control în EUR (conversie la cursul BCE). Contabilitatea rămâne în RON — modulul adaugă doar conversia de raportare în EUR pentru declarația OSS. Implementarea este aliniată la infrastructura comună din `l10n_ro_anaf_base` (date companie/declarant, registru de profile de declarații, validări pentru resursele de export și pentru datele minime ale companiei).

#### 2. Funcționalități Cheie

- **Export XML D398 (Soft J)** — fișier validat automat față de schema XSD oficială ANAF, compatibil cu DUKIntegrator pentru semnare digitală.
- **Export XDP D398 (Soft A)** — fișier de date pentru import în formularul PDF inteligent ANAF (versiunea 1.0.11+); disponibil și ca ZIP cu PDF inclus.
- **Conversie automată în EUR** — sumele sunt convertite folosind cursul de schimb publicat de Banca Centrală Europeană (BCE) din ultima zi a perioadei fiscale, fără a afecta furnizorul de cursuri BNR configurat pentru restul înregistrărilor contabile.
- **Coloane suplimentare în raportul OSS** — „Net (EUR)" și „Tax (EUR)" vizibile direct în interfața rapoartelor OSS Enterprise, pentru verificarea sumelor înainte de export.
- **Grupare automată** pe state membre de consum (MSCON), tip livrare (bunuri/servicii) și cotă TVA (standard/redusă).
- **Validare date companie** — verifică prezența datelor obligatorii (CUI, județ, date contact) înainte de generarea fișierului.
- **Meniu dedicat** — „Declarație 398" disponibil sub meniul „Declarații ANAF" din modulul Contabilitate.
- **Limitări cunoscute:** avertizarea pentru pragul OSS de 10.000 EUR/an și depunerea automată în portalul ANAF nu sunt încă implementate.

#### 3. Dependențe

- `l10n_ro`
- `account_reports`
- `l10n_eu_oss_reports`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n_eu_oss.tax.report.handler`: handler-ul de raport OSS extins de modul; moștenește handler-ul OSS Enterprise împreună cu `l10n_ro_anaf.report.handler.mixin`, adăugând butoanele de export ANAF D398 (XML Soft J / XDP Soft A) și coloanele în EUR (conversie la cursul BCE).

**Date / Vizualizări**

- `data/account_reports.xml`: extinde raportul standard OSS (`l10n_eu_oss_reports.oss_sales_report`) cu butoanele și coloanele D398.
- `data/d398_menu.xml`: intrarea de meniu „Declarație 398" sub „Declarații ANAF".
- `views/report_export_templates.xml`: template-urile de export XML/XDP.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); exportul se declanșează manual din raportul OSS.*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): infrastructura comună ANAF (validări, butoane XML/XDP, date companie, registru de declarații).
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): D398 este o declarație separată de decontul intern de TVA (D300), dar se reconciliază ca proces TVA.
- [l10n_ro_anaf_d318](../l10n_ro_anaf_d318/index.md): altă declarație ANAF din aceeași suită Enterprise.
- `l10n_eu_oss`: pozițiile fiscale și taxele OSS pe state membre, sursa datelor de TVA OSS.
- `l10n_eu_oss_reports`: raportul OSS Enterprise pe care se bazează exportul D398.
