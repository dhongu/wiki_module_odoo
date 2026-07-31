# TNT Shipping (localizat la `deltatech_delivery_tnt/index.md`)

- **Nume Tehnic:** `deltatech_delivery_tnt`
- **Versiune:** `19.0.0.1.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_tnt
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_tnt`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul TNT Shipping integrează în Odoo serviciile de curierat internațional TNT Express (parte din grupul FedEx). Permite generarea expedierilor (AWB) și a etichetelor de transport direct din livrările Odoo, precum și calculul tarifelor de transport în timp real pe comenzile de vânzare, prin comunicare XML cu API-urile ExpressConnect ale TNT.

#### 2. Funcționalități Cheie

- **Creare AWB și etichetă (singura capacitate declarată și testată):** generarea expedierii (`tnt_send_shipping`) direct din livrarea (`stock.picking`) asociată comenzii, urmată automat de preluarea și atașarea etichetei de transport la livrare.
- **Etichete în mai multe formate:** transformare XSLT a răspunsului XML de la TNT în etichete PDF, HTML sau ZPL (câmpul `tnt_label_type`); fișierele `.xsl` pentru toate cele trei formate (inclusiv variante Franța/Italia/Rest of World) există în modul, dar doar formatul HTML este acoperit de testele automate.
- **Calcul tarif de transport:** `tnt_rate_shipment` interoghează în timp real serviciul de prețuri TNT (ExpressConnect Pricing) și distinge automat tariful normal, cu ramburs (opțiune „CO”) sau cu retur (opțiune „RT”).
- **Expediere internațională:** distincție automată domestic/internațional (`line_of_business`) în funcție de țara expeditorului și a destinatarului.
- **Colete multiple și dimensiuni:** suport pentru mai multe colete pe expediere și pentru dimensiunile/greutatea coletului în calculul volumului.
- **Validare XML:** cererea de preț este validată local față de schema XSD (`schemas/PriceRequestIN.xsd`) înainte de a fi trimisă la TNT.
- **Gestiune erori și rezultate incerte:** apelurile HTTP trec printr-un helper comun (`_tnt_http_post`) cu timeout de 90s; la timeout/eroare de rețea pe apelul de expediere (care are efect secundar), rezultatul e marcat explicit drept incert (`TntUncertainResult`) în loc să fie presupus eșuat sau reușit.

**Atenție — capabilități NEsuportate, confirmate în cod (nu doar declarate în readme):** modulul declară explicit, prin `_tnt_api_capabilities()`, că singura capacitate activă este `"ship"` (creare expediere + etichetă). Nu există în cod și nu sunt implementate: **anularea AWB-ului** (`cancel_shipment`), **urmărirea/istoricul de status** (`get_status_history`), listarea/căutarea AWB-urilor, importul de orașe/județe/lockere/puncte de ridicare sau extrasul de ramburs (COD). Testele automate confirmă explicit acest lucru: *„the TNT module does not implement cancel_shipment or status history methods, so there is nothing to cover for those flows”*.

> Corecție aplicată în `readme/DESCRIPTION.md` (versiunea 19.0.0.1.2, 2026-07-31): descrierea revendica anularea AWB-ului, urmărirea statusului livrării, istoricul de livrare și generarea de link de tracking — niciuna nu există în cod — și, invers, nega formatul ZPL, care este implementat. Au fost eliminate din „Key Features”/„Technical Implementation”, iar ZPL a trecut în „Features” cu mențiunea că nu e acoperit de teste automate. Suplimentar față de contradicțiile inițiale: „Delete AWB” și „Get rates for a shipment” apăreau simultan în ambele liste (anularea e doar nesuportată; calculul de tarif e doar suportat — `tnt_rate_shipment`, acoperit de `test_rate_shipment`); linkul de tracking **nu** e generat de modul (nu există `tnt_get_tracking_link`, deci `get_tracking_link()` din `stock_delivery` întoarce `None` — spre deosebire de modulele surori GLS/DPD/UC etc., care îl implementează); „Customs declaration integration” nu are corespondent în `views/templates.xml`; „Special delivery instructions” nu e expus utilizatorului (`DELIVERYINST` e trimis gol, iar `specialInstructions` conține doar textul de ramburs generat automat). Sursa contradicțiilor: descrierea fusese copiată din `deltatech_delivery_gls`, unde anularea și tracking-ul chiar există. Documentul are acum o singură pereche „Features”/„Without Features”, nu două liste divergente.

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
