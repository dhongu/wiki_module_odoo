# Pricelist Bulk Rules (localizat la `deltatech_pricelist_bulk/index.md`)

- **Nume Tehnic:** `deltatech_pricelist_bulk`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_pricelist_bulk
- **Cale Locală:** `odoo-addons/deltatech/deltatech_pricelist_bulk`
- **Ultima Ingestie:** `2026-11-09`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite adăugarea de reguli într-o listă de prețuri pentru mai multe produse deodată și aplicarea aceluiași mod de calcul al prețului pe mai multe reguli existente, în loc să introduci regulile una câte una. Economisește timp la încărcarea și actualizarea prețurilor pentru liste mari de produse.

#### 2. Funcționalități Cheie

- **Adăugare reguli pentru mai multe produse:** butonul **Add Rules** de pe lista de prețuri și acțiunea **Add to Pricelist** pe produsele selectate (listă sau kanban, produse sau variante) deschid un asistent.
- **Aplicare la:** produse, variante de produs sau categorii de produse; lista se poate completa cu toate produsele unor categorii și ale subcategoriilor lor (**Add Products of Categories**).
- **Setări introduse o singură dată:** cantitatea minimă, perioada de valabilitate și modul de calcul al prețului, cu aceleași opțiuni ca la o regulă standard: **Fixed Price**, **Discount** (opțional față de altă listă de prețuri) sau **Formula** (pe baza prețului de vânzare, a costului sau a altei liste, cu discount sau adaos, rotunjire, taxă suplimentară și marje).
- **Tratarea regulilor existente** (același produs, aceeași cantitate minimă și aceeași perioadă): se păstrează, se actualizează sau se adaugă o regulă nouă.
- **Rezultat:** se creează câte o regulă pentru fiecare produs, variantă sau categorie; un mesaj arată câte reguli au fost adăugate, actualizate sau păstrate, iar regulile rezultate se deschid într-o listă.
- **Aplicare formulă pe mai multe reguli:** butonul **Apply Formula** de pe lista de prețuri (toate regulile) sau acțiunea **Apply Formula** pe regulile selectate dintr-o listă de reguli schimbă, deodată, modul de calcul al prețului (valorile celorlalte tipuri de preț se golesc), cantitatea minimă și/sau perioada de valabilitate; ce nu e bifat rămâne neschimbat.
- Cerință: listele de prețuri trebuie activate în *Vânzări > Configurare > Setări*, secțiunea **Pricing**.
- Pașii detaliați și capturile sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `product`

#### 4. Componente Cheie

**Modele**

- `pricelist.bulk.add` (tranzitoriu): asistentul de adăugare a regulilor în masă.
- `pricelist.bulk.formula` (tranzitoriu): asistentul de aplicare a unei formule pe mai multe reguli.
- `pricelist.formula.mixin` (abstract): câmpurile și logica de calcul al prețului, comune celor două asistenți.
- `product.pricelist` și `product.pricelist.item` (extinse): butoanele și acțiunile de lucru în masă.

**Vizualizări**

- `product_pricelist_view_bulk`: adaugă butoanele **Add Rules** și **Apply Formula** în antetul listei de prețuri.
- `pricelist_bulk_add_view_form`: formularul asistentului de adăugare reguli.
- `pricelist_bulk_formula_view_form`: formularul asistentului de aplicare formulă.

**Acțiuni Automate / Acțiuni Server**

- `action_pricelist_bulk_add_template` / `action_pricelist_bulk_add_variant`: acțiuni **Add to Pricelist** pe produse, respectiv variante.
- `action_pricelist_bulk_formula`: acțiune **Apply Formula** pe regulile de preț selectate.
- Nu există acțiuni cron sau automatizări.

#### 5. Conexiuni

- Nicio conexiune funcțională cu alte module ale wiki-ului (modulul depinde doar de `product`).
