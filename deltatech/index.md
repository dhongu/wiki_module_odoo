# Deltatech (localizat la `deltatech/index.md`)

- **Nume Tehnic:** `deltatech`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech
- **Cale Locală:** `odoo-addons/deltatech/deltatech`
- **Ultima Ingestie:** `2026-06-01`

#### 1. Sumar

Modulul `deltatech` este componenta de bază (fundație) a suitei de module Deltatech pentru Odoo. Rolul său principal este să ofere utilitare comune, structuri partajate și o convenție unitară care asigură consistența și interoperabilitatea între toate funcționalitățile dezvoltate de Deltatech. În mod normal nu necesită configurare directă din partea utilizatorului final și se instalează automat ca dependență tehnică atunci când este adăugat orice alt modul din suita Deltatech.

#### 2. Funcționalități Cheie

- Utilitare și helpere partajate pentru gestionarea și validarea consistentă a datelor, plus un cadru standard pentru extinderea modelelor de bază Odoo.
- Consistență la nivel de suită: impune o convenție comună de denumire și o structură unitară pentru toate modulele Deltatech, simplificând instalarea și administrarea trusei de instrumente.
- Funcționează ca dependență centrală pentru module mai avansate din suită.
- Punct comun pentru comunicarea și schimbul de date între diferitele module Deltatech.

#### 3. Dependențe

- `web`
- `base`

#### 4. Componente Cheie

DESCRIPTION.md acoperă Sumarul și Funcționalitățile Cheie. Pentru completitudine, componentele tehnice efective prezente în codul modulului de bază sunt minimale:

**Modele**

- `ir.rule` (extins): adaugă câmpul calculat `model_name` (preluat din `model_id.model`), folosit pentru a configura mai ușor regulile de înregistrare prin widget-ul de domeniu.

**Vizualizări**

- `base_view_rule_form_inherit`: extinde formularul standard de reguli de înregistrare (`base.view_rule_form`), afișează câmpul `model_name` și activează widget-ul `domain` pe `domain_force`.
- `module_form`: ajustare a formularului de modul (`base.module_form`).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server în acest modul.

#### 5. Conexiuni

- Modul fundație al suitei Deltatech: este referit ca dependență de numeroase module `deltatech_*` din monorepo. Aceste module nu au încă pagină wiki, deci nu sunt incluse aici ca link-uri active.
