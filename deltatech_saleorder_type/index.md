# Terrabit - Sale Order Type - Obsolete (localizat la `deltatech_saleorder_type/index.md`)

- **Nume Tehnic:** `deltatech_saleorder_type`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_saleorder_type
- **Cale Locală:** `odoo-addons/deltatech/deltatech_saleorder_type`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Modul **obsolet**, păstrat doar pentru compatibilitate. A fost conceput pentru clasificarea comenzilor de vânzare pe tipuri (de exemplu retail, en-gros, export), cu fluxuri sau valori implicite diferite în funcție de tip. În versiunea 19.0 nu mai conține nicio funcționalitate: este o „carcasă” goală care depinde doar de `deltatech_record_type`, menținută ca bazele de date pe care este încă instalat să se poată actualiza fără erori. Nu este afișat în lista de aplicații și poate fi dezinstalat după migrare. Pentru proiecte noi se folosește gestiunea tipurilor de înregistrări din suita Deltatech sau categorizarea standard Odoo.

#### 2. Funcționalități Cheie

- Fără funcționalitate activă în 19.0: nu are modele, vizualizări sau date (`data` este gol, directorul `models/` nu conține cod sursă).
- Modul ascuns din Apps (`hidden: True`), stare de dezvoltare Beta.
- Rol istoric: tipuri personalizate de comenzi de vânzare, construite peste modulul de bază `deltatech_record_type`.
- Recomandare: dezinstalare după ce nicio personalizare veche nu mai depinde de el.

#### 3. Dependențe

- [deltatech_record_type](../deltatech_record_type/index.md)

#### 4. Componente Cheie

**Modele**

Niciun model definit în 19.0.

**Vizualizări**

Nicio vizualizare definită.

**Acțiuni Automate / Acțiuni Server**

Nicio acțiune definită.

#### 5. Conexiuni

- [deltatech_record_type](../deltatech_record_type/index.md): modulul de bază pentru gestiunea tipurilor, singura legătură a acestui modul.
