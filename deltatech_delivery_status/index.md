# Deltatech Delivery Status (localizat la `deltatech_delivery_status/index.md`)

- **Nume Tehnic:** `deltatech_delivery_status`
- **Versiune:** `20.0.2.3.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_delivery_status
- **Cale Locală:** `odoo-addons/deltatech/deltatech_delivery_status`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)
- **Ultima Ingestie:** `2026-11-27`

#### 1. Sumar

Acest modul extinde sistemul de livrare din Odoo pentru a oferi o urmărire detaliată și o gestionare avansată a stării expedierilor. El adaugă o stare de livrare granulară pe transferurile de stoc, integrează informațiile despre starea transmise de curier cu comenzile de vânzare și permite controlul livrărilor în funcție de plată. Astfel, echipele de vânzări, depozit și clienții beneficiază de o vizibilitate clară și de informații precise privind parcursul fiecărui colet, de la pregătirea în depozit până la livrarea finală către client.

#### 2. Funcționalități Cheie

- Adaugă urmărirea detaliată a stării de livrare pe transferurile de stoc.
- Integrează informațiile de stare de la curier cu comenzile de vânzare.
- Permite gestionarea stării de livrare la nivelul echipelor de vânzări.
- Extinde furnizorii de plată cu informații privind starea de livrare.
- Suportă urmărirea coletelor prin intermediul curierilor.
- Permite monitorizarea stării de livrare pe tot parcursul procesului logistic.
- Îmbunătățește comunicarea între vânzări, depozit și clienți cu privire la starea expedierii.
- Centralizează informațiile de livrare pentru o vizibilitate mai bună în întreaga organizație.

**Blocarea livrărilor**

- **Blocare manuală a livrării:** utilizatorii pot amâna manual livrările marcând transferurile ca amânate (`postponed`); un transfer amânat nu poate fi validat (`button_validate` ridică eroare). Transferurile din comanda amânată rămân în așteptare chiar dacă produsele sunt rezervate.
- **Blocare în funcție de furnizorul de plată:** amânarea automată a livrărilor pe baza configurației furnizorului de plată. Fiecare furnizor poate fi configurat cu opțiunea „Livrare amânată" (`postponed_delivery`); când este activată, livrările sunt blocate la confirmarea comenzii, iar la trecerea tranzacției de plată în starea „efectuată" sistemul eliberează automat livrările blocate ale comenzii respective (o eroare la eliberare este înregistrată în log și nu blochează procesarea plății).
- **Configurare la nivel de echipă de vânzări:** echipele de vânzări (`crm.team`) pot fi configurate să amâne livrările pentru plata prin transfer bancar (`postpone_payment_transfer`), permițând verificarea plății înainte de expediere; aceste livrări se eliberează manual, din comandă, după încasarea plății.
- **Gestionare la nivel de comandă:** comanda de vânzare expune `postpone_delivery()` / `release_delivery()` pentru a amâna (doar transferurile nefinalizate sau neanulate), respectiv elibera, transferurile aferente, prin butoanele **Amână** / **Eliberează** și prin acțiunile de grup pe mai multe comenzi; câmpul calculat și căutabil `postponed_delivery` arată dacă cel puțin un transfer al comenzii este amânat.
- **Configurare implicită pe tip de operațiune:** un tip de transfer (`stock.picking.type`) poate fi marcat implicit „Amânat", caz în care transferurile noi create pe acel tip pornesc deja amânate. Parametrul de sistem `backorders.postponed` = `True` face același lucru pentru comenzile restante (backorder). Căi de configurare: furnizor de plată în Contabilitate → Configurare → Plăți online; echipă în Vânzări → Configurare → Echipe. Pe transferuri există filtrul „Amânat", iar pe comenzi filtrul „Livrare amânată".

**Urmărirea stării de livrare (`delivery_state`)**

Câmp cuprinzător pe transferurile de stoc care urmărește parcursul coletului prin întregul proces logistic: Ciornă, Pregătit în depozit, Pre-aviz (AWB generat, neridicat încă), În tranzit, În depozitul curierului, În livrare, Livrat și Refuzat. Suplimentar, câmpul `available_state` (calculat, stocat) indică vizual disponibilitatea produselor pentru transferurile aflate în lucru: Disponibil, Parțial disponibil sau Indisponibil (pentru transferurile livrate dintr-o dată, și rezervarea parțială înseamnă Indisponibil). Starea de livrare este actualizată de integrările cu curierii și poate fi setată și manual.

#### 3. Dependențe

- `delivery`
- `stock`
- `sales_team`
- `stock_delivery`
- `payment`

#### 4. Componente Cheie

- `stock.picking` (`models/stock_picking.py`): câmpurile `postponed`, `delivery_state`, `available_state`; `button_validate` blochează transferurile amânate, iar `_create_backorder` amână restantele dacă `backorders.postponed` este activ.
- `stock.picking.type`: câmpul `postponed` (implicit amânat pentru transferurile noi).
- `sale.order` (`models/sale.py`): `postponed_delivery` (calculat, căutabil), `postpone_delivery()`, `release_delivery()`, iar `_action_confirm` aplică regulile de amânare.
- `crm.team` (`models/sale_team.py`): `postpone_payment_transfer`.
- `payment.provider`: `postponed_delivery`; `payment.transaction` suprascrie `_set_done` pentru eliberarea automată a livrărilor.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): un comentariu din `stock_picking.py` explică faptul că sarcina cron de status livrare din [deltatech_delivery](../deltatech_delivery/index.md) marchează drept livrate transferurile fără curier alocat după o perioadă de grație, complementând câmpul `delivery_state` introdus aici.
