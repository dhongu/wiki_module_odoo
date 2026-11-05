# Vizualizator Linii Listă de Prețuri (localizat la `deltatech_pricelist_line_viewer/index.md`)

- **Nume Tehnic:** `deltatech_pricelist_line_viewer`
- **Versiune:** `19.0.0.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_pricelist_line_viewer
- **Cale Locală:** `odoo-addons/deltatech/deltatech_pricelist_line_viewer`
- **Ultima Ingestie:** `2026-11-05`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă pe formularul listei de prețuri un buton care deschide toate regulile listei într-o vizualizare de tip listă pe tot ecranul, cu căutare, filtre și grupare standard. Astfel listele de prețuri mari se verifică și se întrețin mult mai ușor decât din fila *Sales Prices* a formularului. În plus, un grup dedicat permite unor utilizatori să gestioneze prețurile fără a fi Administrator Vânzări.

#### 2. Funcționalități Cheie

- **Butonul Pricelist Lines** pe formularul listei de prețuri: deschide doar regulile listei curente, cu coloanele Pricelist, Products, Min. Quantity, Price, Start Date, End Date și, opțional, Currency, Based on și Apply On.
- **Căutare** după **Product**, **Category**, **Pricelist** și **Currency** (aceasta din urmă când există mai multe monede active), plus gruparea standard.
- **Reguli noi din listă**: butonul **New** creează o regulă deja legată de lista de prețuri curentă.
- **Grupul Permit pricelist editing**: acordă drepturi de citire, scriere, creare și ștergere pe listele de prețuri și pe regulile lor, fără rolul de Administrator Vânzări. Se atribuie din *Settings > Users & Companies > Groups* (în modul developer) sau din fișa utilizatorului, fila *Access Rights*, secțiunea *Extra Rights*.
- **Pregătire**: listele de prețuri trebuie activate în *Sales > Configuration > Settings*, secțiunea **Pricing**, opțiunea **Pricelists**; lista se deschide din *Sales > Products > Pricelists*.
- **Detalii de utilizare**: coloana **Price** arată doar prețul fix; pentru regulile de tip *Discount* sau *Formula* prețul se vede deschizând regula. La regulile pe categorie sau pe toate produsele coloana **Products** e goală, iar coloana opțională **Apply On** clarifică tipul. Datele de început și de sfârșit includ ora, deci ora de sfârșit se setează la 23:59 pentru ca regula să se aplice în toată ultima zi.
- Fluxul pas cu pas, cu capturi, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `sale_management`
- `product`

#### 4. Componente Cheie

Sumarul și Funcționalitățile Cheie provin din `readme/DESCRIPTION.md` și `readme/USAGE.md`; conform fluxului de ingestie, analiza detaliată a codului este omisă. Din structura modulului:

**Modele**

- `product.pricelist` (extins în `models/product_pricelist.py`): acțiunea butonului către regulile listei.

**Vizualizări**

- `views/product_pricelist_view.xml`: extinde formularul listei de prețuri cu butonul de acces către vizualizarea de tip listă a regulilor.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite. `data/security_groups.xml` declară grupul **Permit pricelist editing** (nu e o acțiune automată).

#### 5. Conexiuni

- Nicio conexiune suplimentară documentată în afara dependențelor declarate.
