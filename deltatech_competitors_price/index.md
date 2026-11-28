# Competitors Price Tracker (localizat la `deltatech_competitors_price/index.md`)

- **Nume Tehnic:** `deltatech_competitors_price`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_competitors_price
- **Cale Locală:** `odoo-addons/deltatech/deltatech_competitors_price`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite urmărirea prețurilor practicate de concurență pentru produsele proprii, direct din fișa de produs. Pentru fiecare produs se înregistrează adresele URL ale paginilor concurenților, iar prețul afișat acolo este adus la cerere printr-un clic pe butonul „Fetch". Echipele de vânzări și achiziții pot compara rapid poziționarea propriilor prețuri față de piață, fără verificări manuale pe site-uri și fără foi de calcul.

#### 2. Funcționalități Cheie

- Tab „Competitor Prices" pe fișa produsului, cu linii ce rețin concurentul, URL-ul produsului, ultimul preț și moneda, data ultimei preluări și mesajul de stare.
- Preluare la cerere: butonul „Fetch" de pe linie descarcă pagina concurentului, scrie prețul găsit, momentul preluării și starea „OK"; moneda liniei se actualizează dacă pagina indică o monedă existentă în baza de date (ex. EUR, USD).
- Extragere a prețului întâi din datele structurate ale paginii (JSON-LD sau Microdata, *Offer* și *AggregateOffer*), apoi, în lipsa lor, din tipare HTML uzuale: meta `product:price:amount`, atributul `itemprop="price"` și elemente cu clasă ce conține „price". Sunt înțelese ambele stiluri zecimale (1.234,56 și 1,234.56).
- Erori explicite: dacă nu se găsește prețul sau pagina nu poate fi încărcată (ex. 403, 404), linia păstrează ultimul preț, iar motivul apare în „Fetch Status".
- Doar adrese publice: serverul accesează numai adrese http(s) care se rezolvă la IP-uri publice și verifică fiecare redirecționare, astfel încât un URL nu poate fi folosit pentru a ajunge la servicii interne.
- Utilizatorii interni pot citi, crea, modifica și șterge liniile de concurență.
- Limitări: preluarea se face linie cu linie; nu există preluare programată (coloana „Auto Fetch", ascunsă implicit, doar marchează linii și nu are efect); site-urile care încarcă prețul prin JavaScript sau blochează cererile automate nu returnează preț.

#### 3. Dependențe

- `product`

Dependențe externe Python: `extruct`, `w3lib`.

#### 4. Componente Cheie

**Modele**

- `deltatech.competitor.price`: linie de urmărire a prețului concurenței (produs, concurent, URL, ultimul preț și monedă, data preluării, stare, marcaj `auto_fetch`); conține logica de extragere a prețului și `action_fetch_price()`.
- `product.template` (extindere): câmpul `competitor_price_ids` (One2many) și metoda `action_fetch_competitor_prices()`.

**Vizualizări**

- `view_deltatech_competitor_price_tree` / `view_deltatech_competitor_price_form`: listă și formular pentru liniile de preț, cu butonul „Fetch".
- `product_template_form_inherit_competitor_prices`: tab-ul „Competitor Prices" pe formularul produsului.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- `product`: modulul extinde direct fișa de produs (`product.template`) cu tab-ul de prețuri ale concurenței.
