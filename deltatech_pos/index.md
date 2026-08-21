# Print to ECR from POS (localizat la `deltatech_pos/index.md`)

- **Nume Tehnic:** `deltatech_pos`
- **Versiune:** `19.0.2.6.11`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_pos
- **Cale Locală:** `odoo-addons/bitshop/deltatech_pos`
- **Ultima Ingestie:** `2026-08-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul Deltatech POS ECR asigură o integrare eficientă între punctul de vânzare (Point of Sale) din Odoo și diverse case de marcat fiscale (ECR — Electronic Cash Register), permițând generarea automată a bonurilor fiscale și o gestionare completă a numerarului. În practică, modulul creează o punte între POS-ul Odoo și casa de marcat configurată: generează un fișier în formatul potrivit, care este apoi preluat și tipărit de casa de marcat în modul Conexiune PC (este nevoie de un driver de comunicare specific modelului). Astfel, operatorul nu mai lucrează din utilitarul instalat al casei de marcat, ci direct din Odoo — poate tipări bonuri fiscale, introduce sau scoate bani din casă și emite rapoarte X și Z.

#### 2. Funcționalități Cheie

- Generare fișier pentru programul de tipărit Bon Fiscal din POS.
- Suport pentru tipărirea notelor de pe liniile de comandă (note client și note interne).
- Suport pentru tipărirea notei generale a comenzii, după liniile de produse.
- Suport pentru tipărirea numărului comenzii sub formă de cod de bare pe bon (opțional).
- Căutare în POS după codul fiscal (tax ID).
- Gestionare Cash In / Cash Out: efectuare de încasări și plăți de numerar direct din interfața POS.
- Tipărirea documentelor de plată/încasare (dispoziții de plată) pe casa de marcat.
- Opțiune pentru tipărirea duplicatului dispoziției de plată.
- Tipărirea rapoartelor X și Z direct din Odoo.
- Posibilitatea de a configura departamentul implicit pentru liniile de pe bon.
- Output compatibil ASCII pentru driverele ECR: elimină diacriticele și convertește exponenții uzuali (ex.: m² → m2, m³ → m3); orice alt caracter non-ASCII este înlocuit cu spațiu.

**Case de marcat compatibile:**

- Datecs — variantele noi (2018), cu driverele FiscalWire, FiscalNet și DxPrint.
- Optima — cu driverul QComm.
- Incotex Succes — cu driverul FiscalPrinterDevice.
- Daisy — cu driver corespunzător (folosind protocolul Daisy).

**Configurare și utilizare (din `readme/USAGE.md`):**

- Codul ECR se setează per metodă de plată (Punct de vânzare > Configurare > Metode de plată).
- Comportamentul specific ECR (cod de bare pe bon, Cash In/Out, Cash In/Out către ECR, duplicat dispoziție de plată, departament implicit) se configurează în Setările Punctului de Vânzare, secțiunea ECR.
- Rapoartele X și Z se tipăresc din sesiunea POS activă (Punct de vânzare > Comenzi > Sesiuni).

#### 3. Dependențe

- `point_of_sale`
- [deltatech_pos_base](../deltatech_pos_base/index.md)
- [deltatech_ecr_connect](../deltatech_ecr_connect/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile de Componente Cheie au fost omise deoarece modulul include un fișier `readme/DESCRIPTION.md`, folosit pentru Sumar și Funcționalități Cheie.

#### 5. Conexiuni

- [deltatech_pos_base](../deltatech_pos_base/index.md): modul de bază POS Deltatech pe care se construiește integrarea ECR (dependență directă).
- [deltatech_ecr_connect](../deltatech_ecr_connect/index.md): componenta partajată de conectare/comunicare cu casele de marcat, folosită de `deltatech_pos` pentru generarea fișierelor ECR (dependență directă, adăugată față de versiunea anterioară a modulului).
