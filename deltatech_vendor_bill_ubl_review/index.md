# Verificare import UBL factură furnizor

- **Nume Tehnic:** `deltatech_vendor_bill_ubl_review`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_vendor_bill_ubl_review
- **Cale Locală:** `odoo-addons/bitshop/deltatech_vendor_bill_ubl_review`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Când Odoo citește o factură de furnizor dintr-un XML UBL (încărcat manual sau primit din SPV), liniile se completează fără ca cineva să confirme că a fost găsit produsul corect, că prețul este cel obișnuit sau că TVA-ul documentului corespunde taxei de pe linie. Modulul adaugă un **pas de verificare pe factura în ciornă**, înainte de postare, în care contabilul vede și corectează aceste puncte.

#### 2. Funcționalități Cheie

- Butonul **Verifică importul UBL** pe o factură sau o notă de credit furnizor în ciornă, care are atașat un XML UBL; insigna *UBL de verificat* apare lângă tipul documentului.
- **Un rând pe linie din XML**, cu produsul găsit și modul în care a fost găsit: verde pentru cod furnizor, referință internă sau cod de bare, galben pentru potrivire doar după denumire, roșu când nu s-a găsit niciun produs. Orice rând poate primi alt produs (devine verde, *Ales manual*).
- **Verificarea prețului**: prețul din XML față de prețul din lista de prețuri a furnizorului; o abatere peste toleranța companiei (implicit 5%) este evidențiată.
- **Verificarea TVA**: cota din XML față de taxa liniei facturii (taxa de achiziție a produsului prin poziția fiscală); se raportează cote diferite, taxare inversă sau linii intracomunitare (AE/K) fără taxă autolichidată și linii AE/K fără produs. Modulul nu alege niciodată singur taxa.
- **Verificări de antet**: totaluri diferite de cele din XML și posibil duplicat (altă factură a aceluiași furnizor cu aceeași referință).
- **La confirmare**: liniile de produs se rescriu din XML cu produsele, unitățile, prețurile și discounturile confirmate; prețurile furnizorului se pot actualiza (opțional); produsele lipsă se pot crea (opțional, implicit dezactivat); factura primește insigna *UBL verificat*, iar jurnalul verificării se postează în chatter.
- Facturile legate de o comandă de achiziție își păstrează liniile (legătura cu comanda rămâne), dar prețurile furnizorului se actualizează și factura se marchează verificată.
- **Blocare opțională la confirmare**: cu *Cere verificarea UBL înainte de confirmare* activată (implicit dezactivată), o factură creată din UBL nu poate fi postată înainte de verificare.
- Setări în *Facturare > Configurare > Setări*, secțiunea *Facturi furnizor*: blocarea la confirmare și toleranța de preț (%). Potrivirea după cod furnizor cere *Codul produsului la furnizor* pe liniile listei de prețuri.
- Importul standard (încărcare, descărcare SPV) rămâne neschimbat; fluxul pas-cu-pas este în fișa consultant.

#### 3. Dependențe

- `deltatech_account_ubl_import`

#### 4. Componente Cheie

**Modele**

- `account.move` (extins): starea verificării UBL, butonul de verificare, blocarea confirmării.
- `vendor.bill.ubl.review.wizard` și `vendor.bill.ubl.review.wizard.line`: asistentul de verificare și rândurile lui (produs, preț, TVA, tip de potrivire).
- `res.company` / `res.config.settings` (extinse): toleranța de preț și opțiunea de blocare.

**Vizualizări**

- `view_move_form_ubl_review`: insigna și butonul pe factură.
- `view_vendor_bill_ubl_review_wizard_form`: asistentul de verificare.
- `res_config_settings_view_form_ubl_review`: setările din Facturare.

**Acțiuni Automate / Acțiuni Server**

- Nu are sarcini cron sau acțiuni server.

#### 5. Conexiuni

- `deltatech_account_ubl_import`: importul UBL pe care îl completează; potrivirea și parsarea sunt comune cu *Purchase UBL Import* prin modulul de bază *UBL Invoice Import Base*.
