# Services Equipment (localizat la `deltatech_service_equipment/index.md`)

- **Nume Tehnic:** `deltatech_service_equipment`
- **Versiune:** `19.0.1.1.13`
- **Cale:** https://github.com/dhongu/deltatech_service/tree/19.0/deltatech_service_equipment
- **Cale Locală:** `odoo-addons/deltatech_service/deltatech_service_equipment`
- **Ultima Ingestie:** `2026-09-24`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul leagă echipamentele din `deltatech_service_equipment_base` de contractele de service din
`deltatech_service_agreement` și transformă citirile de contor în facturi de vânzare. Aduce ciclul de
viață al echipamentului la client (Disponibil → Instalat, cu adresă și amplasament), asistenții de
**Instalare**, **Adaugă la contract** și dezinstalare (**Elimină din contract**), liniile de contract
legate de contor, calculul consumului din citirile nefacturate și anexa XLS de contoare a facturii.
Valoarea de afaceri constă în facturarea lunară corectă, pe pagină sau pe oră de funcționare, pentru
echipamentele închiriate sau întreținute cu plată pe consum.

#### 2. Funcționalități Cheie

- Ciclul de viață al echipamentului: **Disponibil → Instalat**, controlat doar prin asistenți
  (bara de stare a modulului de bază rămâne dezactivată funcțional pentru acest flux).
- **Creează contoare**: generează câte un contor pentru fiecare șablon al categoriei echipamentului;
  se rulează pe câte un echipament, înainte de instalare.
- **Instalare**: asistent cu client, locație (adresă), amplasament liber, dată și indexul fiecărui
  contor; creează citirile inițiale și scrie în istoric. Fluxul recomandat: Creează contoare →
  Instalare → Adaugă la contract.
- **Adaugă la contract**: leagă echipamentul de un contract deja creat (*Contracte → Nou*, cu
  partener, ciclu de facturare, tip și dată de contract nu mai târziu decât prima citire
  facturabilă); creează, pentru fiecare șablon de contor al categoriei, o linie de contract cu
  serviciul, contorul și unitatea de facturare.
- **Elimină din contract** (dezinstalare): asistent cu perioada de facturare a consumului rămas și
  indexul de la dezinstalare; pregătește consumul rămas, trece echipamentul în Disponibil fără
  client/contract și dezactivează liniile lui de contract.
- **Pregătire facturare** pe contract: pentru fiecare linie legată de un contor creează un consum a
  cărui cantitate este suma diferențelor tuturor citirilor încă nefacturate (nu doar cele din
  perioada aleasă), între data contractului/instalării și sfârșitul perioadei.
- **Necesită citiri pentru facturare** (pe tipul de contract): blochează pregătirea facturării pe
  contractele fără *Citiri efectuate*; excepție grupul **Poate factura fără citiri de contor**;
  facturarea automată programată sare aceste contracte fără avertisment.
- **Schimbă data facturii** pe consumuri, înainte de facturare, pentru a data factura la data ultimei
  citiri incluse (prestare cu decontări succesive, art. 281 alin. (7) și art. 319 alin. (16) din
  Legea 227/2015) — implicit vine din *Data următoarei facturi client* a contractului, care poate fi
  anterioară citirii facturate.
- **Facturare** din consum, cu grupare pe partener, contract sau linie de contract; scade *Cantitatea
  gratuită* a liniei de contract din cantitatea consumului.
- **Exportă contoarele în XLS** pe factură: echipament, serie, contor, adresă, index vechi, index nou
  și diferența, ca document justificativ al cantității facturate.
- **Istoric** (*Serviciu → Serviciu → Istoric echipament/contract*, sau butonul **Istoric amplasare**)
  al instalărilor, adăugărilor în contract și dezinstalărilor.
- **Creare automată a echipamentului** la crearea unei serii (lot) pentru un produs dintr-o categorie
  marcată *Tipul de echipament este obligatoriu*.
- Notă contabilă a facturii: 4111 = 704 (venituri din servicii, ex. pagină) sau 706 (venituri din
  chirie, dacă se facturează separat) + 4427; contul vine din produsul-serviciu, nu e decis de modul.

Fluxul complet de configurare (categorie contor, categorie echipament, tip contract), pas-cu-pas de
utilizare, exemplul numeric de facturare și tabelul de verificări pentru consultant sunt în
[FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_service_agreement](../deltatech_service_agreement/index.md)
- [deltatech_service_equipment_base](../deltatech_service_equipment_base/index.md)
- `analytic`
- `stock`

Dependențe externe Python: `xlwt`.

#### 4. Componente Cheie

Secțiune omisă: pagina urmează fișa consultant, care acoperă Sumarul, Funcționalitățile Cheie și
fluxul operațional; analiza suplimentară a codului pentru Modele/Vizualizări/Acțiuni nu e solicitată
explicit în fișă.

**Limitări cunoscute** (din fișa consultant, secțiunea de verificări și flux):

- Conversia unităților de măsură de facturare este inversată pe Odoo 19 — categoria de contor
  trebuie configurată cu *Unitatea de măsură pentru facturare* **egală** cu unitatea citirii.
- Citirea făcută la instalare este facturată față de *Valoarea inițială* a contorului (implicit 0):
  dacă nu se completează *Valoarea inițială* = indexul de la punere în funcțiune, prima factură ia
  tot indexul, nu doar consumul real.
- Poziția fiscală a clientului este ignorată la facturarea din consumuri — la clienți cu poziție
  fiscală (UE, export), taxa și contul se corectează manual pe factura în ciornă.
- *Data instalării* pe echipament se scrie mereu cu ziua curentă (nu cu data aleasă în asistent) și
  este rescrisă din nou de **Adaugă la contract**; se corectează manual, în fișa echipamentului,
  după ambele operații.
- **Adaugă la contract** propune indexul 0 la citiri; lăsat așa, creează o citire 0 care strică
  diferențele citirilor următoare — trebuie introdus manual indexul curent al fiecărui contor.
- Liniile de contract create de **Adaugă la contract** au prețul 1 — se completează manual prețul
  real pe fiecare linie, înainte de a pune contractul În curs.
- Dezinstalarea (**Elimină din contract**) pe o perioadă deja pregătită pentru facturare este
  refuzată („Trebuie să facturați consumul înainte de dezinstalare”) — se alege o perioadă
  încă nepregătită pentru acel contract.
- Numerotarea echipamentelor funcționează doar în compania principală (limitare moștenită din
  `deltatech_service_equipment_base`, relevantă la instalarea/crearea automată a echipamentelor în
  companii secundare).

#### 5. Conexiuni

- [deltatech_service_equipment_base](../deltatech_service_equipment_base/index.md): modulul de bază
  pentru echipamente, contoare, citiri și estimare; acest modul îi extinde ciclul de viață cu
  instalarea, contractul și facturarea.
- [deltatech_service_agreement](../deltatech_service_agreement/index.md): contractele de service,
  tipurile de contract, perioadele, consumurile, pregătirea facturării și facturarea pe care se
  bazează liniile legate de contor din acest modul.
- [deltatech_service_base](../deltatech_service_base/index.md): meniul, grupurile și ciclurile de
  facturare de bază ale suitei de service, moștenite prin `deltatech_service_agreement`.
- [deltatech_service_consumable](../deltatech_service_consumable/index.md): raportul de eficiență al
  consumabilelor folosește consumul pe perioadă al acelorași contoare gestionate aici.
