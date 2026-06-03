# Stock Auto Transfer (localizat la `deltatech_picking_transit/index.md`)

- **Nume Tehnic:** `deltatech_picking_transit`
- **Versiune:** `19.0.0.0.9`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_picking_transit`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_picking_transit`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul automatizează transferurile interne în doi pași prin intermediul unei locații de tranzit. Pe tipul de operațiune de stoc se poate defini o „operațiune următoare", iar atunci când se efectuează un transfer intern cu un astfel de tip de operațiune, sistemul oferă posibilitatea de a transforma mutarea într-un transfer în doi pași: primul transfer ajunge într-o locație de tranzit, iar al doilea preia mărfurile din tranzit și le duce la destinația finală. Astfel se câștigă trasabilitate și control asupra mărfurilor aflate „în drum" între două locații, fără a bloca posibilitatea de a urmări fiecare etapă separat.

#### 2. Funcționalități Cheie

- Pe formularul tipului de operațiune de stoc se poate adăuga o „operațiune următoare" (next operation).
- La un transfer intern cu un tip de operațiune ce are setată „operațiunea următoare", sistemul oferă, prin butonul „create transfer", opțiunea de a transforma transferul într-unul în doi pași.
- Butonul creează un al doilea transfer, din locația de tranzit către locația selectată în wizard, cu aceleași linii de mutare.
- După crearea celui de-al doilea transfer, liniile de mutare ale transferului inițial nu mai pot fi modificate.
- Opțiune de creare automată a celui de-al doilea transfer, fără a fi nevoie de wizard (din v17.0.0.0.9):
  - Pe tipul de operațiune de stoc apare un checkbox „Auto Second Transfer", vizibil doar dacă „Two Step Transfer Use" este setat pe Delivery.
  - Dacă este bifat, la validarea primului transfer sistemul caută locația de Recepție pe baza partenerului transferului (folosește contactul asociat celui de-al doilea depozit).
  - Dacă pe transfer este setat „Source Document", sistemul **nu** creează automat al doilea transfer.

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

Conform fluxului de ingestie (Readme prezent), analiza detaliată a codului pentru componente este omisă. Structura de fișiere a modulului (din `__manifest__.py`) indică următoarele zone:

**Modele**

- Extinderi în `models/` pentru `stock.picking` și `stock.picking.type` (operațiune următoare, transfer în doi pași, creare automată).

**Vizualizări**

- `views/stock_picking_views.xml`: extinderi ale formularului de transfer (buton „create transfer", blocare linii de mutare).
- `views/stock_picking_type_view.xml`: extinderi ale formularului tipului de operațiune (operațiune următoare, „Auto Second Transfer").
- `wizard/stock_picking_transfer_wizard_views.xml`: wizard-ul pentru crearea celui de-al doilea transfer.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt declarate în fișierele de date din manifest.

#### 5. Conexiuni

- `stock`: modulul extinde direct fluxul de transferuri și tipurile de operațiuni din modulul standard de stoc Odoo.
