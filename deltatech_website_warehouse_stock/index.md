# eCommerce Warehouse Stock (localizat la `deltatech_website_warehouse_stock/index.md`)

- **Nume Tehnic:** `deltatech_website_warehouse_stock`
- **Versiune:** `19.0.0.0.7`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_warehouse_stock
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_warehouse_stock`
- **Ultima Ingestie:** `2026-11-02`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul afișează pe pagina produsului din magazinul online disponibilitatea în stoc a fiecărui depozit. Clienții văd dintr-o privire dacă un produs este în stoc, are stoc redus sau este indisponibil la anumite locații, ceea ce îi ajută să decidă mai ușor. Spre deosebire de funcția standard „Click & Collect" din Odoo 18/19 (selector pe hartă), starea stocului este afișată direct pe pagină, fără clicuri sau ferestre suplimentare, iar cantitățile exacte mari sunt protejate printr-un prag configurabil. Aspectul blocului se alege per site, din setări sau din editorul de website.

#### 2. Funcționalități Cheie

- **Stoc pe depozit pe pagina produsului**: pentru fiecare depozit bifat, se afișează stocul locației principale; numele depozitului este cel din formularul depozitului. Pe fiecare depozit există bifa **Afișare pe site** (activă implicit, inclusiv pe depozitele noi); se iau în calcul doar depozitele companiei site-ului.
- **Cantitate calculată**: stocul disponibil din locația de stoc principală minus ieșirile planificate (confirmate, dar nevalidate).
- **Prag configurabil**: peste prag (implicit 10, unic pe bază, în setările site-ului) se afișează „Disponibil", fără cantitatea exactă; între 0 și prag, inclusiv, se afișează cantitatea; la 0 sau negativ, „Stoc epuizat" sau „La comandă".
- **Opțiuni de aspect, per site** (*Website > Configuration > Settings*, grupul *Warehouse Stock Design*, sau din editorul de website, cu clic pe blocul din pagina produsului):
  - **Poziție**: în detaliile produsului (implicit) sau imediat după preț;
  - **Stil**: etichete (implicit), listă cu pictograme, card sau selector de depozit (clientul alege depozitul și apasă „Verifică stocul"; cantitățile sunt deja în pagină, fără cerere suplimentară la server);
  - **Mesaj la stoc zero**: „Stoc epuizat" (implicit) sau „La comandă", opțional urmat de o notă scurtă (de exemplu termenul de livrare; nota se completează doar din setări);
  - **Afișarea cantității**: cantitatea exactă sub prag (implicit) sau doar „În stoc";
  - **Culorile temei**: etichete nuanțate pe culorile paginii, lizibile pe teme întunecate, în loc de verde, gri și roșu pline.
- **Addon informativ complementar**: completează funcția standard „Click & Collect" (`website_sale_collect`), care alege punctul de ridicare abia la finalizarea comenzii. Stocul afișat este orientativ (calculat la încărcarea paginii), nu o rezervare.
- Fluxul pas-cu-pas, verificările și erorile frecvente sunt în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `website`
- `website_sale_stock`

#### 4. Componente Cheie

**Modele**

- `stock.warehouse`: extins cu bifa `website_stock_display` (Afișare pe site), activă implicit.
- `website`: extins cu opțiunile de aspect ale stocului (`warehouse_stock_position`, `warehouse_stock_style`, `warehouse_stock_zero_message`, `warehouse_stock_zero_note`, `warehouse_stock_qty_display`, `warehouse_stock_theme_colors`) și cu metoda prin care editorul de website scrie opțiunile, cu valoarea validată.
- `product.template`: metoda `get_warehouse_stock_distribution` calculează câte o linie pe depozit (text, culoarea etichetei, stare, mesajul selectorului), în funcție de prag și de opțiunile site-ului.
- `res.config.settings`: expune pragul (parametrul de sistem `deltatech_website_warehouse_stock.threshold`) și opțiunile de aspect ale site-ului selectat.

**Vizualizări**

- `res_config_settings_view_form`: adaugă pragul și grupul de aspect al stocului în setările site-ului, lângă setările de stoc ale magazinului.
- `view_warehouse_inherit`: adaugă bifa **Afișare pe site** pe formularul depozitului.
- `warehouse_stock_block`, `warehouse_stock_badge`, `warehouse_stock_note`: șabloane QWeb care afișează blocul de stoc pe pagina produsului, în cele patru stiluri.
- `cta_wrapper_warehouse_stock`: plasează blocul sub caseta cu prețul, când stilul de cumpărare este „în cutie".
- Asset-uri website: interacțiunea `WarehouseStockSelector` (selectorul de depozit din frontend), stilurile `warehouse_stock.scss` și opțiunile din editorul de website (secțiunea **Stoc pe depozite**).

**Acțiuni Automate / Acțiuni Server**

- Nu există acțiuni `ir.cron`, `base.automation` sau `ir.actions.server` definite în acest modul.

#### 5. Conexiuni

- `website_sale_collect`: funcția standard Odoo 18/19 „Click & Collect" (selector pe hartă, alegere punct de ridicare), pe care acest modul o completează cu afișarea informativă a stocului pe depozite, direct pe pagina produsului.
