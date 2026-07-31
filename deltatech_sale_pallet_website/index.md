# Sale Pallet Website (localizat la `deltatech_sale_pallet_website/index.md`)

- **Nume Tehnic:** `deltatech_sale_pallet_website`
- **Versiune:** `19.0.1.0.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_pallet_website`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_pallet_website`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul extinde logica de paleți din vânzări către magazinul online (eCommerce), astfel încât produsele vândute pe paleți să fie afișate și gestionate corect și pe website. Atunci când un client adaugă în coș un produs care necesită paletizare, modulul recalculează automat liniile de palet direct în coșul de cumpărături, la fel cum se întâmplă deja pe comenzile create din back-office, iar pagina de produs poate afișa prețul corespunzător cantității unui palet.

#### 2. Funcționalități Cheie

- Afișarea pe pagina de produs a prețului corespunzător cantității minime a unui palet, atunci când produsul are configurată o astfel de cantitate.
- Optimizarea experienței de cumpărare pentru achiziții en-gros sau produse vândute în mod tipic pe paleți.
- Recalcularea automată a liniilor de palet din coșul de cumpărături pe măsură ce clientul adaugă sau modifică cantitatea unui produs pe website, păstrând consistența cu logica din `deltatech_sale_pallet`.
- Se bazează pe flag-ul „Palet" configurat la nivelul categoriei de produs pentru a identifica articolele cărora li se aplică logica de paletizare pe website.

#### 3. Dependențe

- [deltatech_sale_pallet](../deltatech_sale_pallet/index.md)
- `website_sale`

#### 4. Componente Cheie

*Sumarul și funcționalitățile au fost preluate din `readme/DESCRIPTION.md`; analiza detaliată a codului pentru această secțiune nu a fost solicitată explicit în Readme. Componentele de mai jos sunt menționate orientativ, pe baza structurii modulului.*

**Modele**

- `sale.order`: extins cu suprascrierea hook-ului `_verify_cart_after_update` (apelat de website_sale după `_cart_add`/`_cart_update_line_quantity` în Odoo 19) pentru a recalcula liniile de palet direct în coșul de cumpărături.

**Vizualizări**

- `views/templates.xml` (`show_pallet_price`): extinde șablonul `website_sale.product` pentru a afișa, pe pagina produsului, prețul corespunzător cantității minime de palet.

#### 5. Conexiuni

- [deltatech_sale_pallet](../deltatech_sale_pallet/index.md): modulul de bază pentru logica de paletizare pe comenzile de vânzare, extins de acest modul pentru magazinul online.
- `website_sale`: platforma eCommerce Odoo ale cărei pagini de produs și coș de cumpărături sunt extinse pentru afișarea și recalcularea paleților.
