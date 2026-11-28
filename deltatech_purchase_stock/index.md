# Purchase Stock (localizat la `deltatech_purchase_stock/index.md`)

- **Nume Tehnic:** `deltatech_purchase_stock`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_purchase_stock
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_stock`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul păstrează separate comenzile de achiziție create manual de cumpărător de cele generate de reaprovizionare. Comenzile generate automat nu se mai contopesc cu comenzile manuale în curs, ceea ce evită modificarea neașteptată a unei comenzi la care lucrează cumpărătorul.

#### 2. Funcționalități Cheie

- Separarea comenzilor de achiziție manuale de cele din reaprovizionare.
- Comenzile generate de reaprovizionare sunt marcate ca atare și sunt reutilizate doar de reaprovizionările următoare.

#### 3. Dependențe

- `purchase_stock`

#### 4. Componente Cheie

Descrierea modulului (`readme/DESCRIPTION.md`) nu detaliază componente tehnice; analiza suplimentară a codului a fost omisă conform schemei.

**Modele**

- `purchase.order`: câmpul boolean `from_replenishment`.
- `stock.rule`: marchează comenzile create de regulă și le caută la grupare doar printre cele cu `from_replenishment`.

**Vizualizări**

Modulul nu definește vizualizări.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește acțiuni automate.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale către alte module cu pagină în wiki.
