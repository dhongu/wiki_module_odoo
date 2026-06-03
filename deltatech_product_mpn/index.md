# Product MPN (localizat la `deltatech_product_mpn/index.md`)

- **Nume Tehnic:** `deltatech_product_mpn`
- **Versiune:** `19.0.0.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_product_mpn
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_mpn`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul adaugă un câmp pentru Codul de Produs al Producătorului (MPN — Manufacturer Part Number) pe șablonul de produs. Acest cod este identificatorul atribuit de producător unei piese sau unui articol și ajută la identificarea precisă a produselor, mai ales atunci când același articol este vândut sub mai multe denumiri sau referințe interne. Câmpul este disponibil și în bara de căutare, astfel încât produsele să poată fi găsite rapid după codul producătorului.

#### 2. Funcționalități Cheie

- Adaugă un câmp MPN (Manufacturer Part Number) pe șablonul de produs.
- Permite căutarea produselor după codul MPN direct din bara de căutare, pentru identificare mai ușoară.

#### 3. Dependențe

- `product`

#### 4. Componente Cheie

Conform prioritizării Readme (`readme/DESCRIPTION.md` prezent), analiza detaliată a componentelor tehnice a fost omisă. La nivel general, modulul extinde modelul `product.template` cu câmpul MPN și adaugă o vizualizare în `views/product_template_view.xml` pentru afișarea și căutarea după acest câmp.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale verificate către alte module cu pagină wiki existentă.
