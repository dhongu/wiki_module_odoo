# Deltatech Contacts (localizat la `deltatech_contact/index.md`)

- **Nume Tehnic:** `deltatech_contact`
- **Versiune:** `19.0.1.4.8`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_contact`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_contact`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul extinde modulul standard de Contacte din Odoo cu date personale suplimentare pentru persoane fizice: CNP (cu validare cifră de control), datele actului de identitate, data nașterii, sexul și mijlocul de transport. Astfel, echipele care lucrează cu persoane fizice au la dispoziție direct în fișa de contact toate câmpurile necesare pentru identificare, fără module externe.

#### 2. Funcționalități Cheie

- Adaugă un tab **Date personale** pe fișa de contact (vizibil doar pentru persoane fizice) cu: CNP, data nașterii, sex, seria/numărul actului de identitate, autoritatea emitentă și data emiterii.
- **Validare CNP**: verifică la salvare cifra de control a CNP-ului românesc din 13 cifre; la import în masă (context `install_mode`) CNP-urile invalide sunt golite silențios, nu blochează importul.
- **Completare automată din CNP**: la introducerea CNP-ului, data nașterii și sexul sunt derivate automat din cifrele codului (și invers, la modificarea datei nașterii, CNP-ul e recalculat).
- **Afișare nume contact**: poate ascunde numele companiei-părinte din numele afișat al contactului, controlat printr-un parametru de sistem (`contact.get_name_only`).
- Câmp **Mijloc de transport** pe fișa contactului.
- **Filtre de căutare extinse**: adaugă filtre de tip adresă de Livrare și de Facturare în vizualizarea de căutare a Contactelor.
- **Afișare inline a adresei**: suportă flag-urile de context `show_phone`, `show_category` și `address_inline` pentru a îmbogăți sau aplatiza numele afișat al contactului în câmpurile relaționale.

#### 3. Dependențe

- `base`
- `contacts`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile de Componente Cheie sunt acoperite de `readme/DESCRIPTION.md` și nu au fost extrase suplimentar din cod. Modulul extinde modelul `res.partner` (vizualizare `views/res_partner_view.xml`) pentru a adăuga noile câmpuri (`cnp`, `id_series`, `id_nr`, `id_issued_by`, `id_issued_at`, `mean_transp`, `birthdate`, `gender`) și pentru a suprascrie logica de generare a numelui afișat.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale documentate către alte module cu pagină wiki existentă.
