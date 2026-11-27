# Generic Partner (localizat la `deltatech_partner_generic/index.md`)

- **Nume Tehnic:** `deltatech_partner_generic`
- **Versiune:** `20.0.2.0.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_partner_generic
- **Cale Locală:** `odoo-addons/deltatech/deltatech_partner_generic`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)
- **Ultima Ingestie:** `2026-11-27`

#### 1. Sumar

Magazinele, punctele de vânzare și importurile înregistrează des vânzări către clienți neidentificați, pe un singur partener „generic”. Acel partener nu trebuie să ajungă pe o factură validată, nu trebuie încasat prin jurnalele greșite și nu trebuie modificat din greșeală, fiindcă apare în toate documentele de vânzare. Modulul declară partenerul generic al fiecărei companii și impune aceste reguli. Restricțiile contabile provin din fostul `deltatech_generic_partner_restriction`, unit cu acest modul și nepublicat pentru 20.0.

#### 2. Funcționalități Cheie

- **Partener generic per companie**: se alege în **Vânzări > Configurare > Setări**, secțiunea **Facturare**, câmpul **Partener generic** (contactul *Generic* creat de modul sau orice alt contact). Setarea doar declară partenerul: nu se completează automat pe comenzi sau facturi. Fără aplicația Vânzări (`sale_management`) setarea nu e vizibilă.
- **Fără factură validată pe partenerul generic**: o factură sau o factură storno de client al cărei client sau adresă de livrare e partenerul generic (ori un contact al lui) nu poate fi validată; eroarea numește factura și cere clientul real. Ciornele rămân permise (POS, eCommerce, importuri). Facturile de furnizor și notele contabile nu sunt afectate.
- **Jurnale de plată restricționate**: jurnalele de bancă și numerar bifate **Restricție generică** (pe formularul jurnalului, plus coloană opțională în listă) nu sunt propuse la plata partenerului generic, nici într-o plată nouă, nici în asistentul **Înregistrare plată** deschis dintr-o factură. Se propun doar jurnale de bancă și numerar, iar jurnalul implicit este mereu unul permis. Filtrul la plata nouă se aplică doar când partenerul plății este chiar partenerul generic, nu un contact al lui.
- **Protecția partenerului generic** (opțională, per companie, bifa **Protejează partenerul generic**): fișa afișează un banner de avertizare, iar modificarea, arhivarea și ștergerea sunt refuzate la salvare. Cei care trebuie să-l modifice primesc grupul **Partener generic: Editor** (administratorii de Setări îl au deja). Scrierile tehnice ale Odoo (chatter, activități, token de portal, geolocalizare) și fluxurile automate cu drepturi elevate rămân permise. Protecția e oprită implicit.
- Modulul nu generează note contabile și nu folosește conturi proprii. Fișa consultant conține fluxul pas cu pas, capturile și mesajele de eroare.

#### 3. Dependențe

- `account`
- `sale`

#### 4. Componente Cheie

**Modele**

- `res.company` (extins): `generic_partner_id` (Many2one către `res.partner`) și `lock_generic_partner` (boolean, activează protecția); `create`/`write`/`unlink` invalidează cache-ul `ormcache` al `res.partner` la schimbarea acestor câmpuri.
- `res.partner` (extins): `generic_partner_locked` (calculat) plus `_get_protected_generic_partner_ids` (cache `@api.ormcache`), `_generic_partners_to_protect` și `_raise_generic_partner_locked`; `write` și `unlink` refuză modificarea partenerului protejat, cu excepția câmpurilor tehnice (`TECHNICAL_FIELDS`).
- `account.move` (extins): `_generic_partner_invoices()` întoarce maparea `{notă: câmp}` a facturilor de client emise pe partenerul generic al propriei companii, iar `_post()` refuză postarea acestora.
- `account.journal` (extins): câmpul boolean `restriction` („Generic Restriction”).
- `account.payment` (extins): `_compute_available_journal_ids` filtrează jurnalele disponibile pentru partenerul generic (exclude cele cu `restriction` bifat, păstrează doar tip bancă/casă), iar `_compute_journal_id` înlocuiește un jurnal implicit nepermis cu unul permis.
- `account.payment.register` (extins, `wizard/account_payment_register.py`): aplică aceeași restricție în asistentul **Înregistrare plată**.
- `res.config.settings` (extins): expune `generic_partner_id` și `lock_generic_partner` (related pe companie) în Setări.

**Vizualizări**

- `res_config_settings_views.xml` — câmpurile din Vânzări > Configurare > Setări, secțiunea Facturare (extinde `sale.res_config_settings_view_form`).
- `res_partner_views.xml` — banner de avertizare pe fișa partenerului când acesta este protejat (extinde `base.view_partner_form`).
- `account_journal_views.xml` — câmpul `restriction` în lista și formularul jurnalului (extinde `account.view_account_journal_tree` / `account.view_account_journal_form`).

**Date**

- `data/data.xml` — creează înregistrarea implicită `partner_generic` (partener „Generic”), cu `noupdate="1"`.

**Migrări**

- `migrations/19.0.2.0.0/pre-migration.py` — preia înregistrările `ir_model_data` de la fostul modul de tranziție `deltatech_generic_partner_restriction` **înainte** ca acesta să fie actualizat, pentru a nu pierde coloana `account_journal.restriction` și bifele existente la clienți (script istoric, păstrat din migrarea 19.0).

#### 5. Conexiuni

- [deltatech_generic_partner_restriction](../deltatech_generic_partner_restriction/index.md): fost modul separat al restricțiilor contabile, unit cu acesta și nepublicat pentru 20.0 (pagina wiki descrie versiunea 19.0).
