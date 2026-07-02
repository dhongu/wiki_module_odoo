# Fișă Modul: Retail fiscal / AMEF — Print to ECR from POS

**Poziție plan:** C19  
**Modul:** `deltatech_pos`  
**FR:** FR-47  
**Capitol manual:** Cap 12.13  
**Utilizator principal:** Responsabil magazin/POS, Casier, Consultant implementare  
**Prioritate:** Ridicată

---

## 1. Scop business

Modulul conectează Odoo POS la casa de marcat fiscală prin fișiere ECR generate la validarea
bonului sau a operațiunilor de numerar. Consultantul trebuie să îl prezinte ca un strat de
integrare operațională pentru retail fiscal: Odoo pregătește fișierul în formatul așteptat de
driverul AMEF, iar aplicația/driverul local al casei de marcat îl preia și îl tipărește.

Modulul nu face comunicare hardware directă și nu citește răspunsul fiscal înapoi în Odoo.

## 2. Bază legală și context

În România, vânzarea cu amănuntul cu numerar/card către populație se fiscalizează prin aparat de
marcat electronic fiscal (AMEF). În această implementare, `deltatech_pos` acoperă partea de
emitere a comenzii de tipărire fiscală din POS și operațiunile conexe:

- bon fiscal la validarea comenzii;
- cash in / cash out;
- raport X și raport Z;
- reimprimare manuală din backoffice a fișierului ECR deja generat.

Pentru raportarea D394 a bonurilor POS se folosește complementar
`l10n_ro_anaf_d394_pos`, nu acest modul.

## 3. Utilizatori și roluri

- Casier POS: emite bonul fiscal și operează cash in / cash out.
- Responsabil magazin: configurează POS-ul, metodele de plată și verifică sesiunile.
- Contabil / backoffice: poate reimprima fișierul fiscal al unei comenzi și verifică rapoartele X/Z.
- Consultant implementare: configurează tipul de ECR, extensia fișierului, prefixul și testează
  fiecare scenariu de fiscalizare.

## 4. Date implicate

- configurația POS (`pos.config`);
- metodele de plată POS și codul lor ECR (`pos.payment.method.cod_ecr`);
- comenzile POS (`pos.order`) și conținutul fișierului fiscal (`file`);
- sesiunile POS (`pos.session`);
- partenerul selectat pe comandă;
- fișierele descărcate pentru driverul AMEF: bon fiscal, cash opening, cash move, raport X/Z.

## 5. Configurare inițială

### Pasul 1 — Instalare și dependențe

1. Instalați `deltatech_pos_base`.
2. Instalați `deltatech_pos`.
3. Verificați că pe stația locală există driverul/utilitarul AMEF care preia fișierele generate de
   Odoo.

### Pasul 2 — Configurare ECR în POS

Mergeți la **Point of Sale → Configuration → Settings** și selectați POS-ul dorit.

Configurați:

- **Type of electronic cash register**: `FiscalWire`, `Optima`, `Daisy`, `Succes`,
  `FiscalNet` sau `Incotex`;
- **Trim long product name** și lungimea maximă, dacă modelul casei are limită strictă;
- **File prefix** și **File extension** pentru fișierul preluat de driver;
- **Cash In/Out** pentru operațiuni de numerar din POS;
- **Cash In/Out to ECR** pentru tipărirea dispozițiilor pe casa de marcat;
- **Print duplicate payment disposal** pentru al doilea exemplar la dispoziție;
- **Print order number as barcode** dacă driverul/modelul folosit suportă acest format.

### Pasul 3 — Configurare metode de plată

În **Point of Sale → Configuration → Payment Methods** completați **Cod ECR** pe fiecare metodă
de plată conform așteptărilor driverului local (de exemplu numerar, card etc.).

### Pasul 4 — Configurare jurnal pentru bonuri simplificate

În setările POS completați **Receipts Journal** dacă doriți generarea de documente contabile de tip
`out_receipt` în jurnal separat pentru bonuri/facturi simplificate.

## 6. Flux de utilizare

### Pasul 1 — Emiterea bonului fiscal din POS

1. Casierul adaugă produsele în POS și selectează metoda de plată.
2. La validarea comenzii, modulul pregătește fișierul ECR în funcție de tipul de casă configurat.
3. Fișierul este descărcat local cu prefixul și extensia configurate.
4. Driverul AMEF preia fișierul și tipărește bonul fiscal.

Pe bon se trimit:

- numele clientului, dacă este selectat;
- referința comenzii (`uuid`);
- nota generală a comenzii;
- liniile de produs, cantități, prețuri și TVA;
- discounturile și totalurile pe tipurile de plată;
- opțional, codul de bare al numărului comenzii.

### Pasul 2 — Deschidere casă și operațiuni cash in / cash out

1. La deschiderea sesiunii, dacă este activ `Cash In/Out to ECR` și suma de deschidere este
   pozitivă, se descarcă fișierul `cash_open.<ext>`.
2. Din POS, utilizatorul poate face **Cash collection** sau **Payment disposal**.
3. Pentru cash in / cash out, sistemul cere partener pe comandă și generează linia de numerar în
   sesiune.
4. Dacă opțiunea ECR este activă, se descarcă și fișierul `cash_move.<ext>` pentru tipărire pe AMEF.

