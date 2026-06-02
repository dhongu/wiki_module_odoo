# Deltatech Category Group (localizat la `deltatech_category_group/index.md`)

- **Nume Tehnic:** `deltatech_category_group`
- **Versiune:** `19.0.0.0.3`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_category_group`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_category_group`
- **Ultima Ingestie:** `2026-06-02`

#### 1. Sumar

Modulul adaugă două elemente suplimentare de grupare pentru categoriile interne de produse: „Tipul categoriei" și „Clasa categoriei". Aceste niveluri suplimentare permit organizarea produselor în structuri mai detaliate decât oferă categoria internă standard, oferind o vedere mai clară asupra portofoliului de produse. Valoarea principală este în raportare: utilizatorul poate analiza marja de vânzare, stocurile și facturile grupate după aceste două noi criterii, fără a fi nevoit să modifice structura existentă a categoriilor.

#### 2. Funcționalități Cheie

- Adaugă două elemente de grupare pentru categoriile interne: „Tipul categoriei" (Category type) și „Clasa categoriei" (Category class).
- Permite gruparea după aceste două elemente în raportul de marjă de vânzare (Sale margin report).
- Permite gruparea după aceste două elemente în analiza stocurilor (Stock quant).
- Permite gruparea după aceste două elemente în raportul de facturi (Account invoice report).

#### 3. Dependențe

- [deltatech_sale_commission](../deltatech_sale_commission/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunea Componente Cheie este omisă deoarece fișierul `readme/DESCRIPTION.md` este prezent și acoperă Sumarul și Funcționalitățile Cheie, fără a solicita explicit analiza codului.

#### 5. Conexiuni

- [deltatech_sale_margin](../deltatech_sale_margin/index.md): modulul extinde raportul de marjă de vânzare cu posibilitatea de grupare după tipul și clasa categoriei.
- `stock`: extinde analiza stocurilor (`stock.quant`) cu cele două noi criterii de grupare.
- `account`: extinde raportul de facturi (`account.invoice.report`) cu cele două noi criterii de grupare.
