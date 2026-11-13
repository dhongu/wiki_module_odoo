# Delivery Price by Category

- **Nume Tehnic:** `deltatech_delivery_category_price`
- **Versiune:** `19.0.1.0.7`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_category_price
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_category_price`
- **Ultima Ingestie:** `2026-11-13`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul calculează tariful de livrare din magazinul online pe baza categoriilor de website ale produselor din coș, nu pe baza categoriilor contabile interne (adesea prea generice, de exemplu o singură categorie „Bunuri” pentru tot catalogul) și nici a unei potriviri fragile după numele produsului. Echipa de vânzări poate astfel configura prețuri de transport realiste pentru categorii distincte (de exemplu saltele, paturi), inclusiv tarife pe tranșe de greutate. Modulul apare în Odoo Apps sub numele *Delivery Price by Category*.

#### 2. Funcționalități Cheie

- **Tarife pe categorii, per metodă de livrare:** fiecare metodă de livrare poate avea o listă de tarife — preț fix pentru una sau mai multe categorii de website (subcategoriile sunt incluse) sau tarif pe tranșe de greutate pentru alte categorii (ex. lenjerie, accesorii).
- **Cel mai mare tarif, nu suma:** când comanda se potrivește cu mai multe tarife, se aplică cel mai mare preț (de exemplu saltea 300 plus pat 350 se livrează cu 350), evitând dubla taxare.
- **Tranșe de greutate:** se folosește prima tranșă (*Up to (kg)* și *Price*) care acoperă greutatea totală a produselor din coș aflate în categoriile tarifului, nu greutatea întregii comenzi. Dacă greutatea depășește cea mai mare tranșă, prețul implicit devine candidat.
- **Preț implicit:** dacă niciun tarif nu se potrivește (sau greutatea depășește toate tranșele și niciun alt tarif din coș nu e mai mare), se aplică prețul implicit al metodei, iar pagina de finalizare afișează „Communicated before delivery” în loc de „Free”; echipa de vânzări comunică ulterior costul real sau împarte livrarea manual. Într-un coș mixt câștigă tariful cel mai mare, deci un tarif fix mai mare se aplică fără nicio notificare.
- **Manipulare (handling):** o bifă opțională „Add handling” la finalizarea comenzii adaugă un supliment configurabil, doar peste tarifele fixe pe categorie (nu peste cele pe greutate sau prețul implicit).
- **Pe comanda de vânzare:** solicitarea de manipulare apare ca banner pe ofertă, iar câmpurile *Delivery handling* și *Handling cost* (doar citire) sunt în tabul *Other Info*; suma se reține la momentul comenzii și nu se recalculează dacă tarifele se schimbă ulterior.
- **Configurare:** *Website → Configuration → eCommerce → Delivery Methods* (sau *Sales → Configuration → Sales Orders → Delivery Methods*); metoda se setează cu *Provider* „Category price (website)”, produsul de livrare și *Published*; în tabul *Category tariffs* se introduc *Default price*, *Handling cost* și câte o linie pe tarif. Pașii cu capturi sunt în fișa consultant.
- **Limitări cunoscute:** valorile *Default price* și *Handling cost* din dreptul listei apar fără etichetă; mesajul „Communicated before delivery” rămâne în engleză pe un website în română; dacă după bifarea manipulării clientul schimbă coșul sau metoda de livrare, bannerul poate rămâne vizibil cu un cost suplimentar 0,00; la tarifele pe greutate coloana *Price* din listă rămâne 0,00, prețurile fiind în tranșele liniei.

#### 3. Dependențe

- `delivery`
- `website_sale`

#### 4. Componente Cheie

**Modele**

- `delivery.carrier` (extins): tipul de livrare `category_price`, lista `category_tariff_ids`, prețul implicit și costul de manipulare; calculează tariful (`category_price_rate_shipment`).
- `delivery.carrier.category.tariff`: o linie de tarif — tip (preț fix pe categorie sau tarif pe greutate), categoriile de website, prețul și tranșele de greutate.
- `delivery.carrier.category.tariff.bracket`: tranșă de greutate (*Up to (kg)*, preț).
- `sale.order` (extins): `category_tariff_is_fallback`, `category_tariff_handling` și `category_tariff_handling_amount`; `_set_delivery_method` resetează câmpurile când metoda de livrare se schimbă sau se elimină.

**Vizualizări**

- `view_delivery_carrier_form_category_price`: tabul *Category tariffs* în formularul metodei de livrare.
- `delivery_method_category_tariff_handling`: șablon de website care extinde `website_sale.delivery_method` cu bifa de manipulare și mesajul „Communicated before delivery”.
- `view_order_form_category_tariff_handling`: bannerul și câmpurile de manipulare în formularul comenzii de vânzare.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite cron-uri sau acțiuni server. Modulul adaugă un controller (`controllers/delivery.py`, rută `jsonrpc`) și un script frontend (`static/src/js/checkout.esm.js`) pentru bifa de manipulare la finalizarea comenzii.

#### 5. Conexiuni

- `delivery`, `website_sale`: tipul de livrare nou se integrează în metodele de livrare și în fluxul de finalizare a comenzii din magazinul online.
