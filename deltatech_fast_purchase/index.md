# Fast Purchase (localizat la `deltatech_fast_purchase/index.md`)

- **Nume Tehnic:** `deltatech_fast_purchase`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_fast_purchase
- **Cale Locală:** `odoo-addons/deltatech/deltatech_fast_purchase`
- **Ultima Ingestie:** `2026-11-12`

#### 1. Sumar

Modulul „Fast Purchase” accelerează procesul de achiziție din Odoo pentru comenzile primite integral și facturate imediat: confirmarea, recepția și facturarea se parcurg dintr-un singur clic, prin butoane dedicate pe comanda de achiziție, fără navigare manuală între documente. Operatorii din departamentul de aprovizionare economisesc astfel timp la generarea recepțiilor de marfă și la introducerea facturilor.

#### 2. Funcționalități Cheie

- **Flux dintr-un clic:** după o confirmare prealabilă, butonul *Confirm, Receipt and Bill* pe o comandă în ciornă (sau *Receipt and Bill* pe una confirmată) confirmă comanda dacă e nevoie, o recepționează și creează și deschide factura de furnizor.
- **Recepție automată:** fiecare recepție pregătită este validată cu cantitățile comandate și cu data comenzii ca dată de perioadă; documentul sursă devine referința furnizorului din comandă (sau numele comenzii), iar marcajul de aviz este șters. O recepție în așteptare este rezervată mai întâi; dacă rezervarea eșuează, acțiunea se oprește cu mesajul *The stock transfer cannot be validated!*.
- **Aviz de recepție:** butonul *Receipt Notice* pe o comandă confirmată setează marcajul de aviz pe recepțiile pregătite și deschide recepțiile comenzii, fără a valida nimic; marcajul este doar stocat și transmis mai departe.
- **Factură din recepție:** o recepție finalizată a unei comenzi de achiziție afișează butonul *Invoice*, care deschide facturile de furnizor ale comenzii și transmite marcajul de aviz.
- Butoanele de pe comandă sunt destinate utilizatorilor interni; *Confirm, Receipt and Bill* apare și pe o ofertă trimisă, pe care însă nu o confirmă și nu o recepționează.

#### 3. Dependențe

- `base`
- `purchase_stock`
- `stock`

#### 4. Componente Cheie

Conform fluxului de ingestie, întrucât există fișierul `readme/DESCRIPTION.md`, analiza detaliată a codului pentru această secțiune este omisă; mai jos sunt doar reperele confirmate în cod.

**Modele**

- `purchase.order` (extins): metodele `receipt_to_stock` (validează recepțiile), `action_button_confirm_to_invoice` (confirmare + recepție + factură) și `action_button_confirm_notice` (marcajul de aviz).
- `stock.picking` (extins): câmpul boolean `notice` (marcaj de aviz) și `action_view_invoice`, care deschide facturile comenzii de achiziție.
- `account.move` (extins): clasă fără logică activă (cod comentat).

**Vizualizări**

- `views/purchase_view.xml`: butoanele *Confirm, Receipt and Bill*, *Receipt and Bill* și *Receipt Notice* pe comanda de achiziție.
- `views/stock_view.xml`: butonul *Invoice* pe recepție.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni `ir.actions.server`.

#### 5. Conexiuni

- [deltatech_fast_sale](../deltatech_fast_sale/index.md): modul analog pentru zona de vânzări, care aplică același principiu de parcurgere rapidă a pașilor (confirmare, livrare, facturare) pe comanda de vânzare.
