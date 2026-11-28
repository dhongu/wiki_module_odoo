# Purchase Order Phases (localizat la `deltatech_purchase_phase/index.md`)

- **Nume Tehnic:** `deltatech_purchase_phase`
- **Versiune:** `20.0.1.2.8`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_purchase_phase`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_phase`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă pe comenzile de achiziție o urmărire simplă pe faze configurabile. Fiecare comandă are o fază curentă, care se poate schimba manual sau automat în funcție de starea documentului și de livrare, fără să modifice fluxul standard al comenzilor de achiziție.

#### 2. Funcționalități Cheie

- Câmpul `phase_id` pe comanda de achiziție, urmărit în chatter, afișat colorat cu widget-ul `many2one_badge`.
- Faze configurabile în *Purchase > Configuration > Purchase Order Phases*: cod unic (ex. `rfq`, `purchase_confirm`), nume, culoare, secvență și o acțiune server opțională. Sunt livrate fazele RFQ, Purchase Confirmed, Pre Advice, Shipped și Delivered.
- Treceri automate: la trimiterea cererii de ofertă (`sent`) faza devine `rfq`; la confirmarea comenzii (`purchase`) devine `purchase_confirm`; o fază al cărei cod lipsește este creată din mers.
- Treceri după starea livrării din transferul de stoc asociat: `pre_advice` → Pre Advice, `in_transit` / `in_warehouse` / `in_delivery` → Shipped, `delivered` → Delivered, `refused` → faza cu codul `refused`.
- Suprascriere manuală oricând; contextul `skip_phase_update=True` oprește actualizările automate la scrieri programatice. Metoda ajutătoare `set_phase(code)` setează faza după cod.
- Pentru extindere la alte stări (ex. `done`, `cancel`) se pot folosi acțiuni server sau mici suprascrieri Python.
- Fișa consultant: [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `purchase_stock`
- [deltatech_widget_many2one_badge](../deltatech_widget_many2one_badge/index.md)

#### 4. Componente Cheie

**Modele**

- `purchase.order.phase`: faza (nume tradus, cod, culoare, secvență, acțiune server opțională).
- `purchase.order` (extins): câmpul `phase_id`, metoda `set_phase` și `write` care actualizează faza la schimbarea stării.
- `stock.picking` (extins): la schimbarea câmpului `delivery_state` actualizează faza comenzii de achiziție asociate.

**Vizualizări**

- `view_purchase_order_phase_form` / `view_purchase_order_phase_tree`: configurarea fazelor.
- `purchase_order_form` / `purchase_order_view_tree`: faza pe formularul și lista comenzilor.

**Acțiuni Automate / Acțiuni Server**

- `action_purchase_order_phase`: acțiunea de fereastră pentru configurarea fazelor.
- Nu sunt definite sarcini `ir.cron`; tranzițiile rulează în `write()`.

#### 5. Conexiuni

- [deltatech_widget_many2one_badge](../deltatech_widget_many2one_badge/index.md): widget-ul `many2one_badge` pentru afișarea colorată a fazei.
- `purchase_stock`: integrare cu transferurile de stoc ale comenzii, fără a altera fluxul standard.
