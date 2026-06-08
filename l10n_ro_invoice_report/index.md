# Romania - Invoice Report Terrabit (localizat la `l10n_ro_invoice_report/index.md`)

- **Nume Tehnic:** `l10n_ro_invoice_report`
- **Versiune:** `19.0.3.4.16`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_invoice_report
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_invoice_report`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Acest modul extinde raportul de factură standard din Odoo pentru a se conforma cerințelor specifice din România și pentru a oferi opțiuni suplimentare de personalizare. Adaugă pe documentele tipărite detalii la nivel de linie (preț fără TVA, valoare TVA, numerotare), informații legale și logistice (delegat, mijloc de transport, mențiunea privind scutirea de semnătură și ștampilă) și gestionează documentele de plată corelate (chitanțe, dispoziții de plată/încasare), oferind în același timp numeroase opțiuni de configurare din setările de facturare.

#### 2. Funcționalități Cheie

- **Detalii linii factură**:
    - Afișarea prețului unitar fără TVA.
    - Afișarea valorii TVA pe fiecare linie.
    - Afișarea totalului cu taxe pe fiecare linie (configurabil).
    - Numerotarea automată a liniilor de factură (Ord).
    - Opțiune de a elimina numele produsului de pe linie dacă există o descriere specifică.
    - Afișarea prețului fără discount.
- **Informații suplimentare pe document**:
    - Câmpuri dedicate pentru **Delegat** și **Mijloc de transport**.
    - Afișarea textului legal privind scutirea de semnătură și ștampilă (conform Codului Fiscal).
    - Posibilitatea de a adăuga un text adițional de la partener pe factură (`info_for_invoice`).
    - Vizibilitatea configurabilă pentru email, telefon și marcaje în adresa facturii.
    - Afișarea informațiilor despre livrări (Pickings) și AWB-uri direct pe factură.
    - Inserarea logoului **Coface** la finalul facturii (activabil din setări).
- **Gestiune documente corelate**:
    - Tipărirea automată a chitanțelor, dispozițiilor de plată sau încasare direct din factură pentru plățile în numerar.
    - Gestionarea corectă a semnelor pentru stornări (Credit Notes).
- **Rapoarte dedicate**:
    - Raport de factură în limba companiei, indiferent de limba partenerului.
- **Configurare flexibilă**:
    - Numeroase opțiuni în setările de facturare pentru a activa sau dezactiva elementele menționate mai sus (Sarcini delegat, comentarii plată, index linii, etc.).

> **Cerințe tehnice:** Necesită instalarea bibliotecii `num2words` (recomandat: `pip3 install num2words==0.5.12`).

#### 3. Dependențe

- `base`
- `account`
- `l10n_ro_config`
- `purchase`
- `sale`
- `stock_delivery`

#### 4. Componente Cheie

> Secțiune omisă: fișierul `readme/DESCRIPTION.md` acoperă deja Sumarul și Funcționalitățile Cheie, iar conform schemei de ingestie analiza codului pentru Componente Cheie (Modele, Vizualizări, Acțiuni Automate / Acțiuni Server) nu se efectuează decât dacă este cerută explicit în Readme.

#### 5. Conexiuni

- `l10n_ro_config`: modulul de configurare al localizării românești care găzduiește setările de facturare valorificate de acest raport.
- `stock_delivery`: sursa informațiilor despre livrări (Pickings) și AWB-uri afișate pe factură.
