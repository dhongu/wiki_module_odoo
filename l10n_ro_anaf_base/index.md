# Romania - Bază ANAF (localizat la `l10n_ro_anaf_base/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_base`
- **Versiune:** `20.0.1.3.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_anaf_base
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_base`
- **Ultima Ingestie:** `2026-09-27`
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
- Export XDP (Adobe) cu înglobare PDF și împachetare ZIP.
- Helper-e pentru adăugarea butoanelor de export XML și XDP în interfața rapoartelor contabile.
- Registru de profile de declarații (`anaf_declaration_profile`) — mecanism centralizat de
  înregistrare și selecție a versiunilor de formulare ANAF, cu suport pentru perioade istorice.
- Extensii pe `res.company`/`res.config.settings`: persoană responsabilă declarații
  (**Setări → Contabilitate → Declarații ANAF → Persoana responsabilă**), identificator
  declarant (`Declaration Identifier`, folosește VAT/CNP-ul persoanei selectate dacă e gol) și
  tip export implicit (**XDP direct** vs. **Arhivă ZIP**, implicit ZIP).
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

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.report.handler.mixin` (`anaf_report_handler_mixin.py`): mixin comun pentru
  handlerele de rapoarte ANAF (date companie/declarant, validări, generare XML/XDP/ZIP).
- `anaf.declaration.profile` (`anaf_declaration_profile.py`): registru al profilelor de
  declarații ANAF, cu suport pentru versiuni istorice de formulare.
- `account.chart.template` (`account_chart_template.py`): extensii de plan de conturi legate
  de declarațiile ANAF.
- `account.move` (`account_move.py`): extensii pe factură/notă contabilă necesare rapoartelor.
- `account.report` (`account_report.py`): metode helper pentru export XML și înregistrarea
  tipului MIME `application/vnd.adobe.xdp+xml` pentru fișierele `.xdp`.
- `res.company` (`res_company.py`): câmpurile `l10n_ro_anaf_declaration_contact_id`,
  `l10n_ro_anaf_declaration_identifier` și `l10n_ro_anaf_export_type`.
- `res.config.settings` (`res_config_settings.py`): setările de configurare comună ANAF și
  instalarea rapidă a modulelor de declarații.
- `res.partner` (`res_partner.py`): câmpuri/validări legate de partenerii incluși în declarații.

**Vizualizări**

- `anaf_menu.xml`: meniul părinte `menu_account_anaf_declarations` (**Contabilitate →
  Declarații ANAF**), sub `account.menu_finance_reports`.
- `res_config_settings_views.xml`: secțiunea de setări comună ANAF (persoană responsabilă,
  identificator declarant, tip export, instalare module D300/D390/D394/D398).

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
- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md): date suplimentare de parteneri
  folosite la validarea și completarea declarațiilor ANAF.
- `account_reports`: infrastructura de rapoarte contabile pe care se bazează handlerele ANAF.
- `l10n_ro`: localizarea românească de bază (plan de conturi, date fiscale companie).
- `accountant`: modulul Enterprise de contabilitate din care se extind rapoartele.
