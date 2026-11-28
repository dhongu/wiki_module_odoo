# Vizualizator Linii Listă de Prețuri (localizat la `deltatech_pricelist_line_viewer/index.md`)

- **Nume Tehnic:** `deltatech_pricelist_line_viewer`
- **Versiune:** `20.0.0.0.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_pricelist_line_viewer
- **Cale Locală:** `odoo-addons/deltatech/deltatech_pricelist_line_viewer`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă pe formularul listei de prețuri butonul **Pricelist Lines**, care deschide toate regulile listei într-o vizualizare de tip listă pe tot ecranul, cu căutare, filtre și grupare standard. Listele mari devin mult mai ușor de verificat și de întreținut decât în fila **Sales Prices**.

#### 2. Funcționalități Cheie

- Butonul **Pricelist Lines** deschide doar regulile listei curente (coloane: Pricelist, Products, Min. Quantity, Price, Start Date, End Date; opțional Currency, Based on, Apply On). Coloana **Price** descrie regula, de exemplu „20 % discount”.
- Căutare după **Product**, **Category**, **Pricelist** și **Currency**; regulile noi create din listă primesc implicit lista curentă.
- Datele de început și de sfârșit includ ora: pentru a acoperi ultima zi întreagă, setați ora de sfârșit la 23:59.
- Grupul **Permit pricelist editing** dă drepturi de citire, scriere, creare și ștergere pe liste de prețuri și reguli, fără a fi Administrator Vânzări.
- Prerechizit: activarea opțiunii **Pricelists** în *Vânzări > Configurare > Setări*, secțiunea **Pricing**.
- Fluxul pas cu pas, cu capturi, este în fișa consultantului.

#### 3. Dependențe

- `sale_management`
- `product`

#### 4. Componente Cheie

**Modele**

- `product.pricelist`: extins pentru acțiunea butonului către regulile listei.

**Vizualizări**

- `views/product_pricelist_view.xml`: butonul **Pricelist Lines** pe formularul listei de prețuri și lista regulilor.

**Acțiuni Automate / Acțiuni Server**

- `data/security_groups.xml`: grupul **Permit pricelist editing** (acordat implicit utilizatorilor `base.user_root` și `base.user_admin`); drepturile sunt în `security/ir.access.csv`.

#### 5. Conexiuni

- [deltatech_pricelist](../deltatech_pricelist/index.md): modul pe aceeași zonă, listele de prețuri, fără dependență declarată.
