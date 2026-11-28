# Create Ticket from Errors

- **Nume Tehnic:** `deltatech_create_ticket_button`
- **Versiune:** `20.0.0.1.14`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_create_ticket_button
- **Cale Locală:** `odoo-addons/bitshop/deltatech_create_ticket_button`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaugă un buton „Open ticket” în dialogul de eroare al Odoo, astfel încât utilizatorii să poată raporta o problemă chiar în momentul apariției ei. Un singur clic deschide formularul de tichete Terrabit într-o filă nouă, deja completat cu detaliile erorii, așa că suportul primește informațiile fără întrebări suplimentare.

#### 2. Funcționalități Cheie

- Butonul **Open ticket** apare sub *See technical details*, doar pentru utilizatorii interni (utilizatorii de portal nu îl văd).
- Subiectul tichetului este mesajul erorii; descrierea conține pagina, eroarea, finalul detaliilor tehnice, numele și e-mailul utilizatorului.
- Raportul tehnic complet este copiat în clipboard (Ctrl+V / Cmd+V), ca să nu se piardă când descrierea e scurtată; utilizatorul adaugă doar ce făcea.
- Nu are setări și nu adaugă meniuri; utilizatorii care raportează trebuie să aibă e-mail pe fișa de utilizator.
- Pe o copie de test (neutralizată), butonul deschide formularul de staging Terrabit, ca testele să nu devină tichete reale.

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

**Modele**

- `ir.http` (extins): adaugă în informațiile de sesiune datele necesare formularului de tichet (nume, e-mail).

**Vizualizări**

- `error_dialog.xml` / `error_dialog.esm.js` (assets backend): butonul Open ticket în dialogul de eroare.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- Nu are conexiuni funcționale cu alte module din wiki; se conectează la formularul de tichete de pe site-ul Terrabit.
