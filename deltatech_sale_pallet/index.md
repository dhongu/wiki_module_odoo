# Paleți pe comenzi de vânzare (localizat la `deltatech_sale_pallet/index.md`)

- **Nume Tehnic:** `deltatech_sale_pallet`
- **Versiune:** `19.0.1.0.9`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_pallet`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_pallet`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul adaugă automat paleți pe comenzile de vânzare și pe facturi. Atunci când un produs care necesită paletizare atinge o cantitate minimă configurată, sistemul introduce automat în comandă produsul de tip palet și ajustează numărul de paleți necesari pe măsură ce cantitatea trece de fiecare multiplu al cantității minime. Astfel, vânzarea reflectă corect ambalarea pe paleți, fără ca operatorul să adauge manual liniile de palet.

#### 2. Funcționalități Cheie

- Definirea unei categorii de produs cu opțiunea „Palet" activată.
- Selectarea produsului de tip palet și încadrarea lui în categoria de mai sus.
- Configurarea unei cantități minime pentru un palet.
- Adăugarea automată a produsului palet pe comanda de vânzare în momentul în care un produs care necesită paleți atinge cantitatea minimă pentru un palet.
- Creșterea automată a cantității de paleți necesari pe măsură ce se atinge următorul multiplu al cantității minime pentru un palet.

#### 3. Dependențe

- `sale_margin`
- `account`
- `stock`

#### 4. Componente Cheie

*Sumarul și funcționalitățile au fost preluate din `readme/DESCRIPTION.md`; analiza detaliată a codului pentru această secțiune nu a fost solicitată explicit în Readme. Componentele de mai jos sunt menționate orientativ, pe baza structurii modulului.*

**Modele**

- `product.category`: extins pentru opțiunea de palet la nivel de categorie.
- `product.template`: extins pentru configurarea produsului ca palet și a cantității minime pentru un palet (`pallet_product_id`, `pallet_qty_min`).
- `sale.order` / `sale.order.line`: recalculează liniile de palet la modificarea comenzii (`onchange_order_line`, `recompute_pallet_lines`, `compute_pallet_number`), adăugând sau ajustând automat linia de palet.
- `account.move`: tratarea paleților la nivel de factură.
- `sale.report`: extinderea raportării de vânzări.

**Vizualizări**

- `views/product_view.xml`: interfața de configurare a categoriei și produsului de tip palet.
- `views/invoice_view.xml`: ajustări de afișare a paleților pe factură.

#### 5. Conexiuni

- `sale_margin`: bază pentru gestionarea liniilor de comandă de vânzare extinse de acest modul.
- `account`: tratarea paleților la nivel de factură.
- `stock`: folosit de teste pentru actualizarea cantităților disponibile (`stock.quant._update_available_quantity`); dependență adăugată explicit în 19.0.1.0.9 (era adusă anterior indirect de alte module instalate).