### Pasul 3 — Rapoarte X și Z

Din popup-ul de închidere POS sau din sesiunea POS din backoffice se poate genera:

- **Print X**;
- **Print Z**.

Sistemul descarcă fișierul specific modelului ECR: `print_x.<ext>` sau `print_z.<ext>`.

### Pasul 4 — Reimprimare din backoffice

În **Point of Sale → Orders**, comanda plătită are:

- câmpul **receipt_print**;
- tabul **ECR data** cu textul fișierului;
- butonul **Print Fiscal Receipt** cât timp comanda este `paid` și bonul nu este marcat ca tipărit.

Acest flux este util când consultantul trebuie să regenereze local fișierul pentru driver fără să
refacă vânzarea.

## 7. Reguli funcționale

| Situație | Comportament |
|---|---|
| Comandă POS normală | se generează fișierul de bon fiscal la validare |
| Metodă de plată non-cash | totalul folosește `cod_ecr` al metodei de plată |
| Metodă de plată cash | totalul cash se trimite separat în fișierul ECR |
| Comandă cu note | nota generală și notele din structura bonului merg în fișierul ECR |
| Denumire produs prea lungă | se taie sau se continuă pe linii suplimentare, după setarea de trim |
| Caractere cu diacritice | sunt transformate în ASCII pentru compatibilitate cu driverul |
| Comandă negativă / restituire | validarea cere client selectat înainte de finalizare |
| Cash in / cash out fără client | utilizatorul este obligat să selecteze clientul înainte de operațiune |
| Sesiune închisă cu pickinguri rămase | există acțiunea **Check Picking** pentru încercare de validare a livrărilor |

## 8. Scenarii de test pentru consultant

| ID | Scenariu | Rezultat așteptat |
|---|---|---|
| AMEF-01 | Bon fiscal cu numerar | se descarcă fișierul ECR și bonul este preluat de driver |
| AMEF-02 | Bon fiscal cu card | totalul folosește `cod_ecr` al metodei card |
| AMEF-03 | Produs cu nume lung și diacritice | ieșirea este ASCII și respectă limita modelului ECR |
| AMEF-04 | Cash collection | se creează linie de numerar și fișier `cash_move.<ext>` |
| AMEF-05 | Payment disposal cu duplicat activ | se tipărește documentul și duplicatul |
| AMEF-06 | Deschidere sesiune cu sumă inițială pozitivă | se descarcă `cash_open.<ext>` |
| AMEF-07 | Raport X / raport Z | se descarcă fișierele dedicate din popup/sesiune |
| AMEF-08 | Restituire cu total negativ și fără client | validarea este blocată până la selectarea clientului |
| AMEF-09 | Reimprimare din backoffice | butonul **Print Fiscal Receipt** oferă fișierul comenzii |

## 9. Legături cu alte module

| Modul | Rol |
|---|---|
| `deltatech_pos_base` | configurare bază ECR: tip casă, prefix/extensie fișier, cod ECR pe metodele de plată |
| `point_of_sale` | fluxul de vânzare și sesiuni POS |
| `l10n_ro_anaf_d394_pos` | duce bonurile POS în declarația D394 |

## 10. Verificări pentru consultant

- [ ] Fiecare metodă de plată are `Cod ECR` corect pentru driverul casei.
- [ ] Tipul de ECR configurat în POS corespunde modelului real din magazin.
- [ ] Fișierele descărcate au prefixul și extensia cerute de utilitarul local.
- [ ] Bonul fiscal se tipărește după validarea comenzii, fără pași manuali suplimentari în Odoo.
- [ ] Cash in / cash out funcționează atât contabil în sesiune, cât și pe AMEF dacă opțiunea e activă.
- [ ] Rapoartele X și Z pot fi generate de utilizatorii operaționali.
- [ ] Pentru retururi și dispoziții de plată există partener selectat.
- [ ] D394 POS este documentată separat când clientul cere și raportarea fiscală a bonurilor.

## 11. Limitări și gap-uri cunoscute

| Limitare | Impact |
|---|---|
| Modulul generează fișier pentru driver, nu comunică direct cu AMEF | depinde de stația locală și de utilitarul casei de marcat |
| Odoo nu importă răspunsul fiscal de la AMEF | seria/numărul bonului fiscal nu se întorc automat în comanda POS |
| Nu există import de jurnal electronic / XML de la casa de marcat | reconcilierea fiscală detaliată rămâne în afara acestui modul |
| Reconcilierea raportului Z și fiscalizarea e-commerce nu sunt acoperite aici | necesită extensii suplimentare |
| Comentariul din cod dezactivează trimiterea CIF-ului clientului pe bon | pentru scenariile care cer CIF pe bon trebuie analizat separat |

## 12. Indicații pentru capturi de ecran

- [ ] [SCREENSHOT: Setări POS — secțiunea ECR]
- [ ] [SCREENSHOT: Metodă de plată cu câmpul Cod ECR]
- [ ] [SCREENSHOT: POS cu validarea bonului fiscal]
- [ ] [SCREENSHOT: Popup / buton Cash In-Cash Out]
- [ ] [SCREENSHOT: Popup / sesiune cu Print X și Print Z]
- [ ] [SCREENSHOT: Comandă POS în backoffice cu tabul ECR data și butonul Print Fiscal Receipt]
