# Fast Sale (localizat la `deltatech_fast_sale/index.md`)

- **Nume Tehnic:** `deltatech_fast_sale`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_fast_sale
- **Cale Locală:** `odoo-addons/deltatech/deltatech_fast_sale`
- **Ultima Ingestie:** `2026-06-01`

#### 1. Sumar

Fast Sale (Vânzare rapidă) accelerează procesul de vânzare din Odoo, comprimând pașii de confirmare a comenzii, livrare și facturare într-o singură acțiune. Modulul adaugă butoane dedicate în comanda de vânzare, astfel încât un operator poate confirma comanda, valida automat livrarea cu cantitățile și prețurile din comandă și deschide direct fluxul de facturare, fără a parcurge manual fiecare etapă. Este util în special acolo unde livrarea coincide cu vânzarea (vânzare la tejghea, livrare imediată), reducând numărul de clicuri și timpul necesar pentru finalizarea unei tranzacții.

#### 2. Funcționalități Cheie

- Buton în comanda de vânzare care parcurge într-un singur pas confirmarea comenzii, livrarea și facturarea.
- Validare automată a livrării folosind cantitățile și prețurile din comanda de vânzare.
- Opțiune separată de livrare pe bază de aviz ("Deliver Notice"), care marchează transferurile ca aviz.

#### 3. Dependențe

- `base`
- `sale_management`
- `stock`
- `sale_stock`

#### 4. Componente Cheie

Conform fișierului `readme/DESCRIPTION.md`, modulul oferă în principal butoane în comanda de vânzare pentru parcurgerea pașilor de confirmare, livrare și facturare. Pentru context, componentele tehnice relevante sunt:

**Modele**

- `sale.order` (extins): adaugă acțiunile `action_button_confirm_to_invoice` (confirmă comanda, validează automat livrarea și deschide asistentul de facturare) și `action_button_confirm_notice` (livrare pe bază de aviz).

**Vizualizări**

- `view_order_form`: extinde formularul standard al comenzii de vânzare adăugând în antet butoanele "Confirm, Deliver and Invoice", "Deliver and Invoice" și "Deliver Notice", precum și câmpurile `client_order_ref` și `date_order`.

#### 5. Conexiuni

- `sale_stock`: integrează fluxul comandă de vânzare cu livrările din stoc, pe care modulul le validează automat.
- `account`: facturarea declanșată de butonul de vânzare rapidă se realizează prin documentele contabile standard.
