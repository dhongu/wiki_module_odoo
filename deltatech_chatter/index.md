# Resizable Chatter Panel

- **Nume Tehnic:** `deltatech_chatter`
- **Versiune:** `20.0.0.2.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_chatter
- **Cale Locală:** `odoo-addons/bitshop/deltatech_chatter`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul îmbunătățește formularele Odoo printr-un panou divizat redimensionabil între conținutul formularului și zona de chatter (istoricul de comunicare). Rezolvă problema în care chatterul ocupă prea mult sau prea puțin loc: fiecare utilizator alocă spațiul de pe ecran după nevoi, glisând separatorul, sau ascunde chatterul când formularul are nevoie de toată lățimea. Modulul nu încarcă cod Python, doar JavaScript, o foaie de stil și biblioteca Split.js, deci poate fi folosit și pe Odoo Online (plan Custom, prin *Apps > Import Module*).

#### 2. Funcționalități Cheie

- **Interfață divizată redimensionabilă:** separare orizontală între formular și chatter, cu raport implicit de 70% pentru formular și 30% pentru chatter.
- **Redimensionare interactivă:** utilizatorii trag de separator; proporția se salvează în browser la eliberarea mouse-ului și se aplică pe toate formularele.
- **Design responsiv:** se adaptează la redimensionarea ferestrei; limite minime de 300px pentru formular și 250px pentru chatter.
- **Ascunderea chatterului:** un buton rotund de pe separator sau **Alt+Shift+F** (pe macOS **Control+Shift+F**) ascunde chatterul, iar formularul ocupă toată lățimea; o bandă subțire cu același buton îl readuce. Alegerea se păstrează în browser pentru toate formularele.
- **Domeniu de aplicare:** pe ecrane late, unde chatterul stă în dreapta formularului; formularele din dialoguri și ecranele înguste, unde chatterul e sub formular, nu sunt afectate.
- Nu necesită configurare; pașii cu capturi sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `mail`

#### 4. Componente Cheie

Modulul nu definește modele, vizualizări sau acțiuni automate. Funcționalitatea este exclusiv în frontend, prin active `web.assets_backend`:

- `static/src/lib/split/split.min.js`: biblioteca Split.js pentru panoul redimensionabil.
- `static/src/js/chatter_split.esm.js`: patch peste `FormRenderer`, care inițializează separatorul, curăță la demontare, ascultă redimensionarea ferestrei, gestionează butonul/scurtătura de ascundere și cazul în care elementele DOM lipsesc.
- `static/src/scss/style.scss`: stilurile panoului divizat.
- `static/tests/`: teste unitare web (`web.assets_unit_tests`).

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale cu alte module documentate în wiki.
