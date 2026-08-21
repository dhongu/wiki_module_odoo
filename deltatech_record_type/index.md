# Terrabit - Record Type (localizat la `deltatech_record_type/index.md`)

- **Nume Tehnic:** `deltatech_record_type`
- **Versiune:** `19.0.1.1.12`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_record_type`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_record_type`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul Terrabit - Record Type oferă o modalitate îmbunătățită de a gestiona mai multe tipuri de înregistrări pentru diverse documente Odoo, inclusiv comenzi de vânzare, comenzi de achiziție și facturi. Permite companiilor să definească și să întrețină tipuri distincte de documente, fiecare cu valori implicite specifice și configurări de rutare a stocului. Astfel se standardizează crearea documentelor, se reduc erorile de introducere a datelor și fiecare utilizator vede doar tipurile relevante pentru rolul său.

#### 2. Funcționalități Cheie

- Definirea de tipuri de înregistrare personalizate pentru comenzi de vânzare, comenzi de achiziție și facturi.
- Asignarea de utilizatori specifici fiecărui tip de înregistrare, pentru control al accesului.
- Setarea de valori implicite pentru câmpuri la crearea unei noi înregistrări de un anumit tip.
- Configurarea rutelor de stoc pentru fiecare tip de înregistrare.
- Afișarea câmpului de tip doar în modelele în care există tipuri definite.

#### 3. Dependențe

- `sale`
- `sale_stock`
- `purchase`

#### 4. Componente Cheie

**Modele**

(menționate explicit în `readme/DESCRIPTION.md`)

- `record.type`: Definește configurația tipului de înregistrare, inclusiv modelul țintă (`sale.order`, `purchase.order`, `account.move`), utilizatorii permiși și rutele de stoc asociate.
- `record.type.default.values`: Gestionează valorile implicite ale câmpurilor pentru fiecare tip de înregistrare, cu selecție dinamică a câmpului în funcție de model.

#### 5. Conexiuni

- [deltatech_marketplace_sale_type](../deltatech_marketplace_sale_type/index.md): depinde de acest modul, folosind cadrul de tipuri de înregistrare pentru comenzile de vânzare din marketplace.
