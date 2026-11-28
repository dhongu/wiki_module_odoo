# SAGA Interface MRP Extension (localizat la `deltatech_saga_mrp/index.md`)

- **Nume Tehnic:** `deltatech_saga_mrp`
- **Versiune:** `20.0.0.0.9`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_saga_mrp
- **Cale Locală:** `odoo-addons/bitshop/deltatech_saga_mrp`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul extinde interfața de export către SAGA astfel încât să acopere și fluxurile specifice de producție (MRP), în special mișcările de stoc generate de kituri (BoM-uri de tip „phantom”). Practic, elimină introducerea manuală de date și reduce erorile prin automatizarea sincronizării dintre producția din Odoo și înregistrările contabile/de gestiune din SAGA, oferind o vedere unitară asupra proceselor de fabricație, în timp ce evidența financiară rămâne consecventă în cele două sisteme.

#### 2. Funcționalități Cheie

- Pentru fiecare kit (listă de materiale de tip *Kit*) livrat în perioadă, exportul SAGA primește consumul componentelor (fișierul `BC_KIT_`) și producția kitului (fișierul `PRODUCTIE_KIT_`), ca SAGA să aibă kitul în stoc la importul facturilor de vânzare.
- **Consumul componentelor**: mișcările de stoc efectuate ale componentelor, în perioada și compania exportului.
- **Producția kitului**: cantitatea fiecărui kit se calculează din componente, pe transfer, și se scrie cu codul, unitatea, costul și gestiunea SAGA a locației; kitul se evaluează la costul curent, deci costul produselor-kit trebuie ținut la zi.
- **Varianta corectă**: un kit definit pe șablon și comun mai multor variante se exportă pentru varianta vândută sau cumpărată, cu componentele care i se aplică.
- **Unități convertite** între mișcări, listă de materiale și produs (2 duzini livrate ca 24 de bucăți înseamnă un kit); **retururile** (componente intrate înapoi în stoc) contează ca producție negativă de kit.
- Fișierele de kit se generează doar la exportul **Cantitativ-Valoric** (și la exportul incremental), doar în format **DBF**; cu doar XML bifat, rezultatul exportului avertizează. Sumarul arată câte kituri și câte consumuri s-au exportat.
- Configurare: *Referință internă* (codul SAGA) pe kit și pe componente și categorie de produs cu *Code SAGA*, altfel linia apare ca eroare (sau blochează exportul fără *Ignore Errors*). Modulul nu trimite date în afara Odoo: doar adaugă fișiere în arhiva exportului, pe care o importați singur în SAGA, odată cu celelalte fișiere.
- Fluxul pas cu pas e în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

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
