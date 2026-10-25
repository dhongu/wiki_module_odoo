# Fișă Modul: Comenzile de achiziție legate de marketplace

**Modul:** `deltatech_marketplace_purchase`
**Utilizator principal:** Consultant Odoo / administrator funcțional (configurare backend), operator achiziții (utilizare curentă)
**Prioritate:** 🟡 Medie (nu are conectori proprii — este folosit punctual de `deltatech_marketplace_odoo`, pentru fluxul B2B Odoo-la-Odoo)

---

## 1. Scop business

Acest modul leagă procesul de achiziție (`purchase.order`) de ecosistemul de marketplace al suitei
Terrabit: permite ca o comandă de achiziție să fie creată dintr-un canal extern (printr-un apel API cu
token de securitate) și păstrează, pentru orice comandă de achiziție legată de un backend, o evidență
separată — `marketplace.purchase.order` — cu referința externă, backend-ul de origine și liniile ei.
Scopul practic este să alinieze aprovizionarea cu vânzările din marketplace: comenzile de achiziție
generate astfel pot fi urmărite distinct de cele introduse manual de un agent de achiziții, iar orice
modificare ulterioară făcută în Odoo pe o astfel de comandă poate fi semnalată mai departe canalului de
origine.

Spre deosebire de `deltatech_marketplace_sale` (hub-ul de comenzi de vânzare, folosit de toți
conectorii concreți din suită — eMAG, Shopify, WooCommerce etc.), acest modul **nu are un conector
propriu care să importe periodic** comenzi de achiziție dintr-un marketplace extern. În acest moment
el este folosit efectiv de un singur consumator: `deltatech_marketplace_odoo`, conectorul care
tratează o altă instanță Odoo ca „marketplace" pentru un flux B2B — acolo, la confirmarea unei comenzi
de achiziție al cărei furnizor este marcat ca backend, se creează automat înregistrarea de binding și
se trimite comanda mai departe.

## 2. Arhitectură tehnică și context

Modulul depinde de `deltatech_marketplace` (framework-ul comun de backend, job-uri și binding-uri) și
de `purchase_stock` (comanda de achiziție cu recepție de stoc). Modelul central este
`marketplace.purchase.order`, un binding peste `purchase.order` (prin `_inherits`), cu liniile lui în
`marketplace.purchase.order.line` (binding peste `purchase.order.line`).

Trei puncte de intrare tehnice, utile de cunoscut înainte de a promite un flux clientului:

- **`create_api(vals, token)`** — metodă apelabilă extern, cu autentificare pe **token de securitate**
  al backend-ului (același `security_token` folosit de toate integrările framework-ului): creează
  comanda de achiziție și, imediat, binding-ul ei. Este calea prin care un sistem extern poate crea o
  comandă de achiziție direct în Odoo.
- **`write()` pe `purchase.order`** — orice scriere pe o comandă de achiziție legată de un backend
  (în afara contextului `from_marketplace`, adică nu una venită chiar din import) declanșează
  `on_write` pe binding-ul ei, care poate trimite mai departe schimbarea către canalul de origine —
  identic ca mecanism cu `deltatech_marketplace_sale`.
- **`on_confirm(vals)`** pe binding — pregătit să notifice canalul (webhook sau job) la confirmarea
  comenzii, dar **acest modul, de unul singur, nu îl apelează niciodată**: nu există niciun
  `button_confirm` sau `_action_confirm` suprascris în `models/purchase_order.py` care să-l cheme.
  Metoda există doar ca hook pentru un conector care alege să-l folosească explicit — tratați-o ca
  neconectată în instalarea de bază, nu ca un comportament activ.

