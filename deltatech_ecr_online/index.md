# Fiscal Receipt for Invoices (Odoo Online) (localizat la `deltatech_ecr_online/index.md`)

- **Nume Tehnic:** `deltatech_ecr_online`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_ecr_online
- **Cale Locală:** `odoo-addons/bitshop/deltatech_ecr_online`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite tipărirea bonului fiscal pentru o factură client achitată, pe o casă de marcat din România, direct din **Odoo Online**. Nu conține cod Python: se importă ca arhivă zip, iar bonul este construit și trimis de browser prin **Terrabit Connect**, agentul local instalat pe calculatorul casierului. Datele nu părăsesc baza de date a clientului: bonul merge din browserul casierului direct la agentul local, fără server Terrabit și fără credite.

#### 2. Funcționalități Cheie

- **Un singur buton pe factură**: *Print Fiscal Receipt* apare pe factura client postată după ce este achitată integral și dispare după tipărire, astfel încât bonul aceleiași facturi să nu fie trimis de două ori.
- **Case de marcat**: Datecs (FiscalWire), Optima, Incotex, Daisy, Succes și FiscalNet, cu formatele de comandă din [deltatech_ecr_connect](../deltatech_ecr_connect/index.md). Tipul casei, adresa agentului (implicit `http://127.0.0.1:8765`) și extensia fișierului de comenzi (implicit `inp`) se setează pe companie, tab *Cash Register*.
- **Rezultat pe factură**: numărul bonului fiscal (BF), numărul documentului fiscal (NR), raportul Z, starea și eroarea casei, în tab-ul *Other Info*, plus un mesaj în chatter.
- **Plăți ca pe casa de marcat**: fiecare plată a facturii pleacă cu codul de plată al jurnalului (numerar, card, tichete; la FiscalWire 0, 2, 1). Un jurnal de numerar fără cod trimite 0, iar unul bancar/card fără cod oprește bonul. Diferența de câțiva bani din rotunjire merge pe plata în numerar.
- **Coduri de TVA**: pe taxe, un cod opțional de casă pentru cazul a două taxe cu aceeași cotă, dar pe grupe de TVA diferite (ex. două taxe de 0%).
- **Erori ale casei**: casierul poate reîncerca (același identificator, fără dublă tipărire), prelucra manual fișierul de comenzi sau anula; dacă agentul nu răspunde în 40 de secunde, fișierul se descarcă și nu se scrie nimic pe factură.
- **Filtre pe facturi**: *Paid, without Fiscal Receipt*, *Fiscal Receipt Printed* și *Fiscal Receipt Error*.
- **Casă simulată**: pentru teste și demonstrații, browserul simulează o casă FiscalWire cu rolă de hârtie, rapoarte X și Z (panoul *Virtual devices*); un bon simulat nu este fiscal și nu marchează factura ca tipărită.
- Fluxul pas-cu-pas, cu capturi, este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- [deltatech_ecr_connect](../deltatech_ecr_connect/index.md)

Incompatibil (`excludes`) cu [deltatech_sale_store](../deltatech_sale_store/index.md): ambele pun același buton pe factură, cu steaguri proprii de tipărit, iar instalate împreună ar permite două bonuri pentru aceeași factură.

#### 4. Componente Cheie

**Modele**

Modulul nu definește modele Python. Câmpurile sunt manuale (`x_`), create din `data/ir_model_fields.xml`:

- `account.move`: `x_ecr_receipt_print` (bon tipărit), `x_ecr_fiscal_state` (stare), `x_ecr_receipt_number` (BF), `x_ecr_doc_number` (NR), `x_ecr_z_number` (Z), `x_ecr_error`, `x_ecr_simulated`.
- `res.company`: `x_ecr_type` (tipul casei) și câmpurile de adresă agent, extensie fișier și simulare.

**Vizualizări**

- `views/account_move_views.xml`: butonul *Print Fiscal Receipt*, secțiunea *Fiscal Receipt* din *Other Info* și filtrele de căutare.
- `views/account_journal_views.xml`: *Cash Register Payment Code* pe jurnale.
- `views/account_tax_views.xml`: *Cash Register Tax Code* pe taxe.
- `views/res_company_views.xml`: tab-ul *Cash Register* pe companie.

**Acțiuni Automate / Acțiuni Server**

- `action_ecr_online_print` (`ir.actions.client`, tag `deltatech_ecr_online.print`): construiește bonul în browser (`ecr_online_print.esm.js`) și îl trimite agentului local. Nu există acțiuni cron.

#### 5. Conexiuni

- [deltatech_ecr_connect](../deltatech_ecr_connect/index.md): furnizează formatele de comandă pentru casele de marcat.
- [deltatech_sale_store](../deltatech_sale_store/index.md): oferă același buton pe factură, cu steag propriu de tipărit; exclusă reciproc.
