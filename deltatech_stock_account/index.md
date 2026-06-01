# Stock Account Extension (localizat la `deltatech_stock_account/index.md`)

- **Nume Tehnic:** `deltatech_stock_account`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_stock_account
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_account`
- **Ultima Ingestie:** `2026-06-01`

#### 1. Sumar

Acest modul extinde funcționalitatea de evaluare a stocurilor din Odoo, aducând informația de valoare a stocului direct la nivelul transferurilor de marfă (livrări/recepții). Astfel, utilizatorii care gestionează mișcările de stoc pot vedea imediat valoarea contabilă asociată unui transfer, fără a fi nevoie să caute aceste date în alte rapoarte sau ecrane. Beneficiul principal este o vizibilitate mai bună asupra valorii bunurilor în mișcare, util pentru echipele de logistică și contabilitate.

#### 2. Funcționalități Cheie

- Adaugă evaluarea stocului la nivelul transferului de marfă (picking).
- Afișează valoarea evaluării stocului direct în formularul transferului.

#### 3. Dependențe

- `stock_account`

#### 4. Componente Cheie

Sumarul și funcționalitățile cheie au fost preluate din fișierul `readme/DESCRIPTION.md`, conform fluxului de ingestie. Analiza detaliată a codului pentru componente nu este necesară, deoarece Readme-ul nu o solicită explicit.

#### 5. Conexiuni

- `stock_account`: modulul standard Odoo de evaluare a stocurilor, pe care această extensie îl completează cu afișarea valorii la nivel de transfer.
