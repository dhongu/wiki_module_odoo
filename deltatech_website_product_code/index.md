# eCommerce Product Code (localizat la `deltatech_website_product_code/index.md`)

- **Nume Tehnic:** `deltatech_website_product_code`
- **Versiune:** `19.0.1.3.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_product_code
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_product_code`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul extinde magazinul online Odoo (eCommerce) pentru a permite accesarea și identificarea produselor pe baza codului intern de referință. Clienții și operatorii pot deschide direct pagina unui produs folosind codul acestuia, iar codul intern este afișat atât pe pagina produsului, cât și în rezultatele căutării. Modulul include și o căutare rapidă optimizată pentru cazul în care mai multe coduri de produs sunt lipite deodată în câmpul de căutare din magazin (util în scenarii B2B, unde produsele sunt cunoscute după cod, nu după denumire).

#### 2. Funcționalități Cheie

- Afișarea paginii produsului folosind codul intern (link: `/shop/product-code/<cod>`)
- Afișarea codului produsului pe pagina produsului
- Afișarea codului produsului în rezultatele căutării
- Căutare rapidă atunci când mai multe coduri de produs sunt lipite deodată în câmpul de căutare al magazinului (găsește orice produs care se potrivește, fără să ceară ca toate codurile să aparțină aceluiași produs)
- Căutare cu potrivire exactă a expresiei (opțională), pentru cataloage ale căror coduri conțin spații (numere de piese OEM, de ex. `352 030 15 97`)
- Parametri de configurare în Website > Configurare > Setări, secțiunea *Product Search*:
  - `website_search.min_term_length` (implicit `3`): termenii de căutare mai scurți decât această valoare sunt ignorați, deoarece nu pot folosi indexurile trigram și doar încetinesc căutarea
  - `website_search.multi_code_min_terms` (implicit `4`): numărul minim de termeni ce arată a coduri (ex. `AMAT1-12345`) lipiți împreună înainte ca să pornească căutarea rapidă multi-cod; se poate dezactiva cu `False`/`0`, revenind la căutarea normală
  - `website_search.exact_phrase` (implicit `False`): caută întregul termen ca un singur șir în loc să-l despartă după spații; util pentru cataloage ale căror coduri conțin spații, astfel încât căutarea `352 030 15 97` returnează produsul cu acel cod exact, nu toate produsele care conțin `352`, `030`, `15` sau `97`. Dacă niciun produs nu se potrivește pe tot termenul, se aplică automat căutarea obișnuită per-termen. Se aplică doar termenilor care conțin o cifră: un termen format doar din cuvinte (`Lant CLAAS`) e tratat ca descriere, nu ca și cod, iar cuvintele lui sunt căutate separat mai departe
  - `website_search.standalone_code_min_length` (implicit `5`): folosit doar cât timp căutarea cu potrivire exactă e activă, ca să distingă o listă de coduri complete lipite de grupurile unui singur cod cu spații; termenii mai scurți decât această valoare sunt considerați grupuri ale unui singur cod, deci nu sunt combinați cu OR între ei; se poate dezactiva cu `False`/`0`, acceptând termeni de orice lungime ca fiind coduri

#### 3. Dependențe

- `website`
- `website_sale`

#### 4. Componente Cheie

*Conform fluxului de ingestie, această secțiune se omite deoarece `readme/DESCRIPTION.md` este prezent și acoperă Sumarul și Funcționalitățile Cheie.*

#### 5. Conexiuni

- Nu au fost identificate conexiuni cu alte module documentate în wiki.
