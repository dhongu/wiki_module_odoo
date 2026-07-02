# Romania - Inventariere și Înregistrări Contabile (FR-18) (localizat la `l10n_ro_inventory_closing/index.md`)

- **Nume Tehnic:** `l10n_ro_inventory_closing`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_inventory_closing
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_inventory_closing`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

## 1. Sumar

Modul pentru înregistrările contabile ale inventarierii conform legislației românești: OMFP 1802/2014 (tratamentul contabil al diferențelor de inventar) și OMFP 2861/2009 (format Proces-Verbal de Inventariere). Generează automat notele contabile pentru cele patru tipuri de diferențe (plus, minus neimputabil, minus imputabil cu TVA, casare) și produce rapoartele PDF aferente (PV, decizie de imputare, decizie de casare).

## 2. Funcționalități Cheie

- **Generare automată note contabile** după validarea inventarului.
- **Suport pentru 4 tipuri de diferențe:** plus inventar (D 3xx / C 607), minus neimputabil (D 607 / C 3xx), minus imputabil (D 607/C 3xx + D 4282/C 7588 + D 635/C 4427 TVA), casare (D 6583 / C 3xx).
- **Calcul automat TVA** la minusurile imputabile (cotă configurabilă, implicit 21%).
- **Stare contabilă inventar:** Necontabilizat → Parțial → Complet.
- **Configurare conturi pe companie** (607, 4282, 7588, 4427, 635, 6583).
- **Rapoarte PDF:** Proces-Verbal Inventariere (OMFP 2861/2009), Decizie de Imputare, Decizie de Casare.

## 3. Dependențe

- `deltatech_stock_inventory`
- `stock_account`
- `l10n_ro`
- `account`

## 4. Componente Cheie

### Modele

- `stock.inventory`: extins cu starea contabilă, notele generate, comisia (președinte, membri), gestionarul și datele PV.
- `stock.inventory.line`: extins cu tipul diferenței, valoarea, persoana responsabilă, valorile de imputare + TVA și marcajul de contabilizare.

### Vizualizări / Date

- `views/stock_inventory_views.xml`: câmpurile RO pe inventar și linii.
- `views/res_config_settings_views.xml`: configurarea conturilor pe companie.
- `wizard/inventory_accounting_wizard_views.xml`: wizardul de generare a notelor contabile.
- `report/report_inventory_pv.xml`, `report/report_inventory_imputare.xml`, `report/report_inventory_casare.xml`: rapoartele PDF.

### Acțiuni Automate / Acțiuni Server

*Notele contabile se generează prin wizard, după validarea inventarului.*

## 5. Conexiuni

- `[[l10n_ro_inventory_items]]`
- `[[l10n_ro_fixed_assets]]`
