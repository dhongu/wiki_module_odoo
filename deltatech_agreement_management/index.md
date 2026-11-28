# Agreement Management (localizat la `deltatech_agreement_management/index.md`)

- **Nume Tehnic:** `deltatech_agreement_management`
- **Versiune:** `20.0.0.0.8`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_agreement_management
- **Cale Locală:** `odoo-addons/deltatech/deltatech_agreement_management`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul gestionează acordurile comerciale și de servicii cu partenerii: numere de referință, date, stări și tipărirea documentului acordului direct din Odoo. Fiecare acord urmează un ciclu de viață simplu, iar tipul acordului stabilește secvența de numerotare și șablonul de tipărire.

#### 2. Funcționalități Cheie

- Acorduri legate de un partener, cu dată a acordului (implicit azi), dată finală opțională, descriere și monedă (implicit moneda companiei).
- Ciclu de viață: **Draft** → **In Progress** (*Set In Progress*) → **Terminated** (*Close Contract*); înapoi în ciornă cu *Set Draft*. După ieșirea din ciornă câmpurile devin doar pentru citire.
- Numărul de referință se generează din secvența tipului de acord, prin butonul **Get number**, cât timp acordul e în ciornă și referința este `/`.
- Tipărirea acordului în PDF cu raportul configurat pe tipul de acord; fără raport configurat, tipărirea dă eroare.
- Doar acordurile în ciornă pot fi șterse.
- Pe partener: buton inteligent **Agreements** cu numărul de acorduri și filtrul de căutare **With agreement**.
- Istoric și activități (chatter) pe fiecare acord.
- Configurare: tipurile de acord (denumire, secvență, raport opțional) la **Agreement → Configuration → Agreement types**; grupurile *Agreement / User* (vizualizare și creare) și *Agreement / Manager* (în plus, meniul de configurare), atribuite din **Settings → Users**.

#### 3. Dependențe

- `base`
- `mail`

#### 4. Componente Cheie

**Modele**

- `general.agreement`: modelul principal; integrează `mail.thread` și `mail.activity.mixin`.
- `general.agreement.type`: tipul de acord (secvență de numerotare și raport de tipărire).
- `res.partner` (extins): legătura dintre parteneri și acorduri.

**Vizualizări**

- `view_agreement_form`, `view_general_agreement_tree` + `action_general_agreement`: interfața acordurilor.
- `view_general_agreement_type_form`, `view_general_agreement_type_tree` + `action_general_agreement_type`: tipurile de acord.
- `view_partner_form_agreement`, `view_partner_search_agreement`: butonul inteligent și filtrul pe partener.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale către alte module cu pagină în wiki.
