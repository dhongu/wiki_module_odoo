# Contact Personal Data (localizat la `deltatech_contact/index.md`)

- **Nume Tehnic:** `deltatech_contact`
- **Versiune:** `20.0.1.4.14`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_contact`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_contact`
- **Ultima Ingestie:** `2026-11-27`

#### 1. Sumar

Modulul extinde aplicația standard Contacte din Odoo cu date personale pentru persoane fizice: CNP-ul românesc cu validarea cifrei de control, datele cărții de identitate, data nașterii, sexul și mijlocul de transport. Echipele care lucrează cu persoane fizice au astfel toate câmpurile de identificare direct în fișa de contact, fără module externe.

#### 2. Funcționalități Cheie

- **Tab Date personale** pe contactele de tip *Contact* care nu sunt companie (în Odoo 20, un contact fără companie-părinte este companie dacă are CUI/TVA). Grupează cartea de identitate (serie și număr, autoritatea emitentă și data emiterii), **CNP**, **data nașterii** și **sexul**. Aceleași câmpuri apar pe formularul contactului adăugat dintr-o companie și pe formularul de creare rapidă.
- **Completare din CNP**: la introducerea CNP-ului, data nașterii se ia din cifrele 2–7, iar sexul din prima cifră. La modificarea datei nașterii, cifrele de dată din CNP se rescriu și cifra de control se recalculează.
- **Validare CNP**: 13 cifre și cifră de control validă. La salvarea unui contact existent, un CNP invalid oprește operația cu mesajul *CNP invalid*. Pe un contact nou (din formular sau import), CNP-ul invalid este golit la salvare, fără mesaj. CNP-ul gol este acceptat.
- **Mijloc de transport** (de exemplu numărul de înmatriculare al mașinii unui delegat): afișat la *Referință*, în tabul **Vânzări și achiziții**, pe contactele care nu sunt companii.
- **Filtre de căutare** în **Contacte > Contacte**: **Persoane** și **Companii** (contacte fără companie-părinte; nu mai există standard în Odoo 20), plus **Livrare** și **Facturare** pentru adresele de aceste tipuri.
- **Tabul Contacte** standard este ascuns pe contactele care aparțin unei companii.
- **Nume de contact fără companie**: când parametrul de sistem `contact.get_name_only` este setat, contactele de tip *Contact* se afișează doar cu numele propriu. Atenție: conform `readme/bugs.md` (P2, deschis), parametrul nu mai influențează numele afișat în Odoo 20.
- **Opțiuni de context pentru dezvoltatori**: `show_phone`, `show_category` și `address_inline` adaugă telefonul sau etichetele la numele contactului în câmpurile relaționale sau pun numele și adresa pe o singură linie.
- **Limitări cunoscute**: un CNP tastat cu cifră de control greșită (sau de 12 cifre) primește cifra corectă fără mesaj, deci se compară cu cartea de identitate; prima cifră 1 sau 2 dă anul nașterii în 1900–1999, orice altă cifră în 2000+, iar sexul e masculin doar pentru primele cifre 1 și 5; un CNP de 8–11 caractere sau cu cifrele 2–7 care nu formează o dată validă produce o eroare tehnică, nu un mesaj de validare; un CNP nenumeric de 13 caractere ridică `ValueError` (P2, deschis).

#### 3. Dependențe

- `base`
- `contacts`

#### 4. Componente Cheie

Conform fluxului de ingestie, componentele sunt acoperite de `readme/DESCRIPTION.md` și nu au fost extrase suplimentar din cod. Modulul extinde `res.partner` (`models/res_partner.py`) cu câmpurile personale (CNP, serie/număr act, emitent, dată emitere, mijloc de transport, data nașterii, sex), validarea CNP și logica numelui afișat, iar interfața vine din `views/res_partner_view.xml`.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale către alte module cu pagină wiki existentă.
