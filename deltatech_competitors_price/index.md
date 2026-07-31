# Deltatech Competitors Price (localizat la `deltatech_competitors_price/index.md`)

- **Nume Tehnic:** `deltatech_competitors_price`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_competitors_price
- **Cale Locală:** `odoo-addons/deltatech/deltatech_competitors_price`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul permite urmărirea prețurilor practicate de concurență pentru produsele proprii, direct din fișa de produs. Pentru fiecare produs se pot înregistra una sau mai multe adrese URL către paginile concurenților, iar prețul afișat acolo poate fi adus automat, la cerere, printr-un simplu clic pe butonul de preluare. Este util echipelor de vânzări și achiziții pentru a compara rapid poziționarea propriilor prețuri față de piață, fără a mai căuta manual pe site-urile concurenților.

#### 2. Funcționalități Cheie

- Linii de concurenți pe fișa produsului (Product Template), fiecare cu: nume concurent, URL-ul produsului pe site-ul concurentului, ultimul preț preluat și moneda acestuia, data/ora ultimei preluări și un mesaj de stare, plus un marcaj „Auto Fetch" pentru o eventuală preluare automată programată ulterior.
- Preluare la cerere: buton „Fetch" pe fiecare linie, plus un buton la nivel de produs („Aducere preț concurență") care preia deodată toate liniile.
- Extragere robustă a prețului: se încearcă întâi date structurate (JSON-LD / Microdata) via `extruct`, dacă biblioteca este instalată, apoi se trece la euristici pe HTML (meta tag-uri, elemente cu clase/atribute de preț) folosind `lxml`.
- Detectarea și actualizarea automată a monedei liniei, dacă codul valutar identificat pe pagină există în baza de date.
- Gestionare clară a erorilor: fiecare linie păstrează un mesaj de stare (ex. „Price not found on page” sau eroarea tehnică întâmpinată), astfel utilizatorul vede imediat de ce o preluare nu a reușit.
- Funcționează și fără `extruct` instalat — se aplică doar fallback-ul euristic pe HTML.

*Sursă: `readme/DESCRIPTION.md` (tradus și adaptat; secțiunea de testare din DESCRIPTION.md menționa un exemplu de rulare cu `odoo18.conf` — corectat mai jos, fără relevanță pentru conținutul funcțional al modulului, care e valabil pentru 19.0).*

#### 3. Dependențe

- `product`

#### 4. Componente Cheie

**Modele**

- `deltatech.competitor.price`: model nou care reține o linie de urmărire preț concurență — produs (`product_tmpl_id`), nume concurent, URL produs, ultimul preț și monedă, data ultimei preluări, mesaj de stare și marcajul `auto_fetch`. Conține logica de extragere a prețului (din date structurate JSON-LD/Microdata via `extruct`, cu fallback pe euristici HTML via `lxml`) și metoda `action_fetch_price()` care declanșează preluarea (HTTP GET cu User-Agent de browser) și scrie rezultatul pe linie.
- `product.template` (extindere): adaugă câmpul `competitor_price_ids` (One2many către `deltatech.competitor.price`) și metoda `action_fetch_competitor_prices()`, care preia dintr-o singură acțiune toate liniile de concurenți ale produsului.

**Vizualizări**

- `view_deltatech_competitor_price_tree` / `view_deltatech_competitor_price_form`: listă editabilă și formular dedicate liniilor de preț concurență, fiecare cu buton „Fetch”.
- `product_template_form_inherit_competitor_prices`: extensie a formularului de produs (`product.product_template_only_form_view`) care adaugă tab-ul „Competitor Prices” cu lista editabilă a liniilor de concurenți direct pe fișa produsului.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni `ir.cron`, `base.automation` sau `ir.actions.server` în modul. Câmpul `auto_fetch` este pregătit pentru o eventuală preluare programată viitoare, dar cron-ul nu este activat implicit.

#### 5. Conexiuni

- `product`: modulul extinde direct fișa de produs (`product.template`) cu tab-ul de prețuri concurență.

---

**Corecții/avertismente aplicate la ingestie:** secțiunea de testare din `readme/DESCRIPTION.md` conținea un exemplu de comandă cu `odoo18.conf`; a fost păstrat doar conținutul funcțional relevant, fără a reproduce comanda cu configurația veche 18, întrucât modulul e livrat pentru 19.0. Dependența `product` nu are încă pagină wiki proprie, așa că a rămas ca text `cod`.
