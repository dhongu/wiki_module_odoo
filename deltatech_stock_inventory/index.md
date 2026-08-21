# Stock Inventory (localizat la `deltatech_stock_inventory/index.md`)

- **Nume Tehnic:** `deltatech_stock_inventory`
- **Versiune:** `19.0.2.7.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_stock_inventory
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_inventory`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul restaurează și extinde funcționalitatea de inventar clasic (`stock.inventory`) din Odoo, eliminată în versiunile mai noi, oferind un instrument complet pentru gestiunea și controlul valoric al stocurilor. Le permite utilizatorilor să creeze documente de inventar, să numere produsele pe locații și să valideze diferențele, actualizând în același timp prețurile de cost și straturile de evaluare a stocului (SVL). Adaugă vizibilitate sporită asupra stocului defalcat pe depozite, câmpuri de localizare manuală (raft, rând, poliță, cutie), scanare cu cititorul de coduri de bare și control de securitate asupra cine poate modifica cantitățile. Este compatibil cu modulele de contabilitate pentru România (l10n_ro), fiind util companiilor care doresc un proces de inventariere riguros și aliniat cerințelor locale.

#### 2. Funcționalități Cheie

- **Sistem de inventar clasic:** readuce funcționalitatea vechiului model `stock.inventory`, eliminat în versiunile recente de Odoo.
- **Evaluare valorică îmbunătățită a stocului:**
  - afișează coloane cu prețul stocului în vizualizările de inventar;
  - permite actualizarea prețurilor de cost ale produselor în timpul validării inventarului.
- **Vizibilitate stoc pe mai multe depozite:**
  - afișează stocul defalcat pe coduri de depozit direct în vizualizarea Kanban a produsului;
  - opțiune de configurare pe depozit pentru a afișa stocul total sau doar din locația principală.
- **Control manual al locației:**
  - adaugă câmpurile Raft, Rând, Poliță și Cutie pe produse și pe liniile de inventar;
  - câmpurile pot fi activate/dezactivate din setările de inventar.
- **Control de securitate:**
  - adaugă grupul de securitate „Poate actualiza cantitățile" pentru a restricționa cine poate modifica cantitățile de inventar.
- **Actualizare preț la inventar:**
  - când parametrul de sistem `stock.use_inventory_price` este setat pe True, prețul de cost al produselor (cu evaluare FIFO) este actualizat cu prețul din liniile de inventar.
- **Arhivarea inventarului:**
  - opțiune de arhivare a vechilor straturi de evaluare a stocului (SVL) și de creare a unora noi pe baza numărătorilor de inventar;
  - compatibilitate cu modulele de contabilitate pentru România (l10n_ro).
- **Suport pentru coduri de bare:**
  - scanare integrată pentru operațiuni de inventar mai rapide;
  - suport pentru scanarea produselor și a numerelor de lot/serie.
- **Raportare îmbunătățită:**
  - rapoarte de inventar încorporate;
  - vizualizări detaliate ale ajustărilor de inventar.
- **Funcții de gestiune a inventarului:**
  - filtrare după locație, raft sau produs;
  - marcarea liniilor de inventar ca „OK" pentru verificare;
  - crearea de inventare noi din liniile neverificate;
  - precompletarea cantităților numărate cu stocul curent sau cu zero;
  - includerea produselor epuizate (cu cantitate zero).

#### 3. Dependențe

- `stock`
- `stock_account`
- `purchase_stock`
- `sale_stock`

#### 4. Componente Cheie

Documentația pentru Sumar și Funcționalități Cheie a fost generată din `readme/DESCRIPTION.md`, care nu solicită explicit detalierea componentelor tehnice. Conform fluxului de ingestie, analiza codului pentru această secțiune a fost omisă.

#### 5. Conexiuni

- [deltatech_stock_account](../deltatech_stock_account/index.md): integrare cu evaluarea contabilă a stocului și straturile de evaluare (SVL) folosite la validarea inventarului.
- `l10n_ro`: compatibilitate cu modulele de contabilitate pentru România, relevante la arhivarea SVL și actualizarea evaluării stocului.
