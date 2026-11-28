# Delivery Batch AWB (localizat la `deltatech_delivery_batch/index.md`)

- **Nume Tehnic:** `deltatech_delivery_batch`
- **Versiune:** `20.0.1.0.9`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_batch
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_batch`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă acțiunile de curierat pe formularul **Batch Transfers** (Inventar), astfel încât un lot de livrări către același destinatar este trimis curierului o singură dată, cu un singur AWB comun tuturor livrărilor din lot. Depozitul nu mai rezervă aceeași expediere o dată pentru fiecare comandă de livrare, iar clientul și depozitul văd același AWB peste tot.

#### 2. Funcționalități Cheie

- **Un singur AWB pe lot**: operatorul aplică detaliile transportatorului pe livrările din lot, apasă **Send to Shipper** pe lot, iar AWB-ul este scris pe toate livrările lotului.
- **Urmărire consecventă**: fiecare livrare din lot are același transportator și aceeași referință de urmărire (tab-ul **Additional Info**), plus propriul buton **Print AWB**.
- **Totul pe lot**: **Carrier Details**, **Print AWB** și anularea expedierii sunt disponibile direct pe lot.
- **Anulare sigură**: link-ul **Cancel** de lângă referința de urmărire anulează expedierea la curier și șterge referința și transportatorul de pe toate livrările; **Cancel** din antet anulează lotul (întâi expedierea, apoi livrările ies din lot).
- **Sursa datelor expedierii**: adresa, coletele, greutatea și rambursul sunt cele ale primei livrări a lotului (în ordinea priorității și a datei programate din Odoo); detaliile trebuie aplicate pe **fiecare** livrare.
- **Limite**: un singur destinatar per lot (altfel apare eroarea „Cumulative deliveries can only be made for the same partner"); valoarea de încasat și greutatea sunt cele ale primei livrări, deci comenzile cu ramburs nu se grupează într-un lot.
- Meniu: *Inventory > Operations > Jobs > Batch Transfers*; necesită activarea opțiunii **Batch Transfers** în *Inventory > Configuration > Settings*. Fluxul pas cu pas este în fișa consultantului.

#### 3. Dependențe

- [deltatech_delivery](../deltatech_delivery/index.md)
- `stock`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunea „Componente Cheie" este omisă: `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie, iar componentele tehnice nu sunt cerute explicit în Readme.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): modulul de bază oferă cadrul de curieri (`send_to_shipper`, `cancel_shipment`, `carrier_details`, `carrier_generate_label`) pe care acest modul îl extinde la nivel de lot de ridicări (`stock.picking.batch`); conexiunea cu curierul vine din modulul de curier folosit împreună cu el.
