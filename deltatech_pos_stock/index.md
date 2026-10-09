# Deltatech POS Stock (localizat la `deltatech_pos_stock/index.md`)

- **Nume Tehnic:** `deltatech_pos_stock`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_pos_stock
- **Cale Locală:** `odoo-addons/deltatech/deltatech_pos_stock`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Acest modul extinde interfața de Punct de Vânzare (POS) afișând direct pe cardul produsului cantitatea de stoc, ajutând casierii să vadă rapid ce mai este disponibil chiar în timpul vânzării. Din perspectivă de business, reduce riscul de a vinde produse epuizate și oferă o imagine clară asupra disponibilității mărfii la casă. Stocul poate fi afișat fie ca stoc fizic (la mână), fie ca cantitate disponibilă, din care se scade ce este deja rezervat pentru comenzi încă neexpediate, util acolo unde livrarea este validată de depozit, nu la casă. Funcționalitatea se configurează separat pentru fiecare punct de vânzare.

#### 2. Funcționalități Cheie

- **Afișare stoc în timp real:** cantitatea fiecărui produs apare pe cardul din interfața POS și se actualizează în sesiunile deja deschise, printr-o notificare live (bus) la modificarea stocului.
- **Afișare preț pe aceeași etichetă (badge):** prețul apare împreună cu stocul, suprapus pe imaginea produsului din grila POS.
- **Control din setările POS:** stocul și prețul se activează/dezactivează separat, în secțiunea „Product Stock" din setările POS (per punct de vânzare).
- **Cantitate afișată (nou în 19.0.1.2.0):** opțiune cu două valori — *On hand* (stoc fizic, implicit, comportament neschimbat) sau *Available* (stoc minus rezervări pentru comenzi care nu au părăsit încă depozitul). Opțiunea apare doar când afișarea stocului este bifată.
- **Avertizare la stoc epuizat (nou în 19.0.1.2.0):** produsele fără cantitate rămasă de vândut au cantitatea afișată în roșu, iar adăugarea lor în comandă generează un avertisment în POS. Vânzarea nu este blocată, pentru ca casierul să poată lucra și când cifra din Odoo este în urmă.
- **Stoc pe depozitul punctului de vânzare:** cantitatea se calculează în contextul depozitului configurat pe POS.
- **Limitat la produse stocabile** și disponibile în POS.
- **Compatibilitate cu arhitectura OWL din Odoo 19.**

#### 3. Dependențe

- `point_of_sale`
- `stock`

#### 4. Componente Cheie

Sumarul și funcționalitățile provin din `readme/DESCRIPTION.md` și `readme/HISTORY.md`; întrucât DESCRIPTION.md nu acoperă noile funcții din 19.0.1.2.0, componentele au fost verificate în cod.

**Modele**

- `pos.config` (extins): câmpurile `display_stock`, `display_price` și `stock_badge_quantity` (selecție `on_hand` / `available`, implicit `on_hand`).
- `res.config.settings` (extins): câmpuri related `pos_display_stock`, `pos_display_price`, `pos_stock_badge_quantity`.
- `product.template` (extins): câmpul calculat `free_qty` (suma cantităților libere ale variantelor, deoarece nucleul nu o agregă pe template); încarcă `qty_available` (și `free_qty` când badge-ul e „Available") în datele POS, cu contextul depozitului POS; metoda `_notify_pos_stock_change` trimite notificarea `STOCK_SYNCHRONISATION` către sesiunile deschise cu afișarea stocului activă.
- `stock.quant` (extins): la modificarea `quantity` notifică sesiunile POS; la modificarea `reserved_quantity` notifică doar casele setate pe „Available" (verificare ieftină prealabilă, ca să nu fie afectate instalările care nu folosesc opțiunea).

**Vizualizări**

- `views/res_config_settings_views.xml` (`res_config_settings_view_form`): setarea „Product Stock" în secțiunea de interfață POS, cu „Show stock", „Show price" și „Quantity shown".
- Frontend OWL: `static/src/xml/product_card.xml` și `static/src/js/product_card.esm.js` (badge), `pos_stock_synchronisation.esm.js` (primește notificarea live și actualizează modelul din memorie), `pos_stock_warning.esm.js` (avertismentul la stoc epuizat), `static/src/css/pos_stock.css`.

**Acțiuni Automate / Acțiuni Server**

- Nu există `ir.cron` sau acțiuni server; actualizarea se face prin notificări bus declanșate din `stock.quant`.

#### 5. Conexiuni

- `point_of_sale`: modulul de bază al Punctului de Vânzare, a cărui interfață de produse este extinsă.
- `stock`: sursa cantităților (fizice și rezervate) afișate pe cardul produsului.
- [deltatech_pos_price_sync](../deltatech_pos_price_sync/index.md): trimite modificările de preț către sesiunile deschise, pe același canal live.
- [deltatech_pos](../deltatech_pos/index.md) și [deltatech_pos_base](../deltatech_pos_base/index.md): restul suitei POS Terrabit (bonuri fiscale, numerar), fără suprapunere.
- [deltatech_pos_fix](../deltatech_pos_fix/index.md): corecții de calcul al totalului în POS, în aceeași suită.
