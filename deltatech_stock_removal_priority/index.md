# Stock Removal Location by Priority (localizat la `deltatech_stock_removal_priority/index.md`)

- **Nume Tehnic:** `deltatech_stock_removal_priority`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_stock_removal_priority
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_removal_priority`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul introduce o strategie de eliminare a stocului bazată pe prioritate pentru locațiile de depozitare din Odoo. Le oferă gestionarilor de inventar control granular asupra ordinii în care articolele sunt ridicate din diferite zone de stocare, asigurând fluxuri logistice optime și o utilizare mai bună a spațiului de depozitare. Modulul este gândit să funcționeze împreună cu `deltatech_putaway_strategy`: regulile de depozitare (putaway) direcționează produsele către sub-locații specifice la recepție, iar acest modul folosește aceleași reguli pentru a stabili ordinea de eliminare la ridicare (picking).

#### 2. Funcționalități Cheie

- Adaugă o strategie de eliminare dedicată, numită **Priority**, la configurarea locațiilor de stoc.
- Asigură că Odoo selectează automat stocul din locațiile cu prioritatea cea mai mare, în timpul procesului de picking.
- Prioritatea de eliminare pentru fiecare quant de stoc este derivată automat din regulile de putaway existente, potrivite mai întâi după produs, apoi după categoria de produs.
- Poate fi configurată o prioritate implicită prin parametrii de sistem (implicit: 999).
- Când o regulă de putaway este creată, modificată sau ștearsă, prioritatea de eliminare a tuturor quanturilor afectate este recalculată automat, fără intervenție manuală.
- Suportă excluderea unor locații specifice din colectarea stocului în timpul operațiunilor de picking.
- Optimizat pentru depozite mari, cu zone de picking preferate sau niveluri multiple de stocare, reducând timpul de deplasare al operatorilor prin extragerea stocului din locațiile cele mai accesibile.
- Flux de utilizare: Inventar > Configurare > Locații, se configurează Regulile de Putaway cu valori de secvență corespunzătoare (secvență mai mică = prioritate mai mare); Inventar > Configurare > Categorii de Produs, se setează Strategia de Eliminare pe **Priority** pentru categoriile dorite; la crearea unei mișcări de stoc pentru un produs din acea categorie, sistemul sugerează automat ridicarea din locațiile cu prioritatea cea mai mare.
- Configurare: cheia de parametru de sistem `stock.removal_priority.default` (Setări > Tehnic > Parametri de Sistem) permite stabilirea unei priorități implicite personalizate (implicit: 999).

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile pentru Componente Cheie au fost acoperite de fișierul `readme/DESCRIPTION.md`, care descrie funcționalitatea principală a modulului (strategia de eliminare „Priority”, derivarea automată a priorității din regulile de putaway și parametrul de sistem `stock.removal_priority.default`). Analiza suplimentară a codului a fost omisă în conformitate cu regula de prioritizare a Readme-ului.

#### 5. Conexiuni

- [deltatech_putaway_strategy](../deltatech_putaway_strategy/index.md): modul complementar explicit menționat în descriere — regulile de putaway definite acolo determină, prin sub-locațiile de destinație și secvența lor, prioritatea de eliminare calculată automat de acest modul.
