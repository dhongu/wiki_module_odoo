# Deltatech Delivery Base (localizat la `deltatech_delivery/index.md`)

- **Nume Tehnic:** `deltatech_delivery`
- **Versiune:** `19.0.5.0.4`
- **Cale:** https://github.com/terrabit-ro/bitshop/tree/19.0/deltatech_delivery
- **Cale Locală:** `odoo-addons/bitshop/deltatech_delivery`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul „Deltatech Delivery Base” este o extensie cuprinzătoare pentru Odoo care îmbunătățește și optimizează capacitățile de gestionare a livrărilor din ecosistemul Odoo. Modulul servește drept fundație pentru diverse integrări specifice fiecărui curier și oferă un cadru robust pentru gestionarea expedierilor către mai mulți furnizori de servicii de livrare. Modulul de bază pune la dispoziție și un cadru partajat de opțiuni de livrare pentru serviciile legate de AWB: opțiuni standard precum livrarea sâmbăta, deschiderea coletului, returul coletului, livrarea personală și notificarea prin SMS sunt definite centralizat și pot fi expuse per curier, în funcție de capabilitățile conectorului. Operatorul selectează doar opțiunile permise de curierul ales, în timp ce structura existentă `shipment_info` rămâne neschimbată pentru compatibilitate retroactivă.

#### 2. Funcționalități Cheie

- **Gestionare îmbunătățită a livrărilor**:
  - Opțiuni îmbunătățite de configurare a curierului de livrare
  - Catalog partajat de opțiuni de livrare pentru serviciile AWB
  - Selectarea opțiunilor de livrare specifice curierului cu `many2many_tags`
  - Capabilități de curier calculate automat (doar citire) din `delivery_type`
  - Metode de expediere și tipuri de livrare extinse
  - Mecanisme flexibile de calcul al costului de livrare
  - Capabilități avansate de gestionare a coletelor

- **Suport pentru mai mulți curieri**:
  - Cadru de bază pentru integrarea mai multor curieri de expediere
  - Interfață unificată pentru gestionarea diferitelor servicii de curierat
  - API standardizat pentru extensiile specifice curierilor
  - Structuri de date comune pentru informațiile de expediere
  - Modulele de curier definesc opțiunile de livrare suportate pentru propriul conector

- **Procesarea expedierilor**:
  - Flux de lucru simplificat pentru crearea și procesarea expedierilor
  - Generarea automată a documentelor de expediere
  - Capabilități de procesare în lot pentru expedieri multiple
  - Urmărirea și sincronizarea stării livrării
  - Opțiunile de livrare sunt stocate compatibil în structura JSON existentă `shipment_info`

- **Gestionarea coletelor**:
  - Suport pentru mai multe colete într-o singură expediere
  - Gestionarea dimensiunilor și greutății coletelor
  - Configurarea și validarea tipurilor de ambalare
  - Gruparea și optimizarea coletelor

- **Gestionarea adreselor**:
  - Capabilități îmbunătățite de validare a adreselor
  - Suport pentru diferite formate de adrese în funcție de țară
  - Normalizarea adreselor pentru cerințele de expediere
  - Tratarea specială a locațiilor de livrare

- **Funcționalități de integrare**:
  - Integrare cu gestionarea stocurilor Odoo
  - Conexiune fără cusur cu procesarea comenzilor de vânzare
  - Crearea automată a livrărilor din vânzări sau transferuri
  - Sincronizare cu operațiunile de facturare

- **Experiența utilizatorului**:
  - Interfețe intuitive pentru operațiunile de expediere
  - Vizibilitate clară asupra informațiilor de expediere
  - Proces simplificat de selectare a curierului
  - Selectarea opțiunilor AWB pe bază de etichete (tags), în locul valorilor booleene fixe din wizard
  - Istoric și urmărire cuprinzătoare a expedierilor

Modulul reprezintă fundația pentru integrările specifice ale curierilor precum Fan Courier, TNT, DHL și alții, oferind un cadru consecvent pentru gestionarea livrărilor indiferent de curierul utilizat. Opțiunile de livrare sunt împărțite intenționat între modulul de bază și submodulele specifice fiecărui curier: modulul de bază definește înregistrările comune de opțiuni și interfața generică, fiecare modul `deltatech_delivery_*` definește ce opțiuni sunt suportate pentru propriul `delivery_type`, iar dacă un modul de curier nu definește un subset specific, toate opțiunile standard rămân disponibile.

Funcționalități care pot fi adăugate în submodule: generarea AWB în format PDF / HTML / ZPL, ștergerea AWB, obținerea tarifelor pentru o expediere, listele de orașe / județe / lockere / puncte de ridicare, istoricul de stare al unei expedieri, lista de AWB-uri, expediere cu mai multe colete, cu valoare declarată (asigurare), cu ramburs, cu id de oraș și județ, ridicare doar din punctul de ridicare indicat, trimiterea id-ului de locker în AWB, notă de restituire în AWB, expediere cu dimensiuni, precum și opțiunile de livrare sâmbăta, colet deschis, retur colet și livrare personală în lockere.

#### 3. Dependențe

- `delivery`
- `payment`
- `base_address_extended`
- [deltatech_delivery_status](../deltatech_delivery_status/index.md)
- `stock`
- `purchase`

#### 4. Componente Cheie

Conform fluxului de ingestie din schema wiki, secțiunea „Sumar” și „Funcționalități Cheie” provin din `readme/DESCRIPTION.md`, care nu solicită explicit analiza codului pentru componente. Prin urmare, această secțiune nu este detaliată din cod.

#### 5. Conexiuni

- [deltatech_delivery_status](../deltatech_delivery_status/index.md): furnizează stările de livrare folosite de cadrul de urmărire a expedierilor din acest modul.
- [deltatech_website_delivery_and_payment](../deltatech_website_delivery_and_payment/index.md): extinde fluxul de livrare și plată în site-ul web, valorificând cadrul de curieri din acest modul.
