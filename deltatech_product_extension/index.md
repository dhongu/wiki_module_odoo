# Deltatech Products Extension (localizat la `deltatech_product_extension/index.md`)

- **Nume Tehnic:** `deltatech_product_extension`
- **Versiune:** `19.0.1.1.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_product_extension
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_extension`
- **Ultima Ingestie:** `2026-11-03`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul extinde modelul standard de produs din Odoo cu câteva informații utile în activitatea zilnică: termenul de valabilitate (durata de viață pe raft), producătorul și dimensiunile produsului, introduse ca text liber. Este destinat companiilor care au nevoie de o urmărire mai detaliată a atributelor produselor, de exemplu pentru stocul perisabil sau sensibil la timp, pentru documente și cataloage sau pentru organizarea partenerilor în funcție de calitatea de producător.

#### 2. Funcționalități Cheie

- **Urmărire logistică îmbunătățită**: adaugă pe șablonul de produs câmpurile **Termen de valabilitate (Shelf Life)** și **Unitate de măsură pentru termenul de valabilitate**, pentru o gestionare mai bună a stocului perisabil sau sensibil la timp.
- **Informații despre producător**: pe fișa produsului apare câmpul **Producător** (partener), sub categoria produsului, cu acces rapid la originea de fabricație și la datele de contact.
- **Dimensiuni ca text liber**: câmpul **Dimensiuni** se completează liber (de exemplu „120 x 60 x 75 cm”) și este util în documente, cataloage și ca referință rapidă. Câmpul nu calculează volumul produsului; pentru lungime, lățime și înălțime numerice care completează volumul se folosește modulul Product Dimensions (`deltatech_product_dimension`).
- **Poziționare pe formular**: **Dimensiunile** și **Termenul de valabilitate** apar în fila **General Information**, lângă cost; produsele se deschid din **Sales > Products > Products** sau **Inventory > Products > Products**.
- **Integrare cu partenerii**: modelul de partener primește bifa **Producător**, pentru etichetarea furnizorilor și filtrarea mai ușoară în aplicația Contacte.
- **Analiza facturilor**: în **Invoice Analysis** se poate căuta și grupa după producător (**Group By > Manufacturer**).

#### 3. Dependențe

- `product`
- `account`

#### 4. Componente Cheie

Conform fluxului de ingestie (prioritizarea Readme), această secțiune nu este detaliată prin analiza codului, deoarece fișierul `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie și nu solicită explicit documentarea Componentelor Cheie.

#### 5. Conexiuni

Nu au fost identificate conexiuni către alte pagini de module din wiki. Dependențele directe (`product`, `account`) sunt module standard Odoo și nu au încă pagină wiki. Pentru dimensiuni numerice cu calcul de volum, vezi modulul `deltatech_product_dimension`.
