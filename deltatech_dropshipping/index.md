# Drop Shipping Enhanced (localizat la `deltatech_dropshipping/index.md`)

- **Nume Tehnic:** `deltatech_dropshipping`
- **Versiune:** `20.0.1.1.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_dropshipping
- **Cale Locală:** `odoo-addons/deltatech/deltatech_dropshipping`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul îmbunătățește fluxul de livrare directă (drop shipping) prin vizibilitate mai bună și control al prețurilor. Afișează adresa de livrare în transfer, astfel încât cei care gestionează expedițiile văd rapid unde trebuie să ajungă marfa. În plus, avertizează pe comanda de achiziție când prețul de achiziție depășește prețul de vânzare al liniei corespunzătoare din comanda de vânzare, comparând automat valorile fără TVA, pentru a preveni vânzarea în pierdere.

#### 2. Funcționalități Cheie

- Câmpul **Livrare la** pe transfer (formular și coloană în lista de transferuri), lângă **Contact**: adresa de livrare a comenzii de vânzare pe transferurile de livrare directă și de recepție legate de o vânzare, contactul transferului pe livrări, adresa depozitului pe celelalte transferuri.
- Avertisment (chenar galben) pe comanda de achiziție dacă prețul de achiziție este mai mare decât prețul de vânzare al liniei corespunzătoare din comanda de vânzare; nu blochează confirmarea.
- Calcul și comparare automată a prețurilor fără TVA pentru ambele documente.
- Limitare cunoscută: comparația nu ține cont de unitatea de măsură, monedă și discount (vezi fișa consultant).

#### 3. Dependențe

- `stock_dropshipping`
- `sale_purchase`

#### 4. Componente Cheie

**Vizualizări**

- `view_picking_form` (`views/stock_picking_view.xml`): adaugă câmpul **Livrare la** pe formularul transferului.
- `vpicktree` (`views/stock_picking_view.xml`): adaugă coloana **Livrare la** în lista de transferuri.
- `purchase_order_form` (`views/purchase_order_view.xml`): afișează avertismentul de preț pe comanda de achiziție.

#### 5. Conexiuni

- `stock_dropshipping`: modulul standard de livrare directă, extins pentru a evidenția adresa de livrare în transferuri.
- `sale_purchase`: legătura standard dintre linia de achiziție și linia de vânzare, necesară pentru compararea prețurilor.
