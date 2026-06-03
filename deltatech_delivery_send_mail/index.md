# Deltatech Delivery Send Mail (localizat la `deltatech_delivery_send_mail/index.md`)

- **Nume Tehnic:** `deltatech_delivery_send_mail`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-ro/bitshop/tree/19.0/deltatech_delivery_send_mail
- **Cale Locală:** `odoo-addons/bitshop/deltatech_delivery_send_mail`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul îmbunătățește satisfacția și transparența față de client prin trimiterea automată de notificări pe email atunci când etichetele de expediere (AWB) sunt generate sau când coletele sunt ridicate de curier. Din perspectivă de business, această comunicare automată reduce volumul de întrebări de tip „Unde este comanda mea?", deoarece clienții sunt informați în timp real despre statusul exact al livrării lor.

#### 2. Funcționalități Cheie

- Experiență îmbunătățită pentru client: informarea proactivă a clienților despre progresul livrării comenzii.
- Costuri de suport reduse: diminuarea volumului de muncă manuală al echipei de relații clienți prin automatizarea actualizărilor de status de rutină.
- Transparență în timp real a expedierii: notificarea imediată a clienților odată ce comanda este împachetată și pregătită pentru transport.
- Încredere sporită în brand: consolidarea încrederii prin actualizări logistice consistente și automate pe parcursul ciclului de onorare a comenzii.
- Comunicare scalabilă: gestionarea automată a notificărilor de expediere pentru un volum mare de comenzi zilnice.

#### 3. Dependențe

- `delivery`
- [deltatech_delivery_status](../deltatech_delivery_status/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile de „Componente Cheie" sunt omise deoarece modulul dispune de un fișier `readme/DESCRIPTION.md` care acoperă scopul și funcționalitățile, fără a solicita explicit detalierea componentelor tehnice.

#### 5. Conexiuni

- [deltatech_delivery_status](../deltatech_delivery_status/index.md): furnizează statusurile de livrare pe baza cărora se declanșează notificările pe email (AWB generat / colet ridicat).
- [deltatech_delivery](../deltatech_delivery/index.md): modul înrudit din ecosistemul Deltatech de gestiune a livrărilor și a curieratului.
