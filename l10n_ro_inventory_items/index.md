# Romania - Obiecte de Inventar (303/603/8035) (localizat la `l10n_ro_inventory_items/index.md`)

- **Nume Tehnic:** `l10n_ro_inventory_items`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_inventory_items
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_inventory_items`
- **Ultima Ingestie:** 2026-06-01

## 1. Sumar

Implementează fluxul complet de gestiune a obiectelor de inventar conform OMFP 1802/2014 — bunuri sub pragul mijloacelor fixe (sub 2.500 RON conform HG 276/2013). Acoperă recepția (Dr 303 = Cr 401), darea în folosință (Dr 603 = Cr 303), evidența extracontabilă opțională pe contul 8035 și scoaterea din gestiune, cu fișă de obiect de inventar, wizard-uri batch și rapoarte PDF.

## 2. Funcționalități Cheie

- **Fișa OI (`l10n.ro.inventory.item`):** nr. inventar auto-generat `OI/AAAA/NNNN`, responsabil, locație/departament cu tracking, stare fizică (Bună/Deteriorată/Casată) și stare flux (Recepționat → Dat în Folosință → Scos din Gestiune).
- **Dare în folosință (`action_use()`):** verificare stoc 303, picking intern către locație virtuală, generare automată `603 = 303` și, opțional, notă extracontabilă `Dr 8035 = Cr 8035C`.
- **Scoatere din gestiune (`action_dispose()`):** stornare notă 8035, motiv, dată, stare fizică și PV PDF cu comisie.
- **Wizard-uri batch** pentru dare în folosință (cu Bon PDF) și scoatere din gestiune (cu PV PDF).
- **Cont extracontabil 8035:** la instalare se creează contul 8035C (off_balance) și jurnalul „Evidență Extracontabilă" (EXTR), cu toggle pe companie; verificare sold prin `_check_8035_balance()`.
- **Rapoarte PDF:** Bon de Dare în Folosință și PV de Scoatere din Gestiune.

## 3. Dependențe

- `stock_account`
- `l10n_ro`

## 4. Componente Cheie

### Modele

- `l10n.ro.inventory.item`: fișa obiectului de inventar cu numerele de inventar, starea fizică, starea de flux și metodele `action_use()` / `action_dispose()`.
- `product.template`: extins cu marcajul „Obiect de Inventar (RO)".
- `res.company`: extins cu toggle-ul `l10n_ro_use_8035_account_move` și conturile aferente.

### Vizualizări / Date

- `views/l10n_ro_inventory_item_views.xml`, `views/product_template_views.xml`, `views/res_company_views.xml`, `views/menus.xml`: interfețele OI, produs, companie și meniul.
- `wizard/inventory_item_use_wizard_views.xml`, `wizard/inventory_item_dispose_wizard_views.xml`: wizard-urile batch.
- `report/report_bon_dare_in_folosinta.xml`, `report/report_pv_scoatere_gestiune.xml`: rapoartele PDF.
- `data/ir_sequence_data.xml`, `data/stock_location_data.xml`: secvența OI și locația virtuală.

### Acțiuni Automate / Acțiuni Server

- `post_init_hook`: creează contul 8035C, jurnalul „Evidență Extracontabilă" (EXTR) și locația virtuală pentru companiile RO.

## 5. Conexiuni

- `[[l10n_ro_fixed_assets]]`
- `[[l10n_ro_inventory_closing]]`
