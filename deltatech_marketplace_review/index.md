# Sale Order Review - Marketplace (localizat la `deltatech_marketplace_review/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_review`
- **Versiune:** `19.0.0.1.1`
- **Cale:** [https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_review](https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_review)
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_review`
- **Ultima Ingestie:** `2026-09-24`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul face vizibile motivele pentru care o comandă preluată de pe un marketplace (eMAG, PrestaShop, Shopify etc.) rămâne nesconfirmată sau blocată înainte de livrare. În loc ca o comandă să stea ca ofertă fără nicio urmă vizibilă, ea apare cu un motiv clar — mesaj de la client, ramburs peste limita permisă, total diferit față de marketplace sau lipsa unui locker ales — atât pe comandă, cât și în coada „De Revizuit”. Se instalează automat când sunt prezente și `deltatech_marketplace_sale`, și [deltatech_sale_order_review](../deltatech_sale_order_review/index.md).

#### 2. Funcționalități Cheie

- Transformă cele două garduri deja existente la conectori — *client a lăsat un mesaj* și *ramburs peste „Max Auto-Confirm COD Amount"* — în motive de revizuire standard, vizibile pe comandă și în coada de revizuire.
- Mesajul clientului blochează comanda **înainte de confirmare**; ramburs-ul peste limită o blochează **înainte de livrare** (comanda e deja confirmată, stocul rezervat, coletul așteaptă aprobare).
- Două reguli proprii modulului: **total diferit față de marketplace** (nepotrivirea deja detectată de conectori devine motiv pe poarta de livrare, nu doar o notă în chatter) și **locker nealeasă încă** (motiv temporar pentru metodele de livrare care necesită punct de ridicare; inactivă implicit, necesită modulele de livrare marketplace și locker curier).
- Cât timp o comandă e blocată doar de motive temporare (fereastra de așteptare, o plată cu cardul încă în curs), conectorul reevaluează la fiecare 5 minute și confirmă automat comanda de îndată ce motivele se sting; un motiv care necesită intervenție umană oprește reîncercările.
- Limita de ramburs configurată pe backend (`auto_confirm_max_cod_amount`) rămâne pragul valabil pentru comenzile acelui backend — un singur loc de configurare per magazin, ca înainte.
- Pentru conectori: `_can_be_confirmed()` întreabă acum regula de revizuire; `_review_cod_amount()` întoarce suma de ramburs raportată de marketplace; `_review_is_online_order()` e adevărat pentru orice comandă importată.

#### 3. Dependențe

- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_sale_order_review](../deltatech_sale_order_review/index.md)

#### 4. Componente Cheie

**Modele**

- `sale.order` (extindere): adaugă legătura cu binding-ul de marketplace și implementează regulile de revizuire — mesaj client (`_review_check_customer_message`), ramburs peste limită (`_review_check_cod_high`, cu prag din backend), total diferit față de marketplace (`_review_check_total_mismatch`) și locker nealeasă (`_review_check_no_locker`).
- `marketplace.sale.order` (extindere `binding_sale_order.py`): reevaluează regulile de revizuire imediat după `save_from_marketplace` și `check_total_amount`; în `try_to_confirm`, reprogramează o nouă încercare de confirmare peste 300 de secunde (5 minute) cât timp comanda e blocată doar de motive temporare (`review_state == "waiting"`).

**Date**

- `data/review_rule_data.xml` (noupdate): trei reguli `sale.order.review.rule` —
  - `rule_customer_message` (poartă `confirm`, tip `manual`): mesajul clientului pe comanda marketplace.
  - `rule_total_mismatch` (poartă `delivery`, tip `manual`, prag `amount_threshold`): totalul Odoo diferă de cel raportat de marketplace.
  - `rule_no_locker` (poartă `delivery`, tip `temporary`, escaladare la 60 de minute, inactivă implicit): metoda de livrare necesită locker și comanda marketplace nu are încă unul ales.

#### 5. Conexiuni

- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): sursa datelor de binding (mesaj client, sumă ramburs, total extern, locker) pe care regulile de revizuire le citesc.
- [deltatech_sale_order_review](../deltatech_sale_order_review/index.md): motorul de reguli/porți de revizuire (`sale.order.review.rule`, coada „De Revizuit”) pe care acest modul îl extinde cu reguli specifice marketplace-ului.
- `deltatech_marketplace_delivery` și modulul de locker curier (ex. `deltatech_courier_locker`): necesare pentru ca regula `no_locker` să aibă efect (câmpurile `marketplace_locker` / `use_locker`); fără ele regula rămâne inactivă și fără obiect.
