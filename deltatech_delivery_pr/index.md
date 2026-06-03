# Poșta Română Shipping (localizat la `deltatech_delivery_pr/index.md`)

- **Nume Tehnic:** `deltatech_delivery_pr`
- **Versiune:** `19.0.1.0.2`
- **Cale:** `https://github.com/terrabit-ro/bitshop/tree/19.0/deltatech_delivery_pr`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_delivery_pr`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul integrează serviciul de curierat al Poștei Române în Odoo, permițând expedierea coletelor direct din platformă. Pe baza livrărilor din Odoo se generează automat scrisori de transport (AWB) prin API-ul Poștei Române, fără introducerea manuală a datelor pe portalul curierului. Modulul aduce valoare comercială prin reducerea muncii repetitive la expediere și prin gestionarea coletelor cu valoare declarată sau ramburs, scenarii frecvente în comerțul online.

#### 2. Funcționalități Cheie

- Generarea AWB-ului în format PDF.
- Ștergerea unui AWB generat anterior.
- Expediere cu mai multe colete (parcels) într-o singură comandă de transport.
- Expediere cu valoare declarată (asigurare).
- Expediere cu plată ramburs (cash on delivery).

Funcționalități neacoperite de modul (conform README): obținerea de tarife pentru o expediere, generarea AWB în format ZPL sau HTML, listele de orașe/județe/lockere/puncte de ridicare, istoricul de status al unei expedieri, expedierea după numele orașului fără id, expedierea cu id de oraș și județ, expedierea cu dimensiuni, livrare sâmbăta, deschiderea coletului, nota de restituire în AWB, ridicarea doar din punctul de ridicare indicat și trimiterea id-ului de locker în AWB.

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, deoarece există fișierul `readme/DESCRIPTION.md`, analiza detaliată a codului pentru această secțiune este omisă. Pentru orientare tehnică, modulul conține modelele din `models/delivery.py` și `models/pr_request.py` (clientul de API către Poșta Română) și vizualizarea `views/delivery_view.xml`.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): modul de bază pentru integrările de curierat, de care depinde direct acest modul.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): urmărirea statusului expedierilor în ecosistemul de livrare Deltatech.
- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): gestionarea livrărilor către lockere, parte din aceeași suită de curierat.
