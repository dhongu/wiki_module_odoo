# Romania - Storno Enhancements (localizat la `l10n_ro_storno_enhancement/index.md`)

- **Nume Tehnic:** `l10n_ro_storno_enhancement`
- **Fost nume tehnic:** `l10n_ro_account_storno` (redenumit pe 07.10.2026)
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_storno_enhancement
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_storno_enhancement`
- **Ultima Ingestie:** `2026-10-07`

#### 1. Sumar

Modulul implementează contabilitatea de tip **storno** (înregistrări în roșu / cu sumă negativă) conform standardelor contabile românești. În loc să anuleze o operațiune greșită printr-o înregistrare pe partea opusă a contului (care umflă artificial rulajele), storno-ul **inversează** suma chiar pe poziția inițială, cu valoare negativă, astfel încât soldurile și rulajele rămân corecte. Notele contabile diverse pot fi marcate și manual ca storno în roșu.

**Redenumire.** Modulul s-a numit anterior `l10n_ro_account_storno`. Numele tehnic vechi este ocupat pe Odoo Apps de alt publicator, așa că modulul a fost redenumit pe 07.10.2026 în `l10n_ro_storno_enhancement` (dhongu/l10n-romania#605 pe 19.0, #606 pe 18.0, #607 pe 20.0). Cine caută după `l10n_ro_account_storno` ajunge la această pagină. Funcționalitatea existentă a rămas neschimbată.

#### 2. Funcționalități Cheie

- **Înregistrări negative (în roșu):** pentru notele marcate ca storno, debitul și creditul se calculează cu valori negative, pe partea naturală a fiecărui cont, pentru raportare corectă în registrele contabile.
- **Utilizarea contului:** câmpul „Usage" pe conturile din planul de conturi, cu valorile **Bifunctional** (implicit), **Activ** și **Pasiv**. Se află pe formularul contului, în fila de contabilitate. La instalare, pentru companiile cu planul de conturi românesc (`chart_template = ro`), valorile se inițializează automat pe baza codului contului (liste de conturi active, pasive și bifuncționale).
- **Logică de storno îmbunătățită:** o notă care stornează o notă existentă este marcată automat ca storno (`is_storno`), iar stornarea unei note deja storno revine la o notă normală (dublă stornare).
- **Storno manual în roșu pe notele contabile:** câmpul „Storno (red reversal)" (`l10n_ro_force_storno`) pe `account.move` forțează înregistrarea în roșu pentru toate liniile unei note. Se folosește pentru a înregistra manual stornări în roșu. Se aplică doar notelor de tip `entry` (note contabile diverse), poate fi modificat doar cât nota este ciornă și nu se copiază la duplicare. Rezultatul calculat apare lângă el în câmpul „Is Storno" (doar citire), în fila „Other Info" a notei.
- **Migrare automată de la numele vechi:** la instalare, `pre_init_hook` preia înregistrările modulului vechi `l10n_ro_account_storno`, dacă este instalat, prin aceiași pași ca `merge_module` din upgrade-util (fără dependență externă). Câmpurile, vizualizările și datele sunt mutate pe noul nume, constrângerile și relațiile modelului sunt reasignate, dependențele altor module sunt redirecționate, iar modulul vechi este scos din lista de module. Valorile „Usage" setate pe conturi se păstrează, deoarece `post_init_hook` nu mai reinițializează conturile când s-a făcut migrarea.
- **Corecție față de DESCRIPTION.md:** readme-ul menționează valorile „Debit, Credit sau Bivalent" și o setare de activare la nivel de companie. În cod, valorile sunt Bifunctional / Activ / Pasiv, iar o setare pe companie nu există în versiunea curentă (logica veche pe `res.company.account_storno` este comentată în cod). Pagina urmează codul.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.account` (extins): adaugă câmpul `l10n_ro_usage` (Bifunctional / Activ / Pasiv, implicit Bifunctional).
- `account.move` (extins): adaugă `l10n_ro_force_storno` și suprascrie `_compute_is_storno`. Nota care stornează o altă notă primește `is_storno` opus celei stornate. Nota de tip `entry` cu `l10n_ro_force_storno` primește `is_storno = True`.
- `res.company` (extins): metoda `_l10n_ro_initialize_accounts`, care setează `l10n_ro_usage` pe conturile companiilor cu planul de conturi `ro`, după codul contului.

**Vizualizări**

- `view_account_form` (`account.account`): afișează câmpul „Usage" în fila de contabilitate a contului.
- `view_move_form` (`account.move`): afișează „Storno (red reversal)" (editabil doar în ciornă) și „Is Storno" (doar citire) în fila de informații suplimentare a notelor diverse.

**Hook-uri**

- `pre_init_hook`: preia înregistrările modulului vechi `l10n_ro_account_storno` (vezi mai sus).
- `post_init_hook`: inițializează „Usage" pe conturi, cu excepția cazului în care s-a făcut migrarea de la modulul vechi.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

**Teste** (`tests/test_storno.py`): câmpul `l10n_ro_usage` și valoarea implicită, storno la stornare și dublă stornare, inițializarea conturilor, storno manual.

#### 5. Conexiuni

- `l10n_ro`: localizarea contabilă pentru România, al cărei plan de conturi determină inițializarea valorilor „Usage".
