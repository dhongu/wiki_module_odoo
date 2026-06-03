# RAL (localizat la `deltatech_ral/index.md`)

- **Nume Tehnic:** `deltatech_ral`
- **Versiune:** `19.0.1.0.3`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_ral`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_ral`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul gestionează folosirea pigmenților de culoare RAL (coduri de culoare RAL) în comenzile de producție. Pe baza atributului de culoare al produsului fabricat, modulul determină automat pigmentul RAL corespunzător și înlocuiește componenta generică „dummy" din rețeta de fabricație (BOM) cu pigmentul real. Astfel, o singură rețetă poate fi folosită pentru toate variantele de culoare ale unui produs, iar lotul rezultat din producție este marcat automat cu pigmentul utilizat. Valoarea de afaceri principală este eliminarea rețetelor duplicate per culoare și trasabilitatea pigmentului pe lotul produs.

#### 2. Funcționalități Cheie

- Permite selectarea unui pigment (RAL) într-o comandă de producție.
- Pigmentul este un material al cărui cod intern începe cu „RAL".
- Dacă în BOM este folosit pigmentul „RAL 0000" (dummy), acesta este înlocuit cu pigmentul din comanda de producție.
- Lotul este creat automat la confirmarea comenzii și primește pigmentul din comanda de producție.

Instrucțiuni de configurare:

- Se creează produsul „Dummy RAL" cu referința internă „RAL 0000".
- În BOM-ul produsului care folosește pigmenți, „Dummy RAL" se setează ca și componentă (FĂRĂ a selecta o variantă).
- Produsul final trebuie să aibă un atribut de tip culoare.
- Se creează produsele pigment cu referința internă „RAL color", unde „color" se înlocuiește cu numele opțiunii din atributul produsului final (ex.: RAL White, RAL Rose etc.).
- La crearea comenzii de producție pentru o variantă, produsul „Dummy RAL" este înlocuit cu pigmentul RAL corespunzător.

#### 3. Dependențe

- `base`
- `stock`
- `mrp`

#### 4. Componente Cheie

**Modele**

- `mrp.production` (extins): adaugă câmpul `ral_id` (Many2one către `product.product`, domeniu pe coduri ce încep cu „RAL"). Determină automat pigmentul din atributul de culoare al produsului și înlocuiește componenta „RAL 0000" din mișcările de materii prime cu pigmentul ales; propagă pigmentul pe loturile generate.
- `stock.lot` (extins): adaugă câmpul `ral_id` (Many2one către `product.product`), pentru a marca lotul produs cu pigmentul RAL utilizat.

**Vizualizări**

- `views/mrp_view.xml`: extinde formularul comenzii de producție pentru afișarea câmpului RAL.
- `views/stock_view.xml`: extinde vizualizarea lotului (`stock.lot`) pentru afișarea pigmentului RAL.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server. Logica rulează prin metode `onchange`/`create`/`_generate_moves` pe `mrp.production`.

#### 5. Conexiuni

- [deltatech_mrp](../deltatech_mrp/index.md): suita de extensii pentru producție din ecosistemul deltatech, complementară gestiunii pigmenților RAL.
