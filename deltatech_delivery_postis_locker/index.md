# Postis Shipping Locker (localizat la `deltatech_delivery_postis_locker/index.md`)

- **Nume Tehnic:** `deltatech_delivery_postis_locker`
- **Versiune:** `19.0.1.0.6`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_postis_locker
- **Cale Locală:** odoo-addons/bitshop_delivery/deltatech_delivery_postis_locker
- **Ultima Ingestie:** `2026-11-24`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul permite clientului unui magazin online să aleagă, direct la finalizarea comenzii, un locker sau un punct de ridicare Postis de pe harta pusă la dispoziție de Postis, astfel încât coletul să fie expediat acolo și nu la adresa de domiciliu. Extinde metoda de livrare **Postis Shipping** cu widget-ul de hartă al Postis, înregistrează locația aleasă în catalogul comun de lockere al suitei, o setează ca adresă de livrare a comenzii, iar AWB-ul emis prin Postis Shipping pleacă la adresa acelei locații, nu la cea a clientului.

#### 2. Funcționalități Cheie

- **Selecția locației pe harta Postis**: harta Postis se deschide din butonul **Select Postis Locker**, la pasul de adresă/livrare din checkout, doar pentru coșurile în care toate produsele pot fi livrate în locker. Harta este încărcată în browserul clientului direct de la Postis.
- **Cheie de hartă configurabilă per client**: în *Inventory → Configuration → Delivery → Delivery Methods*, pe metoda Postis se bifează **Use Locker** și, în tab-ul **Postis Configuration**, se completează **Postis Map Key** — cheia emisă de Postis pentru contul de client; fără ea harta nu se poate deschide. **Postis Map Demo Mode** rulează harta pe datele demo Postis și afectează doar harta: AWB-ul se emite mereu cu credențialele metodei de livrare, care nu părăsesc serverul.
- **Selecția este înregistrată, nu doar afișată**: locația aleasă este salvată în catalogul comun `delivery.locker` (cod `<id locație>-<id curier>`; se reutilizează dacă a mai fost aleasă) și devine adresa de livrare a comenzii, iar transportul este re-cotat cu metoda Postis pentru noua adresă; clientul continuă cu plata. Pe comandă apare bannerul **Delivery to Locker** cu codul locației, iar lista alese până acum este în *Inventory → Configuration → Delivery → Delivery Lockers*.
- **Localitatea locației**: dacă harta trimite o localitate, aceasta este potrivită pe nomenclatorul Odoo (`res.city`/`res.country.state`); un nume ambiguu rămâne nerezolvat, nu e ghicit.
- **Nicio livrare acasă pe tăcute**: o selecție fără id de locație sau de curier (sau ilizibilă) întoarce clientul la checkout cu un mesaj, în loc să lase comanda să plece la adresa de domiciliu; apoi poate alege din nou sau poate opta pentru livrare la domiciliu. Redirecționarea `callback` merge doar către o cale a site-ului, altfel spre `/shop/checkout`.
- **Marcarea produselor eligibile**: pe produsele care încap într-un locker se bifează **Can be delivered in locker** (tab-ul *Inventory*, câmp din `deltatech_delivery_locker_website`); un coș cu un produs stocabil fără acest marcaj nu primește livrarea în locker.
- **Limite cunoscute** (din readme): widget-ul hărții (versiunea 1.0.6) trimite adresa locației ca un singur text, fără localitate, județ sau cod poștal, așa că localitatea de obicei nu se potrivește și AWB-ul poate pleca fără ea; id-ul propriu al locației nu se trimite încă pe AWB, doar adresa (PL-001); nu există import al catalogului de lockere Postis — locațiile intră în catalog pe măsură ce clienții le aleg, deci harta de back-office arată doar locațiile folosite cel puțin o dată; payload-ul hărții nu e un contract publicat, iar câmpurile returnate sub nume necunoscute rămân goale.
- **Date trimise către Postis**: browserul clientului încarcă harta de la Postis și primește cheia hărții, ID-ul clientului Postis și indicatorul demo; expedierea propriu-zisă o trimite **Postis Shipping**, cu adresa locației ca adresă a destinatarului.

