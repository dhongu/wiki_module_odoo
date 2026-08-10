# Romania - Stock Valuation Pack FIFO (localizat la `l10n_ro_stock_pack_fifo/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_pack_fifo`
- **Versiune:** `19.0.1.3.0`
- **Cale:** [https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_stock_pack_fifo](https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_stock_pack_fifo)
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_pack_fifo`
- **Ultima Ingestie:** `2026-08-10`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul-pălărie (bundle) care instalează dintr-o singură mișcare toate modulele necesare pentru gestiunea contabilă a stocurilor în România cu metoda FIFO (primul intrat — primul ieșit), conform OMFP 1802/2014 pct. 293–305. La instalare, configurează automat pe companiile cu țara fiscală România metoda de cost FIFO și valorizarea perpetuă (real time), simplificând semnificativ setarea corectă a contabilității de stoc pentru un consultant sau implementator.

#### 2. Funcționalități Cheie

- Instalează într-un singur pas toate modulele necesare pentru evidența contabilă a stocurilor pe FIFO: dată contabilă pe operațiile de stoc, integritate a datelor (blocare mișcări validate/stoc negativ), fișa de magazie, gestiuni contabile de stoc și note contabile de inventariere.
- La instalare (`post_init_hook`), setează automat pe companiile românești metoda de cost implicită `fifo` și valorizarea stocului `real_time` (perpetuă); valorile se propagă ca implicite doar pentru categoriile de produse **noi** — categoriile existente nu sunt modificate.
- Exclude reciproc coexistența cu pachetul `l10n_ro_stock_pack_cmp` (o singură metodă de evaluare per bază de date, conform principiului permanenței metodelor — OMFP 1802 pct. 287 alin. (1)).
- FIFO este metoda de cost nativă Odoo, deci pachetul nu conține un modul specific de recalcul periodic — diferența față de pachetul CMP este doar configurarea metodei de cost la instalare și absența corecției lunare.
- Monografia contabilă completă (achiziție cu factură, vânzare, retur la furnizor, achiziție pe aviz, inventariere cu minus neimputabil) e documentată și verificată automat prin testul `tests/test_stock_flow.py`.

#### 3. Dependențe

- `purchase_stock`
- `sale_stock`
- [l10n_ro_stock_posting_date](../l10n_ro_stock_posting_date/index.md)
- [l10n_ro_stock_constraints](../l10n_ro_stock_constraints/index.md)
- [l10n_ro_stock_sheet](../l10n_ro_stock_sheet/index.md)
- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md)
- [l10n_ro_inventory_closing](../l10n_ro_inventory_closing/index.md)

#### 4. Componente Cheie

Acest modul nu conține modele, vizualizări sau date proprii — este un pachet pur de dependențe (`data: []`), fără director `models/` sau `views/`. Singurul cod propriu este hook-ul de post-instalare.

**Modele**

Nu definește și nu extinde niciun model.

**Vizualizări**

Nu conține vizualizări proprii.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook` (`hooks.py`): la instalarea modulului, pentru fiecare companie cu `account_fiscal_country_id.code == "ro"`, setează `cost_method = "fifo"` și `inventory_valuation = "real_time"` dacă nu sunt deja astfel; scrierea pe `res.company` propagă valorile ca `ir.default` pe `product.category` (via `_set_category_defaults`), afectând doar categoriile create ulterior.

#### 5. Conexiuni

- [l10n_ro_stock_pack_cmp](../l10n_ro_stock_pack_cmp/index.md): pachet echivalent pentru metoda CMP (cost mediu ponderat); exclus reciproc prin `excludes` în manifest — nu pot coexista în aceeași bază de date.
