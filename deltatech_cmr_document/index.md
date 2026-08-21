# CMR Document (localizat la `deltatech_cmr_document/index.md`)

- **Nume Tehnic:** `deltatech_cmr_document`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_cmr_document
- **Cale Locală:** `odoo-addons/bitshop/deltatech_cmr_document`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul permite generarea documentelor de transport CMR (scrisoarea de transport internațional de mărfuri) în format PDF direct din livrările de stoc. Pornind de la o livrare validată, utilizatorul poate tipări un document CMR completat automat cu datele necesare, ceea ce simplifică pregătirea actelor de transport pentru expedițiile interne și internaționale. Modulul este conceput cu suport pentru cerințele din România și completează automat calcule precum greutatea brută totală și volumul, pe baza produselor incluse în livrare.

#### 2. Funcționalități Cheie

- **Generare CMR**: tipărire facilă a documentului CMR din meniul de imprimare al livrării (Acțiune -> Tipărire -> Document CMR).
- **Calcule automate**: documentul calculează automat greutatea brută totală și volumul pe baza produselor din livrare.
- **Urmărire colete**: secțiunile 6, 7 și 8 afișează automat denumirile de marcaje și numere (colete), numărul de colete de destinație, respectiv modul de ambalare (tipurile de colete), pe baza liniilor de mișcare ale livrării.
- **Suport cod HS**: secțiunea 10 (numărul statistic) afișează codul HS al produsului, în scopuri statistice.
- **Loc întocmire**: secțiunea 21 afișează data programată a livrării.
- **Câmpuri suplimentare pe livrare**: adaugă pe formularul livrării câmpurile necesare:
  - **Delegat**: persoana care acționează ca reprezentant al transportatorului.
  - **Mijloc de transport**: informațiile despre vehicul (de ex. numărul de înmatriculare).
- **Suport localizare**: proiectat special cu suport pentru cerințele din România, inclusiv `l10n_ro_net_weight` pe produse.
- **Traducere după limba partenerului**: textul documentului nu mai este afișat mereu bilingv, ci se traduce în funcție de limba partenerului.

> Notă: pentru utilizatorii care nu folosesc localizarea românească, fișierul `views/additional_fields.xml` trebuie decomentat în `__manifest__.py` pentru a afișa câmpurile suplimentare pe formulare.

#### 3. Dependențe

- `base`
- `stock`
- `delivery`

#### 4. Componente Cheie

Conform fluxului de ingestie, analiza detaliată a componentelor este omisă deoarece secțiunile Sumar și Funcționalități Cheie sunt acoperite de `readme/DESCRIPTION.md`. Modulul livrează în principal rapoarte QWeb pentru documentul CMR și bonul de livrare, un format de hârtie dedicat și câmpuri suplimentare pe livrarea de stoc (delegat și mijloc de transport).

Notă tehnică (versiunea 19.0.1.0.1): câmpul `stock.picking.delegate_id` (Many2one către `res.partner`) a primit `index=True`, pentru a evita scanări secvențiale complete ale tabelei `stock_picking` la ștergerea sau unificarea partenerilor pe baze de date cu volum mare.

#### 5. Conexiuni

- `delivery`: modulul de livrare/curierat din Odoo, sursa transportatorului folosit pe document.
- `stock`: livrarea de stoc (`stock.picking`) este documentul-sursă din care se generează CMR-ul.
