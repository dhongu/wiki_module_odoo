# Batch Transfer Extension (localizat la `deltatech_batch_transfer/index.md`)

- **Nume Tehnic:** `deltatech_batch_transfer`
- **Versiune:** `20.0.0.0.8`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_batch_transfer
- **Cale Locală:** `odoo-addons/deltatech/deltatech_batch_transfer`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde transferul în lot (batch picking) din Odoo, pentru a oferi operatorilor de depozit un control mai bun asupra loturilor care conțin transferuri procesate parțial sau goale. Împiedică validarea transferurilor cu cantități zero și adaugă un asistent „Prepare Batch” cu care se grupează rapid recepțiile sau livrările din comenzile de vânzare/achiziție într-un singur lot.

#### 2. Funcționalități Cheie

- **Gestionarea transferurilor goale la validare**: la apăsarea butonului „Validate” pe lot, transferurile cu toate cantitățile efectuate egale cu zero sunt tratate după parametrul de sistem `deltatech_batch_keep_pickings` (**Setări > Tehnic > Parametri > Parametri de sistem**):
  - parametru absent (implicit, recomandat): transferurile goale sunt eliminate din lot, iar doar cele nevide sunt validate; cele eliminate pot fi adăugate manual în alt lot;
  - parametru `True`: transferurile goale rămân în lot, dar sunt sărite la validare, pentru procesare ulterioară (nerecomandat cu interfața barcode).
- **Asistentul „Prepare Batch”** (**Inventar > Managementul depozitului > Prepare batch**): creează un lot nou din transferurile deschise ale unui partener (furnizor în modul *Purchase*, client în modul *Sale*), cu responsabil, referință și, opțional, cantități efectuate completate dintr-o listă de produse. Se poate lansa și din lista comenzilor de vânzare, cu clientul precompletat.
- **Butonul „Add to batch”** pe transferul care nu e încă într-un lot și nu e finalizat/anulat, pentru atașarea lui la un lot existent.
- **Câmpuri suplimentare pe lot**: `Direction` (incoming/outgoing, doar citire), `Reference` și `Note`.
- **Tab „Received”** pe loturile de intrare: arată doar liniile cu cantitate > 0 (îngroșat), cele cu cantitate zero apar estompat.
- **Raport „Deliveries”** (**Print**): un PDF cu documentele de livrare ale tuturor transferurilor din lot.

Detaliile pas-cu-pas sunt în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `stock`
- `sale_stock`
- `purchase_stock`

#### 4. Componente Cheie

Documentația pentru acest modul a fost generată pe baza fișierului `readme/DESCRIPTION.md`. Conform fluxului de ingestie, analiza detaliată a codului pentru această secțiune a fost omisă, deoarece nu este solicitată explicit în Readme.

#### 5. Conexiuni

- `stock`: funcționalitatea standard de transfer în lot (batch picking) este inclusă în modulul `stock`, iar acest modul o extinde.
