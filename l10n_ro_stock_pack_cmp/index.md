# Romania - Pachet valorizare stocuri CMP (localizat la `l10n_ro_stock_pack_cmp/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_pack_cmp`
- **Versiune:** `19.0.1.5.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_stock_pack_cmp
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_pack_cmp`
- **Ultima Ingestie:** `2026-11-12`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul este un „pachet" (bundle) care instalează dintr-o singură mișcare modulele necesare pentru gestiunea contabilă a stocurilor în România cu metoda costului mediu ponderat (CMP / AVCO), conform OMFP 1802/2014 pct. 96 (metodele de evaluare la ieșire) și pct. 276–291 (evaluarea stocurilor, inventarul permanent). La instalare, configurează automat companiile românești pe metoda de cost „Average Cost" cu valorizare perpetuă, astfel încât un consultant Terrabit poate porni un client pe fluxul de stoc CMP fără să instaleze și să configureze manual mai multe module separate.

#### 2. Funcționalități Cheie

- Instalează într-un singur pas modulele necesare pentru evidența stocurilor pe CMP: dată contabilă pe operațiile de stoc, integritatea datelor (blocarea modificării mișcărilor validate și a stocului negativ), fișa de magazie și balanța analitică, gestiuni contabile de stoc (OMFP 2861/2009) și note contabile de inventariere.
- Recalculul lunar CMP (`l10n_ro_stock_cmp_periodic`) **nu mai face parte din pachet**: nu poate fi instalat împreună cu `deltatech_obyc` (determinarea conturilor prin OBYC). Pe bazele fără OBYC se instalează separat.
- Configurare automată la instalare (`post_init_hook`): pe companiile cu țara fiscală România, setează metoda de cost implicită pe *Average Cost (AVCO)* și valorizarea pe *perpetuă (real time)*; valorile se propagă ca implicite pentru categoriile de produse **noi** — categoriile existente nu sunt modificate, decizia rămânând a consultantului.
- Excludere reciprocă declarată în manifest cu `l10n_ro_stock_pack_fifo`: nu pot coexista pe aceeași bază de date, conform principiului permanenței metodelor (OMFP 1802 pct. 287 alin. (1)) — se alege o singură metodă de evaluare per bază de date.
- Pași de configurare după instalare: în **Setări → Inventar** se bifează *Recepție fără factură (371 = 408)* cu *Cont 408 implicit* și se setează conturile de plus și de minus de inventar (recomandat 607 pentru mărfuri; fără ele asistentul de note de inventariere refuză generarea); categoriile de produse se completează cu *Cont stoc* (371 pentru mărfuri).
- Documentație de utilizare (`readme/USAGE.md`) cu o monografie contabilă a fluxului de stoc pe CMP (achiziție cu recepție și factură pe 408, vânzare cu descărcare 607 = 371 la facturare, retur la furnizor cu stornare în roșu, achiziție pe aviz, inventariere cu minus), verificată automat de testul `tests/test_stock_flow.py`; fluxul detaliat pas cu pas rămâne în fișa consultant.

#### 3. Dependențe

- `purchase_stock`
- `sale_stock`
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
- [l10n_ro_stock_cmp_periodic](../l10n_ro_stock_cmp_periodic/index.md): recalculul lunar CMP, scos din pachet; se instalează separat, doar pe bazele fără `deltatech_obyc`.
- [deltatech_obyc](../deltatech_obyc/index.md): determinarea conturilor prin OBYC, incompatibilă cu `l10n_ro_stock_cmp_periodic` și motivul pentru care acesta a fost scos din pachet.
- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md): gestiunile contabile de stoc (OMFP 2861/2009) pe care se sprijină fluxul descris (pivotul 408, transfer 481).
- [l10n_ro_inventory_closing](../l10n_ro_inventory_closing/index.md): notele contabile de inventariere (plusuri/minusuri) folosite la pasul de inventariere din monografie.
