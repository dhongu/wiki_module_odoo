# Fișă Modul: Categorii publice și imagini de produs din marketplace, pe site-ul Odoo

**Modul:** `deltatech_marketplace_website`
**Utilizator principal:** Administrator Marketplace / eCommerce
**Prioritate:** 🟡 Medie (îmbunătățește fișele de produs pe site, dar nu e critic pentru sincronizarea de bază)

---

## 1. Scop business

Modulul `deltatech_marketplace_website` este o punte între **framework-ul Marketplace** (`deltatech_marketplace`,
folosit de conectoare precum Magento, Shopify, Doraly, PTC etc.) și **magazinul online Odoo** (`website_sale`).
Când comenzile sau produsele sunt sincronizate dintr-un canal extern, acest modul se asigură că informațiile
utile pentru un cumpărător online — categoria publică (folosită pentru navigare pe site), galeria de imagini
suplimentare ale produsului și descrierea lungă de site — ajung corect în Odoo, fără să suprascrie inutil
conținutul deja publicat. Este un modul „Hidden" (nu apare separat în lista de aplicații): se instalează automat
ca dependință a conectorului de marketplace ales, nu se cumpără de sine stătător.

## 2. Bază legală și context

Nu are bază legală fiscală — este un modul pur operațional/tehnic. Contextul de utilizare este integrarea
comerț electronic: sincronizarea produselor și comenzilor dintr-un marketplace (Magento, Shopify, Doraly,
PTC etc.) cu site-ul de vânzări online Odoo (`website_sale`).

## 3. Utilizatori și roluri

Administrator Marketplace (grupul `deltatech_marketplace.group_marketplace_manager`) — configurează backend-ul
de conectare și verifică rezultatul sincronizării. Utilizatorii obișnuiți (`base.group_user`) au doar drept de
citire pe categoriile publice și imaginile de produs importate.

Roluri recomandate pentru testare:
- Administrator funcțional: instalează modulul (ca dependință a unui conector) și configurează backend-ul
- Utilizator operațional (Administrator Marketplace): rulează importul/sincronizarea și verifică rezultatul
- Contabil/manager: nu este implicat — modulul nu produce note contabile

## 4. Conturi și date implicate

Nu sunt implicate conturi contabile — modulul nu generează note contabile sau documente financiare.

Date implicate:
- `product.public.category` (categoriile publice folosite de site pentru navigare)
- `product.image` (imaginile suplimentare din galeria produsului, afișate pe pagina de produs a site-ului)
- `website_description` pe `product.template` (descrierea lungă afișată pe pagina de produs)
- opțional, `website_short_description` (descrierea scurtă), doar dacă este instalat separat modulul
  `deltatech_website_short_description` — fără el, câmpul nu există și valoarea primită de la marketplace este ignorată

Date minime pentru demo:
- un backend de marketplace configurat (`deltatech_marketplace.backend`) — ex. un conector Magento/Shopify/Doraly
- pe backend, opțiunea **Use public category** activată
- cel puțin un produs pe backend, cu categorie externă, câteva imagini și o descriere de site
- modulul `website_sale` instalat, ca să poată fi verificat rezultatul pe pagina de produs a magazinului online

## 5. Configurare inițială

1. Instalați un conector de marketplace (Magento, Shopify, Doraly, PTC etc.); `deltatech_marketplace_website`
   se instalează automat ca dependință.
2. Deschideți **Marketplace → Backends** și editați backend-ul canalului dorit.
3. Bifați **Use public category** (activă implicit) dacă vreți ca subcategoriile marketplace să devină
   categorii publice Odoo, vizibile în navigarea site-ului.
4. Verificați că, la nivel de backend, opțiunea **Ignore images** nu este bifată, altfel imaginile din
   marketplace nu vor fi descărcate.
5. Rulați o sincronizare de categorii și produse (din meniul conectorului respectiv) pentru un set mic de
   produse de test.

## 6. Flux de utilizare

### Pasul 1 — Activarea categoriilor publice pe backend

Accesați **Marketplace → Backends**, deschideți fișa backend-ului canalului (Magento/Shopify/Doraly/...) și
bifați câmpul **Use public category**, adăugat de acest modul lângă opțiunea existentă **Use category**.

