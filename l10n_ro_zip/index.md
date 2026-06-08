# Romania - Coduri Poștale (localizat la `l10n_ro_zip/index.md`)

- **Nume Tehnic:** `l10n_ro_zip`
- **Versiune:** `19.0.0.0.0`
- **Cale:** `https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_zip`
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_zip`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Modulul oferă o bază de date completă a codurilor poștale din România, gata de folosit imediat după instalare. Sunt importate automat aproximativ 52.000 de coduri poștale, fiecare legat de județul și localitatea corespunzătoare. La completarea adresei unui partener, utilizatorul poate alege codul poștal dintr-o listă filtrată după localitate, iar câmpul standard de cod poștal se completează automat. Astfel se elimină erorile de introducere manuală și se asigură date de adresă corecte și consistente, utile pentru livrări, facturare și raportări.

#### 2. Funcționalități Cheie

- Adaugă modelul `res.zip` cu ~52.000 de înregistrări de coduri poștale românești, fiecare conținând: cod poștal, localitate, județ, tip stradă, nume stradă, sector (București), oficiu poștal.
- Datele sunt importate automat la instalare dintr-un fișier SQL și sunt corelate cu județele și localitățile din modulul `l10n_ro_city`.
- Extinde formularul partenerului (`res.partner`) cu câmpul `Cod Poștal (zip_id)`, filtrat după localitate, care completează automat câmpul standard `zip` la selecție.
- Căutarea codurilor poștale funcționează atât după codul numeric, cât și după numele străzii.
- Suportă sectoarele municipiului București (1–6) cu legătură directă la localitățile corespunzătoare.

#### 3. Dependențe

- `base_address_extended`
- `l10n_ro_city`

#### 4. Componente Cheie

Secțiune omisă: fișierul `readme/DESCRIPTION.md` este prezent și acoperă Sumarul și Funcționalitățile Cheie, fără a solicita explicit analiza componentelor tehnice (modele, vizualizări, acțiuni). Conform fluxului de ingestie, analiza suplimentară a codului nu a fost efectuată.

#### 5. Conexiuni

- `l10n_ro_city`: furnizează județele și localitățile cu care sunt corelate codurile poștale.
