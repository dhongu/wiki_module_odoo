# Fișă Modul: Asistent AI pentru planificarea avansată (Advanced Planner AI)

**Modul:** `deltatech_advanced_planner_ai`
**Utilizator principal:** Planificator producție, Responsabil achiziții, Vânzător
**Prioritate:** 🟢 Scăzută (completează planificatorul avansat; nu schimbă nicio dată și nu generează documente)

---

## 1. Scop business

Planificatorul avansat calculează dacă o comandă de vânzare poate fi livrată la data promisă, ce
componente lipsesc și ce posturi de lucru sunt supraîncărcate. Modulul `deltatech_advanced_planner_ai`
adaugă un **asistent AI care explică în limbaj obișnuit** rezultatele acestea și **propune opțiuni**:
cauza întârzierii, cel mult trei acțiuni posibile în Odoo (cu efectul lor în zile) și un mesaj-model
către client. În plus, în fiecare dimineață asistentul poate posta într-un canal de discuții un
**rezumat al riscurilor de planificare**. Planificatorul calculează, AI-ul explică, oamenii decid:
niciun răspuns nu modifică date, cereri de ofertă sau ordine de producție.

Consultantul folosește documentul pentru a configura asistentul pe baza demo și pentru a-l prezenta
planificatorilor și vânzătorilor.

## 2. Bază legală și context

Modulul **nu are bază legală fiscală** — nu generează note contabile și nu alimentează declarații.
Este un instrument operațional, peste `deltatech_advanced_planner`.

Context de utilizare: către furnizorul de AI (Claude, OpenAI sau Google, la alegere) pleacă doar date
de planificare — numere de documente, produse, cantități, date, statusuri, nume de furnizori și
termene de livrare, încărcarea posturilor de lucru. **Nu pleacă prețuri, sume, nume sau date de
contact ale clienților.** Aceasta este o informație de transmis clientului la implementare.
Modulul cere **Odoo Enterprise** (framework-ul AI).

## 3. Utilizatori și roluri

- **Advanced Planner / User** — poate apăsa **Explică planificarea** pe comenzile de vânzare și pe
  comenzile planificate; vede lista cererilor AI în citire.
- **Advanced Planner / Manager** — în plus, vede meniul **Cereri AI** și poate șterge cereri din listă.
- **Administrator** — activează asistentul în Setări, alege modelul AI și cheia de API.
- **Membrii canalului „Rezumat planificare”** — planificatorii și cumpărătorii care citesc rezumatul
  zilnic; se adaugă manual în canal.

## 4. Date implicate (nu există conturi contabile)

Modulul **nu folosește conturi contabile**.

Date minime pentru demo:
- modulul `deltatech_advanced_planner` configurat, cu cel puțin o comandă de vânzare confirmată și
  planificată (status **OK**, **Avertisment** sau **Blocat**) — vezi fișa acelui modul;
- un furnizor de AI configurat: model Claude (modulul *Claude (Anthropic) provider for Odoo AI* și o
  cheie Anthropic), OpenAI sau Google (cheia în **Setări → General → AI**);
- utilizatori de test cu grupul **Advanced Planner / User**, respectiv **Manager**.

## 5. Configurare inițială

1. Instalați modulul pe o bază cu Odoo Enterprise și `deltatech_advanced_planner` (depinde de acesta
   și de modulul `ai`).
2. Deschideți **Setări → Inventar → Asistent AI de planificare** și bifați **Asistent AI de
   planificare**.
3. Apăsați **Configurare agent AI (model LLM)** și alegeți modelul agentului *Planning Assistant*.
   Implicit agentul vine cu un model OpenAI; pentru Claude sau Google schimbați modelul pe formularul
   agentului.
4. Stabiliți **Limită zilnică de cereri AI** (implicit 50 pe companie; 0 = fără limită).
5. Pentru rezumatul zilnic bifați **Rezumat zilnic de planificare** și alegeți canalul (gol = canalul
   **Rezumat planificare**, instalat de modul). Adăugați planificatorii și cumpărătorii ca membri ai
   canalului. Programarea zilnică este oprită la instalare și pornește doar din această bifă.
