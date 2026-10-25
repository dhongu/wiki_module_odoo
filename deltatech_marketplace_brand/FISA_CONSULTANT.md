# Fișă Modul: Sincronizarea Brandurilor de Produs cu Marketplace-urile

**Modul:** `deltatech_marketplace_brand`
**Utilizator principal:** Administrator marketplace / Operator catalog produse
**Prioritate:** 🟡 Medie (relevantă doar acolo unde marketplace-ul conectat (ex. eMAG) folosește branduri ca atribut de categorisire)

---

## 1. Scop business

Modulul `deltatech_marketplace_brand` extinde framework-ul Marketplace (`deltatech_marketplace`) cu
un tip nou de obiect sincronizabil: **brandul de produs** (`product.brand`, adus de
`deltatech_product_brand`). Rolul lui este să lege brandurile importate dintr-un canal de vânzare
extern (eMAG, MerchantPro, Odoo-to-Odoo etc.) de brandurile din Odoo, astfel încât fiecare produs
importat sau exportat să poarte brandul corect pe fiecare canal — fără ca operatorul de catalog să
mai facă maparea manual, brand cu brand. Este util companiilor care vând mai multe branduri pe mai
multe marketplace-uri și au nevoie de raportare/filtrare unitară pe brand în Odoo.

## 2. Bază legală și context

Nu este un modul de contabilitate sau fiscalitate — nu generează note contabile și nu are bază
legală asociată. Contextul este pur operațional: sincronizarea catalogului de produse (brand ca
atribut) între Odoo și platformele de marketplace conectate prin `deltatech_marketplace`.

## 3. Utilizatori și roluri

Utilizatori tipici: administratorul de marketplace (configurează backend-ul și urmărește
sincronizarea) și operatorul de catalog (verifică maparea brandurilor pe produse).

Roluri recomandate pentru testare:
- Administrator funcțional: instalează modulul, configurează backend-ul de marketplace și rulează
  primul import.
- Utilizator operațional (grup `base.group_user`, care are acces la modelul de binding): verifică
  lista de branduri sincronizate și corectează eventualele mapări greșite.
- Manager/consultant: validează faptul că produsele exportate/importate au brandul corect pe
  fiecare canal.

## 4. Conturi și date implicate

Nu sunt implicate conturi contabile — modulul este strict de catalog. Datele relevante:

- modelul tehnic `marketplace.product.brand` (binding), moștenit din `marketplace.binding` și
  `product.brand` (via `_inherits`);
- pe fiecare linie de produs sincronizat (`marketplace.product.template`), câmpul intern
  `product_brand_id` este completat automat la import, pe baza brandului extern.

Date minime pentru demo:
- un backend de marketplace configurat (ex. o instanță de test eMAG/Shopify) sau date de test
  introduse manual pe modelul de binding;
- module instalate: `deltatech_marketplace`, `deltatech_product_brand`, `deltatech_marketplace_brand`;
- cel puțin un brand definit în Odoo (`product.brand`) și un produs asociat unui backend.

## 5. Configurare inițială

1. Instalați modulul `deltatech_marketplace_brand` (instalează automat și dependențele
   `deltatech_marketplace` și `deltatech_product_brand`).
2. Deschideți backend-ul de marketplace pe care doriți să sincronizați brandurile
   (**Marketplace → Backends**).
3. În tabul **Objects** al backend-ului, verificați că a apărut un obiect de tip **Product Brand**
   (adăugat automat de acest modul în lista de tipuri sincronizabile ale backend-ului).
4. Verificați că utilizatorul de test are grupul `base.group_user` (acces la modelul de binding,
   conform `security/ir.model.access.csv`).
5. Rulați un import de produse sau de branduri pe backend, ca să populați lista de mapări.

## 6. Flux de utilizare

### Pasul 1 — Backend-ul de marketplace, obiectul „Product Brand"

Accesați **Marketplace → Backends** și deschideți un backend configurat. În tabul **Objects**
apare, printre celelalte tipuri sincronizabile (Products, Customers, Categories etc.), tipul
**Product Brand**, cu iconul de etichetă (`fa-tags`) și un contor de elemente sincronizate.

![Backend-ul de marketplace, tabul Objects cu obiectul Product Brand](screenshots/01_backend_objects_brand.png)

### Pasul 2 — Lista brandurilor sincronizate