Un al doilea gol de arhitectură, vizibil în `readme/HISTORY.md`: cron-ul de import periodic
(`data/ir_cron_data.xml`, „Marketplace: Get Purchase Orders") apelează
`model.cron_import_purchase_orders()`, o metodă care **a fost eliminată** din `marketplace.backend`
în versiunea 19.0.1.0.3 („Removed the dead `cron_import_purchase_orders` stub"), dar XML-ul cron-ului
nu a fost curățat odată cu codul. Cron-ul este inactiv implicit (`active` = False), deci nu deranjează
nimeni în stare normală — dar dacă cineva îl activează manual (din formular sau din
`ir.cron`), execuția va eșua cu `AttributeError`, pentru că metoda nu mai există.

## 3. Utilizatori și roluri

- **Consultant/administrator funcțional**: configurează pe backend câmpul specific acestui modul
  (**Purchase Order Days**), creează item-ul de backend de tip „Purchase Order" și verifică drepturile
  de acces pe modelele de binding.
- **Operator achiziții**: urmărește comenzile de achiziție legate de un backend, folosește butonul
  **Reimport** dacă suspectează o desincronizare.

Roluri recomandate la testare:
- Administrator funcțional: instalează modulul, configurează backend-ul și item-ul de tip „Purchase
  Order".
- Utilizator operațional: verifică o comandă de achiziție creată prin `create_api` sau prin
  `save_from_marketplace`, confirmă comanda, editează o linie și verifică propagarea.
- Manager/consultant: validează rezultatul (comanda de achiziție, starea binding-ului, liniile legate).

## 4. Date și mapări implicate

Nu există note contabile Dr/Cr generate direct de acest modul — factura de furnizor rezultată din
comanda de achiziție urmează contabilizarea standard Odoo (`purchase`/`account`/`stock`), neatinsă de
acest modul. Ce trebuie pregătit înainte de a testa fluxul:

- **Backend de marketplace** (`marketplace.backend`, din `deltatech_marketplace`) — pe care acest
  modul adaugă un singur câmp vizibil în formular: **Purchase Order Days** (implicit 2), în tab-ul
  **Technical** (Tehnic), grupul **Limits** (Limite) — orizontul, în zile, folosit pentru
  fereastra de import/urmărire a comenzilor de achiziție.
- **Item de backend** (`marketplace.backend.item`) de tip **Purchase Order** — fără el, `prepare_values`
  nu are ce `backend_item_id` să atașeze automat unui binding creat fără această valoare explicită.
- **Token de securitate** (`security_token`) al backend-ului — necesar pentru orice apel la
  `create_api`; fără un token valid, apelul întoarce `{"error": "Invalid token"}` în loc să creeze
  comanda.
- **Furnizor** (`res.partner`) și produs cumpărabil, pentru comanda de test.
- Date minime pentru demo: un backend de test cu token de securitate, un item de tip „Purchase Order",
  un furnizor, un produs, o comandă de test creată prin `create_api` sau `save_from_marketplace`.

## 5. Configurare inițială

1. Instalați modulul `deltatech_marketplace_purchase` (de regulă ca dependință a unui conector concret
   care are nevoie de fluxul de achiziții, de exemplu `deltatech_marketplace_odoo`).
2. Pe backend-ul de marketplace, completați **Purchase Order Days** dacă valoarea implicită (2 zile) nu
   corespunde nevoii clientului.
3. Creați cel puțin un item de backend cu **Item Type = Purchase Order** (tab **Objects**) — fără el,
   binding-urile create fără `backend_item_id` explicit nu se leagă corect.
4. Confirmați că backend-ul are un **token de securitate** generat, dacă urmează să fie folosit apelul
   `create_api`.
5. Pregătiți un furnizor și un produs cumpărabil pentru comanda de test.
6. **Nu activați** cron-ul „Marketplace: Get Purchase Orders" (Marketplace → Configuration → Crons) —
   apelează o metodă eliminată din cod și va eșua (vezi secțiunea 2 și 9).

## 6. Flux de utilizare

### Pasul 1 — Câmpul specific de achiziții pe backend

Deschideți **Marketplace → Backends**, formularul unui backend deja creat, tab-ul **Technical**
(Tehnic). Acest modul adaugă, în grupul **Limits** (Limite), câmpul **Purchase Order Days**
(implicit 2) — alături de celelalte limite generice ale framework-ului (`items_per_page`,
`only_missing`).

![Backend de marketplace — tab Technical, grupul Limits cu Purchase Order Days](screenshots/01_backend_purchase_order_days.png)

### Pasul 2 — Item de backend de tip Purchase Order

Tot pe formularul backend-ului, tab-ul **Objects**, adăugați (sau verificați) un item cu **Item Type =
Purchase Order** — icoana lui este un coș de cumpărături (`fa-shopping-cart`). Fără acest item,
comenzile de achiziție create prin `create_api`/`save_from_marketplace` fără `backend_item_id` explicit
nu găsesc automat itemul corect.

![Tab Objects — item de backend cu Item Type = Purchase Order](screenshots/02_backend_purchase_order_item.png)

### Pasul 3 — Comanda de achiziție legată de un backend

O comandă de achiziție creată prin `create_api` (sau importată prin `save_from_marketplace`) apare ca o
comandă Odoo obișnuită, în **Achiziții → Comenzi**, la fel ca oricare alta — acest modul nu adaugă
câmpuri vizibile pe formularul comenzii de achiziție în sine (spre deosebire de comanda de vânzare, care
capătă `marketplace_ref` și butonul **Refresh**). Legătura cu backend-ul se vede doar din registrul de
binding-uri (pasul următor).

![Comanda de achiziție creată prin marketplace, vizibilă în lista standard Achiziții → Comenzi](screenshots/03_purchase_order_list.png)

### Pasul 4 — Binding-ul comenzii (Marketplace → Bindings → Purchase Orders)

Meniul **Marketplace → Bindings → Purchase Orders** (submeniu al „Bindings", comun tuturor tipurilor de
binding-uri din framework) deschide lista binding-urilor `marketplace.purchase.order`: sursa externă
(`external_id`, `external_code`), backend-ul de origine și, pe formular, tab-ul **Lines** cu liniile
comenzii legate de binding-ul lor extern. Butonul **Reimport** din antet reia importul acelei comenzi
(dacă backend-ul respectiv implementă `<provider>_import_by_id`).

![Lista binding-urilor de comenzi de achiziție — Marketplace → Bindings → Purchase Orders](screenshots/04_marketplace_purchase_order_binding_list.png)

![Formularul binding-ului marketplace.purchase.order — tab Lines și butonul Reimport](screenshots/05_marketplace_purchase_order_binding_form.png)

### Note de monografie și raportare

Nu se aplică — acest modul nu generează note contabile proprii. Comanda de achiziție și factura de
furnizor rezultată urmează contabilizarea standard Odoo (`purchase`/`account`/`stock`), declanșată
normal la confirmare/facturare/recepție, neatinsă de acest modul.

## 7. Legături cu alte module / declarații

| Modul / proces | Rol în flux | Tip legătură |
|---|---|---|
| `deltatech_marketplace` | framework comun: backend, binding-uri, job-uri, `marketplace.binding` | dependență (manifest) |
| `purchase_stock` | comanda de achiziție cu recepție de stoc | dependență (manifest) |
| `deltatech_marketplace_odoo` | singurul consumator curent: la `button_confirm` pe o comandă al cărei furnizor e marcat ca backend, creează binding-ul (`odoo_create`) și trimite comanda mai departe către instanța Odoo tratată ca marketplace | dependent de acest modul |
| `account` | factura de furnizor generată la facturarea comenzii de achiziție | flux standard Odoo |
| `stock` | recepțiile generate din comanda de achiziție | flux standard Odoo |

Ce este automat: crearea binding-ului la apelul `create_api`/`save_from_marketplace`, propagarea unei
scrieri ulterioare pe comandă către binding (`write` → `on_write`), atribuirea automată a item-ului de
backend corect pe baza `item_type` când nu e dat explicit.

Ce rămâne manual sau nu este încă implementat: importul periodic automat de comenzi de achiziție dintr-
un marketplace extern (cron-ul dedicat este dezactivat și, oricum, nefuncțional — vezi secțiunea 2 și
9), notificarea canalului la confirmarea comenzii (`on_confirm` există pe binding, dar nu e apelată de
niciun cod din acest modul).

## 8. Verificări pentru consultant

- [ ] Modulul se instalează fără erori pe baza demo.
- [ ] Backend-ul are un item de tip **Purchase Order** creat (tab Objects) înainte de primul test de
      creare/import de comenzi.
- [ ] **Purchase Order Days** are valoarea așteptată de client (implicit 2 zile) dacă procesul lui
      depinde de acest orizont.
- [ ] Un apel `create_api` cu token valid creează atât comanda de achiziție, cât și binding-ul ei
      (`marketplace.purchase.order`) în același pas.
- [ ] Un apel `create_api` cu token invalid întoarce eroarea `{"error": "Invalid token"}`, nu creează
      nimic.
- [ ] O scriere pe comanda de achiziție (în afara importului) declanșează `on_write` pe binding — de
      verificat doar dacă backend-ul respectiv are `active_on_write` activ pe item.
- [ ] Cron-ul **„Marketplace: Get Purchase Orders"** (Marketplace → Configuration → Crons) rămâne
      **dezactivat** — nu promiteți clientului un import periodic automat de comenzi de achiziție pe
      baza lui: metoda pe care o apelă a fost eliminată din cod (vezi secțiunea 2).
- [ ] Nu promiteți clientului că o comandă de achiziție confirmată notifică automat marketplace-ul —
      `on_confirm` există ca metodă pe binding, dar nu este apelată din acest modul; verificați dacă
      conectorul concret instalat (dacă există) o folosește explicit.
- [ ] Dacă instalarea folosește `deltatech_marketplace_odoo`, verificați că furnizorul comenzii
      corespunde exact `odoo_supplier_id` de pe un item de backend activ — altfel confirmarea comenzii
      nu declanșează crearea binding-ului.

## 9. Mesaje de eroare frecvente

| Mesaj / simptom | Cauză probabilă | Remediere |
|---|---|---|
| `{"error": "Invalid token"}` la apelul `create_api` | Token-ul trimis nu corespunde niciunui `security_token` de backend | Verificați/regenerați token-ul pe backend-ul corect |
| `AttributeError` la rularea manuală a cron-ului „Marketplace: Get Purchase Orders" | Cron-ul apelează `cron_import_purchase_orders`, metodă eliminată din `marketplace.backend` în 19.0.1.0.3 | Nu activați/rulați acest cron; semnalați echipei de dezvoltare pentru curățare sau reimplementare |
| „... missing from Marketplace Order" la importul unei linii | Linia de comandă a fost trimisă înainte de comanda-părinte, sau comanda a fost ștearsă | Verificați ordinea importului; reimportați comanda din binding-ul ei |
| O comandă de achiziție confirmată nu ajunge la marketplace deși clientul se aștepta la asta | `on_confirm` nu este apelată din acest modul — comportament normal în instalarea de bază, nu o eroare | Clarificați cu clientul că notificarea la confirmare nu e implementată aici; verificați dacă un conector specific o adaugă |
| Binding creat fără `backend_item_id` corect | Nu există niciun item de backend cu `item_type = "purchase_order"` pe acel backend | Creați item-ul de tip Purchase Order pe backend înainte de import |

## 10. Capturi de ecran

Nu există încă niciun fișier `.png` în `readme/screenshots/` și niciun `tests/test_screenshots.py`
pentru acest modul — capturile de mai jos sunt **planificate**, nu generate. Recomand rularea
skill-ului `fisa-screenshots` pentru a le produce, cu numele stabilite mai jos, în aceeași ordine ca
pașii din secțiunea 6:

1. `01_backend_purchase_order_days.png` — backend de marketplace, tab Technical, grupul Limits, cu
   Purchase Order Days.
2. `02_backend_purchase_order_item.png` — tab Objects, item de backend cu Item Type = Purchase Order.
3. `03_purchase_order_list.png` — lista standard Achiziții → Comenzi, cu o comandă provenită din
   marketplace.
4. `04_marketplace_purchase_order_binding_list.png` — lista Marketplace → Bindings → Purchase Orders.
5. `05_marketplace_purchase_order_binding_form.png` — formularul binding-ului, tab Lines, buton
   Reimport.

## 11. Observații pentru manual

În manualul final, subliniați clar că acest modul este un **modul de legătură tehnică**, nu un
conector complet: nu importă singur comenzi de achiziție dintr-un marketplace extern (nu are propriul
`<provider>_import`), iar cron-ul dedicat acestui scop este dezactivat și, în plus, nefuncțional din
19.0.1.0.3 încoace (apelează o metodă ștearsă din cod). Singurul consumator curent al acestui modul
este `deltatech_marketplace_odoo`, pentru un flux B2B Odoo-la-Odoo declanșat la confirmarea comenzii.
Nu promiteți clientului o sincronizare bidirecțională completă (import periodic + notificare la
confirmare) până când aceste două goluri nu sunt adresate în cod — semnalați-le explicit echipei de
dezvoltare dacă un proiect concret are nevoie de ele.
