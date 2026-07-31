# Terrabit Google Tag Manager (localizat la `terrabit_google_tag/index.md`)

- **Nume Tehnic:** `terrabit_google_tag`
- **Versiune:** `19.0.0.1.0`
- **Cale:** [https://github.com/terrabit-solutions/bitshop/tree/19.0/terrabit_google_tag](https://github.com/terrabit-solutions/bitshop/tree/19.0/terrabit_google_tag)
- **Cale Locală:** `odoo-addons/bitshop/terrabit_google_tag`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul integrează Google Tag Manager (GTM) cu magazinul online Odoo, permițând urmărirea evenimentelor de comerț electronic (vizualizare produs, adăugare în coș, început de checkout, plată, căutare, contact, formular, achiziție finală) direct în `window.dataLayer`, fără personalizări suplimentare de cod. Astfel, echipele de marketing pot construi rapoarte și campanii de conversie în Google Ads/Analytics folosind un singur container GTM, configurabil direct din setările website-ului.

#### 2. Funcționalități Cheie

- Injectează automat scriptul GTM (și fallback-ul `<noscript>`) în `<head>`-ul fiecărei pagini, pe baza unui ID de container (`Tracking ID`) configurat în Website → Configurare → Setări.
- Trimite către `dataLayer` evenimentele standard de comerț electronic: `view_item`, `add_to_cart`, `begin_checkout`, `add_payment_info`, `search`, `contact`, `generate_lead` și `purchase`.
- Fiecare eveniment de produs conține detalii bogate (`item_id`, `item_name`, `item_brand`, `item_category`, `price`, `quantity`), cu `item_id` configurabil (variantă / șablon / SKU) prin `terrabit_website_sale_tracking_base`.
- Suportă opțional un `Cod de Conversie` Google Ads — la finalizarea comenzii trimite și un eveniment `conversion` cu `send_to` setat pe eticheta de conversie.
- Păstrează formatul (plat) al evenimentelor identic cu versiunea Odoo 18, astfel încât trigger-ele existente din containerul GTM continuă să funcționeze după upgrade.
- Se bazează pe evenimentele native `website_sale` (`view_item_event`, `add_to_cart_event`) și pe evenimentele normalizate din `terrabit_website_sale_tracking_base`, evitând astfel duplicarea logicii de tracking pentru fiecare pixel de marketing.

#### 3. Dependențe

- `website_sale`
- [terrabit_website_sale_tracking_base](../terrabit_website_sale_tracking_base/index.md)
- [deltatech_brand_field](../deltatech_brand_field/index.md)

#### 4. Componente Cheie

**Modele**

- `website`: extins cu `google_tag_code` (ID container GTM) și `google_conversion_code` (etichetă de conversie Google Ads).
- `res.config.settings`: extins cu câmpuri legate (`related`) către `website_id.google_tag_code` / `google_conversion_code`, plus câmpul calculat `has_google_tag` (comutator on/off în setări, care golește codul GTM la dezactivare).

**Vizualizări**

- `res_config_settings_views.xml`: adaugă în Website → Configurare → Setări secțiunea "Google Tag Manager" cu comutatorul `has_google_tag`, câmpul `Tracking ID` și câmpul opțional `Conversion Code`.
- `website_templates.xml`: șabloane QWeb `google_tag_manager` (injectează scriptul GTM și fallback-ul `<noscript>` înainte de `#wrapwrap`), `confirmation` (adaugă `data-google_conversion_code` pe pagina de confirmare comandă, folosit pentru evenimentul de conversie) și `product` (adaugă un `<span itemprop="category">` ascuns pe pagina produsului, pentru ca tracking-ul să poată citi categoria).

**Acțiuni Automate / Acțiuni Server**

- Nu există `ir.cron`, `base.automation` sau `ir.actions.server` definite în acest modul; tracking-ul este condus integral din partea de frontend, printr-o `Interaction` JS (`google_tag_manager.esm.js`) care ascultă evenimentele DOM și le retrimite către `dataLayer`.

#### 5. Conexiuni

- [terrabit_website_sale_tracking_base](../terrabit_website_sale_tracking_base/index.md): furnizează infrastructura comună de tracking (evenimente normalizate, `tracking_item_id_type`, opțiunea "exclude delivery") pe care acest modul o consumă direct.
- [deltatech_brand_field](../deltatech_brand_field/index.md): furnizează câmpul de brand al produsului, folosit la popularea `item_brand` în evenimentele trimise către `dataLayer`.
- [terrabit_facebook_pixel](../terrabit_facebook_pixel/index.md): pixel similar structurat pe aceeași arhitectură de `Interaction` frontend (menționat explicit ca model de referință în documentația modulului).
- `website_sale`: sursa evenimentelor native de comerț electronic (`view_item_event`, `add_to_cart_event`) pe care modulul le redirecționează către GTM; nu are încă pagină wiki proprie.
