# RMA Lot / Serial (localizat la `deltatech_rma_lot/index.md`)

- **Nume Tehnic:** `deltatech_rma_lot`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_rma_lot
- **Cale Locală:** `odoo-addons/bitshop/deltatech_rma_lot`
- **Ultima Ingestie:** 2026-09-24
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Puntea pune lotul sau seria pe cererea de retur, o verifică față de ce a plecat efectiv din depozit către clientul respectiv și o duce pe transferul de retur, ca depozitul să nu o mai tasteze a doua oară. Trasabilitatea valorează ceva doar dacă e adevărată: un lot tastat de mână la intrare e locul cel mai ușor de stricat, fără ca nimic să semnaleze că seria aceea n-a plecat niciodată către clientul acesta. Stă separat de [deltatech_rma](../deltatech_rma/index.md), pentru că cele mai multe magazine nu vând nimic urmărit pe lot.

#### 2. Funcționalități Cheie

- Coloana **Lot / serie** pe fiecare linie de retur, limitată la loturile produsului liniei și editabilă doar la produsele urmărite; vizibilă cu grupul standard *Loturi și numere de serie*.
- Verificare la salvare față de livrarea liniei de comandă (`stock.move.line` de ieșire, efectuate): un lot al altui produs e refuzat, iar un lot al produsului corect, dar livrat altui client, e refuzat cu lista loturilor livrate efectiv în mesaj.
- O cerere a cărei livrare n-a fost încă validată nu se blochează: coletul ajunge uneori înaintea hârtiilor.
- **Repune în stoc** creează transferul de retur cu lotul de pe cerere deja pus pe operațiile detaliate (extindere a `_create_return_picking` din nucleu).
- Lotul apare și în *Retururi → Analiză → Produse returnate*, cu căutare după lot — util la o reclamație de serie către furnizor.

#### 3. Dependențe

- [deltatech_rma](../deltatech_rma/index.md)

#### 4. Componente Cheie

**Modele**

- `deltatech.rma.line` (extins): câmpul `lot_id` și constrângerea `_check_lot_was_delivered`.
- `deltatech.rma` (extins): `_create_return_picking` scrie lotul pe mișcările transferului de retur.

**Vizualizări**

- `view_deltatech_rma_form_lot`: coloana de lot pe liniile cererii.
- `view_deltatech_rma_line_list_lot` / `view_deltatech_rma_line_search_lot`: lotul în lista și căutarea produselor returnate.

Fluxul operațional pas-cu-pas, cu capturi, e în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 5. Conexiuni

- [deltatech_rma](../deltatech_rma/index.md): cererea și transferul de retur pe care puntea le completează.
- `stock`: loturile și mișcările de livrare față de care se verifică.
