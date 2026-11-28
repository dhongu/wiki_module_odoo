# Stock Valuation Guard - Point of Sale

- **Nume Tehnic:** `deltatech_stock_valuation_guard_pos`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech_stock_valuation/tree/20.0/deltatech_stock_valuation_guard_pos
- **Cale Locală:** odoo-addons/deltatech_stock_valuation/deltatech_stock_valuation_guard_pos
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Partea de Punct de vânzare a modulului Stock Valuation Guard. Mișcările unei comenzi POS se validează când comanda ajunge pe server, după tipărirea bonului fiscal; refuzarea lor acolo ar bloca comanda în casă. De aceea verificarea este mutată la coșul de cumpărături.

#### 2. Funcționalități Cheie

- Cu *Block Unvalued Moves* bifat pe companie, un produs stocabil fără cost nu poate fi adăugat în comandă: casa afișează mesajul *Product without cost*, iar coșul rămâne neschimbat. Cere managerului să stabilească costul, apoi reîncarcă casa (casele deschise înainte de activare cer reîncărcare).
- Retururile, consumabilele și serviciile nu sunt blocate.
- Mișcările comenzilor POS nu mai sunt verificate pe server.
- Un șablon cu mai multe variante este verificat doar când varianta e dată direct (scanare, card de variantă); la alegerea în configurator, produsul apare în listele de control din Stock Valuation Guard.
- Se instalează automat împreună cu *Stock Valuation Guard* și *Point of Sale*.

#### 3. Dependențe

- [deltatech_stock_valuation_guard](../deltatech_stock_valuation_guard/index.md)
- `pos_stock`

#### 4. Componente Cheie

**Modele**

- `res.company` (extins): trimite opțiunea de blocare către datele încărcate în POS (`_load_pos_data_fields`).
- `stock.move` (extins): `_valuation_guard_skip` omite verificarea pe server pentru comenzile POS.

**Vizualizări**

- `static/src/js/pos_store.esm.js`: extinde magazinul POS pentru a opri produsul fără cost la adăugarea în coș.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_stock_valuation_guard](../deltatech_stock_valuation_guard/index.md): modulul de bază cu opțiunea și listele de control.
- [deltatech_stock_valuation](../deltatech_stock_valuation/index.md): suita de valorizare a stocului.
