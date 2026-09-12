# Romania - Fișă de magazie pe gestiuni (localizat la `l10n_ro_stock_sheet_gestiune/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_sheet_gestiune`
- **Versiune:** `19.0.1.0.0`
- **Cale:** `https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_stock_sheet_gestiune`
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_sheet_gestiune`
- **Ultima Ingestie:** `2026-09-12`

#### 1. Sumar

Modulul este puntea dintre **Fișa de magazie / Balanța stocurilor** (`l10n_ro_stock_sheet`) și **gestiunile contabile de stoc** (`l10n_ro_stock_gestiune`): permite filtrarea raportului pe una sau mai multe gestiuni, exact cum cere practica românească — fișa de magazie (cod 14-3-8) se ține **per gestiune**, cu gestionar responsabil. Se instalează automat (`auto_install`) de îndată ce ambele module de bază sunt prezente în baza de date.

#### 2. Funcționalități Cheie

- **Buton „Fișă de magazie" pe gestiune** — din fișa gestiunii (`l10n.ro.gestiune`, meniul Inventar → Configurare → Gestiuni contabile) se deschide raportul pre-filtrat pe locațiile interne ale gestiunii, desfășurat complet (cont de stoc → produs → mișcări), cu solduri inițiale, intrări, ieșiri și sold final.
- **Filtru pe gestiune în raport** — opțiunea `l10n_ro_gestiune_ids` din raportul de bază se traduce automat în mulțimea locațiilor interne ale gestiunilor selectate.
- **Prioritate la selecția manuală** — o selecție explicită de locații (`l10n_ro_location_ids`) are prioritate față de gestiuni.
- **Semantică sigură** — o gestiune fără locații produce un raport gol (nu tot stocul companiei), evitând interpretări greșite la inventariere sau predare-primire gestiune.

#### 3. Dependențe

- [l10n_ro_stock_sheet](../l10n_ro_stock_sheet/index.md)
- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.gestiune` (extins): adaugă acțiunea `action_l10n_ro_stock_sheet`, care deschide raportul `l10n_ro_stock_sheet.action_l10n_ro_stock_sheet` pre-filtrat pe gestiunea curentă (`l10n_ro_gestiune_ids`), complet desfășurat (`unfold_all: True`).
- `l10n.ro.stock.sheet.report.handler` (extins): în `_custom_options_initializer`, traduce lista de gestiuni selectate în locațiile interne asociate (`stock.location` cu `usage=internal` și `l10n_ro_gestiune_id` în selecție); dacă gestiunea nu are locații, forțează un rezultat gol (`[0]`) în loc să cadă pe tot stocul companiei.

**Vizualizări**

- `view_l10n_ro_gestiune_form_stock_sheet`: moștenește formularul gestiunii (`l10n_ro_stock_gestiune.view_l10n_ro_gestiune_form`) și adaugă în antet butonul „Fișă de magazie" (`action_l10n_ro_stock_sheet`).

#### 5. Conexiuni

- [l10n_ro_stock_sheet](../l10n_ro_stock_sheet/index.md): raportul de bază (fișă de magazie 14-3-8 și balanță analitică) pe care acest modul îl extinde cu dimensiunea gestiune.
- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md): sursa gestiunilor contabile de stoc (FR-54) și a legăturii lor cu locațiile interne, folosită pentru filtrare.
