# TNT Shipping (localizat la `deltatech_delivery_tnt/index.md`)

- **Nume Tehnic:** `deltatech_delivery_tnt`
- **Versiune:** `20.0.0.1.8`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_tnt
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_tnt`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul integrează în Odoo serviciile de curierat TNT Express (parte din FedEx). Permite calculul tarifelor pe comenzile de vânzare și generarea expedierii (AWB) și a etichetei direct din livrare, prin API-urile XML ExpressConnect. Integrarea acoperă o singură operațiune de expediere: crearea expedierii și preluarea etichetei. TNT nu expune anularea expedierilor, iar modulul nu urmărește starea livrării, deci anularea AWB-ului și urmărirea se fac din portalul TNT.

#### 2. Funcționalități Cheie

- Servicii TNT Express: Express (document / non-document) și Economy Express, cu autentificare pe serviciile web TNT.
- Calcul de tarife în timp real pe comanda de vânzare, cu alegerea automată a serviciului potrivit (standard, ramburs sau retur) și conversia tarifului în moneda comenzii; opțional, un preț fix sub un prag.
- Rutare automată intern / internațional în funcție de țara expeditorului și a destinatarului.
- Generarea AWB-ului la validarea transferului: numărul de consignație TNT se scrie ca referință de urmărire, iar eticheta se atașează livrării și se postează în chatter; **Print AWB** redă eticheta din nou.
- Etichetă în format PDF, HTML sau ZPL (transformări XSLT; ZPL nu este acoperit de teste automate).
- Opțiuni de expediere: colete multiple, dimensiuni, valoare declarată (asigurare), ramburs, oraș dat doar prin nume.
- Capabilități declarate explicit (doar crearea expedierii): operațiunile nesuportate sunt ascunse în interfață și refuzate la apel din cron sau acțiuni server; rezultatele ambigue (timeout, conexiune pierdută) sunt raportate ca incerte, nu ca eșuate.
- Neacoperit: anularea AWB, istoricul de stare, link de urmărire, liste de orașe / județe / lockere / puncte de ridicare, livrare sâmbăta, deschiderea coletului, documente vamale.
- Configurare: din **Inventar → Configurare → Livrare → Metode de livrare**, cu *Provider* = TNT, fila **TNT Configuration** (utilizator și parolă ExpressConnect, cont TNT, serviciu, tip etichetă, metode de plată tratate ca ramburs). Pașii cu capturi în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)

Dependență externă Python: `phonenumbers` (validarea și formatarea numerelor de telefon pentru cererile TNT).

#### 4. Componente Cheie

**Modele**

- `delivery.carrier` (extins, `models/delivery.py`): tipul de livrare `tnt`, câmpurile `tnt_account` și `tnt_label_type`, declarația de capabilități (`_tnt_api_capabilities`), calculul tarifului (`tnt_rate_shipment`), crearea expedierii și preluarea etichetei (`tnt_send_shipping`, `tnt_get_label`) și transformările XSLT aferente.
- `delivery.carrier.service` (extins): valoarea `tnt` la selecția `delivery_type`, folosită de codurile de serviciu TNT.

**Vizualizări**

- `views/delivery_view.xml`: pagina „TNT Configuration” pe formularul transportatorului, vizibilă doar când `delivery_type = 'tnt'`.
- `views/templates.xml`: șabloane QWeb care construiesc payload-urile XML trimise la TNT (`shipRequest`, `priceRequest`, `labelRequest` și variantele cu adresă).

**Acțiuni Automate / Acțiuni Server**

- Nu există `ir.cron`, `base.automation` sau `ir.actions.server`. `data/delivery_data.xml` definește serviciile TNT (`09D`, `10D`, `12D`, `15D`, `09N`, `10N`, `12N`, `15N`, `48N`, `412`).

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): cadrul de bază al metodelor de livrare Deltatech, extins aici cu integrarea TNT (dependență directă).
