# Sale Report Additional Info (localizat la `deltatech_sale_report/index.md`)

- **Nume Tehnic:** `deltatech_sale_report`
- **Versiune:** `20.0.0.0.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_report`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_report`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul adaugă adresa de email a clientului în raportul de analiză a vânzărilor (`sale.report`), astfel încât informația să fie disponibilă direct în analizele standard, fără căutări suplimentare în fișele de contact. *readme/DESCRIPTION.md* este minimal (și menționa o versiune veche, 17.0), deci pagina se bazează pe manifest și cod.

#### 2. Funcționalități Cheie

- Adaugă câmpul `partner_email` (*Partner Email*) în raportul de vânzări, populat din emailul partenerului comenzii și inclus în gruparea SQL a raportului.

#### 3. Dependențe

- `sale`

#### 4. Componente Cheie

**Modele**

- `sale.report` (extins): câmpul `partner_email`, populat prin `_select_dict()` și inclus în agregare prin `_groupby_list()`.

**Vizualizări**

- Modulul nu adaugă vizualizări proprii; câmpul poate fi expus în vizualizările existente ale raportului.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- `sale`: modulul extinde direct raportul standard de vânzări.
