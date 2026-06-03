# Fără Stoc Negativ (localizat la `deltatech_stock_negative/index.md`)

- **Nume Tehnic:** `deltatech_stock_negative`
- **Versiune:** `19.0.2.0.6`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_stock_negative`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_negative`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul împiedică apariția stocurilor negative în locațiile interne ale companiei. Atunci când o operațiune de stoc ar duce la o cantitate disponibilă mai mică decât zero, sistemul oprește operațiunea și afișează un mesaj de eroare, solicitând utilizatorului să corecteze cantitățile sau să realizeze o ajustare de inventar. Pentru situațiile excepționale, modulul permite configurarea anumitor locații în care stocul negativ este totuși acceptat, oferind astfel un control flexibil asupra disciplinei de stoc.

#### 2. Funcționalități Cheie

- Interzice stocul negativ pentru locațiile interne.
- Permite stoc negativ la anumite locații configurate explicit.

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

**Modele**

- `stock.quant` (extins): suprascrie metoda de calcul a cantității disponibile pentru a bloca operațiunile care ar genera stoc negativ în locațiile interne, atunci când opțiunea companiei este activată.
- `stock.location` (extins): adaugă câmpurile `allow_negative_stock` (permite stoc negativ la acea locație) și `check_serial_no` (verificarea numerelor de serie).
- `res.company` (extins): adaugă câmpul `no_negative_stock` care activează interdicția stocului negativ la nivel de companie.
- `res.config.settings` (extins): expune opțiunea `no_negative_stock` în setările de inventar.

**Vizualizări**

- `res_config_view.xml`: extinde setările de inventar (Inventar → Configurare → Setări) pentru a afișa opțiunea „Fără stoc negativ”.
- `stock_location_view.xml`: extinde formularul locației de stoc (Inventar → Configurare → Locații) pentru a permite marcarea locației ca acceptând stoc negativ.

#### 5. Conexiuni

- Nu au fost identificate conexiuni către alte module cu pagină wiki.
