# Agreement Management (localizat la `deltatech_agreement_management/index.md`)

- **Nume Tehnic:** `deltatech_agreement_management`
- **Versiune:** `19.0.0.0.8`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_agreement_management
- **Cale Locală:** `odoo-addons/deltatech/deltatech_agreement_management`
- **Ultima Ingestie:** `2026-11-23`

#### 1. Sumar

Modulul oferă o evidență centralizată a acordurilor (contractelor) comerciale și de servicii încheiate cu partenerii companiei — număr de referință, dată, stare și tipărirea documentului direct din Odoo. Acordurile pot fi clasificate pe tipuri configurabile, fiecare tip având propria secvență de numerotare și șablon de raport, ceea ce simplifică emiterea și organizarea documentelor contractuale.

#### 2. Funcționalități Cheie

- Creare acorduri (**Agreement → Agreements → New**) legate de un partener, cu tip, dată a acordului (implicit azi), dată de expirare (**Final Date**, opțională), descriere scurtă și monedă (implicit moneda companiei).
- Ciclu de viață al acordului cu trei stări: **Draft** → **In Progress** → **Terminated**; câmpurile devin needitabile odată ce acordul iese din Draft. Tranzițiile se fac cu butoanele **Set In Progress**, **Close Contract** (→ Terminated) și **Set Draft** (redeschidere). Bara de stare arată stările reale ale acordului.
- Buton **Get number** (vizibil doar în Draft, cât timp referința e `/`) generează numărul de acord din secvența configurată pe tip.
- Tipurile de acord (**Agreement → Configuration → Agreement types**) au listă și formular proprii și definesc: denumirea (ex. „Service Contract”, „NDA”, „Supply Agreement”), secvența de numerotare (`ir.sequence`) și, opțional, șablonul de raport QWeb (**Layout**) folosit la tipărire; fără secvență sau fără șablon, **Get number**, respectiv **Print**, generează eroare. Se configurează cel puțin un tip înainte de a crea acorduri.
- Buton **Print** generează PDF-ul acordului folosind șablonul de raport asociat tipului.
- Ștergerea unui acord e permisă doar în starea Draft; pentru In Progress/Terminated se ridică eroare de validare.
- Pe fișa partenerului: buton inteligent **Agreements** cu numărul de acorduri legate (care respectă drepturile de acces și regulile de înregistrare ale utilizatorului — fără acces se vede 0), plus filtru de căutare **With agreement** în lista de parteneri, care respectă operatorul și valoarea căutării.
- Două grupuri de securitate (în **Settings → Users**), afișate sub privilegiul „Agreements” (categoria Services): **Agreement / User** (`group_agreement_user`; vizualizare și creare acorduri, acces la butonul inteligent de pe partener) și **Agreement / Manager** (`group_agreement_manager`; drepturi User + meniul de Configurare pentru tipuri de acord); administratorul e inclus implicit în grupul Manager.
- Multi-companie: regulă de înregistrare care arată doar acordurile companiilor permise, plus verificare de consistență a companiei partenerului.
- Urmărirea modificărilor prin firul de discuții și activitățile Odoo (mesagerie și activități) pe fiecare acord.

#### 3. Dependențe

- `base`
- `mail`

#### 4. Componente Cheie

**Modele**

- `general.agreement`: Modelul principal de acord (referință, descriere, partener, companie, monedă, tip, stare, date); integrează `mail.thread` și `mail.activity.mixin` pentru urmărirea istoricului și a activităților și verifică automat consistența companiei (`_check_company_auto`).
- `general.agreement.type`: Tipul de acord configurabil (secvență de numerotare `sequence_id` și șablon de raport `print_template_id`).
- `res.partner` (extins): Adaugă legătura dintre parteneri și acorduri (numărul de acorduri și căutarea pe acesta).

**Vizualizări**

- `views/agreement.xml`: Interfețele pentru acorduri (listă, formular cu bară de stare) și pentru tipurile de acord (listă și formular proprii, în meniul de Configurare).
- `views/res_partner.xml`: Extinderea formularului de partener cu butonul inteligent **Agreements** și filtrul **With agreement** în lista de parteneri.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni `ir.cron`, reguli `base.automation` sau acțiuni server în modul.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale către alte module cu pagină wiki existentă.
