# Sale → Purchase RFQ (Alternative Purchase Orders) (localizat la `deltatech_sale_purchase_requisition/index.md`)

- **Nume Tehnic:** `deltatech_sale_purchase_requisition`
- **Versiune:** `20.0.1.1.3`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_purchase_requisition`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_purchase_requisition`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul permite pornirea de cereri de ofertă (RFQ) către furnizori direct dintr-o ofertă de vânzare, astfel încât cumpărătorul să poată stabili prețurile de achiziție înainte ca oferta să ajungă la client, iar RFQ-urile rămân legate de ofertă. Nu se creează acorduri de achiziție și nu este nevoie de modulul *Purchase Agreements*.

#### 2. Funcționalități Cheie

- **Buton Create RFQ** în antetul ofertei (stările *Quotation* și *Quotation Sent*): deschide un formular nou de comandă de achiziție, nesalvat încă, precompletat cu liniile ofertei care pot fi achiziționate (produs cu *Purchase* bifat și cantitate peste zero), cu unitatea de măsură, cantitatea și descrierea lor (când linia nu are descriere, se folosește descrierea furnizorului din produs).
- Numărul ofertei devine *Source* pe RFQ, iar compania ofertei este preluată; secțiunile și notele sunt ignorate.
- Cumpărătorul alege furnizorul, verifică prețurile și salvează RFQ-ul. Butonul poate fi folosit din nou pentru alți furnizori, deci aceeași ofertă poate fi evaluată de mai mulți furnizori.
- **RFQ-uri legate:** fiecare RFQ păstrează oferta de la care a pornit. Butonul inteligent *RFQs* de pe ofertă arată numărul lor și le deschide (sau deschide direct RFQ-ul, dacă e unul singur).
- **Acces:** butonul este vizibil utilizatorilor cu drepturi de achiziții (*Purchase*: *User* sau *Administrator*).

#### 3. Dependențe

- `purchase`
- `sale`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): adaugă `rfq_ids`, `rfq_count`, acțiunile `action_create_rfq` și `action_view_rfq`.
- `purchase.order` (extins): adaugă `quote_id`, legătura înapoi către oferta de vânzare sursă.

**Vizualizări**

- `view_order_form_inherit_deltatech_requisition`: moștenește `sale.view_order_form`; adaugă butonul *Create RFQ* în antet și butonul inteligent cu numărul de RFQ-uri.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- `purchase`: modulul de achiziții în care se creează RFQ-urile.
- `sale`: oferta de vânzare sursă și liniile ei.
