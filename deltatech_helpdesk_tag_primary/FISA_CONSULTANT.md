# Fișă Modul: Helpdesk Tag Primary & Team Filter

**Modul:** `deltatech_helpdesk_tag_primary`  
**Utilizator principal:** Helpdesk manager, agent suport, consultant implementare  
**Prioritate:** Medie  
**Status document:** Beta consultant

---

## 1. Scop business

Modulul structurează clasificarea tichetelor Helpdesk pe două niveluri:

- **tag-uri principale** selectate în câmpul standard `tag_ids`;
- **tag-uri secundare** dependente de tag-urile principale;
- filtrare a tag-urilor după **echipa Helpdesk**.

Rezultatul este o taxonomie mai curată a tichetelor, cu liste de tag-uri mai scurte și mai relevante
pentru fiecare echipă.

---

## 2. Comportament funcțional

Modulul extinde `helpdesk.tag` cu două câmpuri:

| Câmp | Rol |
|---|---|
| `Primary Tag` | marchează tag-ul curent ca sub-tag al altui tag |
| `Helpdesk Team` | limitează tag-ul la o anumită echipă Helpdesk |

Și extinde `helpdesk.ticket` cu:

| Câmp | Rol |
|---|---|
| `Secondary Tags` | tag-uri copil disponibile doar după selectarea unui tag principal |

Reguli aplicate în interfață:

1. în câmpul standard **Tags** apar doar tag-urile fără `Primary Tag`;
2. în plus, acestea sunt filtrate pe echipa tichetului: tag-uri cu `team_id = team_id` sau fără echipă;
3. după alegerea tag-urilor principale, apare câmpul **Secondary Tags**;
4. în `Secondary Tags` pot fi selectate doar tag-uri al căror `Primary Tag` este unul dintre tag-urile principale deja alese.

---

## 3. Configurare inițială

### Pasul 1 — Definire tag-uri principale

Mergeți în **Helpdesk → Configuration → Tags** și creați tag-urile principale.

Pentru un tag principal:

- lăsați câmpul **Primary Tag** gol;
- completați **Helpdesk Team** dacă tag-ul trebuie folosit doar într-o echipă.

Exemple:

| Tag | Primary Tag | Team |
|---|---|---|
| Hardware | — | Support |
| Software | — | Support |
| Billing | — | Backoffice |

### Pasul 2 — Definire tag-uri secundare

Tot în **Helpdesk → Configuration → Tags**, creați tag-urile detaliate și completați:

- **Primary Tag** = tag-ul părinte;
- **Helpdesk Team** = echipa în care tag-ul este valabil, dacă e cazul.

Exemple:

| Tag secundar | Primary Tag | Team |
|---|---|---|
| Printer | Hardware | Support |
| Windows | Software | Support |
| Invoice Copy | Billing | Backoffice |

### Pasul 3 — Reguli de consistență

Modulul nu permite ca un tag să se refere la el însuși în câmpul **Primary Tag**.

---

## 4. Flux de utilizare

### Pasul 1 — Creare tichet

În **Helpdesk → Tickets**, utilizatorul alege echipa tichetului.

Această alegere influențează lista disponibilă în câmpul standard **Tags**:

- se văd doar tag-urile de nivel principal;
- se văd doar cele comune sau cele asociate echipei selectate.

### Pasul 2 — Alegere tag-uri principale

În câmpul **Tags**, agentul selectează una sau mai multe categorii principale.

Exemplu:

- `Hardware`
- `Software`

### Pasul 3 — Alegere tag-uri secundare

După ce există cel puțin un tag principal, apare câmpul **Secondary Tags**.

În acest câmp se pot selecta doar tag-uri copil relevante pentru selecția anterioară.

Exemplu:

- dacă `Tags = Hardware`, atunci `Secondary Tags` poate include `Printer`, `Scanner`, `POS`;
- dacă `Tags = Billing`, atunci `Secondary Tags` poate include doar sub-tag-urile definite sub `Billing`.

### Pasul 4 — Vizualizare în kanban

În vizualizarea kanban a tichetelor, pe lângă tag-urile standard, sunt afișate și
**Secondary Tags**, astfel încât clasificarea detaliată să fie vizibilă direct în board.

---

## 5. Beneficii operaționale

- reduce aglomerarea listei standard de tag-uri;
- evită selectarea unor tag-uri nerelevante pentru altă echipă;
- permite clasificare pe două niveluri fără schimbarea fluxului standard Helpdesk;
- ajută la raportare și filtrare mai clară pe categorii principale și detalii.

---

## 6. Limitări și atenționări

1. Filtrarea este implementată în interfață, nu ca regulă complexă de business pe toate fluxurile externe.
2. `Secondary Tags` nu înlocuiește `tag_ids`; funcționează complementar.
3. Dacă un tag secundar nu are `Primary Tag`, el nu va apărea în lista de `Secondary Tags`.
4. Modulul nu adaugă rapoarte sau automatizări suplimentare; acoperă doar organizarea și selecția tag-urilor.

---

## 7. Scenariu demo recomandat

Configurați două echipe și câteva tag-uri:

| Echipa | Tag principal | Tag secundar |
|---|---|---|
| Support | Hardware | Printer |
| Support | Software | Windows |
| Backoffice | Billing | Invoice Copy |

Demo:

1. creați un tichet pe echipa **Support**;
2. verificați că în `Tags` nu apare `Billing`;
3. selectați `Hardware`;
4. verificați că în `Secondary Tags` apare `Printer`, dar nu `Invoice Copy`.

---

## 8. Indicații pentru capturi de ecran

Capturi utile pentru manual:

1. lista de tag-uri cu coloanele **Primary Tag** și **Helpdesk Team**;
2. formular de tag cu relația părinte-copil;
3. formular de tichet cu filtrarea `Tags` după echipă;
4. câmpul **Secondary Tags** după selectarea tag-urilor principale;
5. card kanban cu tag-uri principale și secundare afișate.
