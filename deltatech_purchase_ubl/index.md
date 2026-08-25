# Deltatech Purchase UBL (localizat la `deltatech_purchase_ubl/index.md`)

- **Nume Tehnic:** `deltatech_purchase_ubl`
- **Versiune:** `19.0.1.3.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_purchase_ubl
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_ubl`
- **Ultima Ingestie:** `2026-08-25`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul importă facturi de la furnizori în format UBL XML (Universal Business Language) și le folosește pentru a actualiza fluxurile de achiziție din Odoo. Pe baza fișierului XML, modulul identifică furnizorul și comanda de achiziție, potrivește produsele, actualizează prețurile de la furnizor, poate valida recepția de stoc și poate genera factura de la furnizor. Valoarea de afaceri principală este reducerea muncii manuale și a erorilor la prelucrarea documentelor electronice de achiziție.

#### 2. Funcționalități Cheie

- **Rezolvare automată a furnizorului și a comenzii:** asistentul (wizard) păstrează comanda de achiziție selectată și poate, de asemenea, identifica furnizorul și comanda din XML (`OrderReference`, codul fiscal al furnizorului, numele furnizorului) atunci când contextul nu mai este disponibil.
- **Potrivire automată a produselor:** produsele sunt potrivite după cod de bare (GS1/EAN), cod de furnizor, referință internă sau nume exact.
- **Integrare cu comanda de achiziție:**
    - când comanda are deja linii, importul actualizează doar liniile existente care se potrivesc;
    - liniile noi din XML nu sunt adăugate la o comandă existentă cu linii, iar asistentul afișează acest avertisment înainte de import;
    - liniile noi neconsumate (produse care nu erau pe comanda originală, ex. o linie de „Ecovaloare" adăugată de furnizor) sunt totuși adăugate ca linii noi pe comandă;
    - când nu se rezolvă nicio comandă, asistentul poate totuși identifica furnizorul din XML și actualiza prețurile de la furnizor.
- **Gestionarea prețurilor:** actualizează prețurile de la furnizor în `product.supplierinfo` direct din datele XML.
- **Suport pentru reduceri:** extrage reducerile de pe linii din `AllowanceCharge` (`ChargeIndicator=false`) și le aplică drept reduceri procentuale pe liniile comenzii de achiziție.
- **Verificarea totalului:** compară totalul comenzii cu totalul din XML (`PayableAmount` / `TaxInclusiveAmount`, cu revenire la valoarea fără taxe) și afișează un avertisment când există o diferență.
- **Automatizare de stoc:** validează opțional recepția de stoc asociată, potrivind cantitățile din XML; liniile de servicii cu politică de facturare „la recepție" (ex. taxele de eco-tax) sunt marcate manual ca recepționate, deoarece nu au mișcări de stoc.
- **Contabilitate:** creează și leagă opțional o factură de la furnizor pornind de la comanda de achiziție. Factura se creează automat când documentul sursă identifică un număr de factură, dar numai dacă înainte comanda a fost confirmată (`state` în `purchase`/`done`) — pentru a evita generarea unor facturi „fantomă" cu cantități zero pe comenzi neconfirmate.
- **Produse lipsă:** opțiune de creare automată a produselor lipsă folosind datele din fișierul UBL.
- **Previzualizare cu potrivire pe culori** (nou în 19.0.1.3.0, ticket #9315): fluxul interactiv (butonul „Importă UBL” de pe comandă) are acum doi pași — „Preview” analizează XML-ul și afișează câte o linie per articol din factură, cu produsul identificat de algoritm și modul în care a fost găsit, codificat pe culori: verde = potrivire după cod de furnizor sau cod de bare (sigură), galben = potrivire doar după nume (de verificat), roșu = nicio potrivire (s-ar crea un produs nou). Utilizatorul poate alege manual alt produs pe orice linie înainte de a confirma; alegerea manuală înlocuiește potrivirea automată (`_process_invoice_data(product_map=...)`). Punctul de intrare headless `action_import` rămâne neschimbat, deci apelanții automatizați funcționează în continuare.
- **Creare de produse controlată pe fluxul automat** (fix în 19.0.1.3.0, ticket #9315): `_process_attachments_for_post` rula întotdeauna importul headless cu `create_missing_products=True`. Era în regulă pentru wizard-ul interactiv, unde un utilizator revizuiește ce se creează, dar era și singurul punct de intrare pentru atașamentele XML postate de apelanți automatizați (ex. `l10n_ro_message_spv_purchase`, care atașează XML-ul SPV pe comenzi de achiziție create înainte ca factura să existe). Când linia din factura sursă nu avea cod de furnizor și numele nu se potrivea exact cu un produs existent, importul headless crea în tăcere un produs duplicat, nerevizuit de nimeni. Acum, `_process_attachments_for_post` respectă cheia de context `purchase_ubl_no_new_products`: când e setată, importul headless rulează cu `create_missing_products=False`, iar liniile nepotrivite rămân în jurnalul „produse nepotrivite” al wizard-ului, în loc să creeze un produs.

Modulul suportă namespace-urile standard UBL Invoice și mapările uzuale de coduri de unitate de măsură (C62, KGM, LTR etc.).

Logica de potrivire produse/preț/recepție/facturare este extrasă într-un mixin comun (`purchase.invoice.import.mixin`), reutilizabil și de alte asistente de import facturi (ex. PDF pentru Marso, Delta, Sigemo, Procar); acest wizard păstrează doar partea specifică UBL-XML (parsare XML, detecție format, unități de măsură).

#### 3. Dependențe

- `purchase_stock`
- `account`

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, funcționalitatea principală este expusă printr-un asistent (wizard) de import UBL (`purchase.ubl.import.wizard`) care orchestrează rezolvarea furnizorului/comenzii, potrivirea produselor, actualizarea prețurilor, validarea recepției și crearea facturii de la furnizor, pe baza logicii comune din mixin-ul `purchase.invoice.import.mixin`. (Detalierea modelelor/vizualizărilor nu a fost extrasă din cod, conform fluxului de ingestie bazat pe Readme.)

#### 5. Conexiuni

- `purchase_stock`: actualizează liniile comenzii de achiziție, prețurile de la furnizor și validează recepția de stoc asociată, potrivind cantitățile din XML.
- `account`: creează și leagă opțional factura de la furnizor pornind de la comanda de achiziție.
