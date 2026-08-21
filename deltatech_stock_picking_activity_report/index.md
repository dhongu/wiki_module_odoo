# Stock Picking Activity Report (localizat la `deltatech_stock_picking_activity_report/index.md`)

- **Nume Tehnic:** `deltatech_stock_picking_activity_report`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_stock_picking_activity_report
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_picking_activity_report`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul ține evidența activității pe fiecare transfer de stoc (recepție, livrare sau transfer intern): înregistrează automat modificările de câmpuri, mesajele postate în chatter și evenimentele de validare (cu numărul de produse recepționate, livrate sau mutate intern), astfel încât managerii de depozit pot vedea, din meniul Inventar -> Raportare -> Raport Activitate, cine a lucrat pe fiecare document și ce s-a schimbat. Înregistrările mai vechi de 2 luni sunt șterse automat prin mecanismul Data Recycle, astfel încât raportul rămâne relevant fără a acumula date istorice inutile.

#### 2. Funcționalități Cheie

- Înregistrează modificările detaliate pe transferurile de stoc, inclusiv schimbările de câmpuri și actualizările liniilor.
- Captează mesajele postate în chatter pentru un istoric complet al activității.
- Urmărește automat evenimentele de validare și categorizează numărul de produse procesate (Intrare, Ieșire sau Intern).
- Oferă un Raport de Activitate accesibil din Inventar -> Raportare -> Raport Activitate pentru analiză statistică.
- Șterge automat înregistrările de activitate mai vechi de 2 luni prin mecanismul Data Recycle.

#### 3. Dependențe

- `stock`
- `data_recycle`

#### 4. Componente Cheie

Conform fluxului de ingestie, această secțiune este omisă deoarece `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie și nu solicită explicit analiza componentelor tehnice.

#### 5. Conexiuni

- Niciun modul conex cu pagină wiki existentă nu a fost identificat.
