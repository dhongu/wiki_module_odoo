# Vendor Products Granit (localizat la `deltatech_vendor_products_granit/index.md`)

- **Nume Tehnic:** `deltatech_vendor_products_granit`
- **Versiune:** `20.0.1.0.6`
- **Cale:** https://github.com/terrabit-solutions/bitshop_vendor/tree/20.0/deltatech_vendor_products_granit
- **Cale Locală:** `odoo-addons/bitshop_vendor/deltatech_vendor_products_granit`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul conectează catalogul de produse al furnizorilor la magazinul online Granit Parts (granit-parts.ro), astfel încât prețurile și disponibilitatea Granit pot fi verificate direct din Odoo, fără copiere manuală. Căutarea unui cod de articol interoghează Granit în timp real și întoarce prețul de listă, prețul de achiziție și cantitatea disponibilă.

#### 2. Funcționalități Cheie

- **Verificare de preț la cerere:** când un flux de furnizor de tip Granit are căutarea online activată, codul de articol căutat este interogat la Granit în momentul în care ai nevoie de el.
- **Disponibilitate la vedere:** vezi cantitatea disponibilă la Granit înainte de a promite un termen de livrare.
- **Mai puține erori de tastare:** codurile și prețurile vin direct de la Granit.
- Articolele marcate de Granit ca neonorabile sunt excluse din rezultate.
- **Limitări:** conectorul caută un singur cod de articol o dată; nu importă catalogul Granit, nu creează variante, iar butoanele „Load Price” de pe flux nu actualizează prețurile pentru acest tip de conexiune.
- Fluxul pas-cu-pas (flux de furnizor, căutare în shop, pagina produsului, catalog, produs generat) este în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_vendor_products_website](../deltatech_vendor_products_website/index.md)

#### 4. Componente Cheie

Documentația se bazează pe `readme/DESCRIPTION.md`, care nu detaliază componente tehnice individuale; analiza codului este omisă conform schemei.

**Modele**

- `vendor.feed` (extins): adaugă tipul de conexiune `granit` și câmpurile de autentificare (token, expirare, JWT), vizibile doar administratorilor.

#### 5. Conexiuni

- [deltatech_vendor_products_website](../deltatech_vendor_products_website/index.md): căutarea online în shop pe care conectorul Granit o folosește pentru a interoga furnizorul.
- [deltatech_vendor_products](../deltatech_vendor_products/index.md): catalogul de produse furnizor (`vendor.feed`, `vendor.product`) extins de conector.
