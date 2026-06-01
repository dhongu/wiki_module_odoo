# Invoice Pickings (localizat la `deltatech_invoice_picking/index.md`)

- **Nume Tehnic:** `deltatech_invoice_picking`
- **Versiune:** `19.0.1.0.9`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_invoice_picking
- **Cale Locală:** `odoo-addons/deltatech/deltatech_invoice_picking`
- **Ultima Ingestie:** `2026-06-01`

#### 1. Sumar

Acest modul permite generarea facturilor direct din livrări (pickings), oferind o alternativă la facturarea pornind de la comanda de vânzare sau de achiziție. Pe factură sunt preluate doar produsele din livrare împreună cu cantitățile efectiv realizate (done), ceea ce asigură o corelare exactă între ce s-a livrat și ce se facturează. Modulul aduce valoare în special în fluxurile unde cantitatea livrată poate diferi de cea comandată, simplificând munca echipelor de logistică și facturare.

#### 2. Funcționalități Cheie

- O factură poate fi creată dintr-una sau mai multe livrări.
- O factură poate fi creată dintr-un lot de livrări (batch).
- Pe factură sunt adăugate doar produsele din livrare, cu cantitățile lor realizate (done).
- Pot fi facturate doar livrările care provin dintr-o comandă de vânzare sau de achiziție.
- O livrare trebuie să fie în starea „done" pentru a putea fi facturată.
- Pe livrări este adăugat un câmp „to invoice", util pentru filtrare: este setat pe True la crearea unei livrări de vânzare, devine False la crearea facturii și revine la True dacă factura este anulată sau ștearsă.
- Pe livrări este adăugat un câmp cu legătură către factură, calculat pentru a indica factura generată din livrarea respectivă.
- **Dacă se fac modificări asupra facturii (linii șterse, cantități modificate), câmpurile facturii din livrările asociate nu vor fi actualizate.**

#### 3. Dependențe

- `account`
- `sale_management`
- `stock`
- `sale_stock`
- `stock_picking_batch`
- `purchase`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunea „Componente Cheie" este omisă deoarece există un fișier `readme/DESCRIPTION.md` care acoperă Sumarul și Funcționalitățile Cheie, fără a solicita explicit detalierea componentelor tehnice.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale către alte module cu pagină wiki existentă. Toate dependențele sunt module core Odoo (`account`, `sale_management`, `stock`, `sale_stock`, `stock_picking_batch`, `purchase`).
