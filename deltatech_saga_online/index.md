# Export SAGA pentru Odoo Online

- **Nume Tehnic:** `deltatech_saga_online`
- **Versiune:** `20.0.1.0.4`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_saga_online`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_saga_online`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Exportă facturile de vânzare ale unei perioade ca fișiere XML de import SAGA, inclusiv pe Odoo Online: modulul nu are cod Python și se importă ca zip, iar fișierele sunt construite de serviciul Terrabit, arhiva revenind atașată exportului. Contabilul o importă apoi în SAGA.

#### 2. Funcționalități Cheie

- **Un export pe perioadă**: *Contabilitate > Raportare > Export SAGA*, perioada (luna precedentă implicit) și, opțional, jurnalele de vânzări; *Export* trimite facturile, notele de credit și bonurile înregistrate. *Exportă din nou* retrimite o perioadă după corecții.
- **Fișierele arhivei**: clienții (`CLI`), facturile în RON (`IE`, câte un fișier per jurnal, bonurile cu `C`), facturile în valută și ale clienților străini (`IEV`, per jurnal și monedă). Export pe valoare: contul de venit al fiecărei linii, cota de TVA, note de credit cu cantități negative, cursul facturii.
- **Tip de document**: tipul SAGA al poziției fiscale (T, X...), T pentru taxare inversă internă, TVA la încasare din poziția fiscală sau pentru toate facturile. Factura cu linii mixte (taxare inversă și regulate) este omisă, exportată cu T sau fără tip, după opțiune, cu mesaj.
- **Cod client**: CUI (implicit) sau codul SAGA al partenerului, completat cu zerouri dacă se dorește.
- **Perioade lungi**: cereri de cel mult 100 de facturi (configurabil), îmbinate de server într-un fișier din fiecare fel; progresul și mesajele sunt pe export, iar o cerere fără răspuns se retrimite după 10 minute.
- **Mai puține date personale**: telefonul și e-mailul clienților nu se trimit decât dacă se alege; datele facturilor din cerere se golesc după răspuns; serverul nu păstrează facturile, iar mesajele răspunsurilor rămân 30 de zile în jurnalul cererilor.
- **Credite**: fiecare factură exportată se taxează în contul Terrabit (o factură reexportată în 30 de zile e gratuită); creditele se văd și se cumpără din *Setări > Credite Terrabit*.
- Tokenul serviciului rămâne la administratori; utilizatorii de facturare exportă fără să citească serviciul SAGA.
- Configurare: serviciul **SAGA Export** se activează în *Setări > Credite Terrabit > Servicii și credite* (administrator); pe pozițiile fiscale se completează *Tip SAGA* și *TVA la încasare (SAGA)*; fără CUI ca cod client, se completează *Cod client SAGA* pe parteneri. Fluxul detaliat este în fișa consultantului.

#### 3. Dependențe

- `deltatech_iap_online`
- `account`

#### 4. Componente Cheie

**Modele**

- `x_saga_export` (model definit prin date, fără Python): exportul unei perioade, cu starea, progresul, arhiva și mesajele.
- `x_iap_online_service` (extins prin date): setările serviciului SAGA (cod client, TVA la încasare, facturi mixte, un fișier per fel, format dată, facturi per cerere).
- `res.partner` și `account.fiscal.position` (extinse în vizualizări): codul SAGA al clientului, tipul SAGA și TVA la încasare.

**Vizualizări**

- `view_x_saga_export_form`, `view_x_saga_export_list`: formularul și lista exporturilor, cu meniul `menu_x_saga_export`.
- `view_account_position_form`: tipul SAGA pe poziția fiscală.
- `view_partner_form`: codul SAGA al clientului.
- Vizualizarea serviciului Terrabit cu grupul de setări **SAGA Export**.

**Acțiuni Automate / Acțiuni Server**

- *Export to SAGA*: pornește exportul perioadei.
- *SAGA: apply the answer of the service*: aplică răspunsul serviciului pe export (arhivă, mesaje, progres).

#### 5. Conexiuni

- [deltatech_saga_xml](../deltatech_saga_xml/index.md): construiește fișierele XML SAGA pe serverul Terrabit pentru bazele care nu rulează Python.
- [deltatech_saga](../deltatech_saga/index.md): interfața SAGA clasică (export/import prin fișiere) pentru instalările pe care se poate rula Python.
- `deltatech_iap_online`: serviciile și creditele Terrabit prin care se trimit cererile.
