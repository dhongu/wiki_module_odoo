# Sales Dashboard - Returns (localizat la `deltatech_sale_dashboard_rma/index.md`)

- **Nume Tehnic:** `deltatech_sale_dashboard_rma`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_sale_dashboard_rma
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_sale_dashboard_rma`
- **Ultima Ingestie:** 2026-11-28

#### 1. Sumar

Adaugă pe tabloul de bord de vânzări cererile de retur și reclamațiile de garanție din modulul de retururi. Managerul de vânzări vede dintr-o privire câte retururi așteaptă o decizie și câte sunt în curs, fără să deschidă separat aplicația de retururi. Modulul se instalează automat când sunt prezente ambele module de bază.

#### 2. Funcționalități Cheie

- **Retururi de aprobat**: cererile trimise, care așteaptă o decizie.
- **Retururi în curs**: cererile aprobate și neînchise (colet așteptat, primit sau inspectat).
- **Cereri de retur** în rezultatele perioadei, comparate cu perioada anterioară.
- O cerere de retur aparține agentului de vânzări responsabil și echipei de vânzări a comenzii sale.
- Un clic pe card deschide lista cererilor numărate de acesta.

#### 3. Dependențe

- [deltatech_sale_dashboard](../deltatech_sale_dashboard/index.md)
- [deltatech_rma](../deltatech_rma/index.md)

#### 4. Componente Cheie

**Modele**

- `deltatech.sale.dashboard` (extins): adaugă cardurile și indicatorii de retur.

**Vizualizări**

- Modulul nu definește vizualizări proprii; folosește tabloul de bord din `deltatech_sale_dashboard`.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_sale_dashboard](../deltatech_sale_dashboard/index.md): tabloul de bord extins.
- [deltatech_rma](../deltatech_rma/index.md): sursa cererilor de retur.
