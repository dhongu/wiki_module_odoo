# Deltatech Generic Partner (localizat la `deltatech_partner_generic/index.md`)

- **Nume Tehnic:** `deltatech_partner_generic`
- **Versiune:** `19.0.2.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_partner_generic
- **Cale Locală:** `odoo-addons/deltatech/deltatech_partner_generic`
- **Ultima Ingestie:** `2026-08-31`

#### 1. Sumar

Modulul oferă o modalitate eficientă de a gestiona tranzacțiile cu parteneri generici sau anonimi, permițând definirea unui „Partener Generic” în configurarea Odoo. Acest partener implicit este folosit ca opțiune de rezervă atunci când un partener specific nu este necesar, simplificând introducerea datelor pentru companiile care lucrează cu mulți clienți ocazionali sau anonimi. Din versiunea `19.0.2.0.0` modulul conține și **restricțiile contabile** aferente partenerului generic, preluate din `deltatech_generic_partner_restriction`, plus **protecția** partenerului împotriva modificărilor accidentale.

#### 2. Funcționalități Cheie

- Definirea unui „Partener Generic” implicit, folosit atunci când nu este necesar un partener specific.
- Gestionarea automată a selectării acestui partener în diverse fluxuri de business, precum vânzările și facturarea.
- Simplificarea introducerii datelor pentru companiile care lucrează cu mulți clienți ocazionali sau anonimi.
- Integrare completă cu setările standard de contabilitate și vânzări din Odoo.
- **Blocarea validării facturilor de client** emise pe partenerul generic: postarea e refuzată cu eroare explicită, care numește câmpul vinovat. Se verifică atât `partner_id`, cât și `partner_shipping_id`. Ciornele rămân permise, deci fluxurile care trec prin partenerul generic (POS, eCommerce, importuri) continuă să funcționeze. Facturile de furnizor și notele contabile nu sunt afectate.
- **Restricționarea jurnalelor la înregistrarea plăților** pentru partenerul generic, prin bifa „Generic Restriction” de pe jurnal.
- **Protecția partenerului generic** (opțională, per companie): odată activată, partenerul nu mai poate fi redenumit, arhivat sau șters.

#### 3. Dependențe

- `account`
- `sale`

#### 4. Componente Cheie

**Modele**

- `res.company` (extins): `generic_partner_id` (Many2one către `res.partner`) și `lock_generic_partner` (boolean, activează protecția); `create`/`write`/`unlink` supravegheate.
- `res.partner` (extins): `generic_partner_locked` (calculat) plus `_get_protected_generic_partner_ids`, `_generic_partners_to_protect` și `_raise_generic_partner_locked`; `write` și `unlink` refuză modificarea partenerului protejat.
- `account.move` (extins): `_generic_partner_invoices()` întoarce maparea `{notă: câmp}` a facturilor de client emise pe partenerul generic (verifică `partner_id` și `partner_shipping_id`, inclusiv prin `commercial_partner_id`), iar `_post()` refuză postarea acestora.
- `account.journal` (extins): câmpul boolean `restriction` („Generic Restriction”).
- `account.payment` (extins): filtrează jurnalele disponibile pentru partenerul generic.
- `res.config.settings` (extins): expune configurarea în Setări.

**Vizualizări**

- `res_config_settings_views.xml` — secțiunea „Partener Generic” din Setări > Setări generale > Vânzări.
- `res_partner_views.xml` — indicarea partenerului protejat pe fișa partenerului.
- `account_journal_views.xml` — câmpul `restriction` în lista și formularul jurnalului.

**Migrări**

- `migrations/19.0.2.0.0/pre-migration.py` — preia înregistrările `ir_model_data` de la modulul de tranziție **înainte** ca acesta să fie actualizat. Fără acest pas, Odoo ar curăța înregistrările nemaideclarate și ar șterge coloana `account_journal.restriction` împreună cu bifele puse de client.

#### 5. Conexiuni

- [deltatech_generic_partner_restriction](../deltatech_generic_partner_restriction/index.md): modul de tranziție, gol, care depinde de acesta; bazele care îl au instalat preiau restricțiile la actualizare.
