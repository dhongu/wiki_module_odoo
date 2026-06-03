# Deltatech Chatter

- **Nume Tehnic:** `deltatech_chatter`
- **Versiune:** `19.0.0.0.3`
- **Cale:** https://github.com/terrabit-ro/bitshop/tree/19.0/deltatech_chatter
- **Cale Locală:** `odoo-addons/bitshop/deltatech_chatter`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul Deltatech Chatter îmbunătățește vizualizarea de tip formular din Odoo prin introducerea unui panou divizat redimensionabil între conținutul formularului și zona de chatter (istoricul de comunicare). Modulul rezolvă o problemă frecventă de utilizabilitate, în care secțiunea de chatter ocupă fie prea mult, fie prea puțin spațiu pentru o urmărire eficientă a mesajelor. Astfel, fiecare utilizator poate aloca spațiul de pe ecran în funcție de propriile nevoi, glisând pur și simplu separatorul dintre cele două zone.

#### 2. Funcționalități Cheie

- **Interfață divizată redimensionabilă:** introduce o separare orizontală între conținutul formularului și secțiunea de chatter.
- **Raport de dimensiune personalizabil:** dimensionare implicită de 70% pentru conținutul formularului și 30% pentru chatter.
- **Redimensionare interactivă:** utilizatorii pot trage de separator pentru a ajusta proporția după preferințe.
- **Design responsiv:** se adaptează automat la redimensionarea ferestrei.
- **Limite minime de dimensiune:** previne micșorarea excesivă a secțiunilor (300px pentru formular, 250px pentru chatter).

#### 3. Dependențe

- `base`

#### 4. Componente Cheie

Modulul nu definește modele, vizualizări sau acțiuni automate noi. Funcționalitatea este implementată exclusiv la nivel de frontend, prin active web (`web.assets_backend`):

- `static/src/lib/split/split.min.js`: biblioteca Split.js folosită pentru a crea interfața redimensionabilă.
- `static/src/js/chatter_split.esm.js`: patch aplicat peste `FormRenderer` din Odoo pentru a adăuga funcționalitatea de divizare în vizualizările formular (inițializare dinamică a separatorului, curățare la demontarea componentei, ascultători pentru redimensionarea ferestrei și tratarea cazurilor în care elementele DOM necesare nu sunt disponibile).
- `static/src/scss/style.scss`: stilurile aferente panoului divizat.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale cu alte module documentate în wiki.
