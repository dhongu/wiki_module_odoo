# IAP Server - Odoo Online Couriers (localizat la `terrabit_iap_server_online_delivery/index.md`)

- **Nume Tehnic:** `terrabit_iap_server_online_delivery`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_iap_server_online_delivery
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_server_online_delivery`
- **Ultima Ingestie:** `2026-11-20`

#### 1. Sumar

Baza de curierat a serverului IAP Terrabit pentru Odoo Online. Execută operațiunile de expediere ale modulului fără cod `deltatech_delivery_online` (AWB, etichetă, anulare, urmărire), la fel pentru orice curier. Fiecare curier adaugă un modul mic cu adaptorul său (primul: FAN Courier, `terrabit_iap_server_online_fc`). Modulul este în stadiul Alpha.

#### 2. Funcționalități Cheie

- **Contul de curier ținut pe server:** administratorul bazei clientului trimite o singură dată credențialele curierului. Ele sunt verificate la curier, păstrate pe server (vizibile doar administratorilor serverului), nu sunt trimise înapoi și sunt scoase din cerere. Tokenul curierului este reutilizat între apeluri.
- **Un singur AWB per livrare:** o livrare retrimisă (fără răspuns la client, dublu clic) primește același AWB, fără taxare repetată. Doar AWB-urile create aici pot fi tipărite, anulate sau urmărite.
- **AWB-ul nu se pierde:** este salvat înainte de cererea de etichetă, iar o etichetă eșuată poate fi cerută din nou.
- **Răspunsurile incerte nu se reîncearcă:** un timeout sau o eroare de server a curierului la o modificare este raportată ca incertă, netaxată, pentru verificare în aplicația curierului.
- **Taxare doar pentru AWB nou:** creditele se aplică per răspuns al serviciului (1 credit = 1 EUR); contul, eticheta, anularea și urmărirea sunt gratuite.
- **Fără date personale păstrate:** cererile se șterg după 30 de zile (`terrabit_iap_server_online`); un AWB păstrează doar referința livrării și numărul său.

#### 3. Dependențe

- [terrabit_iap_server_online](../terrabit_iap_server_online/index.md)

#### 4. Componente Cheie

**Modele**

- `iap.online.delivery.account`: contul de curier al unei baze client, ținut pe server.
- `iap.online.delivery.awb`: AWB-ul creat, cu referința livrării și numărul.
- `iap.server.service` (extins): configurare specifică curieratului pe serviciul IAP.
- `iap.online.request` (extins): adaptat pentru operațiunile de curierat.

**Vizualizări**

- `view_iap_server_service_form`: formularul serviciului IAP, extins.
- `view_iap_online_delivery_account_list` / `_form`: conturile de curier (meniu `menu_iap_online_delivery_account`).
- `view_iap_online_delivery_awb_list` / `_search`: AWB-urile create (meniu `menu_iap_online_delivery_awb`).

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește acțiuni automate sau server.

#### 5. Conexiuni

- [deltatech_delivery_online](../deltatech_delivery_online/index.md): modulul fără cod din baza Odoo Online, ale cărui operațiuni de expediere sunt executate aici.
- `terrabit_iap_server_online_fc`: adaptorul FAN Courier, menționat în descriere (fără pagină wiki).
