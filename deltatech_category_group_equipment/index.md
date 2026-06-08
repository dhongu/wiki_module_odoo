# Deltatech Equipment Category Group (localizat la `deltatech_category_group_equipment/index.md`)

- **Nume Tehnic:** `deltatech_category_group_equipment`
- **Versiune:** `19.0.0.0.2`
- **Cale:** https://github.com/dhongu/deltatech_service/tree/19.0/deltatech_category_group_equipment
- **Cale Locală:** `odoo-addons/deltatech_service/deltatech_category_group_equipment`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Modulul adaugă elemente de grupare pentru echipamente, preluate din grupurile definite pe categoria internă a produsului asociat echipamentului. Astfel, echipamentele pot fi organizate și filtrate după „tipul categoriei" și „clasa categoriei", facilitând clasificarea și raportarea parcului de echipamente în mod consecvent cu categoriile de produse.

#### 2. Funcționalități Cheie

- Adaugă două elemente de grupare pentru echipamente: „tipul categoriei" (Category type) și „clasa categoriei" (Category class).
- Aceste grupări sunt legate de categoria internă a produsului echipamentului.

#### 3. Dependențe

- [deltatech_category_group](../deltatech_category_group/index.md)
- `deltatech_service_equipment`

#### 4. Componente Cheie

Documentația pentru această secțiune a fost omisă, deoarece fișierul `readme/DESCRIPTION.md` nu solicită explicit analiza componentelor tehnice (modele, vizualizări, acțiuni automate / acțiuni server).

#### 5. Conexiuni

- [deltatech_category_group](../deltatech_category_group/index.md): furnizează grupurile de categorii (tip și clasă) pe care acest modul le propagă la nivel de echipament.
- `deltatech_service_equipment`: definește modelul de echipamente extins de acest modul cu cele două elemente de grupare.
