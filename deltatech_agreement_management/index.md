# Agreement Management (localizat la `deltatech_agreement_management/index.md`)

- **Nume Tehnic:** `deltatech_agreement_management`
- **Versiune:** `19.0.0.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_agreement_management
- **Cale Locală:** `odoo-addons/deltatech/deltatech_agreement_management`
- **Ultima Ingestie:** `2026-06-01`

#### 1. Sumar

Modulul oferă o evidență centralizată a acordurilor (contractelor) încheiate cu partenerii companiei. Permite gestionarea numerelor, datelor și stărilor acordurilor, astfel încât echipa să poată urmări într-un singur loc situația documentelor contractuale. Acordurile pot fi clasificate pe tipuri configurabile, fiecare tip având propria secvență de numerotare și șablon de raport, ceea ce simplifică emiterea și organizarea documentelor.

#### 2. Funcționalități Cheie

- Gestionarea acordurilor: număr, dată și stare.
- Configurarea tipurilor de acord, fiecare cu secvență proprie de numerotare și șablon de raport.
- Integrare cu partenerii (`res.partner`), pentru a lega acordurile de contacte/clienți.
- Urmărirea modificărilor prin firul de discuții și activitățile Odoo (mesagerie și activități).

#### 3. Dependențe

- `base`
- `mail`

#### 4. Componente Cheie

**Modele**

- `general.agreement`: Modelul principal de acord; integrează `mail.thread` și `mail.activity.mixin` pentru urmărirea istoricului și a activităților.
- `general.agreement.type`: Tipul de acord configurabil (secvență de numerotare și șablon de raport).
- `res.partner` (extins): Adaugă legătura dintre parteneri și acorduri.

**Vizualizări**

- `views/agreement.xml`: Interfețele pentru acorduri și tipurile de acord.
- `views/res_partner.xml`: Extinderea formularului de partener cu informații legate de acorduri.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale către alte module cu pagină wiki existentă.
