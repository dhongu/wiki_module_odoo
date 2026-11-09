# TNT Shipping (localizat la `deltatech_delivery_tnt/index.md`)

- **Nume Tehnic:** `deltatech_delivery_tnt`
- **Versiune:** `19.0.0.1.7`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_tnt
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_tnt`
- **Ultima Ingestie:** `2026-11-09`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul TNT Shipping integrează în Odoo serviciile de curierat internațional TNT Express (parte din grupul FedEx). Permite generarea expedierilor (AWB) și a etichetelor de transport direct din livrările Odoo, precum și calculul tarifelor de transport în timp real pe comenzile de vânzare, prin comunicare XML cu API-urile ExpressConnect ale TNT.

#### 2. Funcționalități Cheie

- **Tarif pe comanda de vânzare:** `tnt_rate_shipment` interoghează în timp real serviciul de prețuri TNT (ExpressConnect Pricing) pentru greutatea, dimensiunile și serviciul expedierii, convertește tariful în moneda comenzii și alege automat serviciul potrivit (normal, cu ramburs „CO” sau cu retur „RT”); alternativ se poate folosi un preț fix sub pragul metodei de livrare.
- **Creare AWB și etichetă la validarea livrării:** la validarea transferului (`stock.picking`) expedierea se creează la TNT (`tnt_send_shipping`), numărul ei se scrie ca referință de urmărire, iar eticheta se atașează livrării; butonul **Print AWB** regenerează eticheta.
- **Etichete în mai multe formate:** transformare XSLT a răspunsului XML de la TNT în etichete PDF, HTML sau ZPL (câmpul `tnt_label_type`), cu layout-urile TNT pentru Franța, Italia și restul lumii; doar formatul HTML este acoperit de testele automate.
- **Intern și internațional:** distincție automată domestic/internațional (`line_of_business`) după țara expeditorului și a destinatarului; numerele de telefon se despart în prefix și număr, cum cere TNT.
- **Date de expediere:** mai multe colete cu greutate și dimensiuni, valoare declarată și ramburs (metodele de plată tratate ca ramburs se aleg pe metoda de livrare), pe serviciul TNT ales (Express sau Economy Express, document sau non-document). Detaliile se verifică în **Carrier Details** pe livrare.
- **Validare XML:** cererea de preț este validată local față de schema XSD (`schemas/PriceRequestIN.xsd`) înainte de a fi trimisă la TNT.
- **Reîncercări sigure:** apelurile HTTP trec prin `_tnt_http_post` (timeout 90s); la timeout sau eroare de rețea pe apelul de expediere (cu efect secundar), rezultatul e marcat drept incert (`TntUncertainResult`), ca aceeași expediere să nu fie creată de două ori la o nouă apăsare a butonului.
- **Configurare:** *Inventar > Configurare > Livrare > Metode de expediere*, cu **Provider** = TNT; fila **TNT Configuration** cere **User** și **Password** ExpressConnect și **TNT Account**, plus serviciul și tipul etichetei.
- **Date trimise la TNT:** numărul contului, datele expeditorului și destinatarului (nume, adresă, contact, telefon), coletele (număr, greutate, dimensiuni, volum), valoarea declarată, rambursul și referința comenzii.

**Atenție — capabilități NEsuportate, confirmate în cod:** `_tnt_api_capabilities()` declară ca singură capacitate activă `"ship"` (creare expediere + etichetă). Nu sunt implementate: **anularea AWB-ului** (TNT ExpressConnect nu o expune; se face din portalul TNT), **urmărirea/istoricul de status** și linkul de tracking (`get_tracking_link()` din `stock_delivery` întoarce `None`), listarea AWB-urilor, importul de localități/județe/lockere/puncte de ridicare, livrarea de sâmbătă, pachetul deschis, documentele vamale și instrucțiunile speciale de livrare. Fluxul pas-cu-pas este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)

Dependență externă Python: `phonenumbers` (validarea și formatarea numerelor de telefon pentru cererile TNT).

#### 4. Componente Cheie

**Modele**

- `delivery.carrier` (extins, `models/delivery.py`): adaugă tipul de livrare `tnt`, câmpurile `tnt_account` și `tnt_label_type`, declarația de capabilități (`_tnt_api_capabilities`), calculul tarifului (`tnt_rate_shipment`), crearea expedierii și preluarea etichetei (`tnt_send_shipping`, `tnt_get_label`) și transformările XSLT aferente (PDF/HTML/ZPL).
- `delivery.carrier.service` (extins): adaugă valoarea `tnt` la selecția `delivery_type`, folosită de codurile de serviciu TNT definite în `data/delivery_data.xml`.

**Vizualizări**

- `view_delivery_carrier_form_with_provider_tnt` (`views/delivery_view.xml`): pagina „TNT Configuration” pe formularul transportatorului (`delivery.carrier`), vizibilă doar când `delivery_type = 'tnt'` — credențiale, cont TNT, tip de etichetă și serviciu.
- `views/templates.xml`: șabloane QWeb (nu UI) care construiesc payload-urile XML trimise la TNT — `shipRequest`, `priceRequest` / `priceRequest_address`, `labelRequest` / `labelRequest_address`.

**Date**

- `data/delivery_data.xml`: înregistrările `delivery.carrier.service` pentru codurile de produs TNT (`09D`, `10D`, `12D`, `15D`, `09N`, `10N`, `12N`, `15N`, `48N`, `412` — variante Express document/non-document și Economy Express).

Nu există `ir.cron`, `base.automation` sau `ir.actions.server` definite în modul.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): cadrul de bază pentru metodele de livrare Deltatech (credențiale, detalii expediere din comandă/livrare, atașare etichetă, notificare) pe care acest modul îl extinde cu integrarea TNT (dependență directă).
