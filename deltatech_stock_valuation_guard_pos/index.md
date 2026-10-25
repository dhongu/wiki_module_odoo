# Stock Valuation Guard - Point of Sale

- **Nume Tehnic:** `deltatech_stock_valuation_guard_pos`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech_stock_valuation/tree/19.0/deltatech_stock_valuation_guard_pos
- **Cale Locală:** `odoo-addons/deltatech_stock_valuation/deltatech_stock_valuation_guard_pos`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Partea de Punct de Vânzare (POS) a modulului *Stock Valuation Guard*. Mișcările de stoc ale unei comenzi POS se validează abia când comanda ajunge pe server, după ce bonul fiscal a fost deja tipărit, iar refuzul de acolo ar lăsa comanda blocată în casă. De aceea verificarea costului este mutată în coșul casei: un produs fără cost nu mai poate fi adăugat în comandă, astfel încât stocul să nu rămână fără valoare.

#### 2. Funcționalități Cheie

- Cu opțiunea *Block Unvalued Moves* bifată pe companie, un produs stocabil fără cost nu poate fi adăugat într-o comandă POS; casa afișează un mesaj („Product without cost”) care cere stabilirea costului produsului.
- Rambursările (preset de tip retur) și cantitățile negative sau zero nu sunt blocate.
- Mișcările comenzilor POS nu mai sunt verificate a doua oară pe server (sunt excluse din verificarea modulului de bază).
- Un șablon de produs cu mai multe variante este verificat doar când varianta e dată direct (scanare, card de variantă); dacă varianta se alege în configurator, produsul apare în schimb în listele de control din *Stock Valuation Guard*.
- Se instalează automat când sunt prezente *Stock Valuation Guard* și *Point of Sale*.

#### 3. Dependențe

- [deltatech_stock_valuation_guard](../deltatech_stock_valuation_guard/index.md)
- `point_of_sale`

#### 4. Componente Cheie

**Modele**

- `res.company`: încarcă în datele POS câmpul `valuation_guard_zero_cost` (opțiunea de blocare), pentru ca interfața casei să îl cunoască.
- `stock.move`: suprascrie `_valuation_guard_skip` astfel încât mișcările legate de o comandă sau o sesiune POS să fie omise de verificarea pe server.

**Vizualizări**

- Fără vizualizări XML; modulul adaugă doar cod JS pentru casa POS.
- `static/src/js/pos_store.esm.js`: patch pe `PosStore.addLineToOrder`, care afișează dialogul de alertă și oprește adăugarea liniei pentru produsele stocabile fără cost.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [deltatech_stock_valuation_guard](../deltatech_stock_valuation_guard/index.md): modulul de bază, care deține opțiunea *Block Unvalued Moves* și verificarea pe mișcările de stoc.
- `point_of_sale`: casa în care este aplicată verificarea.
