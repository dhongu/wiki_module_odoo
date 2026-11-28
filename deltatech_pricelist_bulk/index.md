# Pricelist Bulk Rules (localizat la `deltatech_pricelist_bulk/index.md`)

- **Nume Tehnic:** `deltatech_pricelist_bulk`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_pricelist_bulk
- **Cale Locală:** `odoo-addons/deltatech/deltatech_pricelist_bulk`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite adăugarea de reguli într-o listă de prețuri pentru mai multe produse deodată și aplicarea aceluiași calcul de preț pe mai multe reguli existente, în loc să se introducă regulile una câte una. Economisește timp la întreținerea listelor de prețuri mari.

#### 2. Funcționalități Cheie

- Buton **Add Rules** pe formularul listei de prețuri și acțiunea **Add to Pricelist** pe produsele selectate (listă sau kanban, produse sau variante) deschid un wizard de adăugare în masă.
- Regulile se pot aplica pe **produse**, **variante** sau **categorii de produse**; se pot încărca automat toate produsele unor categorii și ale subcategoriilor lor.
- Se setează o singură dată cantitatea minimă, perioada de valabilitate și calculul prețului, cu aceleași opțiuni ca la o regulă standard: preț fix, discount (pe prețul de vânzare sau pe altă listă) sau adaos (pe prețul de vânzare, cost sau altă listă), cu rotunjire, sumă adăugată și marje.
- Dacă lista are deja o regulă pentru același produs, cantitate minimă și perioadă, se alege între păstrare, actualizare sau adăugarea unei reguli noi.
- La final, un mesaj arată câte reguli au fost adăugate, actualizate sau păstrate, iar regulile rezultate se deschid într-o listă.
- Butonul și acțiunea **Apply Formula** (pe lista de prețuri sau pe regulile selectate) schimbă în masă calculul prețului, cantitatea minimă și/sau perioada de valabilitate; valorile tipului de preț vechi sunt șterse, ca în formularul standard.
- Necesită activarea listelor de prețuri în *Sales > Configuration > Settings* (secțiunea Pricing). Fluxul detaliat este în fișa consultantului.

#### 3. Dependențe

- `product`

#### 4. Componente Cheie

**Modele**

- `pricelist.bulk.add`: wizard pentru adăugarea regulilor în masă.
- `pricelist.bulk.formula`: wizard pentru aplicarea unei formule pe mai multe reguli.
- `pricelist.formula.mixin`: câmpurile comune de calcul al prețului, partajate de cele două wizard-uri.
- `product.pricelist`, `product.pricelist.item`: extinse cu acțiunile de adăugare și de aplicare a formulei.

**Vizualizări**

- `product_pricelist_view_bulk`: butoanele din formularul listei de prețuri.
- `pricelist_bulk_add_view_form`, `pricelist_bulk_formula_view_form`: formularele celor două wizard-uri.

**Acțiuni Automate / Acțiuni Server**

- `action_pricelist_bulk_add`, `action_pricelist_bulk_add_template`, `action_pricelist_bulk_add_variant`, `action_pricelist_bulk_formula`: acțiuni de fereastră care deschid wizard-urile.

#### 5. Conexiuni

- [deltatech_pricelist](../deltatech_pricelist/index.md): alt modul Terrabit pentru liste de prețuri.
