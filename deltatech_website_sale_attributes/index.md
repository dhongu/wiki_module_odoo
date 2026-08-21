# eCommerce Attribute Values (localizat la `deltatech_website_sale_attributes/index.md`)

- **Nume Tehnic:** `deltatech_website_sale_attributes`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_sale_attributes
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_sale_attributes`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul îmbunătățește modul în care sunt afișate valorile atributelor produselor pe site-ul de comerț electronic. În mod implicit, Odoo afișează toate valorile posibile ale unui atribut, chiar și pe cele care nu mai corespund niciunui produs disponibil. Modulul filtrează aceste valori astfel încât clientul vede doar opțiunile relevante pentru produsele afișate efectiv, oferind o experiență de selecție mai clară și mai curată în magazinul online.

#### 2. Funcționalități Cheie

- Afișarea valorilor de atribut pe baza produselor determinate (relevante pentru selecția curentă).
- Filtrarea valorilor de atribut pentru a afișa doar pe cele relevante pentru produsele disponibile în acel moment.
- Optimizarea experienței de selecție a atributelor pentru clienți în magazinul online.
- Modificarea comportamentului implicit al Odoo prin ajustarea șablonului `website_sale.products_attributes`, astfel încât să afișeze doar opțiunile relevante.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

Documentația de Sumar și Funcționalități Cheie a fost preluată din `readme/DESCRIPTION.md`, care nu solicită explicit detalierea componentelor tehnice. Conform fluxului de ingestie, analiza detaliată a Modelelor, Vizualizărilor și Acțiunilor a fost omisă.

#### 5. Conexiuni

- `website_sale`: modulul standard Odoo de comerț electronic, al cărui șablon de afișare a atributelor produselor este extins și ajustat de acest modul.
