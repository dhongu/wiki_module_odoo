# Website City (localizat la `deltatech_website_city/index.md`)

- **Nume Tehnic:** `deltatech_website_city`
- **Versiune:** `19.0.1.2.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_city`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_city`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul îmbunătățește gestionarea adreselor în zonele de eCommerce și Portal din Odoo, oferind o selecție structurată a orașelor. În loc de a introduce numele orașului ca text liber, clientul îl alege dintr-o listă predefinită, ceea ce este util în special pentru regiunile unde numele orașelor trebuie validate sau standardizate. Rezultatul este o introducere a adresei mai precisă și mai puține erori la finalizarea comenzii.

#### 2. Funcționalități Cheie

- **Selecție structurată a orașului:** înlocuiește câmpul liber de oraș cu un mecanism de selecție structurat pe paginile de checkout din magazin și pe paginile de adresă din portal; se integrează cu modulul `base_address_extended` pentru a folosi gestionarea orașelor nativă din Odoo.
- **Mapare automată cod poștal / ZIP:** facilitează completarea sau validarea automată a codului poștal în funcție de orașul selectat, reducând erorile de introducere și îmbunătățind acuratețea livrării.
- **Integrare frontend și portal:** oferă JavaScript personalizat (module ES) pentru gestionarea dinamică a interacțiunilor oraș/cod poștal în browser, asigurând o experiență consecventă de completare a adresei între magazinul public și portalul privat al clientului.
- **Filtrare oraș după catalogul curierului (adăugat în 19.0.1.2.0):** pe adresa de livrare din checkout, lista de localități se limitează la cele cunoscute de curierul selectat, dacă acesta expune propriul catalog de localități (`delivery.carrier._get_city_domain()`). Filtrul se aplică atât la randare, cât și la interogarea `/portal/state_infos`, iar o localitate trimisă în afara catalogului este respinsă și la validarea pe server. Se aplică doar adresei de livrare — cea de facturare nu este afectată. Filtrul este sărit când nu e ales încă niciun curier, când curierul nu are catalog propriu, sau când catalogul nu acoperă județul respectiv, astfel încât clientul nu rămâne niciodată cu o listă goală.

#### 3. Dependențe

- `portal`
- `website_sale`
- `base_address_extended`

#### 4. Componente Cheie

**Modele**

- `res.country.state` (extins): adaugă relația `city_ids` (One2many către `res.city`) și metoda `get_website_sale_cities()` care întoarce orașele aferente unui județ/stat pentru afișarea în website.

**Vizualizări**

- `address_form_fields` (moștenește `portal.address_form_fields`): inserează un câmp `select` „City” (`city_id`) în formularul de adresă, populat cu orașele filtrate după județul selectat (și, dacă e cazul, după catalogul curierului ales).

**Controllere / Frontend**

- `CustomerPortalCity` (extinde `portal.CustomerPortal`):
  - `_get_carrier_city_domain()`: calculează domeniul de restricție a localităților pe baza catalogului curierului ales pe coșul curent (`request.cart.carrier_id`), folosind duck-typing (`hasattr(carrier, "_get_city_domain")`) pentru a rămâne compatibil chiar și fără modulul `deltatech_delivery` instalat; se aplică doar pe adresa de livrare.
  - `_prepare_address_form_values()`: pregătește valorile formularului de adresă (`state`, `state_cities`, `city`), aplicând domeniul de filtrare a orașelor calculat mai sus.
  - `_get_mandatory_address_fields()`: forțează câmpurile obligatorii `city_id`/`state_id` (eliminând `city` text liber) când țara are `enforce_cities`.
  - `_validate_address_values()`: respinge server-side orașul selectat dacă acesta nu se regăsește în catalogul curierului ales, cu mesaj de eroare dedicat.
  - ruta JSON-RPC `/portal/state_infos/<state>`: întoarce orașele și codurile poștale pentru județul ales, aplicând același filtru de curier.
- `static/src/interactions/address.esm.js`: interacțiune frontend care gestionează dinamic selecția oraș/cod poștal pe pagina de adresă.
- `data/ir_model_fields.xml`: date de configurare a câmpurilor de model aferente.

#### 5. Conexiuni

- [deltatech_delivery_locker_website](../deltatech_delivery_locker_website/index.md): depinde de acest modul, reutilizând selecția structurată a orașului în fluxul de alegere a punctului de livrare (locker) pe website.
- [deltatech_delivery](../deltatech_delivery/index.md): furnizează metoda `delivery.carrier._get_city_domain()` folosită (opțional, prin duck-typing) pentru a restricționa localitățile oferite la catalogul curierului selectat pe adresa de livrare; nu este o dependență strictă în manifest.
