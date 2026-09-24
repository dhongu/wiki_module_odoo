# Stock Inventory (localizat la `deltatech_stock_inventory/index.md`)

- **Nume Tehnic:** `deltatech_stock_inventory`
- **Versiune:** `19.0.2.10.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_stock_inventory
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_inventory`
- **Ultima Ingestie:** `2026-09-24`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul readuce documentul clasic de inventar (`stock.inventory`), eliminat din nucleul Odoo în
versiunile recente, oferind gestionarilor de stoc un document cu număr, filtre pe locații și produse,
stări *Ciornă → În desfășurare → Validat* și mișcări de stoc generate la validare. Pe fiecare linie
arată impactul valoric înainte de validare — cost unitar, valoare scriptică, valoare numărată,
diferență — astfel încât managerul de stoc vede câți lei înseamnă plusurile și minusurile înainte de
a le înregistra. În jurul documentului, modulul mai adaugă amplasamente manuale pe produs, defalcarea
stocului pe depozite în kanban, un drept separat pentru cine poate modifica cantitățile, confirmarea
rapidă a stocului unui produs, unirea inventarelor validate și gruparea zilnică a reaprovizionărilor
manuale.

#### 2. Funcționalități Cheie

- **Sistem de inventar clasic:** documente cu număr din secvența `INV`, filtre pe locații/produse,
  opțiunea de a include produsele epuizate și de a precompleta cantitatea numărată (stoc curent sau
  zero).
- **Evaluare valorică pe linie** (vizibilă doar grupului *Inventar / Administrator*): valoare unitară
  fotografiată la generare, valoare teoretică/numărată/diferență pe linie și pe document, plus
  valoarea efectiv postată la validare; mișcarea de stoc păstrează legătura cu linia care a generat-o.
- **Actualizare preț la inventar:** cu parametrul de sistem `stock.use_inventory_price` activ
  (implicit), plusurile pe produse FIFO/cost mediu intră la **Prețul** liniei, fără reevaluarea
  stocului existent; minusurile ies mereu la costul curent.
- **Vizibilitate stoc pe mai multe depozite:** stocul defalcat pe coduri de depozit în kanban-ul de
  produse, cu opțiune per depozit (Toate / Locație principală / Detaliat cu rezervat, blocat, în
  tranzit, așteptat).
- **Control manual al locației:** câmpuri Raft, Rând, Etaj și Casetă pe produse și pe liniile de
  inventar, activabile din setările de inventar.
- **Control de securitate:** grupul „Poate actualiza cantitățile" restricționează cine aplică
  ajustări cu diferență pe **Inventariere fizică**; grupul „Unire documente inventar" restricționează
  unirea documentelor.
- **Funcții de gestiune a inventarului:** tipărirea listei de numărare și a raportului de diferențe,
  marcarea liniilor ca „E Ok", mutarea liniilor nenumărate într-un inventar nou sau eliminarea lor,
  unirea mai multor inventare validate, confirmarea rapidă a stocului unui produs (creează un inventar
  fără diferențe) și reaprovizionare grupată zilnic pe depozit.

#### 3. Dependențe

- `stock`
- `stock_account`
- `purchase_stock`
- `sale_stock`

#### 4. Componente Cheie

Documentația pentru Sumar și Funcționalități Cheie a fost generată din `readme/DESCRIPTION.md` și
`readme/FISA_CONSULTANT.md`, care nu solicită explicit detalierea componentelor tehnice. Conform
fluxului de ingestie, analiza codului pentru această secțiune a fost omisă.

#### 5. Conexiuni

- [l10n_ro_inventory_closing](../l10n_ro_inventory_closing/index.md): procesul RO de inventariere
  anuală (tipul diferenței — neimputabil, imputabil cu TVA, casare — și procesul-verbal OMFP
  2861/2009), complementar documentului operațional din acest modul.
- [l10n_ro_inventory_register](../l10n_ro_inventory_register/index.md): Registrul-inventar anual
  preia soldul stocurilor rezultat după inventariere.
- `purchase_stock`, `sale_stock`: sursa stocului așteptat de la furnizori afișat în kanban-ul de
  produse și baza asistentului de reaprovizionare grupată.

---

### Notă privind corectările față de DESCRIPTION.md

`readme/DESCRIPTION.md` menționează două funcționalități care nu mai există în codul 19.0 și care au
fost tratate ca atare (nu ca funcționalități active), conform fișei consultant:

- **arhivarea straturilor de evaluare a stocului (SVL)** — straturile de valoare nu mai există în
  19.0, opțiunea nu are efect și nu apare pe formular;
- **integrare proprie de coduri de bare** — modulul nu are integrare proprie; numărarea cu scanerul
  se face din aplicația standard, pe **Inventariere fizică**.

Ambele sunt documentate ca limitări cunoscute în [FISA_CONSULTANT.md](FISA_CONSULTANT.md), secțiunea
„Limitări cunoscute", nu ca funcționalități curente.
