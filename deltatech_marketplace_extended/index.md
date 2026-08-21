# Extended Marketplace Connector (localizat la `deltatech_marketplace_extended/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_extended`
- **Versiune:** `19.0.0.0.14`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_extended`
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_extended`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul este un conector specific care leagă platforma de e-commerce externă „Extended" de Odoo, folosind cadrul generic de marketplace al suitei Terrabit. El adaugă providerul „Extended" în lista de conectori de marketplace și permite sincronizarea automată, în ambele sensuri, a datelor comerciale: produse, furnizori, clienți, comenzi, curieri de livrare, metode de plată, categorii publice de site și etape de vânzare. La exportul de stoc, conectorul poate trimite acum și un mesaj de termen de livrare calculat în Odoo (pe baza reaprovizionării așteptate sau a timpului de livrare al produsului) și poate mapa mesajele proprii pe dicționarul de disponibilitate al platformei Extended (`stoc_informativ_id`), astfel încât textele afișate clienților în magazinul online să corespundă realității din stoc.

#### 2. Funcționalități Cheie

- Adaugă providerul „Extended" la configurarea backend-ului de marketplace, cu opțiuni proprii (data de start a importului, numărul de produse importate, codul de furnizor propriu).
- Import de produse de pe platforma Extended, paginat și procesat asincron prin cozi de joburi.
- Import de furnizori (`/?furnizori`) în maparea `marketplace.supplier`, folosită pentru identificarea sursei de stoc la export.
- Import de clienți pe intervale de timp (segmente de 15 zile), pornind de la o dată configurabilă.
- Import de comenzi de vânzare, cu posibilitatea de preluare în timp real prin webhook (la primirea unui `order_id`).
- Sincronizarea curierilor de livrare și a metodelor de plată între Extended și Odoo (cu mapare către produse de tip serviciu, respectiv către providerul de plată prin transfer bancar).
- Import al categoriilor publice de site (arborescent, cu păstrarea ierarhiei părinte-copil) și al etapelor/statusurilor de vânzare.
- Export de stoc (`update_stoc`) sub codul de furnizor configurat pe backend (**Extended Supplier Code**, implicit `1` = stocul propriu al magazinului); furnizorii externi (drop-ship, gestionați direct în Extended) nu sunt atinși de export.
- Mesaj de termen de livrare la export de stoc, opțional (**Send Delivery Term**), pentru produsele fără stoc disponibil: dată de reaprovizionare formatată pe jumătate de lună (dacă există o mișcare de intrare programată, plus o marjă configurabilă — **Delivery Term Margin**, implicit 14 zile) sau interval săptămânal derivat din timpul de livrare al produsului; punct de extensie (`_extended_availability_date`) pentru module de feed furnizor care vor să-și aducă propria sursă de dată.
- Dicționar de mesaje de disponibilitate Extended (`stoc_informativ_id`), învățat automat la importul de produse și editabil pe formularul backend-ului; fiecărei intrări i se poate atribui un rol (în stoc / fără stoc / interval de livrare / perioadă de livrare), folosit apoi la exportul de stoc pentru a trimite mesajul corect către Extended.
- Comunicare cu API-ul Extended pe bază de cheie API, cu documentație publicată (specificație Swagger / webhook API).

#### 3. Dependențe

- `sale`
- `purchase_stock`
- [deltatech_marketplace](../deltatech_marketplace/index.md)
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_marketplace_website](../deltatech_marketplace_website/index.md)
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md)
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md)
- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md)

#### 4. Componente Cheie

**Modele**

- `marketplace.backend` (extins): adaugă providerul `extended`, câmpurile `extended_start_date`, `extended_products_number`, `extended_supplier_code`, `extended_send_delivery_term`, `extended_delivery_margin_days`, `extended_stock_info_ids` și `auto_replenishment`, metoda de apel API `extended_call` (autentificare cu `apikey`) și importul recursiv de categorii publice.
- `marketplace.product` (extins): import paginat și export de produse către/din Extended, inclusiv calculul mesajului de termen de livrare la export de stoc.
- `marketplace.supplier` (extins): import al listei de furnizori Extended (`/?furnizori`), sursa pentru codul de furnizor folosit la exportul de stoc.
- `marketplace.customer` (extins): import de clienți pe intervale de date prin joburi asincrone.
- `marketplace.sale.order` (extins): import comenzi și endpoint de webhook (`extended_webhook`) pentru preluarea comenzilor în timp real.
- `marketplace.delivery.carrier` (extins): mapare a curierilor Extended către curieri/produse serviciu Odoo.
- `marketplace.payment.provider` (extins): mapare a metodelor de plată Extended (implicit către providerul de transfer bancar).
- `marketplace.public.category` (extins): import recursiv al categoriilor publice de site, cu păstrarea ierarhiei.
- `marketplace.sale.phase` (extins): import al statusurilor/etapelor de vânzare.
- `marketplace.extended.stock.info`: dicționarul de mesaje de disponibilitate Extended (`stoc_informativ_id` → text), cu rol asociat (în stoc / fără stoc / interval sau perioadă de livrare), folosit la exportul de stoc.

**Vizualizări**

- `view_marketplace_backend_form`: extinde formularul backend-ului de marketplace pentru a afișa câmpurile specifice Extended (dată de start import, număr de produse, cod furnizor, termen de livrare și marja lui, dicționarul de mesaje de disponibilitate, reaprovizionare automată), vizibile doar când providerul este `extended`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite înregistrări `ir.cron`, `base.automation` sau `ir.actions.server` proprii în acest modul. Sincronizarea se realizează prin joburi în coadă (`with_delay`) și prin webhook, declanșate din cadrul generic de marketplace; dicționarul de mesaje de disponibilitate se poate importa și manual, printr-un buton dedicat pe backend (nu există un endpoint Extended separat pentru el — importul „mătură" paginile de produse).

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): cadrul de bază al familiei de marketplace; furnizează modelul `marketplace.backend` și mecanica generică de conectare extinsă aici pentru providerul „Extended".
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): furnizează modelul `marketplace.sale.order` extins aici pentru importul de comenzi și webhook.
- [deltatech_marketplace_website](../deltatech_marketplace_website/index.md): furnizează modelul `marketplace.public.category` extins aici pentru importul categoriilor publice de site.
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md): furnizează modelul `marketplace.delivery.carrier` extins aici pentru maparea curierilor.
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md): furnizează modelul `marketplace.payment.provider` extins aici pentru maparea metodelor de plată.
- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md): furnizează modelul `marketplace.sale.phase` extins aici pentru importul etapelor de vânzare.
