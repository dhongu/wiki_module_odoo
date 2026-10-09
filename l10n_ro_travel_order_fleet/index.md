# Romania - Ordin de deplasare cu mașina unității (localizat la `l10n_ro_travel_order_fleet/index.md`)

- **Nume Tehnic:** `l10n_ro_travel_order_fleet`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_travel_order_fleet
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_travel_order_fleet`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Leagă ordinul de deplasare de flota unității: pe ordin se alege vehiculul, iar din el se creează direct foaia de parcurs. În plus, pentru deplasările în străinătate cu vehiculul unității (transporturi internaționale de marfă) modulul tipărește formularul „Ordin de deplasare în străinătate – transporturi internaționale” (14-5-4/a). Se instalează automat când sunt prezente ambele module de care depinde.

#### 2. Funcționalități Cheie

- Alegerea vehiculului unității pe ordinul de deplasare; mijlocul de transport devine *Autoturismul unității*.
- Butonul **Creează foaia de parcurs**, disponibil după aprobare: deschide foaia cu vehiculul, angajatul ca șofer și perioada ordinului (cea efectivă, dacă e completată, altfel cea planificată). Traseele și alimentările se completează apoi ca de obicei.
- Butonul **Foi de parcurs** pe ordin listează foile legate; pe foaia de parcurs apare ordinul de deplasare.
- Opțiunea **Transport internațional** (pentru ordine „În străinătate”), cu pagina dedicată: comanda de transport (număr și emitent), locul de încărcare și locul de descărcare.
- Raportul **Ordin de deplasare în străinătate – transporturi internaționale (14-5-4/a)** (din *Tipărire*): titularul de avans, țara, autovehiculul (număr și marcă), scopul, comanda, încărcarea/descărcarea, plecarea și înapoierea, tabelul km pe relații (din foile de parcurs), avansul în valută și în lei pentru diurnă și cheltuieli, diferența de primit sau de restituit și semnăturile (CFP opțional, ca la 14-5-4).

#### 3. Dependențe

- `l10n_ro_travel_order`
- [deltatech_fleet](../deltatech_fleet/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.travel.order` (extins): câmpurile `vehicle_id`, `map_sheet_ids`, `international_transport`, `cargo_order_ref`, `cargo_order_issuer`, `loading_place`, `unloading_place`; acțiunile `action_create_map_sheet` și `action_view_map_sheets`.
- `fleet.map.sheet` (extins): legătura `l10n_ro_travel_order_id` către ordinul de deplasare.

**Vizualizări**

- `view_l10n_ro_travel_order_form_fleet`: extinde formularul ordinului cu vehicul, butoane și pagina „Transport internațional”.
- `fleet_map_sheet_form_travel_order`: afișează ordinul de deplasare pe foaia de parcurs.

**Acțiuni Automate / Acțiuni Server**

- `action_report_l10n_ro_travel_order_international`: raportul QWeb 14-5-4/a (nu există cron sau acțiuni server).

#### 5. Conexiuni

- `l10n_ro_travel_order`: modulul de bază al ordinelor de deplasare (încă fără pagină wiki).
