# Vendor Products Bepco (localizat la `deltatech_vendor_products_bepco/index.md`)

- **Nume Tehnic:** `deltatech_vendor_products_bepco`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop_vendor/tree/19.0/deltatech_vendor_products_bepco
- **Cale Locală:** `odoo-addons/bitshop_vendor/deltatech_vendor_products_bepco`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul oferă un conector către catalogul furnizorului Bepco, care aduce în Odoo datele produselor (cod, denumire, imagine, preț de achiziție și stoc disponibil). Elimină introducerea manuală a produselor Bepco și menține catalogul și prețurile la zi, ceea ce ușurează aprovizionarea și planificarea stocurilor.

#### 2. Funcționalități Cheie

- Import automat de catalog: produsele Bepco se preiau direct din sursa furnizorului, fără introducere manuală.
- Acuratețe a datelor: coduri, denumiri (în limba română) și imagini sunt preluate exact din catalogul furnizorului.
- Tip nou de conexiune „Bepco” pe fluxul de furnizor (`vendor.feed`), cu autentificare pe baza utilizatorului, parolei și numărului de client configurate pe flux.
- Căutare online după codul piesei; pentru fiecare piesă găsită se interoghează și prețul de achiziție și disponibilitatea.
- Disponibilitate: dacă furnizorul marchează piesa ca indisponibilă (cod `T`), stocul se setează la 0; altfel se preia cantitatea disponibilă și se aplică termenul de livrare (`purchase_delay`) al fluxului.
- Produsele furnizorului devin căutabile pe website (prin mixin-ul de căutare din modulul de bază).
- Observație: API-ul interogat este cel al TVH (`api.tvh.com`), conform documentului de integrare din `data/`.

#### 3. Dependențe

- [deltatech_vendor_products_website](../deltatech_vendor_products_website/index.md)

#### 4. Componente Cheie

**Modele**

- `vendor.feed` (extins): adaugă tipul de conexiune `bepco`, câmpurile `token_temp`, `token_expires_in`, `token_auth_jwt` și metodele `online_get_values`, `bepco_get_values`, `bepco_get_item_price`.
- `vendor.product` (extins): adaugă `website.searchable.mixin`.

**Vizualizări**

- Modulul nu definește vizualizări proprii.

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau acțiuni server proprii.

#### 5. Conexiuni

- [deltatech_vendor_products](../deltatech_vendor_products/index.md): modulul de bază care definește `vendor.feed` și `vendor.product` (dependență indirectă).
- [deltatech_vendor_products_granit](../deltatech_vendor_products_granit/index.md): conector similar pentru alt furnizor.
- [deltatech_vendor_products_kramp](../deltatech_vendor_products_kramp/index.md): conector similar pentru alt furnizor.
