# Romania - Stock Valuation Pack FIFO (localizat la `l10n_ro_stock_pack_fifo/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_pack_fifo`
- **Versiune:** `19.0.1.3.3`
- **Cale:** [https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_stock_pack_fifo](https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_stock_pack_fifo)
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_pack_fifo`
- **Ultima Ingestie:** `2026-08-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul-pălărie (bundle) care instalează dintr-o singură mișcare toate modulele necesare pentru gestiunea contabilă a stocurilor în România cu metoda FIFO (primul intrat — primul ieșit), conform OMFP 1802/2014 pct. 96 (metode de evaluare la ieșire) și pct. 276–291 (evaluarea stocurilor, inventarul permanent). La instalare, configurează automat pe companiile cu țara fiscală România metoda de cost FIFO și valorizarea perpetuă (real time), simplificând semnificativ setarea corectă a contabilității de stoc pentru un consultant sau implementator.

#### 2. Funcționalități Cheie

- Instalează într-un singur pas toate modulele necesare pentru evidența contabilă a stocurilor pe FIFO: dată contabilă pe operațiile de stoc (cu gardă cronologică pentru corectitudinea straturilor FIFO), integritate a datelor (blocare mișcări validate/stoc negativ), fișa de magazie (14-3-8) și balanța analitică a stocurilor, gestiuni contabile de stoc conform OMFP 2861/2009 (gestionar, conturi pe gestiune, transfer 481, recepție fără factură 371=408) și note contabile de inventariere (plusuri/minusuri).
- La instalare (`post_init_hook`), setează automat pe companiile românești metoda de cost implicită `fifo` și valorizarea stocului `real_time` (perpetuă); valorile se propagă ca implicite doar pentru categoriile de produse **noi** — categoriile existente nu sunt modificate.
- Exclude reciproc coexistența cu pachetul `l10n_ro_stock_pack_cmp` (o singură metodă de evaluare per bază de date, conform principiului permanenței metodelor — OMFP 1802 pct. 287 alin. (1): metoda aleasă se aplică cu consecvență, schimbarea fiind permisă doar în situații excepționale, cu prezentarea motivului și a efectelor în notele explicative).
- FIFO este metoda de cost nativă Odoo, deci pachetul nu conține un modul specific de recalcul periodic — diferența față de pachetul CMP este doar configurarea metodei de cost la instalare și absența corecției lunare.
- Monografia contabilă completă (achiziție cu factură, vânzare, retur la furnizor, achiziție pe aviz cu factură ulterioară, vânzare pe două straturi, inventariere cu minus neimputabil) e documentată în `readme/USAGE.md` și verificată automat prin testul `tests/test_stock_flow.py`; include și un comparativ cu rezultatul aceluiași scenariu rulat pe pachetul CMP.

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

- `post_init_hook` (`hooks.py`): la instalarea modulului, pentru fiecare companie cu `account_fiscal_country_id.code == "RO"`, setează `cost_method = "fifo"` și `inventory_valuation = "real_time"` dacă nu sunt deja astfel; scrierea pe `res.company` propagă valorile ca `ir.default` pe `product.category` (via `_set_category_defaults`), afectând doar categoriile create ulterior.

#### 5. Conexiuni

- [l10n_ro_stock_pack_cmp](../l10n_ro_stock_pack_cmp/index.md): pachet echivalent pentru metoda CMP (cost mediu ponderat); exclus reciproc prin `excludes` în manifest — nu pot coexista în aceeași bază de date. Monografia din `readme/USAGE.md` include un comparativ direct al aceluiași scenariu contabil rulat pe cele două pachete.
