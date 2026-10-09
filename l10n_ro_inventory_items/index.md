# Romania - Obiecte de inventar (303/603/8035) (localizat la `l10n_ro_inventory_items/index.md`)

- **Nume Tehnic:** `l10n_ro_inventory_items`
- **Versiune:** `19.0.2.5.1`
- **Cale:** `https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_inventory_items`
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_inventory_items`
- **Ultima Ingestie:** `2026-10-09`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Implementează fluxul complet de gestiune a obiectelor de inventar conform OMFP 1802/2014 — bunuri sub pragul fiscal al mijloacelor fixe (5.000 lei din anul fiscal 2026, art. 28 alin. (2) lit. b) din Legea 227/2015, modificat prin OUG 8/2026). Acoperă recepția (Dr 303 = Cr 401), darea în folosință (Dr 603 = Cr 303), evidența extrabilanțieră opțională pe contul 8035 (contrapartidă 803999) și scoaterea din gestiune, cu fișă de obiect de inventar, wizard-uri batch și rapoarte PDF. Fișa OI se creează automat la recepția produselor marcate „Obiect de Inventar (RO)", iar nota de dare în folosință e generată de modul și atunci când valorizarea de stoc nu o produce.

#### 2. Funcționalități Cheie

- **Fișa OI (`l10n.ro.inventory.item`):** nr. inventar auto-generat `OI/AAAA/NNNN`, responsabil, locație/departament cu tracking, stare fizică (Bună/Deteriorată/Casată) și stare flux (Recepționat → Dat în Folosință → Scos din Gestiune). Se poate crea și manual (obiecte aflate în stoc înainte de activare).
- **Creare automată la recepție:** hook pe `stock_move._action_done()` — o recepție (`picking_type.code == "incoming"`) de produs marcat „Obiect de Inventar (RO)" creează fișa OI în starea „Recepționat (în stoc 303)", cu valoarea din prețul recepției (sau costul standard) și responsabil utilizatorul care validează; fișa e legată de mișcarea de stoc, fără dublare la re-rulare.
- **Dare în folosință (`action_use()`):** verificare stoc 303, picking intern către locație virtuală, nota `603 = 303` și, opțional, nota extracontabilă `Dr 8035 = Cr 803999`. Se consumă întreaga cantitate a fișei (fără dare parțială). Data aleasă în wizard datează fișa, pickingul, mișcările de stoc și notele.
- **Nota 603=303 independentă de valorizare (`_create_usage_entry()`):** dacă produsul nu e pe o categorie cu valorizare în timp real, modulul înregistrează el nota, pe conturile din categoria produsului, cu revenire pe codurile `603%` / `303%` din planul companiei. Acolo unde valorizarea o generează deja, nu se dublează. Dacă lipsesc conturile sau jurnalul, motivul e postat în chatter.
- **Validarea datelor operațiilor:** data dării în folosință / scoaterii nu poate fi în viitor, înaintea intrării în stoc (respectiv a dării în folosință) și nici într-o perioadă contabilă blocată.
- **Scoatere din gestiune (`action_dispose()`):** tratament distinct pe `disposal_type` — casare (fără notă bilanțieră, valoarea e deja pe 603), restituire la magazie (picking invers + `Dr 303 = Cr 603` + revenire în „Recepționat"), lipsă la inventar. Comisia de inventariere aleasă se salvează pe fișă și apare în PV.
- **Imputarea lipsei la inventar:** din wizardul de scoatere, dacă lipsa e imputabilă, se înregistrează `Dr 4282` (salariat) sau `Dr 461` (terț) `= Cr 7588`, cu valoarea imputată (implicit valoarea de înregistrare, editabilă), fără TVA colectată (HG 1/2016, Titlul VII, pct. 78 alin. (6) lit. a)). Fără imputare nu se înregistrează nicio notă.
- **Wizard-uri batch** (meniul Inventar → Obiecte de Inventar): „Dare în Folosință (batch)" cu Bon PDF și „Scoatere din Gestiune (batch)" cu PV PDF.
- **Casare obiecte de inventar vechi (wizard „Scrap Old Inventory Items"):** propune obiectele în folosință de peste N luni (implicit 12), opțional ale unui responsabil; comisia și motivul sunt obligatorii; fiecare obiect e scos ca „casat" (stornând 8035 contra 803999), cu un singur PV pentru toate.
- **Conturi explicite pe companie** (`l10n_ro_oi_expense_account_id`, `l10n_ro_oi_stock_account_id`, `l10n_ro_oi_journal_id`): conturile categoriei de produs sunt acceptate doar dacă au codul 603/303 — altfel ar da 607/371. Jurnalul extrabilanțier EXTR e exclus explicit.
- **Evidență extrabilanțieră 8035:** toggle pe companie (Setări → Companie → „Obiecte de Inventar (RO)"); contrapartida tehnică comună 803999 și jurnalul „Evidență extrabilanțieră" (EXTR) vin din `l10n_ro_off_balance` și se creează și pe companiile apărute după instalare. Opțional, pe produs se poate seta un „Cont 8035" diferit. Butonul „Verifică reconciliere 8035" din listă compară soldul 8035 cu valoarea obiectelor în folosință.
- **Rapoarte PDF:** Bon de Dare în Folosință, PV de Scoatere din Gestiune și Registrul Obiectelor de Inventar (multi-document, grupat pe responsabil cu subtotal, totaluri **pe stări** — „în folosință" comparabil cu 8035, „în stoc" cu 303 —, bloc de semnături). Fiecare raport are un template „document complet" cu `web.html_container`, altfel randarea PDF pică în `_prepare_html`.
- **Atenție la compatibilitatea cu OCA `l10n_ro_stock_account`:** câmpul „Consume Account" de pe contul 303 trebuie lăsat necompletat, altfel apare o notă tehnică suplimentară (ex. „603=603").
- **Salariat pe fișă:** prin modulul separat `l10n_ro_inventory_items_hr`; modulul de bază nu depinde de Angajați.

#### 3. Dependențe

- `stock_account`
- `l10n_ro`
- [l10n_ro_off_balance](../l10n_ro_off_balance/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.inventory.item`: fișa obiectului de inventar cu numerele de inventar, starea fizică, starea de flux, `disposal_type` (casat / lipsă / restituit) și metodele `action_use()` / `action_dispose()`. Notele contabile: `_create_usage_entry()` (`usage_entry_id`), `_create_off_balance_entry()` (`off_balance_entry_in_id` / `_out_id`), `_create_imputation_entry()` (`imputation_move_id`) și `_create_return_entry()`. `_check_operation_date()` validează datele operațiilor; `_get_holder_name()` e punctul de extindere pentru responsabil (folosit de bon, PV și registru). `_get_oi_consumption_location()` citește locația cu `sudo` înainte de a compara compania, ca să evite `AccessError` în multi-company.
- `stock.move`: hook `_action_done()` → `_l10n_ro_oi_create_inventory_items()`, crearea fișei la recepție.
- `product.template`: marcajul `l10n_ro_is_inventory_item` și contul opțional `l10n_ro_oi_off_balance_account_id` („Cont 8035").
- `res.company`: toggle-ul `l10n_ro_use_off_balance_entries` și conturile/jurnalul `l10n_ro_oi_*`.
- `inventory.item.use.wizard`, `inventory.item.dispose.wizard` (tip scoatere, motiv, comisie, imputare: `imputable`, `imputation_kind`, `imputation_partner_id`, `imputation_amount`) și `inventory.item.auto.dispose.wizard` (casarea obiectelor vechi) — wizard-urile din `wizard/`.

**Vizualizări**

- `views/l10n_ro_inventory_item_views.xml`, `views/product_template_views.xml`, `views/res_company_views.xml`, `views/menus.xml`: interfețele OI, produs, companie și meniul (Registru OI, Dare în Folosință batch, Scoatere din Gestiune batch, Casare obiecte de inventar vechi).
- `wizard/inventory_item_use_wizard_views.xml`, `wizard/inventory_item_dispose_wizard_views.xml`, `wizard/inventory_item_auto_dispose_wizard_views.xml`: wizard-urile.
- `report/report_bon_dare_in_folosinta.xml`, `report/report_pv_scoatere_gestiune.xml`, `report/report_registru_oi.xml`: rapoartele PDF (wrapper `web.html_container` + template `_document`).
- `report/report_actions.xml`: acțiunile de raport; `report_name` trebuie să trimită la wrapper, nu la `_document`.
- `data/ir_sequence_data.xml`, `data/stock_location_data.xml`: secvența OI și locația virtuală.

**Acțiuni Automate / Acțiuni Server**

Nu există `ir.cron` sau acțiuni server. Scripturi de migrare și hook:

- `migrations/19.0.2.0.0/pre-migration.py`: redenumește coloanele după ieșirea numerelor de cont din API.
- `migrations/19.0.2.1.0/post-migration.py`: completează conturile și jurnalul dării în folosință (`l10n_ro_oi_*`) pe companiile RO existente.
- `migrations/19.0.2.5.0/post-migration.py`: mută soldul 8035C pe 803999 printr-o notă de transfer **în ciornă** în jurnalul EXTR (de verificat și postat de contabil; apoi 8035C se poate arhiva).
- `post_init_hook`: activează evidența 8035 pentru companiile RO (contrapartida 803999 și jurnalul EXTR vin din `l10n_ro_off_balance`) și pregătește locația virtuală.

#### 5. Conexiuni

- [l10n_ro_inventory_items_hr](../l10n_ro_inventory_items_hr/index.md): adaugă salariatul pe fișă, în wizardul de dare în folosință și în documente.
- [l10n_ro_fixed_assets](../l10n_ro_fixed_assets/index.md): mijloace fixe, categoria de active de peste pragul OI.
- [l10n_ro_inventory_closing](../l10n_ro_inventory_closing/index.md): inventarierea/închiderea de inventar, unde registrul OI servește comisiei.
