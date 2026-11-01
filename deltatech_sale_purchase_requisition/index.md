# Sale → Purchase RFQ (Alternative Purchase Orders) (localizat la `deltatech_sale_purchase_requisition/index.md`)

- **Nume Tehnic:** `deltatech_sale_purchase_requisition`
- **Versiune:** `19.0.1.1.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_purchase_requisition
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_purchase_requisition`
- **Ultima Ingestie:** `2026-11-01`

#### 1. Sumar

Modulul adaugă un buton pe oferta de vânzare (cotația) care permite crearea de cereri de ofertă către furnizori (RFQ-uri) pornind de la liniile cotației, legându-le apoi înapoi de oferta de vânzare. Fluxul este unul simplu, aliniat la abordarea standard Odoo de achiziții alternative (alternative purchase orders), fără a folosi acorduri de achiziție (purchase requisition/agreements). Astfel, agentul de vânzări poate iniția rapid procesul de aprovizionare pentru produsele dintr-o ofertă, iar cumpărătorul alege furnizorul și finalizează cererea de ofertă. Modul nou în 19.0.

#### 2. Funcționalități Cheie

- Buton în antetul ofertei de vânzare, „Create RFQ”, pentru a genera cereri de ofertă din liniile cotației; este vizibil doar în stările ciornă/trimisă și doar pentru utilizatorii de achiziții.
- Deschide formularul de comandă de achiziție în mod creare, precompletat cu produsele eligibile din ofertă (fără creare automată); originea și oferta sursă sunt completate automat.
- Cumpărătorul selectează furnizorul și salvează cererea de ofertă (comandă de achiziție în starea draft); prețul unitar rămâne de completat de cumpărător.
- Buton inteligent (smart button) „RFQs” pe ofertă, care afișează numărul și deschide cererile de ofertă legate (direct formularul, dacă există una singură).
- Reguli de eligibilitate pentru linii: produsul trebuie să fie achiziționabil (`purchase_ok = True`), cantitatea trebuie să fie strict mai mare decât 0, iar liniile de secțiune/notă/afișaj sunt ignorate. Dacă oferta nu are linii sau nicio linie nu e eligibilă, utilizatorul primește un mesaj de eroare.
- Compatibil cu comenzile de achiziție alternative, fără a introduce acorduri de achiziție.

#### 3. Dependențe

- `purchase`
- `sale`

#### 4. Componente Cheie

Readme-ul nu cere explicit detalierea componentelor; mai jos sunt cele verificate în cod.

**Modele**

- `sale.order`: extins cu `rfq_ids`, `rfq_count`, acțiunea `action_create_rfq` (deschide formularul de achiziție precompletat) și `action_view_rfq` (butonul inteligent).
- `purchase.order`: extins cu câmpul `quote_id` („Sale Quote”), legătura înapoi către oferta de vânzare sursă.

**Vizualizări**

- `view_order_form_inherit_deltatech_requisition`: moștenește formularul `sale.view_order_form`; adaugă în antet butonul „Create RFQ” (vizibil în stările `draft`/`sent`, pentru grupul `purchase.group_purchase_user`) și un buton inteligent „RFQs” în `button_box`, vizibil când există cereri legate.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server în modul.

#### 5. Conexiuni

- `purchase`: modulul de achiziții pe care se bazează cererile de ofertă (RFQ) generate.
- `sale`: modulul de vânzări care furnizează oferta sursă și liniile sale.
