# Packeta Shipping (localizat la `deltatech_delivery_packeta/index.md`)

- **Nume Tehnic:** `deltatech_delivery_packeta`
- **Versiune:** `20.0.1.5.7`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_packeta`
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_packeta`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul **Packeta Shipping**, dezvoltat de Terrabit, oferă o integrare completă între sistemul de gestiune a livrărilor din Odoo și serviciile de curierat Packeta (cunoscut în Cehia și Slovacia sub numele de Zásilkovna). Soluția permite automatizarea fluxului de expediere, de la generarea etichetelor de transport (AWB) până la urmărirea coletelor în timp real, direct din interfața Odoo. Packeta este apreciat pentru rețeaua sa extinsă de puncte de ridicare (Pickup Points) și de lockere automate (Z-BOX), iar modulul facilitează utilizarea acestora pentru a oferi clienților maximum de flexibilitate la livrare.

#### 2. Funcționalități Cheie

- **Generare AWB în mai multe formate**:
  - Format PDF pentru imprimare standard.
  - Format ZPL pentru imprimante de etichete termice.
  - Format HTML pentru vizualizare rapidă în browser.
- **Gestiunea punctelor de ridicare și a lockerelor**:
  - Suport complet pentru Z-BOX și Pickup Points (PUDO), prin integrarea cu API-ul Packeta v5 pentru preluarea listei actualizate de puncte de livrare.
    - **PUDO**: puncte de ridicare partenere (magazine, puncte comerciale).
    - **Z-BOX**: lockerele automate proprii Packeta.
  - **Hartă interactivă în checkout**: clientul își poate selecta punctul de ridicare preferat (PUDO/Z-BOX) direct de pe hartă în timpul procesului de comandă.
  - **Import automat**: posibilitatea de a importa și sincroniza baza de date locală a punctelor PUDO Packeta.
  - **Filtrare avansată**: căutare după cod poștal, oraș sau zonă geografică pe hartă (Bounds).
- **Opțiuni de expediere**:
  - Suport pentru expedieri cu mai multe colete (multi-package).
  - **Expedieri pe baza dimensiunilor coletului**: dimensiunile (lungime, lățime, înălțime) se calculează automat pe baza celor definite în șablonul produsului (necesită modulul `deltatech_product_dimension`) sau pot fi introduse manual în asistentul de livrare.
  - Livrare asigurată (valoare declarată).
  - Gestionarea ramburs-ului (Cash on Delivery – COD).
  - Istoric complet al stărilor pentru fiecare expediere.
- **Integrare tehnică**:
  - Utilizarea API-ului modern Packeta JSON v5 (`pickup-point.api.packeta.com`).
  - Extinderea modelului standard de livrare din Odoo pentru a include funcționalități specifice Packeta.
  - Maparea automată a datelor de livrare către cerințele curierului.

*Limitări (versiunea curentă):* nu sunt incluse calculul automat al tarifelor (Get rates) și opțiunile de livrare sâmbăta sau deschiderea coletului la livrare.

*Detalii operaționale (fluxul pas-cu-pas e în fișa consultantului):*

- Pe metoda de livrare, fila **Packeta**: cheie API, parolă API, e-shop, serviciu și **Fix Price** (Packeta nu returnează tarif prin acest modul, deci costul pe comandă e prețul fix al metodei).
- **Initialization** importă curierii parteneri ca servicii (*Inventar > Configurare > Livrare > Carrier Services*); serviciul se alege pentru livrare la domiciliu și se lasă gol pentru puncte de ridicare.
- Cu **Use Locker** bifat, **Get Lockers** importă punctele și Z-BOX-urile în *Delivery Lockers*; un al doilea import le actualizează, fără dubluri.
- Rambursul se calculează din ultima plată a comenzii; se poate corecta cu **Manual Value to Collect**.
- Anularea (**Cancel AWB**) șterge referința de urmărire și eticheta; dacă Packeta raportează un răspuns pierdut, nu se reîncearcă, ci se verifică mai întâi coletul la Packeta.
- Fila **History** arată evenimentele Packeta și ale curierului partener, citite la **Refresh** sau printr-o acțiune programată.

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)

*Dependență externă Python:* `zeep`.

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunea „Sumar" și „Funcționalități Cheie" provin din `readme/DESCRIPTION.md` (cu detalii din `USAGE.md`), prin urmare analiza detaliată a codului (Modele, Vizualizări, Acțiuni Automate) a fost omisă. Singura informație structurală derivată din manifest este fișierul de date `views/delivery_view.xml`, care extinde vizualizarea de configurare a metodei de livrare (`delivery.carrier`) cu o pagină dedicată „Packeta" (chei API, plătitor transport, serviciu, e-shop, formate/tip etichetă, folosirea locațiilor PUDO/Z-BOX etc.), vizibilă doar când `delivery_type = 'packeta'`.

#### 5. Conexiuni

- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): necesar pentru selectarea punctelor de ridicare (PUDO/Z-BOX) direct pe hartă în checkout; oferă interfața unificată și integrarea hărții pentru mai mulți furnizori de livrare.
- [deltatech_product_dimension](../deltatech_product_dimension/index.md): oferă dimensiunile produsului (lungime/lățime/înălțime) folosite la calculul automat al dimensiunilor coletului.
