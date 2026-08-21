# GLS Shipping (localizat la `deltatech_delivery_gls/index.md`)

- **Nume Tehnic:** `deltatech_delivery_gls`
- **Versiune:** `19.0.2.0.12`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_gls
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_gls`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul GLS Shipping integrează direct în Odoo serviciile de curierat GLS (General Logistics Systems), unul dintre marii furnizori europeni de livrare colete. Permite companiilor să își automatizeze operațiunile de expediere cu GLS fără a părăsi mediul Odoo, acoperind întregul flux de livrare: de la generarea AWB-urilor și a etichetelor de transport, la urmărirea statusului coletelor și reconcilierea plăților ramburs (COD). Beneficiile principale sunt economisirea timpului (elimină crearea manuală a AWB-urilor), reducerea erorilor de transcriere, transparența costurilor de transport și o experiență mai bună pentru client prin informații de urmărire exacte.

#### 2. Funcționalități Cheie

- **Integrare cu serviciile GLS:** suport pentru ambele versiuni de API (GLS Online și MyGLS), autentificare securizată cu serviciile web GLS, suport multi-țară (România, Croația, Cehia, Ungaria, Slovenia, Slovacia), configurare ID expeditor și suport PSD (Parcel Shop Delivery).
- **Generare și gestionare etichete:** generarea etichetelor de transport în mai multe formate (PDF, ZPL), suport pentru dimensiuni variate (A4, A6, termic) și machete multiple (A4_2x2, A4_4x1, Thermo etc.), cu atașare automată a etichetei la livrare.
- **Management expedieri:** creare AWB direct din comenzi de vânzare sau din livrări, anulare AWB pentru comenzi respinse sau modificate, urmărire completă a statusului livrării.
- **Urmărire (tracking):** generare linkuri de urmărire, preluarea și afișarea istoricului de status al coletului, actualizarea statusului de livrare în Odoo pe baza statusului GLS.
- **Management tranzacții:** import tranzacții de plată din GLS, urmărirea plăților ramburs (cash-on-delivery), potrivirea tranzacțiilor GLS cu înregistrările Odoo și raportare istorică.
- **Gestionare listă AWB:** preluarea listei de AWB-uri din sistemul GLS, auto-crearea înregistrărilor AWB în Odoo, potrivirea informațiilor expeditor/destinatar și stocarea referințelor.
- **Opțiuni avansate de expediere:** ramburs (COD), valoare declarată (asigurare), colete multiple, instrucțiuni speciale de livrare, livrare sâmbăta, colet deschis la livrare.
- **Livrare la locker:** import automat al punctelor de livrare GLS (lockere) pentru România și Ungaria, selecție interactivă a locker-ului în checkout-ul Odoo și sugestii de locker pe bază de proximitate față de client; posibilitatea trimiterii ID-ului de locker în AWB.

Limitări cunoscute (nesuportate): calculul tarifelor pentru o expediere, listele de orașe/județe/puncte de pickup, generarea AWB în format HTML, expedierea cu ID oraș și ID județ, expedierea cu dimensiuni și nota de retur în AWB.

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)

Dependență externă Python: `zeep` (client SOAP pentru serviciile web GLS).

#### 4. Componente Cheie

> Conform README-ului (secțiunea „Technical Implementation”), modulul extinde modelul de transportator (delivery carrier) din Odoo cu funcționalitate specifică GLS. Componentele de mai jos sunt sintetizate din structura modulului.

**Modele**

- `delivery.carrier` (extins, `models/delivery_gls.py`): adaugă metoda de livrare GLS și logica de creare/anulare AWB, generare etichete și urmărire status.
- `gls.request` (`models/gls_request.py`): wrapper peste API-urile GLS Online și MyGLS (apeluri SOAP prin `zeep`), responsabil de generarea etichetelor, tracking, import tranzacții și sincronizare listă AWB.
- `res.config.settings` (extins, `models/res_config_settings.py`): expune setările de configurare GLS (credențiale, ID expeditor, opțiuni API).

**Vizualizări**

- `views/delivery_gls_view.xml`: vizualizările de configurare a metodei de livrare GLS și acțiunile aferente AWB/tracking.

**Date**

- `data/delivery_gls_data.xml`: înregistrările inițiale ale modulului (metoda de livrare GLS și date de configurare implicite).

**Hook-uri**

- `uninstall_hook`: rutină de curățare executată la dezinstalarea modulului.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): cadrul de bază pentru metodele de livrare Deltatech pe care acest modul îl extinde cu integrarea GLS (dependență directă).
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): valorifică statusurile de livrare actualizate de pe baza informațiilor de tracking GLS.
