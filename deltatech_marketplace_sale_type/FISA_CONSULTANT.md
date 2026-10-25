# Fișă Modul: Tipul comenzii de vânzare pentru comenzile de marketplace

**Modul:** `deltatech_marketplace_sale_type`
**Utilizator principal:** Consultant Odoo / administrator funcțional (configurare backend), contabil/manager vânzări (analiză pe tip de comandă)
**Prioritate:** 🟡 Medie (îmbunătățește raportarea, dar nu blochează importul comenzilor dacă lipsește)

---

## 1. Scop business

Acest modul foarte mic completează hub-ul de comenzi de marketplace (`deltatech_marketplace_sale`)
cu o singură automatizare: la importul unei comenzi dintr-un canal (eMAG, Shopify, WooCommerce etc.),
comanda de vânzare Odoo primește automat un **tip de comandă** (`so_type`, un `record.type` cu
modelul restricționat la `sale.order`), preluat din configurarea backend-ului de marketplace. Practic,
consultantul stabilește o dată, pe fiecare backend, „toate comenzile de pe acest canal sunt de tipul
X" (de exemplu „Comandă eMAG", „Comandă Shopify B2C"), iar de atunci încolo fiecare comandă importată
de pe acel canal moștenește automat clasificarea, fără nicio intervenție manuală la fiecare comandă.
Beneficiul e în raportare: comenzile pot fi grupate/filtrate după tip alături de comenzile clasice
(non-marketplace), pentru analize de vânzări granulare pe canal sau pentru a distinge rapid o comandă
de marketplace de o comandă directă în listele și rapoartele care folosesc deja clasificarea
`record.type`.

## 2. Bază legală și context

Nu există bază legală — este o clasificare internă, operațională, fără implicații fiscale sau
contabile directe. Contextul este pur organizatoric: susține raportarea de vânzări pe canal/tip de
comandă în cadrul suitei de conectori de marketplace Terrabit.

## 3. Utilizatori și roluri

- **Consultant/administrator funcțional**: configurează, o singură dată per backend, tipul de comandă
  implicit (`so_type_id`) și se asigură că există înregistrarea `record.type` corectă pentru modelul
  `sale.order`.
- **Contabil/manager vânzări**: folosește clasificarea rezultată pentru grupare/filtrare și rapoarte
  de vânzări pe tip de comandă.

Roluri recomandate la testare:
- Administrator funcțional: instalează modulul, completează câmpul pe backend.
- Utilizator operațional: importă (sau simulează importul) unei comenzi de pe acel backend.
- Manager/consultant: verifică pe comanda rezultată că tipul a fost preluat corect.

## 4. Conturi și date implicate

Nu sunt implicate conturi contabile — modulul nu generează note contabile, doar completează un câmp
de clasificare pe comanda de vânzare. Date minime pentru demo:

- un **backend de marketplace** (`marketplace.backend`, din `deltatech_marketplace`) existent sau nou;
- cel puțin o înregistrare **`record.type`** (model tehnic furnizat de modulul dependent
  `deltatech_record_type`) restricționată la modelul `sale.order` — de exemplu „Comandă Marketplace";
- un client și o comandă de test importată de pe acel backend (prin fluxul real al unui conector, sau
  prin apelul tehnic `save_from_marketplace` folosit și în testele automate ale modulului).

> Notă: modelul `record.type` și câmpul `so_type` de pe `sale.order` sunt furnizate de modulul
> dependent `deltatech_record_type`, nu de acest modul. Pentru meniul exact unde se creează/gestionează
> tipurile de înregistrare și pentru orice altă utilizare a clasificării (pe alte documente decât
> comanda de vânzare), consultați fișa modulului `deltatech_record_type`. Acest modul
> (`deltatech_marketplace_sale_type`) adaugă strict legătura automată backend → comandă importată.

## 5. Configurare inițială

1. Instalați modulul `deltatech_marketplace_sale_type` (necesită `deltatech_marketplace_sale` și
   `deltatech_record_type` deja instalate, conform manifestului).
2. Creați (sau identificați) o înregistrare `record.type` cu modelul setat la `sale.order` pentru
   fiecare categorie de comandă pe care vreți să o distingeți (ex. „Comandă eMAG", „Comandă Shopify").
3. Pe fiecare backend de marketplace relevant, deschideți formularul și completați câmpul **Order
   Type** (`so_type_id`) cu tipul dorit.
4. Pregătiți un client și importați (sau simulați importul) unei comenzi de test de pe acel backend.

## 6. Flux de utilizare

### Pasul 1 — Setarea tipului de comandă pe backend

Deschideți **Marketplace → Backends**, formularul unui backend, și completați câmpul **Order Type**
(`so_type_id`) — vizibil în grupul unde acest modul îl adaugă alături de câmpurile de plată ale
backend-ului. Câmpul acceptă orice `record.type` al cărui model este `sale.order`.

![Backend de marketplace — câmpul Order Type completat](screenshots/01_backend_so_type_field.png)

### Pasul 2 — Comanda importată preia automat tipul

La importul unei comenzi de pe acel backend (fluxul standard al unui conector, sau tehnic prin
`save_from_marketplace`), comanda de vânzare Odoo rezultată are câmpul `so_type` completat automat
cu valoarea `so_type_id` a backend-ului, fără nicio acțiune suplimentară a operatorului. Dacă
backend-ul nu are niciun tip setat, comanda rămâne fără tip (comportamentul standard Odoo, neschimbat
de acest modul).

