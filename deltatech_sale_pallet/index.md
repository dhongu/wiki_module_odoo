# Paleți pe comenzi de vânzare (localizat la `deltatech_sale_pallet/index.md`)

- **Nume Tehnic:** `deltatech_sale_pallet`
- **Versiune:** `19.0.1.0.8`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_pallet`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_pallet`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul adaugă automat paleți pe comenzile de vânzare și pe facturi. Atunci când un produs care necesită paletizare atinge o cantitate minimă configurată, sistemul introduce automat în comandă produsul de tip palet și ajustează numărul de paleți necesari pe măsură ce cantitatea trece de fiecare multiplu al cantității minime. Astfel, vânzarea reflectă corect ambalarea pe paleți, fără ca operatorul să adauge manual liniile de palet.

#### 2. Funcționalități Cheie

- Definirea unei categorii de produs cu opțiunea „Palet" activată.
- Selectarea produsului de tip palet și încadrarea lui în categoria de mai sus.
- Configurarea unei cantități minime pentru un palet.
- Adăugarea automată a produsului palet pe comanda de vânzare în momentul în care un produs care necesită paleți atinge cantitatea minimă pentru un palet.
- Creșterea automată a cantității de paleți necesari pe măsură ce se atinge următorul multiplu al cantității minime pentru un palet.

#### 3. Dependențe

- `sale_margin`
- `account`

#### 4. Componente Cheie

*Sumarul și funcționalitățile au fost preluate din `readme/DESCRIPTION.md`; analiza detaliată a codului pentru această secțiune nu a fost solicitată în Readme. Componentele de mai jos sunt menționate orientativ, pe baza structurii modulului.*

**Modele**

- `product.category`: extins pentru opțiunea de palet la nivel de categorie.
- `product.template`: extins pentru configurarea produsului ca palet și a cantității minime pentru un palet.
- `sale.order` / `sale.order.line`: logica de adăugare automată a liniilor de palet pe comanda de vânzare.
- `account.move`: tratarea paleților la nivel de factură.
- `sale.report`: extinderea raportării de vânzări.

**Vizualizări**

- `views/product_view.xml`: interfața de configurare a categoriei și produsului de tip palet.
- `views/invoice_view.xml`: ajustări de afișare a paleților pe factură.

#### 5. Conexiuni

- `sale_margin`: bază pentru gestionarea liniilor de comandă de vânzare extinse de acest modul.
- `account`: tratarea paleților la nivel de factură.
