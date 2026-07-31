# Deltatech Kit Price (localizat la `deltatech_kit_price/index.md`)

- **Nume Tehnic:** `deltatech_kit_price`
- **Versiune:** `19.0.0.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_kit_price
- **Cale Locală:** `odoo-addons/deltatech/deltatech_kit_price`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul calculează automat prețul de cost al produselor de tip „kit" direct pe liniile comenzii de vânzare. Este util pentru companiile care vând produse compuse din mai multe componente (seturi/kituri) și care au nevoie de o marjă calculată corect, pe baza costurilor reale ale componentelor, nu a unui cost static sau introdus manual pe produsul-kit.

#### 2. Funcționalități Cheie

- Calculează automat costul unui produs pe linia comenzii de vânzare atunci când acesta este configurat ca **Kit** printr-o Listă de Materiale (BoM) de tip phantom.
- Parcurge toate componentele kitului și însumează costurile individuale ale acestora într-un cost total pentru linia comenzii.
- Asigură calculul marjelor de vânzare pe baza costurilor reale ale componentelor, nu a unui cost static/manual introdus pe produsul-kit, oferind o imagine financiară mai corectă echipelor de vânzări și managementului.
- Se integrează nativ cu modulele Odoo de **Vânzări**, **Producție (BoM)** și **Marjă**.

#### 3. Dependențe

- `sale_margin`
- `mrp`

#### 4. Componente Cheie

`readme/DESCRIPTION.md` acoperă scopul și funcționalitățile de bază ale modulului (secțiunile 1 și 2). Deoarece descrierea face referire explicită la mecanismul de calcul al costului kitului pe baza componentelor din BoM, se notează mai jos componenta tehnică ce implementează acest calcul.

**Modele**

- `sale.order.line` (extins): suprascrie `_compute_purchase_price()` — dacă produsul liniei este de tip consumabil (`type="consu"`) și are BoM-uri asociate, identifică prima listă de materiale de tip phantom (kit) prin metoda `get_available_phantom_bom_id()`, calculează costul agregat al componentelor cu `product_id._compute_bom_price()`, convertește rezultatul la unitatea de măsură și moneda liniei, apoi îl scrie în câmpul `purchase_price` al liniei.
- Metoda `get_available_phantom_bom_id()` este publică și explicit gândită pentru a fi suprascrisă de alte module care au nevoie de o logică personalizată de identificare a BoM-ului phantom.

#### 5. Conexiuni

- [deltatech_sale_margin](../deltatech_sale_margin/index.md): folosește același câmp `purchase_price` de pe `sale.order.line` (calculat aici pentru produsele-kit) pentru verificările de vânzare sub prețul de achiziție și pentru afișarea/blocarea marjei.
- `mrp` (`mrp.bom`): sursa listelor de materiale de tip phantom folosite pentru identificarea componentelor kitului și calculul costului agregat.
- `sale_margin`: modulul de bază Odoo extins, care introduce câmpurile de marjă și cost de achiziție pe comanda de vânzare.
