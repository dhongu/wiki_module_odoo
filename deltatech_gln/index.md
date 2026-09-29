# Deltatech Partner GLN (localizat la `deltatech_gln/index.md`)

- **Nume Tehnic:** `deltatech_gln`
- **Versiune:** `19.0.1.1.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_gln
- **Cale Locală:** `odoo-addons/deltatech/deltatech_gln`
- **Ultima Ingestie:** `2026-09-29`

> **Notă:** Conform documentației modulului, acesta este considerat **Obsolet**. Funcționalitatea sa de bază a fost mutată și este acum mai bine acoperită de modulul `account_add_gln`. Pentru proiecte noi se recomandă utilizarea directă a `account_add_gln`.

#### 1. Sumar

Acest modul a fost conceput pentru a gestiona Numărul Global de Locație (GLN — Global Location Number) la nivel de parteneri în Odoo. Rolul său este să se asigure că datele GLN sunt corect stocate și sincronizate pentru schimbul electronic de date (EDI) și pentru procesele logistice. În prezent modulul este marcat ca **obsolet**: funcționalitatea sa principală a fost preluată de modulul `account_add_gln`, iar `deltatech_gln` rămâne în principal ca strat de compatibilitate pentru configurațiile mai vechi care încă depind de el.

#### 2. Funcționalități Cheie

- **Integrarea câmpului GLN**: adaugă un câmp dedicat **GLN (Global Location Number)** în vizualizarea formularului de partener, făcând datele GLN ușor accesibile și editabile pentru fiecare locație de business.
- **Strat de compatibilitate**: acționează ca punte pentru configurațiile vechi (legacy) care necesită dependența `deltatech_gln`.
- **Suport pentru migrare**: sprijină migrarea datelor GLN către noul standard `account_add_gln`.
- **Transfer automat al valorilor către câmpul standard** (din 19.0.1.1.0): la actualizare, valorile din `gln` sunt copiate în câmpul standard `global_location_number` (modulul `account_add_gln`, instalat automat cu `account`). Se completează doar valorile goale din câmpul standard, deci nu se suprascrie nicio corecție făcută acolo, iar operația poate fi rulată din nou fără risc. Partenerii care au două valori diferite sunt raportați în log, nu modificați. Dacă baza de date nu are câmpul standard (fără `account`), nu se face nimic.
- **Pictogramă proprie** (din 19.0.1.1.1), în locul celei generice.

#### 3. Dependențe

- `base`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile „Componente Cheie" sunt omise deoarece „Sumar" și „Funcționalități Cheie" provin din `readme/DESCRIPTION.md`, iar acesta nu solicită explicit analiza codului. Modulul adaugă, la nivel de implementare, un câmp GLN pe partener prin vizualizarea `views/res_partner_view.xml`, iar scriptul de migrare `migrations/19.0.1.1.0/post-migration.py` copiază valorile în câmpul standard `global_location_number`.

#### 5. Conexiuni

- `account_add_gln`: modulul succesor care preia gestionarea GLN; modulele noi ar trebui să îl folosească pe acesta în locul lui `deltatech_gln`. (Nu are încă pagină wiki.)
