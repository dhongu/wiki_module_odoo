# Purchase Orders Bulk Email with XLSX (localizat la `deltatech_purchase_mail/index.md`)

- **Nume Tehnic:** `deltatech_purchase_mail`
- **Versiune:** `20.0.1.1.6`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_purchase_mail`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_mail`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Când mai multe cereri de ofertă sau comenzi merg către același furnizor, trimiterea lor una câte una înseamnă un e-mail pentru fiecare. Modulul le trimite împreună, într-un singur e-mail, cu un rezumat Excel al tuturor liniilor și cu PDF-ul fiecărei comenzi.

#### 2. Funcționalități Cheie

- Un singur e-mail pentru mai multe comenzi: se selectează comenzile în lista *Purchase > Orders > Requests for Quotation* sau *Purchase > Orders > Purchase Orders* și se alege *Actions > Send Email*; se deschide compozitorul standard, cu furnizorul ca destinatar.
- Rezumat XLSX cu un rând pe linie de comandă: referința comenzii, codul produsului, descrierea, cantitatea și prețul unitar fără taxe; coloanele text sunt scrise ca text, deci o valoare care începe cu „=" nu este citită ca formulă.
- PDF-ul standard al fiecărei comenzi selectate este atașat aceluiași e-mail.
- Trasabilitate pe fiecare comandă: doar la trimiterea efectivă se adaugă o notă cu corpul e-mailului, rezumatul și PDF-ul propriu, iar cererile de ofertă din starea draft trec în *RFQ Sent*; închiderea compozitorului fără trimitere nu schimbă nimic.
- Textul vine din șablonul „Purchase Orders: Send with XLSX", editabil în *Settings > Technical > Email > Templates* (mod dezvoltator).
- Limitări: toate comenzile selectate trebuie să aibă același furnizor, iar furnizorul trebuie să aibă adresă de e-mail (altfel apare mesajul „You must select exactly one vendor to send the email to."); doar adresa furnizorului este precompletată, alți destinatari se adaugă manual.
- Fișa consultant: [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `purchase`
- `mail`

#### 4. Componente Cheie

**Modele**

- `purchase.order` (extins): construiește rezumatul XLSX, pregătește atașamentele (XLSX și PDF-uri) și deschide compozitorul (`action_compose_batch_email`).
- `mail.compose.message` (extins): după trimiterea efectivă înregistrează nota pe fiecare comandă.
- `purchase.send.xlsx.wizard`: wizard cu comenzile, șablonul, destinatarul și opțiunile de atașare a rezumatului XLSX și a PDF-urilor.

**Vizualizări**

- Nu există vizualizări noi; funcția apare ca acțiune în meniul *Actions* al listelor de achiziții.

**Acțiuni Automate / Acțiuni Server**

- `action_purchase_compose_batch_email` (`ir.actions.server`): acțiunea „Send Email" din listele de comenzi.
- `mail_template_purchase_send_xlsx` (`mail.template`): șablonul e-mailului.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale către alte module cu pagină în wiki.
