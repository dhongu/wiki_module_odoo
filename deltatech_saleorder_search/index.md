# Sale Order Search by Contact (localizat la `deltatech_saleorder_search/index.md`)

- **Nume Tehnic:** `deltatech_saleorder_search`
- **Versiune:** `19.0.1.1.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_saleorder_search
- **Cale Locală:** `odoo-addons/deltatech/deltatech_saleorder_search`
- **Ultima Ingestie:** `2026-11-11`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul îmbunătățește căutarea comenzilor de vânzare din Odoo, permițând utilizatorilor să găsească rapid o comandă pe baza datelor de contact ale clientului — e-mail sau telefon — nu doar după numele partenerului sau numărul comenzii. Este util în special echipelor de vânzări și de suport care primesc un telefon sau un e-mail de la client și trebuie să localizeze instant comanda asociată.

#### 2. Funcționalități Cheie

- Bara de căutare din oferte și comenzi de vânzare primește opțiunea **Search E-mail for: ...**, care returnează comenzile al căror client are o adresă de e-mail ce conține textul introdus (de exemplu un domeniu comun, `@example.com`, găsește comenzile tuturor clienților de pe acel domeniu).
- Opțiunea **Search Phone for: ...** face același lucru pentru telefonul clientului; textul se potrivește exact așa cum a fost scris, deci se introduce numărul în formatul stocat pe contact (un fragment scurt, fără spații sau prefix, găsește cele mai multe variante).
- Funcționează în *Vânzări > Comenzi > Oferte* și *Vânzări > Comenzi > Comenzi*, precum și în orice altă listă de comenzi care folosește vizualizarea de căutare standard; nu necesită configurare.
- Căutarea se face după e-mailul și telefonul contactului setat ca *Client* pe comandă, nu după celelalte contacte ale aceleiași companii.
- Modulul conține doar date (fără cod Python), deci poate fi folosit și pe Odoo Online (plan Custom), prin *Aplicații > Importă modul*.

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
