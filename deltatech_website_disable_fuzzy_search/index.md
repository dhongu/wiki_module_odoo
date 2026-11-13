# Website Disable Fuzzy Search

- **Nume Tehnic:** `deltatech_website_disable_fuzzy_search`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_disable_fuzzy_search
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_disable_fuzzy_search`
- **Ultima Ingestie:** `2026-11-13`

#### 1. Sumar

Când potrivirea „fuzzy” (aproximativă) este activă, căutarea din website poate găsi cuvinte apropiate de cel introdus. Acest modul dezactivează potrivirea aproximativă în bara de căutare a website-ului și în căutarea de produse din magazinul online, astfel încât clientul să primească doar rezultate care corespund efectiv termenului introdus.

#### 2. Funcționalități Cheie

- **Bara de căutare:** bara de căutare a website-ului nu mai folosește potrivirea aproximativă, indiferent ce cere pagina.
- **Căutarea în magazin:** căutarea de produse din magazinul online nu o folosește nici ea.
- **Mereu activ:** nu există setare sau meniu. Odată instalat, modulul se aplică tuturor website-urilor, vizitatorilor și limbilor din baza de date.
- **Fără excepții per website:** fiindcă nu are setări, modulul nu poate fi oprit pentru un singur website; pentru a recăpăta căutarea aproximativă, modulul se dezinstalează.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

- Modulul nu definește și nu extinde modele.

**Vizualizări**

- Modulul nu adaugă vizualizări, date, meniuri sau reguli de acces.

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau acțiuni server. Modificarea se face în controllere (`controllers/main.py`): `Website.autocomplete` și `WebsiteSale._get_search_options` forțează `allowFuzzy = False` pentru autocompletare, respectiv pentru căutarea din magazin.

#### 5. Conexiuni

- `website_sale`: modulul de bază pentru magazinul online, ale cărui controllere de căutare sunt extinse pentru a dezactiva potrivirea aproximativă.
