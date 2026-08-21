# Deltatech Drop Shipping (localizat la `deltatech_dropshipping/index.md`)

- **Nume Tehnic:** `deltatech_dropshipping`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_dropshipping
- **Cale Locală:** `odoo-addons/deltatech/deltatech_dropshipping`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul îmbunătățește fluxul de drop shipping oferind vizibilitate mai bună și control asupra prețurilor. Afișează adresa de livrare direct în documentul de transfer (picking), astfel încât cei care gestionează expedițiile văd rapid unde trebuie livrată marfa fără a deschide alte documente. În plus, atrage atenția pe comanda de achiziție atunci când prețul de achiziție depășește prețul de vânzare al liniei corespunzătoare din comanda de vânzare, calculând și comparând automat valorile fără TVA pentru ambele documente, pentru a preveni pierderile pe fluxurile de drop shipping.

#### 2. Funcționalități Cheie

- Afișarea adresei de livrare în documentul de transfer (picking).
- Avertisment pe comanda de achiziție dacă prețul de achiziție este mai mare decât prețul de vânzare al liniei corespunzătoare din comanda de vânzare, în fluxurile de drop shipping.
- Calcul și comparare automată a prețurilor fără TVA pentru comanda de achiziție și cea de vânzare, pentru acuratețea avertismentului.

#### 3. Dependențe

- `stock_dropshipping`
- `sale_purchase`

#### 4. Componente Cheie

Conform fișierului `readme/DESCRIPTION.md`, funcționalitatea modulului constă în afișarea adresei de livrare în picking și avertizarea de preț pe comanda de achiziție; nu sunt detaliate componente tehnice suplimentare în Readme. Din structura modulului, extinderile ating documentul de transfer (`views/stock_picking_view.xml`) și comanda de achiziție (`views/purchase_order_view.xml`).

#### 5. Conexiuni

- `stock_dropshipping`: modulul core de drop shipping din Odoo, pe care acest modul îl extinde pentru a evidenția adresa de livrare în transferuri.
- `sale_purchase`: puntea standard Odoo dintre vânzări și achiziții, folosită pentru a lega linia comenzii de achiziție de linia comenzii de vânzare corespunzătoare, necesară pentru compararea prețurilor.
