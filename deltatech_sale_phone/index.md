# Sale Phone (localizat la `deltatech_sale_phone/index.md`)

- **Nume Tehnic:** `deltatech_sale_phone`
- **Versiune:** `19.0.1.0.6`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_phone
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_phone`
- **Ultima Ingestie:** `2026-11-12`

#### 1. Sumar

Echipa de vânzări și cea de contabilitate au adesea nevoie să sune un client în timp ce lucrează la o ofertă sau la o factură. Acest modul afișează numărul de telefon al clientului direct pe formularul comenzii de vânzare și pe cel al facturii, fără a fi nevoie să deschidă mai întâi fișa contactului.

#### 2. Funcționalități Cheie

- **Telefon pe comenzile de vânzare:** un câmp *Phone* apare imediat după client pe formularul comenzii, afișat cu widget-ul de telefon.
- **Telefon pe facturi:** același câmp *Phone* apare în grupul din stânga al antetului facturii, după adresa de livrare.
- **Preluat de la client:** valoarea este telefonul clientului din document, iar câmpul rămâne gol dacă clientul nu are telefon. Este doar pentru citire: pentru a schimba numărul se editează clientul.
- **Nestocat:** numărul nu se salvează pe document; afișează mereu telefonul curent al clientului, inclusiv pe facturile postate.
- Modulul nu adaugă meniuri, setări sau grupuri și nu modifică listele sau documentele tipărite.

#### 3. Dependențe

- `sale`
- `account`

#### 4. Componente Cheie

Conform fluxului de ingestie, Sumarul și Funcționalitățile Cheie provin din `readme/DESCRIPTION.md`; mai jos sunt doar reperele confirmate în cod.

**Modele**

- `sale.order` (extins): adaugă câmpul calculat și nestocat `partner_phone`, preluat din telefonul partenerului comenzii.
- `account.move` (extins): adaugă câmpul calculat și nestocat `partner_phone`, preluat din telefonul partenerului facturii.

**Vizualizări**

- `sale_order_view_form`: extinde formularul comenzii de vânzare (`sale.view_order_form`) pentru a afișa câmpul de telefon după partener.
- `view_move_form`: extinde formularul facturii (`account.view_move_form`) pentru a afișa câmpul de telefon după adresa de livrare.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate, sarcini cron sau acțiuni server în acest modul.

#### 5. Conexiuni

- Nu au fost identificate conexiuni funcționale relevante către alte module cu pagină wiki.
