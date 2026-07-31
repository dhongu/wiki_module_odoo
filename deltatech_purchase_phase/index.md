# Deltatech Purchase Order Stage (localizat la `deltatech_purchase_phase/index.md`)

- **Nume Tehnic:** `deltatech_purchase_phase`
- **Versiune:** `19.0.1.2.6`
- **Cale:** [https://github.com/dhongu/deltatech/tree/19.0/deltatech_purchase_phase](https://github.com/dhongu/deltatech/tree/19.0/deltatech_purchase_phase)
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_phase`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul adaugă o urmărire ușoară a fazei (stadiului) pe comenzile de achiziție, complementară stării standard a documentului. Fiecare comandă de achiziție primește o fază curentă (ex: RFQ, Confirmat achiziție, Pre-aviz, Expediat, Livrat), actualizată automat pe măsură ce comanda avansează prin flux, dar și modificabilă manual. Astfel, echipa de achiziții și logistică poate vedea dintr-o privire, direct pe formularul comenzii, în ce etapă reală se află aprovizionarea — nu doar starea tehnică a documentului.

#### 2. Funcționalități Cheie

- Câmp nou `phase_id` pe `purchase.order`, afișat ca insignă colorată (`many2one_badge`) și urmărit în chatter (tracking).
- Tranziții automate de fază legate de starea comenzii: la trimiterea RFQ (`state = sent`) faza devine `rfq`; la confirmarea comenzii (`state = purchase`) faza devine `purchase_confirm`.
- Tranziții automate de fază legate de livrare: când un transfer de stoc (`stock.picking`) asociat comenzii de achiziție își schimbă `delivery_state`, faza comenzii este actualizată automat — `pre_advice` → fază `pre_advice`; `in_transit`/`in_warehouse`/`in_delivery` → fază `shipped`; `delivered` → fază `delivered`; `refused` → fază `refused` (*funcționalitate implementată în cod, dar nemenționată în `readme/DESCRIPTION.md` — vezi avertismentul din raport*).
- Fazele sunt configurabile liber (cod tehnic unic + nume afișat) din meniul Achiziții → Configurare → Purchase Order Phase; dacă un cod de fază referit nu există, se creează automat.
- Control manual: utilizatorii pot schimba oricând faza direct din formularul comenzii, iar modificările sunt auditabile prin chatter.
- Opțiune de a sări peste actualizările automate ale fazei, prin contextul `{"skip_phase_update": True}` la scrieri programatice pe `purchase.order` (util la import de date sau fluxuri speciale).

#### 3. Dependențe

- `purchase_stock`
- [deltatech_widget_many2one_badge](../deltatech_widget_many2one_badge/index.md)

#### 4. Componente Cheie

**Modele**

- `purchase.order.phase`: model nou care definește fazele configurabile (nume tradus, cod tehnic unic, secvență de ordonare, culoare pentru insignă, acțiune server opțională asociată).
- `purchase.order` (extindere): adaugă câmpul `phase_id` (urmărit în chatter) și metoda helper `set_phase(phase_step)` care caută/creează faza după cod și o scrie pe comandă; suprascrie `write()` pentru a declanșa automat tranziții de fază la schimbarea stării (`sent` → `rfq`, `purchase` → `purchase_confirm`), respectând cheia de context `skip_phase_update`.
- `stock.picking` (extindere): suprascrie `write()` pentru a propaga faza pe comanda de achiziție asociată (`purchase_id`) în funcție de `delivery_state` (`pre_advice`, `shipped`, `delivered`, `refused`).

**Vizualizări**

- `view_purchase_order_phase_form` / `view_purchase_order_phase_tree`: formular și listă pentru configurarea fazelor (nume, secvență, cod, culoare).
- `action_purchase_order_phase` + meniul `menu_purchase_order_phase`: acces din Achiziții → Configurare → Purchase Order Phase.
- `purchase_order_form` (extindere): adaugă câmpul `phase_id` ca insignă colorată pe formularul comenzii de achiziție.
- `purchase_order_view_tree` (extindere): adaugă câmpul `phase_id` ca insignă colorată în lista comenzilor de achiziție.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` proprii în modul. Modelul `purchase.order.phase` expune totuși un câmp opțional `action_id` (legătură către `ir.actions.server`), pregătit pentru extinderi, dar neutilizat implicit.
- Date demo/configurare inițială (`data/purchase_order_phase_data.xml`): fazele predefinite `rfq`, `purchase_confirm`, `pre_advice`, `shipped`, `delivered`.

#### 5. Conexiuni

- [deltatech_widget_many2one_badge](../deltatech_widget_many2one_badge/index.md): furnizează widget-ul `many2one_badge` folosit pentru afișarea colorată a fazei pe comandă.
- `purchase_stock`: modulul se integrează cu fluxul standard de achiziție-stoc (stare comandă și transferuri de stoc asociate) fără a-l altera.
