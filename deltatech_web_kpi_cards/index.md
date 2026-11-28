# Carduri KPI

- **Nume Tehnic:** `deltatech_web_kpi_cards`
- **Versiune:** `20.0.1.2.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_web_kpi_cards
- **Cale Locală:** odoo-addons/deltatech/deltatech_web_kpi_cards
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modul tehnic care oferă o bandă de carduri KPI pe care alte module o plasează deasupra vizualizărilor din backend, plus legătura care face ca un clic pe card să activeze filtrul de căutare corespunzător. Nu adaugă modele, meniuri sau date și se instalează doar ca dependență a modulelor care afișează carduri.

#### 2. Funcționalități Cheie

- Aspect unitar pentru toate tablourile de bord: card cu număr (sau sume, câte o linie per monedă), etichetă, pictogramă și culoare de accent; cardul la zero rămâne colorat, estompat, iar cardul activ are contur. Culorile sunt variabilele temei Odoo, deci urmează modul luminos și întunecat.
- Evoluția în timp: variația față de perioada anterioară (verde în sus, roșu în jos), bară de progres către o țintă și linie de tendință, desenate doar dacă cardul le furnizează.
- Clicul este filtru: `useKpiCardFilters` activează filtrul cardului, elimină filtrele celorlalte carduri (două carduri nu se adună) și îl șterge la al doilea clic; filtrele proprii ale utilizatorului rămân.
- Pentru dezvoltatori: se adaugă modulul în `depends` și se folosește componenta `KpiCards` dintr-un component OWL; cardul are `key`, `label`, `count` sau `amounts`, opțional `subtitle`, `title`, `icon` și `tone` (`info`, `success`, `warning`, `danger`, `purple`, `action`, `slate`).
- Filtrele cardurilor se țin într-un grup separat în vizualizarea de căutare, cu `<separator/>` înainte și după; cardul și filtrul său trebuie să aibă același domeniu pe server.

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

**Modele**

- Niciunul (modul exclusiv JavaScript).

**Vizualizări**

- Componenta OWL `KpiCards` și hook-ul `useKpiCardFilters` (`static/src/kpi_cards/`), încărcate în `web.assets_backend`.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- Niciuna verificată în cod; se instalează ca dependență a modulelor care afișează carduri.
