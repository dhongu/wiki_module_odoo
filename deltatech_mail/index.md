# Mail Substitution (localizat la `deltatech_mail/index.md`)

- **Nume Tehnic:** `deltatech_mail`
- **Versiune:** `20.0.1.0.8`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_mail
- **Cale Locală:** `odoo-addons/deltatech/deltatech_mail`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Bazele de test și de instruire nu trebuie să trimită emailuri reale clienților. Modulul redirecționează emailurile de ieșire către altă adresă, stabilește expeditorul și rescrie texte în mesajele postate.

#### 2. Funcționalități Cheie

- **Redirecționare destinatari**: o regulă *Receiver* trimite emailurile modelului ales (*Related Document Model*) la adresa din *Substitution* în loc de destinatarii reali și elimină copiile CC; fără model, redirecționează toate emailurile.
- **Expeditor fix**: o regulă *Sender* stabilește adresa ca expeditor al emailurilor potrivite; se aplică prima regulă potrivită.
- **Expeditor companie**: dacă parametrul de sistem `mail.use_company_email` este `True`, mesajele postate și emailurile din coadă pleacă de la adresa companiei; postarea este refuzată dacă firma nu are email.
- **Înlocuire text în corp**: în **Body Substitution**, textul *Body Part* este înlocuit cu *Substitution* în mesajele postate pe orice înregistrare; mesajele deja postate nu se schimbă.
- Regulile se gestionează în mod dezvoltator, la **Settings → Technical → Email**, și se aplică tuturor utilizatorilor și companiilor; doar administratorii le modifică. O regulă *Receiver* fără model trebuie ștearsă înainte de producție.

#### 3. Dependențe

- `mail`

#### 4. Componente Cheie

**Modele**

- `mail.substitution`: regulile de destinatar/expeditor.
- `mail.body.substitution`: regulile de înlocuire a textului din corpul mesajelor.
- `mail.mail` (extins): aplică substituțiile la trimitere și la pregătirea listei de destinatari.
- `mail.thread` (extins): `message_post()` și `_message_compute_author()` pentru înlocuirea textului și expeditorul companiei.
- `res.config.settings` (extins).

**Vizualizări**

- `mail_substitution_tree`, `mail_substitution_form`, `mail_body_substitution_tree`: listele și formularul regulilor; acțiunile `action_mail_substitution` și `action_mail_body_substitution`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

Nu au fost identificate module conexe cu pagină wiki.
