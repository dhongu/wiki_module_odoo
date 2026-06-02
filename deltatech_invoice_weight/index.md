# Invoice Weight (localizat la `deltatech_invoice_weight/index.md`)

- **Nume Tehnic:** `deltatech_invoice_weight`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_invoice_weight
- **Cale Locală:** `odoo-addons/deltatech/deltatech_invoice_weight`
- **Ultima Ingestie:** `2026-06-02`

#### 1. Sumar

Modulul adaugă urmărirea greutății logistice direct în sistemele de facturare și de gestiune a comenzilor din Odoo. Este destinat companiilor care au nevoie să monitorizeze și să raporteze greutatea netă și greutatea brută totală a articolelor facturate, achiziționate sau vândute, oferind astfel o transparență suplimentară pentru operațiunile logistice și de transport.

#### 2. Funcționalități Cheie

- **Câmpuri de greutate pe documente**: adaugă câmpurile Greutate Netă și Greutate Brută pe facturi, comenzi de achiziție și comenzi de vânzare, cu calculul automat al greutăților totale ale documentului pe baza articolelor incluse.
- **Raportare și analiză**: activează raportarea pe bază de greutate în vizualizarea de analiză a facturilor și suportă vizualizări de tip Pivot, permițând agregarea greutăților pe partener, produs sau perioadă.
- **Greutate pe raportul tipărit**: afișează informațiile de greutate pe raportul tipărit al facturii, pentru transparență logistică.
- **Consistență între documente**: asigură menținerea și transferul corect al datelor de greutate între documentele de vânzare/achiziție și factura finală.

#### 3. Dependențe

- `account`
- `purchase`
- `stock`
- `sale`

#### 4. Componente Cheie

Conform fluxului de ingestie, această secțiune este derivată din `readme/DESCRIPTION.md`. Modulul extinde documentele standard de facturare, vânzare și achiziție pentru a adăuga câmpurile de greutate netă și brută, calculul automat al acestora, raportarea de tip Pivot pe analiza facturilor și afișarea greutăților pe raportul tipărit al facturii.

#### 5. Conexiuni

Nu au fost identificate conexiuni către alte module documentate în wiki. Modulul se integrează cu funcționalitățile standard Odoo de contabilitate (`account`), achiziții (`purchase`), stoc (`stock`) și vânzări (`sale`).
