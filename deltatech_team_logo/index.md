# Sales Team Logo (localizat la `deltatech_team_logo/index.md`)

- **Nume Tehnic:** `deltatech_team_logo`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_team_logo
- **Cale Locală:** `odoo-addons/deltatech/deltatech_team_logo`
- **Ultima Ingestie:** `2026-11-01`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite afișarea unui logo diferit în rapoartele PDF (factură, ofertă/comandă, aviz de livrare) în funcție de echipa de vânzare a documentului. Este util pentru companiile care operează mai multe branduri sub aceeași firmă juridică: fiecare echipă de vânzare poate avea propriul logo, iar acesta este folosit automat în antetul rapoartelor. Dacă echipa nu are un logo configurat, comportamentul rămâne identic cu cel standard, folosind logo-ul firmei. Modul nou în 19.0.

#### 2. Funcționalități Cheie

- Adaugă un câmp **Logo** pe echipa de vânzare (`crm.team`), completat ca logo-ul companiei, în **Vânzări > Configurare > Echipe de vânzări**.
- La randarea raportului, dacă documentul are o echipă de vânzare cu logo propriu, se folosește acel logo; altfel (echipa fără logo sau document fără echipă) se folosește logo-ul firmei.
- Funcționează pentru oferte și comenzi de vânzare, facturi și avize/livrări provenite dintr-o comandă de vânzare; livrarea preia echipa comenzii sursă.
- Mecanism generic implementat în dispecerul `web.external_layout`, care acoperă toate variantele de layout (Standard, Striped, Boxed, Bold, Folder, Wave, Bubble) și orice document care are câmpul `team_id`.
- Fără logo pe echipă, rapoartele se tipăresc exact ca în Odoo standard.
- Pașii detaliați de configurare și utilizare sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `sale_stock`

#### 4. Componente Cheie

Readme-ul nu cere explicit detalierea componentelor; mai jos sunt cele verificate în cod.

**Modele**

- `crm.team` (extins): câmpul nou `logo` (Binary, stocat ca atașament), folosit ca antet în rapoartele emise pentru echipa respectivă.
- `stock.picking` (extins): câmpul calculat și nestocat `team_id`, derivat din comanda de vânzare sursă (`sale_id.team_id`), pentru a permite selectarea logo-ului în avize/livrări.

**Vizualizări**

- `views/crm_team_views.xml`: extinde formularul echipei de vânzare pentru a expune câmpul `logo`.
- `report/report_layout.xml`: `external_layout_team_logo` calculează `report_logo` o singură dată (logo-ul echipei, altfel cel al companiei), iar câte un template per variantă de layout (`external_layout_standard_team_logo`, ..., `external_layout_bubble_team_logo`) înlocuiește `company.logo` cu `report_logo`.

**Acțiuni Automate / Acțiuni Server**

- Nu există sarcini `ir.cron`, reguli `base.automation` sau acțiuni server definite în acest modul.

#### 5. Conexiuni

- `sale_stock`: sursa câmpurilor native `team_id` pe `sale.order` și a legăturii dintre comandă și livrare (`stock.picking`).
