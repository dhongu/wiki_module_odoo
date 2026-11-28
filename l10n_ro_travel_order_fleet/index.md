# Romania - Ordin de deplasare cu mașina unității (localizat la `l10n_ro_travel_order_fleet/index.md`)

- **Nume Tehnic:** `l10n_ro_travel_order_fleet`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_travel_order_fleet
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_travel_order_fleet`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Leagă ordinul de deplasare de flota companiei: pe ordin se alege vehiculul unității, iar foaia de parcurs se creează direct din ordin. Pentru deplasările în străinătate cu vehiculul unității, modulul tipărește și formularul 14-5-4/a, ordinul de deplasare în străinătate pentru transporturi internaționale.

#### 2. Funcționalități Cheie

- Alegerea vehiculului pe ordin; mijlocul de transport devine *Autoturismul unității* dacă era gol.
- Butonul **Creează foaia de parcurs** (pe ordinul *Aprobat* sau *În deplasare*, cu vehicul și fără foaie): foaia primește vehiculul, angajatul ca șofer și perioada ordinului (efectivă, dacă e completată, altfel planificată).
- Butonul **Foi de parcurs** pe ordin și ordinul de deplasare vizibil pe foaia de parcurs.
- Transport internațional: bifa **Transport internațional** cu numărul și emitentul comenzii de transport, locul de încărcare și cel de descărcare.
- Raportul **Ordin de deplasare în străinătate – transporturi internaționale (14-5-4/a)**: titular, țară, autovehicul, comandă, încărcare/descărcare, km pe relații din foile de parcurs, avans pentru diurnă (valută și lei) și cheltuieli, diferența de primit sau de restituit, semnături (CFP opțional).
- Meniu: **Contabilitate → Furnizori → Ordine de deplasare**; pentru foi de parcurs e nevoie de rolul **Flotă / Administrator**.
- Se instalează automat când sunt instalate ambele module de care depinde. Fluxul pas-cu-pas este în fișa consultantului.

#### 3. Dependențe

- `l10n_ro_travel_order`
- [deltatech_fleet](../deltatech_fleet/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.travel.order` (extins): vehicul, foi de parcurs, câmpurile transportului internațional și acțiunile de creare/vizualizare a foilor.
- `fleet.map.sheet` (extins): legătura către ordinul de deplasare.

**Vizualizări**

- `view_l10n_ro_travel_order_form_fleet`: vehicul, butoane și pagina *Transport internațional* pe ordin.
- `fleet_map_sheet_form_travel_order`: ordinul de deplasare pe foaia de parcurs.

**Acțiuni Automate / Acțiuni Server**

- `action_report_l10n_ro_travel_order_international`: raportul 14-5-4/a.

#### 5. Conexiuni

- `l10n_ro_travel_order_pontaj`: cealaltă punte a ordinului de deplasare (pontaj).
