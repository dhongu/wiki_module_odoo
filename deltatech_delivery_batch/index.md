# Delivery Batch AWB (localizat la `deltatech_delivery_batch/index.md`)

- **Nume Tehnic:** `deltatech_delivery_batch`
- **Versiune:** `19.0.1.0.9`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_batch
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_batch`
- **Ultima Ingestie:** `2026-11-08`

#### 1. Sumar

Modulul „Delivery Batch AWB" fluidizează logistica de depozit prin generarea AWB-urilor (scrisorilor de transport) direct dintr-un transfer în lot, pentru mai multe livrări deodată. Din perspectivă de business, automatizarea crește productivitatea departamentului de expediere, permițând unui singur operator să proceseze un volum mare de comenzi în minute, nu în ore.

#### 2. Funcționalități Cheie

- **Onorare accelerată a comenzilor**: procesează mai multe expedieri deodată, reducând timpul petrecut pe generarea manuală de AWB-uri.
- **Scalabilitate operațională îmbunătățită**: gestionează vârfurile de volum prin acțiuni în lot asupra loturilor de ridicări (`stock.picking.batch`).
- **Acuratețe logistică sporită**: reduce erorile umane la crearea etichetelor de expediere prin date consistente pentru toate comenzile dintr-un lot.
- **Comunicare integrată cu curierii**: trimite expedierea către curier direct din Odoo, prin butoanele de pe formularul lotului: **Send to Shipper**, **Carrier Details**, **Print AWB** și **Cancel** (anulează și expedierea).
- **Distribuție eficientă din punct de vedere al costurilor**: maximizează eficiența personalului și reduce timpul până la livrare prin fluxuri de lucru în lot.
- Trimiterea se face o singură dată pe lot, prin prima livrare din lot; numărul de urmărire și curierul rezultate se copiază apoi pe toate livrările lotului. La anularea lotului, expedierea se anulează întâi (doar dacă există număr de urmărire), apoi livrările se detașează din lot.

#### 3. Dependențe

- [deltatech_delivery](../deltatech_delivery/index.md)
- `stock_picking_batch`

#### 4. Componente Cheie

**Modele**

- `stock.picking.batch` (extins): câmpurile calculate `carrier_ready` și `carrier_tracking_ref` (agregate din livrările lotului) și metodele `send_to_shipper()`, `carrier_details()`, `carrier_print_label()` (apelează `carrier_generate_label` pe prima livrare), `cancel_shipment()` și `action_cancel()` (anulează expedierea înainte ca `super()` să detașeze livrările din lot).

**Vizualizări**

- `stock_picking_batch_form`: extinde formularul lotului de ridicări cu butoanele **Send to Shipper**, **Carrier Details**, **Print AWB** și **Cancel**.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): modulul de bază oferă cadrul de curieri (`send_to_shipper`, `cancel_shipment`, `carrier_details`, `carrier_generate_label`) pe care acest modul îl extinde la nivel de lot de ridicări (`stock.picking.batch`).
- `stock_picking_batch`: modul standard Odoo care oferă modelul de lot de ridicări extins de acest modul.
