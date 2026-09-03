# Fără Stoc Negativ (localizat la `deltatech_stock_negative/index.md`)

- **Nume Tehnic:** `deltatech_stock_negative`
- **Versiune:** `19.0.2.0.7`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_stock_negative`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_negative`
- **Ultima Ingestie:** `2026-09-03`

#### 1. Sumar

Acest modul împiedică apariția stocurilor negative în locațiile interne ale companiei. Atunci când validarea unei operațiuni de stoc ar lăsa o cantitate fizică mai mică decât zero într-o locație, sistemul oprește operațiunea și afișează un mesaj de eroare, solicitând utilizatorului să corecteze cantitățile sau să realizeze o ajustare de inventar. Pentru situațiile excepționale, modulul permite configurarea anumitor locații în care stocul negativ este totuși acceptat, oferind astfel un control flexibil asupra disciplinei de stoc.

#### 2. Funcționalități Cheie

- Interzice stocul negativ pentru locațiile interne.
- Opțiunea globală se activează din `Inventar → Configurare → Setări → Trasabilitate → Stoc negativ` (bifa „Fără stoc negativ”, câmpul `no_negative_stock` de pe companie).
- Excepțiile per-locație se configurează din `Inventar → Configurare → Locații`, pe formularul fiecărei locații de stoc, bifând opțiunea care permite stoc negativ (`allow_negative_stock`) — util pentru locații virtuale/de tranzit sau alte cazuri unde blocarea nu trebuie aplicată.

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

**Modele**

- `stock.move.line` (extins): la `_action_done()`, verifică pentru fiecare linie dacă locația de destinație este internă, nu acceptă explicit stoc negativ și dacă opțiunea companiei `no_negative_stock` este activă; dacă retragerea ar duce cantitatea fizică a quant-ului sub zero, blochează validarea cu `UserError`. Verificarea se face pe cantitatea fizică (`quantity`), nu pe cea disponibilă, pentru a nu conta rezervarea proprie a mișcării ca cerere concurentă.
- `stock.quant` (extins): în `_get_available_quantity`, ignoră lotul/seria la calculul disponibilității pentru produsele cu trasabilitate pe serie atunci când locația nu are activată verificarea numerelor de serie și nu permite stoc negativ; rămâne fără efecte secundare, doar de citire/calcul (regula de blocare se aplică exclusiv la validarea mișcării, în `stock.move.line`).
- `stock.location` (extins): adaugă câmpurile `allow_negative_stock` (permite stoc negativ la acea locație) și `check_serial_no` (activ implicit; controlează dacă numerele de serie sunt verificate pe mișcări).
- `res.company` (extins): adaugă câmpul `no_negative_stock` care activează interdicția stocului negativ la nivel de companie.
- `res.config.settings` (extins): expune opțiunea `no_negative_stock` (câmp related pe companie) în setările de inventar.

**Vizualizări**

- `res_config_view.xml`: extinde setările de inventar (Inventar → Configurare → Setări → Trasabilitate → Stoc negativ) pentru a afișa opțiunea „Fără stoc negativ”.
- `stock_location_view.xml`: extinde formularul locației de stoc (Inventar → Configurare → Locații) pentru a permite marcarea locației ca acceptând stoc negativ.

#### 5. Conexiuni

- Nu au fost identificate conexiuni către alte module cu pagină wiki.
