# Replenish Vendor (Compatibility) (localizat la `deltatech_replenish/index.md`)

- **Nume Tehnic:** `deltatech_replenish`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_replenish
- **Cale Locală:** `odoo-addons/deltatech/deltatech_replenish`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modul de compatibilitate: alegerea furnizorului în wizard-ul de reaprovizionare este acum funcționalitate standard Odoo (`purchase_stock`). Modulul rămâne doar ca substituent pentru bazele de date migrate din 18.0, unde funcția era oferită de Deltatech, și nu adaugă modele, vizualizări sau date.

#### 2. Funcționalități Cheie

Funcționalități oferite acum de Odoo standard:

- Câmpul **Supplier/Vendor** în wizard-ul de reaprovizionare (`product.replenish`), afișat când ruta cumpără produsul.
- Alegerea unui furnizor anume din lista furnizorilor produsului, transmis procurement-ului ca `procurement_partner`.
- Furnizorul ales este folosit la crearea comenzii de achiziție, iar termenul lui de livrare intră în data programată.
- Utilizare: în produs, butonul **Replenish**, alegerea unei rute de cumpărare, apoi a furnizorului.

#### 3. Dependențe

- `purchase_stock`

#### 4. Componente Cheie

**Modele**

- Niciunul.

**Vizualizări**

- Niciuna.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_replenishment_explain](../deltatech_replenishment_explain/index.md): alt modul Terrabit pentru reaprovizionare (legătură doar tematică).
