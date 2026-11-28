# Romania - Stock Base

- **Nume Tehnic:** `l10n_ro_stock_base`
- **Versiune:** `20.0.0.0.2`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_stock_base
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_stock_base`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Pune la dispoziție locațiile și operațiunile de stoc necesare pentru consumul intern și darea în folosință, plus greutatea netă a produselor. Este înlocuitorul Terrabit al modulului OCA `l10n_ro_stock`, scris fără dependență de `l10n_ro_config`. Numele câmpurilor sunt cele din modulul OCA, deci o bază de date care îl avea instalat își păstrează datele la trecerea pe acest modul.

#### 2. Funcționalități Cheie

- Tipuri de locație noi, **Dare în folosință** și **Consum**: mișcările din/către ele se consideră intrări, respectiv ieșiri, la evaluarea stocului.
- Fiecare companie cu țara fiscală România primește o locație de consum și una de dare în folosință (`l10n_ro_consume_location_id`, `l10n_ro_usage_location_id`), create la instalare pentru companiile existente și la creare pentru cele noi; locațiile existente sunt refolosite.
- Fiecare depozit al unei astfel de companii primește tipurile de operațiune **Consum** și **Dare în folosință**, cu secvențe proprii (`<cod depozit>/CONS/`, `<cod depozit>/USAGE/`); redenumirea depozitului sau schimbarea codului redenumește și secvențele.
- Transferul de tip Consum se creează din *Inventar → Prezentare generală*; ieșirea se validează ca transfer intern către locația de consum, iar returul revine în aceeași secvență, dacă tipul de retur nu e setat altfel.
- **Greutate netă** (`l10n_ro_net_weight`) pe produs, în fila Inventar, în aceeași unitate ca greutatea.
- Pentru a vedea meniul de locații este nevoie de setarea **Locații de stocare**; fluxul pas cu pas este în fișa consultantului.

#### 3. Dependențe

- `account`
- `stock`

#### 4. Componente Cheie

**Modele**

- `stock.location`: extinde tipurile de locație cu Consum și Dare în folosință.
- `stock.warehouse`: câmpurile `l10n_ro_consume_type_id` și `l10n_ro_usage_type_id`, creează tipurile de operațiune și secvențele.
- `res.company`: locațiile implicite de consum și dare în folosință.
- `product.template` / `product.product`: `l10n_ro_net_weight`.
- `stock.move`: extins pentru tratarea locațiilor de consum/folosință la evaluare.

**Vizualizări**

- `view_warehouse_l10n_ro_stock_base`: tipurile de operațiune românești pe formularul depozitului.
- `l10n_ro_stock_base_product_template_form`: greutatea netă pe formularul produsului.

**Acțiuni Automate / Acțiuni Server**

- Nu are cron-uri sau acțiuni server; `post_init_hook` creează locațiile și tipurile de operațiune pentru companiile existente (datele sunt în `data/stock_data.xml`).

#### 5. Conexiuni

- [l10n_ro_stock_account_base](../l10n_ro_stock_account_base/index.md): construiește peste aceste locații și operațiuni evaluarea de stoc românească.
- `l10n_ro_stock_account`: motorul de evaluare care tratează consumul și darea în folosință ca ieșiri/intrări.
