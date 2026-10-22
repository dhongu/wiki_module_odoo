# Stock Valuation Guard (localizat la `deltatech_stock_valuation_guard/index.md`)

- **Nume Tehnic:** `deltatech_stock_valuation_guard`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech_stock_valuation/tree/19.0/deltatech_stock_valuation_guard
- **Cale Locală:** `odoo-addons/deltatech_stock_valuation/deltatech_stock_valuation_guard`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Modulul adaugă două verificări care păstrează evaluarea stocului de încredere, fiecare activată separat pe companie. Prima impune o singură metodă de cost (și o singură evaluare, periodică sau perpetuă) pentru toate categoriile de produse ale companiei. A doua refuză mișcările de stoc fără valoare, astfel încât o intrare la valoare zero să nu ducă la un cost al mărfurilor vândute egal cu zero la vânzările următoare. Listele de control din Inventar > Raportare permit curățarea situației existente înainte de activarea blocării.

#### 2. Funcționalități Cheie

- **O singură metodă de cost** (opțiunea *One Cost Method*): o categorie de produse poate folosi doar metoda de cost și evaluarea companiei; crearea sau modificarea unei categorii către altă metodă este refuzată.
- **Aliniere categorii** (butonul *Align the categories*): aduce toate categoriile companiei pe metoda ei dintr-un singur pas. Pentru că Odoo recalculează costul produselor din categoriile modificate, costurile curente se salvează înainte într-un atașament JSON pe companie, pentru o eventuală revenire țintită. Se recomandă rularea mai întâi pe o bază de test.
- **Blocarea mișcărilor fără valoare** (opțiunea *Block Unvalued Moves*):
  - o intrare a unui produs stocabil este refuzată dacă valoarea ar fi zero (recepție fără preț, plus la inventar sau actualizare de cantitate la produs fără cost, retur evaluat la zero);
  - o ieșire este refuzată dacă produsul nu are cost;
  - la validare, utilizatorul vede lista produselor de corectat; setează costul produsului sau prețul din comanda de achiziție și validează din nou.
- **Liste de control** (*Inventory > Reporting > Valuation Control*):
  - categorii cu altă metodă de cost decât compania;
  - produse stocabile fără cost;
  - stoc evaluat la zero (intrări la valoare zero cu cantitate rămasă în stoc, pe care vânzările următoare le scot la cost zero);
  - mișcări evaluate la zero în ultimele 30 de zile.
- **Configurare** în *Inventory > Configuration > Settings*, secțiunea *Valuation*. Recomandare: înainte de activarea blocării, se completează costul produselor încă vândute din lista *Storable Products without Cost*.
- Reevaluarea stocului deja intrat la zero este o decizie contabilă (ce cost, ce notă contabilă); lista doar arată ce este afectat.
- Modulul blochează mișcările validate de utilizatori. Mișcările validate de procese neconduse de utilizator, precum comenzile din Punctul de Vânzare, sunt tratate de `deltatech_stock_valuation_guard_pos`, care oprește produsul la coș.

#### 3. Dependențe

- `stock_account`

#### 4. Componente Cheie

**Modele**

- `stock.valuation.guard` (abstract): furnizează acțiunile listelor de control (categorii nealiniate, produse fără cost, stoc la zero, mișcări la zero).
- `product.category` (extins): verifică metoda de cost la create/write și oferă alinierea categoriilor cu salvarea prealabilă a costurilor.
- `stock.move` (extins): `_action_done` verifică mișcările fără valoare și refuză validarea.
- `res.company` (extins): opțiunile de pornire/oprire ale verificărilor.
- `res.config.settings` (extins): opțiunile din Setări și butonul de aliniere.

**Vizualizări**

- `views/res_config_settings_views.xml`: secțiunea de setări *Valuation* cu opțiunile și butonul de aliniere.
- `views/menu_views.xml`: meniul *Valuation Control* sub Inventory > Reporting.

**Acțiuni Automate / Acțiuni Server**

- `action_misaligned_categories`, `action_products_without_cost`, `action_zero_valued_stock`, `action_zero_valued_moves`: acțiuni server care deschid cele patru liste de control.

#### 5. Conexiuni

- [deltatech_stock_valuation_guard_pos](../deltatech_stock_valuation_guard_pos/index.md): extensie pentru Punctul de Vânzare, care oprește produsul fără valoare la coș.
- [deltatech_stock_valuation](../deltatech_stock_valuation/index.md): același domeniu (evaluarea stocului), din aceeași suită.
