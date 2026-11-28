# Romania - Stock Accounting Notice

- **Nume Tehnic:** `l10n_ro_stock_notice_default`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_stock_notice_default
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_stock_notice_default`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaugă pe tipurile de operațiune de stoc opțiunea „Romania - Is a notice”. Transferurile create pentru un astfel de tip sunt marcate implicit ca aviz, deci recepțiile și livrările folosesc conturile 408/418 fără ca utilizatorul să bifeze avizul pe fiecare transfer.

#### 2. Funcționalități Cheie

- Bifa „Romania - Is a notice” pe tipul de operațiune (*Inventar → Configurare → Tipuri de operațiuni*, de exemplu Recepții).
- Transferurile noi de acel tip au indicatorul de aviz setat de la creare.
- Evaluarea avizului și notele 408/418 le face `l10n_ro_stock_account`; câmpul `l10n_ro_notice` este ținut de `l10n_ro_stock_account_base`.

#### 3. Dependențe

- [l10n_ro_stock_account_base](../l10n_ro_stock_account_base/index.md)

#### 4. Componente Cheie

**Modele**

- `stock.picking.type`: câmpul `l10n_ro_notice_default`.
- `stock.picking`: preia valoarea implicită a avizului din tipul de operațiune.

**Vizualizări**

- `view_picking_type_form`: bifa pe formularul tipului de operațiune.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- `l10n_ro_stock_account`: folosește avizul pentru conturile 408/418.
