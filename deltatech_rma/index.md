# RMA - Returns and Warranty Claims (localizat la `deltatech_rma/index.md`)

- **Nume Tehnic:** `deltatech_rma`
- **Versiune:** `19.0.1.1.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_rma
- **Cale Locală:** `odoo-addons/bitshop/deltatech_rma`
- **Ultima Ingestie:** 2026-09-23
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul gestionează returul comercial și reclamațiile de garanție pentru vânzările online și B2B: clientul deschide cererea direct din comanda proprie, fișa de retur se generează cu cod de bare, iar coletul se recepționează în depozit prin scanare. Este vorba despre returul *comercial* — produs defect, articol greșit, piesă necorespunzătoare — un act diferit de retragerea legală de 14 zile (dreptul unilateral al consumatorului), acoperită de modulul [deltatech_sale_withdrawal](../deltatech_sale_withdrawal/index.md): acolo comerciantul confirmă primirea, aici comerciantul decide.

#### 2. Funcționalități Cheie

- Cerere de retur deschisă de client din portal, pe fiecare linie de comandă, cu poze și video.
- IBAN-ul pentru rambursare cerut direct în formularul din portal, doar la cererile care se pot încheia cu banii înapoi (renunțare și produs greșit, nu garanție). Câmpul e opțional; un IBAN completat se verifică după ISO 13616 (țară, lungime, suma de control mod 97), iar unul greșit întoarce clientul la formular. Aceeași verificare se aplică și în back office. Validatorul e scris în modul: `stdnum.iban` nu se poate importa în procesul Odoo 19, iar `base_iban` ar începe să valideze conturile bancare ale tuturor partenerilor.
- Fișă de retur PDF cu cod de bare, trimisă clientului prin e-mail pentru a fi pusă în colet.
- Recepție în depozit prin scanare: un singur câmp, se scanează codul de bare al fișei sau AWB-ul de retur, iar produsele așteptate se deschid direct pentru verificare.
- Verdict pe fiecare produs — bun, defect confirmat, fără defect constatat, deteriorat, lipsă.
- Motive de retur configurate ca date, nu ca cod: fiecare motiv are propriul interval de taxă de manipulare, obligativitatea pozelor și cine plătește transportul de retur.
- Decizie finală — înlocuire, reparație, rambursare, refuz — cu e-mail automat către client.
- Produsele cu verdict „bun" reintră în stoc prin transferul standard de retur al Odoo, legat de livrarea pe care o anulează.
- Registru de retururi cu vechime (ageing), pe companie, cu reguli de înregistrare astfel încât fiecare client își vede doar propriile cereri.
- Flux client din portal (**Returns and Warranty Claims** din *My Account* sau butonul de pe comanda confirmată): alege tipul cererii (produs defect / articol greșit / retur), bifează produsele și cantitatea, motivul pe fiecare produs, descrierea problemei și pozele. Când un produs bifat are un motiv care cere poze, eticheta câmpului trece din „opțional" în „obligatorii la motivul ales", iar formularul fără poze se oprește chiar în pagină, cu mesajul lângă câmp, fără drum la server. Serverul verifică oricum încă o dată: un fișier care nu se deschide ca imagine respinge formularul înainte de creare, ca să nu rămână o cerere fără dovezi. Mesajele verificărilor din pagină sunt traduse ca restul șablonului.
- Flux echipă din back office (**Returns → Returns and Warranty Claims**): **Approve and Send the Slip** trimite fișa cu cod de bare (blocat dacă motivul cere poze și acestea lipsesc); **Returns → Parcel Check-in (Scan)** este ecranul de depozit, tolerant la spații, cratime, slash-uri și majuscule, cu avertizare la AWB regăsit pe mai multe cereri sau la scanare dublă; **All Good** marchează tot coletul cu verdict bun dintr-o singură apăsare; **Put Back In Stock** creează transferul de retur doar pentru liniile cu verdict bun; închiderea cu rambursare cere IBAN, iar de acolo se pot genera **Credit Note**, **Replacement Order** sau **Ship Back To Customer**.
- **Returns → Analysis** arată retururile pe lună și tip, plus rata de retur per produs (raportat la cantitățile vândute).
- Configurare în **Returns → Configuration → Return Reasons** (categorie, interval taxă, obligativitate poze/video, cine plătește transportul, explicația afișată clientului, opțiunea *Staff Only* pentru motive interne) și în **Settings → Sales → Returns and Warranty Claims** (accesul automat al colegilor, fereastra de eligibilitate, opțiunea de motiv obligatoriu, taxa de manipulare implicită). Explicația afișată clientului la fiecare motiv e traductibilă.
- Opțiunea *Not Returnable* pe produs sau categorie exclude transportul, taxele de manipulare și serviciile din formularul clientului; serviciile sunt oricum excluse automat.
- Două grupuri de securitate: **User** (gestionează cererile) și **Manager** (configurează motive, etichete și motive de închidere, poate șterge o cerere). La instalare, orice utilizator intern devine automat **User**, ca în `agroamat_retururi`. Accesul automat se poate opri din setări, cu opțiunea *All Internal Users Handle Returns*; după asta, accesul rămâne doar celor cărora li s-a dat explicit, iar actualizarea modulului nu îl mai repornește. O bază actualizată de pe `19.0.1.0.0`, versiune care nu avea opțiunea, primește accesul automat o singură dată, prin scriptul `migrations/19.0.1.1.1/post-migration.py`. Scriptul nu atinge bazele aflate deja pe `19.0.1.1.0`: acolo lipsa regulii înseamnă că a fost oprită deliberat.

#### 3. Dependențe

- `sale_stock`
- `portal`

#### 4. Componente Cheie

Documentația acestei secțiuni se bazează pe fișierul `readme/DESCRIPTION.md` și pe `readme/USAGE.md` / `readme/CONFIGURE.md`, care nu detaliază componentele tehnice individuale (modele, vizualizări, acțiuni server). Conform fluxului de ingestie, analiza codului pentru aceste elemente a fost omisă, deoarece Readme-ul este prezent și nu solicită explicit această analiză. Fluxul operațional pas-cu-pas este documentat integral în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 5. Conexiuni

- [deltatech_sale_withdrawal](../deltatech_sale_withdrawal/index.md): acoperă retragerea legală de 14 zile (dreptul unilateral al consumatorului), un act distinct de returul comercial gestionat de acest modul.
- `sale_stock`: transferul standard de retur folosit la „Put Back In Stock" și legătura cu livrarea originală.
- `mail`: infrastructura de e-mail și șabloanele folosite pentru trimiterea fișei de retur și notificarea deciziei finale.
