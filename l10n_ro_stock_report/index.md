# Romania - Stock Report (Fișă Magazie) (localizat la `l10n_ro_stock_report/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_report`
- **Versiune:** `19.0.2.0.0`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_stock_report
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_stock_report`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Acest modul adaugă un raport de stocuri conform cerințelor legislației din România. El oferă fișa de magazie și balanța analitică a stocurilor, documente specifice gestiunii românești, pe care companiile sunt obligate să le poată genera pentru evidența mișcărilor și a soldurilor de produse pe gestiuni. Scopul principal este să aducă în Odoo aceste rapoarte standard cerute de contabilitatea românească, fără a fi nevoie de prelucrări externe.

#### 2. Funcționalități Cheie

- Generarea fișei de magazie pentru evidența intrărilor, ieșirilor și soldurilor de produse pe gestiuni.
- Generarea balanței analitice a stocurilor, conform cerințelor din România.
- Integrare cu fluxurile native Odoo de stoc, contabilitate, achiziții și vânzări.

#### 3. Dependențe

- `stock`
- `account`
- `purchase`
- `sale`
- `l10n_ro_config`

#### 4. Componente Cheie

Fișierul `readme/DESCRIPTION.md` este prezent și acoperă secțiunile „Sumar" și „Funcționalități Cheie". Conform fluxului de ingestie din schemă, analiza codului pentru această secțiune a fost omisă, deoarece Readme-ul nu solicită explicit detalierea componentelor tehnice (Modele, Vizualizări, Acțiuni Automate / Acțiuni Server).

#### 5. Conexiuni

- `l10n_ro_stock_picking_report`: modul înrudit din aceeași suită care furnizează documentele de mișcare a stocurilor (NIR, bon de consum, aviz de însoțire), complementar rapoartelor de sold oferite aici.
