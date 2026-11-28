# POS Price Sync (localizat la `deltatech_pos_price_sync/index.md`)

- **Nume Tehnic:** `deltatech_pos_price_sync`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_pos_price_sync
- **Cale Locală:** `odoo-addons/deltatech/deltatech_pos_price_sync`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul trimite imediat modificările de preț ale produselor către sesiunile de Punct de Vânzare deja deschise, astfel încât casierii văd mereu prețul corect, fără reîncărcarea paginii sau redeschiderea sesiunii.

#### 2. Funcționalități Cheie

- Detectează modificările `list_price` / `standard_price` pe produsele disponibile în POS.
- Trimite o notificare live pe bus către fiecare sesiune POS deschisă, cu același model de canal ca `deltatech_pos_stock`.
- Interfața POS integrează prețul nou direct în modelul din memorie, fără reîncărcare.
- Rezolvă situația „am schimbat prețul, dar casierul îl vede pe cel vechi chiar și după F5”: o sesiune rămasă deschisă nu mai rulează sincronizarea bazată pe `write_date` la reîncărcare.

#### 3. Dependențe

- `point_of_sale`

#### 4. Componente Cheie

Sumarul provine din `readme/DESCRIPTION.md`; componentele au fost verificate punctual în cod.

**Modele**

- `product.template` (extins): `write()` detectează schimbarea prețurilor pe produsele `available_in_pos`, iar `_notify_pos_price_change()` trimite evenimentul `PRICE_SYNCHRONISATION` către sesiunile deschise ale companiilor relevante.

**Vizualizări**

- `pos_price_synchronisation.esm.js` (asset POS): se abonează la `PRICE_SYNCHRONISATION` și injectează produsele actualizate în modelele din memorie.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- [deltatech_pos_stock](../deltatech_pos_stock/index.md): același model de canal bus pentru notificări live către POS (fără dependență în manifest).
