# Fast Sale (localizat la `deltatech_fast_sale/index.md`)

- **Nume Tehnic:** `deltatech_fast_sale`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_fast_sale
- **Cale Locală:** `odoo-addons/deltatech/deltatech_fast_sale`
- **Ultima Ingestie:** `2026-10-28`

#### 1. Sumar

Fast Sale (Vânzare rapidă) accelerează procesul de vânzare din Odoo, comprimând confirmarea comenzii, livrarea și facturarea într-un singur click direct pe comanda de vânzare. Operatorul nu mai validează separat transferul și nu mai parcurge manual pașii asistentului de facturare. Modulul este util acolo unde livrarea coincide cu vânzarea (vânzare la tejghea, livrare imediată), reducând numărul de clicuri și timpul necesar finalizării unei tranzacții.

#### 2. Funcționalități Cheie

- **Confirm, Deliver and Invoice:** buton pe comenzile în stare *Draft* sau *Sent* (meniul **Sales > Orders > Orders**), care confirmă comanda, validează livrarea cu cantitățile comandate și deschide asistentul standard de creare a facturii.
- **Deliver and Invoice:** același flux, disponibil pe comenzile deja confirmate (stare *Sale Order*).
- **Livrări în mai mulți pași:** pentru rute de tip pick + ship sau pick + pack + ship, fiecare etapă este validată în ordine, astfel încât marfa ajunge la client și cantitățile livrate sunt setate.
- **Deliver Notice:** pe comenzile confirmate, marchează transferurile pregătite ca aviz (`notice = True`), fără a crea factură, și deschide transferul rezultat pentru verificare sau tipărire; dacă există mai multe transferuri, se deschide lista lor.
- **Buton Invoice pe transfer:** în formularul transferului (**Inventory > Operations > Transfers**), pentru livrări în stare *Done* legate de o comandă de vânzare, deschide asistentul de facturare al comenzii.
- **Verificarea stocului:** dacă vreun produs nu este disponibil integral, acțiunea este blocată cu mesajul „Not all products are available.”
- Data facturii este setată automat la data de azi.
- Pe formularul comenzii apar și câmpurile `client_order_ref` și `date_order`, după termenul de plată.

#### 3. Dependențe

- `base`
- `sale_management`
- `stock`
- `sale_stock`

#### 4. Componente Cheie

DESCRIPTION.md acoperă funcționalitățile; componentele tehnice relevante din cod sunt:

**Modele**

- `sale.order` (extins): `action_button_confirm_to_invoice` (confirmă, validează pe rând transferurile deschise și întoarce asistentul de facturare), `action_button_confirm_notice` (marchează transferurile pregătite ca aviz) și `_prepare_invoice` (data facturii = azi).
- `stock.picking` (extins): câmpul boolean `notice` și metoda `action_view_sale_invoice`, care deschide asistentul de facturare pentru comanda asociată.
- `account.move` (extins): clasă goală, fără logică.

**Vizualizări**

- `view_order_form` (`sale.order`): adaugă în antet butoanele „Confirm, Deliver and Invoice”, „Deliver and Invoice” și „Deliver Notice” (grup `base.group_user`, cu confirmare pentru primele două) și câmpurile `client_order_ref` și `date_order`.
- `view_picking_form` (`stock.picking`): adaugă butonul „Invoice”, vizibil doar pentru transferuri *Done* legate de o comandă de vânzare.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- `sale_stock`: integrează comanda de vânzare cu livrările din stoc, pe care modulul le validează automat.
- `account`: facturarea declanșată de butoane trece prin documentele contabile standard.
