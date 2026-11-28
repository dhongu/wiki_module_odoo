# Internal Category Groups (localizat la `deltatech_category_group/index.md`)

- **Nume Tehnic:** `deltatech_category_group`
- **Versiune:** `20.0.0.0.7`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_category_group
- **Cale Locală:** `odoo-addons/deltatech/deltatech_category_group`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul adaugă două elemente suplimentare de grupare pentru categoriile interne de produse: „Tipul categoriei" și „Clasa categoriei". Aceste niveluri permit segmentarea produselor mai fin decât oferă ierarhia standard a categoriilor. Valoarea principală este în raportare: utilizatorul poate analiza marja de vânzare, stocurile și facturile grupate după aceste două criterii, fără a modifica structura existentă a categoriilor.

#### 2. Funcționalități Cheie

- Câmpurile „Tipul categoriei" și „Clasa categoriei" pe fiecare categorie de produs, ca relații many2one către liste de configurare dedicate.
- Liste configurabile de tipuri și clase, cu secvență (ordonare prin tragere), gestionate din *Inventory > Configuration > Category options*.
- Filtre de căutare și grupare după tip și clasă în raportul de marjă de vânzare (din `deltatech_sale_commission`).
- Filtre de căutare și grupare după tip și clasă în analiza stocurilor (*Inventory > Reporting > Inventory*, stock quant).
- Filtre de căutare și grupare după tip și clasă în raportul de facturi (*Accounting > Reporting > Invoice Analysis*).
- Accesul la listele de configurare este controlat de grupul de securitate „Manage category groups", atribuit implicit administratorului; alți utilizatori se adaugă din *Settings > Users & Companies > Groups*.

#### 3. Dependențe

- [deltatech_sale_commission](../deltatech_sale_commission/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunea Componente Cheie este omisă deoarece `readme/DESCRIPTION.md` este prezent și acoperă Sumarul și Funcționalitățile Cheie, fără a solicita explicit analiza codului.

#### 5. Conexiuni

- [deltatech_sale_margin](../deltatech_sale_margin/index.md): raportul de marjă de vânzare primește gruparea după tipul și clasa categoriei.
- `stock`: extinde analiza stocurilor (`stock.quant`) cu cele două criterii de grupare.
- `account`: extinde raportul de facturi (`account.invoice.report`) cu cele două criterii de grupare.
