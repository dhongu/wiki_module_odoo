# Event Badge Numbers (localizat la `deltatech_event/index.md`)

- **Nume Tehnic:** `deltatech_event`
- **Versiune:** `19.0.0.0.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_event
- **Cale Locală:** `odoo-addons/bitshop/deltatech_event`
- **Ultima Ingestie:** `2026-10-31`

#### 1. Sumar

Acest modul îmbunătățește sistemul de management al evenimentelor din Odoo prin adăugarea unui cod scurt de bilet, tipărit mare pe insigne și pe biletele pe pagină întreagă, pentru identificarea rapidă a participanților. Din punct de vedere business, organizatorii pot recunoaște și verifica ușor participanții pe baza codului afișat, în loc să scaneze sau să citească tot codul de bare, ceea ce ajută la un eveniment mai ordonat, inclusiv la cele de mare amploare. Pe Odoo Apps modulul apare sub numele „Event Badge Numbers” (anterior „Event Insignia Numbering”).

#### 2. Funcționalități Cheie

- **Cod de bilet scurt pe insignă:** fiecare înregistrare primește un cod de bilet, preluat din ultimele caractere ale codului de bare al înregistrării, și tipărit cu litere mari, cu spații între caractere, pe insigna participantului și pe biletul pe pagină întreagă.
- **Complexitate configurabilă pe eveniment:** câmpul **Ticket Code Complexity** din formularul evenimentului (lângă formatul insignei) stabilește lungimea codului: *Low* (2 caractere), *Medium* (4), *High* (6) sau *Very High* (9). Dacă nu este ales nimic, se folosesc 2 caractere.
- **Coduri de bare cu caractere distincte:** codurile de bare noi generate pentru înregistrări au ultimele 9 caractere toate diferite, astfel încât codul scurt să fie mai ușor de citit.
- **Identificare mai ușoară a participanților:** codul de bilet apare și în formularul înregistrării, sub codul de bare.
- **Administrare simplificată:** nu necesită pași suplimentari la înregistrare; codul se calculează automat.

#### 3. Dependențe

- `event`

#### 4. Componente Cheie

*Sumarul și Funcționalitățile Cheie provin din `readme/DESCRIPTION.md`, care nu detaliază componentele tehnice; descrierea de mai sus a fost corectată după cod (vezi raportul). Mai jos sunt reperele confirmate în cod.*

**Modele**

- `event.event` (extins): câmpul selecție `code_complexity` („Ticket Code Complexity”).
- `event.registration` (extins): câmpul calculat `ticket_code` (depinde de `barcode`) și `_get_random_barcode()`, care reia generarea până când ultimele 9 caractere sunt distincte.

**Vizualizări**

- `event_event_form_inherit`: adaugă `code_complexity` după `badge_format` în formularul evenimentului.
- `event_registration_form_inherit`: adaugă `ticket_code` după `barcode` în formularul înregistrării.
- `deltatech_event_event_report_template_badge_card_inherit` și `event_report_template_full_page_ticket`: rapoarte moștenite din `event`, care tipăresc `ticket_code` cu litere mari pe insignă și pe biletul pe pagină întreagă.

#### 5. Conexiuni

Nu au fost identificate conexiuni explicite către alte module documentate în wiki.