![Fișa backend-ului marketplace cu opțiunea Use public category](screenshots/01_backend_public_category.png)

> Dacă opțiunea este debifată, categoriile externe nu mai sunt importate ca `product.public.category`,
> iar produsele importate nu vor primi categorii publice pe site.

### Pasul 2 — Importul categoriilor din marketplace

La rularea sincronizării de categorii a conectorului (acțiune specifică fiecărui canal, de regulă din fișa
backend-ului), fiecare categorie externă este creată sau actualizată ca `product.public.category` în Odoo,
prin înregistrarea tehnică de tip binding `marketplace.public.category`. Categoriile importate se regăsesc
și pe site, în meniul de navigare al magazinului online.

Lista bindingurilor de categorii publice se poate consulta tehnic prin acțiunea **Public Categories**
(`marketplace.public.category`); modulul nu adaugă un meniu propriu pentru ea — accesați-o din
**Setări → Tehnic → Acțiuni → Acțiuni fereastră** (mod dezvoltator) sau printr-un buton adăugat de conectorul
instalat, dacă acesta o expune.

![Lista categoriilor publice importate din marketplace](screenshots/02_lista_categorii_publice.png)

Fiecare înregistrare arată corespondența dintre `external_id` (identificatorul din marketplace) și categoria
publică Odoo (`odoo_id`), plus butonul **Reimport** pentru resincronizare punctuală.

![Fișa unei categorii publice importate, cu ID extern și buton Reimport](screenshots/03_fisa_categorie_publica.png)

### Pasul 3 — Importul imaginilor suplimentare de produs

La sincronizarea unui produs, dacă acesta primește o listă de imagini de la marketplace, modulul le descarcă
și le salvează în galeria produsului (`product.image`). Sincronizarea este **idempotentă**: la reimport,
imaginile deja existente (identificate după URL) nu sunt șterse și redescărcate — se adaugă doar cele noi și
se elimină doar cele care nu mai vin din marketplace, restul galeriei rămânând neatinsă.

Lista bindingurilor de imagini se consultă tehnic prin acțiunea **Public Images**
(`marketplace.product.image`), în aceleași condiții ca la categorii (fără meniu propriu, acces din tehnic sau
din conector).

![Lista imaginilor de produs importate din marketplace](screenshots/04_lista_imagini_produs.png)

### Pasul 4 — Verificarea pe pagina de produs a site-ului

Deschideți magazinul online (**Website → eCommerce**, sau direct pagina publică a produsului) și verificați
pagina produsului sincronizat: categoria publică apare în firul de navigare/filtrele de categorie, iar
imaginile suplimentare apar în galeria produsului.

**Găsește pe ecran** — pe pagina publică a produsului, galeria de imagini (thumbnails sub imaginea principală)
și, dacă tema site-ului o afișează, categoria/breadcrumb-ul de navigare.

**Verifică** — numărul de imagini din galerie corespunde cu numărul de imagini trimise de marketplace pentru
acel produs (fără duplicate); categoria publică afișată corespunde categoriei externe mapate; descrierea de
site (`website_description`) conține textul primit din marketplace, în limba activă a site-ului.

**Treci mai departe** — dacă toate cele de mai sus corespund, produsul poate fi publicat/verificat ca gata
pentru vânzare online; dacă nu, reveniți la Pasul 1–3 și verificați configurarea backend-ului.

![Pagina publică a produsului pe site, cu categoria și galeria de imagini din marketplace](screenshots/05_pagina_produs_website.png)

### Note de monografie și raportare

Modulul nu generează note contabile — nu produce facturi, plăți sau alte documente financiare. Nu se aplică
secțiunea de monografie Dr/Cr.

## 7. Legături cu alte module / declarații

| Modul / proces | Rol în flux | Tip legătură |
|---|---|---|
| `deltatech_marketplace` | oferă modelele de bază (`marketplace.backend`, `marketplace.product`, `marketplace.product.template`, `marketplace.binding.item`) pe care acest modul le extinde | dependență (manifest) |
| `website_sale` | afișează pe site categoria publică, galeria de imagini și descrierea produsului | dependență (manifest) |
| conectoare de marketplace (Magento, Shopify, Doraly, PTC etc.) | trimit datele de categorie externă, imagini și descriere de site care sunt procesate de acest modul | integrare prin convenție (fiecare conector populează `external_public_category_ids`, `images`, `website_description`) |
| `deltatech_website_short_description` (opțional, nu e în `depends`) | dacă e instalat, activează salvarea câmpului `website_short_description` primit de la marketplace | integrare opțională, condiționată în cod |