6. Apăsați **Trimite rezumatul acum** ca să verificați imediat configurarea.

## 6. Flux de utilizare

### Pasul 1 — Activarea asistentului și alegerea modelului

În **Setări → Inventar → Asistent AI de planificare** se bifează asistentul, se alege modelul din
agent, se fixează limita zilnică și, opțional, rezumatul zilnic. Setările limită și rezumat apar doar
după ce asistentul este activat.

![Setările asistentului AI de planificare: activare, agent, limită zilnică și rezumat zilnic](screenshots/01_setari_asistent_ai.png)

### Pasul 2 — Explicația unei comenzi de vânzare întârziate sau blocate

Deschideți o comandă de vânzare planificată de Advanced Planner (status **OK**, **Avertisment** sau
**Blocat**) și apăsați **Explică planificarea** din antet. Butonul nu apare pe ofertele nerecalculate
sau fără planificare, nici când asistentul e dezactivat.

![Comandă de vânzare blocată, cu butonul Explică planificarea în antet](screenshots/02_so_buton_explica.png)

Răspunsul se postează ca **notă internă** în chatter, de către agentul *Planning Assistant*, cu trei
secțiuni scurte:

1. **Cauza** — de ce comanda e întârziată sau la risc, cu componenta, furnizorul sau postul de lucru
   și numărul de zile.
2. **Opțiuni** — cel mult trei acțiuni disponibile în Odoo (urgentarea unei cereri de ofertă, alt
   furnizor din listă, livrare parțială, mutarea datei promise, capacitate suplimentară), fiecare cu
   efectul în zile.
3. **Mesaj către client** — o ciornă scurtă, fără numere de documente interne, furnizori sau posturi,
   cu cea mai devreme dată realizabilă.

Dacă comanda e la termen, răspunsul spune asta într-o propoziție și omite opțiunile. Răspunsul este în
limba utilizatorului.

1. **Găsiți pe ecran** — nota din chatter și cele trei secțiuni.
2. **Verificați** — data din notă coincide cu data efectivă calculată de planificator (tabul
   **Planificare avansată**); documentele și furnizorii numiți există pe comandă; opțiunile sunt
   acțiuni pe care le puteți face în Odoo.
3. **Treceți mai departe** — decideți și acționați chiar dumneavoastră: urgentați cererea de ofertă,
   schimbați data promisă, trimiteți clientului mesajul, după ce l-ați citit și ajustat.

![Nota internă a asistentului pe comandă: cauză, opțiuni și mesaj către client](screenshots/03_nota_explicatie.png)

### Pasul 3 — Explicația unei comenzi planificate

Același buton **Explică planificarea** există în antetul unei comenzi planificate (de exemplu o
propunere de reaprovizionare pentru stoc), cu excepția celor în starea **Finalizat** sau **Anulat**.
Nota se postează pe comanda planificată.

![Comandă planificată cu butonul Explică planificarea și nota asistentului](screenshots/04_comanda_planificata_explicatie.png)

### Pasul 4 — Rezumatul zilnic de planificare

Cu rezumatul activat, în fiecare dimineață asistentul postează în canal, pentru fiecare companie cu
asistentul activ, un mesaj cu trei secțiuni (se omit cele fără conținut, cel mult 250 de cuvinte):

- **Ce s-a schimbat** — comenzi noi blocate și abateri;
- **De făcut azi** — cel mult șapte acțiuni prioritizate, cu documentul numit;
- **Riscuri** — comenzi întârziate sau critice și posturi de lucru supraîncărcate în următoarele 6 săptămâni.

Rezumatul se bazează pe comenzile de vânzare cu risc mediu sau ridicat, comenzile planificate blocate
din ziua precedentă, abaterile detectate, comenzile de lansat în fereastra de lansare și sloturile CRP
supraîncărcate. Se poate declanșa oricând din setări cu **Trimite rezumatul acum**.

