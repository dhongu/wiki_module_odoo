# Romania - Bază ANAF (localizat la `l10n_ro_anaf_base/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_base`
- **Versiune:** `20.0.1.6.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_anaf_base
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_base`
- **Ultima Ingestie:** `2026-11-27`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul de bază (ascuns, fără interfață proprie pentru utilizatori) care oferă infrastructura
comună pentru toate declarațiile fiscale ANAF din suita `l10n_ro_ent`. Centralizează logica
de generare și export a declarațiilor către ANAF (Soft A — Adobe XDP și Soft J — XML),
eliminând duplicarea codului între modulele individuale D300, D390, D394, D398 etc. Nu se
instalează manual — este adus automat ca dependență de fiecare modul de declarație ANAF.

#### 2. Funcționalități Cheie

- Mixin pentru handlere de rapoarte (`L10nRoAnafReportHandlerMixin`) — date companie (CUI,
  CAEN, județ cu cod ANAF 01–52, reprezentant legal), date declarant (nume, prenume, funcție,
  identificator fiscal/CNP, email, telefon, adresă) cu fallback pe userul curent.
- Validare companie înainte de export: VAT, adresă fiscală, județ, CAEN, contact.
- Validare parteneri: VAT obligatoriu pentru partenerii incluși în declarații.
- Validare XML față de schemele XSD oficiale ANAF.
- Generare automată a numelui de fișier conform convențiilor ANAF.
- Export XDP (Adobe) direct, ZIP cu XDP + PDF sau PDF ANAF completat direct (actualizare
  incrementală, păstrează extensiile Adobe Reader; necesită `pypdf` ≥ 5.0, altfel revine la ZIP).
- Helper-e pentru adăugarea butoanelor de export XML și XDP în interfața rapoartelor contabile.
- Registru de profile de declarații (`anaf_declaration_profile`) — mecanism centralizat de
  înregistrare și selecție a versiunilor de formulare ANAF, cu suport pentru perioade istorice.
- Extensii pe `res.company`/`res.config.settings`: persoană responsabilă declarații
  (**Setări → Contabilitate → Declarații ANAF → Persoana responsabilă**), identificator
  declarant (`Declaration Identifier`, folosește VAT/CNP-ul persoanei selectate dacă e gol) și
  tip export implicit (**XDP direct**, **Arhivă ZIP** sau **PDF cu datele incluse**, implicit PDF).
- Cod CAEN al declarațiilor ținut pe companie (`l10n_ro_anaf_caen_code`, 4 cifre), separat de
  `l10n_ro_caen_code` de pe partener; la migrare se preia din codul vechi al partenerului companiei.
- Nomenclator de coduri de produs D394 (`l10n_ro.d394.product.code`, grupe cereale / categorii
  ANAF, marcaje pentru sumarele C și D), atribuibil pe produs sau pe categorie (cu moștenire de la
  categoria părinte); meniu **Contabilitate → Declarații ANAF → D394 product codes**.
- Determinarea codului NC al produsului din primul câmp completat (`l10n_ro_nc_code`,
  `l10n_ro_nc8_code`, cod Intrastat, `hs_code`), cu liste de coduri pentru taxarea inversă.
- Facturi demo românești (TVA 21% / 11%) postate pe compania demo.
- Instalare rapidă din setări a modulelor D300, D390, D394 și D398.
- Meniu comun **Contabilitate → Declarații ANAF**, sub care fiecare modul individual
  (D300, D390, D394, D398 etc.) își înregistrează propriul sub-meniu.
- Convenție unică de împărțire a numelui (`_split_contact_name`): primul cuvânt din câmpul
  `name` este considerat nume de familie, restul prenume — se scrie „Popescu Ion", nu
  „Ion Popescu" — aplicată atât persoanei responsabile cu declarațiile, cât și liniilor
  nominale din D112.
- Clasă de bază pentru teste (`AnafTestCommon`, `tests/common.py`) — reutilizabilă de toate
  modulele ANAF pentru configurarea automată a companiei RO și a contactului ANAF în teste.

#### 3. Dependențe

- `account_reports`
- [l10n_ro](../l10n_ro/index.md)
- `accountant`
- `l10n_ro_move_guard`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.report.handler.mixin` (`anaf_report_handler_mixin.py`): mixin comun pentru
  handlerele de rapoarte ANAF (date companie/declarant, validări, generare XML/XDP/ZIP).
- `anaf.declaration.profile` (`anaf_declaration_profile.py`): registru al profilelor de
  declarații ANAF, cu suport pentru versiuni istorice de formulare.
- `l10n_ro.d394.product.code` (`l10n_ro_d394_product_code.py`): nomenclatorul codurilor de produs D394.
- `product.template` / `product.category` (`product_template.py`, `product_category.py`): câmpul
  `l10n_ro_d394_code_id`.
- `product.product` (`product_product.py`): `_l10n_ro_d394_code` (cod produs → categorie → părinți),
  `_l10n_ro_nc_code` și coduri pentru taxarea inversă.
- `account.chart.template` (`account_chart_template.py`): pregătirea și postarea facturilor demo ANAF.
- `account.report` (`account_report.py`): metode helper pentru export XML și înregistrarea
  tipului MIME `application/vnd.adobe.xdp+xml` pentru fișierele `.xdp`.
- `res.company` (`res_company.py`): `l10n_ro_anaf_caen_code`, `l10n_ro_anaf_declaration_contact_id`,
  `l10n_ro_anaf_declaration_identifier` și `l10n_ro_anaf_export_type`.
- `res.config.settings` (`res_config_settings.py`): setările de configurare comună ANAF și
  instalarea rapidă a modulelor de declarații.

**Vizualizări**

- `anaf_menu.xml`: meniul părinte `menu_account_anaf_declarations` (**Contabilitate →
  Declarații ANAF**), sub `account.menu_finance_reports`, plus meniul codurilor D394.
- `l10n_ro_d394_product_code_views.xml`, `product_views.xml`, `res_company_views.xml`: vizualizări
  pentru coduri D394, câmpul de cod pe produs/categorie și CAEN pe companie.
- `res_config_settings_views.xml`: secțiunea de setări comună ANAF (persoană responsabilă,
  identificator declarant, CAEN, tip export, instalare module D300/D390/D394/D398).

**Acțiuni Automate / Acțiuni Server**

- Nu definește `ir.cron`, `base.automation` sau `ir.actions.server` proprii.

#### 5. Conexiuni

- [l10n_ro_anaf_d100](../l10n_ro_anaf_d100/index.md): declarația D100, extinde mixin-ul
  și infrastructura din acest modul.
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): declarația privind TVA D300.
- [l10n_ro_anaf_d390](../l10n_ro_anaf_d390/index.md): declarația recapitulativă
  intracomunitară D390.
- [l10n_ro_anaf_d394](../l10n_ro_anaf_d394/index.md): declarația informativă
  livrări/achiziții D394.
- [l10n_ro_anaf_d398](../l10n_ro_anaf_d398/index.md): declarația specială de TVA (OSS) D398.
- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md): declarația privind obligațiile de
  plată la bugetul de stat D112, folosește aceeași convenție de nume de familie/prenume
  pentru liniile nominale.
- `l10n_ro_move_guard`: dependență directă din manifest.
- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md): date suplimentare de parteneri
  folosite la validarea și completarea declarațiilor ANAF.
- `account_reports`: infrastructura de rapoarte contabile pe care se bazează handlerele ANAF.
- `l10n_ro`: localizarea românească de bază (plan de conturi, date fiscale companie).
- `accountant`: modulul Enterprise de contabilitate din care se extind rapoartele.
