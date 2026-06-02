# Deltatech Analytic distribution enforcer (localizat la `deltatech_analytic_distribution/index.md`)

- **Nume Tehnic:** `deltatech_analytic_distribution`
- **Versiune:** `19.0.0.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_analytic_distribution
- **Cale Locală:** `odoo-addons/deltatech/deltatech_analytic_distribution`
- **Ultima Ingestie:** `2026-06-02`

#### 1. Sumar

Acest modul impune completarea corectă a distribuției analitice pe facturile de la furnizori. Atunci când validarea este activată, fiecare linie de pe o factură de furnizor trebuie să aibă distribuția analitică completată integral, cu toate dimensiunile cerute (Locație, Departament, Linie de business), iar procentele de pe fiecare linie trebuie să însumeze exact 100%. Astfel se asigură o repartizare analitică completă și coerentă a cheltuielilor, evitând înregistrările incomplete care ar denatura analiza de costuri.

#### 2. Funcționalități Cheie

- Facturile de la furnizori vor cere ca distribuția analitică să însumeze 100% pe fiecare linie, iar toate câmpurile să fie completate (Locație, Departament, Linie de business).
- Pentru a activa această validare se bifează opțiunea „Enable Analytic Distribution Validation" din configurare, în blocul Vendor Bills (Facturi furnizori).

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, documentarea componentelor tehnice se face la nivel de funcționalitate (vezi secțiunile 1 și 2). Analiza detaliată a modelelor, vizualizărilor și acțiunilor nu este reluată aici, întrucât DESCRIPTION.md acoperă scopul modulului.

#### 5. Conexiuni

- Nu au fost identificate conexiuni funcționale cu alte module documentate în wiki.
