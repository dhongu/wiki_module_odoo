# Credentials Store (localizat la `deltatech_credentials/index.md`)

- **Nume Tehnic:** `deltatech_credentials`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_credentials
- **Cale Locală:** odoo-addons/deltatech/deltatech_credentials
- **Ultima Ingestie:** `2026-10-30`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă un loc centralizat în Odoo pentru păstrarea acreditărilor folosite la conectarea cu servicii externe. În loc ca cheile API, token-urile și perechile de autentificare să fie risipite prin parametri de sistem sau fișiere de configurare, administratorii le gestionează într-un singur loc, sub **Setări → Utilizatori și companii → Credentials**. Modulul e gândit ca dependență comună pentru integrări, conectori EDI și punți API.

#### 2. Funcționalități Cheie

- Acreditări pentru orice serviciu extern, cu **Name** (obligatoriu) și un **Code** opțional, prin care alte module pot căuta înregistrarea programatic (codul nu are constrângere de unicitate în model).
- Trei tipuri de acces (**Access Type**), cu afișarea doar a câmpurilor relevante:
  - *User and password* — **Username** și **Password** (mascată în interfață);
  - *Client ID and Client Secret* — **Client Id** și **Client Secret / API key**;
  - *Access token* — **Access Token**.
- Acces rezervat implicit administratorilor (`base.group_system`); o acreditare se modifică sau se revocă din listă.
- Fișa consultant detaliază utilizarea; nu este refăcută aici.

#### 3. Dependențe

- `base`

#### 4. Componente Cheie

**Modele**

- `access.credentials`: stochează o acreditare pentru un serviciu extern — `name`, `code`, `access_type` (implicit `user`) și câmpurile aferente fiecărui tip: `username`/`password`, `client_id`/`client_secret`, `access_token`.

**Vizualizări**

- `view_access_credentials_tree`: lista acreditărilor (nume și cod).
- `view_access_credentials_form`: formularul de editare, cu câmpuri afișate condiționat după tipul de acces.
- `view_access_credentials_filter`: căutare după nume.
- `action_access_credentials` / `menu_access_credentials`: acțiunea și meniul adăugat sub `base.menu_users`.

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau acțiuni server.

#### 5. Conexiuni

- Nicio dependență a vreunui modul din suita `deltatech` nu referă acest modul în manifest; `access.credentials` e infrastructură de uz general, pe care alte module de integrare o pot consuma pentru a-și citi acreditările.
