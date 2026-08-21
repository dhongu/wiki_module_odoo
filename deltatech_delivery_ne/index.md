# Nemo Express Shipping (localizat la `deltatech_delivery_ne/index.md`)

- **Nume Tehnic:** `deltatech_delivery_ne`
- **Versiune:** `19.0.0.0.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_ne
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_ne`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul conectează Odoo la serviciul de curierat **Nemo Express**, permițând expedierea coletelor direct din livrările de stoc și urmărirea lor online. Practic, adaugă Nemo Express ca opțiune de transportator, iar generarea AWB-urilor și schimbul de date cu API-ul curierului se fac prin infrastructura comună Courier Manager, deja folosită de alți curieri din suita Terrabit.

#### 2. Funcționalități Cheie

- Generare AWB în format PDF
- Generare AWB în format ZPL
- Ștergere AWB
- Obținere tarife (rate) pentru o expediere
- Obținere listă orașe
- Obținere listă județe
- Obținere istoric status pentru o expediere
- Expediere cu mai multe colete (multi-parcel)
- Expediere cu valoare declarată (asigurare)
- Expediere cu ramburs (cash on delivery)
- Expediere cu id de oraș și județ
- Expediere cu nume de oraș fără id de oraș

Funcționalități **neacoperite** momentan de integrare (conform DESCRIPTION.md):

- Generare AWB în format HTML
- Listă lockere
- Listă puncte de ridicare (pickup point)
- Expediere cu dimensiuni
- Notă de restituire în AWB
- Opțiune livrare sâmbăta
- Opțiune "pachet deschis"
- Livrare limitată strict la punctul de ridicare indicat
- Trimiterea id-ului de locker în AWB

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