Ce este automat: importul categoriilor publice (dacă opțiunea e activă), sincronizarea idempotentă a
imaginilor de produs, salvarea descrierii lungi de site pe limba activă.
Ce rămâne manual: activarea opțiunii **Use public category** pe fiecare backend, verificarea vizuală a
rezultatului pe pagina de produs a site-ului, instalarea modulului opțional pentru descrierea scurtă dacă
este dorită.

## 8. Verificări pentru consultant

- [ ] Modulul se instalează fără erori, ca dependință a unui conector de marketplace.
- [ ] Opțiunea **Use public category** este vizibilă și funcțională pe fișa backend-ului.
- [ ] La sincronizarea unei categorii externe, apare o categorie publică nouă (sau actualizată) în Odoo.
- [ ] La sincronizarea unui produs cu imagini, galeria produsului conține imaginile așteptate, fără duplicate.
- [ ] La resincronizare (reimport), imaginile deja existente nu sunt șterse și redescărcate inutil.
- [ ] Descrierea de site a produsului reflectă textul primit din marketplace, pe limba activă.
- [ ] Pe pagina publică a produsului (site), categoria și galeria de imagini se văd corect.
- [ ] Dacă backend-ul are **Ignore images** bifat, imaginile nu se mai descarcă (comportament așteptat).

## 9. Mesaje de eroare frecvente

| Mesaj / simptom | Cauză probabilă | Remediere |
|-----------------|-----------------|-----------|
| Categoria externă nu apare ca `product.public.category` | Opțiunea **Use public category** este debifată pe backend | Bifați opțiunea pe fișa backend-ului și rulați din nou sincronizarea de categorii |
| Imaginile de produs nu se descarcă | Backend-ul are **Ignore images** bifat, sau URL-ul imaginii primite de la marketplace nu este valid | Debifați **Ignore images**; verificați log-urile jobului de sincronizare pentru URL-uri invalide |
| Galeria produsului se golește și se reconstruiește complet la fiecare reimport | Comportament din versiuni anterioare 19.0; corectat — verificați că versiunea instalată este cea curentă (vezi `readme/NOUTATI_19.md`) | Actualizați modulul la ultima versiune |
| `website_short_description` nu se salvează deși marketplace-ul o trimite | Modulul opțional `deltatech_website_short_description` nu este instalat | Instalați modulul opțional dacă doriți descrierea scurtă pe site |
| Descrierea de site rămâne în limba greșită | Contextul de import nu avea limba (`lang`) setată corect la momentul sincronizării | Verificați limba backend-ului/conectorului și limba companiei; resincronizați produsul |

## 10. Capturi de ecran

Capturile din `readme/screenshots/` nu există încă pentru acest modul. Sunt planificate următoarele (nume
și ordine conform pașilor din secțiunea 6), de generat prin rularea skill-ului `fisa-screenshots`:

1. `01_backend_public_category.png` — fișa backend-ului marketplace, cu opțiunea „Use public category".
2. `02_lista_categorii_publice.png` — lista categoriilor publice importate din marketplace.
3. `03_fisa_categorie_publica.png` — fișa unei categorii publice, cu ID extern și buton „Reimport".
4. `04_lista_imagini_produs.png` — lista imaginilor de produs importate din marketplace.
5. `05_pagina_produs_website.png` — pagina publică a produsului pe site, cu categoria și galeria de imagini.

Recomand rularea skill-ului `fisa-screenshots` pentru a genera aceste capturi, pe o bază demo cu un backend
de marketplace configurat și `website_sale` instalat.

## 11. Observații pentru manual

În manualul final, precizați clar că modulul este o extensie tehnică „Hidden" — nu se instalează separat, ci
vine automat cu un conector de marketplace. Accentul pentru utilizator trebuie pus pe opțiunea **Use public
category** (singurul comportament configurabil direct) și pe verificarea vizuală a rezultatului pe pagina de
produs a site-ului, nu pe detalii tehnice de sincronizare (idempotență, binding-uri).
