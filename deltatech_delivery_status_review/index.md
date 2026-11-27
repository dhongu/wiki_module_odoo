# Sale Order Review - Held Deliveries (localizat la `deltatech_delivery_status_review/index.md`)

- **Nume Tehnic:** `deltatech_delivery_status_review`
- **Versiune:** `19.0.0.2.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_delivery_status_review
- **Cale Locală:** `odoo-addons/bitshop/deltatech_delivery_status_review`
- **Ultima Ingestie:** `2026-11-27`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul face puntea dintre verificarea comenzilor și amânarea livrărilor: dacă o comandă are un
motiv deschis pe poarta „Înainte de livrare" (ramburs mare, adresă incompletă, plată online
nefinalizată), livrările ei de ieșire sunt ținute automat în depozit — rămân în așteptare și nu
pot fi validate — până când motivul este aprobat sau se rezolvă de la sine. Nu se instalează
automat: se instalează explicit, doar acolo unde se folosește verificarea comenzilor. Nu are meniu
propriu.

#### 2. Funcționalități Cheie

- O comandă cu un motiv deschis pe poarta *Înainte de livrare* are livrările de ieșire amânate
  automat, la **fiecare pas** (pick, pack, out): rămân în *Așteptare*, iar butonul **Validează** le
  refuză. Într-un depozit cu livrare în doi sau trei pași, Odoo creează la confirmare doar pick-ul,
  iar acesta e transferul deschis de butonul inteligent **Livrare**.
- Modulul eliberează doar transferurile pe care le-a reținut el (câmp tehnic *Held by Review* pe
  transfer): un transfer amânat manual, prin setarea de backorder sau de alt modul (de ex. așteptare
  avans) rămâne amânat când motivele dispar și se eliberează prin mijlocul prin care a fost amânat.
- Amânările deja existente în `deltatech_delivery_status` (furnizor de plată cu *Postponed
  Delivery*, transfer bancar neconfirmat, butonul **Amână**) devin motive vizibile pe comandă, cu
  autor și cale de ieșire. O amânare acoperită de o regulă de plată nu primește motiv manual.
- O plată finalizată închide doar propriul motiv — livrarea este eliberată doar dacă nu mai rămâne
  niciun alt motiv deschis (ex. rambursul sau adresa). Plata e judecată după ultima tranzacție ieșită
  din ciornă: un checkout cu cardul început și abandonat după alegerea transferului bancar nu închide
  motivul *Transfer bancar neprimit*.
- Motivele se pot șterge în trei moduri echivalente, toate în istoric: **Aprobă** pe rândul motivului,
  **Aprobă verificările** (wizard cu toate motivele deschise) sau **Eliberează**.
- Butonul **Eliberează** de pe comandă deschide wizardul *Release Held Delivery* (motivele care rețin
  livrarea, poarta la care se opresc, câmpul **Notă**), în loc să ridice amânarea fără verificare;
  **Aprobă** aprobă motivele în numele utilizatorului, lasă o notă în chatter și eliberează livrarea.
  Un utilizator fără drept de aprobare pentru toate motivele primește mesajul cu lista lor, nu wizardul.
- **Eliberează livrarea** funcționează și pe mai multe comenzi selectate din listă (meniul **Acțiune**):
  comenzile pe care nu le reține nicio regulă de verificare se eliberează imediat, wizardul primește doar
  comenzile reținute, iar refuzul (dacă există un motiv neaprobabil) vine înainte de orice eliberare și
  numește comenzile de lăsat deoparte.
- Bifa **Amânată** nu poate fi debifată manual cât timp comanda are motive deschise, iar validarea e
  refuzată pe baza motivelor deschise ale comenzii, nu doar a bifei; trimiterea la curier e refuzată la fel.
  Mesajele listează transferul și motivele și trimit la **Eliberează** pe comandă.
- **Amână** pe o comandă fără probleme oprește livrarea (ex. clientul vrea să adauge un produs), cu motivul
  *Delivery postponed by <nume>*; comanda intră în coada **To Review**.
- Formularul livrării afișează panglica **POSTPONED** și un banner cu motivele de pe comandă; filtrul
  **Postponed** din lista de transferuri arată toate livrările reținute. Un utilizator de depozit fără
  drepturi de vânzări poate folosi **Amână** și vede motivele (*Inventory / User* are acces de citire).
- La instalare, livrările deja amânate prin alte mijloace primesc automat un motiv manual (*Delivery
  postponed before installing the review module*), ca să intre în coada de verificare (`post_init_hook`).
- Trei reguli de verificare, toate pe poarta *Înainte de livrare*, active implicit: *Livrare amânată de un
  operator* (aprobare manuală), *Furnizorul de plată reține livrarea* și *Transfer bancar neprimit* (ambele
  temporare, se închid la confirmarea tranzacției); se văd în *Vânzări → Configurare → Order Review Rules*.
- Configurare: pentru plăți online care trebuie să sosească înainte de expediere se bifează **Postponed
  Delivery** pe furnizorul de plată; pentru transfer bancar, **Postpone delivery for payment by transfer** pe
  echipa de vânzări; se verifică pragul și grupul de aprobare ale regulii *High cash on delivery*.
- Audit: lista motivelor pe comandă (butonul inteligent **Checks**), nota din chatter la aprobare și câmpul
  **Postponed** al transferului, urmărit în chatter.

Fluxul pas cu pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_sale_order_review](../deltatech_sale_order_review/index.md)
- [deltatech_delivery_status](../deltatech_delivery_status/index.md)

#### 4. Componente Cheie

**Modele**

- `sale.order` (extindere): adaugă logica de reținere/eliberare a livrărilor pe baza motivelor de
  verificare și butonul **Eliberează** care deschide wizardul de aprobare.
- `stock.picking` (extindere): leagă bifa **Amânată** de motivele comenzii, marchează transferurile reținute
  de verificare, refuză debifarea și **Validează** cât timp există motive deschise și afișează bannerul cu
  motivele pe formularul livrării.

**Vizualizări**

- `sale_order_views.xml`: adaugă pe formularul comenzii butonul **Eliberează** și bannerul motivelor
  care rețin livrarea.
- `stock_picking_views.xml`: adaugă pe formularul livrării panglica **Amânată** și bannerul cu
  motivele preluate de pe comanda de vânzare.

**Date**

- `review_rule_data.xml`: definește cele trei reguli de verificare pe poarta *Înainte de livrare*
  (amânare manuală, furnizor de plată cu livrare amânată, transfer bancar neprimit).

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook` (`hooks.py`): la instalare, atribuie un motiv manual livrărilor deja amânate
  prin alte mijloace, ca să intre în coada de verificare existentă.

#### 5. Conexiuni

- [deltatech_delivery_review](../deltatech_delivery_review/index.md): modul-frate opțional — dialogul „Trimite la curier" și raportul de
  validare a livrărilor numesc motivul care reține livrarea, dacă este instalat.
- `payment` (prin `deltatech_delivery_status`): tranzacțiile de plată închid motivele temporare la
  confirmare.
