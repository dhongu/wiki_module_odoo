# UBL Invoice Import Base

- **Nume Tehnic:** `deltatech_account_ubl_import`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_account_ubl_import
- **Cale Locală:** odoo-addons/deltatech/deltatech_account_ubl_import
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul tehnic de bază, folosit în comun de instrumentele care importă facturi de furnizor în format UBL XML. Nu are meniu, vizualizări sau setări proprii și nu modifică fluxurile standard; oferă doar logica de citire a fișierului și de potrivire a datelor cu cele din Odoo.

#### 2. Funcționalități Cheie

- **Citirea UBL**: antetul documentului (număr, date, monedă, referința comenzii, totaluri, CUI și nume furnizor; nota de credit este recunoscută după tipul documentului sau codul 381) și liniile facturii (cod furnizor, cod de bare, denumire, cantitate, unitate, preț, discount din `AllowanceCharge`, cotă și categorie TVA).
- **Căutarea furnizorului** după CUI (cu sau fără prefixul `RO`) sau după nume.
- **Potrivirea produselor** după cod de bare, cod furnizor, referință internă, denumirea la furnizor sau denumirea produsului, cu raportarea modului în care a fost găsit produsul.
- **Conversia unităților de măsură** din codurile UBL (C62, KGM, LTR etc.) în unitățile Odoo.
- **Actualizarea prețului** în lista de prețuri a furnizorului și **crearea produsului** dintr-o linie de factură.
- **Căutarea facturilor duplicat** și citirea cotei de TVA declarate pe fiecare linie.
- Fluxul de utilizare pas-cu-pas este în fișa consultantului.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.ubl.import.mixin`: model abstract cu parserul UBL, căutarea furnizorului, potrivirea produselor, conversia unităților și actualizarea prețurilor de furnizor.

**Vizualizări**

- Nu are vizualizări.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [deltatech_purchase_ubl](../deltatech_purchase_ubl/index.md): folosește baza comună pentru importul UBL în achiziții.
- [deltatech_vendor_bill_ubl_review](../deltatech_vendor_bill_ubl_review/index.md): folosește baza comună pentru verificarea facturilor de furnizor UBL.
