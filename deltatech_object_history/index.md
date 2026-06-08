# Deltatech Object History (localizat la `deltatech_object_history/index.md`)

- **Nume Tehnic:** `deltatech_object_history`
- **Versiune:** `19.0.0.0.1`
- **Cale:** https://github.com/dhongu/deltatech_service/tree/19.0/deltatech_object_history
- **Cale Locală:** `odoo-addons/deltatech_service/deltatech_object_history`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Modulul creează un istoric paralel pentru documentele Odoo, separat de sistemul standard de mesaje (chatter). Spre deosebire de mesajele obișnuite, care pot fi șterse periodic, intrările din acest istoric sunt păstrate permanent. Astfel, utilizatorii pot înregistra comentarii și note importante legate de un document, cu garanția că acestea nu vor fi eliminate în timp, oferind o evidență durabilă a observațiilor relevante pentru afacere.

#### 2. Funcționalități Cheie

- Creează un model nou (`object.history`) pentru stocarea comentariilor utilizatorilor, separat de sistemul standard de chatter/mesaje Odoo.
- Istoricul nou nu este șters periodic.
- Intrările în istoric pot fi adăugate folosind o acțiune (wizard).
- TODO: legarea istoricului cu modelul de parteneri.

#### 3. Dependențe

- `contacts`
- `account`
- `stock`

#### 4. Componente Cheie

Nu se aplică. Fișierul `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie și nu solicită explicit analiza codului pentru această secțiune, conform fluxului de ingestie din schemă. Analiza codului a fost, prin urmare, omisă.

#### 5. Conexiuni

Nu au fost identificate conexiuni documentate în fișierele readme.
