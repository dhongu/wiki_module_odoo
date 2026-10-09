# KPI Cards (localizat la `deltatech_web_kpi_cards/index.md`)

- **Nume Tehnic:** `deltatech_web_kpi_cards`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_web_kpi_cards
- **Cale Locală:** `odoo-addons/deltatech/deltatech_web_kpi_cards`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modul tehnic care oferă o bandă de carduri KPI, pe care alte module o așază deasupra vizualizărilor din backend, și legătura care face ca un clic pe card să activeze filtrul de căutare corespunzător. Toate tablourile de bord au astfel același aspect și același comportament. Modulul nu face nimic singur: se instalează ca dependență a modulelor care afișează carduri.

#### 2. Funcționalități Cheie

- Aspect unitar: un card arată un număr (sau sume, câte o linie pe monedă), o etichetă, o pictogramă și o culoare de accent; cardul cu valoarea zero rămâne colorat, dar estompat, iar cardul activ are contur. Culorile sunt variabilele de temă Odoo, deci cardurile urmează modul luminos și cel întunecat.
- Cifră urmărită în timp: un card poate afișa și variația față de perioada anterioară (`delta`, în procente, verde când crește și roșu când scade, cu `deltaLabel`), o bară de progres spre țintă (`progress`, cu `progressLabel`) și o linie de tendință (`trend`, ultimele valori). Fiecare parte se desenează doar dacă cardul o primește; cardurile fără ele arată ca înainte.
- Clicul este un filtru: `useKpiCardFilters` activează filtrul cardului, scoate filtrele celorlalte carduri (două carduri nu se adună niciodată) și îl dezactivează la al doilea clic. Filtrele proprii ale utilizatorului se păstrează.
- Cardurile împart toată lățimea paginii, fără spațiu gol la capătul rândului.
- Numere mari: de la 100.000 în sus, sumele și numărătorile se afișează în mii sau milioane (1,9M lei, 123,5k), cu formatul compact Odoo; `formatKpiAmount` și `formatKpiCount` sunt disponibile modulelor care construiesc cardurile, iar `title` (tooltip) poate purta valoarea exactă.
- Un card are `key` (și atributul `data-card`), `label`, apoi `count` sau `amounts`, opțional `subtitle`, `title`, `icon` (clasă Font Awesome), opțional `delta`/`deltaLabel`, `progress`/`progressLabel`, `trend`, și `tone`: `info`, `success`, `warning`, `danger`, `purple`, `action` sau `slate` (implicit).
- Convenții de utilizare: filtrele cardurilor stau într-un grup propriu în vizualizarea de căutare, cu `<separator/>` înainte și după; cardul și filtrul lui folosesc același domeniu pe server, astfel încât numărul de pe card este numărul de rânduri deschise la clic.
- Nu adaugă modele, meniuri sau date; nu are nimic de configurat.

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

**Modele**

- Niciun model (modul exclusiv de front-end).

**Vizualizări**

- `KpiCards` (`static/src/kpi_cards/kpi_cards.esm.js` și `.xml`): componentă OWL cu banda de carduri; primește `cards` și `onCardClick`.
- `useKpiCardFilters(filterNames)`: hook care leagă cardurile de filtrele de căutare (`isActive`, `toggle`).
- `formatKpiAmount`, `formatKpiCount`, `formatKpiDelta`, `kpiSparklinePoints`, `KPI_TONES`, `KPI_COMPACT_FROM`: utilitare exportate (`formatKpiDelta` formatează variația ca `+3,5%`; `kpiSparklinePoints` produce atributul `points` al liniei de tendință).

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_customer_analysis](../deltatech_customer_analysis/index.md): tabloul de analiză a clienților folosește cardurile (îl are în `depends`).
- [deltatech_sale_missions](../deltatech_sale_missions/index.md): tabloul de misiuni de vânzare folosește `KpiCards` (dependență indirectă, prin `deltatech_customer_analysis`).
- [deltatech_delivery_dashboard](../deltatech_delivery_dashboard/index.md): tabloul de livrări, de unde au fost extrase cardurile (îl are în `depends`).
- [deltatech_sale_dashboard](../deltatech_sale_dashboard/index.md): tabloul de vânzări (îl are în `depends`).
- [deltatech_dashboard_builder](../deltatech_dashboard_builder/index.md): constructorul de tablouri de bord folosește cardurile (îl are în `depends`).
- [deltatech_advanced_planner](../deltatech_advanced_planner/index.md): tabloul de planificare avansată folosește cardurile (îl are în `depends`).
