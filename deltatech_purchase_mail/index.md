# Achiziții: Trimitere comenzi multiple pe email cu XLSX (localizat la `deltatech_purchase_mail/index.md`)

- **Nume Tehnic:** `deltatech_purchase_mail`
- **Versiune:** `19.0.1.1.6`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_purchase_mail
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_mail`
- **Ultima Ingestie:** `2026-11-05`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Când mai multe cereri de ofertă sau comenzi de achiziție merg către același furnizor, trimiterea lor pe rând înseamnă câte un email pentru fiecare. Modulul le trimite împreună, într-un singur email către furnizor, cu un sumar Excel al tuturor liniilor și cu PDF-ul fiecărei comenzi.

#### 2. Funcționalități Cheie

- **Un singur email pentru mai multe comenzi**: se selectează comenzile în lista din *Purchase > Orders > Requests for Quotation* sau *Purchase > Orders > Purchase Orders* și se alege **Actions > Send Email**. Se deschide compozitorul standard de email, cu furnizorul ca destinatar.
- **Sumar XLSX**: emailul poartă un fișier Excel cu câte un rând pe linie de comandă: referința comenzii, codul produsului, descrierea, cantitatea și prețul unitar fără taxe. Coloanele text sunt scrise ca text, deci o valoare care începe cu „=" nu este interpretată ca formulă.
- **PDF pentru fiecare comandă**: PDF-ul standard al fiecărei comenzi selectate este atașat aceluiași email.
- **Urmă pe fiecare comandă**: doar la trimiterea efectivă, fiecare comandă primește o notă cu corpul emailului, sumarul și propriul PDF, iar cererile de ofertă rămase în ciornă trec în **RFQ Sent**. Închiderea compozitorului fără trimitere nu schimbă nimic.
- **Șablon de email**: textul vine din șablonul **Purchase Orders: Send with XLSX**, editabil din *Settings > Technical > Email > Templates* (modul developer).
- **Limitări**: toate comenzile selectate trebuie să aibă același furnizor, iar furnizorul trebuie să aibă adresă de email; altfel acțiunea se oprește cu mesajul „You must select exactly one vendor to send the email to.", inclusiv când problema este doar lipsa emailului. Singurul destinatar completat este adresa furnizorului; alți destinatari se adaugă manual în compozitor.
- Fluxul pas cu pas, cu capturi, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `purchase`
- `mail`

#### 4. Componente Cheie

Sumarul și Funcționalitățile Cheie provin din `readme/DESCRIPTION.md`; conform fluxului de ingestie, analiza detaliată a codului este omisă. Din structura modulului:

**Modele**

- `purchase.send.xlsx.wizard` (`wizard/purchase_send_xlsx_wizard.py`): wizard care pregătește emailul, sumarul XLSX și PDF-urile comenzilor selectate.
- `purchase.order` (extins): logica de trimitere și de înregistrare a urmei pe comenzi (`_log_sent_email`).
- `mail.compose.message` (extins): după trimiterea efectivă a emailului generat de wizard, apelează înregistrarea urmei pe comenzile selectate.

**Vizualizări**

- `views/purchase_order_actions.xml`: acțiunea de trimitere pe email, disponibilă din meniul *Actions* al listei de comenzi de achiziție.

**Acțiuni Automate / Acțiuni Server**

- `data/mail_template.xml`: șablonul de email **Purchase Orders: Send with XLSX**.

#### 5. Conexiuni

- Nicio conexiune suplimentară documentată în afara dependențelor declarate.
