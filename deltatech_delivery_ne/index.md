# Nemo Express Shipping (localizat la `deltatech_delivery_ne/index.md`)

- **Nume Tehnic:** `deltatech_delivery_ne`
- **Versiune:** `19.0.0.0.9`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_ne
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_ne`
- **Ultima Ingestie:** `2026-11-15`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite expedierea cu **Nemo Express** direct din livrările Odoo: tariful pe comanda de vânzare, AWB-ul cu eticheta PDF, urmărirea și anularea, prin API-ul Nemo Express. Nemo Express rulează pe platforma Courier Manager, deci modulul folosește conectorul [deltatech_delivery_cm](../deltatech_delivery_cm/index.md), cu adresa Nemo Express deja setată.

#### 2. Funcționalități Cheie

- **Tarif pe comanda de vânzare**: costul transportului este cotat de Nemo Express sau se folosește un preț fix, cu un prag opțional peste care se interoghează Nemo Express.
- **AWB și etichetă**: AWB-ul se rezervă din livrare și se confirmă pentru ridicare, cu eticheta PDF în format A4, A6 sau patru etichete A6 pe o pagină A4; eticheta poate fi adusă din nou, iar AWB-ul anulat.
- **Servicii**: serviciile Nemo Express ale contului se importă, iar unul se alege per metodă de livrare.
- **Opțiuni de expediere**: mai multe colete, valoare declarată (asigurare), ramburs virat în contul bancar al companiei și cine plătește transportul (expeditor sau destinatar).
- **Urmărire**: istoricul de stare este citit de la Nemo Express și scris pe livrare, până la livrarea coletului.
- **Configurare** (*Inventar > Configurare > Livrare > Metode de expediere*, **Provider** = *Nemo Express*, produs de livrare de tip serviciu; **Endpoint** vine precompletat): în tabul **Nemo Express Configuration** se completează **API Key** (câmpurile **Username** și **Password** sunt cerute de formular, dar API-ul folosește doar cheia); butonul **Initialization** importă serviciile contului, apoi se alege **Service**; **Get city** adaugă localitățile Nemo Express lipsă din agenda Odoo; se aleg formatul etichetei, cine plătește transportul și metodele de plată tratate ca ramburs.
- **Utilizare**: pe livrare, **Carrier Details** deschide expediția (serviciu, număr de colete, greutate, valoare colet, valoare de încasat); la validarea transferului AWB-ul este rezervat și confirmat pentru ridicare, referința de urmărire se scrie pe livrare și eticheta PDF se atașează; **Print AWB** o tipărește, **Cancel AWB** o anulează.
- **Date trimise către Nemo Express**: la fiecare ofertă și expediție se transmit numele, strada, numărul, localitatea, județul, codul poștal și telefonul expeditorului și destinatarului, numărul de colete, greutatea, valoarea declarată și rambursul.
- **Neacceptate**: lockere și puncte de ridicare, etichete ZPL sau HTML, dimensiunile coletelor, livrarea sâmbăta, coletul deschis, nota de restituire și un link de urmărire către site-ul Nemo Express.

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)
- [deltatech_delivery_cm](../deltatech_delivery_cm/index.md)

#### 4. Componente Cheie

Secțiunile 1 și 2 provin din `readme/DESCRIPTION.md`, completat cu `CONFIGURE.md` și `USAGE.md`; componentele de mai jos au fost verificate în cod.

**Modele**

- `delivery.carrier` (extins): adaugă tipul de livrare `ne` (Nemo Express) și metodele `ne_login`, `ne_rate_shipment`, `ne_send_shipping`, `ne_cancel_shipment`, `ne_init_carrier`, `ne_import_carrier_city`, `ne_get_status_history`, toate delegate către omoloagele `cm_*` din [deltatech_delivery_cm](../deltatech_delivery_cm/index.md); `ne_get_tracking_link` returnează `False`. Capabilitățile declarate sunt `ship`, `cancel`, `cities` și `tracking`. La schimbarea tipului pe `ne`, endpoint-ul devine `https://app.nemoexpress.ro/nemo/API`.
- `delivery.carrier.service` (extins): adaugă `ne` la `delivery_type`.
- `stock.package.type` (extins): adaugă `ne` la `package_carrier_type`.
- `res.config.settings` (extins): switch-ul `module_deltatech_delivery_ne` pentru instalarea modulului din setări.

**Vizualizări**

- `view_delivery_carrier_form_with_provider_ne`: tabul **Nemo Express Configuration** pe metoda de livrare (vizibil doar pentru `ne`), cu endpoint, subscription key, utilizator, parolă, partener companie, metode de plată ramburs, serviciu și format etichetă.
- Vizualizare în `res_config_settings_views.xml` pentru activarea modulului din setări.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește acțiuni automate sau acțiuni server.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): infrastructura comună de integrare a curierilor.
- [deltatech_delivery_cm](../deltatech_delivery_cm/index.md): conține logica reală de comunicare cu API-ul Courier Manager; operațiunile Nemo Express sunt delegări către metodele `cm_*`.
