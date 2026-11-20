# UBL Invoice Import Base (localizat la `deltatech_account_ubl_import/index.md`)

- **Nume Tehnic:** `deltatech_account_ubl_import`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_account_ubl_import
- **Cale Locală:** `odoo-addons/deltatech/deltatech_account_ubl_import`
- **Ultima Ingestie:** `2026-11-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul tehnic de bază, partajat de instrumentele care importă facturi de la furnizori în format UBL XML. Citește factura electronică, găsește furnizorul și produsele din Odoo și pregătește datele pentru modulele care creează comenzi sau facturi. Nu are meniu, vizualizări sau setări proprii și nu modifică fluxurile standard, așa că se instalează automat odată cu instrumentele care îl folosesc.

#### 2. Funcționalități Cheie

- **Citirea UBL**: antetul documentului (număr, date, monedă, referința comenzii, totaluri, CUI și nume furnizor; nota de credit e recunoscută după tipul documentului sau codul 381) și liniile facturii (cod furnizor, cod de bare, denumire, cantitate, unitate, preț, discount din `AllowanceCharge`, cota și categoria de TVA).
- **Căutarea furnizorului** după codul de TVA (CUI românesc, cu sau fără prefixul `RO`) sau, în lipsă, după nume.
- **Potrivirea produselor** după cod de bare, cod furnizor, referință internă, denumirea produsului la furnizor sau denumirea produsului, cu raportarea modului în care a fost găsit produsul.
- **Conversia unităților de măsură** din codurile UBL (C62, KGM, LTR etc.) în unitățile Odoo.
- **Actualizarea prețului furnizorului** în lista de prețuri a furnizorului și **crearea unui produs** pornind de la o linie de factură.
- **Căutarea facturilor duplicat** și citirea cotei de TVA declarate pe fiecare linie.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.ubl.import.mixin`: model abstract cu parserul UBL, căutarea furnizorului, potrivirea produselor, conversia unităților, actualizarea prețului furnizorului, crearea produselor și căutarea facturilor duplicat.

**Vizualizări**

- Niciuna (modul tehnic, fără interfață proprie).

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_vendor_bill_ubl_review](../deltatech_vendor_bill_ubl_review/index.md): *Vendor Bill UBL Review*, folosește parserul și potrivirea de produse din acest modul.
- [deltatech_purchase_ubl](../deltatech_purchase_ubl/index.md): *Purchase UBL Import*, din care a fost extrasă logica partajată (conform `HISTORY.md`).
