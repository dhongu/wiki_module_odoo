# Purchase Targets by Manufacturer (Ținte de achiziții pe producători)

- **Nume Tehnic:** `deltatech_purchase_target`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_purchase_target
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_target`
- **Ultima Ingestie:** `2026-10-30`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă ținte de achiziții pe producător și arată, în timp real, din facturile de furnizor postate, cât din țintă a fost realizat, atât total, cât și pe categorii de eCommerce, pe trimestru și cumulat de la începutul anului. Răspunde la întrebarea „cum stăm cu acordurile comerciale ale producătorilor?": ce producător sau categorie mai are nevoie de achiziții pentru a atinge bonusul de volum și dacă vânzările pe aceleași produse țin pasul cu achizițiile.

#### 2. Funcționalități Cheie

- **Ținte pe producător**: o țintă pe producător și an, exprimată ca valoare (fără TVA, în moneda companiei) sau cantitate, defalcată pe trimestru și pe categorie eCommerce (meniu *Achiziții › Produse › Manufacturer Targets*).
- **Linii de țintă**: pe fila *Targets*, o linie per trimestru; fără categorie = ținta generală, cu categorie = ținta categoriei respective (categoriile copil sunt incluse).
- **Contează doar facturile producătorului**: implicit furnizorul este chiar producătorul, facturile revânzătorilor sunt excluse; în câmpul *Vendors* se pot adăuga și alte firme ale producătorului.
- **Realizat vs. Țintă** (*Achiziții › Raportare*): realizat în trimestru și cumulat, procent realizat, rest până la țintă și vânzările pe aceleași produse, cu detaliere către liniile de factură și către raportul de marjă la vânzare.
- **Reguli de calcul**: realizat = facturi de furnizor postate minus note de credit, fără TVA, după data contabilă; un produs din două categorii eCommerce se numără în fiecare țintă de categorie, dar o singură dată în ținta generală; la ținte pe cantitate, liniile în altă unitate de măsură sunt convertite în unitatea produsului.
- **Comparație costuri furnizori** (*Achiziții › Raportare*): prețul mediu de achiziție al fiecărui produs, pe furnizor, din facturile de furnizor.
- **Producător în analiza achizițiilor**: căutare și grupare a comenzilor de achiziție după producător.
- **Drepturi**: utilizatorii de achiziții văd țintele și raportul, managerii de achiziții definesc țintele; detalierea vânzărilor cere drepturile raportului de marjă la vânzare.
- **Pregătire date**: bifa *Is manufacturer* pe partenerii producători, câmpul *Manufacturer* pe produse și produse încadrate în categoriile eCommerce folosite de ținte. Pașii detaliați sunt în fișa consultantului.

#### 3. Dependențe

- `purchase`
- `website_sale`
- [deltatech_product_extension](../deltatech_product_extension/index.md)
- [deltatech_sale_margin](../deltatech_sale_margin/index.md)

#### 4. Componente Cheie

**Modele**

- `purchase.target`: ținta unui producător pe un an (tip: valoare sau cantitate, companie, furnizori luați în calcul, linii, notă).
- `purchase.target.line`: linia de țintă (trimestru, categorie eCommerce opțională, valoare țintă) cu câmpuri calculate: realizat, realizat cumulat, țintă cumulată, procent, rest și vânzări (acestea din urmă restricționate la grupurile de marjă/vânzări).
- `purchase.report` (extins): adaugă câmpul `manufacturer_id` (Producător) pentru căutare și grupare.
- `account.move.line` (vizualizări dedicate): folosit la detalierea liniilor de factură și la comparația costurilor pe furnizor.

**Vizualizări**

- `view_purchase_target_list` / `view_purchase_target_form` / `view_purchase_target_search`: definirea țintelor pe producător.
- `view_purchase_target_line_list` / `view_purchase_target_line_search`: raportul Realizat vs. Țintă.
- `view_move_line_purchase_target_list` / `view_move_line_purchase_target_search`: liniile de factură din spatele realizatului și comparația costurilor.
- `view_purchase_order_search`: filtrare/grupare după producător în analiza achizițiilor.
- Acțiuni: `action_purchase_target`, `action_purchase_target_line` (Achieved vs Target), `action_vendor_cost_compare` (Vendor Cost Comparison).

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_product_extension](../deltatech_product_extension/index.md): furnizează câmpul Manufacturer pe produs și indicatorul de producător pe partener.
- [deltatech_sale_margin](../deltatech_sale_margin/index.md): raportul de marjă la vânzare, deschis din detalierea vânzărilor.
