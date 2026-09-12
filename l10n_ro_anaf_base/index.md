# Romania - Bază ANAF (localizat la `l10n_ro_anaf_base/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_base`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_base
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_base`
- **Ultima Ingestie:** 2026-09-12
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul este infrastructura comună (de bază, ascunsă) pentru toate declarațiile fiscale ANAF din suita `l10n_ro_ent`. Centralizează logica de generare și export a declarațiilor către ANAF (Soft A — Adobe XDP și Soft J — XML), eliminând duplicarea codului între modulele individuale D300, D390, D394, D398 etc.

#### 2. Funcționalități Cheie

- **Mixin pentru handlere (`L10nRoAnafReportHandlerMixin`)** — date companie (CUI, CAEN, județ cod ANAF 01–52, reprezentant legal), date declarant (nume, prenume, funcție, identificator fiscal/CNP, email, telefon, adresă) cu fallback pe userul curent.
- Validare companie înainte de export: VAT, adresă fiscală, județ, CAEN, contact.
- Validare parteneri: VAT obligatoriu pentru partenerii incluși în declarații.
- Validare XML față de scheme XSD oficiale ANAF.
- Generare nume fișier conform convențiilor ANAF.
- Export XDP (Adobe) cu înglobare PDF și împachetare ZIP.
- Helper-e pentru adăugarea butoanelor de export XML și XDP în interfața rapoartelor.
- Registru de profile de declarații (funcție `register_anaf_profile` / `_ANAF_PROFILES`) — mecanism centralizat de înregistrare și selecție a versiunilor de formulare ANAF, cu suport pentru perioade istorice.
- Extensii pe `res.company` și `res.config.settings` — persoană responsabilă declarații, identificator declarant, tip export implicit, instalare module ANAF.
- Extensie `account.report` — înregistrare tip MIME `application/vnd.adobe.xdp+xml` pentru fișierele `.xdp`.
- **Gardă de postare pentru companii RO (`account.move._l10n_ro_posting_guard_errors`)** — hook extensibil, opt-in, prin care alte module de localizare pot bloca postarea unui document (de ex. parteneri inactivi la ANAF) fără a schimba comportamentul implicit al instalărilor existente.
- **Codul CAEN al companiei, definit acum aici (nou în 19.0.1.2.0)** — câmpul `l10n_ro_caen_code`, pe partener, cu oglindă pe `res.company` (editabil) și expus în setările contabile. E obligatoriu și enumerat strict în schemele ANAF (D100, D101, D112 și celelalte), dar anterior venea doar din `l10n_ro_config` (l10n-romania-oca), de care suita de declarații nu depinde — pe o instalare fără acel modul, orice declarație se genera cu CAEN gol. Când ambele module sunt instalate, definițiile de câmp fuzionează și rămâne un singur câmp.
- **Fără fallback tăcut pe `"0000"`** — spre deosebire de `l10n_ro_config`, câmpul CAEN nu are valoare implicită, pentru că `"0000"` nu există în nomenclatorul ANAF și ar produce un XML respins de schemă cu un mesaj criptic. `_get_anaf_company_data` întoarce valoarea reală a companiei, iar `_validate_anaf_export_company(require_caen=True)` prinde atât câmpul gol, cât și placeholderul `"0000"` lăsat de `l10n_ro_config`, cu un mesaj acționabil.
- Clasa de bază `AnafTestCommon` (`tests/common.py`) — reutilizabilă de toate modulele ANAF pentru configurarea automată a mediului de test (companie RO cu adresă fiscală completă, contact ANAF).

Configurare (Setări → Contabilitate → Declarații ANAF, partajată de toate modulele de declarații):

- **Persoana responsabilă** — contactul care apare ca declarant în XML (`<Declarant>`/`<Preparer>`).
- **Declaration Identifier** — codul fiscal/CNP al declarantului; dacă e gol, se preia din VAT/CNP-ul persoanei responsabile.
- **Tip export** — `XDP direct` (descărcare directă a fișierului, pentru upload pe portalul ANAF) sau `Arhivă ZIP` (XDP + PDF, implicit).
- Din același ecran se pot activa rapid modulele individuale D300, D390, D394 și D398.

#### 3. Dependențe

- `account_reports`
- `l10n_ro`
- `accountant`

#### 4. Componente Cheie

**Modele**

- `l10n_ro_anaf.report.handler.mixin` (`L10nRoAnafReportHandlerMixin`, mixin abstract de `account.report.custom.handler`): logica comună pentru declarant, validări (inclusiv `_validate_anaf_export_company(require_caen=...)`), XSD, export XDP/ZIP, `_get_anaf_company_data`.
- `account.move` (extins): adaugă hook-ul `_l10n_ro_posting_guard_errors()` și suprascrie `_post()` pentru a bloca postarea documentelor companiilor RO în funcție de motivele raportate de acest hook.
- `res.partner` (extins): câmpul `l10n_ro_caen_code` (codul CAEN), fără valoare implicită — deliberat, spre deosebire de `l10n_ro_config`.
- `res.company` (extins): `l10n_ro_caen_code` (related, editabil, pe `partner_id`), `l10n_ro_anaf_declaration_contact_id`, `l10n_ro_anaf_declaration_identifier`, `l10n_ro_anaf_export_type`.
- `res.config.settings` (extins): interfață de configurare pentru toate câmpurile de mai sus, plus togglurile de instalare `module_l10n_ro_anaf_d300/d390/d394/d398`.
- `account.report` (extins): metode helper pentru generarea XML-urilor ANAF și înregistrarea tipului MIME pentru fișierele `.xdp`.
- `account.chart.template` (extins, model abstract): pregătire/postare facturi demo ANAF la instalare.
- Registru Python `anaf_declaration_profile.py` (`register_anaf_profile`, `_ANAF_PROFILES`) — nu este un model Odoo, ci un registru global în memorie prin care modulele Dxxx își înregistrează și selectează versiunile de formulare.

**Vizualizări**

- `views/anaf_menu.xml`: creează meniul principal Contabilitate → Declarații ANAF, sub care modulele individuale de declarații (D300, D390, D394, D398 etc.) își înregistrează sub-meniurile proprii.
- `views/res_config_settings_views.xml`: adaugă opțiunile de configurare ANAF (inclusiv CAEN) în interfața de setări generale.
- `demo/demo_data.xml`: date de test pentru demonstrații și dezvoltare.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`, `base.automation`, `ir.actions.server`); funcționalitatea este integrată în mixin-uri, hook-uri și extensii de model.*

#### 5. Conexiuni

- `l10n_ro`: localizarea contabilă românească pe care se bazează validările fiscale (CUI, județ, adresă).
- `account_reports`: infrastructura de rapoarte contabile extinsă de mixin-ul de handler ANAF.
- `accountant`: modulul de contabilitate enterprise necesar pentru rapoartele custom-handler.
- `l10n_ro_config` (OCA, l10n-romania-oca): definește câmpul `l10n_ro_caen_code` cu aceeași denumire și cu un default `"0000"`; când e instalat împreună cu acest modul, definițiile de câmp fuzionează, dar `l10n_ro_anaf_base` tratează `"0000"` ca valoare invalidă la validare.
- Modulele individuale de declarații ANAF (D300, D390, D394, D398 etc.) din suita `l10n_ro_ent` depind funcțional de acest modul de bază, dar nu au încă pagină wiki proprie.
