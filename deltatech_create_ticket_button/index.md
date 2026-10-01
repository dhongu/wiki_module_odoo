# Error Dialog (Create Ticket Button)

- **Nume Tehnic:** `deltatech_create_ticket_button`
- **Versiune:** `19.0.0.1.8`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_create_ticket_button
- **Cale Locală:** `odoo-addons/bitshop/deltatech_create_ticket_button`
- **Ultima Ingestie:** `2026-10-01`

#### 1. Sumar

Modulul adaugă un buton „Open ticket" direct în fereastra de eroare a Odoo, astfel încât utilizatorul să poată raporta problema imediat, în momentul în care apare. Butonul deschide într-o filă nouă pagina de suport Terrabit, ceea ce scurtează timpul dintre apariția unei erori și raportarea ei către echipa de suport.

#### 2. Funcționalități Cheie

- Buton „Open ticket" afișat în dialogul de eroare, sub butonul existent de tip link (de exemplu „Close"), cu un singur clic până la raportare.
- Butonul deschide într-o filă nouă adresa de suport `https://www.terrabit.ro/helpdesk`.
- Butonul este plasat în corpul dialogului, nu în footer, pentru că pe 19.0 un al doilea buton în footer ar ascunde butonul „Close" al Odoo.
- Adresa de suport este expusă în informațiile de sesiune, atât prin cheia proprie `terrabit_support_url`, cât și prin `support_url`. Pe Enterprise, `web_enterprise` rescrie `support_url`, de aceea butonul citește mai întâi cheia proprie.
- Beneficii de afaceri: raportare rapidă a erorilor, canal direct între utilizatori și echipa de suport, date utile pentru îmbunătățirea continuă.

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

**Modele**

- `ir.http` (extins): metoda `session_info` adaugă în informațiile de sesiune cheile `terrabit_support_url` și `support_url`.

**Vizualizări**

- Template-ul QWeb `web.ErrorDialog` (extensie, `static/src/xml/error_dialog.xml`): adaugă butonul „Open ticket" după butonul `btn-link`.
- Patch OWL pe `ErrorDialog` (`static/src/js/error_dialog.esm.js`): metoda `onClickOpenTicket` deschide adresa de suport într-o filă nouă.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- Nu există legături funcționale cu alte module care au pagină wiki.

