# Romania - Fișă de magazie pe gestiuni (localizat la `l10n_ro_stock_sheet_gestiune/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_sheet_gestiune`
- **Versiune:** `19.0.1.0.6`
- **Cale:** `https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_stock_sheet_gestiune`
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_sheet_gestiune`
- **Ultima Ingestie:** `2026-11-11`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul este puntea dintre **Fișa de magazie / Balanța stocurilor** (`l10n_ro_stock_sheet`) și **gestiunile contabile de stoc** (`l10n_ro_stock_gestiune`): permite filtrarea raportului pe una sau mai multe gestiuni, exact cum cere practica românească — fișa de magazie (cod 14-3-8) se ține **per gestiune**, cu gestionar responsabil. Se instalează automat (`auto_install`) de îndată ce ambele module de bază sunt prezente în baza de date.

#### 2. Funcționalități Cheie

- **Buton „Fișă de magazie" pe gestiune** — din fișa gestiunii (`l10n.ro.gestiune`, meniul Inventar → Configurare → Gestiuni contabile) se deschide raportul pre-filtrat pe locațiile interne ale gestiunii, desfășurat complet (cont de stoc → produs → mișcări), cu solduri inițiale, intrări, ieșiri și sold final.
- **Filtru pe gestiune în raport** — opțiunea `l10n_ro_gestiune_ids` din raportul de bază se traduce automat în mulțimea locațiilor interne ale gestiunilor selectate.
- **Prioritate la selecția manuală** — o selecție explicită de locații (`l10n_ro_location_ids`) are prioritate față de gestiuni.
- **Semantică sigură** — o gestiune fără locații produce un raport gol (nu tot stocul companiei), evitând interpretări greșite la inventariere sau predare-primire gestiune.
- **Transferul valoric între gestiuni intră în balanță (19.0.1.0.2)** — mișcările internă → internă (predare-primire gestiune) sunt ignorate de raportul de bază, pentru că nu sunt nici intrări nici ieșiri pentru companie și `stock_move.value` e 0 pe ele. Modulul reintroduce câte un rând de ieșire pe gestiunea sursă și unul de intrare pe gestiunea destinație, cu contul și valoarea preluate din nota de transfer contabilă (`l10n_ro_transfer_move_id`, ex. 371.A → 371.B, eventual prin contul de tranzit 371.T). Astfel, pe conturile gestiunilor *Diferența* iese 0 (nu ± valoarea transferului nereflectat), iar filtrarea raportului pe o singură gestiune arată corect valoarea transferului, inclusiv marfa pe drum pe contul de tranzit al locației de tranzit.
- **Filtrul „Warehouse account” / „Cont gestiune” (19.0.1.0.6)** — mișcările fără notă contabilă pe mișcare (istoric din stiva OCA, recepții sau livrări fără notă) apar pe **contul de stoc al gestiunii** locației lor interne (`l10n_ro_account_stock_id`), nu pe contul categoriei produsului. Mișcările cu notă își păstrează contul din notă; o gestiune fără cont, sau o locație fără gestiune, rămâne pe contul categoriei. Butonul din bara de filtre (opțiunea `l10n_ro_gestiune_account_fallback`) este activ implicit; dacă îl oprești, coloana *Diferența* (sold stoc minus balanța sintetică din contabilitate) arată decalajul — pozitiv pe contul categoriei, negativ pe contul gestiunii — iar totalul rămâne 0. Nu se scrie nimic pe mișcare sau în contabilitate; contul gestiunii se citește din locație la deschiderea raportului.

#### 3. Dependențe

- [l10n_ro_stock_sheet](../l10n_ro_stock_sheet/index.md)
- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.gestiune` (extins): adaugă acțiunea `action_l10n_ro_stock_sheet`, care deschide raportul `l10n_ro_stock_sheet.action_l10n_ro_stock_sheet` pre-filtrat pe gestiunea curentă (`l10n_ro_gestiune_ids`), complet desfășurat (`unfold_all: True`).
- `l10n.ro.stock.sheet.report.handler` (extins): în `_custom_options_initializer`, traduce lista de gestiuni selectate în locațiile interne asociate (`stock.location` cu `usage=internal` și `l10n_ro_gestiune_id` în selecție); dacă gestiunea nu are locații, forțează un rezultat gol (`[0]`) în loc să cadă pe tot stocul companiei. În `_custom_options_initializer` setează și `l10n_ro_gestiune_account_fallback` (implicit `True`, preluat din opțiunile anterioare). În `_moves_cte`, scoate din CTE-ul de bază mișcările care au notă de transfer (`l10n_ro_transfer_move_id`) și le reintroduce printr-un `UNION ALL`: câte un rând pe fiecare linie de stoc (clasa 3) a notei de transfer, cu creditul ca ieșire din locația sursă și debitul ca intrare în locația destinație, respectând filtrele de locație/produs/companie ale raportului; tot aici, mișcările fără notă iau contul de stoc al gestiunii locației când opțiunea de fallback e activă.

**Vizualizări**

- `static/src/stock_sheet_filters.xml` (asset `web.assets_backend`): adaugă în bara de filtre a raportului butonul „Warehouse account” (`l10n_ro_gestiune_account_fallback`).
- `view_l10n_ro_gestiune_form_stock_sheet`: moștenește formularul gestiunii (`l10n_ro_stock_gestiune.view_l10n_ro_gestiune_form`) și adaugă în antet butonul „Fișă de magazie" (`action_l10n_ro_stock_sheet`).

#### 5. Conexiuni

- [l10n_ro_stock_sheet](../l10n_ro_stock_sheet/index.md): raportul de bază (fișă de magazie 14-3-8 și balanță analitică) pe care acest modul îl extinde cu dimensiunea gestiune și cu transferul valoric între gestiuni.
- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md): sursa gestiunilor contabile de stoc (FR-54), a legăturii lor cu locațiile interne și a notei de transfer contabile (`l10n_ro_transfer_move_id`) folosite pentru filtrare și pentru rândurile de transfer.
