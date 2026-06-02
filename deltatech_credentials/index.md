# Credentials (localizat la `deltatech_credentials/index.md`)

- **Nume Tehnic:** `deltatech_credentials`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_credentials
- **Cale Locală:** `odoo-addons/deltatech/deltatech_credentials`
- **Ultima Ingestie:** `2026-06-02`

#### 1. Sumar

Modulul oferă un loc centralizat în Odoo pentru păstrarea și gestionarea acreditărilor (credențialelor) folosite la conectarea cu servicii externe. Adaugă o secțiune dedicată „Credentials" sub Setări / Utilizatori și Companii, unde administratorii pot înregistra date de autentificare precum nume de utilizator și parolă, perechi client_id / client_secret sau token-uri de acces. Scopul este să țină aceste informații sensibile la un loc, ușor de administrat, în loc să fie risipite prin diferite configurări.

#### 2. Funcționalități Cheie

- Adaugă fila/meniul „Credentials" sub Setări / Utilizatori și Companii.
- Permite definirea de acreditări pentru servicii externe, cu un cod unic de identificare.
- Suportă trei tipuri de autentificare: utilizator și parolă, client_id și client_secret (cheie API), respectiv token de acces.
- Afișează doar câmpurile relevante pentru tipul de acces selectat (parola este mascată).

#### 3. Dependențe

- `base`

#### 4. Componente Cheie

**Modele**

- `access.credentials`: Model ce stochează o acreditare pentru un serviciu extern. Conține numele, un cod, tipul de acces (`access_type`) și câmpurile aferente fiecărui tip — `username`/`password`, `client_id`/`client_secret`, respectiv `access_token`.

**Vizualizări**

- `view_access_credentials_tree`: Listă cu acreditările definite (nume și cod).
- `view_access_credentials_form`: Formular de editare a unei acreditări, cu câmpuri afișate condiționat în funcție de tipul de acces ales.
- `view_access_credentials_filter`: Vizualizare de căutare după nume.
- `action_access_credentials` / `menu_access_credentials`: Acțiunea de fereastră și elementul de meniu adăugat sub meniul de utilizatori (`base.menu_users`).

#### 5. Conexiuni

- Nu există conexiuni funcționale documentate cu alte module din wiki. Modulul furnizează modelul `access.credentials` ca infrastructură de uz general, care poate fi consumat de alte module pentru integrări cu servicii externe.
