# Credentials Store (localizat la `deltatech_credentials/index.md`)

- **Nume Tehnic:** `deltatech_credentials`
- **Versiune:** `20.0.1.0.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_credentials
- **Cale Locală:** `odoo-addons/deltatech/deltatech_credentials`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă un loc centralizat în Odoo pentru păstrarea și gestionarea acreditărilor folosite la conectarea cu servicii externe. În loc ca cheile API, token-urile și perechile de autentificare să fie risipite prin parametri de sistem sau fișiere de configurare, administratorii le țin la un loc, în *Settings > Users & Companies > Credentials*.

#### 2. Funcționalități Cheie

- Acreditări pentru orice serviciu extern, cu nume descriptiv (obligatoriu) și cod opțional, pe care alte module îl pot folosi pentru a găsi înregistrarea.
- Trei tipuri de acces: utilizator și parolă, „Client Id" și „Client Secret / API key", respectiv token de acces; se afișează doar câmpurile relevante tipului ales.
- Parola este mascată în interfață.
- Acces rezervat implicit administratorilor Odoo (`base.group_system`).
- Gândit ca dependență comună: modulele de integrare pot consulta programatic înregistrările `access.credentials`, ținând secretele în afara setărilor de modul.

#### 3. Dependențe

- `base`

#### 4. Componente Cheie

**Modele**

- `access.credentials`: stochează o acreditare (nume, cod, `access_type` și câmpurile aferente fiecărui tip).

**Vizualizări**

- `view_access_credentials_tree`: listă cu acreditările definite.
- `view_access_credentials_form`: formular cu câmpuri condiționate de tipul de acces.
- `view_access_credentials_filter`: căutare după nume.
- `action_access_credentials`: acțiunea de fereastră, cu meniu sub *Users & Companies*.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- Nu există conexiuni funcționale documentate cu alte module din wiki. Modelul `access.credentials` este infrastructură de uz general, consumabilă de alte module pentru integrări cu servicii externe.
