# Deltatech Sale Invoice Status (localizat la `deltatech_sale_invoice_status/index.md`)

- **Nume Tehnic:** `deltatech_sale_invoice_status`
- **Versiune:** `19.0.0.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_invoice_status
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_invoice_status`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul corectează statusul de facturare al comenzilor de vânzare atunci când acestea combină produse și servicii: dacă produsele nu au fost încă livrate, linia de comandă nu poate fi facturată separat doar pe baza serviciilor, evitând astfel facturarea prematură a bunurilor nelivrate.

#### 2. Funcționalități Cheie

- Gestionează statusul de facturare al comenzii de vânzare pe baza livrării, pentru produsele consumabile.
- Dacă în linii există atât produse, cât și servicii, iar produsele nu au fost livrate, statusul de facturare rămâne „Nu" pentru linia de produs.
- Dacă în comandă există doar servicii, statusul de facturare este „De facturat".

#### 3. Dependențe

- `sale`
- `delivery`

#### 4. Componente Cheie

**Modele**

- `sale.order.line`: suprascrie `_can_be_invoiced_alone()` astfel încât o linie să poată fi facturată singură doar dacă produsul nu este de tip `service` (pe lângă condițiile standard Odoo).

**Vizualizări**

Nu sunt definite vizualizări noi — modulul intervine exclusiv la nivel de logică de model (Python).

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- `sale`: modulul extinde direct fluxul de facturare al comenzilor de vânzare.
- `delivery`: dependință folosită pentru a determina corect politica de livrare/facturare a liniilor.
