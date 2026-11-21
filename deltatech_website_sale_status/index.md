# eCommerce Sale Order status (localizat la `deltatech_website_sale_status/index.md`)

- **Nume Tehnic:** `deltatech_website_sale_status`
- **Versiune:** `19.0.2.0.14`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_sale_status
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_sale_status`
- **Ultima Ingestie:** `2026-11-21`

#### 1. Sumar

Starea standard a comenzii (Ofertă, Comandă de vânzare, Anulată) nu îi spune clientului din magazinul online, nici echipei de vânzări, unde se află comanda: așteaptă stoc, e gata de expediere, la curier sau livrată. Modulul adaugă pe comanda de vânzare un câmp **Etapă** (*Stage*), calculat din comandă, din transferurile ei și din starea curierului, și îl afișează în back office și în portalul clientului.

#### 2. Funcționalități Cheie

- **Etapa comenzii** este calculată și stocată pe fiecare comandă, cu urmărire în chatter:
  - **Plasată** (*Placed*) – ofertă de website trimisă clientului (doar cu opțiunea de etapă detaliată);
  - **În procesare** (*In Process*) – comanda este tratată de echipa de vânzări;
  - **Request for Quotation** – comandă confirmată fără nimic de livrat încă, a cărei cerere de ofertă de achiziție a fost trimisă furnizorului (doar dacă este instalat `sale_purchase`);
  - **Așteaptă disponibilitate** (*Waiting availability*) – un transfer al comenzii așteaptă stoc;
  - **Amânată** (*Postponed*) – livrarea a fost amânată (marcajul *Postponed delivery* al transferurilor);
  - **De livrat** (*To Be Delivery*) – produsele sunt disponibile și comanda poate fi expediată;
  - **Pre advice** – a fost generat un AWB pentru colet (doar etapă detaliată);
  - **În livrare** (*In Delivery*) – coletul este la curier;
  - **Livrată** (*Delivered*) – toate transferurile sunt finalizate sau, cu etapa detaliată, curierul a livrat coletul;
  - **Anulată** (*Canceled*) – comanda a fost anulată.
  - Coșurile de website netrimise nu au etapă.
- **Etapă detaliată:** opțiune în *Sales > Configuration > Settings*, secțiunea *Invoicing*, *Detailed order stage* (dezactivată implicit). Dezactivată, comanda este *Livrată* la validarea transferurilor; activată, o ofertă de website trimisă este *Plasată*, iar după validare etapa urmărește starea curierului (*Pre advice*, *În livrare*) până la livrarea de către curier. Sunt urmărite doar transferurile validate în ultimele 30 de zile.
- **Back office:** etapa apare ca insignă colorată în listele de oferte și comenzi și în formularul comenzii, lângă termenii de plată. Căutarea comenzilor primește filtrele **Placed**, **In process** și **To Be Delivery** și o căutare după **Telefon** pe client. Etapa este disponibilă și în raportul de analiză a vânzărilor.
- **Portal client:** în *My Account > Sales Orders*, lista comenzilor arată etapa ca insignă, poate fi filtrată după **Open Orders**, **Closed Orders** sau după fiecare etapă și sortată după **Order Stage**; filtrele **Canceled** și **Closed Orders** includ și comenzile anulate; pager-ul păstrează filtrul ales.
- **Unpaid Orders:** meniul *Website > eCommerce > Unpaid Orders* listează și comenzile de website confirmate care nu sunt plătite integral.
- **Limitări:**
  - valoarea **Returnată** (*Returned*) există în listă, dar nicio regulă nu o setează: o comandă returnată nu este afișată ca atare (pagina anterioară o prezenta greșit ca etapă funcțională; corectat);
  - domeniul *Unpaid Orders* folosește câmpul de stare a plății adăugat de [deltatech_sale_payment](../deltatech_sale_payment/index.md), care nu este dependență; fără acel modul meniul dă eroare.

#### 3. Dependențe

- `portal`
- `website_sale_stock`
- [deltatech_delivery_status](../deltatech_delivery_status/index.md)
- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): câmpul stocat `stage` (cu urmărire), calculat de `_compute_stage`; `_get_stage_from_delivery_state` aplică starea curierului peste etapele din stoc; `_action_confirm` forțează recalcularea etapei la confirmare.
- `sale.report` (extins): câmpul `stage`, pentru raportarea pe etapele comenzilor.
- `res.config.settings` (extins): opțiunea `sale_detailed_stage` (*Detailed order stage*).

**Vizualizări**

- `view_quotation_tree`, `view_order_tree`, `view_order_form`: insigna etapei în liste și în formularul comenzii.
- `view_sales_order_filter`: filtrele după etapă și căutarea după telefon (`partner_id.phone`).
- `res_config_settings_view_form`: opțiunea *Detailed order stage* în setările de vânzări.
- `website_sale.action_view_unpaid_quotation_tree` (extins): acțiunea meniului *Unpaid Orders*.
- `portal_my_quotations_status`, `portal_my_orders_status`: șabloane QWeb care afișează etapa în listele din portal.

**Controllere**

- `CustomerPortal` (extinde controllerul din `portal`): filtrele și sortarea după etapă în *Sales Orders*, domeniul comenzilor și păstrarea filtrului în pager.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni `ir.cron`, reguli `base.automation` sau acțiuni server în acest modul.

#### 5. Conexiuni

- [deltatech_delivery_status](../deltatech_delivery_status/index.md): furnizează starea curierului pe care acest modul o folosește pentru etapele *Pre advice*, *În livrare* și *Livrată*.
- [deltatech_sale_payment](../deltatech_sale_payment/index.md): adaugă câmpul de stare a plății de care depinde meniul *Unpaid Orders* (nu este dependență).
- `sale_purchase`: dacă este instalat, activează etapa *Request for Quotation*.
