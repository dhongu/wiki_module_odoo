# Product Price History (localizat la `deltatech_product_price_history/index.md`)

- **Nume Tehnic:** `deltatech_product_price_history`
- **Versiune:** `20.0.1.1.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_product_price_history
- **Cale Locală:** `odoo-addons/bitshop/deltatech_product_price_history`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul anunță reducerile din magazinul online așa cum cere legea UE: conform Directivei Omnibus (UE 2019/2161, care a introdus art. 6a în Directiva 98/6/CE), o reducere se anunță față de cel mai mic preț aplicat în ultimele 30 de zile dinainte. Odoo standard taie prețul de vânzare și nu păstrează istoric de prețuri. Modulul înregistrează istoricul prețurilor listelor de prețuri și taie pe grila magazinului și pe pagina produsului prețul corect; când o reducere nu poate fi dovedită, nu taie nimic.

#### 2. Funcționalități Cheie

- **Prețul de referință tăiat**: lângă o reducere se afișează cel mai mic preț practicat în cele 30 de zile dinainte de începerea reducerii, nu prețul de vânzare. Funcționează pentru orice reducere venită dintr-o regulă *Discount* a listei de prețuri (cu sau fără rotunjire și taxă suplimentară), nu doar pentru campanii.
- **Fără reducere fără dovadă**: dacă istoricul nu are un preț anterior mai mare, magazinul arată doar prețul, fără preț tăiat (nici măcar *Compare to Price*).
- **Comenzi neschimbate**: prețul de referință e doar pentru afișare; linia comenzii păstrează prețul și reducerea standard ale listei.
- **Liste urmărite**: bifa *Track Price History* pe lista de prețuri; prețul fiecărei variante vandabile se înregistrează în fiecare noapte, doar dacă s-a schimbat.
- **Schimbări înregistrate imediat**: un preț nou pe produs și o regulă de listă creată, modificată sau ștearsă (pe produs, variantă sau categorie) se înregistrează pe loc; o regulă programată, în ora de după început sau sfârșit; o regulă pe toate produsele rămâne pe seama rulării de noapte.
- **Butoane**: *Price History* pe produs, variantă și listă; *Record Prices Now* pe lista urmărită (de rulat o dată, ca punct de plecare).
- **Instalare**: o reducere deja activă nu are preț anterior în istoric și apare fără preț tăiat până apare un preț mai mare din ultimele 30 de zile; modulul se instalează și listele se urmăresc din timp, înainte de anunțarea reducerilor.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

- `product.price.history`: preț per listă și variantă, cu data de la care e valabil.
- `product.pricelist`: bifa *Track Price History* și acțiunea *Record Prices Now*.
- `product.pricelist.item`: declanșează înregistrarea la crearea, modificarea sau ștergerea regulilor.
- `product.template`, `product.product`: butonul *Price History* și calculul prețului de referință.

**Vizualizări**

- `product_pricelist_view`: bifa, butonul și butonul inteligent pe lista de prețuri.
- `product_template_form_view`: butonul *Price History* pe produs.
- `view_product_price_history_list` / `_search`, `action_product_price_history`: istoricul prețurilor.

**Acțiuni Automate / Acțiuni Server**

- *Price History: record the prices of the tracked pricelists*: `ir.cron` zilnic (`_cron_record_prices`).
- *Price History: record the pricelist rules that started or ended*: `ir.cron` din oră în oră (`_cron_record_rule_boundaries`).

#### 5. Conexiuni

- [deltatech_website_sale_campaign](../deltatech_website_sale_campaign/index.md): campaniile folosesc cel mai mic preț dinainte de start ca referință pentru toate etapele.
