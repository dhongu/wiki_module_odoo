# Deltatech Partner Gifts (localizat la `deltatech_partner_gifts/index.md`)

- **Nume Tehnic:** `deltatech_partner_gifts`
- **Versiune:** `19.0.0.1.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_partner_gifts
- **Cale Locală:** `odoo-addons/bitshop/deltatech_partner_gifts`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul gestionează cadourile oferite anumitor parteneri (clienți sau contacte). Permite generarea de linii de cadou pornind de la partenerii selectați, tipărirea etichetelor de cadou (expeditor/destinatar, pentru livrare) și colectarea de date despre parteneri (de exemplu totalul facturat în anul curent) printr-o acțiune de server. De asemenea, oferă posibilitatea de a copia și modifica în masă cadourile existente, simplificând astfel organizarea campaniilor de cadouri către parteneri.

#### 2. Funcționalități Cheie

- Generarea de linii de cadou pornind de la partenerii selectați.
- Tipărirea etichetei de cadou (expeditor/destinatar) pentru livrare.
- Obținerea datelor despre partener (de exemplu totalul facturat în anul curent) printr-o acțiune de server.
- Copierea și modificarea în masă a cadourilor.

#### 3. Dependențe

- `contacts`

#### 4. Componente Cheie

Conform regulilor de ingestie, secțiunea „Sumar" și „Funcționalități Cheie" au fost preluate din `readme/DESCRIPTION.md`, iar analiza detaliată a codului pentru componente nu a fost solicitată explicit de acesta. Pentru orientare, structura modulului include: modele în `models/`, vizualizări în `views/` (listă/formular cadou, extindere `res.partner`, raport etichetă cadou), o acțiune de server în `data/ir_server_actions.xml` și expertizi (wizard) pentru adăugarea partenerilor și copierea cadourilor în `wizard/`.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale verificate către alte module documentate în wiki.
