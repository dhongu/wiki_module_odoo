# Fișă Modul: Etape de vânzare pe comenzile din marketplace

**Modul:** `deltatech_marketplace_sale_stage`
**Utilizator principal:** Operator marketplace, Responsabil vânzări online
**Prioritate:** 🟡 Medie (util pentru companiile cu volum mare de comenzi din canale externe)

---

## 1. Scop business

Modulul leagă etapele de vânzare interne (modulul `deltatech_sale_stage`, câmpul „Fază" de pe
comanda de vânzare) de stadiile de comandă definite pe canalele de marketplace conectate (eMAG,
Shopify, PTC etc., prin suita `deltatech_marketplace`). Practic, permite ca fiecare comandă
importată dintr-un marketplace să primească automat o „Fază" Odoo corespunzătoare stadiului ei din
canalul extern, astfel încât echipa de vânzări/operare vede într-un singur loc — lista de comenzi
Odoo — în ce etapă se află fiecare comandă, indiferent dacă a fost creată manual sau a venit dintr-un
canal de marketplace. Este util companiilor care vând simultan pe mai multe canale și vor o
urmărire unitară a fluxului de procesare (preluare → confirmare → expediere → livrare → facturare).

## 2. Bază legală și context

Nu există temei legal specific; este un modul pur operațional/tehnic de integrare, fără implicații
contabile sau fiscale directe. Contextul este operațional: sincronizarea stărilor comenzii între
un marketplace extern și fluxul intern de procesare a comenzilor din Odoo.

## 3. Utilizatori și roluri

Operator marketplace, Responsabil vânzări/operare comenzi.

Roluri recomandate pentru testare:
- Administrator funcțional (grup `deltatech_marketplace.group_marketplace_manager`): configurează
  backend-ul de marketplace și gestionează corespondența etapelor.
- Utilizator operațional (`base.group_user`): vede și poate consulta faza comenzii pe formularul
  comenzii de marketplace, dar nu poate crea/modifica corespondențe de etape (acces doar-citire).

## 4. Conturi și date implicate

Nu sunt implicate conturi contabile — modulul nu generează note contabile. Datele implicate sunt
strict operaționale:
- un backend de marketplace configurat și funcțional (`marketplace.backend`);
- etapele de vânzare Odoo definite în `deltatech_sale_stage` (model `sale.order.phase`: nume,
  secvență, și marcajele `confirmed`/`shipped`/`delivered`/`invoiced`/`paid`/`canceled` etc.);
- cel puțin o comandă importată dintr-un marketplace, cu un stadiu extern asociat.

Date minime pentru demo:
- un backend de test (`marketplace.backend`) cu locație de stoc asociată;
- câteva etape Odoo (`sale.order.phase`) create în prealabil de `deltatech_sale_stage`;
- o comandă de marketplace importată, cu partener și cel puțin o linie de produs.

## 5. Configurare inițială

1. Instalați modulul `deltatech_marketplace_sale_stage` (instalează automat dependențele
   `deltatech_marketplace_sale` și `deltatech_sale_stage`, dacă nu sunt deja instalate).
2. Verificați că backend-ul de marketplace este configurat (**Marketplace → Backends**) și
   funcțional (conexiune activă, cron-uri de import active).
3. Verificați/creați etapele de vânzare Odoo relevante (`sale.order.phase`) — de regulă acestea
   sunt deja definite de `deltatech_sale_stage` pe baza fluxului intern de procesare.
4. Rulați o sincronizare/import de comenzi din marketplace, ca să existe date de test pentru
   corespondența de etape.
5. Verificați că utilizatorul de test are grupul `deltatech_marketplace.group_marketplace_manager`
   dacă trebuie să administreze corespondența de etape, respectiv doar `base.group_user` dacă
   trebuie doar să vizualizeze faza pe comandă.

## 6. Flux de utilizare

### Pasul 1 — Activarea tipului de obiect „Sale Stage" pe backend

Deschideți **Marketplace → Backends**, selectați backend-ul de test și mergeți la tabul
**Objects**. Aici apare, printre tipurile de obiecte sincronizabile, cardul de tip **Sale Stage**
(icon etichetă, adăugat de acest modul).

