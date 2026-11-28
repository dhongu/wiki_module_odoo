# Cod scurt de bilet pe ecusoane și bilete (localizat la `deltatech_event/index.md`)

- **Nume Tehnic:** `deltatech_event`
- **Versiune:** `20.0.0.0.7`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_event
- **Cale Locală:** `odoo-addons/bitshop/deltatech_event`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă pe fiecare înscriere la eveniment un **cod scurt de bilet**, tipărit pe ecuson și pe bilet, astfel încât participanții să poată fi identificați rapid la intrare, mai ales când nu există cititor de coduri de bare. Codul este o referință ușor de citit sau de dictat, nu un identificator unic.

#### 2. Funcționalități Cheie

- **Cod de bilet din codul de bare:** codul scurt reprezintă ultimele cifre ale codului de bare al înscrierii (ex. 4021593726048 devine 6048).
- **Lungime configurabilă pe eveniment:** câmpul **Complexitate cod bilet** (*Evenimente > Evenimente*, tabul *Note și documente*, sub *Dimensiune insignă*) are valorile Mic (2), Mediu (4), Mare (6) și Foarte mare (9); codul conține doar cifre, deși etichetele vorbesc de „litere". Când câmpul e gol, codul are 2 cifre; modificarea se aplică imediat tuturor înscrierilor evenimentului.
- **Coduri de bare mai distincte:** codurile de bare se generează astfel încât ultimele 9 caractere să fie toate diferite, pentru mai puține coduri asemănătoare.
- **Tipărire pe ecuson și bilet:** codul apare cu cifre mari sub numele participantului, pe ecuson și pe biletul pe pagină întreagă (rotița de pe înscriere > *Tipăriți*). Pentru a tipări și codul de bare lângă codul QR se activează **Use Event Barcode** în *Evenimente > Configurare > Setări*.
- **Limite:** la 2 sau 4 cifre două înscrieri pot avea același cod; codul este calculat și nestocat, deci nu poate fi căutat sau filtrat; pentru căutare exactă (ex. în *Registration Desk*) se folosește codul de bare.
- Fluxul pas cu pas, cu capturi, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `event`

#### 4. Componente Cheie

*Informațiile pentru această secțiune au fost preluate din `readme/DESCRIPTION.md`, care nu detaliază componentele tehnice; la verificarea rapidă a codului s-au confirmat elementele de mai jos.*

**Modele**

- `event.event` (extindere): câmpul `code_complexity` (Complexitate cod bilet).
- `event.registration` (extindere): câmpul calculat `ticket_code` și suprascrierea `_get_random_barcode`.

**Vizualizări**

- `event_event_form_inherit` și `event_registration_form_inherit` (`views/event_view.xml`): afișează complexitatea pe eveniment și codul de bilet pe înscriere.
- `report/event_event_template.xml`: extinde șabloanele de ecuson și de bilet pe pagină întreagă din `event` cu codul scurt.

#### 5. Conexiuni

Nu au fost identificate conexiuni explicite către alte module documentate în wiki.
