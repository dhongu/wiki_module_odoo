# Deltatech Delivery Status (localizat la `deltatech_delivery_status/index.md`)

- **Nume Tehnic:** `deltatech_delivery_status`
- **Versiune:** `19.0.2.3.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_delivery_status
- **Cale Locală:** `odoo-addons/deltatech/deltatech_delivery_status`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul extinde sistemul de livrare din Odoo pentru a oferi o urmărire detaliată și o gestionare avansată a stării expedierilor. El adaugă o stare de livrare granulară pe transferurile de stoc, integrează informațiile despre starea transmise de curier cu comenzile de vânzare și permite controlul livrărilor în funcție de plată. Astfel, echipele de vânzări, depozit și clienții beneficiază de o vizibilitate clară și de informații precise privind parcursul fiecărui colet, de la pregătirea în depozit până la livrarea finală către client.

#### 2. Funcționalități Cheie

- Adaugă urmărirea detaliată a stării de livrare pe transferurile de stoc.
- Integrează informațiile de stare de la curier cu comenzile de vânzare.
- Permite gestionarea stării de livrare la nivelul echipelor de vânzări.
- Extinde furnizorii de plată cu informații privind starea de livrare.
- Suportă urmărirea coletelor prin intermediul curierilor.
- Permite monitorizarea stării de livrare pe tot parcursul procesului logistic.
- Îmbunătățește comunicarea între vânzări, depozit și clienți cu privire la starea expedierii.
- Centralizează informațiile de livrare pentru o vizibilitate mai bună în întreaga organizație.

**Blocarea livrărilor**

- **Blocare manuală a livrării:** utilizatorii pot amâna manual livrările marcând transferurile ca amânate.
- **Blocare în funcție de furnizorul de plată:** amânarea automată a livrărilor pe baza configurației furnizorului de plată. Fiecare furnizor poate fi configurat cu opțiunea „Livrare amânată"; când este activată, livrările sunt blocate până la confirmarea plății, iar la confirmare sistemul eliberează automat livrările blocate.
- **Configurare la nivel de echipă de vânzări:** echipele de vânzări pot fi configurate să amâne livrările pentru anumite metode de plată (tratament special pentru transferurile bancare, permițând verificarea plății înainte de expediere).
- **Gestionare la nivel de comandă:** funcții pentru amânarea sau eliberarea livrărilor la nivelul comenzii de vânzare.
- **Vizibilitatea stării:** afișează starea „amânat" pe comenzi și transferuri pentru o mai bună conștientizare operațională.

**Urmărirea stării de livrare (`delivery_state`)**

Câmp cuprinzător pe transferurile de stoc care urmărește parcursul coletului prin întregul proces logistic: Ciornă, Pregătit în depozit, Pre-aviz (AWB generat, neridicat încă), În tranzit, În depozitul curierului, În livrare și Livrat. Suplimentar, câmpul `available_state` indică vizual disponibilitatea produselor: Disponibil, Parțial disponibil sau Indisponibil.

#### 3. Dependențe

- `delivery`
- `stock`
- `sales_team`
- `stock_delivery`
- `payment`

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, modulul extinde modele standard Odoo: transferurile de stoc (`stock.picking` — câmpurile `delivery_state` și `available_state`), comenzile de vânzare (`sale.order`), echipele de vânzări (`crm.team`) și furnizorii de plată (`payment.provider` — opțiunea „Livrare amânată"). Pentru detaliile tehnice complete, consultați codul sursă al modulului.

#### 5. Conexiuni

- Niciun modul conex cu pagină wiki existentă nu a fost identificat.
