# eCommerce Warehouse Stock (localizat la `deltatech_website_warehouse_stock/index.md`)

- **Nume Tehnic:** `deltatech_website_warehouse_stock`
- **Versiune:** `20.0.0.0.8`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_website_warehouse_stock`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_warehouse_stock`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul afișează pe pagina produsului din website disponibilitatea în stoc pentru fiecare depozit, ca să știe clientul unde găsește produsul înainte de comandă. Complementează funcția standard „Click & Collect” (`website_sale_collect`): starea stocului e vizibilă direct, fără clicuri sau ferestre, iar datele exacte de inventar sunt protejate printr-un prag configurabil.

#### 2. Funcționalități Cheie

- Se afișează stocul locației principale a fiecărui depozit care are bifa de afișare pe site (pe formularul depozitului).
- Stoc negativ sau zero: „Out of stock”; între 0 și prag (implicit 10): cantitatea; peste prag: „Available”. Pragul se setează în setările site-ului.
- Poziție: în detaliile produsului (implicit) sau imediat după preț.
- Stil: insigne (implicit), listă cu pictograme, card sau selector de depozit (clientul alege depozitul și apasă „Check stock”; cantitățile sunt deja în pagină, fără cerere suplimentară).
- Mesaj la stoc zero: „Out of stock” sau „On order”, cu o notă opțională (de exemplu termenul de livrare).
- Afișarea cantității: cantitatea exactă sub prag (implicit) sau doar „In stock”.
- Culori de temă: insigne în culorile paginii, lizibile pe teme închise.
- Opțiunile se setează pe site, în *Website → Configurare → Setări* (Warehouse Stock Design) sau din editorul de website, selectând blocul pe pagina produsului.
- Configurarea, verificările și capturile pentru consultant sunt în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `website`
- `website_sale_stock`

#### 4. Componente Cheie

Secțiune omisă: `readme/DESCRIPTION.md` este prezent și nu solicită explicit analiza codului pentru componente.

#### 5. Conexiuni

- `website_sale_collect`: funcția standard Odoo „Click & Collect” (selector pe hartă, punct de ridicare), completată de acest modul cu afișarea informativă a stocului pe depozite.
