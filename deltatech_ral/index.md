# RAL Pigments (localizat la `deltatech_ral/index.md`)

- **Nume Tehnic:** `deltatech_ral`
- **Versiune:** `20.0.1.0.8`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_ral`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_ral`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Producătorii care vopsesc același produs în multe culori RAL ar avea nevoie, fără acest modul, de câte o listă de materiale (BOM) pentru fiecare culoare, diferite doar prin pigment. Cu modulul, o singură BOM folosește un pigment generic, iar fiecare comandă de producție îl înlocuiește cu pigmentul real al culorii produse. Culoarea este păstrată și pe lotul produsului finit, pentru trasabilitate.

#### 2. Funcționalități Cheie

- **Pigment pe comanda de producție:** câmpul **RAL** conține pigmentul folosit. La crearea comenzii, pigmentul este ales din culoarea variantei de produs: valoarea atributului cu tipul de afișare *Color* indică pigmentul a cărui referință internă conține `RAL <valoare>`. Planificatorul îl poate schimba cât comanda este în ciornă sau confirmată.
- **Pigment generic înlocuit în componente:** componenta provenită din linia de BOM cu pigmentul generic (referința internă `RAL 0000`) este înlocuită cu pigmentul din câmpul **RAL**, cu aceeași cantitate. Înlocuirea se păstrează la recalcularea componentelor (ex. la schimbarea cantității de produs), deci se consumă stocul pigmentului real.
- **RAL pe lot:** loturile și numerele de serie au câmpul **RAL**, afișat în formular și listă. Când Odoo generează lotul produsului finit (butoanele **Generate Lot** / **Generate Serial** sau lotul creat la producție fără lot), pigmentul comenzii se scrie pe acel lot.
- **Configurare:**
  - se creează pigmentul generic cu referința `RAL 0000` și pigmenții reali cu referința `RAL ` urmată de numele valorii de culoare (ex. `RAL White`);
  - se creează un atribut de tip *Color* în **Inventar > Configurare > Produse > Atribute** (cu variantele activate) și se adaugă produsului finit;
  - în BOM-ul produsului (pe șablon, fără variantă) se adaugă `RAL 0000` ca componentă;
  - pentru a păstra culoarea pe lot, produsul finit se urmărește pe loturi sau serii.
- **Limitări:** pigmentul se potrivește printr-o căutare parțială pe referința internă, deci referințe care se conțin una pe alta (`RAL White` și `RAL White Matt`) pot da pigmentul greșit; câmpul **RAL** se scrie doar pe loturile generate de Odoo pentru comandă, nu și pe cele introduse manual.

#### 3. Dependențe

- `base`
- `stock`
- `mrp`

#### 4. Componente Cheie

**Modele**

- `mrp.production` (extins): câmpul `ral_id` (Many2one către `product.product`, domeniu pe coduri care încep cu „RAL"); determinarea pigmentului la schimbarea produsului, înlocuirea componentei `RAL 0000` la `create`, la `onchange_ral_id` și în `_get_move_raw_values` (componentele sunt recalculate din BOM); propagarea pigmentului pe loturi în `action_generate_serial`.
- `stock.lot` (extins): câmpul `ral_id` pentru pigmentul RAL folosit.

**Vizualizări**

- `views/mrp_view.xml`: câmpul RAL pe formularul comenzii de producție.
- `views/stock_view.xml`: câmpul RAL pe formularul și lista lotului.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate sau server; logica rulează prin `onchange`, `create` și `_get_move_raw_values`.

#### 5. Conexiuni

- [deltatech_mrp](../deltatech_mrp/index.md): suita de extensii pentru producție din ecosistemul deltatech, complementară gestiunii pigmenților RAL.
