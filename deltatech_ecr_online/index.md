# Fiscal Receipt for Invoices (Odoo Online)

- **Nume Tehnic:** `deltatech_ecr_online`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_ecr_online
- **Cale Locală:** `odoo-addons/bitshop/deltatech_ecr_online`
- **Ultima Ingestie:** `2026-11-14`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite tipărirea bonului fiscal al unei facturi de client plătite pe o casă de marcat din România, direct din **Odoo Online**. Nu conține cod Python: se importă ca arhivă zip, iar bonul este construit și trimis de browser, prin **Terrabit Connect**, agentul local instalat pe calculatorul casierului. Nimic nu pleacă din baza de date către un server Terrabit și nu se consumă credite.

#### 2. Funcționalități Cheie

- **Un singur buton pe factura plătită**: *Print Fiscal Receipt* apare pe factura de client confirmată, după ce este plătită integral, și dispare după tipărirea bonului, deci același bon nu se trimite de două ori.
- **Case de marcat**: Datecs (FiscalWire), Optima, Incotex, Daisy, Succes și FiscalNet, cu formatele de comenzi din `deltatech_ecr_connect`.
- **Rezultat pe factură**: numărul bonului fiscal (BF), numărul documentului fiscal (NR), raportul Z, starea și eroarea casei de marcat, în tab-ul *Other Info*, plus mesaj în chatter. Stările: Printed, Canceled, Error.
- **Plăți ca pe casa de marcat**: fiecare plată a facturii pleacă cu codul de plată al jurnalului (numerar, card, tichete); diferența de câțiva bani din rotunjire se adaugă la plata în numerar.
- **Erori ale casei de marcat**: casierul poate reîncerca (același identificator, fără dublă tipărire), procesa manual fișierul de comenzi sau anula; dacă agentul nu răspunde (40 s), fișierul de comenzi se descarcă și nu se scrie nimic pe factură. Fișierul se tipărește fie cu programul casei, fie prin butonul din Odoo, niciodată ambele.
- **Filtre în căutarea facturilor**: *Paid, without Fiscal Receipt*, *Fiscal Receipt Printed*, *Fiscal Receipt Error*.
- **Casă simulată** (doar teste/demonstrații): browserul simulează o casă FiscalWire, cu rolă de hârtie, rapoarte X și Z (panoul *Virtual devices*); bonul simulat nu este fiscal și nu marchează factura ca tipărită. Se activează din *Cash Register Simulation* pe companie (simulat în Odoo sau prin agent).
- **Configurare**:
  - Compania (*Settings > Users & Companies > Companies*, tab *Cash Register*): tipul casei (implicit FiscalWire), URL-ul Terrabit Connect (implicit `http://127.0.0.1:8765`), extensia fișierului de comenzi (implicit `inp`).
  - Jurnalele bancă/card (tab *Incoming Payments*): *Cash Register Payment Code* (FiscalWire: 0 numerar, 1 tichete, 2 card). Jurnalul de numerar fără cod trimite 0; cel de bancă/card fără cod oprește bonul.
  - Taxe (opțional): *Cash Register Tax Code*, când două taxe cu aceeași cotă merg în grupe de TVA diferite pe casă (ex. două taxe de 0%).
  - Agentul Terrabit Connect trebuie să permită adresa bazei de date (`TERRABIT_ALLOWED_ORIGIN`); în Chrome se permite accesul la rețeaua locală.
- Modulul exclude `deltatech_sale_store` (același buton pe factură, cu propriul indicator de tipărire; instalate împreună ar permite două bonuri pentru aceeași factură).

#### 3. Dependențe

- `account`
- [deltatech_ecr_connect](../deltatech_ecr_connect/index.md)

#### 4. Componente Cheie

**Modele**

Fără modele Python; câmpuri manuale (`x_`) create prin date, pentru compatibilitate cu importul pe Odoo Online:

- `account.move`: `x_ecr_receipt_print` (bon tipărit), `x_ecr_fiscal_state` (stare: Printed/Canceled/Error), `x_ecr_receipt_number` (BF), `x_ecr_doc_number` (NR), plus Z și eroarea casei.
- `res.company`, `account.journal`, `account.tax`: setări ale casei, cod de plată și cod de taxă.

**Vizualizări**

- `views/account_move_views.xml`: butonul *Print Fiscal Receipt*, secțiunea *Fiscal Receipt* din *Other Info* și filtrele de căutare.
- `views/account_journal_views.xml`: *Cash Register Payment Code* pe jurnal.
- `views/account_tax_views.xml`: *Cash Register Tax Code* pe taxă.
- `views/res_company_views.xml`: tab-ul *Cash Register* pe companie.

**Acțiuni Automate / Acțiuni Server**

- Acțiune client `deltatech_ecr_online.print` (*Print Fiscal Receipt*, pe `account.move`): construiește bonul în browser și îl trimite agentului local. Fără cron-uri.
- Cod JavaScript (`static/src/*.esm.js`): setări, construirea documentului, tipărirea și dispozitivele virtuale.

#### 5. Conexiuni

- [deltatech_ecr_connect](../deltatech_ecr_connect/index.md): formatele de comenzi ale caselor de marcat folosite de acest modul.
- [deltatech_ecr_fiscal](../deltatech_ecr_fiscal/index.md): definește câmpurile de audit fiscal (BF, NR, Z, stare) cu același rol; aici câmpurile sunt manuale (`x_`), pentru Odoo Online.
- [deltatech_sale_store](../deltatech_sale_store/index.md): același buton pe factură; incompatibil, modulele se exclud reciproc.
