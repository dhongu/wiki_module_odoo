# Contact Personal Data (localizat la `deltatech_contact/index.md`)

- **Nume Tehnic:** `deltatech_contact`
- **Versiune:** `19.0.1.4.16`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_contact`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_contact`
- **Ultima Ingestie:** `2026-11-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde aplicația standard Contacte din Odoo cu date personale pentru persoane fizice: CNP (cu validare a cifrei de control), datele actului de identitate, data nașterii, sexul și mijlocul de transport. Echipele care lucrează cu persoane fizice au astfel, direct în fișa de contact, câmpurile necesare pentru identificare, fără module externe.

#### 2. Funcționalități Cheie

- **Tab Date personale** (Personal Data) pe contactele de tip *Persoană* cu tipul de adresă *Contact*: act de identitate (**Card ID Number** – serie și număr; **Card ID Issued** – autoritate emitentă și dată), **CNP**, **Data nașterii** și **Sex**. Aceleași câmpuri apar și pe formularul unui contact adăugat dintr-o companie și pe formularul de creare rapidă.
- **Completare automată din CNP**: data nașterii se ia din cifrele 2–7, sexul din prima cifră; la modificarea datei nașterii, cifrele de dată din CNP se rescriu și cifra de control se recalculează.
- **Validare CNP**: 13 cifre și cifră de control validă. La salvarea unui contact existent, un CNP invalid oprește operația cu mesajul *CNP invalid*; pe un contact nou (formular sau import) CNP-ul invalid este golit la salvare, fără mesaj. Un CNP gol este acceptat.
- **Mijloc de transport** (**Mean Transport**, de exemplu numărul de înmatriculare al mașinii unui delegat): afișat sub *Reference*, în tabul **Vânzări și achiziții** al unei persoane.
- **Filtre de căutare**: în **Contacte > Contacte** apar filtrele **Livrare** și **Facturare** pentru adresele de aceste tipuri; filtrele standard **Persoane** și **Companii** afișează doar contactele fără companie-părinte.
- **Tabul standard Contacte** este ascuns pe un contact care aparține unei companii.
- **Nume contact fără companie**: când parametrul de sistem `contact.get_name_only` este setat, contactele de tip *Contact* se afișează cu numele propriu, fără numele companiei.
- **Opțiuni de afișare pentru dezvoltatori**: cheile de context `show_phone`, `show_category` și `address_inline` adaugă telefonul sau etichetele la numele contactului în câmpurile relaționale, sau pun numele și adresa pe un singur rând.
- **Limitări cunoscute**: un CNP tastat cu cifră de control greșită (sau de 12 cifre) primește cifra corectă fără mesaj, deci se compară cu actul de identitate; prima cifră 1 sau 2 dă anul nașterii în 1900, oricare alta în 2000, iar sexul este masculin doar pentru prima cifră 1 sau 5; un CNP de 8–11 caractere sau cu cifrele 2–7 care nu formează o dată validă provoacă o eroare tehnică în formular, nu un mesaj de validare.

#### 3. Dependențe

- `base`
- `contacts`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile de Componente Cheie sunt acoperite de `readme/DESCRIPTION.md` și nu au fost extrase suplimentar din cod. Modulul extinde modelul `res.partner` (vizualizări în `views/res_partner_view.xml`) pentru a adăuga câmpurile `cnp`, `id_series`, `id_nr`, `id_issued_by`, `id_issued_at`, `mean_transp`, `birthdate`, `gender` și `is_department`, și pentru a suprascrie logica numelui afișat.

#### 5. Conexiuni

Nu există conexiuni suplimentare față de dependențele din manifest (`base`, `contacts`), iar acestea nu au pagină wiki.