1. **Găsiți pe ecran** — mesajul agentului în canalul **Rezumat planificare** (Discuții).
2. **Verificați** — documentele numite sunt comenzi reale cu risc în Panoul de control al
   planificatorului; datele coincid cu cele din **Risc de livrare**.
3. **Treceți mai departe** — lansați cererile de ofertă sau ordinele de producție numite, din
   comenzile planificate.

![Rezumatul zilnic postat de asistent în canalul Rezumat planificare](screenshots/05_rezumat_zilnic.png)

### Pasul 5 — Audit și cost

**Producție → Planificare avansată → Cereri AI** (doar Manager) listează fiecare apel către furnizorul
de AI: data, tipul (**Explicație** sau **Rezumat zilnic**), documentul, utilizatorul și starea
(**În așteptare**, **Finalizat**, **Eșuat**), cu mesajul de eroare ca coloană opțională. Filtrele
**Astăzi** și **Eșuate** și gruparea după tip sau zi ajută la controlul costului.

Când limita zilnică e atinsă, butonul **Explică planificarea** afișează mesajul de refuz, iar rezumatul
programat este sărit până a doua zi. Dacă furnizorul nu răspunde, utilizatorul primește o notificare, iar
cererea rămâne în listă cu starea **Eșuat** și motivul.

![Lista Cereri AI cu starea și documentul fiecărei cereri](screenshots/06_cereri_ai.png)

### Curățarea datelor de test (modulul `terrabit_clear_data`)

Opțiunea **Sterge date tranzactionale din module** a modulului `terrabit_clear_data` șterge cererile AI
ale companiei selectate (pe cele fără companie, doar când se șterg și datele fără companie). Contorul
limitei zilnice pornește astfel de la zero. Notele și mesajele deja postate în chatter sau în canal
nu sunt afectate. Operația nu se folosește pe o bază de producție.

### Ce generează modulul (rezultate operaționale)

Modulul **nu generează note contabile** (Dr/Cr). Rezultatele sunt:

- note interne pe comenzile de vânzare și pe comenzile planificate;
- mesajul zilnic în canalul de rezumat;
- înregistrările din **Cereri AI**.

## 7. Legături cu alte module / declarații

| Modul / proces | Rol în flux | Tip legătură |
|---|---|---|
| `deltatech_advanced_planner` | calculează datele, statusurile și încărcarea; asistentul le explică | dependență (manifest) |
| `ai` | framework-ul AI și agentul *Planning Assistant* (**Odoo Enterprise**) | dependență (manifest) |
| Furnizor AI (Claude / OpenAI / Google) | modelul care scrie răspunsurile | configurare în Setări |
| `terrabit_clear_data` | curăță cererile AI pe bazele de test | opțional |

**Ce este automat:** rezumatul zilnic (după activare), înregistrarea fiecărui apel și verificarea
limitei zilnice.

**Ce rămâne manual:** apăsarea butonului **Explică planificarea**, citirea și aprobarea răspunsului,
orice acțiune propusă (urgentarea unei cereri de ofertă, schimbarea datei promise, mesajul către
client), alegerea modelului AI și adăugarea membrilor în canal.

## 8. Verificări pentru consultant

- [ ] Modulul se instalează pe o bază cu Odoo Enterprise și `deltatech_advanced_planner`, fără erori.
- [ ] Setările **Limită zilnică de cereri AI** și **Rezumat zilnic de planificare** apar doar după bifarea asistentului.
- [ ] Pe o comandă planificată, **Explică planificarea** postează o notă internă cu cauză, opțiuni și mesaj către client, în limba utilizatorului.
- [ ] Data din notă coincide cu data efectivă calculată de planificator; nu apar prețuri, sume sau date ale clientului.
- [ ] Butonul lipsește pe o ofertă nerecalculată și pe o comandă planificată finalizată sau anulată.
- [ ] Cererea apare în **Cereri AI** cu starea **Finalizat**; fără răspuns de la furnizor, cu starea **Eșuat** și motivul.
- [ ] La atingerea limitei zilnice, butonul refuză cu mesajul de limită; cu limita 0 nu există restricție.
- [ ] **Trimite rezumatul acum** postează mesajul în canalul ales; bifa **Rezumat zilnic de planificare** pornește programarea.
- [ ] Un utilizator fără grupul Manager nu vede meniul **Cereri AI**.
- [ ] Nicio dată, cerere de ofertă sau ordin de producție nu se modifică după un răspuns al asistentului.
- [ ] Pe o bază de test, **Sterge date tranzactionale din module** șterge cererile AI ale companiei selectate și lasă notele deja postate.

