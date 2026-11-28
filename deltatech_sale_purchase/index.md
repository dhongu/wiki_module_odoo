# Sale-Purchase Sync (localizat la `deltatech_sale_purchase/index.md`)

- **Nume Tehnic:** `deltatech_sale_purchase`
- **Versiune:** `20.0.1.0.4`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_purchase`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_purchase`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Când o comandă de vânzare cu produse aprovizionate la comandă generează o cerere de ofertă (RFQ) prin regulile de aprovizionare, anularea comenzii în Odoo standard lasă liniile de achiziție pe loc, iar cumpărătorul fie le caută și le șterge manual, fie comandă marfa fără client. Modulul curăță automat aceste linii la anularea comenzii de vânzare, păstrând sincronizarea între echipa de vânzări și cea de achiziții.

#### 2. Funcționalități Cheie

- **Liniile de achiziție se elimină la anularea comenzii de vânzare:** la **Anulare**, liniile de achiziție create pentru mișcările de stoc ale comenzii sunt șterse, cât timp comanda de achiziție este încă RFQ (ciornă). O comandă de achiziție deja trimisă sau confirmată rămâne în grija cumpărătorului.
- **Liniile partajate se reduc, nu se șterg:** dacă furnizorul grupează RFQ-urile (**Group RFQ** pe *Daily*, *Weekly* sau *Always*, în fila **Sales & Purchase** a furnizorului), o linie poate acoperi mai multe comenzi de vânzare. Linia se păstrează, mișcările anulate se detașează de ea, iar cantitatea lor, convertită în unitatea de măsură de achiziție, se scade din linie.
- Nu există configurare: comportamentul este activ după instalare.
- **Limitări:** se tratează doar anularea întregii comenzi de vânzare (scăderea cantității pe o linie confirmată nu modifică linia de achiziție), iar comenzile de achiziție în starea *RFQ Sent* sau *Purchase Order* nu se modifică.
- Fluxul detaliat pentru consultant este în fișa consultantului.

#### 3. Dependențe

- `sale_purchase`
- `sale_stock`
- `purchase_stock`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): suprascrie `_action_cancel()` pentru a șterge sau a reduce liniile de achiziție generate (`order_line.move_ids.created_purchase_line_ids`) aflate în comenzi de achiziție ciornă, înainte de fluxul standard de anulare.

**Vizualizări**

- Modulul nu adaugă vizualizări proprii.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`; logica rulează sincron în `_action_cancel`.

#### 5. Conexiuni

- `sale_stock`: leagă liniile comenzii de vânzare de mișcările de stoc (`move_ids`) din care se determină liniile de achiziție generate.
- `purchase_stock`: populează `created_purchase_line_ids` pe mișcările de stoc când regulile de aprovizionare generează o comandă de achiziție.
