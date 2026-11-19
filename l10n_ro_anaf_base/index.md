# Romania - Bază ANAF (localizat la `l10n_ro_anaf_base/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_base`
- **Versiune:** `19.0.1.5.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_base
- **Cale Locală:** odoo-addons/l10n_ro_ent/l10n_ro_anaf_base
- **Ultima Ingestie:** `2026-11-19`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul este infrastructura comună (de bază, ascunsă) pentru toate declarațiile fiscale ANAF din suita `l10n_ro_ent`. Centralizează logica de generare și export a declarațiilor către ANAF (Soft A — Adobe XDP și Soft J — XML), eliminând duplicarea codului între modulele individuale D300, D390, D394, D398 etc. Nu se instalează manual: vine automat ca dependență a oricărui modul de declarație ANAF.

#### 2. Funcționalități Cheie

- **Mixin pentru handlere (`L10nRoAnafReportHandlerMixin`)** — date companie (CUI, CAEN, județ cod ANAF 01–52, reprezentant legal), date declarant (nume, prenume, funcție, identificator fiscal/CNP, email, telefon, adresă) cu fallback pe userul curent.
- Validare companie înainte de export: VAT, adresă fiscală, județ, CAEN, contact.
- Validare parteneri: VAT obligatoriu pentru partenerii incluși în declarații; prefixul codului de TVA ține cont de VIES (ex. Grecia, `GR` → `EL`).
- Validare XML față de scheme XSD oficiale ANAF.
- Generare nume fișier conform convențiilor ANAF.
- Export XDP (Adobe) direct, împachetat ZIP cu formularul PDF sau scris direct în formularul PDF ANAF; helper-e pentru butoanele de export XML și XDP din interfața rapoartelor.
- Registru de profile de declarații (funcție `register_anaf_profile` / `_ANAF_PROFILES`) — mecanism centralizat de înregistrare și selecție a versiunilor de formulare ANAF, cu suport pentru perioade istorice.
- **Cod CAEN al companiei** — câmpul `l10n_ro_anaf_caen_code` pe companie (4 cifre), completat pe formularul companiei sau în Setări → Contabilitate → Declarații ANAF. Nu e modificat de căutarea ANAF a partenerilor, deci o firmă trecută pe CAEN Rev.3 își poate păstra în declarații codul acceptat de schema ANAF. Exportul refuză un cod care nu are exact 4 cifre sau e `0000` (`is_valid_caen_code()`), fără fallback tăcut.
- **Convenția „Nume Prenume"** pentru numele de persoane — `_split_contact_name` consideră primul cuvânt nume de familie, restul prenume (ex. `Popescu Ion` → Popescu / Ion); se aplică persoanei responsabile cu declarațiile și salariaților din D112. Ordinea inversă nu e respinsă de ANAF, dar apare inversată pe declarația depusă.
- **Cod produs pentru taxare inversă (art. 331)** — `product.product._l10n_ro_reverse_charge_code()` calculează codul din nomenclatorul ANAF într-un singur loc (categoriile 22–31, prefixul NC al cerealelor sau primele 8 cifre ale codului NC), folosit de D394 și D300.
- Clasa de bază `AnafTestCommon` (`tests/common.py`) — reutilizabilă de toate modulele ANAF pentru configurarea mediului de test.

Configurare (Setări → Contabilitate → Declarații ANAF, partajată de toate modulele de declarații):

- **Persoana responsabilă** — contactul care apare ca declarant în XML (`<Declarant>`/`<Preparer>`); numele se scrie „Nume Prenume".
- **Declaration Identifier** — codul fiscal/CNP al declarantului; dacă e gol, se preia din VAT/CNP-ul persoanei responsabile.
- **Tip export** — `XDP direct` (descărcare directă a fișierului XDP), `Arhivă ZIP` (XDP + PDF) sau `PDF cu datele incluse` (implicit, formularul PDF ANAF completat prin actualizare incrementală, care păstrează extensiile Adobe Reader). Opțiunea PDF cere `pypdf` 5.0+ pe server; fără el exportul revine la arhiva ZIP, iar setările afișează un avertisment.
- Din același ecran se pot activa rapid modulele D300, D390, D394 și D398.

#### 3. Dependențe

- `account_reports`
- `l10n_ro`
- `accountant`
- `l10n_ro_move_guard`

#### 4. Componente Cheie

**Modele**

- `l10n_ro_anaf.report.handler.mixin` (`L10nRoAnafReportHandlerMixin`, mixin abstract): logica comună pentru declarant, validări (inclusiv `_validate_anaf_export_company(require_caen=...)`), XSD, export XDP/ZIP/PDF, `_get_anaf_company_data`, `_split_contact_name`.
- `res.company` (extins): `l10n_ro_anaf_caen_code`, `l10n_ro_anaf_declaration_contact_id`, `l10n_ro_anaf_declaration_identifier`, `l10n_ro_anaf_export_type` (implicit `pdf`).
- `res.config.settings` (extins): interfață de configurare pentru câmpurile de mai sus, plus togglurile de instalare `module_l10n_ro_anaf_d300/d390/d394/d398`.
- `account.report` (extins): metode helper pentru generarea XML-urilor ANAF și înregistrarea tipului MIME `application/vnd.adobe.xdp+xml` pentru fișierele `.xdp`.
- `product.product` (extins): `_l10n_ro_nc_code()` (codul NC din primul câmp completat: `l10n_ro_nc_code`, `l10n_ro_nc8_code`, codul Intrastat, `hs_code`) și `_l10n_ro_reverse_charge_code()`.
- `account.chart.template` (extins, model abstract): pregătire/postare facturi demo ANAF la instalare.
- Registru Python `anaf_declaration_profile.py` (`register_anaf_profile`, `_ANAF_PROFILES`) — nu este un model Odoo, ci un registru global în memorie prin care modulele Dxxx își înregistrează și selectează versiunile de formulare.

**Vizualizări**

- `views/anaf_menu.xml`: creează meniul principal Contabilitate → Declarații ANAF, sub care modulele individuale de declarații își înregistrează sub-meniurile proprii.
- `res_config_settings_view_form`: opțiunile de configurare ANAF (persoană responsabilă, identificator, tip export, CAEN) în Setări → Contabilitate.
- `view_company_form`: câmpul CAEN pe formularul companiei.
- `demo/demo_data.xml`: date de test pentru demonstrații și dezvoltare.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`, `base.automation`, `ir.actions.server`); funcționalitatea este integrată în mixin-uri, hook-uri și extensii de model.*

#### 5. Conexiuni

- `l10n_ro_move_guard`: găzduiește garda comună de postare (`_l10n_ro_posting_guard_errors()`), mutată aici din acest modul; la update se instalează automat, iar comportamentul rămâne același.
- `l10n_ro`: localizarea contabilă românească pe care se bazează validările fiscale (CUI, județ, adresă).
- `account_reports` și `accountant`: infrastructura de rapoarte contabile (Enterprise) extinsă de mixin-ul de handler ANAF.
- `l10n_ro_config` (OCA, l10n-romania-oca): definește câmpul `l10n_ro_caen_code` cu default `"0000"`; modulul de bază nu mai definește acest câmp pe partener și folosește propriul `l10n_ro_anaf_caen_code` pe companie.
- Modulele individuale de declarații ANAF din suita `l10n_ro_ent` depind funcțional de acest modul de bază: [l10n_ro_anaf_d100](../l10n_ro_anaf_d100/index.md), [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md), [l10n_ro_anaf_d390](../l10n_ro_anaf_d390/index.md), [l10n_ro_anaf_d394](../l10n_ro_anaf_d394/index.md), [l10n_ro_anaf_d398](../l10n_ro_anaf_d398/index.md), [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md) ș.a.