## 9. Mesaje de eroare frecvente

| Mesaj | Cauză | Remediere |
|---|---|---|
| „Asistentul AI de planificare nu este activat pentru …” | Bifa din Setări nu e activă pe compania curentă | Activați **Asistent AI de planificare** în Setări → Inventar |
| „Limita zilnică de … cereri AI a fost atinsă pentru …” | S-au consumat cererile zilei | Încercați mâine sau măriți **Limită zilnică de cereri AI** |
| „Furnizorul AI nu a răspuns: …” | Cheie de API lipsă sau greșită, model indisponibil, rețea | Verificați cheia și modelul din agentul *Planning Assistant*; vedeți mesajul în **Cereri AI** |
| „Furnizorul AI nu a răspuns: răspuns gol” | Furnizorul a răspuns fără text | Reîncercați; schimbați modelul dacă se repetă |
| „Alegeți un canal pentru rezumat în setări.” | Nu există canal de rezumat | Alegeți un canal în **Rezumat zilnic de planificare** |
| „Agentul AI de planificare lipsește. Actualizați modulul.” | Agentul a fost șters | Actualizați modulul ca să-l recreeze |
| Nimeni nu vede rezumatul zilnic | Utilizatorii nu sunt membri ai canalului | Adăugați-i în canalul **Rezumat planificare** |

## 10. Capturi de ecran

Modulul nu are încă `tests/test_screenshots.py`, deci folderul `static/description/` conține doar
iconița și bannerul. Capturile de mai jos sunt **planificate**; trebuie rulat skill-ul
`fisa-screenshots` (mixinul `ScreenshotCase` din `l10n_ro_doc_screenshots`, import defensiv, în
română, pe planul RO) ca să fie generate. Ordinea corespunde pașilor din secțiunea 6:

1. `01_setari_asistent_ai.png` — setările asistentului AI: activare, agent, limită zilnică, rezumat zilnic.
2. `02_so_buton_explica.png` — comandă de vânzare blocată, cu butonul **Explică planificarea**.
3. `03_nota_explicatie.png` — nota internă a asistentului pe comandă (cauză, opțiuni, mesaj către client).
4. `04_comanda_planificata_explicatie.png` — comandă planificată cu butonul și nota asistentului.
5. `05_rezumat_zilnic.png` — rezumatul zilnic în canalul **Rezumat planificare**.
6. `06_cereri_ai.png` — lista **Cereri AI**.

Regenerare, după crearea testului:

```bash
./odoo/odoo-bin -c odoo.conf -d <db> -i deltatech_advanced_planner_ai,l10n_ro_doc_screenshots \
    --test-tags=fise_screenshots --stop-after-init --http-port=8987 --gevent-port=8988
```

## 11. Observații pentru manual

Păstrați mesajul **„planificatorul calculează, AI-ul explică, oamenii decid”**: nimic nu se schimbă
automat, iar fiecare răspuns e o notă pe care utilizatorul o citește. Explicați clar ce date pleacă
spre furnizorul de AI (doar date de planificare, fără prețuri, sume sau date ale clienților), cum se
alege modelul și cum se controlează costul (limita zilnică și lista **Cereri AI**). Menționați
cerința **Odoo Enterprise** și faptul că modulul nu generează note contabile.
