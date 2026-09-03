# Delivery Status in Customer Portal (localizat la `deltatech_delivery_portal/index.md`)

- **Nume Tehnic:** `deltatech_delivery_portal`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_portal
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_portal`
- **Ultima Ingestie:** `2026-09-03`

#### 1. Sumar

Modulul arată clienților, direct în portalul Odoo pe care îl folosesc deja, unde se află coletul lor. În mod standard, portalul Odoo raportează starea *transferului de depozit* — odată ce transferul e validat, comanda rămâne "Expediată" indiferent ce face curierul mai departe, iar referința de urmărire apare ca un simplu link fără conținut. Acest modul înlocuiește acea informație cu starea reală a *expedierii*, preluată din statusul de livrare pe care `deltatech_delivery` îl colectează deja automat de la curieri — fără nicio configurare sau muncă suplimentară.

#### 2. Funcționalități Cheie

- Badge de status pe fiecare rând din lista de comenzi a portalului (`/my/orders`), agregat la nivelul întregii comenzi: dacă o comandă e împărțită pe mai multe colete, badge-ul reflectă coletul cel mai puțin avansat — `Delivered` apare doar când toate coletele au ajuns, iar o comandă cu colete în stări diferite (unul livrat, unul anulat) afișează `Partially delivered`.
- Pe pagina comenzii, fiecare transfer de livrare are propriul card cu badge de status, transportator, AWB și un buton **Track shipment** atunci când curierul oferă un link de urmărire.
- Secțiune extensibilă **Delivery history** sub fiecare card, cu evenimentele raportate de curier (dată, descriere, locație), cele mai recente primele — până la 10 evenimente per colet.
- Coletele nu sunt niciodată contopite: o comandă expediată în trei colete afișează trei carduri separate, fiecare cu statusul și istoricul propriu.
- Stările vizibile clientului: `Preparing`, `Ready for shipping`, `Shipment registered`, `In transit`, `At the courier hub`, `Out for delivery`, `Delivered`, `Refused`, `Shipment cancelled` și `Partially delivered`.
- Comenzile fără expediere (doar servicii) rămân cu celula de status goală, fără să sugereze o livrare care nu va avea loc niciodată.
- Nu necesită nicio configurare proprie — este suficient ca cronul de status de livrare din `deltatech_delivery` să fie activ (*Settings → Technical → Scheduled Actions*) și ca transportatorii folosiți să suporte interogarea de status; fără el, portalul revine la starea de livrare stocată pe transfer (corectă, dar mai puțin detaliată și fără istoric de derulat).

#### 3. Dependențe

- [deltatech_delivery](../deltatech_delivery/index.md)
- `sale_stock`
- `stock_delivery`

#### 4. Componente Cheie

Nu se face analiză de cod suplimentară — `readme/DESCRIPTION.md` acoperă complet scopul modulului, iar acesta se limitează la un controller de portal (`controllers/portal.py`) și o vizualizare (`views/portal_templates.xml`) care extind paginile deja existente ale portalului cu informațiile de livrare colectate de `deltatech_delivery`, fără modele proprii.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): sursa datelor de status/AWB/istoric pe care acest modul le afișează în portal; cronul lui de sincronizare trebuie activ pentru ca portalul să aibă detalii complete.
