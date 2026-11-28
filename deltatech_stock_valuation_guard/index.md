# Stock Valuation Guard

- **Nume Tehnic:** `deltatech_stock_valuation_guard`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech_stock_valuation/tree/20.0/deltatech_stock_valuation_guard
- **Cale Locală:** odoo-addons/deltatech_stock_valuation/deltatech_stock_valuation_guard
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Două verificări care păstrează valorizarea stocului credibilă, fiecare activabilă per companie: o singură metodă de cost pentru toate categoriile de produse și nicio mișcare de stoc fără valoare. Un produs intrat în stoc la valoare zero iese tot la valoare zero, iar costul mărfii vândute al vânzărilor ulterioare devine zero; modulul previne această situație și oferă liste de control pentru depistarea problemelor existente.

#### 2. Funcționalități Cheie

- **One Cost Method** (*Inventar → Configurare → Setări*, secțiunea *Valuation*): o categorie de produse poate folosi doar metoda de cost și valorizarea companiei; crearea sau schimbarea la altă metodă este refuzată.
- Butonul **Align the categories** aduce toate categoriile companiei pe metoda ei. Costurile curente se salvează întâi într-un atașament JSON pe companie, pentru o eventuală revenire țintită; se recomandă rularea mai întâi pe o bază de test.
- **Block Unvalued Moves**: o mișcare de intrare a unui produs stocabil este refuzată dacă valoarea ar fi zero (recepție fără preț, plus de inventar, retur valorizat zero), iar una de ieșire este refuzată dacă produsul nu are cost. La validare apare lista produselor de corectat.
- Se bifează *Block Unvalued Moves* abia după ce produsele vândute au cost.
- **Liste de control** (*Inventar → Rapoarte → Valuation Control*): categorii cu altă metodă de cost, produse stocabile fără cost, stoc valorizat zero (intrări la zero cu cantitate rămasă) și mișcări valorizate zero în ultimele 30 de zile.
- Mișcările validate de procese fără utilizator (comenzile din Punctul de vânzare) sunt tratate de [deltatech_stock_valuation_guard_pos](../deltatech_stock_valuation_guard_pos/index.md).
- Pașii detaliați, cu capturi, sunt în fișa consultantului.

#### 3. Dependențe

- `stock_account`

#### 4. Componente Cheie

**Modele**

- `res.company` (extins): opțiunile `valuation_guard_unique_method` și `valuation_guard_zero_cost`.
- `res.config.settings` (extins): setările din Inventar și acțiunea `action_valuation_guard_align`.
- `product.category` (extins): constrângerea metodei unice și alinierea categoriilor.
- `stock.move` (extins): blocarea mișcărilor fără valoare.
- `stock.valuation.guard` (abstract): acțiunile care deschid listele de control.

**Vizualizări**

- `res_config_settings_view_form`: setările de valorizare și butonul de aliniere.
- `menu_valuation_guard` și submeniurile listelor de control, în *Inventar → Rapoarte*.

**Acțiuni Automate / Acțiuni Server**

- `action_misaligned_categories`: Categories with Another Cost Method.
- `action_products_without_cost`: Storable Products without Cost.
- `action_zero_valued_stock`: Stock Valued at Zero.
- `action_zero_valued_moves`: Moves Valued at Zero.

#### 5. Conexiuni

- [deltatech_stock_valuation_guard_pos](../deltatech_stock_valuation_guard_pos/index.md): mută verificarea la coșul din Punctul de vânzare.
- [deltatech_stock_valuation](../deltatech_stock_valuation/index.md): suita de valorizare a stocului.
