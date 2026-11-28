# eCommerce Sale Order status (localizat la `deltatech_website_sale_status/index.md`)

- **Nume Tehnic:** `deltatech_website_sale_status`
- **Versiune:** `20.0.2.0.14`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_website_sale_status`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_sale_status`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Starea standard a comenzii (ofertă, comandă de vânzare, anulată) nu arată clientului din magazinul online, nici echipei de vânzări, unde se află comanda: așteaptă stoc, e gata de livrare, e la curier sau a fost livrată. Modulul adaugă pe comanda de vânzare o **Etapă** calculată din comandă, din transferurile ei și din starea curierului, și o afișează atât în back office, cât și în portalul clientului.

#### 2. Funcționalități Cheie

- **Etapa comenzii**: câmp calculat și stocat, cu urmărire în chatter:
  - **Plasată** – ofertă de website trimisă clientului (doar cu etapa detaliată);
  - **În procesare** – comanda este preluată de echipa de vânzări;
  - **Cerere de ofertă** – comandă confirmată fără nimic de livrat încă, a cărei cerere de ofertă către furnizor a fost trimisă (doar cu `sale_purchase` instalat);
  - **Așteaptă disponibilitate** – un transfer al comenzii așteaptă stoc;
  - **Amânată** – livrarea a fost amânată (indicatorul de livrare amânată de pe transferuri);
  - **De livrat** – produsele sunt disponibile și comanda poate fi expediată;
  - **Pre-aviz** – a fost generat un AWB pentru colet (doar etapa detaliată);
  - **În livrare** – coletul este la curier;
  - **Livrată** – toate transferurile sunt finalizate sau, cu etapa detaliată, curierul a livrat coletul;
  - **Anulată** – comanda a fost anulată.
  - Coșurile de website netrimise nu au etapă.
- **Etapă detaliată a comenzii**: opțiune în **Vânzări > Configurare > Setări**, secțiunea *Facturare*, *Detailed order stage* (implicit dezactivată). Dezactivată, comanda e **Livrată** la validarea transferurilor. Activată, oferta de website trimisă e **Plasată**, iar după validare etapa urmărește starea curierului (**Pre-aviz**, **În livrare**) până la livrare. Se urmăresc doar transferurile validate în ultimele 30 de zile.
- **Back office**: etapa apare ca insignă colorată în listele de oferte și comenzi și pe formularul comenzii, lângă termenii de plată. Căutarea comenzilor primește filtrele **Plasată**, **În procesare** și **De livrat**, plus o căutare după **Telefon** pe client. Etapa este disponibilă și în raportul de analiză a vânzărilor.
- **Portal client**: în *Contul meu > Comenzi de vânzare*, lista arată etapa ca insignă, poate fi filtrată după **Comenzi deschise**, **Comenzi închise** sau după fiecare etapă și sortată după **Etapa comenzii**. Filtrele **Anulată** și **Comenzi închise** includ și comenzile anulate; paginatorul păstrează filtrul ales.
- **Comenzi neplătite**: acțiunea standard eCommerce *Unpaid Orders* listează și comenzile de website confirmate care nu sunt plătite integral.
- **Limitări**: valoarea **Returnată** există în listă, dar nicio regulă nu o setează; în Odoo 20 acțiunea *Unpaid Orders* nu are meniu (se deschide doar dintr-un link sau un meniu personalizat); domeniul ei folosește câmpul de stare a plății adăugat de `deltatech_sale_payment`, care nu este dependență, deci fără acel modul acțiunea dă eroare.

#### 3. Dependențe

- `portal`
- `website_sale_stock`
- [deltatech_delivery_status](../deltatech_delivery_status/index.md)
- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `sale.order`: model extins cu etapa comenzii (calculată din comandă, transferuri și starea curierului).
- `sale.report`: raport de vânzări extins cu etapa comenzii.
- `res.config.settings`: opțiunea *Detailed order stage*.

**Vizualizări**

- `views/sale_view.xml`: extinderi ale vizualizărilor comenzii de vânzare cu insigna etapei, filtrele și căutarea după telefon.
- `views/res_config_settings_views.xml`: opțiunea etapei detaliate în setările de vânzări.
- `views/templates.xml`: șabloane QWeb pentru afișarea etapei în portalul clientului.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni `ir.cron`, reguli `base.automation` sau acțiuni server în acest modul.

#### 5. Conexiuni

- [deltatech_delivery_status](../deltatech_delivery_status/index.md): furnizează starea curierului pe care modulul o folosește pentru etapele de livrare.
- `deltatech_sale_payment`: furnizează câmpul de stare a plății folosit de acțiunea *Unpaid Orders* (nu este dependență).
