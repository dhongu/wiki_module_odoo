# Marketplace Dashboard (localizat la `deltatech_marketplace_dashboard/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_dashboard`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/20.0/deltatech_marketplace_dashboard
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_dashboard`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Un singur ecran pentru toate marketplace-urile (eMAG, Trendyol, Shopify, PrestaShop etc.), care răspunde, în ordinea importanței de dimineață, la trei întrebări: ce am de făcut acum, cum merg vânzările și dacă se câștigă ceva.

#### 2. Funcționalități Cheie

- Banda de conexiune: starea sincronizării fiecărui backend (erori în ultimele 24 de ore, joburi eșuate, nesincronizat niciodată), backend-uri cu importul comenzilor dezactivat și starea jobului de import.
- Contoare pe pașii listei de lucru (de mapat, de confirmat, de expediat, de predat, plus cele aduse de conectori: de confirmat la eMAG, întârziate, anulare solicitată) și *de încasat* (facturi postate neplătite); click deschide lista comenzilor numărate, pe același domeniu.
- Lista *De făcut*, sortată după termenul de expediere stabilit de marketplace; butoane pe rând pentru pașii pe care conectorul îi poate rula (eMAG: acceptare).
- Vânzări pe zile, produse best-seller și marja brută (vânzări fără TVA - cost de achiziție - comision estimat) pe 7, 30, 90 sau 365 de zile; marja se vede doar utilizatorilor cu drept de a vedea costul produsului.
- Retururi deschise ale marketplace-urilor; sumele în alte valute se convertesc la cursul zilei.
- Meniu: *Marketplace > Dashboard*, pentru grupul *Marketplace Manager*. Comisionul estimat se setează pe backend (*Estimated Commission (%)*), iar parametrul de sistem `deltatech_marketplace_dashboard.worklist_days` (implicit 90) limitează vechimea comenzilor din listă.
- Conectorii pot extinde ecranul prin hook-urile `_dashboard_steps()`, `_dashboard_kpis()`, `_dashboard_row_actions()`, `_dashboard_row_values()`.

#### 3. Dependențe

- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)

#### 4. Componente Cheie

**Modele**

- `marketplace.dashboard` (model abstract): calculează datele ecranului (contoare, listă de lucru, vânzări, marjă, retururi).
- `marketplace.backend` (extins): câmpul de comision estimat pentru calculul marjei.
- `marketplace.sale.order` (extins): hook-urile de dashboard pentru pașii listei de lucru.

**Vizualizări**

- `view_marketplace_backend_form`: adaugă comisionul estimat pe formularul backend-ului.
- `action_marketplace_dashboard` (acțiune client) și meniul `menu_marketplace_dashboard`: componenta OWL a dashboard-ului.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): meniul rădăcină și backend-urile pe care le agregă dashboard-ul.
- [deltatech_marketplace_emag](../deltatech_marketplace_emag/index.md): adaugă pași proprii (de confirmat, întârziate, anulare solicitată).
