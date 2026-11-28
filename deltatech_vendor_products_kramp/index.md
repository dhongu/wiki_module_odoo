# Vendor Products Kramp (localizat la `deltatech_vendor_products_kramp/index.md`)

- **Nume Tehnic:** `deltatech_vendor_products_kramp`
- **Versiune:** `20.0.1.2.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop_vendor/tree/20.0/deltatech_vendor_products_kramp
- **Cale Locală:** `odoo-addons/bitshop_vendor/deltatech_vendor_products_kramp`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul conectează catalogul de produse al furnizorilor la Kramp, distribuitorul de piese de schimb agricole, prin API-ul webshop-ului Kramp. Elimină introducerea manuală a produselor și ține în Odoo prețurile, disponibilitatea și termenele de livrare actualizate.

#### 2. Funcționalități Cheie

- **Căutare online:** un cod sau un termen căutat în shop-ul website-ului este căutat la Kramp, iar articolele găsite intră în catalogul furnizorului cu nume, imagine, preț net (de achiziție) și preț brut (de listă).
- **Actualizare prețuri:** butonul „Load Price API” de pe flux sau de pe produsele furnizorului citește prețurile curente, în loturi de 25 de produse pe cerere.
- **Disponibilitate:** Kramp nu publică stocul, așa că el este dedus din planurile de livrare: cantitatea livrată în 10 zile devine cantitate disponibilă (maximum 999), iar zilele până la prima livrare devin termenul de achiziție.
- **Adăugare din produse:** produsele care au deja Kramp ca furnizor sunt căutate la Kramp după codul din linia de furnizor sau după codul de bare (EAN) și adăugate în catalog, legate de produs.
- **Sincronizare nocturnă:** acțiunea programată adaugă produsele noi, apoi actualizează pentru fiecare produs legat prețul de achiziție, cantitatea și termenul pe linia de furnizor, plus prețul de vânzare (după regulile de preț ale fluxului). Nu creează produse, iar un produs fără preț Kramp își păstrează prețul de vânzare.
- **Configurare:** *Purchase > Products > Vendor Feed*, tip conexiune **Kramp**, utilizator și parolă ale contului webshop, moneda fluxului (RON pentru Kramp România) și *Kramp Locale* (implicit `ro_RO`; prețurile se întorc doar în locale-ul propriului shop). Fără credențiale căutarea întoarce doar nume și imagini, fără prețuri.
- Butonul **Kramp Sync** de pe flux rulează sincronizarea la cerere. Fluxul detaliat este în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_vendor_products_website](../deltatech_vendor_products_website/index.md)

#### 4. Componente Cheie

Sumarul și funcționalitățile provin din `readme/DESCRIPTION.md`; componentele sunt listate pe scurt, din codul modulului.

**Modele**

- `vendor.feed` (extins): adaugă tipul de conexiune `kramp`, `kramp_locale` și câmpurile de token (vizibile doar administratorilor); conține clientul webshop Kramp.

**Vizualizări**

- `view_vendor_feed_form`: extinde formularul fluxului de furnizor cu setările Kramp.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_kramp_sync` („Kramp: Sync Prices and Stock”): rulează zilnic, activă după instalare.

#### 5. Conexiuni

- [deltatech_vendor_products_website](../deltatech_vendor_products_website/index.md): căutarea online în shop folosită de conectorul Kramp.
- [deltatech_vendor_products](../deltatech_vendor_products/index.md): catalogul de produse furnizor (`vendor.feed`, `vendor.product`) pe care se construiește conectorul.
