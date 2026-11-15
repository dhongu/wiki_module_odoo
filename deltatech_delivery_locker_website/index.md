# Delivery in locker - website (localizat la `deltatech_delivery_locker_website/index.md`)

- **Nume Tehnic:** `deltatech_delivery_locker_website`
- **Versiune:** `19.0.0.0.14`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_locker_website
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_locker_website`
- **Ultima Ingestie:** `2026-11-15`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul aduce livrarea în locker în checkout-ul de website. Clientul alege un locker sau un punct de ridicare al curierului pe harta Odoo cu locații de ridicare, alimentată din catalogul comun de lockere din [deltatech_delivery_locker](../deltatech_delivery_locker/index.md), iar metoda de livrare în locker este oferită doar pentru coșurile care încap într-un locker. Astfel clientul vede doar opțiunile de livrare relevante.

#### 2. Funcționalități Cheie

- **Metode locker doar pentru coșuri compatibile**: dacă în coș există un produs fizic nemarcat ca livrabil în locker, metodele de livrare care folosesc lockere nu sunt oferite în checkout; serviciile și produsele digitale nu contează.
- **Alegerea lockerului pe hartă**: locațiile arătate clientului vin din catalogul de lockere al curierului (importat și ținut la zi de modulul de bază); la comenzile plătite la livrare sunt excluse cele care nu încasează plata.
- **Lockerul ales ajunge în AWB**: lockerul selectat pe website, adresa de livrare și AWB-ul citesc aceeași valoare, deci coletul nu e rezervat la alt locker decât cel ales de client.
- **Insignă „Locker” pe produse**: o insignă opțională pe pagina de produs arată ce produse pot fi livrate în locker; se activează din vizualizarea ei (Setări → Tehnic → Interfață utilizator → Vizualizări, căutare *Locker badge on product page*, bifat **Active**, în modul dezvoltator). Insigna de pe cardul de produs nu poate fi activată încă pe 19.0 (remediere în așteptare, issue #491).
- **Date de checkout pentru modulele de curieri**: pagina de checkout știe dacă coșul încape într-un locker, informație folosită de modulele specifice curierilor (harta Sameday easybox, harta Postis) pentru propriile butoane.
- **Configurare**: metodele de livrare în locker se configurează cu [deltatech_delivery_locker](../deltatech_delivery_locker/index.md) (**Use Locker**, **Get Lockers**) și se publică pe website; **Get Lockers** încarcă lockerele alese de clienți, iar **Get Pickup Locations** este alt buton, care încarcă punctele de ridicare ale expeditorului. Pe produsele care încap într-un locker se bifează **Can be delivered in locker**.
- **Flux client** (detaliat în fișa consultant): coș → checkout → metoda locker → **Select a location** → fereastra **Choose a pick-up point** (listă și hartă) → **Choose this location**; lockerul devine adresa de livrare, iar pe comandă apar bannerul *Delivery to Locker* și câmpul **Locker**.

#### 3. Dependențe

- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md)
- [deltatech_website_city](../deltatech_website_city/index.md)
- `website_sale`

#### 4. Componente Cheie

Secțiunile 1 și 2 provin din `readme/DESCRIPTION.md`, completat cu `CONFIGURE.md` și `USAGE.md`; componentele de mai jos au fost verificate în cod.

**Modele**

- `sale.order` (extins): `_get_delivery_methods()` exclude curierii cu `use_locker` dacă în comandă există cel puțin un produs stocabil cu `for_locker = False`. Câmpul `locker` este definit ca derivat în [deltatech_delivery_locker](../deltatech_delivery_locker/index.md) și nu mai este redefinit aici.

**Controlere**

- `WebsiteSaleLocker` (extinde `WebsiteSale`): `shop_checkout` elimină parametrul `express`; `_prepare_checkout_page_values` adaugă în valorile paginii indicatorul `for_locker`, calculat pe produsele stocabile din comandă.

**Vizualizări**

- `product_locker_badge_on_pdp` (moștenește `website_sale.product`, inactivă implicit): insigna „Locker” pe pagina de produs, pentru produsele cu `for_locker`.
- `products_item_locker_badge_on_card` (moștenește `website_sale.products_item`, inactivă implicit): aceeași insignă pe cardul de produs; nu poate fi activată încă pe 19.0 (#491).
- Stil: `static/src/scss/locker_badge.scss`, încărcat în `web.assets_frontend`.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește acțiuni automate sau acțiuni server.

#### 5. Conexiuni

- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): modulul de bază pentru livrarea în locker și catalogul de lockere, extins aici pentru website.
- [deltatech_website_city](../deltatech_website_city/index.md): selecția localității în fluxul de checkout.
- `website_sale`: fluxul standard de eCommerce în care se filtrează metodele de livrare și se afișează insignele.