![Comanda de vânzare rezultată din import, cu tipul preluat de pe backend](screenshots/02_sale_order_so_type.png)

### Note de monografie și raportare

Nu se aplică — modulul nu generează note contabile. Contabilizarea comenzii/facturii urmează fluxul
standard Odoo (`sale`/`account`), complet neatinsă de această clasificare.

## 7. Legături cu alte module / declarații

| Modul / proces | Rol în flux | Tip legătură |
|---|---|---|
| `deltatech_marketplace_sale` | hub-ul comenzilor de marketplace — `marketplace.sale.order`, `prepare_values`, `save_from_marketplace` | dependență (manifest) |
| `deltatech_record_type` | furnizează modelul `record.type` și câmpul `so_type` pe `sale.order` | dependență (manifest) |
| Conectorii concreți (`_emag`, `_shopify`, `_woocommerce`, `_magento`, `_prestashop`, `_merchantpro`, `_trendyol`) | declanșează importul care produce comanda clasificată | flux standard prin `deltatech_marketplace_sale` |

Ce este automat: completarea câmpului `so_type` pe comanda de vânzare importată, pe baza `so_type_id`
al backend-ului, la fiecare import (inclusiv reimport).

Ce rămâne manual: crearea/gestionarea înregistrărilor `record.type` (asigurată de modulul
`deltatech_record_type`), alegerea tipului potrivit pe fiecare backend, și orice reclasificare
manuală ulterioară a unei comenzi deja importate (modulul nu suprascrie o schimbare manuală ulterioară
decât la un nou import/reimport).

## 8. Verificări pentru consultant

- [ ] Modulul se instalează fără erori, cu `deltatech_marketplace_sale` și `deltatech_record_type`
      deja prezente.
- [ ] Câmpul **Order Type** apare pe formularul backend-ului de marketplace și acceptă doar
      `record.type` cu modelul `sale.order`.
- [ ] O comandă importată de pe un backend cu **Order Type** completat are câmpul `so_type` setat
      corect pe comanda de vânzare rezultată.
- [ ] O comandă importată de pe un backend **fără** **Order Type** completat rămâne fără tip (nicio
      eroare, comportament degradat elegant).
- [ ] Reimportul unei comenzi existente (`Reimport`/`Refresh Marketplace` din
      `deltatech_marketplace_sale`) recalculează `so_type` dacă tipul backend-ului s-a schimbat între
      timp.
- [ ] Semnătura metodei `prepare_values(values, skip_ignore_fields=False)` este respectată — o
      suprascriere ulterioară a acestei metode (în alt modul custom) trebuie să păstreze ambii
      parametri, altfel apare `TypeError` la apelul din `save_from_marketplace`.
- [ ] Rapoartele/listele de vânzări care grupează după tipul comenzii reflectă corect distincția
      marketplace vs. comenzi directe.

## 9. Mesaje de eroare frecvente

| Mesaj / simptom | Cauză probabilă | Remediere |
|---|---|---|
| `TypeError` la `save_from_marketplace` / `prepare_values` | O suprascriere custom a `prepare_values` pe `marketplace.sale.order` (în alt modul) nu respectă semnătura de bază `(values, skip_ignore_fields=False)` | Corectați semnătura suprascrierii custom, ca în acest modul |
| Comanda importată nu are niciun tip completat | Backend-ul nu are **Order Type** (`so_type_id`) setat | Completați câmpul pe backend, apoi reimportați comanda |
| Câmpul **Order Type** nu apare pe formularul backend-ului | View-ul `deltatech_marketplace.view_marketplace_backend_form` a fost modificat/înlocuit de alt modul, iar xpath-ul de inserare (`group name="payment"`) nu se mai potrivește | Verificați moștenirea de view-uri pe formularul backend-ului și grupul `payment` |
| Tipul de comandă nu se actualizează după ce a fost schimbat pe backend | Comanda deja importată nu a fost reimportată — câmpul se recalculează doar la (re)import | Reimportați comanda din binding-ul ei (`Reimport`) sau din `Refresh Marketplace` |

## 10. Capturi de ecran

Modulul nu are încă folderul `readme/screenshots/` populat — capturile de mai jos sunt **planificate**,
în ordinea pașilor din secțiunea 6, și trebuie generate cu skill-ul `fisa-screenshots` (mixinul
`ScreenshotCase` din `l10n_ro_doc_screenshots`, import defensiv), pe planul de conturi RO:

1. `01_backend_so_type_field.png` — formularul backend-ului de marketplace, cu câmpul **Order Type**
   completat.
2. `02_sale_order_so_type.png` — comanda de vânzare rezultată din import, cu tipul preluat automat.

Regenerare (după ce testul de capturi este scris):

```bash
./odoo/odoo-bin -c odoo.conf -d <db> -u deltatech_marketplace_sale_type,l10n_ro_doc_screenshots \
    --test-enable --test-tags=fise_screenshots --stop-after-init
```

## 11. Observații pentru manual

În manualul final, tratați acest modul ca pe o completare minoră, nu ca pe un modul de sine stătător:
valoarea lui e o singură automatizare (backend → tip de comandă la import), utilă doar dacă
`deltatech_record_type` e deja folosit de client pentru clasificarea comenzilor de vânzare. Nu
prezentați clasificarea `record.type` ca fiind definită de acest modul — ea aparține modulului
`deltatech_record_type` și trebuie documentată acolo, cu meniul real de configurare a tipurilor.
