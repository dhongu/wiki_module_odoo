# Baza ANAF România (localizat la `l10n_ro_anaf_base/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_base`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_base
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_base`
- **Ultima Ingestie:** 2026-08-20
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
- Clasa de bază `AnafTestCommon` (`tests/common.py`) — reutilizabilă de toate modulele ANAF pentru configurarea automată a mediului de test (companie RO cu adresă fiscală completă, contact ANAF).

#### 3. Dependențe

- `account_reports`
- `l10n_ro`
- `accountant`

#### 4. Componente Cheie

**Modele**

- `l10n_ro_anaf.report.handler.mixin` (`L10nRoAnafReportHandlerMixin`, mixin abstract de `account.report.custom.handler`): logica comună pentru declarant, validări, XSD, export XDP/ZIP.
- `account.move` (extins): adaugă hook-ul `_l10n_ro_posting_guard_errors()` și suprascrie `_post()` pentru a bloca postarea documentelor companiilor RO în funcție de motivele raportate de acest hook.
- `res.company` (extins): câmpurile `l10n_ro_anaf_declaration_contact_id`, `l10n_ro_anaf_declaration_identifier`, `l10n_ro_anaf_export_type`.
- `res.config.settings` (extins): interfață de configurare pentru setările ANAF de mai sus.
- `account.report` (extins): metode helper pentru generarea XML-urilor ANAF și înregistrarea tipului MIME pentru fișierele `.xdp`.
- `account.chart.template` (extins, model abstract): pregătire/postare facturi demo ANAF la instalare.
- Registru Python `anaf_declaration_profile.py` (`register_anaf_profile`, `_ANAF_PROFILES`) — nu este un model Odoo, ci un registru global în memorie prin care modulele Dxxx își înregistrează și selectează versiunile de formulare.

**Vizualizări**

- `views/anaf_menu.xml`: creează meniul principal Contabilitate → Declarații ANAF, sub care modulele individuale de declarații (D300, D390, D394, D398 etc.) își înregistrează sub-meniurile proprii.
- `views/res_config_settings_views.xml`: adaugă opțiunile de configurare ANAF în interfața de setări generale.
- `demo/demo_data.xml`: date de test pentru demonstrații și dezvoltare.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`, `base.automation`, `ir.actions.server`); funcționalitatea este integrată în mixin-uri, hook-uri și extensii de model.*

#### 5. Conexiuni

- `l10n_ro`: localizarea contabilă românească pe care se bazează validările fiscale (CUI, județ, adresă).
- `account_reports`: infrastructura de rapoarte contabile extinsă de mixin-ul de handler ANAF.
- `accountant`: modulul de contabilitate enterprise necesar pentru rapoartele custom-handler.
- Modulele individuale de declarații ANAF (D300, D390, D394, D398 etc.) din suita `l10n_ro_ent` depind funcțional de acest modul de bază, dar nu au încă pagină wiki proprie.
