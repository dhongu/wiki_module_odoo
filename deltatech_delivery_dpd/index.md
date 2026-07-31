# DPD Romania Shipping (localizat la `deltatech_delivery_dpd/index.md`)

- **Nume Tehnic:** `deltatech_delivery_dpd`
- **Versiune:** `19.0.0.2.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_delivery_dpd
- **Cale Locală:** `odoo-addons/bitshop/deltatech_delivery_dpd`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul DPD Romania Shipping integrează Odoo cu serviciul de curierat DPD (Dynamic Parcel Distribution), automatizând operațiunile de livrare direct din ERP. Permite calcularea tarifelor de transport, generarea etichetelor de expediere (AWB), urmărirea coletelor și gestionarea livrărilor, eliminând introducerea manuală a datelor și reducând erorile. Modulul este deosebit de util pentru companiile din România și țările vecine care folosesc DPD și au nevoie de o legătură strânsă între Odoo și operațiunile de expediere. Se construiește peste funcționalitatea de bază oferită de modulul Deltatech Delivery.

#### 2. Funcționalități Cheie

- **Integrare cu serviciile DPD**: import automat al tipurilor de servicii DPD, suport pentru multiple servicii de expediere (DPD Standard, DPD International etc.), conectivitate cu API-urile DPD și autentificare securizată.
- **Generare și gestionare AWB**: generarea etichetelor de expediere în formate PDF și ZPL, suport pentru diverse dimensiuni de etichete (A4, A6, A4_4xA6), integrare directă în fluxul de livrare Odoo și funcție de anulare a expedierilor.
- **Calculul tarifelor**: calculul tarifelor de transport în timp real, estimarea automată a costurilor pe comenzile de vânzare și prețuri în funcție de greutate și dimensiuni.
- **Gestionarea localizărilor**: import automat al bazei de date de orașe DPD pentru România, maparea orașelor și județelor cu ID-urile de localizare DPD și validarea adreselor.
- **Funcții de urmărire**: generarea linkurilor de tracking, accesul la istoricul de stare al expedierii și actualizarea stării livrării în Odoo pe baza statusului DPD.
- **Opțiuni avansate de expediere**: ramburs (cash on delivery), valoare declarată (asigurare), instrucțiuni speciale de livrare și gestionarea coletelor multiple, opțiune de pachet deschis și livrare sâmbăta.
- **Gestionarea punctelor de ridicare (pickup)**: configurarea punctelor de ridicare DPD, asocierea cu adresele companiei și detectarea automată a client ID-ului.

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunea „Componente Cheie" este omisă deoarece fișierul `readme/DESCRIPTION.md` acoperă „Sumarul" și „Funcționalitățile Cheie", iar componentele tehnice nu sunt cerute explicit în Readme.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): modulul de bază pentru curierat peste care se construiește integrarea DPD; furnizează modelul și fluxul generic de livrare.
