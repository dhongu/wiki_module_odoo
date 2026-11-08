# Mail Substitution (localizat la `deltatech_mail/index.md`)

- **Nume Tehnic:** `deltatech_mail`
- **Versiune:** `19.0.1.0.7`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_mail
- **Cale Locală:** `odoo-addons/deltatech/deltatech_mail`
- **Ultima Ingestie:** `2026-11-08`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite filtrarea emailurilor și redirecționarea lor către o altă adresă. Este util mai ales pe bazele de date de test sau de instruire, unde clienții și furnizorii nu trebuie să primească mesajele reale, dar și pentru centralizarea corespondenței către un alt destinatar. Poate înlocui și expeditorul, poate corecta automat texte din mesajele postate și poate trimite mesajele de pe adresa de email a companiei.

#### 2. Funcționalități Cheie

- Regulile se gestionează în modul dezvoltator, la **Setări → Tehnic → Email**, și se aplică tuturor utilizatorilor și companiilor din baza de date.
- **Substituție email** (tip *Destinatar* sau *Expeditor*), opțional pe un anumit model de document; fără model, regula se aplică tuturor emailurilor:
  - *Receiver* înlocuiește toți destinatarii emailului și elimină copiile CC, deci destinatarii originali nu sunt contactați;
  - *Sender* înlocuiește expeditorul.
- Pe bazele de test se recomandă o regulă generică *Receiver*, care se șterge înainte de trecerea în producție.
- **Substituție în corpul mesajelor**: textul din *Body Part* este înlocuit cu textul din *Substitution* în fiecare mesaj postat din chatter; mesajele deja postate nu se modifică.
- **Email companie ca expeditor**: cu parametrul de sistem `mail.use_company_email` setat pe `True` (**Setări → Tehnic → Parametri → Parametri de sistem**), mesajele postate și emailurile din coadă pleacă de pe adresa de email a companiei autorului; un expeditor explicit (email primit, șablon) se păstrează. Compania trebuie să aibă adresă de email, altfel postarea mesajului este refuzată.
- **Securitate** (din versiunea `19.0.1.0.7`): doar administratorii (*Administrare: Setări*) pot crea sau modifica regulile; utilizatorii interni le pot doar citi. Înainte, orice utilizator intern putea adăuga o regulă *Receiver* care redirecționa toate emailurile bazei de date. Substituțiile din corp se citesc cu `sudo` la postare, deci se aplică și autorilor fără acces la reguli (ex. portal).

#### 3. Dependențe

- `mail`

#### 4. Componente Cheie

**Modele**

- `mail.substitution`: regulă de substituție a destinatarului sau expeditorului (model document, adresă, tip).
- `mail.body.substitution`: regulă de înlocuire a unui text din corpul mesajelor postate.
- `mail.mail` (extins): aplică substituțiile la trimitere (`_prepare_outgoing_list`, `send`).
- `mail.thread` (extins): aplică substituțiile de corp în `message_post` și expeditorul companiei în `_message_compute_author`.
- `res.config.settings` (extins): opțiunea de email al companiei ca expeditor.

**Vizualizări**

- `mail_substitution_tree` / `mail_substitution_form`: lista și formularul regulilor de substituție email.
- `mail_body_substitution_tree`: lista regulilor de substituție în corpul mesajelor.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește acțiuni automate sau acțiuni server. Acțiunile de fereastră `action_mail_substitution` și `action_mail_body_substitution` deschid listele de reguli.

#### 5. Conexiuni

Nu au fost identificate conexiuni către alte module cu pagină wiki existentă.
