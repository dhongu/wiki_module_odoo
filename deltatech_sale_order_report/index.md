# Deltatech Sale Order Report - Obsolete (localizat la `deltatech_sale_order_report/index.md`)

- **Nume Tehnic:** `deltatech_sale_order_report`
- **Versiune:** `19.0.1.0.7`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/deltatech_sale_order_report
- **Cale Locală:** `odoo-addons/terrabit/deltatech_sale_order_report`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modul **obsolet**, păstrat doar pentru ca bazele de date existente să poată fi actualizate. Formularul comenzii de vânzare pe care îl oferea înainte se află acum în [l10n_ro_sale_order_report](../l10n_ro_sale_order_report/index.md). Modulul nu conține cod, vizualizări sau raport propriu; instalarea lui într-o bază nouă doar aduce dependența respectivă.

#### 2. Funcționalități Cheie

- Nu oferă funcționalități proprii: este un modul de tranziție (punte) către `l10n_ro_sale_order_report`.
- Pentru instalări noi, se depinde direct de `l10n_ro_sale_order_report`.
- Instalările existente pot dezinstala modulul după ce nimic din addon-urile proprii nu mai depinde de el.

#### 3. Dependențe

- `sale`
- [l10n_ro_sale_order_report](../l10n_ro_sale_order_report/index.md)

#### 4. Componente Cheie

**Modele**

- Niciun model (modulul nu are cod Python).

**Vizualizări**

- Nicio vizualizare (lista `data` din manifest este goală).

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [l10n_ro_sale_order_report](../l10n_ro_sale_order_report/index.md): modulul care a preluat raportul comenzii de vânzare.
