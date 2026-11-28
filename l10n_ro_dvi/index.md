# Romania - DVI (Declarație Vamală de Import)

- **Nume Tehnic:** `l10n_ro_dvi`
- **Versiune:** `20.0.0.3.0`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_dvi
- **Cale Locală:** odoo-addons/l10n-romania-oca/l10n_ro_dvi
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul leagă factura de achiziție de declarația vamală de import (DVI) și înregistrează automat TVA-ul și cheltuielile vamale prin costuri suplimentare (landed cost), distribuindu-le corect pe produse.

#### 2. Funcționalități Cheie

- DVI creat din **Contabilitate → Acțiuni → DVI**, cu data, jurnalul, taxa TVA deductibilă și facturile asociate.
- Se completează valoarea taxei vamale și a comisionului vamal, precum și cantitățile declarate pe liniile DVI.
- La **Postare** se generează automat un landed cost (cu linii pentru taxa vamală, comision și TVA) care distribuie sumele pe produse și creează notele contabile pentru TVA-ul plătit.
- DVI poate fi stornat: se creează straturi de evaluare cu minus și se anulează nota contabilă a landed cost-ului inițial.
- Contul 447 trebuie să fie cont de reconciliere, pentru a putea fi închis prin bancă.
- Din factură se poate deschide DVI-ul asociat; diferențele de TVA se înregistrează pe un produs dedicat.
- Documentație suplimentară în `doc/DVI.docx` (în modul).

#### 3. Dependențe

- `l10n_ro_stock_account_landed_cost`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.account.dvi`: declarația vamală (stare, taxă, facturi, valori vamale, landed costs, diferență TVA).
- `l10n.ro.account.dvi.line`: linii DVI legate de liniile facturii, cu cantitatea declarată.
- `account.move`: legătura cu DVI-urile (`action_view_dvis`).
- `stock.landed.cost`, `stock.valuation.adjustment.lines`, `account.tax`, `res.company`: extinse pentru fluxul DVI.

**Vizualizări**

- `view_account_dvi_form`: formularul DVI.
- `view_move_form`: legătura din factură.
- `view_stock_landed_cost_form`: legătura din landed cost.

**Acțiuni Automate / Acțiuni Server**

- Nu are; meniul `menu_action_account_dvi` deschide lista DVI.

#### 5. Conexiuni

- `l10n_ro_stock_account_landed_cost`: sursa mecanismului de costuri suplimentare.
