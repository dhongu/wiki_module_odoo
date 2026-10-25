# Fișă Modul: Maparea curierilor de marketplace și punctul de ridicare (locker)

**Modul:** `deltatech_marketplace_delivery`
**Utilizator principal:** Consultant/administrator marketplace, Operator logistică e-commerce
**Prioritate:** 🟡 Medie (necesar la orice conector marketplace cu livrare prin curier)

---

## 1. Scop business

Modulul `deltatech_marketplace_delivery` face legătura dintre metoda de livrare aleasă de
cumpărător pe un marketplace (Shopify, WooCommerce, eMAG, Magento, PrestaShop, OpenCart,
Trendyol etc.) și curierul Odoo (`delivery.carrier`) care va executa efectiv expedierea.
Fără această mapare, comenzile importate ar ajunge fără curier corect atribuit, iar punctul
de ridicare (locker) ales de cumpărător la finalizarea comenzii s-ar pierde. Modulul rezolvă
ambele probleme: creează automat legătura curier-marketplace ↔ curier Odoo și păstrează codul
locker-ului pe comanda de marketplace, indiferent dacă suita de curierat Terrabit
(`deltatech_delivery`) este instalată sau nu.

## 2. Bază legală și context

Nu este vorba de un flux cu bază legală fiscală, ci de un context pur operațional/logistic:
sincronizarea metodei de livrare și a punctului de ridicare între platforma de marketplace și
Odoo, astfel încât comanda să poată fi onorată corect (curier potrivit, AWB cu locker-ul corect
dacă suita de curierat e instalată).

## 3. Utilizatori și roluri

Consultant marketplace, Operator logistică/expediții.

Roluri recomandate pentru testare:
- Administrator funcțional: instalează modulul, configurează backend-ul de marketplace și
  verifică meniurile.
- Utilizator operațional: rulează importul comenzilor și urmărește maparea curierilor.
- Consultant/manager: validează corectitudinea mapării și corectează eventualele mapări greșite.

## 4. Conturi și date implicate

Modulul nu generează note contabile — este un modul de integrare logistică, nu de contabilitate.

Date minime pentru demo:
- un backend de marketplace configurat (`marketplace.backend`), cu cel puțin o locație de stoc
  atașată;
- cel puțin un curier Odoo (`delivery.carrier`) existent în bază (poate fi și curierul implicit
  "Free delivery");
- un element de backend (`marketplace.backend.item`) de tip **Delivery Carrier** — apare automat
  la instalare, prin extinderea listei de tipuri de element din modulul de bază;
- (opțional, pentru scenariul de locker) un modul conector instalat care importă comenzi cu punct
  de ridicare (ex. eMAG) și, dacă vreți să verificați și trecerea pe AWB, suita
  `deltatech_delivery` + `deltatech_delivery_locker`.

## 5. Configurare inițială

1. Instalați modulul `deltatech_marketplace_delivery` pe baza demo (necesită deja
   `deltatech_marketplace_sale` și `delivery`).
2. Verificați că backend-ul de marketplace are un element de tip **Delivery Carrier** în tab-ul
   Items (apare automat, nu necesită configurare suplimentară).
3. Pregătiți în Odoo cel puțin un curier (`delivery.carrier`) cu un nume identic cu cel trimis de
   marketplace (ex. „Fan Courier", „Cargus"), pentru a testa maparea automată corectă.
4. Verificați că utilizatorul de test are grupul de acces la modulul marketplace
   (`group_marketplace_manager`), pentru a vedea meniul **Marketplace**.

## 6. Flux de utilizare

### Pasul 1 — Elementul „Delivery Carrier" pe backend

Accesați **Marketplace → Backends**, deschideți backend-ul conectorului (ex. Shopify, eMAG) și
mergeți la tab-ul cu elementele sincronizate (Items). Modulul adaugă automat un card de tip
**Delivery Carrier**, alături de celelalte tipuri (Produse, Clienți, Comenzi etc.).

