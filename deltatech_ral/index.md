# RAL Pigments (localizat la `deltatech_ral/index.md`)

- **Nume Tehnic:** `deltatech_ral`
- **Versiune:** `19.0.1.0.8`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_ral
- **Cale Locală:** odoo-addons/deltatech/deltatech_ral
- **Ultima Ingestie:** `2026-11-19`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Producătorii care vopsesc același produs în mai multe culori RAL ar avea nevoie, fără acest modul, de o rețetă de fabricație (BOM) separată pentru fiecare culoare, diferite doar prin pigment. Cu modulul, o singură rețetă folosește un pigment generic, pe care fiecare comandă de producție îl înlocuiește cu pigmentul real al culorii produse. Culoarea este păstrată și pe lotul produsului finit, ceea ce oferă trasabilitatea pigmentului. Valoarea de afaceri principală este eliminarea rețetelor duplicate per culoare.

#### 2. Funcționalități Cheie

- **Pigment pe comanda de producție:** câmpul **RAL** conține pigmentul folosit. La crearea comenzii, pigmentul se alege din culoarea variantei produsului: valoarea atributului cu tipul de afișare *Color* indică pigmentul a cărui referință internă conține `RAL <valoare>`. Planificatorul îl poate schimba cât timp comanda e în ciornă sau confirmată.
- **Pigment generic înlocuit în componente:** componenta provenită din linia de BOM cu pigmentul generic (referința internă `RAL 0000`) este înlocuită cu pigmentul din câmpul **RAL**, cu aceeași cantitate. Înlocuirea se păstrează la recalcularea componentelor (de exemplu la schimbarea cantității de produs), deci se consumă stocul pigmentului real.
- **RAL pe lot:** loturile și numerele de serie au câmpul **RAL**, afișat pe formular și în listă. Când Odoo generează lotul produsului finit pentru comandă (butonul **Generate Lot** / **Generate Serial**, sau lotul creat la producerea comenzii fără lot), pigmentul comenzii se scrie pe acel lot.
- **Configurare:**
  - produsul generic cu referința internă `RAL 0000` și pigmenții reali, cu referința `RAL ` urmată de numele valorii de culoare (ex. `RAL White` pentru valoarea *White*);
  - un atribut de culoare cu tipul de afișare *Color* (Inventar → Configurare → Produse → Atribute, cu variantele de produs activate), adăugat pe produsul finit;
  - în BOM-ul șablonului produsului finit (fără variantă) se adaugă `RAL 0000` ca componentă;
  - pentru a păstra culoarea pe lot, produsul finit se urmărește pe loturi sau numere de serie.
- **Limitări:** pigmentul se potrivește printr-o căutare parțială pe referința internă, deci referințele care se conțin una pe alta (`RAL White` și `RAL White Matt`) pot da pigmentul greșit — referințele trebuie să rămână distincte; câmpul **RAL** se scrie doar pe loturile generate de Odoo pentru comandă, nu pe cele introduse sau selectate manual.

#### 3. Dependențe

- `base`
- `stock`
- `mrp`

#### 4. Componente Cheie

**Modele**

- `mrp.production` (extins): adaugă câmpul `ral_id` (Many2one către `product.product`, domeniu pe coduri ce încep cu „RAL"). La schimbarea produsului (`_onchange_product_id`) determină pigmentul din atributul de culoare al variantei; la `create` și la selectarea pigmentului (`onchange_ral_id`) înlocuiește componenta „RAL 0000" din materiile prime. Substituția este reafirmată și în `_get_move_raw_values`, deoarece `move_raw_ids` este câmp calculat în Odoo 19 și componentele sunt regenerate din liniile de BOM la fiecare recalculare. La `action_generate_serial` propagă pigmentul pe loturile produse (`lot_producing_ids`).
- `stock.lot` (extins): adaugă câmpul `ral_id` (Many2one către `product.product`, indexat), pentru a marca lotul produs cu pigmentul RAL utilizat.

**Vizualizări**

- `deltatech_ral_mrp_production_form_view` (`views/mrp_view.xml`): afișează câmpul RAL sub produs pe comanda de producție, editabil doar în stările ciornă și confirmat.
- `views/stock_view.xml`: extinde vizualizările lotului (`stock.lot`) pentru afișarea pigmentului RAL.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server. Logica rulează prin metode `onchange`/`create`/`_get_move_raw_values` pe `mrp.production`.

#### 5. Conexiuni

- [deltatech_mrp](../deltatech_mrp/index.md): suita de extensii pentru producție din ecosistemul deltatech, complementară gestiunii pigmenților RAL.
