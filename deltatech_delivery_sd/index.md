# Sameday Shipping (localizat la `deltatech_delivery_sd/index.md`)

- **Nume Tehnic:** `deltatech_delivery_sd`
- **Versiune:** `19.0.1.13.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_sd
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_sd`
- **Ultima Ingestie:** `2026-09-29`

#### 1. Sumar

Modulul Sameday Shipping este o extensie Odoo care oferă integrare completă cu Sameday Courier, unul dintre principalii curieri din România. Integrarea permite companiilor să automatizeze operațiunile de expediere prin Sameday direct din Odoo, simplificând întregul proces de la calculul tarifelor până la urmărirea coletelor și actualizarea stării livrării. Valoarea de afaceri constă în eliminarea introducerii manuale a datelor pentru generarea AWB-urilor, reducerea erorilor prin validarea automată a adreselor și oferirea de informații de urmărire precise către clienți.

#### 2. Funcționalități Cheie

- **Integrare servicii Sameday**: import automat al tipurilor de servicii Sameday, suport pentru servicii multiple de expediere, conectivitate cu API-urile Sameday și autentificare securizată cu serviciile web Sameday.
- **Generare și gestionare AWB**: generarea etichetelor de expediere în mai multe formate (PDF, HTML) și dimensiuni (A4, A6), integrare directă cu fluxul de livrare Odoo și anularea expedierilor pentru comenzi respinse sau modificate.
- **Calcul tarife**: estimarea în timp real a costurilor de expediere pentru comenzile de vânzare, integrată cu sistemul de prețuri de livrare Odoo și cu suport pentru diverse tipuri de colete (colet, colet mic, colet mare).
- **Gestionarea locațiilor**: import automat al bazei de orașe Sameday pentru România, maparea orașelor și județelor cu ID-urile de locație Sameday și validarea adreselor.
- **Gestionarea punctelor de ridicare (pickup)**: import automat al punctelor de ridicare Sameday, configurarea acestora și asocierea cu adresele companiei (suport pentru locații multiple).
- **Urmărire (tracking)**: generarea linkurilor de urmărire, accesarea istoricului de stare a expedierilor și actualizarea stării livrării în Odoo pe baza statusului Sameday.
- **Opțiuni avansate de expediere**: ramburs (cash on delivery), taxe de serviciu în funcție de tipul coletului, opțiune de deschidere colet la livrare, opțiune de retur colet și livrare personală.
- **Gestionarea contului de numerar**: regăsirea informațiilor de cont de numerar, urmărirea plăților prin ramburs și raportare pe perioade.
- **Livrare la puncte out-of-home (easybox și Sameday Point / PUDO)**: AWB-ul poartă locația în parametrul `oohLastMile` (același pentru ambele rețele; înlocuiește `lockerLastMile`, depreciat), la emitere și la estimarea prețului. Serviciile PUDO 57 și 58 sunt suportate, alături de cele de locker (15, 30); la **Inițializare** ambele tipuri sunt marcate ca servicii de locker (setare implicită la primul import, corecția manuală nu se suprascrie). Expedierea este refuzată înainte de a ajunge la Sameday dacă o locație e setată pe un serviciu care nu livrează out-of-home sau dacă un serviciu out-of-home nu are locație. Rețeaua locației nu se verifică față de serviciu, intenționat: Sameday acceptă un Sameday Point pe serviciu de locker.
- **Ramburs per locație**: rambursul către un punct out-of-home depinde de ce raportează Sameday pentru locația respectivă (**Payment at pickup**), nu de tipul locației; refuzul Sameday este reformulat într-un mesaj clar, cu numele locației și suma.
- **Catalog de locații**: citit din `client/ooh-locations` cu `listingType=1` (ambele rețele), în pagini de 500; necesită modulul `deltatech_delivery_locker` cu opțiunea **Use Locker** pe curier și butonul **Get Lockers**. Importul complet arhivează locațiile pe care Sameday nu le mai listează (doar când catalogul a fost adus integral), rulează pe coadă (`queue_job`, loturi de 500) când e instalat și sincron din acțiunea programată. Două curieri Sameday pe același cont și același server se arhivează reciproc corect.
- **Reobținerea etichetei**: eticheta unui AWB existent poate fi regăsită de la Sameday când atașamentul a fost șters, cu extensia corectă (PDF/ZPL).
- **Funcționalități suportate suplimentar**: expediere cu colete multiple, expediere cu valoare declarată (asigurare), expediere cu ramburs, trimiterea ID-ului de locker în AWB.

Configurare: curierul se definește la **Inventory > Configuration > Delivery > Shipping Methods**, cu **Provider** = *Sameday*, produs de tip serviciu și credențialele pe fila **Sameday Configuration**; butonul **Initialization** importă serviciile din contract, județele, orașele și punctele de ridicare. Pe livrare: **Carrier Details**, **Send to Shipper**, **Print AWB**, **Tracking**, **Cancel**.

Notă: pentru funcționalitatea de selectare a lockerului pe hartă este necesară și instalarea modulului [deltatech_delivery_locker](../deltatech_delivery_locker/index.md).

Limitări cunoscute (neacoperite): generare AWB în format ZPL, expediere fără ID de oraș, notă de restituire în AWB, expediere cu dimensiuni și opțiune de livrare sâmbăta.

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

*Conform fluxului de ingestie, secțiunea Componente Cheie este omisă deoarece există `readme/DESCRIPTION.md`, care a fost folosit pentru Sumar și Funcționalități Cheie. Analiza detaliată a codului (modele, vizualizări, acțiuni) nu este reluată aici, nefiind solicitată explicit în Readme.*

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): modulul de bază pentru gestionarea livrărilor și a curierilor, extins de acest modul Sameday.
- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): necesar pentru selectarea lockerelor Sameday pe hartă.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): gestionarea stărilor de livrare actualizate pe baza statusului Sameday.
- [deltatech_delivery_sd_easybox](../deltatech_delivery_sd_easybox/index.md): modul soră pentru lockerele Sameday (Easybox).
