# RMA - Returns and Warranty Claims (localizat la `deltatech_rma/index.md`)

- **Nume Tehnic:** `deltatech_rma`
- **Versiune:** `19.0.1.4.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_rma
- **Cale Locală:** `odoo-addons/bitshop/deltatech_rma`
- **Ultima Ingestie:** 2026-09-24
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul gestionează returul comercial și reclamațiile de garanție pentru vânzările online și B2B: clientul deschide cererea direct din comanda proprie, fișa de retur se generează cu cod de bare, iar coletul se recepționează în depozit prin scanare. Este vorba despre returul *comercial* — produs defect, articol greșit, piesă necorespunzătoare — un act diferit de retragerea legală de 14 zile (dreptul unilateral al consumatorului), acoperită de modulul [deltatech_sale_withdrawal](../deltatech_sale_withdrawal/index.md): acolo comerciantul confirmă primirea, aici comerciantul decide.

#### 2. Funcționalități Cheie

- Cerere de retur deschisă de client din portal, pe fiecare linie de comandă, cu poze și video.
- Curierul pe cerere (`carrier_id`), preluat din metoda de livrare a comenzii și modificabil. Apare în formular, în listă, la căutare și la grupare.
- IBAN-ul pentru rambursare cerut direct în formularul din portal, doar la cererile care se pot încheia cu banii înapoi (renunțare și produs greșit, nu garanție). Câmpul e opțional; un IBAN completat se verifică după ISO 13616 (țară, lungime, suma de control mod 97), iar unul greșit întoarce clientul la formular. Aceeași verificare se aplică și în back office. Validatorul e scris în modul: `stdnum.iban` nu se poate importa în procesul Odoo 19, iar `base_iban` ar începe să valideze conturile bancare ale tuturor partenerilor.
- Fișă de retur PDF cu cod de bare, trimisă clientului prin e-mail pentru a fi pusă în colet.
- Recepție în depozit prin scanare: un singur câmp, se scanează codul de bare al fișei sau AWB-ul de retur, iar produsele așteptate se deschid direct pentru verificare.
- Verdict pe fiecare produs — bun, defect confirmat, fără defect constatat, deteriorat, lipsă.
- Motive de retur configurate ca date, nu ca cod: fiecare motiv are propriul interval de taxă de manipulare, obligativitatea pozelor și cine plătește transportul de retur.
- Decizie finală — înlocuire, reparație, rambursare, refuz — cu e-mail automat către client.
- Produsele cu verdict „bun" reintră în stoc prin transferul standard de retur al Odoo, legat de livrarea pe care o anulează.
- Registru de retururi cu vechime (ageing), pe companie, cu reguli de înregistrare astfel încât fiecare client își vede doar propriile cereri.
- Flux client din portal (**Returns and Warranty Claims** din *My Account* sau butonul de pe comanda confirmată): alege tipul cererii (produs defect / articol greșit / retur), bifează produsele și cantitatea, motivul pe fiecare produs, descrierea problemei și pozele. Când un produs bifat are un motiv care cere poze, eticheta câmpului trece din „opțional" în „obligatorii la motivul ales", iar formularul fără poze se oprește chiar în pagină, cu mesajul lângă câmp, fără drum la server. Serverul verifică oricum încă o dată: un fișier care nu se deschide ca imagine respinge formularul înainte de creare, ca să nu rămână o cerere fără dovezi. Mesajele verificărilor din pagină sunt traduse ca restul șablonului.
- Flux echipă din back office (**Returns → Returns and Warranty Claims**): **Approve and Send the Slip** trimite fișa cu cod de bare (blocat dacă motivul cere poze și acestea lipsesc); **Returns → Parcel Check-in (Scan)** este ecranul de depozit, tolerant la spații, cratime, slash-uri și majuscule, cu avertizare la AWB regăsit pe mai multe cereri sau la scanare dublă; **All Good** marchează tot coletul cu verdict bun dintr-o singură apăsare; **Put Back In Stock** creează transferul de retur doar pentru liniile cu verdict bun; închiderea cu rambursare cere IBAN, iar de acolo se pot genera **Credit Note**, **Replacement Order** sau **Ship Back To Customer**. Transferul de ieșire creat de **Ship Back To Customer** primește curierul cererii, așa că AWB-ul îl generează conectorul curierului. Coletul care intră de la client nu primește curier, pentru că AWB-ul lui l-a făcut clientul.
- Sumele cererii (*Total*, *Taxă de manipulare*, *De returnat clientului*) sunt **cu TVA**, la prețul vândut după discount, calculate cu motorul de taxe al facturilor Odoo 19 din aceleași valori și cu aceeași rotunjire ca nota de credit: suma afișată clientului în portal și pe fișă e, la ban, totalul notei; taxa de manipulare iese prin diferență.
- **Credit Note** stornează factura inițială: preț, discount, taxe (cota de la faptul generator) și unitate de măsură ale liniei de factură, taxa de manipulare compusă în discount, jurnalul, clientul, moneda și cursul facturii, legătura `reversed_entry_id`. Nota se leagă de linia comenzii (`sale_line_ids`) doar la politica „la livrare” cu returul fizic validat, ca comanda să nu fie refacturată; un produs nefacturat nu primește notă (se ajustează comanda). Trimiterea structurată la factura inițială în XML-ul e-Factura (BillingReference) nu e încă completată de localizare.
- Puncte de extindere pentru retururile care se cer în alt canal: `sale.order._rma_external_return_channel()` (implicit `False`) scoate comanda din formularul de retur din portal, înlocuiește butonul de pe pagina comenzii cu indicația canalului și pune un avertisment pe o cerere deschisă de mână (`external_return_warning`). Le folosește [deltatech_rma_marketplace](../deltatech_rma_marketplace/index.md). O a doua notă de credit pe aceeași factură e semnalată pe cerere.
- **Returns → Analysis** arată retururile pe lună și tip, plus rata de retur per produs (raportat la cantitățile vândute).
- Configurare în **Returns → Configuration → Return Reasons** (categorie, interval taxă, obligativitate poze/video, cine plătește transportul, explicația afișată clientului, opțiunea *Staff Only* pentru motive interne) și în **Settings → Sales → Returns and Warranty Claims** (accesul automat al colegilor, fereastra de eligibilitate, termenele promise clientului, opțiunea de motiv obligatoriu, taxa de manipulare implicită). Explicația afișată clientului la fiecare motiv e traductibilă. Termenele promise sunt *Answer Within* (zile lucrătoare, implicit 1) și *Check Within* (implicit 0, adică nu se promite niciun termen). Apar în portal, în e-mailul de aprobare și pe fișa de retur; frazele sunt termeni de traducere întregi, cu `{days}` înlocuit la afișare.
- Cele trei e-mailuri (aprobat, refuzat, rezolvat) sunt șabloane `noupdate`, editabile din **Settings → Technical → Email Templates**. Modificările rămân la actualizarea modulului. Migrarea spre `19.0.1.2.0` le reîncarcă o singură dată, cu textul nou: până atunci, orice actualizare scria peste ele.
- Opțiunea *Not Returnable* pe produs sau categorie exclude transportul, taxele de manipulare și serviciile din formularul clientului; serviciile și linia de transport adăugată de metoda de livrare (`is_delivery`) sunt oricum excluse automat.
- Două grupuri de securitate: **User** (gestionează cererile) și **Manager** (configurează motive, etichete și motive de închidere, poate șterge o cerere). La instalare, orice utilizator intern devine automat **User**, ca în `agroamat_retururi`. Accesul automat se poate opri din setări, cu opțiunea *All Internal Users Handle Returns*; după asta, accesul rămâne doar celor cărora li s-a dat explicit, iar actualizarea modulului nu îl mai repornește. O bază actualizată de pe `19.0.1.0.0`, versiune care nu avea opțiunea, primește accesul automat o singură dată, prin scriptul `migrations/19.0.1.1.1/post-migration.py`. Scriptul nu atinge bazele aflate deja pe `19.0.1.1.0`: acolo lipsa regulii înseamnă că a fost oprită deliberat.

#### 3. Dependențe

- `sale_stock`
- `portal`
- `stock_delivery` (aduce și `delivery`): curierul de pe comandă și cel de pe transferul de ieșire. A intrat în `19.0.1.2.0` direct în modul, fără punte separată, fiind vorba de un singur câmp.

#### 4. Componente Cheie

Documentația acestei secțiuni se bazează pe fișierul `readme/DESCRIPTION.md` și pe `readme/USAGE.md` / `readme/CONFIGURE.md`, care nu detaliază componentele tehnice individuale (modele, vizualizări, acțiuni server). Conform fluxului de ingestie, analiza codului pentru aceste elemente a fost omisă, deoarece Readme-ul este prezent și nu solicită explicit această analiză. Fluxul operațional pas-cu-pas este documentat integral în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 5. Conexiuni

- [deltatech_sale_withdrawal](../deltatech_sale_withdrawal/index.md): acoperă retragerea legală de 14 zile (dreptul unilateral al consumatorului), un act distinct de returul comercial gestionat de acest modul.
- `sale_stock`: transferul standard de retur folosit la „Put Back In Stock" și legătura cu livrarea originală.
- `stock_delivery` / `delivery`: curierul cererii, preluat de pe comandă; transferul „Ship Back To Customer” pleacă pe el, iar AWB-ul îl face conectorul curierului.
- `mail`: infrastructura de e-mail și șabloanele folosite pentru trimiterea fișei de retur și notificarea deciziei finale.
- [deltatech_rma_lot](../deltatech_rma_lot/index.md): punte — lot / serie pe linia de retur, verificat față de livrare și dus pe transferul de retur.
- [deltatech_rma_withdrawal](../deltatech_rma_withdrawal/index.md): punte — retragerea în 14 zile își ia fișa cu cod de bare și recepția prin scanare de aici.
- [deltatech_rma_helpdesk](../deltatech_rma_helpdesk/index.md): punte (Enterprise) — cerere de retur deschisă dintr-un tichet de Helpdesk, cu rezultatul scris înapoi pe tichet.
- [deltatech_rma_marketplace](../deltatech_rma_marketplace/index.md): punte — retururile eMAG / Shopify pe fluxul de depozit, cererea născută la recepție, rambursarea marketplace-ului lângă nota de credit.
