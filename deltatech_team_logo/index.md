# Siglă pe Echipa de Vânzări (localizat la `deltatech_team_logo/index.md`)

- **Nume Tehnic:** `deltatech_team_logo`
- **Versiune:** `20.0.1.0.3`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_team_logo`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_team_logo`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

O singură firmă, mai multe mărci: în Odoo standard toate rapoartele PDF poartă aceeași siglă a companiei. Cu acest modul fiecare echipă de vânzări poate avea sigla proprie, iar facturile, ofertele, comenzile de vânzare și avizele de livrare emise pentru echipa respectivă o afișează automat în antet.

#### 2. Funcționalități Cheie

- **Siglă pe echipa de vânzări**: câmpul **Logo** pe echipă, completat ca sigla companiei (*Vânzări > Configurare > Echipe de vânzări*).
- **Folosită automat**: un document a cărui echipă are siglă se tipărește cu ea; celelalte documente păstrează sigla companiei.
- **Facturi, oferte și livrări**: funcționează pentru comenzi și oferte, facturi și avize provenite dintr-o comandă de vânzare (avizul preia echipa comenzii sursă).
- **Toate aspectele de raport**: Standard, Wave, Bubble, Folder, Center, Dual, Lines și Compact.
- **Fără siglă, nimic nu se schimbă**: o echipă fără siglă (sau un document fără echipă) tipărește ca Odoo standard.

#### 3. Dependențe

- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `crm.team` (extins): câmpul `logo` (Binary), folosit în antetul rapoartelor echipei.
- `stock.picking` (extins): câmp calculat `team_id`, derivat din comanda de vânzare sursă, pentru alegerea siglei pe avize.

**Vizualizări**

- `views/crm_team_views.xml`: extinde formularul echipei cu câmpul `logo`.
- `report/report_layout.xml`: suprascrie aspectele de raport pentru a alege sigla echipei.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- `sale_stock`: sursa echipei de vânzări (`team_id`) pe comenzi și a legăturii comandă–livrare.
