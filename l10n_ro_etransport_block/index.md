# Romania - e-Transport Block (localizat la `l10n_ro_etransport_block/index.md`)

- **Nume Tehnic:** `l10n_ro_etransport_block`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_etransport_block
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_etransport_block`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

## 1. Sumar

Extinde modulul `l10n_ro_edi_stock` pentru a bloca validarea avizelor care conțin produse cu risc fiscal ridicat până la confirmarea UIT-ului de către ANAF, și pentru a actualiza automat statusul UIT printr-un job programat. Asigură astfel conformitatea cu reglementările e-Transport pentru categoriile de mărfuri cu risc fiscal ridicat.

## 2. Funcționalități Cheie

- **Blocare hard la validare:** câmpul „Risc fiscal ridicat" pe fișa produsului; dacă avizul conține cel puțin un astfel de produs, validarea (`button_validate`) este blocată până când UIT-ul intră în starea „Validat" (`stock_validated`).
- **Categorii cu risc fiscal ridicat** conform ANAF: combustibili, tutun, alcool, metale prețioase, produse electrocasnice, echipamente IT etc.
- **Actualizare automată status UIT:** job programat (la fiecare 30 de minute) care interoghează ANAF pentru avizele cu UIT în așteptare (`stock_sent`) și actualizează starea, eliminând actualizarea manuală.

## 3. Dependențe

- `l10n_ro_edi_stock`
- `purchase`
- `sale`

## 4. Componente Cheie

### Modele

- `product.template`: extins cu câmpul „Risc fiscal ridicat".
- `stock.picking`: extins cu blocarea validării în funcție de starea UIT.
- `purchase.order` / `sale.order`: extinse pentru afișarea informațiilor de risc fiscal/UIT.

### Vizualizări / Date

- `views/product_template_view.xml`: câmpul de risc fiscal pe produs.
- `views/stock_picking_view.xml`, `views/purchase_order_view.xml`, `views/sale_order_view.xml`: interfețele extinse.
- `data/ir_cron.xml`: jobul programat de actualizare a statusului UIT.

### Acțiuni Automate / Acțiuni Server

- Cron (la fiecare 30 de minute): interoghează ANAF pentru avizele cu UIT în starea `stock_sent` și actualizează starea în Odoo.

## 5. Conexiuni

- `[[l10n_ro_efactura_b2c]]`
- `[[l10n_ro_efactura_dedup]]`