#### 3. Dependențe

- [deltatech_delivery_postis](../deltatech_delivery_postis/index.md)
- [deltatech_delivery_locker_website](../deltatech_delivery_locker_website/index.md)

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, secțiunile de Sumar și Funcționalități Cheie provin din readme; suplimentar, `readme/HISTORY.md` și codul sursă indică următoarele componente tehnice relevante.

**Modele**

- `delivery.carrier` (extindere): adaugă câmpurile `postis_widget_key` (cheia de hartă, vizibilă doar pentru `base.group_system`) și `postis_widget_demo` (mod demo pentru hartă).
- `website` (extindere): conține logica de integrare cu widget-ul Postis —
  - `postis_locker_client()`: pregătește configurația trimisă către browser (cheie, mod demo, id-ul curierului), fără a expune credențialele API ale metodei de livrare;
  - `postis_locker_values(data)`: normalizează selecția primită de la browser, trimisă plat (`location_id`, `courier_id` identifică punctul; restul îl descriu, citite prin `POSTIS_FIELD_ALIASES`); codul lockerului este perechea `<location_id>-<courier_id>`, iar curierul se păstrează și în `external_ref`; ridică eroare dacă lipsește id-ul locației sau al curierului;
  - `get_postis_locker_partner(data)`: creează/actualizează locația în `delivery.locker` (prin `upsert_from_data`, din suita de bază locker) și adresa de livrare (`res.partner`) asociată acesteia;
  - `_postis_complete_locker_location(locker, values)`: rezolvă localitatea liberă a lockerului pe `res.city`/`res.country.state`, conservator — o potrivire ambiguă rămâne nerezolvată.

**Controlere**

- `WebsiteSalePostisLocker` (extinde `website_sale.WebsiteSale`):
  - `POST /shop/postis_locker_client`: întoarce configurația hărții pentru browser;
  - `GET|POST /shop/postis_locker_set`: primește selecția de pe hartă (parametri plați), o transformă în adresă de livrare, o setează pe comandă (`request.cart`) și re-cotează livrarea prin `_set_delivery_method`; o selecție refuzată redirecționează către `/shop/checkout` cu un mesaj de eroare, în loc să confirme comanda; parametrul `callback` e urmat doar dacă e o cale a site-ului (`_internal_callback`).

**Vizualizări**

- `view_delivery_carrier_form_with_provider_postis_locker`: adaugă pe formularul metodei de livrare Postis câmpurile `postis_widget_key` și `postis_widget_demo`, vizibile doar când „Use Locker” este activ.
- `delivery_form` (moștenește `website_sale.delivery_form`): introduce pe pagina de checkout butonul „Select Postis Locker” și containerul hărții, vizibile doar când coșul este eligibil pentru locker (`for_locker`).

**Assets front-end**

- `postis_locker.esm.js`: interacțiune publică (`Interaction`) care încarcă SDK-ul și CSS-ul hărții Postis, inițializează widget-ul (în mod pickup) cu configurația primită de la server și, la selecție, redirecționează către `/shop/postis_locker_set`.
- `postis_selection.esm.js`: aplatizează obiectul imbricat întors de widget (`{delivery, location: {id, courierId, ...}}`) în parametri plați (`location_id`, `courier_id`, nume, adresă, coordonate); are teste unitare JS (`static/tests/postis_selection.test.js`).

#### 5. Conexiuni

- [deltatech_delivery_postis](../deltatech_delivery_postis/index.md): metoda de livrare Postis de bază, pe care acest modul o extinde cu selecția de locker pe hartă.
- [deltatech_delivery_locker_website](../deltatech_delivery_locker_website/index.md): furnizează filtrarea metodelor de livrare pe baza compatibilității produselor (`for_locker`) și contextul de checkout de care depinde afișarea butonului hărții.
- `deltatech_delivery_locker` (via `deltatech_delivery_locker_website`): catalogul comun `delivery.locker` în care este înregistrată locația aleasă și de unde restul suitei de curierat citește adresa lockerului pentru AWB.
