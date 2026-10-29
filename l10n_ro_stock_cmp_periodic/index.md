# Romania - CMP periodic lunar (localizat la `l10n_ro_stock_cmp_periodic/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_cmp_periodic`
- **Versiune:** `19.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_stock_cmp_periodic
- **Cale Locală:** odoo-addons/l10n_ro_ent/l10n_ro_stock_cmp_periodic
- **Ultima Ingestie:** `2026-10-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul recalculează lunar Costul Mediu Ponderat (CMP) conform OMFP 1802/2014, pentru firmele care folosesc CMP periodic (lunar) în locul CMP perpetuu folosit implicit de Odoo 19. La finele lunii, modulul calculează CMP-ul lunar din stocul inițial și toate intrările, determină diferența față de valoarea perpetuă deja postată și generează o singură notă contabilă de corecție, fără să modifice notele postate anterior, cu audit trail complet. Firmele care folosesc FIFO sau acceptă CMP perpetuu nu au nevoie de el.

#### 2. Funcționalități Cheie

- **Recalcul CMP lunar:** `CMP_lunar = (Val_stoc_inițial + Val_intrări) / (Cant_stoc_inițial + Cant_intrări)`; la numitor zero se folosește `standard_price` ca fallback.
- **Notă de corecție (Abordarea B):** o singură notă echilibrată `602/607 ↔ 302/371`, datată în ultima zi a lunii, cu două linii per produs cu Δ ≠ 0; conturile se iau din fișa produsului. Δ pozitiv înseamnă ieșiri subevaluate, Δ negativ ieșiri supraevaluate, iar la Δ = 0 nu se generează linie. Corecția nu afectează TVA.
- **Wizard cu previzualizare:** **Contabilitate → CMP Periodic Lunar → Recalcul CMP Periodic**; perioada implicită este luna curentă, produsele se pot restrânge opțional, iar tabelul arată per produs stocul inițial, intrările, ieșirile, CMP perpetuu și periodic, valorile și Δ corecție, înainte de confirmare.
- **Activare per categorie de produs:** pe companie se activează opțiunea și se alege un jurnal de tip *Operațiuni diverse*; se procesează doar categoriile bifate „CMP periodic lunar", cu metoda de cost Cost mediu (AVCO).
- **Audit trail:** **Registru CMP Periodic** (stări draft/calculat/postat) cu stoc inițial, intrări, CMP perpetuu vs. periodic, Δ corecție și nota asociată; fiecare mișcare de ieșire din lună este marcată cu valoarea provizorie (CMP perpetuu) și valoarea finală (CMP periodic).
- **Protecții:** recalculul este blocat dacă luna este deja postată sau perioada este blocată fiscal; pentru a recalcula, nota se anulează și liniile lunii se șterg sau se resetează din registru.
- **Recalcul automat opțional:** job lunar, **inactiv implicit**, care rulează în ultima zi a lunii (bifa „Recalcul automat la închidere lună"); mișcările înregistrate după rulare nu intră în corecție.
- Coexistă cu coeficientul K (metode independente, pot fi active simultan).

#### 3. Dependențe

- `account`
- `stock_account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n_ro.cmp_period_line`: registrul de audit al calculelor CMP periodic, per produs și lună.
- `l10n_ro.cmp_periodic_wizard` / `l10n_ro.cmp_periodic_wizard.line` (wizard): calculul previzual și generarea notei de corecție.
- `res.company`, `res.config.settings`, `product.category`, `stock.move`, `account.move` (extinse): activarea pe companie și categorie, câmpurile de valoare provizorie/finală pe mișcări, marcarea notelor de corecție.

**Vizualizări**

- `view_l10n_ro_cmp_periodic_wizard_form`: wizardul de recalcul cu previzualizare.
- `view_l10n_ro_cmp_period_line_list` / `view_l10n_ro_cmp_period_line_form`: Registrul CMP Periodic.
- `view_product_category_form_cmp_periodic`: bifa pe categoria de produs.
- `view_stock_move_form_cmp_periodic`: secțiunea CMP Periodic pe mișcarea de stoc.
- `view_account_move_search_cmp_periodic`: filtrul „Corecții CMP periodic" pe note contabile.
- `res_config_settings_view_form_cmp_periodic`: setările CMP periodic.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_cmp_periodic` („CMP Periodic Lunar — Recalcul automat"): recalcul lunar în ultima zi a lunii pentru companiile cu funcția activă și jurnal configurat; inactiv implicit.

#### 5. Conexiuni

- [l10n_ro_stock_k_coefficient](../l10n_ro_stock_k_coefficient/index.md): metodă alternativă pentru prețuri prestabilite, independentă; pot fi active simultan.
