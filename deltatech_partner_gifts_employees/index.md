# Employee Gifts (Cadouri pentru angajați)

- **Nume Tehnic:** `deltatech_partner_gifts_employees`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_partner_gifts_employees
- **Cale Locală:** `odoo-addons/bitshop/deltatech_partner_gifts_employees`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Modulul extinde gestiunea cadourilor pentru parteneri ([deltatech_partner_gifts](../deltatech_partner_gifts/index.md)) cu angajații din modulul HR. Permite planificarea rapidă a cadourilor pentru angajați, fie pentru o selecție din listă, fie pentru toți angajații companiei, fără introducere manuală a fiecărei linii. Astfel, programele de recunoaștere și beneficii pentru angajați sunt administrate centralizat, cu evidență clară a cadourilor atribuite.

#### 2. Funcționalități Cheie

- Atribuirea de cadouri angajaților printr-un wizard dedicat, în câteva clicuri.
- Două moduri de lucru: acțiunea „Add to gifts" din lista de angajați (pentru angajații selectați) și meniul „Add all employees" din meniul principal al cadourilor (toți angajații companiilor active).
- În wizard se alege tipul cadoului (Calendar, Simple, Medium, VIP), data cadoului, tipul de transport (Carrier, Logistics, Sales, Service) și motivul (implicit „Employee").
- Pentru fiecare angajat se creează o linie de cadou în stare ciornă, cu partenerul = contactul de lucru al angajatului, utilizatorul curent ca responsabil, iar etichetele se recalculează automat.
- Dacă un angajat nu are contact de lucru (adresă), operațiunea este oprită cu un mesaj de eroare.
- Acces limitat la grupul de administratori ai cadourilor.
- Stadiu: Beta; modul comercial (licență OPL-1).

#### 3. Dependențe

- [deltatech_partner_gifts](../deltatech_partner_gifts/index.md)
- `hr`

#### 4. Componente Cheie

**Modele**

- `add.employees.wizard`: model tranzitoriu pentru crearea în masă a liniilor `partner.gift.line` pentru angajați.

**Vizualizări**

- `add_employees_wizard_form`: formularul wizardului (tip cadou, dată, tip transport, motiv).

**Acțiuni Automate / Acțiuni Server**

- `action_employees_wizard`: acțiune „Add to gifts", legată de lista `hr.employee`.
- `action_add_all_employees_wizard`: acțiune „Add all employees", accesibilă din meniul cadourilor (`menu_add_employees_gifts_wizard`).

#### 5. Conexiuni

- [deltatech_partner_gifts](../deltatech_partner_gifts/index.md): modulul de bază; liniile de cadou și meniul părinte provin de acolo.
- `hr`: sursa angajaților.
