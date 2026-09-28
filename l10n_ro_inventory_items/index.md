# Romania - Obiecte de inventar (303/603/8035) (localizat la `l10n_ro_inventory_items/index.md`)

- **Nume Tehnic:** `l10n_ro_inventory_items`
- **Versiune:** `19.0.2.3.0`
- **Cale:** `https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_inventory_items`
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_inventory_items`
- **Ultima Ingestie:** `2026-09-21`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Implementează fluxul complet de gestiune a obiectelor de inventar conform OMFP 1802/2014 — bunuri sub pragul mijloacelor fixe (sub 2.500 RON conform HG 276/2013). Acoperă recepția (Dr 303 = Cr 401), darea în folosință (Dr 603 = Cr 303), evidența extracontabilă opțională pe contul 8035 și scoaterea din gestiune, cu fișă de obiect de inventar, wizard-uri batch și rapoarte PDF. Fișa OI se creează automat la recepția produselor marcate „Obiect de Inventar (RO)", iar nota de dare în folosință e generată de modul și atunci când valorizarea de stoc nu o produce.

#### 2. Funcționalități Cheie

- **Fișa OI (`l10n.ro.inventory.item`):** nr. inventar auto-generat `OI/AAAA/NNNN`, responsabil, locație/departament cu tracking, stare fizică (Bună/Deteriorată/Casată) și stare flux (Recepționat → Dat în Folosință → Scos din Gestiune).
- **Creare automată la recepție:** hook pe `stock_move._action_done()` — o recepție (`picking_type.code == "incoming"`) de produs marcat „Obiect de Inventar (RO)" creează fișa OI, legată de mișcarea de stoc, fără dublare la re-rulare.
- **Dare în folosință (`action_use()`):** verificare stoc 303, picking intern către locație virtuală, nota `603 = 303` și, opțional, notă extracontabilă `Dr 8035 = Cr 8035C`.
- **Nota 603=303 independentă de valorizare (`_create_usage_entry()`, din 19.0.1.1.0):** dacă produsul nu e pe o categorie cu valorizare în timp real, `stock_account` nu produce nicio notă la validarea pickingului; modulul o înregistrează atunci el, pe conturile din categoria produsului, cu revenire pe codurile `603%` / `303%` din planul companiei. Acolo unde valorizarea generează deja nota, nu se dublează. Dacă lipsesc conturile sau jurnalul, motivul e postat în chatter, în loc ca fluxul să pară reușit.
- **Scoatere din gestiune (`action_dispose()`):** tratament distinct pe `disposal_type` — casare (fără notă bilanțieră, valoarea e deja pe 603), restituire (picking invers + `Dr 303 = Cr 603` + revenire în „Recepționat"), lipsă la inventar (nicio notă automată: imputabilitatea e decizia clientului). `physical_state` rămâne starea fizică, distinctă de tipul scoaterii.
- **Wizard-uri batch** pentru dare în folosință (cu Bon PDF) și scoatere din gestiune (cu PV PDF).
- **Conturi explicite pe companie** (`l10n_ro_oi_expense_account_id`, `l10n_ro_oi_stock_account_id`, `l10n_ro_oi_journal_id`): conturile categoriei de produs sunt acceptate doar dacă au codul 603/303 — altfel ar da 607/371 (descărcare de marfă). Jurnalul extrabilanțier EXTR e exclus explicit.
- **Cont extrabilanțier 8035:** la instalare se creează contul 8035C (off_balance) și jurnalul „Evidență Extracontabilă" (EXTR), cu toggle pe companie; verificare sold prin `_check_8035_balance()`.
- **Rapoarte PDF:** Bon de Dare în Folosință, PV de Scoatere din Gestiune și Registrul Obiectelor de Inventar (multi-document, grupat pe responsabil cu subtotal, totaluri **pe stări** — cel „în folosință" e comparabil cu soldul 8035, cel „în stoc" cu 303 —, plus dată de întocmire și bloc de semnături). Fiecare raport are un template „document complet" care apelează `web.html_container` — fără el randarea PDF pică în `_prepare_html` cu `IndexError` pe `//main`.

#### 3. Dependențe

- `stock_account`
- `l10n_ro`

#### 4. Componente Cheie

##### Modele

- `l10n.ro.inventory.item`: fișa obiectului de inventar cu numerele de inventar, starea fizică, starea de flux și metodele `action_use()` / `action_dispose()`. Notele contabile: `_create_usage_entry()` (dare în folosință, câmp `usage_entry_id`) și `_create_off_balance_entry()` (extracontabil, `off_balance_entry_in_id` / `_out_id`). Din 19.0.2.0.0 numerele de cont nu mai apar în API — doar în etichetele vizibile; pre-migrarea `19.0.2.0.0` redenumește coloanele. `_get_oi_consumption_location()` citește locația din date cu `sudo` înainte de a-i compara compania — fără asta, într-o bază multi-company darea în folosință pică cu `AccessError`.
- `stock.move`: hook `_action_done()` → `_l10n_ro_oi_create_inventory_items()`, crearea fișei la recepție.
- `product.template`: extins cu marcajul „Obiect de Inventar (RO)".
- `res.company`: extins cu toggle-ul `l10n_ro_use_off_balance_entries` și conturile aferente.

##### Vizualizări / Date

- `views/l10n_ro_inventory_item_views.xml`, `views/product_template_views.xml`, `views/res_company_views.xml`, `views/menus.xml`: interfețele OI, produs, companie și meniul.
- `wizard/inventory_item_use_wizard_views.xml`, `wizard/inventory_item_dispose_wizard_views.xml`: wizard-urile batch.
- `report/report_bon_dare_in_folosinta.xml`, `report/report_pv_scoatere_gestiune.xml`, `report/report_registru_oi.xml`: rapoartele PDF (wrapper `web.html_container` + template de conținut `_document`).
- `report/report_actions.xml`: acțiunile de raport; `report_name` trebuie să trimită la wrapper, nu la `_document` — ruta `/report/html/<reportname>` rezolvă numele prin `ir.actions.report.report_name`.
- `data/ir_sequence_data.xml`, `data/stock_location_data.xml`: secvența OI și locația virtuală.

##### Acțiuni Automate / Acțiuni Server

- `migrations/19.0.2.0.0/pre-migration.py`: redenumește coloanele după ieșirea numerelor de cont din API.
- `post_init_hook`: creează contul 8035C, jurnalul „Evidență Extracontabilă" (EXTR) și locația virtuală pentru companiile RO.

#### 5. Conexiuni

- `[[l10n_ro_fixed_assets]]`
- `[[l10n_ro_inventory_closing]]`
