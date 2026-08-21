# Romania - Stock Valuation Pack CMP (AVCO) (localizat la `l10n_ro_stock_pack_cmp/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_pack_cmp`
- **Versiune:** `19.0.1.3.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_stock_pack_cmp
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_pack_cmp`
- **Ultima Ingestie:** `2026-08-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul este un „pachet" (bundle) care instalează dintr-o singură mișcare toate modulele necesare pentru gestiunea contabilă a stocurilor în România cu metoda costului mediu ponderat (CMP / AVCO), conform OMFP 1802/2014 pct. 96 (metodele de evaluare la ieșire) și pct. 276–291 (evaluarea stocurilor, inventarul permanent). La instalare, configurează automat companiile românești pe metoda de cost „Average Cost" cu valorizare perpetuă, astfel încât un consultant Terrabit poate porni un client pe fluxul complet de stoc CMP fără să instaleze și să configureze manual șase module separate.

#### 2. Funcționalități Cheie

- Instalează într-un singur pas toate modulele necesare pentru evidența stocurilor pe CMP: recalcul lunar CMP, dată contabilă pe operațiile de stoc, integritatea datelor (blocarea modificării mișcărilor validate și a stocului negativ), fișa de magazie și balanța analitică, gestiuni contabile de stoc (OMFP 2861/2009) și note contabile de inventariere.
- Configurare automată la instalare (`post_init_hook`): pe companiile cu țara fiscală România, setează metoda de cost implicită pe *Average Cost (AVCO)* și valorizarea pe *perpetuă (real time)*; valorile se propagă ca implicite pentru categoriile de produse **noi** — categoriile existente nu sunt modificate, decizia rămânând a consultantului.
- Excludere reciprocă declarată în manifest cu `l10n_ro_stock_pack_fifo`: nu pot coexista pe aceeași bază de date, conform principiului permanenței metodelor (OMFP 1802 pct. 287 alin. (1)) — se alege o singură metodă de evaluare per bază de date.
- Documentație de utilizare (`readme/USAGE.md`) cu o monografie contabilă completă a fluxului de stoc pe CMP (achiziție cu factură, vânzare, retur la furnizor, achiziție pe aviz, inventariere, corecție CMP periodic la închiderea lunii), verificată automat de testul `tests/test_stock_flow.py`.

#### 3. Dependențe

- `purchase_stock`
- `sale_stock`
- [l10n_ro_stock_cmp_periodic](../l10n_ro_stock_cmp_periodic/index.md)
- [l10n_ro_stock_posting_date](../l10n_ro_stock_posting_date/index.md)
- [l10n_ro_stock_constraints](../l10n_ro_stock_constraints/index.md)
- [l10n_ro_stock_sheet](../l10n_ro_stock_sheet/index.md)
- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md)
- [l10n_ro_inventory_closing](../l10n_ro_inventory_closing/index.md)

#### 4. Componente Cheie

Modulul nu definește modele sau vizualizări proprii — este un pachet fără directoare `models/` sau `views/`, format exclusiv din declarația de dependențe și un hook de configurare la instalare.

**Modele**

- Niciun model propriu; toată logica de business e furnizată de modulele dependente.

**Vizualizări**

- Nicio vizualizare proprie.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook` (`hooks.py`): rulează o singură dată, la instalare. Caută companiile cu țara fiscală România (`account_fiscal_country_id.code == "RO"`) și, dacă e nevoie, le setează `cost_method = "average"` și `inventory_valuation = "real_time"`. Aceste valori se propagă apoi ca `ir.default` pe categoriile de produse noi.

#### 5. Conexiuni

- [l10n_ro_stock_pack_fifo](../l10n_ro_stock_pack_fifo/index.md): pachet echivalent pentru metoda FIFO; se exclud reciproc prin `excludes` în manifest — nu pot coexista în aceeași bază de date.
- [l10n_ro_stock_cmp_periodic](../l10n_ro_stock_cmp_periodic/index.md): oferă recalculul lunar CMP folosit în monografia din `readme/USAGE.md`.
- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md): gestiunile contabile de stoc (OMFP 2861/2009) pe care se sprijină fluxul descris (pivotul 408, transfer 481).
- [l10n_ro_inventory_closing](../l10n_ro_inventory_closing/index.md): notele contabile de inventariere (plusuri/minusuri) folosite la pasul de inventariere din monografie.
