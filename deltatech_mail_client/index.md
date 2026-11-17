# Mail Client (localizat la `deltatech_mail_client/index.md`)

- **Nume Tehnic:** `deltatech_mail_client`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_mail_client
- **Cale Locală:** `odoo-addons/bitshop/deltatech_mail_client`
- **Ultima Ingestie:** `2026-11-17`

#### 1. Sumar

Mail Client va fi un client de e-mail generic pentru Odoo, conectat la orice server IMAP și SMTP, astfel încât utilizatorii să poată citi și trimite e-mailurile companiei direct din Odoo. În prezent modulul este doar un placeholder (stadiu Alpha): conține manifestul, descrierea și planul de dezvoltare, iar **nu este instalabil** (`installable: False`).

#### 2. Funcționalități Cheie

Modulul nu oferă încă funcționalități. Etapele planificate (din `ROADMAP.md`); fiecare se încheie cu un modul instalabil și testat:

- **Etapa 1, nucleul de e-mail:** cont IMAP/SMTP per utilizator (fără parole în clar), listare foldere și mesaje, citire, marcare citit/cu stea, randare HTML în siguranță (cadru izolat, fără scripturi, fără resurse externe implicit).
- **Etapa 2, gestiunea folderelor:** mutarea mesajelor între foldere (IMAP `MOVE`, cu fallback `COPY` + `\Deleted` + `EXPUNGE`), într-un folder ales de utilizator, cu reîmprospătarea listei de foldere.
- **Etapa 3, redactare:** răspuns, răspuns tuturor, redirecționare, mesaje noi, trimitere de pe adresa proprie, salvare în folderul Sent.
- **Etapa 4, legătura cu documentele de business:** atașarea unui mesaj sau a anexelor la partener, comandă de vânzare sau alte documente, afișarea înregistrărilor legate de adresa expeditorului.
- **Etapa 5, securitate și audit:** rezultate SPF, DKIM, DMARC, avertizări de spoofing, jurnal de acces append-only (deschidere, trimitere, atașare).
- **Etapa 6, căsuțe partajate și notificări:** acces explicit per utilizator, notificări în Odoo la mesaje noi.
- **Etapa 7, migrare:** script de migrare de la `agroamat_mail` (setări căsuță, drepturi de acces, legături la anexe); mesajele nu se copiază, fiind citite direct de pe server.

#### 3. Dependențe

- `mail`

#### 4. Componente Cheie

**Modele**

- Niciun model definit încă (placeholder).

**Vizualizări**

- Nicio vizualizare definită încă.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- `agroamat_mail`: modul client din care este planificată migrarea setărilor (Etapa 7).
