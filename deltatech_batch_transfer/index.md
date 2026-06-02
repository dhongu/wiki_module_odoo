# Deltatech Batch Transfer (localizat la `deltatech_batch_transfer/index.md`)

- **Nume Tehnic:** `deltatech_batch_transfer`
- **Versiune:** `19.0.0.0.2`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_batch_transfer`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_batch_transfer`
- **Ultima Ingestie:** `2026-06-02`

#### 1. Sumar

Modulul îmbunătățește funcționalitatea de transfer în lot (batch picking) din Odoo, oferind o gestionare inteligentă a livrărilor „goale” — adică acele transferuri din lot la care toate cantitățile procesate sunt zero. În mod standard, Odoo procesează toate cantitățile pentru aceste livrări atunci când lotul este validat, ceea ce poate duce la rezultate nedorite. Acest modul permite excluderea automată a livrărilor goale din lot la validare, astfel încât doar transferurile cu cantități reale să fie procesate, restul putând fi tratate ulterior. Pe lângă acest comportament, modulul adaugă și câmpuri suplimentare utile pentru organizarea loturilor.

#### 2. Funcționalități Cheie

- Gestionează automat livrările „goale” (transferuri cu toate cantitățile zero) dintr-un lot la apăsarea butonului „Validează”.
- Dacă parametrul de sistem `deltatech_batch_keep_pickings` **nu** este prezent: livrările goale sunt eliminate din lot la validare și sunt procesate doar transferurile ne-goale (comportament recomandat). Livrările goale pot fi adăugate manual într-un alt lot. Dacă toate livrările din lot sunt goale, lotul devine gol.
- Dacă parametrul de sistem `deltatech_batch_keep_pickings` **este** prezent: livrarea goală nu este procesată, dar rămâne în lot pentru a fi tratată ulterior (nerecomandat, întrucât nu funcționează corect în interfața barcode).
- Adaugă câmpurile suplimentare `direction`, `reference` și `note` pe transferul în lot.

#### 3. Dependențe

- `stock`
- `stock_picking_batch`
- `sale_stock`
- `purchase_stock`

#### 4. Componente Cheie

Conform fluxului de ingestie, componentele tehnice nu sunt detaliate deoarece secțiunile „Sumar" și „Funcționalități Cheie" provin din `readme/DESCRIPTION.md`, care nu solicită explicit analiza codului pentru această secțiune.

#### 5. Conexiuni

- `stock_picking_batch`: modulul standard Odoo de transfer în lot, a cărui funcționalitate este extinsă de acest modul.
