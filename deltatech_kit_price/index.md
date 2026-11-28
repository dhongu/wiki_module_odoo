# Kit Price on Sale Orders (localizat la `deltatech_kit_price/index.md`)

- **Nume Tehnic:** `deltatech_kit_price`
- **Versiune:** `20.0.0.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_kit_price
- **Cale Locală:** `odoo-addons/deltatech/deltatech_kit_price`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul calculează automat prețul de cost al produselor de tip „kit" direct pe liniile comenzii de vânzare. Este util companiilor care vând produse compuse din mai multe componente și au nevoie de o marjă calculată pe baza costurilor reale ale componentelor, nu a unui cost static sau introdus manual pe produsul-kit.

#### 2. Funcționalități Cheie

- Calculează costul liniei de comandă când produsul are o listă de materiale (BoM) de tip **Kit**, însumând costurile componentelor.
- Marja de vânzare se bazează pe costul real al componentelor, nu pe costul de pe produsul-kit.
- Mod de lucru: se configurează BoM-ul de tip Kit, se definește costul componentelor, apoi se adaugă kitul pe comanda de vânzare; costul și marja apar pe linie. Fluxul detaliat este în fișa consultant.
- Integrare cu modulele Odoo de vânzări, producție (BoM) și marjă.

#### 3. Dependențe

- `sale_margin`
- `mrp`
- `mrp_account`: furnizează `product.product._compute_bom_price`; este `auto_install`, așa că este declarat explicit.

#### 4. Componente Cheie

**Modele**

- `sale.order.line` (extins, `models/sale_order_line.py`): suprascrie `_compute_purchase_price()` pentru produsele cu BoM phantom; metoda `get_available_phantom_bom_id()` poate fi suprascrisă de alte module pentru alegerea BoM-ului.

#### 5. Conexiuni

- [deltatech_sale_margin](../deltatech_sale_margin/index.md): folosește același câmp `purchase_price` al liniei pentru verificările de vânzare sub preț și afișarea marjei.
- `mrp`, `mrp_account`, `sale_margin`: sursa BoM-urilor, a costului agregat și a câmpurilor de marjă.
