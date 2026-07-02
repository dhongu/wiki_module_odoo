# Grup Fiscal TVA Consolidat România (localizat la `l10n_ro_vat_group/index.md`)

- **Nume Tehnic:** `l10n_ro_vat_group`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_vat_group
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_vat_group`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

## 1. Sumar

Acest modul gestionează grupurile fiscale TVA conform art. 269² Cod Fiscal și OPANAF 2731/2016. Permite definirea unui grup de companii cu relații de control (deținere >50%) ca un singur subiect fiscal TVA, cu CUI unic, marcarea automată a tranzacțiilor intra-grup (excluse din baza TVA) și generarea unui raport TVA consolidat per membru, depus de membrul raportor printr-un singur D300.

## 2. Funcționalități Cheie

- **Model grup TVA (`l10n.ro.vat.group`):** configurare companii membre, membru raportor și CUI unic (`RO_GRP_XXXXXX`), cu state machine `În constituire → Activ → Dizolvat`.
- **Setare automată la activare:** câmpul „Grup fiscal TVA" se completează pe toate companiile membre.
- **Marcare automată tranzacții intra-grup:** la postarea facturilor către o companie membră, acestea sunt marcate „Tranzacție intra-grup TVA", cu banner de avertizare și marcare retroactivă disponibilă.
- **Raport TVA consolidat (wizard):** TVA colectată/deductibilă, intra-grup colectat/deductibil și TVA net per companie, plus total consolidat fără intra-grup.
- **Blocare perioadă:** setează `tax_lock_date` sincronizat pe toate companiile membre.

## 3. Dependențe

- `account`
- `l10n_ro`

## 4. Componente Cheie

Conform `readme/DESCRIPTION.md`:

### Modele

- `l10n.ro.vat.group`: Grupul fiscal TVA, cu companii membre, membru raportor, CUI unic și state machine.
- `account.move`: Extins cu marcarea tranzacțiilor intra-grup TVA.

### Vizualizări / Date

- `views/l10n_ro_vat_group_views.xml`: Formularul grupului fiscal TVA.
- `views/account_move_views.xml`: Bannerul și câmpul de marcare intra-grup pe factură.
- `wizard/l10n_ro_vat_group_report_wizard_views.xml`: Wizardul raportului TVA consolidat.

### Acțiuni Automate / Acțiuni Server

*Nu sunt definite acțiuni automate; marcarea intra-grup se aplică la postarea facturilor.*

## 5. Conexiuni

- `l10n_ro_vat_regularization`
- `l10n_ro_vat_deductibility`
- `l10n_ro_vat_refund`
