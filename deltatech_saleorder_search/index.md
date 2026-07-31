# Deltatech Sale Order Search by Partner Fields (localizat la `deltatech_saleorder_search/index.md`)

- **Nume Tehnic:** `deltatech_saleorder_search`
- **Versiune:** `19.0.1.0.2`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_saleorder_search`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_saleorder_search`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul îmbunătățește căutarea comenzilor de vânzare din Odoo, permițând utilizatorilor să găsească rapid o comandă pe baza datelor de contact ale clientului — e-mail sau telefon — nu doar după numele partenerului sau numărul comenzii. Este util în special echipelor de vânzări și de suport care primesc un telefon sau un e-mail de la client și trebuie să localizeze instant comanda asociată.

#### 2. Funcționalități Cheie

- Extinde opțiunile implicite de căutare din listele de oferte și comenzi de vânzare cu câmpurile de e-mail și telefon ale partenerului.
- Permite echipelor de vânzări să găsească rapid o comandă atunci când dispun doar de datele de contact ale clientului.
- Îmbunătățește eficiența căutării și capacitatea de răspuns către clienți.
- Se integrează direct în vizualizarea standard de căutare (search view) din modulul Vânzări, fără a modifica alte fluxuri.

#### 3. Dependențe

- `sale`

#### 4. Componente Cheie

**Modele**

- Modulul nu definește sau extinde niciun model Python; adaugă exclusiv câmpuri de filtrare în vizualizarea de căutare, mapate pe `partner_id.email` și `partner_id.phone` de pe modelul `sale.order`.

**Vizualizări**

- `view_sales_order_filter`: extinde vizualizarea de căutare standard (`sale.view_sales_order_filter`) adăugând două filtre suplimentare — „E-mail" (`partner_id.email`) și „Phone" (`partner_id.phone`) — ambele cu potrivire parțială (`ilike`).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate, sarcini cron sau acțiuni server în acest modul.

#### 5. Conexiuni

- Nu au fost identificate conexiuni funcționale relevante către alte module cu pagină wiki.
