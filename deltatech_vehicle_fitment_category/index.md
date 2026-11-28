# Compatibilitate vehicule din categoriile magazinului

- **Nume Tehnic:** `deltatech_vehicle_fitment_category`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_vehicle_fitment_category
- **Cale Locală:** `odoo-addons/bitshop/deltatech_vehicle_fitment_category`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul preia compatibilitatea pieselor cu utilajele direct din categoriile eCommerce, pentru magazinele care își organizează deja piesele pe mașini (de exemplu `Piese combine / CLAAS / Claas Lexion / Lexion 570` sau `Piese tractor / JOHN DEERE / MOTOR`). Fiecare produs ajunge să se potrivească automat cu toate utilajele din categoriile în care este plasat, fără introducere manuală pe fiecare produs.

#### 2. Funcționalități Cheie

- Grup **Compatibilitate vehicule** pe categoria eCommerce: tip de vehicul, marcă, serie și model. Câmpurile goale se iau de la categoria părinte, iar *Fără vehicul* oprește moștenirea pentru o întreagă ramură (piese universale).
- Asistentul **Detectare vehicule în categorii** completează câmpurile din denumirile categoriilor: marca (cu lista de mărci și denumirile lor alternative), seria și modelele de sub ea. Categoriile setate manual rămân neschimbate.
- Un produs se potrivește cu toate utilajele categoriilor sale (trei categorii de model înseamnă trei linii de compatibilitate); când produsul e și într-o categorie, și într-o subcategorie a ei, contează doar subcategoria.
- O categorie cu marcă și tip de vehicul (`Piese combine / CLAAS`) acoperă toate seriile mărcii de acel tip; dacă marca nu are serie de tipul respectiv, se creează una denumită după tip, cu un model pentru selectorul de vehicule din magazin.
- Compatibilitățile urmează categoriile: mutarea produsului sau modificarea categoriei actualizează liniile imediat. Se modifică doar liniile cu sursa *Categorie produs* care nu sunt verificate.
- Meniuri: *Vânzări > Configurare > Vehicule > Categorii eCommerce* (coloana *Se potrivește*) și *Detectare vehicule în categorii*; tipurile de vehicul se creează în *Tipuri de vehicule*. Fluxul pas-cu-pas este în fișa consultant.

#### 3. Dependențe

- [deltatech_vehicle_fitment](../deltatech_vehicle_fitment/index.md)
- `website_sale`

#### 4. Componente Cheie

**Modele**

- `product.public.category` (extins): câmpurile de compatibilitate (tip, marcă, serie, model, fără vehicul) și coloana calculată *Se potrivește*.
- `product.template` (extins): linii de compatibilitate cu sursa *Categorie produs*, urmărind categoriile.
- `vehicle.category.sync`: sincronizarea compatibilităților produselor cu categoriile.
- `vehicle.category.detect.wizard`: asistentul de detectare a vehiculelor din denumirile categoriilor.

**Vizualizări**

- `product_public_category_form_view` / `product_public_category_tree_view`: grupul de compatibilitate și coloana *Se potrivește* pe categorii.
- `view_category_detect_wizard_form`: asistentul de detectare.

**Acțiuni Automate / Acțiuni Server**

- `action_vehicle_categories` și `action_category_detect_wizard`: acțiuni de fereastră pentru meniurile de mai sus; nu există sarcini cron.

#### 5. Conexiuni

- [deltatech_vehicle_fitment](../deltatech_vehicle_fitment/index.md): modulul de bază care ține liniile de compatibilitate pe produs.