![Tabul Objects al backend-ului, cu tipul Sale Stage disponibil](screenshots/01_backend_objects_sale_stage.png)

Din meniul cardului (⋮) sunt disponibile acțiunile standard de sincronizare a tipului de obiect:
**Import** (aduce doar stadiile noi/lipsă din canalul extern) și **Import All** (reimportă toate
stadiile), plus **Edit** (deschide direct lista corespondențelor de etape, vezi Pasul 2).

> Notă tehnică: tipul de obiect este identificat intern ca `sale_stage`; modelul de corespondență
> (binding) este `marketplace.sale.phase`, iar modelul Odoo țintă este `sale.order.phase`
> (cel din `deltatech_sale_stage`).

### Pasul 2 — Corespondența etape marketplace ↔ etape Odoo

Din meniul cardului **Sale Stage** alegeți **Edit** (sau **View Logs** pentru a vedea istoricul
sincronizărilor). Se deschide lista corespondențelor („bindings") dintre stadiile din canalul
extern și etapele Odoo:

![Lista corespondențelor etapă marketplace ↔ etapă Odoo](screenshots/02_lista_binding_etape.png)

Fiecare rând conține: denumirea etapei așa cum vine din marketplace (**binder_name**),
identificatorul extern al stadiului (**external_id**) și etapa Odoo asociată (**odoo_id**,
câmpul „Fază" din `sale.order.phase`).

Deschideți o corespondență pentru a o revizui sau ajusta manual:

![Formularul unei corespondențe de etapă, cu etapa Odoo și opțiunea „Skip Order"](screenshots/03_formular_binding_etapa.png)

Pe formular puteți:
- corecta etapa Odoo (`odoo_id`) la care se mapează stadiul extern, dacă importul automat a
  asociat-o greșit sau nu a găsit o etapă existentă cu același nume;
- bifa **Skip Order** pentru stadiile externe care nu trebuie să influențeze fluxul de procesare
  Odoo (de exemplu, stări intermediare, tehnice, ale marketplace-ului, fără corespondent relevant
  în fluxul intern).

> La import, dacă nu există încă o corespondență pentru stadiul extern respectiv, modulul caută
> automat o etapă Odoo cu **exact același nume**; dacă nu găsește, cere ca numele stadiului să
> fie completat (altfel importul acelei corespondențe eșuează cu eroare).

### Pasul 3 — Vizualizarea fazei pe comanda de marketplace

Deschideți o comandă importată din marketplace (**Marketplace → Bindings → (tipul de comandă)**
sau din lista de comenzi Odoo obișnuită) și priviți câmpul **Fază**, adăugat de acest modul chiar
lângă partener, pe formularul comenzii de marketplace:

![Formularul comenzii de marketplace, cu câmpul Fază lângă partener](screenshots/04_comanda_marketplace_faza.png)

Faza se actualizează pe baza corespondenței definite la Pasul 2, pe măsură ce sincronizarea aduce
schimbări de stadiu din canalul extern; poate fi de asemenea văzută/urmărită și pe formularul
standard al comenzii de vânzare Odoo (câmpul „Fază" adus de `deltatech_sale_stage`).

### Note de monografie și raportare

Modulul nu generează note contabile — nu produce înregistrări Dr/Cr și nu afectează planul de
conturi. Impactul este exclusiv operațional: câmpul `phase_id` de pe comanda de vânzare reflectă
etapa curentă de procesare, utilă pentru rapoarte operaționale de tip „comenzi pe etape" sau pentru
declanșarea automată a acțiunilor asociate etapei (dacă etapa are o acțiune server configurată în
`deltatech_sale_stage`).

## 7. Legături cu alte module / declarații

| Modul / proces | Rol în flux | Tip legătură |
|---|---|---|
| `deltatech_marketplace_sale` | comanda de marketplace (`marketplace.sale.order`) pe care se afișează câmpul Fază | dependență (manifest) |
| `deltatech_sale_stage` | definește etapele Odoo (`sale.order.phase`) și câmpul `phase_id` pe comanda de vânzare | dependență (manifest) |
| `deltatech_marketplace` | infrastructura de backend, tipuri de obiecte sincronizabile și bindings | dependență indirectă (prin `deltatech_marketplace_sale`) |

Ce este automat: importul stadiilor externe ca etape Odoo (cu potrivire după nume), asocierea
etapei pe comanda de marketplace la sincronizare.
Ce rămâne manual: corectarea corespondențelor greșite sau ambigue (etape cu nume diferit între
canal și Odoo), bifarea `Skip Order` pentru stadiile fără relevanță operațională, configurarea
etapelor Odoo în sine (acest modul nu le creează, doar le leagă de stadiile externe).

## 8. Verificări pentru consultant

- [ ] Modulul se instalează fără erori peste `deltatech_marketplace_sale` și `deltatech_sale_stage`.
- [ ] Pe backend, tabul **Objects** afișează cardul **Sale Stage** cu opțiunile de import.
- [ ] Rularea **Import** pe tipul Sale Stage creează corespondențe (`marketplace.sale.phase`) fără erori.
- [ ] Corespondențele importate au etapa Odoo (`odoo_id`) corect asociată sau, dacă nu s-a găsit o
      potrivire după nume, eroarea afișată este clară („Sale stage name is required").
- [ ] Câmpul **Fază** apare pe formularul comenzii de marketplace, lângă partener.
- [ ] Bifarea **Skip Order** pe o corespondență nu produce erori și corespondența rămâne vizibilă în listă.
- [ ] Utilizatorul cu grup `base.group_user` poate vedea corespondențele dar nu poate crea/edita/șterge (acces doar-citire).

## 9. Mesaje de eroare frecvente

| Mesaj / simptom | Cauză probabilă | Remediere |
|-----------------|-----------------|-----------|
| „Sale stage name is required" | Stadiul importat din marketplace nu are nume și nu există deja o corespondență/etapă Odoo cu care să fie asociat automat | Verificați configurarea stadiilor pe canalul extern sau creați manual corespondența, alegând etapa Odoo dorită |
| Corespondența se creează, dar `odoo_id` rămâne goală/greșită | Nu există o etapă Odoo (`sale.order.phase`) cu exact același nume ca stadiul extern | Creați/redenumiți etapa Odoo corespunzătoare, apoi rulați din nou importul, sau completați manual `odoo_id` pe corespondență |
| Câmpul Fază nu se actualizează pe comanda de marketplace | Sincronizarea pentru tipul „Sale Stage" nu a fost rulată sau backend-ul nu are cron-ul de import activ | Rulați manual **Import**/**Import All** pe cardul Sale Stage sau verificați job-urile programate ale backend-ului |
| Utilizatorul obișnuit nu poate modifica o corespondență | Grupul `base.group_user` are acces doar de citire (regulă din `ir.model.access.csv`) | Modificările se fac de un utilizator din grupul `deltatech_marketplace.group_marketplace_manager` |

## 10. Capturi de ecran

Capturile nu există încă în `readme/screenshots/`. Lista planificată, în ordinea pașilor din
secțiunea 6, este:

1. `01_backend_objects_sale_stage.png` — tabul Objects al backend-ului, cu tipul Sale Stage disponibil.
2. `02_lista_binding_etape.png` — lista corespondențelor etapă marketplace ↔ etapă Odoo.
3. `03_formular_binding_etapa.png` — formularul unei corespondențe, cu etapa Odoo și opțiunea „Skip Order".
4. `04_comanda_marketplace_faza.png` — formularul comenzii de marketplace, cu câmpul Fază lângă partener.

Se recomandă rularea skill-ului `fisa-screenshots` pentru a genera aceste capturi (de exemplu prin
metoda A — test Playwright reproductibil — folosind un backend de test și etape Odoo predefinite),
după care fișa să fie re-verificată pentru a lega fiecare captură de pasul corespunzător.

## 11. Observații pentru manual

În manualul final, subliniați că acest modul nu introduce funcționalitate nouă de business, ci
doar leagă două module existente (`deltatech_marketplace_sale` și `deltatech_sale_stage`): scopul
practic este ca echipa de operare comenzi să vadă etapa de procesare la fel, indiferent dacă
comanda vine dintr-un marketplace sau a fost creată manual în Odoo. Menționați explicit că
potrivirea automată a etapelor se face după nume identic, iar corectarea corespondențelor greșite
este o operație de configurare, nu de utilizare zilnică.
