# Batch Reception Note (localizat la `deltatech_reception_note/index.md`)

- **Nume Tehnic:** `deltatech_reception_note`
- **Versiune:** `20.0.0.1.7`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_reception_note`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_reception_note`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul permite recepția mărfii de la furnizor pe note de recepție care consumă cantitățile deschise ale mai multor comenzi de achiziție deodată, în loc să se valideze separat recepția fiecărei comenzi. Este util când o livrare acoperă mai multe comenzi sau când o comandă sosește în mai multe livrări.

#### 2. Funcționalități Cheie

- **Tipuri de comenzi de achiziție:** fiecare comandă are un *Type*:
  - *Normal*: comanda standard;
  - *RFQ Only*: o cerere care păstrează cantitățile încă așteptate de la furnizor; nu poate fi confirmată și are butonul *Set as sent*;
  - *Reception Note*: livrarea efectiv primită, cu *Delivery Note No* al furnizorului.
- **Create reception note:** pe o comandă *Normal*, *Actions > Create reception note* mută cantitățile deschise pe o comandă nouă *RFQ Only* în starea *RFQ Sent* (același furnizor, companie, monedă, poziție fiscală, termene de plată, prețuri și taxe, cu cantitatea încă nerecepționată pe fiecare linie). Recepțiile *Ready* ale comenzii sursă sunt anulate, deci marfa se recepționează doar prin note de recepție.
- **Nota de recepție:** la confirmare, cantitățile se iau din comenzile *RFQ Only* trimise, ale aceluiași furnizor și companii, începând cu cele mai vechi, în unitatea de măsură a produsului; recepția se creează prin confirmarea standard. O comandă *RFQ Only* consumată integral este marcată ca goală.
- **Ignore quantities:** dacă un produs sau o cantitate nu se găsește pe o comandă *RFQ Only* trimisă, confirmarea se oprește cu un mesaj; bifa *Ignore quantities* permite confirmarea, iar cantitățile forțate sunt listate în chatter.
- **Meniuri și filtre:** *Achiziții > Reception notes* are *Prepare reception note* (note neconfirmate sau nefacturate), *To arrive* (transferuri de intrare *Ready*) și *To invoice* (transferuri de intrare *Done*, indiferent dacă au fost facturate). Listele afișează opțional *Type* și *Date sent*; căutarea are filtrele *Not empty* și *Empty* pentru comenzile *RFQ Only*.
- **Limitare:** modulul nu adaugă document tipărit propriu; nota se tipărește cu rapoartele standard de achiziție.

#### 3. Dependențe

- `purchase_stock`

#### 4. Componente Cheie

**Modele**

- `purchase.order` (extins): tipul comenzii, numărul notei de livrare, logica de creare și consum a notelor de recepție.
- `reception.note.create` (wizard): crearea notei de recepție din comanda de achiziție.

**Vizualizări**

- `views/purchase_view.xml`: formulare, liste și căutare cu tipul comenzii; acțiunile de meniu *Prepare reception note*, *To arrive* și *To invoice*.
- `wizard/reception_note.xml`: wizardul de creare a notei de recepție.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate sau server.

#### 5. Conexiuni

- [deltatech_fast_purchase](../deltatech_fast_purchase/index.md): extindere a fluxului de achiziție din aceeași suită deltatech.
- [deltatech_purchase_price](../deltatech_purchase_price/index.md): logică de prețuri pe comenzile de achiziție, complementară fluxului de recepție.
- [deltatech_stock_account](../deltatech_stock_account/index.md): contabilizarea mișcărilor de stoc rezultate din recepții.
