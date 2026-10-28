# Deltatech (localizat la `deltatech/index.md`)

- **Nume Tehnic:** `deltatech`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech
- **Cale Locală:** `odoo-addons/deltatech/deltatech`
- **Ultima Ingestie:** `2026-10-28`

#### 1. Sumar

Modulul `deltatech` este dependența tehnică de bază a întregii suite de module Deltatech pentru Odoo. Oferă extensii comune și mici îmbunătățiri de infrastructură pe care se sprijină celelalte module din suită, pentru un comportament unitar. Nu are meniuri sau fluxuri pentru utilizatorul final; este destinat dezvoltatorilor și administratorilor de sistem care întrețin suita, iar instalarea oricărui alt modul Deltatech îl aduce automat.

#### 2. Funcționalități Cheie

- Adaugă câmpul de conveniență `model_name` pe regulile de înregistrare (`ir.rule`), afișat pe formular lângă domeniu, astfel încât numele tehnic al modelului să fie vizibil direct la configurarea regulilor de acces.
- Activează widget-ul interactiv de domeniu pentru editorul domeniului din regulile de înregistrare, ceea ce reduce erorile la scrierea regulilor de acces.
- Elimină legătura externă din formularul modulului, pentru o interfață Apps mai curată în instanțele Odoo private.
- Punct unic de instalare: instalarea oricărui alt modul Deltatech îl instalează automat și pe acesta.

#### 3. Dependențe

- `web`
- `base`

#### 4. Componente Cheie

DESCRIPTION.md acoperă Sumarul și Funcționalitățile Cheie. Componentele tehnice din codul modulului sunt minimale:

**Modele**

- `ir.rule` (extins): adaugă câmpul calculat `model_name` (preluat din `model_id.model`), folosit de widget-ul de domeniu pentru a configura mai ușor regulile de înregistrare.

**Vizualizări**

- `base_view_rule_form_inherit`: extinde formularul standard de reguli de înregistrare (`base.view_rule_form`), afișează câmpul `model_name` după `model_id` și activează widget-ul `domain` pe `domain_force` (deschis în dialog).
- `module_form`: extinde formularul de modul (`base.module_form`) și elimină legătura externă din el.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server în acest modul.

#### 5. Conexiuni

- Modul fundație al suitei Deltatech: este referit ca dependență de numeroase module `deltatech_*` din monorepo. Acestea nu sunt listate aici individual.
