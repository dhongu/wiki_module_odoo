# Postis Shipping Locker (localizat la `deltatech_delivery_postis_locker/index.md`)

- **Nume Tehnic:** `deltatech_delivery_postis_locker`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_postis_locker
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_postis_locker`
- **Ultima Ingestie:** `2026-09-03`

#### 1. Sumar

Acest modul permite clientului unui magazin online să aleagă, direct la finalizarea comenzii, un locker sau un punct de ridicare Postis de pe harta pusă la dispoziție de Postis, astfel încât coletul să fie expediat acolo și nu la adresa de domiciliu. Extinde metoda de livrare **Postis Shipping** cu widget-ul de hartă al Postis, înregistrează locația aleasă în catalogul comun de lockere al suitei și se asigură că AWB-ul este adresat corect către acea locație, nu către client.

#### 2. Funcționalități Cheie

- **Selecția locației pe harta Postis**: harta de livrare Postis se deschide la checkout, la pasul de livrare, doar pentru coșurile în care toate produsele sunt marcate ca potrivite pentru locker (`for_locker`, din `deltatech_delivery_locker_website`).
- **Cheie de hartă configurabilă per client**: pe metoda de livrare Postis se bifează „Use Locker” și se completează câmpul **Postis Map Key** — cheia emisă de Postis pentru contul de client; fără ea harta nu se poate deschide. Există și un mod demo (**Postis Map Demo Mode**) care rulează harta pe setul de date demo al Postis, independent de credențialele API folosite pentru emiterea AWB-ului.
- **Selecția este înregistrată, nu doar afișată**: locația aleasă este salvată în catalogul comun `delivery.locker`; se creează (sau se reutilizează, dacă locația a mai fost aleasă) o adresă de livrare pe baza ei, care este apoi setată pe comandă, iar comanda este re-cotată (re-quoted) pentru noua adresă.
- **Adresare corectă a AWB-ului**: expedierea folosește id-ul și localitatea proprii ale locației, nu pe cele ale clientului; localitatea este rezolvată pe nomenclatorul Odoo (`res.city`/`res.country.state`), astfel încât Postis primește un id de localitate, nu doar un nume. O localitate ambiguă este lăsată nerezolvată, nu ghicită.
- **Selecție ilizibilă blochează checkout-ul**: payload-ul hărții este acceptat sub toate variantele de denumire de câmp folosite până acum de Postis (`lockerId`/`locationId`/`pickupPointId`/`id` etc.); o selecție fără id de locație identificabil întoarce clientul la pasul de livrare cu un mesaj, în loc să confirme o comandă care ar fi expediată acasă.
- **Marcarea produselor eligibile**: produsele care încap într-un locker se marchează cu **For Locker** (câmp din `deltatech_delivery_locker_website`); un coș care conține un produs fără acest marcaj nu primește oferta curierului cu locker.
- **Limită cunoscută**: nu există import al catalogului de lockere Postis — locațiile intră în catalog pe măsură ce clienții le aleg pe hartă, deci harta de back-office a lockerelor arată doar locațiile deja folosite cel puțin o dată.

#### 3. Dependențe

- [deltatech_delivery_postis](../deltatech_delivery_postis/index.md)
- [deltatech_delivery_locker_website](../deltatech_delivery_locker_website/index.md)

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, secțiunile de Sumar și Funcționalități Cheie provin din readme; suplimentar, `readme/HISTORY.md` și codul sursă indică următoarele componente tehnice relevante.

**Modele**

- `delivery.carrier` (extindere): adaugă câmpurile `postis_widget_key` (cheia de hartă, vizibilă doar pentru `base.group_system`) și `postis_widget_demo` (mod demo pentru hartă).
- `website` (extindere): conține logica de integrare cu widget-ul Postis —
  - `postis_locker_client()`: pregătește configurația trimisă către browser (cheie, mod demo, id-ul curierului), fără a expune credențialele API ale metodei de livrare;
  - `postis_locker_values(data)`: normalizează payload-ul hărții Postis, citind fiecare valoare sub toate denumirile de câmp cunoscute (`POSTIS_FIELD_ALIASES`); ridică eroare dacă nu găsește un id de locație;
  - `get_postis_locker_partner(data)`: creează/actualizează locația în `delivery.locker` (prin `upsert_from_data`, din suita de bază locker) și adresa de livrare (`res.partner`) asociată acesteia;
  - `_postis_complete_locker_location(locker, values)`: rezolvă localitatea liberă a lockerului pe `res.city`/`res.country.state`, conservator — o potrivire ambiguă rămâne nerezolvată.

**Controlere**

- `WebsiteSalePostisLocker` (extinde `website_sale.WebsiteSale`):
  - `POST /shop/postis_locker_client`: întoarce configurația hărții pentru browser;
  - `GET|POST /shop/postis_locker_set`: primește selecția de pe hartă, o transformă în adresă de livrare, o setează pe comandă și re-cotează livrarea prin `_set_delivery_method`; o selecție refuzată redirecționează către checkout cu un mesaj de eroare, în loc să confirme comanda.

**Vizualizări**

- `view_delivery_carrier_form_with_provider_postis_locker`: adaugă pe formularul metodei de livrare Postis câmpurile `postis_widget_key` și `postis_widget_demo`, vizibile doar când „Use Locker” este activ.
- `delivery_form` (moștenește `website_sale.delivery_form`): introduce pe pagina de checkout butonul „Select Postis Locker” și containerul hărții, vizibile doar când coșul este eligibil pentru locker (`for_locker`).

**Assets front-end**

- `postis_locker.esm.js`: interacțiune OWL publică (`Interaction`) care încarcă SDK-ul și CSS-ul hărții Postis, inițializează widget-ul cu configurația primită de la server și, la selecție, redirecționează către `/shop/postis_locker_set` cu payload-ul brut al hărții.

#### 5. Conexiuni

- [deltatech_delivery_postis](../deltatech_delivery_postis/index.md): metoda de livrare Postis de bază, pe care acest modul o extinde cu selecția de locker pe hartă.
- [deltatech_delivery_locker_website](../deltatech_delivery_locker_website/index.md): furnizează filtrarea metodelor de livrare pe baza compatibilității produselor (`for_locker`) și contextul de checkout de care depinde afișarea butonului hărții.
- `deltatech_delivery_locker` (via `deltatech_delivery_locker_website`): catalogul comun `delivery.locker` în care este înregistrată locația aleasă și de unde restul suitei de curierat citește adresa lockerului pentru AWB.
