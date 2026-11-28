# Nemo Express Shipping (localizat la `deltatech_delivery_ne/index.md`)

- **Nume Tehnic:** `deltatech_delivery_ne`
- **Versiune:** `20.0.0.0.8`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_ne`
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_ne`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite expedierea cu Nemo Express direct din livrările Odoo: tariful pe comanda de vânzare, AWB-ul și eticheta PDF, urmărirea și anularea, prin API-ul Nemo Express. Nemo Express funcționează pe platforma Courier Manager, deci modulul folosește conectorul `deltatech_delivery_cm`, cu adresa Nemo Express deja setată.

#### 2. Funcționalități Cheie

- Tarif pe comanda de vânzare calculat de Nemo Express, sau preț fix: întotdeauna ori doar când tariful curierului e sub o limită de preț.
- AWB emis din livrare și confirmat pentru ridicare, cu etichetă PDF în format A4, A6 sau patru etichete A6 pe o pagină A4; AWB-ul se poate anula, iar eticheta se salvează la emitere.
- Serviciile Nemo Express ale contului se importă (buton **Initialization**), iar pe fiecare metodă de livrare se alege unul; **Get city** adaugă localitățile lipsă din nomenclatorul Odoo.
- Opțiuni de expediere: mai multe colete, valoare declarată (asigurare), ramburs virat în cont bancar (metodele de plată tratate ca ramburs se aleg în configurare).
- Urmărire: istoricul stărilor se citește de la Nemo Express și se scrie pe livrare, până la predare.
- Configurare: *Inventar > Configurare > Livrare > Metode de livrare*, provider *Nemo Express*, fila **Nemo Express Configuration** (**API Key**; username și parolă sunt cerute de formular, dar API-ul folosește doar cheia).
- Date trimise curierului: nume, adresă, localitate, județ, cod poștal și telefon ale expeditorului și destinatarului, numărul de colete, greutatea, valoarea declarată și rambursul.
- Nesuportate: lockere și puncte de ridicare, etichete ZPL sau HTML, dimensiunile coletului, livrare sâmbăta, colet deschis, nota de restituire, link de urmărire pe site-ul Nemo Express.

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)
- [deltatech_delivery_cm](../deltatech_delivery_cm/index.md)

#### 4. Componente Cheie

**Modele**

- `delivery.carrier` (extins): adaugă opțiunea `ne` (Nemo Express) la câmpul `delivery_type` și metodele specifice (`ne_login`, `ne_rate_shipment`, `ne_send_shipping`, `ne_get_tracking_link`, `ne_cancel_shipment`, `ne_init_carrier`, `ne_import_carrier_city`, `ne_get_status_history`). Toate aceste metode delegă efectiv către omoloagele `cm_*` din `deltatech_delivery_cm` (Courier Manager) — Nemo Express refolosește integral logica API a Courier Manager. La schimbarea `delivery_type` pe `ne`, endpoint-ul implicit este setat la `https://app.nemoexpress.ro/nemo/API`.
- `delivery.carrier.service` (extins): adaugă opțiunea `ne` la selecția `delivery_type`.
- `stock.package.type` (extins): adaugă opțiunea `ne` la selecția `package_carrier_type`.
- `res.config.settings` (extins): expune switch-ul `module_deltatech_delivery_ne` pentru (dez)instalarea modulului din setări.

**Vizualizări**

- `view_delivery_carrier_form_with_provider_ne`: adaugă pe formularul transportatorului (`delivery.carrier`) o filă "Nemo Express Configuration" (vizibilă doar când `delivery_type = 'ne'`), cu câmpurile endpoint, subscription key, utilizator, parolă, partener companie, moduri de plată la livrare, serviciu și format etichetă.
- Vizualizare adăugată în `res_config_settings_views.xml` pentru activarea modulului din setările de Inventar/Livrare.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): furnizează infrastructura generică de integrare curieri (câmpuri comune de configurare a transportatorului) pe care se bazează acest modul.
- [deltatech_delivery_cm](../deltatech_delivery_cm/index.md): conține logica reală de comunicare cu API-ul curierului (Courier Manager); toate operațiunile Nemo Express (`ne_*`) sunt implementate ca simple delegări către metodele `cm_*` din acest modul.
