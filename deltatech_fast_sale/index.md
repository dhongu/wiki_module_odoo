# Fast Sale (localizat la `deltatech_fast_sale/index.md`)

- **Nume Tehnic:** `deltatech_fast_sale`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_fast_sale
- **Cale Locală:** `odoo-addons/deltatech/deltatech_fast_sale`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Vânzarea rapidă comprimă confirmarea, livrarea și facturarea comenzii într-un singur clic, direct din comanda de vânzare. Este gândită pentru comenzi simple, cum este vânzarea la tejghea, unde nu e nevoie de validarea separată a livrării sau de parcurgerea manuală a asistentului de facturare.

#### 2. Funcționalități Cheie

- **Confirm, Deliver and Invoice**: buton pe comenzile în stare Ciornă sau Trimisă; confirmă comanda, validează livrarea cu cantitățile comandate și deschide asistentul de facturare (meniu: Vânzări > Comenzi > Comenzi).
- **Deliver and Invoice**: același flux pe o comandă deja confirmată.
- **Deliver Notice**: validează livrarea și o marchează ca aviz (`notice = True`), fără facturare imediată, apoi deschide transferul rezultat pentru verificare sau tipărire.
- **Buton de facturare pe livrare**: scurtătură către asistentul de facturare din formularul transferului, pentru personalul de depozit.
- **Verificarea stocului**: dacă un produs nu este disponibil integral, acțiunea este blocată cu un mesaj clar.
- **Data facturii**: se setează automat la data de azi.

#### 3. Dependențe

- `base`
- `sale_management`
- `stock`
- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): acțiunile `action_button_confirm_to_invoice` și `action_button_confirm_notice`.
- `stock.picking` (extins): acțiunea de facturare de pe livrare.
- `account.move` (extins).

**Vizualizări**

- `view_order_form`: butoanele „Confirm, Deliver and Invoice", „Deliver and Invoice" și „Deliver Notice" în antetul comenzii.
- `view_picking_form`: butonul de facturare pe transfer.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- [deltatech_fast_purchase](../deltatech_fast_purchase/index.md): modul analog pentru achiziții (confirmare, recepție, facturare într-un pas).
- `sale_stock`: livrările din stoc pe care modulul le validează automat.
