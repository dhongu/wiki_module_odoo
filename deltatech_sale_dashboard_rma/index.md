# Sales Dashboard - Returns (localizat la `deltatech_sale_dashboard_rma/index.md`)

- **Nume Tehnic:** `deltatech_sale_dashboard_rma`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_sale_dashboard_rma
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_sale_dashboard_rma`
- **Ultima Ingestie:** `2026-10-06`

#### 1. Sumar

Puntea dintre tabloul de bord de vânzări și modulul de retururi/garanții. Adaugă pe dashboard cererile de retur și de garanție care așteaptă o decizie sau sunt în curs de procesare, astfel încât responsabilul de vânzări să vadă dintr-o privire ce are de aprobat. Se instalează automat atunci când ambele module sunt prezente.

#### 2. Funcționalități Cheie

- **Retururi de aprobat** (indicator de lucru): cererile trimise, care așteaptă o decizie (stare „trimisă”).
- **Retururi în curs** (indicator de lucru): cererile aprobate și neînchise — colet așteptat, recepționat sau inspectat.
- **Cereri de retur** în rezultatele perioadei, comparate cu perioada anterioară (ciorne și anulate excluse, după data cererii).
- O cerere aparține agentului de vânzări responsabil și echipei de vânzări a comenzii sale.
- Click pe un card deschide lista cererilor numărate.

#### 3. Dependențe

- [deltatech_sale_dashboard](../deltatech_sale_dashboard/index.md)
- [deltatech_rma](../deltatech_rma/index.md)

Modulul are `auto_install: True`.

#### 4. Componente Cheie

**Modele**

- `deltatech.sale.dashboard` (model abstract, extins): adaugă indicatorii `rma_to_approve` și `rma_in_progress` (în `_dashboard_work_kpis`) și `period_rma` (în `_dashboard_period_kpis`), peste modelul `deltatech.rma`.

**Vizualizări**

- Fără vizualizări proprii; cardurile deschid acțiunea `deltatech_rma.action_deltatech_rma_all`.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_sale_dashboard_delivery](../deltatech_sale_dashboard_delivery/index.md): punte soră, aduce livrările pe același dashboard.
