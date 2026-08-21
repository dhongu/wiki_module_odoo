# Deltatech POS Price Sync (localizat la `deltatech_pos_price_sync/index.md`)

- **Nume Tehnic:** `deltatech_pos_price_sync`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_pos_price_sync
- **Cale Locală:** `odoo-addons/deltatech/deltatech_pos_price_sync`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul trimite instant modificările de preț ale produselor către sesiunile de Punct de Vânzare (POS) deja deschise, astfel încât casierii să vadă mereu prețul corect fără să fie nevoiți să reîncarce pagina sau să închidă și să redeschidă sesiunea.

#### 2. Funcționalități Cheie

- Detectează modificările câmpurilor `list_price`/`standard_price` pe produsele disponibile în POS.
- Trimite o notificare live prin bus către toate sesiunile POS deschise, reutilizând același model de canal folosit de `deltatech_pos_stock`.
- Interfața POS integrează prețul proaspăt direct în modelul din memorie, fără reîncărcare de pagină.
- Rezolvă problema „am schimbat prețul, dar casierul tot vede prețul vechi chiar și după F5": o sesiune POS rămasă deschisă nu mai rulează sincronizarea bazată pe `write_date` la reîncărcare.

#### 3. Dependențe

- `point_of_sale`

#### 4. Componente Cheie

**Modele**

- `product.template` (extins): suprascrie `write()` pentru a detecta schimbările de `list_price`/`standard_price` pe produsele `available_in_pos` și declanșează `_notify_pos_price_change()`, care caută sesiunile POS cu starea `opened` din companiile relevante și trimite pe bus evenimentul `PRICE_SYNCHRONISATION` cu datele produsului reîncărcate.

**Frontend (assets POS)**

- `pos_price_synchronisation.esm.js`: patch pe `PosStore` — se conectează la websocket-ul `PRICE_SYNCHRONISATION` în `processServerData()` și, la primirea unui eveniment, injectează direct datele noi de produs în modelele POS din memorie (`connectNewData`), fără RPC suplimentar sau reîncărcare.

#### 5. Conexiuni

- `deltatech_pos_stock`: modulul reutilizează același model de canal bus pentru notificări live către sesiunile POS deschise (pattern comun, nu dependență de manifest).
- `point_of_sale`: extinde ciclul de încărcare a datelor POS (`processServerData`) pentru sincronizarea live a prețurilor.
