# Interfață SAGA

- **Nume Tehnic:** `deltatech_saga`
- **Versiune:** `20.0.6.26.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_saga
- **Cale Locală:** `odoo-addons/bitshop/deltatech_saga`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Interfața Deltatech SAGA este un modul cuprinzător conceput pentru a facilita schimbul de date între Odoo și SAGA, un program de contabilitate larg răspândit în România. Această punte de integrare asigură transferul fără probleme al datelor contabile și de stoc între cele două sisteme, eliminând necesitatea introducerii manuale a datelor și reducând riscul de erori. Modulul se adresează companiilor care își gestionează operațiunile în Odoo, dar își păstrează evidența contabilă în SAGA, și este adaptat specific cerințelor fiscale și contabile din România. Integrarea este bazată pe fișiere (export/import), nu pe sincronizare în timp real prin API.

#### 2. Funcționalități Cheie

- Export de date contabile din Odoo către SAGA (clienți și furnizori, facturi de achiziție, facturi de vânzare inclusiv în valută, note contabile, încasări/plăți).
- Import de date din SAGA în Odoo (clienți și furnizori, facturi de achiziție, facturi de vânzare, note contabile) — util atât pentru sincronizarea curentă, cât și, la pornirea unei implementări peste o bază SAGA existentă, pentru preluarea inițială a nomenclatoarelor de parteneri și articole cu codurile SAGA originale, înainte de primul export.
- Export/import de parteneri și contacte, cu două câmpuri de referință pentru codurile de Client și de Furnizor din SAGA pe partener.
- Export/import de produse și stocuri; categoriile de produse au un câmp nou pentru tipul de articol SAGA.
- Suport pentru cerințele fiscale și contabile românești, inclusiv tratamente speciale (TVA la încasare, deductibilitate limitată 50%, taxare inversă).
- Maparea configurabilă a pozițiilor fiscale și corelarea codurilor de taxe; taxele au un câmp pentru tipul de deducere SAGA (indexul „N50" pentru deductibilitate limitată 50%, „I" pentru nedeductibilitate totală).
- Suport pentru ambele formate de schimb de date: XML (recomandat pentru versiunile noi de SAGA) și DBF.
- Generarea automată a codurilor SAGA pentru parteneri folosind secvențe sau codul de TVA.
- Câmp „Gestiune" pe factură pentru a indica locația de stoc folosită la exportul cantitativ-valoric.
- Asistentul de export are un câmp „Tip dată" — *Data documentului* (selectează după data contabilă, exportul lunar obișnuit) sau *Data modificării* (selectează după data de creare, pentru exporturi incrementale, filtrând și partenerii creați/modificați în interval) — și un câmp „Tip export" cu valorile *Global-Valoric* (parteneri, facturi, note contabile, plăți) sau *Cantitativ-Valoric* (adaugă fișierul de articole și mișcările de consum/producție).
- O singură rulare a exportului generează o arhivă ZIP unică (`ExportOdoo_<de la>_<până la>.zip`) cu toate fișierele relevante perioadei: parteneri, articole (doar cantitativ-valoric), facturi RON/valută pe intrări și ieșiri, note contabile, încasări/plăți și mișcări de consum/producție.
- Coloana `TIP` din exportul facturilor reflectă natura documentului (factură normală, bon fiscal cu factură, bon fiscal fără factură, bon cu CIF, sau un cod SAGA prioritar setat pe poziția fiscală precum `T` taxare inversă sau `A` aviz) — determinată din integrarea cu `deltatech_sale_store`, dacă e instalat, sau din flag-ul jurnalului de bonuri fiscale ca rezervă.
- La finalul exportului de facturi, wizard-ul afișează un sumar HTML al operațiunilor exportate și o secțiune de reconciliere (total venituri clasa 7 vs. total exportat pe `TIP`), utilă pentru a depista notele contabile manuale sau documentele de furnizor înregistrate greșit pe cont de venit.
- **Istoric exporturi** (**Accounting → Accounting → Saga → SAGA Exports**, model `saga.export`): fiecare export (clasic, pas cu pas sau trimis prin API) se păstrează cu perioada, jurnalele, opțiunile, utilizatorul, data, arhiva ZIP, mesajele exportului și răspunsul SAGA, numărul de facturi și de parteneri exportați; arhiva se poate descărca oricând, iar **Export again** redeschide asistentul cu aceeași perioadă și aceleași opțiuni. Înregistrările sunt limitate la companiile utilizatorului.
- **Trimitere în SAGA prin API** (butonul **Send to SAGA**, doar pentru fișierele XML; blocul *SAGA Web API* din setările contabilității): fiecare fișier XML al arhivei se încarcă, rezultatul fiecăruia se vede pe export, iar starea devine *Sent to SAGA* sau *Sent with errors*. Fișierele de furnizori, clienți și articole (`FUR_`, `CLI_`, `ART_`) pleacă primele. Butonul nu se apasă a doua oară (retrimite tot, cu risc de dublare); notele contabile (`NC_`) și fișierele de stoc (`BC_`, `PRODUCTIE_`) există doar în DBF și nu se trimit prin API.
- **Comparare stocuri cu SAGA** (**Accounting → Accounting → Saga → Stock comparison**, `saga.stock.compare`): compară stocul din Odoo cu cel din SAGA Web pe locații cu *Code SAGA*, cu linii colorate pe stare (*Equal*, *Different quantity*, *Not found in Odoo*, *Not found in SAGA*); are doar rol informativ și nu corectează nimic.
- Facturile și notele de credit făcute dintr-o comandă de **Point of Sale** se exportă cu `TIP` „f” (factură cu bon fiscal), indiferent de jurnal sau de flag-ul *Sale from store*; un cod SAGA pus pe poziția fiscală rămâne prioritar. La exportul XML, `<ClientTara>` poartă țara clientului.
- Opțiuni suplimentare la export: *Use product's account* (la facturile de furnizor, produsele stocabile folosesc contul de evaluare al categoriei, doar cu inventar permanent), *Mixed reverse charge invoices* (facturi cu linii de taxare inversă și linii cu TVA normal: nu se exportă / tip T / fără tip), *Export only cash payments*, *Include cancelled documents*, *Ignore Errors*. La import: *Skip existing*, *Reset partner code*, *Import With Delay* (prin `queue_job`, dacă e instalat), *Negative Accounting*.
- Ordinea recomandată de import al fișierelor în SAGA: parteneri (Furnizori/Clienți) → articole → facturi (IN/IE/INV/IEV) → note contabile (NC) → încasări/plăți (I/P); nu se importă simultan fișierele DBF și XML generate din același export, pentru că ar duplica înregistrările în SAGA.
- Pentru Odoo Community, utilizatorii trebuie incluși în grupul „Show Full Accounting Features" pentru a accesa meniul de export SAGA.

#### 3. Dependențe

- `base`
- `account`
- `stock`
- `purchase_stock`
- `sale_stock`
- [deltatech_contact](../deltatech_contact/index.md)
- `l10n_ro`
- [deltatech_task_progress](../deltatech_task_progress/index.md): bara de progres pentru exportul și importul rulate pe fundal (`task.progress.mixin`).

#### 4. Componente Cheie

*Conform fluxului de ingestie, secțiunea „Componente Cheie" este omisă deoarece modulul dispune de fișierul `readme/DESCRIPTION.md` (completat de `readme/CONFIGURE.md` și `readme/USAGE.md`), care a fost folosit pentru Sumar și Funcționalități Cheie. Fluxul pas cu pas, cu capturi, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).*

#### 5. Conexiuni

- [deltatech_task_progress](../deltatech_task_progress/index.md): progresul exportului și al importului rulate pe fundal.
- [deltatech_contwin](../deltatech_contwin/index.md): modul înrudit de export contabil (interfață către WinMentor / Contwin), documentat în paralel ca alternativă pentru schimbul de date contabile pe piața RO.
- [deltatech_sale_store](../deltatech_sale_store/index.md): furnizează flag-ul „Sale from store" propagat pe factură/comandă, folosit pentru a determina automat coloana `TIP` (`f`) la exportul facturilor emise pe bon fiscal.
- [deltatech_saga_mrp](../deltatech_saga_mrp/index.md): extensie opțională care adaugă exportul consumurilor și producției din MRP la exportul cantitativ-valoric.
- [l10n_ro_doc_screenshots](../l10n_ro_doc_screenshots/index.md): mixin-ul folosit de `tests/test_screenshots.py` pentru generarea reproductibilă a capturilor din fișa consultant.
