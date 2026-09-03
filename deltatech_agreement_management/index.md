# Agreement Management (localizat la `deltatech_agreement_management/index.md`)

- **Nume Tehnic:** `deltatech_agreement_management`
- **Versiune:** `19.0.0.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_agreement_management
- **Cale Locală:** `odoo-addons/deltatech/deltatech_agreement_management`
- **Ultima Ingestie:** `2026-09-03`

#### 1. Sumar

Modulul oferă o evidență centralizată a acordurilor (contractelor) comerciale și de servicii încheiate cu partenerii companiei — număr de referință, dată, stare și tipărirea documentului direct din Odoo. Acordurile pot fi clasificate pe tipuri configurabile, fiecare tip având propria secvență de numerotare și șablon de raport, ceea ce simplifică emiterea și organizarea documentelor contractuale.

#### 2. Funcționalități Cheie

- Creare acorduri legate de un partener, cu dată a acordului și dată de expirare (opțională).
- Ciclu de viață al acordului cu trei stări: **Draft** → **In Progress** → **Terminated**; câmpurile devin needitabile odată ce acordul iese din Draft.
- Buton **Get number** (vizibil doar în Draft, cât timp referința e `/`) generează numărul de acord din secvența configurată pe tip.
- Tipurile de acord (meniu **Agreement → Configuration → Agreement types**) definesc secvența de numerotare și șablonul de raport (QWeb) folosit la tipărire; fără șablon setat, tipărirea generează eroare.
- Buton **Print** generează PDF-ul acordului folosind șablonul de raport asociat tipului.
- Butoane **Set In Progress**, **Close Contract** (→ Terminated) și **Set Draft** (reactivare) pentru tranziția între stări.
- Ștergerea unui acord e permisă doar în starea Draft; pentru In Progress/Terminated se ridică eroare de validare.
- Pe fișa partenerului: buton inteligent **Agreements** cu numărul de acorduri legate, plus filtru de căutare **With agreement** în lista de parteneri.
- Două grupuri de securitate: **Agreement / User** (vizualizare și creare acorduri, acces la butonul inteligent de pe partener) și **Agreement / Manager** (drepturi User + meniul de Configurare pentru tipuri de acord); administratorul e inclus implicit în grupul Manager.
- Urmărirea modificărilor prin firul de discuții și activitățile Odoo (mesagerie și activități) pe fiecare acord.

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
