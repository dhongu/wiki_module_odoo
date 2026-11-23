# Delivery Status in Customer Portal (localizat la `deltatech_delivery_portal/index.md`)

- **Nume Tehnic:** `deltatech_delivery_portal`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_portal
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_portal`
- **Ultima Ingestie:** `2026-11-23`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul arată clienților, direct în portalul Odoo pe care îl folosesc deja, unde se află coletul lor. În mod standard, portalul Odoo raportează starea *transferului de depozit* — odată ce transferul e validat, comanda rămâne „Expediată” indiferent ce face curierul mai departe, iar referința de urmărire apare ca un simplu link fără conținut. Acest modul înlocuiește acea informație cu starea reală a *expedierii*, preluată din statusul de livrare pe care `deltatech_delivery` îl colectează deja automat de la curieri — fără nicio configurare sau muncă suplimentară.

#### 2. Funcționalități Cheie

- Badge de status pe fiecare rând din lista de comenzi a portalului (`/my/orders`, coloana **Shipping Status**), agregat la nivelul întregii comenzi: `Delivered` apare doar când toate coletele au ajuns, iar `Shipment cancelled` doar când toate au fost anulate. Altfel decide coletul cel mai avansat care nu a fost încă livrat, în ordinea `Refused`, `Out for delivery`, `In transit`, `At the courier hub`, `Shipment registered`, `Ready for shipping`, `Preparing`; o comandă cu colete terminate diferit (unul livrat, unul anulat) afișează `Partially delivered`. Lista citește doar starea stocată pe transfer, fără apeluri către curier.
- Pe pagina comenzii, fiecare transfer de livrare are propriul card cu badge de status, transportator, AWB, ultima actualizare cu locația și un buton **Track shipment** atunci când curierul oferă un link de urmărire valid (doar URL absolut http/https).
- Secțiune extensibilă **Delivery history** sub fiecare card, cu evenimentele raportate de curier (dată, descriere, locație), cele mai recente primele — până la 10 evenimente per colet.
- Coletele nu sunt niciodată contopite: o comandă expediată în trei colete afișează trei carduri separate, fiecare cu statusul și istoricul propriu.
- Stările vizibile clientului: `Preparing`, `Ready for shipping`, `Shipment registered`, `In transit`, `At the courier hub`, `Out for delivery`, `Delivered`, `Refused`, `Shipment cancelled` și `Partially delivered`; o stare necunoscută cade pe `Shipment registered`, iar un transfer anulat se afișează ca anulat, indiferent de starea de livrare păstrată.
- Comenzile fără expediere (doar servicii) rămân cu celula de status goală, fără să sugereze o livrare care nu va avea loc niciodată.
- Verificare din backend: starea afișată în portal e cea raportată de curier și stocată pe transferul de livrare (**Inventory → Operations → Transfers**, fila *History*; *Refresh* reinterogă curierul); acțiunea planificată *Delivery: Update delivery status* (**Settings → Technical → Scheduled Actions**) face același lucru pentru toate expedierile deschise.
- Nu necesită nicio configurare proprie — este suficient ca cronul de status de livrare din `deltatech_delivery` să fie activ și ca transportatorii folosiți să suporte interogarea de status; fără el, portalul revine la starea de livrare stocată pe transfer (corectă, dar mai puțin detaliată și fără istoric de derulat). Fluxul pas-cu-pas este în fișa consultantului.

#### 3. Dependențe

- [deltatech_delivery](../deltatech_delivery/index.md)
- `sale_stock`
- `stock_delivery`

#### 4. Componente Cheie

Nu se face analiză de cod suplimentară pentru modele și acțiuni — `readme/DESCRIPTION.md` acoperă scopul modulului, iar acesta se limitează la un controller de portal (`controllers/portal.py`) și o vizualizare (`views/portal_templates.xml`) care extind paginile existente ale portalului cu informațiile de livrare colectate de `deltatech_delivery`, fără modele proprii.

**Alte componente**

- `controllers/portal.py` (`DeliveryPortal`, extinde `CustomerPortal`): suprascrie `portal_my_orders` și `portal_order_page` și adaugă în contextul QWeb badge-urile agregate pe comandă, respectiv cardurile pe transfer (citirea istoricului se face cu drepturi ridicate, doar pentru transferurile comenzii deja autorizate, iar șablonul primește dicționare simple).
- `views/portal_templates.xml`: șabloanele portalului pentru coloana de status și cardurile de livrare.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): sursa datelor de status/AWB/istoric pe care acest modul le afișează în portal; cronul lui de sincronizare trebuie activ pentru ca portalul să aibă detalii complete.
