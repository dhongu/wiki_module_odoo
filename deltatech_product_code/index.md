# Codificare Produse (localizat la `deltatech_product_code/index.md`)

- **Nume Tehnic:** `deltatech_product_code`
- **Versiune:** `20.0.1.2.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_product_code
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_code`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă instrumente pentru generarea automată a referinței interne (cod intern) și a codului de bare al produselor, plus verificări care împiedică codurile duplicate. Este destinat companiilor care au nevoie de o codificare strictă și uniformă pe tot catalogul, pentru produse și variante.

#### 2. Funcționalități Cheie

- Generarea automată a referinței interne dintr-o secvență aleasă pe categoria de produs (**Inventar → Configurare → Categorii de produse**, grupul *Produse*, câmpul *Secvență cod*). O referință introdusă manual se păstrează.
- Generarea codului de bare, dacă pe categorie este bifat *Generează cod de bare*. Sursa codului: *prefix intern* (prefix de 2 cifre între `20` și `29`, urmat de cifrele referinței sau de un număr aleatoriu, după bifa *Cod de bare aleatoriu*) sau *prefix de companie GS1*.
- Alocarea GTIN-13 din prefixul de companie GS1 (6-11 cifre): fiecare produs nou primește următorul cod liber din plaja alocată, cu cifra de control calculată automat; câmpul *Coduri GTIN libere* arată câte au rămas.
- Acțiunile din meniul **Acțiuni** al produsului: *Forțează cod intern nou* (număr nou din secvență, chiar dacă produsul are deja referință; codul de bare existent nu se schimbă) și *Găsește duplicate* (listează produsele care au aceeași referință, în aceeași companie și cu aceeași stare activă).
- Doi produși activi din aceeași companie nu pot avea aceeași referință: salvarea este refuzată cu mesajul „Internal Reference already exists”.
- Codul se generează la salvarea produsului cu categorie aleasă; o creare rapidă (doar denumirea) nu are categorie, deci nu primește cod. Fluxul detaliat este în fișa consultantului.

#### 3. Dependențe

- `product`
- `barcodes`

#### 4. Componente Cheie

**Modele**

- `product.category` (extins): secvența de cod, opțiunile de generare a codului de bare, prefixul GS1 și numărătorul de coduri GTIN libere.
- `product.template` / `product.product` (extinse): generarea referinței la creare și constrângerea de unicitate a referinței interne.

**Vizualizări**

- `views/product_view.xml`: câmpurile de codificare pe categoria de produs și acțiunile din fișa produsului.

**Acțiuni Automate / Acțiuni Server**

- Acțiunile *Forțează cod intern nou* și *Găsește duplicate* din meniul Acțiuni al produsului.

#### 5. Conexiuni

- Nu au fost identificate conexiuni către alte pagini wiki de module.
