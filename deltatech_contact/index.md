# Contact Personal Data (localizat la `deltatech_contact/index.md`)

- **Nume Tehnic:** `deltatech_contact`
- **Versiune:** `19.0.1.4.15`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_contact
- **Cale Locală:** `odoo-addons/deltatech/deltatech_contact`
- **Ultima Ingestie:** `2026-11-15`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde modulul standard de Contacte din Odoo cu date personale pentru persoane fizice: CNP (cu validarea cifrei de control), datele actului de identitate, data nașterii, sexul și mijlocul de transport. Echipele care lucrează cu persoane fizice găsesc astfel în fișa de contact câmpurile necesare pentru identificare, fără module externe.

#### 2. Funcționalități Cheie

- Tab **Date personale** pe fișa unei persoane de tip adresă *Contact*, cu actul de identitate (**Card ID Number**: serie și număr; **Card ID Issued**: autoritate emitentă și dată), **CNP**, **data nașterii** și **sex**. Aceleași câmpuri apar și în formularul unui contact adăugat dintr-o companie și în formularul de creare rapidă.
- **Data nașterii și sexul din CNP**: la introducerea CNP-ului, data nașterii se ia din cifrele 2–7 și sexul din prima cifră (1 sau 5 = masculin). La modificarea datei nașterii, cifrele de dată din CNP se rescriu și cifra de control se recalculează.
- **Validare CNP**: 13 cifre și cifră de control validă. La salvarea unui contact existent cu CNP invalid apare mesajul *CNP invalid*. Pe un contact nou (din formular sau din import) un CNP invalid este golit la salvare, fără mesaj. Un CNP gol este acceptat. În contextul `install_mode` validarea este omisă.
- Câmpul **Mijloc de transport** (de exemplu numărul de înmatriculare al mașinii delegatului), afișat sub *Referință* în tabul **Vânzări și Achiziții** al unei persoane.
- **Filtre de căutare**: în **Contacte > Contacte** apar filtrele **Livrare** și **Facturare** pentru adrese de acest tip, iar filtrele standard **Persoane** și **Companii** arată doar contactele fără companie-părinte.
- Tabul standard **Contacte** este ascuns pe un contact care aparține unei companii.
- **Nume fără companie**: dacă parametrul de sistem `contact.get_name_only` este setat, contactele de tip *Contact* sunt afișate doar cu numele propriu.
- **Opțiuni de afișare a numelui pentru dezvoltatori**: cheile de context `show_phone`, `show_category` și `address_inline` adaugă telefonul sau etichetele la numele contactului în câmpurile relaționale ori aduc numele și adresa pe o singură linie.
- **Limitări**: un CNP tastat în formular cu cifră de control greșită (sau de 12 cifre) primește silențios cifra corectă, deci se compară cu actul de identitate; prima cifră 1 sau 2 dă anul nașterii în secolul 20, oricare alta în secolul 21; un CNP de 8–11 caractere sau cu cifrele 2–7 care nu formează o dată validă produce o eroare tehnică în formular, nu un mesaj de validare.

#### 3. Dependențe

- `base`
- `contacts`

#### 4. Componente Cheie

Secțiunea este acoperită de `readme/DESCRIPTION.md`; analiza codului a servit doar la verificarea comportamentului descris.

**Modele**

- `res.partner` (extins): adaugă câmpurile `cnp`, `id_series`, `id_nr`, `id_issued_by`, `id_issued_at`, `mean_transp`, `birthdate`, `gender` (male / female / other) și `is_department`; validare CNP prin constrângerea `check_cnp`, onchange-uri pe `cnp` și `birthdate`, golirea CNP-ului invalid la `create` și suprascrierea numelui afișat.

**Vizualizări**

- `view_partner_form`: tabul **Date personale**, grupul de date personale din formularul contactelor copil și câmpul `mean_transp` după `ref`.
- `view_hide_partner_form`: ascunde tabul **Contacte** când contactul are companie-părinte.
- `view_partner_simple_form`: câmpurile personale în formularul simplificat de creare rapidă.
- `deltatech_res_partner_kanban_view`: adaugă `vat` în kanban-ul partenerilor.
- `view_res_partner_filter`: filtrele **Livrare** / **Facturare** și domeniul modificat al filtrelor **Persoane** / **Companii**.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește acțiuni automate sau acțiuni server.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale către alte module cu pagină wiki existentă.
