# Delivery Route Driver (Șofer rută de livrare)

- **Nume Tehnic:** `deltatech_delivery_route_driver`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_delivery_route_driver
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_delivery_route_driver`
- **Ultima Ingestie:** `2026-11-27`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Partea de șofer a planificatorului de rute de livrare: șoferul deschide pe telefon opririle zilei, în ordinea planificată, și confirmă pe loc fiecare predare sau refuz. Dispecerul vede pe lot, cât timp vehiculul e pe drum, ce s-a livrat, ce s-a refuzat și ce a mai rămas. Șoferul este utilizator de portal, deci nu are nevoie de licență internă. Modulul este pe 20.0 (Beta, licență OPL-1, preț 120 EUR).

#### 2. Funcționalități Cheie

- **Rutele mele** în portal: loturile lansate în care utilizatorul este șofer, cu data, vehiculul, kilometrii și contoarele de opriri de livrat, livrate și refuzate.
- **Opriri în ordinea planificată**: sosirea planificată, clientul, adresa, telefonul (apel dintr-o atingere), greutatea și referința livrării.
- **Navigare**: Google Maps și Waze către fiecare oprire (la coordonate, altfel la adresă) și Google Maps prin opririle rămase de livrat, în ordine.
- **Predat**: cine a primit marfa (obligatoriu), semnătura pe ecran (în câmpul standard *Semnătură* al livrării, cu bonul de livrare semnat atașat), până la trei fotografii și poziția telefonului, citită doar la confirmare. Transferul în sine nu este validat.
- **Refuzat**: motiv dintr-o listă configurabilă (patru motive create la instalare: avarie în transport, mărime greșită, client absent, șantier nepregătit), notă și fotografii; se programează o activitate *Livrare refuzată* pentru responsabilul lotului, care face returul.
- **În back office**: starea predării pe fiecare livrare și în lista de transferuri a lotului, contoarele pe lot, filtrul *Refuzat la predare* și butonul *Resetare predare*, care permite șoferului să confirme din nou o oprire confirmată din greșeală.
- **Configurare**: motivele de refuz în *Inventar → Configurare → Gestiunea depozitului → Motive de refuz*; acces de portal pe contactul șoferului (*Acțiune → Acordă acces la portal*); șoferul este setat pe vehicul (*Flotă → Vehicul*), iar loturile create de planificator îl preiau.

Fluxul detaliat pas cu pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_delivery_route_planner](../deltatech_delivery_route_planner/index.md)
- `portal`

#### 4. Componente Cheie

**Modele**

- `delivery.route.refusal.reason`: motivele de refuz alese de șofer (ordonabile, arhivabile); utilizatorii de stoc au citire, managerii acces complet.
- Extinderi: `stock.picking` (starea predării, cel care a primit, ora și poziția confirmării, motivul și nota de refuz, resetare) și `stock.picking.batch` (contoarele de opriri de livrat, livrate, refuzate).

**Vizualizări**

- `stock_picking_batch_form` și `stock_picking_batch_tree`: grupul *Predare* și contoarele pe lot.
- `view_picking_form`, `stock_picking_view_batch_tree_ref`, `view_picking_internal_search`: grupul *Predare* pe livrare, coloana de stare în fila *Transferuri* și filtrul *Refuzat la predare*.
- `delivery_route_refusal_reason_list` / `delivery_route_refusal_reason_search`: lista motivelor de refuz.
- Șabloane de portal: `portal_my_routes`, `portal_my_route`, `portal_my_route_stop` (plus `portal_breadcrumbs`), cu intrarea `portal_driver_routes` în pagina de start; interacțiuni JS în `static/src/interactions/`.

**Acțiuni Automate / Acțiuni Server**

- `action_delivery_route_refusal_reason` (meniul *Motive de refuz*). Nu există acțiuni programate; la refuz se programează o activitate pe lot.

#### 5. Conexiuni

- [deltatech_delivery_route_planner](../deltatech_delivery_route_planner/index.md): creează loturile pe vehicul și zi, cu ordinea opririlor și sosirea planificată pe care șoferul le parcurge; este și dependență.
- `fleet`: șoferul lotului provine din vehicul.
