# Posta Romana Shipping (localizat la `deltatech_delivery_pr/index.md`)

- **Nume Tehnic:** `deltatech_delivery_pr`
- **Versiune:** `20.0.1.2.6`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_pr
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_pr`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul integrează serviciul de curierat al Poștei Române în Odoo, permițând expedierea coletelor direct din platformă. Pe baza livrărilor din Odoo se generează AWB-uri prin API-ul Poștei Române, fără introducerea manuală a datelor pe portalul curierului. Aduce valoare prin reducerea muncii repetitive la expediere și prin gestionarea coletelor cu valoare declarată sau ramburs.

#### 2. Funcționalități Cheie

- Generarea AWB-ului în format PDF și tipărirea lui cu **Print AWB**.
- Anularea unui AWB (**Cancel AWB**) direct din livrare.
- Expediere cu mai multe colete, cu valoare declarată (asigurare) și cu ramburs.
- Configurare: **Inventory > Configuration > Delivery > Shipping Methods**, cu **Provider** = *Posta Romana*, produs de tip serviciu, **Username** și **Password** în fila de configurare Poșta Română și **Fix Price** (modulul nu cere tarife de la Poșta Română).
- Opțional, un **Service** al cărui cod se trimite ca tip de trimitere (`codTrimitere`; implicit `3,1,10`); se aleg și metodele de plată tratate ca ramburs.
- Pe livrare, în **Carrier Details** se verifică greutatea, valoarea coletului și suma de încasat; la validare AWB-ul se rezervă, referința de urmărire se scrie pe livrare, iar eticheta PDF se atașează. AWB-ul apare în **Inventory > Operations > Delivery AWB** după **Get AWB history**.
- Fluxul pas cu pas este în [fișa consultantului](FISA_CONSULTANT.md).
- Neacoperit: tarife, AWB în ZPL/HTML, liste de orașe/județe/lockere/puncte de ridicare, istoric de status, expediere cu dimensiuni, livrare sâmbăta, deschiderea coletului, nota de restituire, trimiterea id-ului de locker în AWB.

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, deoarece există `readme/DESCRIPTION.md`, analiza codului pentru această secțiune este omisă. Pentru orientare, modulul extinde `delivery.carrier` și `delivery.carrier.service` și conține vizualizarea `views/delivery_view.xml`.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): modul de bază pentru integrările de curierat, de care depinde direct.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): urmărirea statusului expedierilor în ecosistemul de livrare.
- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): livrări către lockere, din aceeași suită de curierat.
