# Deltatech Team Logo (localizat la `deltatech_team_logo/index.md`)

- **Nume Tehnic:** `deltatech_team_logo`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_team_logo
- **Cale Locală:** `odoo-addons/deltatech/deltatech_team_logo`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul permite afișarea unui logo diferit în rapoartele PDF (factură, ofertă/comandă, aviz de livrare) în funcție de echipa de vânzare a documentului. Este util pentru companiile care operează mai multe branduri sub aceeași firmă juridică: fiecare echipă de vânzare poate avea propriul logo, iar acesta este folosit automat în antetul rapoartelor. Dacă echipa nu are un logo configurat, comportamentul rămâne identic cu cel standard, folosind logo-ul firmei.

#### 2. Funcționalități Cheie

- Adaugă un câmp **Logo** pe echipa de vânzare (`crm.team`).
- La randarea raportului, dacă documentul are o echipă de vânzare cu logo propriu, se folosește acel logo; altfel se folosește logo-ul firmei.
- Mecanism generic implementat în dispecerul `web.external_layout`, care acoperă toate variantele de layout (standard, striped, boxed, bold, folder, wave, bubble) și orice document care are câmpul `team_id`:
  - `sale.order` (ofertă/comandă) — `team_id` nativ.
  - `account.move` (factură) — `team_id` nativ.
  - `stock.picking` (aviz/livrare) — `team_id` calculat din comanda sursă.

#### 3. Dependențe

- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `crm.team` (extins): primește un câmp nou `logo` (Binary), folosit ca antet în rapoartele emise pentru echipa de vânzare respectivă.
- `stock.picking` (extins): primește un câmp calculat `team_id`, derivat din comanda de vânzare sursă (`sale_id.team_id`), pentru a permite selectarea logo-ului în avizele/livrările de marfă.

**Vizualizări**

- `views/crm_team_views.xml`: extinde formularul echipei de vânzare pentru a expune câmpul `logo`.

**Acțiuni Automate / Acțiuni Server**

- Nu există sarcini `ir.cron`, reguli `base.automation` sau acțiuni server definite în acest modul. Personalizarea de antet se face prin override-ul layout-ului de raport (`report/report_layout.xml`).

#### 5. Conexiuni

- `sale_stock`: sursa câmpurilor native `team_id` pe `sale.order` și a legăturii dintre comandă și livrare (`stock.picking`).
