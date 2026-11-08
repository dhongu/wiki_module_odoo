# Competitors Price Tracker (localizat la `deltatech_competitors_price/index.md`)

- **Nume Tehnic:** `deltatech_competitors_price`
- **Versiune:** `19.0.1.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_competitors_price
- **Cale Locală:** `odoo-addons/deltatech/deltatech_competitors_price`
- **Ultima Ingestie:** `2026-11-08`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul permite urmărirea prețurilor practicate de concurență pentru produsele proprii, direct din fișa de produs. Pentru fiecare produs se pot înregistra una sau mai multe adrese URL către paginile concurenților, iar prețul afișat acolo poate fi adus la cerere, printr-un clic pe butonul de preluare al liniei. Este util echipelor de vânzări și achiziții pentru a compara rapid poziționarea propriilor prețuri față de piață, fără a mai căuta manual pe site-urile concurenților sau a copia prețurile în foi de calcul.

#### 2. Funcționalități Cheie

- Tab-ul **Competitor Prices** pe fișa produsului, cu linii de concurenți: **Competitor** (nume), **Product URL** (adresa produsului pe site-ul concurentului), **Last Price** și **Currency**, **Last Fetch** (data ultimei preluări) și **Fetch Status** (mesaj de stare).
- Preluare la cerere, **linie cu linie**: butonul **Fetch** de pe linie descarcă pagina concurentului și scrie prețul găsit, momentul preluării și starea *OK*. Nu există un buton care să preia deodată toate liniile unui produs.
- Dacă pagina indică o monedă care există în baza de date (ex. EUR, USD), moneda liniei se actualizează automat.
- Extragerea prețului: se citesc întâi datele structurate ale paginii (JSON-LD sau Microdata, *Offer* și *AggregateOffer*); dacă lipsesc, se încearcă tipare HTML uzuale (meta tag-ul `product:price:amount`, atributul `itemprop="price"`, elemente cu clasa „price"). Sunt înțelese ambele stiluri de zecimale (1.234,56 și 1,234.56).
- Erori clare: dacă nu se găsește prețul sau pagina nu se poate încărca (ex. 403, 404), linia își păstrează ultimul preț, iar motivul apare în **Fetch Status**.
- Doar adrese publice: serverul preia numai adrese http(s) care se rezolvă exclusiv la adrese IP publice și verifică fiecare redirecționare (cel mult 5), deci un URL nu poate fi folosit pentru a ajunge la servicii interne. URL-urile din intranet sau de pe adrese private nu mai sunt preluate.
- Utilizatorii interni pot citi, crea, modifica și șterge liniile de concurenți.
- Limitări: coloana **Auto Fetch** (ascunsă implicit) doar marchează liniile și nu are efect, nu există preluare programată; site-urile care încarcă prețul prin JavaScript sau blochează cererile automate nu returnează preț.

#### 3. Dependențe

- `product`

Dependențe externe Python (din manifest): `extruct`, `w3lib`; în cod, `extruct` este tratat ca opțional (fără el se aplică doar euristicile HTML).

#### 4. Componente Cheie

**Modele**

- `deltatech.competitor.price`: linie de urmărire a prețului concurenței — produs (`product_tmpl_id`), nume concurent, URL, ultimul preț și monedă, data ultimei preluări, mesaj de stare și marcajul `auto_fetch`. Conține extragerea prețului (date structurate prin `extruct`, apoi euristici HTML prin `lxml`), verificarea adreselor publice (`_check_public_url`, redirecționări urmărite manual) și `action_fetch_price()`, care declanșează preluarea.
- `product.template` (extindere): adaugă câmpul `competitor_price_ids` (One2many către `deltatech.competitor.price`) și metoda `action_fetch_competitor_prices()`, care preia toate liniile unui produs; nicio vizualizare nu o expune printr-un buton.

**Vizualizări**

- `view_deltatech_competitor_price_tree` / `view_deltatech_competitor_price_form`: listă editabilă și formular pentru liniile de preț concurență, cu butoanele **Fetch** și **Fetch Now**.
- `product_template_form_inherit_competitor_prices`: extinde formularul de produs cu tab-ul **Competitor Prices**, cu lista editabilă a liniilor.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite acțiuni `ir.cron`, `base.automation` sau `ir.actions.server`. Câmpul `auto_fetch` este doar un marcaj, fără preluare programată.

#### 5. Conexiuni

- `product`: modulul extinde direct fișa de produs (`product.template`) cu tab-ul de prețuri concurență.
