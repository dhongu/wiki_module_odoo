# Deltatech (localizat la `deltatech/index.md`)

- **Nume Tehnic:** `deltatech`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech
- **Cale Locală:** `odoo-addons/deltatech/deltatech`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul `deltatech` este baza tehnică comună a suitei de module Deltatech: oferă extensii mici de infrastructură pe care se sprijină toate celelalte module. Nu are meniuri sau fluxuri pentru utilizatorul final; este o dependență tehnică pentru dezvoltatori și administratori, instalată automat odată cu orice alt modul Deltatech.

#### 2. Funcționalități Cheie

- Adaugă câmpul de conveniență `model_name` pe înregistrările de acces (`ir.access`, care înlocuiește regulile de înregistrare în Odoo 20), afișat în formular lângă widget-ul de domeniu.
- Folosește widget-ul interactiv de domeniu la editarea domeniului de acces, reducând erorile de configurare.
- Elimină linkul extern din formularul modulului, pentru o interfață Apps curată în instanțele private.
- Punct unic de instalare: orice alt modul Deltatech îl aduce automat.

#### 3. Dependențe

- `web`
- `base`

#### 4. Componente Cheie

DESCRIPTION.md acoperă Sumarul și Funcționalitățile; componentele din cod sunt minimale.

**Modele**

- `ir.access` (extins): câmpul `model_name`, înrudit cu `model_id.model`, doar citire.

**Vizualizări**

- `base_ir_access_form_view_inherit`: extinde formularul de acces (`base.ir_access_form_view`), afișează `model_name` și activează widget-ul de domeniu.
- `module_form`: ajustare a formularului de modul (`base.module_form`).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- Modul fundație al suitei: este dependență pentru numeroase module `deltatech_*`, majoritatea fără pagină wiki încă sau neinterconectate aici.
