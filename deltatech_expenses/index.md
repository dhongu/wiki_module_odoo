# Expenses Deduction (localizat la `deltatech_expenses/index.md`)

- **Nume Tehnic:** `deltatech_expenses`
- **Versiune:** `19.0.2.2.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_expenses
- **Cale Locală:** `odoo-addons/deltatech/deltatech_expenses`
- **Ultima Ingestie:** `2026-06-01`

#### 1. Sumar

Modulul gestionează decontarea cheltuielilor efectuate de angajați pe baza avansurilor primite. Permite introducerea unui decont de cheltuieli într-un document distinct, care generează automat chitanțele de achiziție aferente, iar la validare produce notele contabile de avans și înregistrează plățile. Astfel, soldul avansurilor de decontat (cont 542) se închide corect, calculându-se automat diferența de restituit sau de încasat între avansul acordat și cheltuielile justificate, inclusiv TVA-ul deductibil.

#### 2. Funcționalități Cheie

- Introducerea decontului de cheltuieli într-un document distinct care generează automat chitanțe de achiziție.
- Validarea documentului duce la generarea notelor contabile de avans și înregistrarea plăților.
- Calculul automat al diferenței dintre avansul acordat și totalul cheltuielilor (restituire sau încasare).
- Calculul corect al TVA-ului deductibil aferent cheltuielilor.
- Generarea documentului de încasare (Chitanță / Dispoziție de Încasare) pentru restituirea soldului de către angajat.
- Închiderea automată a contului de avansuri de decontat (542) la contabilizarea finală.

> **Configurare:** În registrul de numerar trebuie completat câmpul "Cash advances" cu contul 542.

#### 3. Dependențe

- `l10n_ro`
- `account`
- `product`
- `deltatech_partner_generic`

#### 4. Componente Cheie

Informațiile pentru Componente Cheie nu sunt acoperite de `readme/DESCRIPTION.md`, iar conform fluxului de ingestie analiza suplimentară a codului se omite atunci când Sumarul și Funcționalitățile Cheie sunt preluate din Readme.

#### 5. Conexiuni

Nu au fost identificate conexiuni către alte module cu pagină wiki existentă.
