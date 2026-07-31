# Deltatech Website Product Placeholder (localizat la `deltatech_website_product_placeholder/index.md`)

- **Nume Tehnic:** `deltatech_website_product_placeholder`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_product_placeholder
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_product_placeholder`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul permite configurarea unei imagini de rezervă (placeholder) pentru produsele care nu au o poză încărcată în magazinul online. În loc ca Odoo să genereze dinamic o imagine implicită pentru fiecare produs fără poză, modulul servește o singură imagine statică sau configurabilă per website, ceea ce reduce încărcarea serverului și îmbunătățește cache-ul din browser și CDN. Rezultatul este un site mai rapid și o experiență vizuală mai consistentă pentru produsele fără fotografie.

#### 2. Funcționalități Cheie

- Imagine de placeholder configurabilă per website (din Setări > Website).
- Revenire (fallback) automată la o imagine statică implicită dacă nu este configurată una personalizată.
- Convertor QWeb de imagine optimizat, care folosește direct URL-ul placeholder-ului în HTML, fără generare dinamică.
- SEO și viteză de încărcare îmbunătățite, prin evitarea procesării imaginilor lipsă la fiecare afișare de pagină.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

- `product.template` / `product.product`: suprascriu `_get_placeholder_filename()` pentru a returna, în lipsa unei imagini proprii, calea către imaginea de placeholder configurată pe website (`website/<id>/product_placeholder_image`) sau, dacă aceasta nu e setată, imaginea statică implicită din modul.
- `website`: adaugă câmpul `product_placeholder_image` (imagine implicită per website, configurabilă din Setări).
- `res.config.settings`: expune câmpul `product_placeholder_image` (legat de `website_id.product_placeholder_image`) în ecranul de setări Website.
- `ir.binary` (model abstract): extinde `_get_placeholder_stream()` pentru a servi conținutul imaginii placeholder a website-ului atunci când calea cerută corespunde formatului `website/<id>/product_placeholder_image`.
- `ir.qweb.field.image` (model abstract): extinde `_get_src_urls()` pentru câmpurile imagine ale produsului (`image_1920`, `image_1024`, `image_512`, `image_256`, `image_128`), astfel încât să genereze direct URL-ul static/placeholder în HTML, fără a mai trece prin generarea dinamică de imagine.

**Vizualizări**

- `res_config_settings_view_form` (extinde `website.res_config_settings_view_form`): adaugă în blocul de setări Website câmpul „Product Placeholder" pentru încărcarea imaginii implicite.

**Acțiuni Automate / Acțiuni Server**

- Nu au fost identificate `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

- `website_sale`: modulul se integrează direct cu magazinul online, înlocuind imaginea implicită de produs afișată pe site.
