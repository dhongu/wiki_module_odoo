# PTT Express (Memex) Shipping (localizat la `deltatech_delivery_memex/index.md`)

- **Nume Tehnic:** `deltatech_delivery_memex`
- **Versiune:** `19.0.1.0.5`
- **Cale:** `https://github.com/terrabit-ro/bitshop/tree/19.0/deltatech_delivery_memex`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_delivery_memex`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul integrează curierul PTT Express (Memex) în Odoo, permițând expedierea coletelor direct din platformă. Pe baza datelor din livrări se generează automatizat AWB-ul (scrisoarea de transport) în format PDF, fără a mai fi nevoie de operațiuni manuale în portalul curierului. Modulul acoperă scenarii uzuale de livrare precum colete multiple, valoare declarată (asigurare), ramburs și opțiuni suplimentare de livrare, fiind util companiilor care folosesc acest curier pentru livrarea către clienți.

#### 2. Funcționalități Cheie

- Generare AWB în format PDF
- Ștergere AWB
- Expediere cu colete multiple
- Expediere cu dimensiuni
- Expediere cu valoare declarată (asigurare)
- Expediere cu ramburs (cash on delivery)
- Expediere folosind numele orașului, fără id de oraș
- Opțiune de livrare sâmbăta
- Opțiune de notificare prin SMS

Funcționalități neacoperite (limitări cunoscute):

- Obținerea tarifelor pentru o expediere
- Generare AWB în format ZPL sau HTML
- Obținerea listelor de orașe, județe, lockere sau puncte de ridicare
- Obținerea istoricului de stare pentru o expediere
- Nota de retur în AWB
- Opțiunea de colet deschis
- Expediere cu id de oraș și id de județ
- Punct de ridicare doar din punctul indicat
- Trimiterea id-ului de locker în AWB

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)

Dependență externă Python: `zeep` (client SOAP pentru comunicarea cu serviciul web al curierului).

#### 4. Componente Cheie

Documentația pentru Sumar și Funcționalități Cheie a fost preluată din `readme/DESCRIPTION.md`, conform fluxului de ingestie. Analiza detaliată a componentelor tehnice (Modele, Vizualizări, Acțiuni Automate) nu a fost efectuată, deoarece Readme-ul nu o solicită explicit.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): modulul de bază pentru integrările de curierat, pe care acest modul îl extinde pentru curierul Memex.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): urmărirea stării expedierilor pentru integrările de livrare.
- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): gestionarea lockerelor pentru curierii care oferă livrare în puncte de ridicare automate.
