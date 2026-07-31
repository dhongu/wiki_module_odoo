# NAP (localizat la `deltatech_nap/index.md`)

- **Nume Tehnic:** `deltatech_nap`
- **Versiune:** `19.0.1.4.4`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_nap`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_nap`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul NAP (de la „Need and Availability Planning" — planificarea necesarului și a disponibilității) este o extensie Odoo dezvoltată de Terrabit/Deltatech care se concentrează pe planificarea cererii de stoc și pe gestionarea disponibilității produselor. Oferă companiilor instrumente avansate pentru optimizarea proceselor de gestiune a stocurilor: urmărirea cererii de produse, analiza istoricului livrărilor și fundamentarea deciziilor de aprovizionare. Scopul de afaceri este reducerea rupturilor de stoc și a stocurilor în exces, printr-o prognoză mai bună a necesarului de achiziție. Se integrează cu sistemul standard de gestiune a stocurilor din Odoo și este util în special companiilor cu nevoi complexe de gestiune a stocurilor, unde prognoza și planificarea corectă sunt esențiale pentru eficiența operațională.

#### 2. Funcționalități Cheie

- **Analiza cererii de stoc**: instrumente pentru analiza și prognoza cererii de produse pe baza datelor istorice și a tendințelor curente.
- **Urmărirea istoricului livrărilor**: monitorizarea detaliată a tiparelor de livrare a produselor pentru a optimiza planificarea viitoare a stocurilor.
- **Gestionarea disponibilității produselor**: capabilități extinse de monitorizare și planificare a disponibilității produselor.
- **Integrare cu planificarea stocurilor**: integrare cu sistemul de gestiune a stocurilor din Odoo pentru decizii mai bune de planificare.
- **Analiza stocurilor cu mișcare lentă (slow move)**: raport specializat care identifică produsele cu stoc pozitiv care nu au avut ieșiri semnificative într-o perioadă selectată, cu filtrare inteligentă pentru a exclude produsele nou recepționate sau nou create.
- **Valorificarea datelor istorice**: folosește datele anterioare de livrare și de cerere pentru a îmbunătăți prognoza stocurilor.

Beneficii: acuratețe îmbunătățită a prognozei stocurilor, reducerea rupturilor și a stocurilor în exces, o mai bună înțelegere a tiparelor de cerere, decizii mai bune de aprovizionare și producție, procese de gestiune a stocurilor mai fluide.

#### 3. Dependențe

- `purchase`
- `product`
- `stock`
- `purchase_stock`
- `sale`

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, modulul extinde mai multe modele de bază Odoo:

**Modele**

- `product.product` / `product.template`: extinderea modelului de produs pentru capabilități suplimentare de planificare a stocurilor. Începând cu versiunea 18.0.1.4.1, câmpurile `planning_relevant` și `replacement_product_id` sunt specifice variantei.
- `stock.demand`: model personalizat pentru urmărirea și analiza cererii de produse.
- `stock.delivery.history`: urmărirea istoricului livrărilor pentru analize de planificare.
- `stock.slow.move` (wizard): raportare pentru stocul cu mișcare lentă.

#### 5. Conexiuni

- `deltatech_nap_website`: modul soră care adaugă integrarea pe website pentru funcționalitățile NAP; completează acest modul de planificare a necesarului. (încă nedocumentat în wiki)
