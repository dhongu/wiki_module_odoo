# Sale Order Review - Marketplace (localizat la `deltatech_marketplace_review/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_review`
- **Versiune:** `20.0.0.4.0`
- **Cale:** [https://github.com/terrabit-solutions/bitshop_marketplace/tree/20.0/deltatech_marketplace_review](https://github.com/terrabit-solutions/bitshop_marketplace/tree/20.0/deltatech_marketplace_review)
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_review`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul face vizibile motivele pentru care o comandă preluată de pe un marketplace (eMAG, PrestaShop, Shopify etc.) rămâne nesconfirmată sau blocată înainte de livrare. În loc ca o comandă să stea ca ofertă fără nicio urmă vizibilă, ea apare cu un motiv clar — mesaj de la client, ramburs peste limita permisă, total diferit față de marketplace, status nepermis sau lipsa unui locker ales — atât pe comandă, cât și în coada „De Revizuit". Conectează verificarea comenzilor ([deltatech_sale_order_review](../deltatech_sale_order_review/index.md)) la conectorii de marketplace (`deltatech_marketplace_sale`) și se instalează explicit, acolo unde verificarea este dorită (nu mai este instalat automat).

#### 2. Funcționalități Cheie

- Transformă cele două garduri deja existente la conectori — *client a lăsat un mesaj* și *ramburs peste „Max Auto-Confirm COD Amount"* — în motive de revizuire standard, vizibile pe comandă și în coada de revizuire.
- Mesajul clientului blochează comanda **înainte de confirmare**; ramburs-ul peste limită o blochează **înainte de livrare** (comanda e deja confirmată, stocul rezervat, coletul așteaptă aprobare).
- Reguli proprii modulului: **total diferit față de marketplace** (nepotrivirea detectată de conectori devine motiv pe poarta de livrare, nu doar o notă în chatter), **locker nealeasă încă** (motiv temporar pentru metodele de livrare cu punct de ridicare; inactivă implicit, necesită modulele de livrare marketplace și locker curier), **clientul a scris după confirmare** (mesajele numărate de conector după confirmare opresc livrarea până când cineva le citește și aprobă; un mesaj nou redeschide motivul) și **status marketplace nepermis pentru confirmare automată** (cu lista *Auto-Confirm Only For Statuses* de pe backend completată, o comandă al cărei status nu e în listă rămâne ofertă până când statusul devine permis sau cineva o aprobă; listă goală = statusul nu contează).
- Cât timp o comandă e blocată doar de motive temporare (fereastra de așteptare, o plată cu cardul încă în curs), conectorul reevaluează la fiecare 5 minute și confirmă automat comanda de îndată ce motivele se sting; un motiv care necesită intervenție umană oprește reîncercările. Reîncercările se opresc după 24 de ore de la import dacă regula temporară nu are „Escalate After", cu o notă pe comandă care cere confirmare manuală.
- Limita de ramburs configurată pe backend (`auto_confirm_max_cod_amount`) rămâne pragul valabil pentru comenzile acelui backend — un singur loc de configurare per magazin.
- Pentru conectori: `_can_be_confirmed()` întreabă acum regula de revizuire; `_review_cod_amount()` întoarce suma de ramburs raportată de marketplace; `_review_is_online_order()` e adevărat pentru orice comandă importată.
- Funcționează cu oricare dintre motoarele de joburi (`queue_job` sau [deltatech_background_job](../deltatech_background_job/index.md)).

#### 3. Dependențe

- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md)
- [deltatech_sale_order_review](../deltatech_sale_order_review/index.md)

#### 4. Componente Cheie

**Modele**

- `sale.order` (extindere): implementează regulile de revizuire — mesaj client (`_review_check_customer_message`), mesaj după confirmare (`_review_check_customer_message_late`), status nepermis (`_review_check_phase_not_allowed`), ramburs peste limită (`_review_check_cod_high`, cu prag din backend), total diferit față de marketplace (`_review_check_total_mismatch`) și locker nealeasă (`_review_check_no_locker`).
- `marketplace.sale.order` (extindere `binding_sale_order.py`): reevaluează regulile de revizuire după `save_from_marketplace`, `check_total_amount` și la schimbarea `marketplace_late_message_count`; în `try_to_confirm`, reprogramează o nouă încercare de confirmare peste 300 de secunde cât timp comanda e blocată doar de motive temporare (`review_state == "waiting"`).
- `marketplace.backend` (extindere): câmpul *Auto-Confirm Only For Statuses* folosit de regula de status.

**Date**

- `data/review_rule_data.xml` (noupdate): reguli `sale.order.review.rule` —
  - `rule_customer_message` (poartă `confirm`): mesajul clientului pe comanda marketplace.
  - `rule_phase_not_allowed` (poartă `confirm`, temporară): statusul marketplace nu e în lista permisă pentru confirmare automată.
  - `rule_customer_message_late` (poartă `delivery`, aprobare manuală): clientul a scris după confirmare.
  - `rule_total_mismatch` (poartă `delivery`, aprobare manuală, prag `amount_threshold`): totalul Odoo diferă de cel raportat de marketplace.
  - `rule_no_locker` (poartă `delivery`, temporară, escaladare la 60 de minute, inactivă implicit): metoda de livrare necesită locker și comanda nu are încă unul ales.

**Vizualizări**

- `views/backend_views.xml`: extinde formularul backend-ului marketplace cu setările de confirmare automată folosite de reguli.

#### 5. Conexiuni

- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): sursa datelor de binding (mesaj client, sumă ramburs, total extern, locker, mesaje după confirmare) pe care regulile le citesc.
- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md): aduce statusurile marketplace pe care se bazează regula de status nepermis.
- [deltatech_sale_order_review](../deltatech_sale_order_review/index.md): motorul de reguli/porți de revizuire (coada „De Revizuit") pe care acest modul îl extinde cu reguli specifice marketplace-ului.
- `deltatech_marketplace_delivery` și modulul de locker curier (ex. `deltatech_courier_locker`): necesare pentru ca regula `no_locker` să aibă efect; fără ele regula rămâne inactivă.