Apăsați pe contorul de sub **Product Brand** (butonul „Elements"). Se deschide lista brandurilor
sincronizate pentru acel backend (`marketplace.product.brand`), cu codul și numele extern, brandul
Odoo asociat (`odoo_id`) și backend-ul de origine.

![Lista brandurilor sincronizate cu backend-ul](screenshots/02_lista_branduri.png)

### Pasul 3 — Fișa unui brand sincronizat

Deschideți un rând din listă. Formularul arată numele brandului, brandul Odoo la care este legat
(`odoo_id`, editabil dacă maparea automată nu a nimerit brandul corect), codul/ID-ul extern și
backend-ul. Butonul **Reimport** din antet reia importul acelui brand direct de pe marketplace,
utilă când brandul extern și-a schimbat numele sau logo-ul.

![Fișa unui brand sincronizat, cu butonul Reimport](screenshots/03_fisa_brand.png)

### Note de monografie și raportare

Nu se aplică — modulul nu produce înregistrări contabile. Singurul efect „de raportare" este că
produsele sincronizate primesc automat `product_brand_id`, ceea ce permite filtrarea/raportarea
vânzărilor pe brand în Odoo (raportare comercială, nu contabilă).

## 7. Legături cu alte module / declarații

| Modul / proces | Rol în flux | Tip legătură |
|---|---|---|
| `deltatech_marketplace` | framework de bază (backend, binding, joburi de import/export) | dependență (manifest) |
| `deltatech_product_brand` | modelul `product.brand` din Odoo, ținta binding-ului | dependență (manifest) |
| `marketplace.product.template` (binding produs) | primește `product_brand_id` la import, pe baza brandului extern | integrare directă (suprascriere `save_from_marketplace`) |
| conectori marketplace (eMAG, MerchantPro, Odoo-to-Odoo etc.) | furnizează valorile de brand la import, prin metodele `<provider>_import_by_id` | prin convenția framework-ului `deltatech_marketplace` |

Ce este automat: crearea/actualizarea brandului la import, legarea produsului de brandul corect
(dacă brandul există deja în Odoo cu același nume, se leagă automat; altfel se creează unul nou).
Ce rămâne manual: corectarea mapării atunci când brandul extern nu corespunde exact cu un brand deja
existent în Odoo (ex. denumiri diferite pentru același brand) — se editează manual câmpul `odoo_id`
pe fișa binding-ului.

## 8. Verificări pentru consultant

- [ ] Modulul se instalează fără erori pe baza demo (împreună cu `deltatech_marketplace` și
      `deltatech_product_brand`).
- [ ] După instalare, tipul **Product Brand** apare în tabul Objects al backend-ului.
- [ ] Un import de produse/branduri populează lista `marketplace.product.brand` cu date corecte
      (nume, cod extern, backend).
- [ ] Brandul Odoo (`odoo_id`) este cel corect — verificați mai ales cazul în care denumirea externă
      diferă ușor de cea din Odoo (maparea automată se face după `name` exact).
- [ ] Produsele importate ulterior au `product_brand_id` completat corect pe baza brandului extern.
- [ ] Butonul **Reimport** funcționează și actualizează datele brandului fără erori.
- [ ] Utilizatorul de test are drepturile necesare pe modelul `marketplace.product.brand`.

## 9. Mesaje de eroare frecvente

| Mesaj / simptom | Cauză probabilă | Remediere |
|-----------------|-----------------|-----------|
| Brandul apare de două ori în Odoo (duplicat) | Numele brandului extern nu se potrivește exact cu numele brandului existent în Odoo (maparea automată caută după `name` identic) | Editați manual `odoo_id` pe fișa binding-ului ca să legați brandul extern de cel corect, apoi ștergeți duplicatul creat |
| Produsul importat nu are brand completat | Backend-ul nu trimite `external_product_brand_id` în valorile produsului, sau importul brandului nu a rulat încă | Verificați maparea de câmpuri a conectorului; rulați mai întâi importul de branduri |
| „Method `<provider>_import_by_id` must be implemented" la apăsarea **Reimport** | Conectorul de marketplace folosit nu are implementată metoda de import pentru branduri | Verificați dacă acel provider suportă importul de branduri; contactați dezvoltatorul conectorului |
| Logo-ul brandului nu se încarcă | Backend-ul are opțiunea „Ignore Images" activată, sau URL-ul logo-ului nu este accesibil | Dezactivați „Ignore Images" pe backend sau verificați accesibilitatea URL-ului sursă |

## 10. Capturi de ecran

Capturile nu există încă în `readme/screenshots/`. Rulați skill-ul `fisa-screenshots` pentru a le
genera (metoda A — test Playwright cu mixinul `ScreenshotCase`, metoda B — Preview MCP, sau metoda
C — pluginul Chrome), cu următoarele nume planificate, în ordinea pașilor din secțiunea 6:

1. `01_backend_objects_brand.png` — backend-ul de marketplace, tabul Objects, cu obiectul Product Brand.
2. `02_lista_branduri.png` — lista brandurilor sincronizate cu backend-ul.
3. `03_fisa_brand.png` — fișa unui brand sincronizat, cu butonul Reimport.

Notă: acest modul nu ține de localizarea contabilă RO, deci mixinul `setup_country("ro")` din
`l10n_ro_doc_screenshots` nu este relevant; capturile trebuie generate pe o bază de test cu
`deltatech_marketplace` configurat (backend + cel puțin un brand sincronizat).

## 11. Observații pentru manual

În manualul final, precizați clar că acesta este un modul tehnic de sincronizare de catalog, nu unul
contabil: valoarea lui pentru utilizator este eliminarea mapării manuale a brandurilor la import/export
pe marketplace-uri, și posibilitatea de a corecta manual maparea (`odoo_id`) atunci când denumirile
diferă între Odoo și canalul extern.
