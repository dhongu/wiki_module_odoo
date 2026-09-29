# Cargus Shipping (localizat la `deltatech_delivery_uc/index.md`)

- **Nume Tehnic:** `deltatech_delivery_uc`
- **Versiune:** `19.0.1.0.1`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_uc`
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_uc`
- **Ultima Ingestie:** `2026-09-29`

#### 1. Sumar

Modulul integrează în Odoo serviciul de curierat Urgent Cargus (UC), permițând expedierea coletelor și urmărirea lor online direct din platformă. Pentru fiecare livrare poate genera AWB-ul (scrisoarea de transport) în format PDF, ZPL sau HTML, poate solicita tarife de transport și poate sincroniza istoricul de stare al expedierii. Modulul aduce valoare prin automatizarea completă a relației cu Urgent Cargus pentru companiile românești, inclusiv expedierea către lockere și puncte de ridicare Cargus.

#### 2. Funcționalități Cheie

- Generare AWB în format PDF, ZPL și HTML.
- Ștergere AWB.
- Calcul tarife pentru o expediere.
- Obținere liste de localități, județe, lockere și puncte de ridicare.
- Obținere istoric de stare pentru o expediere și listă de AWB-uri.
- Import și gestiune lockere Cargus (puncte de ridicare).
- Hartă interactivă pentru selecția lockerului în checkout.
- Curățare automată a lockerelor cu coordonate invalide.
- Expediere cu colete multiple și cu dimensiuni.
- Expediere cu valoare declarată (asigurare) și cu ramburs (cash on delivery).
- Expediere cu id localitate și id județ.
- Opțiune de livrare sâmbăta și opțiune de colet deschis.
- Ridicare doar din punctul de ridicare indicat și posibilitatea trimiterii id-ului de locker în AWB.
- Expediere către alte țări deservite de Cargus pe același API, între care Polonia: țările al căror catalog se importă se configurează pe transportator (`uc_country_ids`; gol înseamnă doar România, deci configurațiile existente rămân neschimbate), iar AWB-ul transmite țara destinatarului (`CountryId`, luat din țara localității). Scurtătura sectoarelor Bucureștiului se aplică doar adreselor din România.
- Reobținerea etichetei unui AWB existent direct de la Cargus (`uc_get_label`), utilă când eticheta livrării a fost ștearsă.
- Lockerele care nu mai apar în lista Cargus (`PudoPoints`) sunt arhivate automat la import, iar importul se face în lot.
- Localitățile raportate de Cargus se înregistrează în catalogul de mapări al transportatorului; cele ambigue sau necunoscute apar ca „de mapat”, fără a crea localități duplicate în nomenclator.
- Interogarea stărilor este protejată: un AWB problematic nu mai oprește interogarea livrărilor următoare, iar istoricul se rescrie doar când starea sau istoricul s-au schimbat.

> Notă: Pentru funcționalitatea de selecție a lockerului pe hartă este necesară și instalarea modulului `deltatech_delivery_locker`. De asemenea, extensia `unaccent` trebuie instalată în baza de date (`CREATE EXTENSION IF NOT EXISTS unaccent`), deoarece unele localități din România au denumiri diferite față de baza SIRUTA (ex: Popești-Leordeni).
>
> Limitări cunoscute: expedierea cu nume de localitate fără id de localitate și nota de retur (restitution note) în AWB nu sunt suportate.

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

Documentația pentru Sumar și Funcționalități Cheie a fost preluată din `readme/DESCRIPTION.md`. Conform fluxului de ingestie, analiza detaliată a codului pentru această secțiune a fost omisă, întrucât Readme-ul nu o acoperă explicit.

#### 5. Conexiuni

- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): necesar pentru selecția lockerului Cargus pe hartă în checkout.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): gestionarea și urmărirea stărilor de expediere/AWB.
