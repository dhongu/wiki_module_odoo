# Câmp Marcă Produs (Deltatech Brand Field) (localizat la `deltatech_brand_field/index.md`)

- **Nume Tehnic:** `deltatech_brand_field`
- **Versiune:** `19.0.0.0.6`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_brand_field
- **Cale Locală:** `odoo-addons/bitshop/deltatech_brand_field`
- **Ultima Ingestie:** `2026-10-31`

#### 1. Sumar

Acest modul oferă un mecanism centralizat pentru gestionarea mărcilor de produse în mai multe module Odoo, asigurând că toate informațiile legate de marcă sunt stocate într-un câmp dedicat, consecvent. Din perspectivă de business, modulul rezolvă complexitatea generată de faptul că diverse module își definesc propriile câmpuri de marcă, creând un sistem unificat și ușor de căutat pentru marca produselor, valabil pentru toate funcțiile integrate.

#### 2. Funcționalități Cheie

- **Identitate de marcă unificată:** consolidează informațiile despre marcă într-un singur câmp standardizat, valabil în toate modulele și procesele Odoo relevante.
- **Consecvență îmbunătățită a datelor:** asigură uniformitatea datelor de marcă în întregul sistem, ducând la raportări și filtrări mai precise.
- **Catalogare îmbunătățită a produselor:** construiește o bază de date de produse mai structurată și profesională, ușor de gestionat și de navigat după marcă.
- **Aliniere strategică a mărcii:** folosește un câmp de marcă consecvent pentru a sprijini strategii mai eficiente de marketing, vânzări și inventar.
- **Gestionare scalabilă:** permite administrarea cu ușurință a unui număr mare de mărci de produse dintr-o locație centrală, facilitând extinderea catalogului.
- **Câmp de marcă configurabil:** în setările Website se alege câmpul de produs folosit ca marcă (parametrul de sistem `product.brand_field`); poate fi atât un câmp Many2one, cât și Char/Text.
- **Marcă goală tratată corect:** dacă marca nu este completată pe produs (Char/Text sau Many2one), rezultatul este un șir gol, iar feed-urile de produse nu mai răspund cu eroare HTTP 500 (corecție din versiunea `19.0.0.0.6`).

#### 3. Dependențe

- `website_sale_stock`

#### 4. Componente Cheie

*Sumarul și Funcționalitățile Cheie provin din `readme/DESCRIPTION.md`, iar `readme/HISTORY.md` a fost folosit doar pentru corecția din ultima versiune; analiza detaliată a componentelor nu este cerută de readme. Mai jos sunt doar reperele confirmate în cod.*

**Modele**

- `product.template` (extins): câmpul calculat `brand_name` și metoda `get_brand_name(brand_field=None)`, care citește marca din câmpul configurat.
- `product.product` (extins): `get_brand_name`, delegat către șablonul de produs.
- `res.config.settings` (extins): câmpul `brand_field` (parametrul `product.brand_field`) și `module_deltatech_brand_field`.

**Vizualizări**

- `res_config_settings_view_form`: moștenește formularul de setări Website și adaugă câmpul „Brand Field” după setarea de disponibilitate a produselor.

#### 5. Conexiuni

- [deltatech_feed](../deltatech_feed/index.md): depinde de acest modul și folosește marca produsului în feed-urile de produse.
