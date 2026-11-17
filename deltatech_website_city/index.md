# Website City (localizat la `deltatech_website_city/index.md`)

- **Nume Tehnic:** `deltatech_website_city`
- **Versiune:** `19.0.1.2.5`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_city`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_city`
- **Ultima Ingestie:** `2026-11-17`

#### 1. Sumar

Modulul îmbunătățește gestionarea adreselor în zonele de eCommerce și Portal din Odoo, oferind o selecție structurată a orașelor. În loc de a introduce numele orașului ca text liber, clientul îl alege dintr-o listă predefinită, ceea ce este util în special pentru regiunile unde numele orașelor trebuie validate sau standardizate. Rezultatul este o introducere a adresei mai precisă și mai puține erori la finalizarea comenzii.

#### 2. Funcționalități Cheie

- **Selecție structurată a orașului:** înlocuiește câmpul liber de oraș cu un mecanism de selecție pe paginile de checkout din magazin și pe paginile de adresă din portal; folosește gestionarea orașelor din `base_address_extended`. Lista de orașe/localități se definește la **Contacte > Configurare > Orașe**.
- **Mapare automată cod poștal:** codul poștal se completează sau se validează în funcție de orașul ales, reducând erorile de introducere și îmbunătățind acuratețea livrării.
- **Integrare frontend și portal:** JavaScript propriu (module ES) gestionează dinamic interacțiunea oraș/cod poștal, cu aceeași experiență în magazinul public și în portalul clientului.
- **Filtrare după catalogul curierului (19.0.1.2.0):** pe adresa de livrare din checkout, lista de localități se limitează la cele cunoscute de curierul ales, dacă acesta are catalog propriu. Filtrul se aplică la randare și la interogarea `/portal/state_infos`, iar o localitate din afara catalogului este respinsă și la validarea pe server. Nu se aplică adresei de facturare și este sărit când nu e ales curier, când curierul nu are catalog sau când catalogul nu acoperă județul, ca lista să nu rămână goală.
- **Completarea câmpului text „oraș” din localitatea aleasă (19.0.1.2.3):** adresa salvată la checkout păstrează și numele orașului în câmpul liber `city`, nu doar `city_id`, astfel încât postarea facturii, etichetele curierului și rapoartele să găsească orașul. O migrare completează orașul la partenerii deja salvați fără el.
- **Migrare la upgrade din 18.0 (19.0.1.2.5):** o migrare elimină vechea vizualizare `address`, rămasă în baza de date și raportată ca șablon defect pe site; câmpul de oraș este adăugat de vizualizarea `address_form_fields`.

#### 3. Dependențe

- `portal`
- `website_sale`
- `base_address_extended`

#### 4. Componente Cheie

**Modele**

- `res.country.state` (extins): relația `city_ids` (One2many către `res.city`) și metoda `get_website_sale_cities()`, care întoarce orașele unui județ pentru afișare în website.

**Vizualizări**

- `address_form_fields` (moștenește `portal.address_form_fields`): inserează câmpul `select` „City” (`city_id`) în formularul de adresă, populat după județul ales și, unde e cazul, după catalogul curierului.

**Controllere / Frontend**

- `CustomerPortalCity` (extinde `portal.CustomerPortal`):
  - `_get_carrier_city_domain()`: domeniul de restricție a localităților din catalogul curierului ales pe coșul curent (`request.cart`), prin `hasattr(carrier, "_get_city_domain")`; doar pentru adresa de livrare.
  - `_prepare_address_form_values()`: pregătește valorile formularului (`state`, `state_cities`, `city`) cu filtrul de curier.
  - `_get_mandatory_address_fields()`: când țara are `enforce_cities`, cere `city_id`/`state_id` și elimină `city` din câmpurile obligatorii.
  - `_parse_form_data()`: completează `city` (text) cu numele localității din `city_id`, dacă `city` e gol.
  - `_validate_address_values()`: respinge o localitate din afara catalogului curierului, cu mesaj de eroare dedicat.
  - ruta JSON-RPC `/portal/state_infos/<state>`: întoarce orașele și codurile poștale ale județului, cu același filtru.
- `static/src/interactions/address.esm.js`: interacțiunea frontend pentru selecția dinamică oraș/cod poștal.
- `data/ir_model_fields.xml`: adaugă `city_id` de pe `res.partner` în lista albă a form builder-ului.
- `migrations/19.0.1.2.3` și `migrations/19.0.1.2.5`: completarea `city` la partenerii existenți, respectiv ștergerea vizualizării vechi `address`.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): oferă `delivery.carrier._get_city_domain()`, folosită opțional (verificare `hasattr`) la filtrarea localităților; nu e dependență în manifest.
- [deltatech_delivery_locker_website](../deltatech_delivery_locker_website/index.md): are acest modul în `depends`.
- [terrabit_pro](../terrabit_pro/index.md): include acest modul în `depends`.