![Cardul „Delivery Carrier" pe backend-ul de marketplace](screenshots/01_backend_item_delivery_carrier.png)

### Pasul 2 — Importul/maparea curierilor

La primul import de comenzi (sau la apăsarea acțiunii de import pe cardul Delivery Carrier, dacă
conectorul o expune), pentru fiecare metodă de livrare distinctă trimisă de marketplace se
creează o mapare `marketplace.delivery.carrier`. Deschideți lista de mapări (din cardul de mai
sus, prin numărul de elemente, sau direct din acțiunea **Delivery Carrier**).

> Regula de potrivire: modulul caută în Odoo un `delivery.carrier` cu **numele identic** cu cel
> trimis de marketplace. Dacă găsește, leagă maparea de acel curier; dacă nu găsește, folosește
> curierul implicit `delivery.free_delivery_carrier`.

![Lista mapărilor curier marketplace ↔ curier Odoo](screenshots/02_lista_mapari_curieri.png)

### Pasul 3 — Verificarea/corectarea unei mapări

Deschideți o mapare din listă. Formularul arată numele curierului așa cum a fost trimis de
marketplace (`binder_name`), curierul Odoo asociat (`odoo_id`) și identificatorul extern
(`external_id`/`external_code`). Dacă maparea a căzut pe curierul implicit din cauza unui nume
care nu se potrivește exact, corectați aici curierul Odoo asociat.

![Formularul unei mapări de curier, cu curierul Odoo asociat](screenshots/03_formular_mapare_curier.png)

Butoanele **Reimport** și **Delete** din antet permit resincronizarea mapării din marketplace,
respectiv ștergerea ei (fără a șterge curierul Odoo).

### Pasul 4 — Alerta pentru un curier nerecunoscut

Când numele curierului trimis de marketplace nu se potrivește exact cu niciun curier Odoo,
comanda este pusă pe curierul implicit, iar modulul **programează automat o activitate** pe
backend-ul de marketplace, ca să nu se repete greșeala neobservată la fiecare comandă ulterioară
cu același identificator.

> **Găsește pe ecran** — deschideți fișa backend-ului de marketplace și consultați tab-ul
> Activități: activitatea are ca titlu „Curier necunoscut: <nume>" și în notă indică backend-ul,
> numele primit de la marketplace și curierul implicit pe care a fost pusă comanda.
>
> **Verifică** — confirmați că numele semnalat corespunde unui curier real (nu unei valori
> generice precum „courier"/„pickup" trimisă de unele platforme) și că nu există deja un
> `delivery.carrier` cu acel nume scris puțin diferit (spații, diacritice, majuscule).
>
> **Treci mai departe** — dacă e un curier real, creați sau redenumiți curierul Odoo să
> corespundă exact, apoi corectați maparea (Pasul 3) sau reimportați-o; dacă e o valoare
> generică fără corespondent, marcați activitatea ca rezolvată — curierul implicit rămâne corect.

![Activitatea „Curier necunoscut" programată pe backend](screenshots/04_activitate_curier_necunoscut.png)

### Pasul 5 — Punctul de ridicare (locker) pe comanda de marketplace

Deschideți o comandă importată din **Marketplace → Bindings** (comanda de vânzare de marketplace,
`marketplace.sale.order`). Câmpul **Marketplace Locker**, adăugat de acest modul lângă partener,
arată codul punctului de ridicare exact așa cum a fost trimis de marketplace la momentul
finalizării comenzii de către cumpărător.

![Câmpul „Marketplace Locker" pe comanda de marketplace](screenshots/05_camp_marketplace_locker.png)

### Note de monografie și raportare

Modulul nu produce note contabile (nu este un modul de facturare/contabilitate). Efectele sale
sunt exclusiv operaționale:
- crearea/actualizarea înregistrării `marketplace.delivery.carrier` (mapare curier marketplace →
  `delivery.carrier`);
- programarea unei activități pe `marketplace.backend` când numele curierului nu se potrivește
  cu niciun curier existent;
- completarea câmpului `marketplace_locker` pe `marketplace.sale.order` și, dacă suita de
  curierat Terrabit este instalată, oglindirea codului pe `sale.order.locker` și trimiterea lui
  ca `lockerId` în payload-ul AWB (`get_order_delivery_details` / `get_picking_delivery_details`).

## 7. Legături cu alte module / declarații

| Modul / proces | Rol în flux | Tip legătură |
|---|---|---|
| `deltatech_marketplace_sale` | comanda de marketplace (`marketplace.sale.order`) pe care se păstrează locker-ul | dependență (manifest) |
| `delivery` | modelul `delivery.carrier` peste care se face maparea | dependență (manifest) |
| conectorii de marketplace (Shopify, WooCommerce, eMAG, Magento, PrestaShop, OpenCart, Trendyol) | trimit numele curierului și, unde e cazul, codul locker-ului | integrare prin import |
| `deltatech_delivery` | citește `marketplace_locker`/`sale.order.locker` la generarea AWB | opțional, nu e dependență |
| `deltatech_delivery_locker` | oglindește codul de locker pe `sale.order.locker` | opțional, nu e dependență |

Ce este automat: crearea mapării curierului la import, alertarea pe curier nerecunoscut,
păstrarea codului de locker pe comanda de marketplace și oglindirea lui pe comanda de vânzare
(dacă suita de curierat e instalată).
Ce rămâne manual: corectarea unei mapări greșite (redenumirea curierului Odoo sau editarea
mapării) și decizia dacă o alertă de „curier necunoscut" e reală sau o valoare generică fără
corespondent.

## 8. Verificări pentru consultant

- [ ] Modulul se instalează fără erori pe baza demo (peste `deltatech_marketplace_sale` și `delivery`).
- [ ] Elementul „Delivery Carrier" apare automat pe tab-ul Items al backend-ului.
- [ ] La import, o comandă cu un curier al cărui nume se potrivește exact cu un `delivery.carrier` existent este mapată corect (nu pe curierul implicit).
- [ ] La import, o comandă cu un nume de curier necunoscut este pusă pe curierul implicit și generează o activitate pe backend.
- [ ] Codul de locker (`marketplace_locker`) apare pe comanda de marketplace după import, chiar dacă `deltatech_delivery_locker` nu este instalat.
- [ ] Dacă `deltatech_delivery_locker` este instalat, codul de locker se oglindește pe `sale.order.locker` și ajunge în payload-ul AWB (`lockerId`).
- [ ] Butoanele **Reimport**/**Delete** din formularul unei mapări funcționează fără eroare.

## 9. Mesaje de eroare frecvente

| Mesaj / simptom | Cauză probabilă | Remediere |
|-----------------|-----------------|-----------|
| Comanda ajunge mereu pe curierul „Free delivery" | Numele curierului trimis de marketplace nu se potrivește exact (spații, diacritice, majuscule) cu niciun `delivery.carrier` | Redenumiți curierul Odoo identic cu numele trimis de marketplace, apoi corectați/reimportați maparea |
| Activitate „Curier necunoscut: …" reapare pentru aceeași metodă de livrare | Maparea a fost corectată pe înregistrare, dar curierul Odoo tot nu are numele exact așteptat | Verificați exact numele din notă (case-sensitive) și potriviți-l cu `delivery.carrier.name` |
| Codul de locker nu apare pe `sale.order` deși există pe comanda de marketplace | `deltatech_delivery_locker` nu este instalat — codul rămâne doar pe `marketplace.sale.order`, ceea ce este comportamentul așteptat, nu o eroare | Instalați `deltatech_delivery_locker` dacă vreți oglindirea pe `sale.order.locker`; altfel folosiți direct câmpul de pe comanda de marketplace |
| Locker-ul nu apare în payload-ul AWB | Curierul folosit nu are `use_locker` bifat sau AWB-ul este emis fără `deltatech_delivery` instalat | Verificați configurarea curierului și instalarea suitei de curierat |
| Nu găsesc meniul de mapări curieri | Acțiunea `action_delivery_carrier` nu are meniu dedicat — se accesează din cardul „Delivery Carrier" de pe backend | Deschideți backend-ul de marketplace → tab Items → cardul Delivery Carrier |

## 10. Capturi de ecran

Capturile de mai jos nu există încă în `readme/screenshots/` — rulați skill-ul `fisa-screenshots`
pentru a le genera automat (mixinul `ScreenshotCase`), în limba română. Lista planificată,
în ordinea pașilor din secțiunea 6:

1. `01_backend_item_delivery_carrier.png` — cardul „Delivery Carrier" pe tab-ul Items al backend-ului de marketplace.
2. `02_lista_mapari_curieri.png` — lista mapărilor curier marketplace ↔ curier Odoo.
3. `03_formular_mapare_curier.png` — formularul unei mapări, cu curierul Odoo asociat.
4. `04_activitate_curier_necunoscut.png` — activitatea „Curier necunoscut" programată pe backend.
5. `05_camp_marketplace_locker.png` — câmpul „Marketplace Locker" pe comanda de marketplace.

Regenerare (după ce testul de capturi este creat):

```bash
./odoo/odoo-bin -c odoo.conf -d <db> -i deltatech_marketplace_delivery,l10n_ro_doc_screenshots \
    --test-tags=fise_screenshots --stop-after-init
```

## 11. Observații pentru manual

În manualul final, prezentați modulul ca pe un pas de configurare tehnică din spatele fiecărui
conector de marketplace, nu ca pe un flux zilnic al operatorului: consultantul îl verifică o
singură dată la punerea în funcțiune a unui backend (maparea curierilor) și revine la el doar
când apare o alertă de curier necunoscut sau când se schimbă metodele de livrare oferite de
marketplace. Subliniați diferența clară față de contabilitate: acest modul nu generează note
contabile, ci doar corectitudinea logistică a expedierii.
