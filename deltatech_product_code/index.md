# Codificare Produse (localizat la `deltatech_product_code/index.md`)

- **Nume Tehnic:** `deltatech_product_code`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_product_code
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_code`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Acest modul îmbunătățește gestiunea produselor din Odoo, oferind instrumente avansate pentru generarea automată a referinței interne, administrarea codurilor de bare și menținerea consistenței datelor. Este destinat companiilor care au nevoie de o codificare strictă și structurată a produselor pe întregul catalog, evitând codurile duplicate și asigurând o identificare uniformă a produselor și a variantelor. Codurile de bare pot fi generate fie dintr-un prefix intern, fie din prefixul de companie primit de la GS1.

#### 2. Funcționalități Cheie

- Generarea automată a referinței interne pe baza secvențelor definite pe categoria de produs. Dacă numărul propus este deja folosit (inclusiv de produse arhivate sau din alte companii), secvența este mutată peste cel mai mare număr existent cu același prefix/sufix, deci nu mai apare eroarea „Internal Reference already exists”. Secvențele cu intervale de date nu se sincronizează.
- Gestionarea îmbunătățită a codurilor de bare: pe categoria de produs se bifează generarea codului de bare și se alege „Sursa codului de bare” (Barcode Source).
  - „Internal prefix”: codul se construiește din prefixul intern (2 cifre, implicit `20`, intervalul GS1 rezervat uz intern) și din referința internă sau un număr aleatoriu.
  - „GS1 company prefix”: fiecare produs nou primește următorul GTIN-13 liber din intervalul prefixului de companie primit de la GS1 (6–11 cifre), cu cifra de control calculată automat. Se iau în calcul codurile de bare ale produselor și ale ambalajelor, inclusiv cele arhivate. Categoria afișează câte coduri mai sunt libere, iar la epuizarea intervalului se afișează o eroare.
- Verificări de consistență pentru a preveni codurile de produs duplicate, ținând cont de companie, cu acțiunea „Find Duplicate” disponibilă pe produs și pe variantă.
- Suport atât pentru produse (șabloane), cât și pentru variantele de produs; butonul „New internal code” generează un cod nou din formular.

#### 3. Dependențe

- `product`
- `barcodes`

#### 4. Componente Cheie

> Secțiune omisă conform fluxului de ingestie: fișierul `readme/DESCRIPTION.md` este prezent și acoperă Sumarul și Funcționalitățile Cheie, fără a solicita explicit analiza componentelor tehnice.

#### 5. Conexiuni

- Nu au fost identificate conexiuni documentate către alte pagini wiki de module.
