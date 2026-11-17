# Deltatech Generic Partner (localizat la `deltatech_partner_generic/index.md`)

- **Nume Tehnic:** `deltatech_partner_generic`
- **Versiune:** `19.0.2.0.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_partner_generic
- **Cale Locală:** `odoo-addons/deltatech/deltatech_partner_generic`
- **Ultima Ingestie:** `2026-11-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Magazinele, punctele de vânzare și importurile înregistrează adesea vânzări către clienți neidentificați, sub un singur partener generic. Acesta nu trebuie să ajungă pe o factură reală, nu trebuie să încaseze prin jurnale nepotrivite și nu trebuie modificat din greșeală, fiindcă e accesibil din toate documentele de vânzare. Modulul declară partenerul generic al fiecărei companii și impune aceste reguli. Restricțiile contabile provin din modulul `deltatech_generic_partner_restriction`, rămas acum doar ca modul de tranziție.

#### 2. Funcționalități Cheie

- **Partener generic per companie**: se setează în **Contabilitate > Configurare > Setări**, secțiunea **Facturi clienți**, câmpul **Generic Partner** (disponibil și fără aplicația Vânzări). Modulul creează un contact de companie „Generic”, dar poate fi ales orice alt contact. Setarea doar declară partenerul: nu îl completează automat pe comenzi sau facturi.
- **Blocarea validării facturilor de client** emise pe partenerul generic (sau pe un contact al lui), atât la client, cât și la adresa de livrare: eroarea numește factura și cere clientul real. Ciornele rămân permise, deci fluxurile prin partenerul generic (POS, eCommerce, importuri) funcționează. Facturile de furnizor și notele contabile nu sunt afectate.
- **Jurnale de plată restricționate**: jurnalele de bancă și numerar bifate **Generic Restriction** (pe formularul jurnalului și ca coloană opțională în listă) nu sunt propuse la plățile partenerului generic, nici în plata nouă, nici în wizardul **Înregistrare plată** deschis dintr-o factură. Se propun doar jurnale de bancă și numerar, iar jurnalul implicit este mereu unul permis.
- **Protecția partenerului generic** (opțională, bifa **Protect Generic Partner** în aceeași setare, dezactivată implicit): fișa afișează un banner de avertizare, iar orice modificare, arhivare sau ștergere e refuzată la salvare. Utilizatorii care trebuie să îl modifice primesc grupul **Generic Partner: Editor**; administratorii de Setări îl au deja. Scrierile făcute de Odoo (chatter, activități, token-uri de portal, geolocație) și fluxurile automate cu drepturi ridicate rămân permise.
- Pașii detaliați sunt în fișa consultant.

#### 3. Dependențe

- `account`
- `sale`

#### 4. Componente Cheie

**Modele**

- `res.company` (extins): `generic_partner_id` (Many2one către `res.partner`) și `lock_generic_partner` (boolean, activează protecția); `create`/`write`/`unlink` supravegheate.
- `res.partner` (extins): `generic_partner_locked` (calculat) plus `_get_protected_generic_partner_ids`, `_generic_partners_to_protect` și `_raise_generic_partner_locked`; `write` și `unlink` refuză modificarea partenerului protejat.
- `account.move` (extins): `_generic_partner_invoices()` întoarce maparea `{notă: câmp}` a facturilor de client emise pe partenerul generic (verifică `partner_id` și `partner_shipping_id`, inclusiv prin `commercial_partner_id`), iar `_post()` refuză postarea acestora.
- `account.journal` (extins): câmpul boolean `restriction` („Generic Restriction”).
- `account.payment` (extins): filtrează jurnalele disponibile și propune un jurnal implicit permis pentru partenerul generic.
- `account.payment.register` (wizard, extins): aceeași restricție de jurnale în wizardul Înregistrare plată.
- `res.config.settings` (extins): expune `generic_partner_id` și `lock_generic_partner` în Setări.
- Grup `group_generic_partner_editor` („Generic Partner: Editor”): permite modificarea partenerului protejat; dat implicit administratorilor de Setări.

**Vizualizări**

- `res_config_settings_views.xml` — câmpurile „Generic Partner” și „Protect Generic Partner” în Contabilitate > Setări, secțiunea Facturi clienți.
- `res_partner_views.xml` — bannerul de avertizare pentru partenerul protejat și indicarea partenerului protejat pe fișa partenerului.
- `account_journal_views.xml` — câmpul `restriction` în lista și formularul jurnalului.

**Migrări**

- `migrations/19.0.2.0.0/pre-migration.py` — preia înregistrările `ir_model_data` de la modulul de tranziție **înainte** ca acesta să fie actualizat. Fără acest pas, Odoo ar curăța înregistrările nemaideclarate și ar șterge coloana `account_journal.restriction` împreună cu bifele puse de client.

#### 5. Conexiuni

- [deltatech_generic_partner_restriction](../deltatech_generic_partner_restriction/index.md): modul de tranziție, gol, care depinde de acesta; bazele care îl au instalat preiau restricțiile la actualizare.
