# Purchase UBL (localizat la `deltatech_purchase_ubl/index.md`)

- **Nume Tehnic:** `deltatech_purchase_ubl`
- **Versiune:** `19.0.1.4.19`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_purchase_ubl
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_ubl`
- **Ultima Ingestie:** `2026-10-21`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul importă facturile de la furnizori (în format UBL XML, iar prin extensii și PDF) și le folosește pentru a actualiza fluxurile de achiziție din Odoo. Pe baza documentului, modulul identifică furnizorul și comanda de achiziție, potrivește produsele, actualizează prețurile de la furnizor, poate valida recepția de stoc și poate genera factura de la furnizor. Din versiunea 19.0.1.4.19, butonul de pe comanda de achiziție și titlul asistentului se numesc **Import Invoice** („Import factură”), în loc de „Import UBL”, deoarece asistentul primește și PDF-ul facturii (prin [deltatech_ai_purchase_pdf](../deltatech_ai_purchase_pdf/index.md)). Valoarea de afaceri principală este reducerea muncii manuale și a erorilor la prelucrarea documentelor de achiziție.

#### 2. Funcționalități Cheie

- **Rezolvare automată a furnizorului și a comenzii:** asistentul păstrează comanda de achiziție selectată și poate identifica furnizorul și comanda din document (`OrderReference`, codul fiscal al furnizorului, numele furnizorului) când contextul nu mai e disponibil. Codurile fiscale se compară fără spații și fără prefixul RO. O comandă goală creată prin butonul Upload din lista de achiziții (furnizor = utilizatorul curent sau compania) își preia furnizorul din document; un furnizor necunoscut oprește importul cu un mesaj.
- **Potrivire automată a produselor:** după cod de bare (GS1/EAN), cod de furnizor, referință internă sau nume exact.
- **Integrare cu comanda de achiziție:**
    - liniile existente care se potrivesc sunt actualizate (cantitate, preț, discount), iar liniile al căror produs nu e încă pe comandă sunt adăugate, nu ignorate;
    - asistentul avertizează înainte de import când comanda are deja linii, ca utilizatorul să verifice ce se schimbă;
    - fără comandă rezolvată, asistentul poate totuși identifica furnizorul din document și actualiza prețurile de la furnizor.
- **Previzualizare cu potrivire pe culori:** fluxul interactiv are doi pași. „Preview” afișează câte un rând per linie de factură, cu produsul găsit și modul de potrivire: verde = cod de furnizor sau cod de bare, galben = doar nume, roșu = fără potrivire. Fiecare rând are o acțiune: *Use product* (alt produs), *Create new product* sau *Ignore*; liniile fără produs sunt ignorate implicit, iar un produs nou se creează doar la alegerea explicită. Coloana de descriere se numește „Vendor Description”, deoarece liniile pot veni și din PDF.
- **Gestionarea prețurilor:** actualizează prețurile de la furnizor în `product.supplierinfo` direct din date, fără a suprascrie rândul altei variante a aceluiași produs.
- **Suport pentru reduceri:** extrage reducerile de linie din `AllowanceCharge` (`ChargeIndicator=false`) și le aplică drept reduceri procentuale.
- **Unități de măsură:** cantitățile și prețurile sunt convertite din `unitCode` în unitatea liniei de comandă (ex. GRM către kg), cu mapări uzuale (C62, KGM, LTR etc.) și avertismente când conversia nu e posibilă.
- **Verificarea totalului și a TVA:** comanda este comparată cu documentul pe valoarea fără TVA și, când documentul o indică, pe totalul cu TVA; jurnalul le arată pe ambele. Orice diferență oprește importul direct și deschide previzualizarea. O linie al cărei TVA diferă de cota din document este doar raportată în jurnal (TVA-ul se corectează din produse/poziția fiscală). Taxarea inversă sau intracomunitară contează ca 0% pentru documente K/AE, dar este raportată pentru documente scutite/zero/în afara sferei/export (E, Z, O, G).
- **Facturi de credit:** o notă de credit furnizor (document CreditNote sau Invoice cu cod 381) este recunoscută și nu se importă; comanda rămâne neschimbată, iar jurnalul afișează un avertisment.
- **Automatizare de stoc:** validează opțional recepția asociată, potrivind cantitățile din document; la facturi parțiale, restul merge în backorder. Liniile de servicii cu politică de facturare „la recepție” (ex. eco-taxe) sunt marcate manual ca recepționate.
- **Contabilitate:** creează și leagă opțional factura de la furnizor din comanda de achiziție, doar dacă comanda e confirmată (`purchase`/`done`), mai are ceva de facturat și toate liniile au fost potrivite (altfel factura e omisă, cu motivul în jurnal). Cota 0% explicită (Z, E, O, G) se aplică pe factură; existența unei facturi cu același număr se verifică doar în compania comenzii.
- **Execuții automate controlate:** importul headless (ex. mesaje SPV atașate pe comenzi) respectă cheia de context `purchase_ubl_no_new_products` (nu creează produse duplicate) și, când totalul nu se potrivește sau rămân linii nepotrivite, programează pe comandă o activitate „SPV import needs review”, atribuită cumpărătorului, cu jurnalul colorat în notă. Activitatea nu se dublează la reprocesare.
- **Jurnal lizibil:** mesaje colorate pe nivel (✅ ⚠️ ❌ ℹ️), setat la sursă și în limba utilizatorului; prețurile actualizate sunt rezumate într-un singur mesaj; textele spun „document sursă”.
- **Traduceri RO** și pictogramă proprie.

Logica de potrivire produse/preț/recepție/facturare este în mixin-ul comun `purchase.invoice.import.mixin`, reutilizabil de alte asistente de import (ex. PDF). Punctul de extensie `_parse_source` permite altor module să citească alte formate de fișier cu aceeași previzualizare, potrivire și creare de factură; acest asistent păstrează doar partea specifică UBL-XML.

#### 3. Dependențe

- `purchase_stock`
- `account`

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, funcționalitatea principală este expusă printr-un asistent (wizard) de import (`purchase.ubl.import.wizard`, buton „Import Invoice” pe comanda de achiziție) care orchestrează rezolvarea furnizorului/comenzii, potrivirea produselor, actualizarea prețurilor, validarea recepției și crearea facturii de la furnizor, pe baza logicii comune din mixin-ul `purchase.invoice.import.mixin`. (Detalierea modelelor/vizualizărilor nu a fost extrasă din cod, conform fluxului de ingestie bazat pe Readme.)

#### 5. Conexiuni

- [deltatech_ai_purchase_pdf](../deltatech_ai_purchase_pdf/index.md): extinde asistentul prin `_parse_source`, ca să importe și PDF-ul facturii; motivul redenumirii butonului în „Import Invoice”.
- [deltatech_purchase_ubl_ai](../deltatech_purchase_ubl_ai/index.md): propune cu AI produsul pentru liniile pe care potrivirea standard nu le-a asociat.
- `purchase_stock`: actualizează liniile comenzii, prețurile de la furnizor și validează recepția de stoc asociată.
- `account`: creează și leagă opțional factura de la furnizor pornind de la comanda de achiziție.
- `l10n_ro_message_spv_purchase`: apelant automat care atașează XML-ul SPV pe comenzi de achiziție.
