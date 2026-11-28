# Romania - Stock Accounting Store

- **Nume Tehnic:** `l10n_ro_stock_account_store`
- **Versiune:** `20.0.1.1.2`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_stock_account_store
- **Cale Locală:** odoo-addons/l10n-romania/l10n_ro_stock_account_store
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Contabilitatea stocurilor de mărfuri ținute la preț de vânzare (magazin cu amănuntul) pentru companiile din România. O locație marcată ca **Magazin** păstrează marfa la preț de vânzare, cu TVA inclus; fiecare mișcare care intră sau iese din ea primește, pe lângă nota de stoc la cost, o notă separată pentru adaosul comercial (378) și TVA neexigibil (4428).

#### 2. Funcționalități Cheie

- Primirea mărfii de la furnizor cu factură (371 = 401, 4426 = 401, apoi 371 = 378 și 371 = 4428) sau cu aviz (371 = 408, apoi adaos și TVA; la sosirea facturii 408 = 401).
- Transferul din depozit (la cost) în magazin: transferul la cost, apoi 371 = 378 și 371 = 4428.
- Ieșirea din magazin (livrare, consum, minus la inventar, transfer în depozit): 378 = 371 și 4428 = 371, alături de ieșirea la cost.
- Retururile (către furnizor, de la client) stornează în roșu adaosul și TVA ale mișcării returnate, la prețul ei de vânzare.
- Prețul de vânzare se ia din produs (**Sales Price** și **Customer Taxes**); sumele rămân pe mișcarea de stoc (**Store Sale Amount**, **Store Markup**, **Store Uneligible VAT**), vizibile în grupul **Store Valuation** (*Inventar > Raportare > Moves History*).
- Reevaluarea automată la schimbarea prețului de vânzare, cu document numerotat (*Inventar > Raportare > Store Revaluations*): creștere 371 = 378 / 4428, reducere în sens invers. Reducerea sub costul unitar și schimbarea într-o perioadă blocată sunt refuzate.
- Configurare: **Not Eligible Tax Account** (4428) pe companie, **Romania - Store Markup Account** (378) pe categoria de produs cu evaluare perpetuă, opțional un cont dedicat pentru TVA neexigibil, iar pe locație **Romania - Merchandise type** = **Store**.
- Limite: transferul între două magazine nu mută adaos sau TVA; stocul existent la instalare cere o notă de deschidere (371 = 378 / 4428); nu acoperă eliberarea lunară cu coeficientul K, vânzările din POS, procesul-verbal de modificare a prețurilor și raportul de inventar la preț de vânzare.

#### 3. Dependențe

- `l10n_ro_stock_account`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.store.revaluation`: reevaluarea numerotată a stocului din magazin.
- `stock.location`: tipul de marfă (Magazin).
- `stock.move`: sumele de adaos și TVA neexigibil.
- `product.category`, `product.template`, `product.template.attribute.value`: contul de adaos și detectarea schimbării prețului.

**Vizualizări**

- `view_location_store_form`, `view_location_tree_store`, `view_location_search_store`: locația de tip magazin.
- `view_product_category_store_form`: conturile de adaos și TVA neexigibil pe categorie.
- `view_move_form_store`, `view_move_tree_store`: grupul Store Valuation pe mișcarea de stoc.
- `view_store_revaluation_list`, `view_store_revaluation_form`, `view_store_revaluation_search`: reevaluările magazinului.

**Acțiuni Automate / Acțiuni Server**

- Secvență de numerotare pentru reevaluări (`data/ir_sequence.xml`); fără cron.

#### 5. Conexiuni

- `l10n_ro_stock_account`: baza contabilității de stoc pe care se montează notele de magazin.
