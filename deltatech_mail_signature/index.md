# Mail Signature Templates (localizat la `deltatech_mail_signature/index.md`)

- **Nume Tehnic:** `deltatech_mail_signature`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_mail_signature
- **Cale Locală:** `odoo-addons/deltatech/deltatech_mail_signature`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Fără acest modul, fiecare utilizator își scrie singur semnătura din preferințe: fonturi diferite, siglă lipită sau nu, un număr de telefon vechi. Modulul păstrează **un singur șablon pe companie**, scris o dată în editorul Odoo, cu imagini și câmpuri (`{{name}}`, `{{job_title}}`, `{{phone}}`, `{{company_address}}`), și generează din el semnătura fiecărui utilizator intern. Tot ce trimite semnătura utilizatorului (chatter, oferte, facturi, Mail Client) o folosește fără alte configurări.

#### 2. Funcționalități Cheie

- Șablon pe companie, scris în editorul HTML Odoo (siglă, banner, culori, linkuri); o companie poate avea un singur șablon activ.
- Câmpuri completate cu datele utilizatorului și ale companiei: nume, funcție, e-mail, telefon, mobil (din angajat, aplicația HR), numele, site-ul, telefonul, e-mailul, adresa pe un rând și CUI-ul companiei.
- O linie în care toate câmpurile sunt goale (de exemplu „Tel: {{phone}}" la un utilizator fără telefon) nu apare deloc; recomandare: un câmp pe linie sau pe celulă de tabel.
- Un câmp necunoscut este refuzat la salvarea șablonului, cu lista câmpurilor valide (tabul *Câmpuri disponibile*).
- Buton *Generează semnăturile utilizatorilor* pe șablon (meniul *Setări > Utilizatori și companii > Șabloane de semnătură*) și *Regenerează semnătura mea* în preferințele fiecărui utilizator.
- Semnătura se reîmprospătează la schimbarea numelui, funcției sau telefonului (se poate dezactiva cu *Reîmprospătează automat*).
- Semnăturile scrise de mână nu sunt suprascrise niciodată de generarea în masă sau de reîmprospătare; editarea manuală a unei semnături generate o transformă în semnătură proprie.
- Securitate: valorile sunt escapate HTML, linkurile sunt verificate (fără `javascript:`), iar rezultatul trece prin curățarea HTML din Odoo.
- Imaginile șablonului sunt partajate, deci se văd și la destinatarii din afara Odoo (PNG, JPEG, GIF, cel mult 5 imagini de 300 KB).

Fluxul pas-cu-pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `mail`
- `html_editor`

#### 4. Componente Cheie

**Modele**

- `mail.signature.template`: șablonul de semnătură al companiei (nume, companie, `auto_refresh`, `body_html`); validează câmpurile folosite, unicitatea șablonului activ pe companie și generează semnăturile utilizatorilor.
- `res.users` (extins): regenerarea semnăturii proprii și marcarea semnăturilor generate vs. scrise de mână.
- `res.partner` (extins): reîmprospătarea semnăturii la schimbarea datelor utilizatorului.

**Vizualizări**

- `mail_signature_template_view_list` / `_form` / `_search`: lista, formularul (editor, buton de generare, tab *Câmpuri disponibile*) și căutarea șabloanelor.
- `view_users_form_signature` și `view_users_form_simple_modif_signature`: butonul *Regenerează semnătura mea* în formularul utilizatorului și în preferințe.

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau acțiuni server; reîmprospătarea se face la `write` pe utilizator.

#### 5. Conexiuni

- [deltatech_mail_client](../deltatech_mail_client/index.md): folosește semnătura utilizatorului la redactarea mesajelor.
