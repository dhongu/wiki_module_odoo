# SAGA Interface MRP Extension (localizat la `deltatech_saga_mrp/index.md`)

- **Nume Tehnic:** `deltatech_saga_mrp`
- **Versiune:** `19.0.0.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_saga_mrp
- **Cale Locală:** `odoo-addons/bitshop/deltatech_saga_mrp`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul extinde interfața de export către SAGA astfel încât să acopere și fluxurile specifice de producție (MRP), în special mișcările de stoc generate de kituri (BoM-uri de tip „phantom”). Practic, elimină introducerea manuală de date și reduce erorile prin automatizarea sincronizării dintre producția din Odoo și înregistrările contabile/de gestiune din SAGA, oferind o vedere unitară asupra proceselor de fabricație, în timp ce evidența financiară rămâne consecventă în cele două sisteme.

#### 2. Funcționalități Cheie

- Sincronizare automată a mișcărilor de stoc generate de comenzile de producție și de kituri (BoM phantom) din Odoo către SAGA.
- Export dedicat pentru consumurile și producțiile aferente kiturilor, cu fișiere separate (`BC_KIT_`, `PRODUCTIE_KIT_`).
- Schimb de date în timp real pentru costurile de producție, actualizările de inventar și contabilitatea de producție.
- Reducerea erorilor umane și a discrepanțelor de date prin transmiterea electronică a înregistrărilor de fabricație.
- Vedere unificată asupra proceselor de producție în Odoo, menținând în același timp înregistrări financiare consistente în SAGA.
- Interoperabilitate scalabilă — se pot adăuga ușor noi facilități de producție și linii de fabricație pe măsură ce afacerea crește.

#### 3. Dependențe

- [deltatech_saga](../deltatech_saga/index.md)
- `mrp`

#### 4. Componente Cheie

**Modele**

- `export.saga` (extindere, `wizard/export_saga.py`): adaugă la colectarea datelor de export identificarea mișcărilor de stoc (`stock.move`) legate de linii de BoM (`bom_line_id`) de tip `phantom` (kituri), le grupează pe recepție/livrare (`picking_id`) și produs, calculând cantitățile consumate/produse proporțional cu rețeta (BoM); adaugă și statistici de export (nr. kituri, nr. consumuri) și declanșează exportul lor în arhiva ZIP (`do_export_productions_kit`).
- `export.saga.models` (extindere, `wizard/export_saga_models.py`): construiește înregistrările de tip „producție” pentru fiecare kit (`_export_production_kit`), validând existența codului SAGA pe categoria de produs (`code_saga`), determinând gestiunea (locația de stoc) și calculând valoarea (cantitate x preț standard) pentru fișierul DBF trimis către SAGA.

**Vizualizări**

- Nu sunt definite vizualizări proprii — modulul nu conține fișiere de date/views (`"data": []` în manifest); reutilizează integral interfața wizard-ului de export definită în `deltatech_saga`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` — exportul se declanșează manual, prin wizard-ul de export SAGA (`export.saga`).

#### 5. Conexiuni

- [deltatech_saga](../deltatech_saga/index.md): modulul de bază peste care se grefează, oferind wizard-ul și infrastructura de export (scriitor DBF/XML, parametri de export).
- `mrp`: sursa datelor de producție — BoM-uri (inclusiv cele de tip `phantom`/kit) și mișcările de stoc generate de comenzile de fabricație.
- `stock`: modulul furnizează modelul `stock.move` folosit pentru identificarea și calculul consumurilor/producțiilor de kituri.
