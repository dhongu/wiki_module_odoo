# Deltatech Generic Partner (localizat la `deltatech_partner_generic/index.md`)

- **Nume Tehnic:** `deltatech_partner_generic`
- **Versiune:** `20.0.2.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_partner_generic
- **Cale Locală:** `odoo-addons/deltatech/deltatech_partner_generic`
- **Ultima Ingestie:** `2026-09-27`

#### 1. Sumar

Modulul oferă o modalitate eficientă de a gestiona tranzacțiile cu parteneri generici sau anonimi, permițând definirea unui „Partener Generic” în configurarea Odoo. Acest partener implicit este folosit ca opțiune de rezervă atunci când un partener specific nu este necesar, simplificând introducerea datelor pentru companiile care lucrează cu mulți clienți ocazionali sau anonimi. Modulul include și **restricțiile contabile** aferente partenerului generic (preluate din fostul `deltatech_generic_partner_restriction`), plus **protecția** partenerului împotriva modificărilor accidentale.

#### 2. Funcționalități Cheie

- Definirea unui „Partener Generic” implicit, folosit atunci când nu este necesar un partener specific (Setări > Setări generale > Vânzări, secțiunea „Generic partner”).
- Gestionarea automată a selectării acestui partener în diverse fluxuri de business, precum vânzările și facturarea.
- Simplificarea introducerii datelor pentru companiile care lucrează cu mulți clienți ocazionali sau anonimi.
- Integrare completă cu setările standard de contabilitate și vânzări din Odoo.
- **Blocarea validării facturilor de client** emise pe partenerul generic: postarea e refuzată cu eroare explicită, care numește câmpul vinovat. Se verifică atât `partner_id`, cât și `partner_shipping_id` (inclusiv prin `commercial_partner_id`). Ciornele rămân permise, deci fluxurile care trec prin partenerul generic (POS, eCommerce, importuri) continuă să funcționeze. Facturile de furnizor și notele contabile nu sunt afectate.
- **Restricționarea jurnalelor la înregistrarea plăților** pentru partenerul generic, prin bifa „Generic Restriction” de pe jurnal (doar jurnale de tip bancă/casă rămân propuse).
- **Protecția partenerului generic** (opțională, per companie, bifa „Protect Generic Partner”): odată activată, partenerul nu mai poate fi redenumit, modificat sau șters; fișa partenerului afișează un banner de avertizare. Scrierile tehnice ale Odoo (chatter, activități, semnătură portal, geolocalizare) și fluxurile automate rulate cu drepturi elevate nu sunt afectate. Utilizatorii cărora li se atribuie grupul „Generic Partner: Editor” pot modifica totuși partenerul; administratorii de Setări au deja acest grup implicit.

#### 3. Dependențe

- `account`
- `sale`

#### 4. Componente Cheie

**Modele**

- `res.company` (extins): `generic_partner_id` (Many2one către `res.partner`) și `lock_generic_partner` (boolean, activează protecția); `create`/`write`/`unlink` invalidează cache-ul `ormcache` al `res.partner` la schimbarea acestor câmpuri.
- `res.partner` (extins): `generic_partner_locked` (calculat) plus `_get_protected_generic_partner_ids` (cache `@api.ormcache`), `_generic_partners_to_protect` și `_raise_generic_partner_locked`; `write` și `unlink` refuză modificarea partenerului protejat, cu excepția câmpurilor tehnice (`TECHNICAL_FIELDS`).
- `account.move` (extins): `_generic_partner_invoices()` întoarce maparea `{notă: câmp}` a facturilor de client emise pe partenerul generic al propriei companii, iar `_post()` refuză postarea acestora.
- `account.journal` (extins): câmpul boolean `restriction` („Generic Restriction”).
- `account.payment` (extins): `_compute_available_journal_ids` filtrează jurnalele disponibile pentru partenerul generic (exclude cele cu `restriction` bifat, păstrează doar tip bancă/casă).
- `res.config.settings` (extins): expune `generic_partner_id` și `lock_generic_partner` (related pe companie) în Setări.

**Vizualizări**

- `res_config_settings_views.xml` — secțiunea „Generic partner” din Setări > Setări generale > Vânzări (extinde `sale.res_config_settings_view_form`).
- `res_partner_views.xml` — banner de avertizare pe fișa partenerului când acesta este protejat (extinde `base.view_partner_form`).
- `account_journal_views.xml` — câmpul `restriction` în lista și formularul jurnalului (extinde `account.view_account_journal_tree` / `account.view_account_journal_form`).

**Date**

- `data/data.xml` — creează înregistrarea implicită `partner_generic` (partener „Generic”), cu `noupdate="1"`.

**Migrări**

- `migrations/19.0.2.0.0/pre-migration.py` — preia înregistrările `ir_model_data` de la fostul modul de tranziție `deltatech_generic_partner_restriction` **înainte** ca acesta să fie actualizat, pentru a nu pierde coloana `account_journal.restriction` și bifele existente la clienți (script istoric, păstrat din migrarea 19.0).

#### 5. Conexiuni

- [deltatech_generic_partner_restriction](../deltatech_generic_partner_restriction/index.md): fost modul de tranziție (gol, depindea de acesta) prin care bazele mai vechi preluau restricțiile contabile la actualizare; nu are pagină wiki proprie pe 20.0.
