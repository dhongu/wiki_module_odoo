# Romania - Cash Journal Numbering (localizat la `l10n_ro_account_sequence/index.md`)

- **Nume Tehnic:** `l10n_ro_account_sequence`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_account_sequence
- **Cale Locală:** odoo-addons/l10n-romania/l10n_ro_account_sequence
- **Ultima Ingestie:** `2026-10-30`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul dă documentelor din jurnalul de casă numerotare separată pe tip de document, așa cum cere evidența casieriei într-o firmă românească: chitanțe emise, chitanțe primite de la furnizori, dispoziții de plată și dispoziții de încasare. Fiecare tip are propria serie, cu prefix, iar numerele rămân consecutive și reîncep de la 1 în fiecare an, ceea ce face registrul de casă corect și ușor de verificat. Plățile prin casă se înregistrează direct în contul casei, iar nota contabilă primește documentul justificativ potrivit în loc de „Notă contabilă”.

#### 2. Funcționalități Cheie

- Câmp nou **Tip document** pe plățile din jurnalele de casă (nu apare pe cele bancare), propus automat după sensul plății și tipul partenerului și modificabil cât timp plata e în ciornă:
  - *Chitanță client* (prefix **CH**) — încasare de la client;
  - *Chitanță furnizor* (**PL**) — plată către furnizor;
  - *Dispoziție de plată* (**DP**) — plată către un client, de exemplu restituirea unui avans;
  - *Dispoziție de încasare* (**DI**) — încasare de la un furnizor;
  - *Transfer intern* (**IT**) — doar ales manual; *Altele* — fără prefix.
- Serie separată pentru fiecare tip, de forma `<prefix><cod jurnal>/<an>/<nr. de ordine>` (ex. `CHCSH1/2026/00001`); numărul se dă la confirmare. Plățile prin bancă rămân pe numerotarea standard. Seriile se aplică doar companiilor cu planul de conturi `ro`.
- Metodele de plată ale jurnalului de casă înregistrează direct în contul casei (5311), fără cont intermediar de plăți în curs. Sincronizarea rulează la crearea jurnalului și la modificarea contului implicit sau a metodelor de plată; liniile deja înregistrate pe vechiul cont se mută pe contul casei, inclusiv cele din perioade închise.
- Nota contabilă a plății primește documentul justificativ corespunzător (Chitanță client, Chitanță furnizor, Dispoziție de plată, Dispoziție de încasare), afișat în jurnalele românești; notele existente se completează la actualizarea la 19.0.1.1.0.
- Coloană, filtru și grupare după **Tip document** în lista de plăți (**Facturare → Clienți / Furnizori → Plăți**); tipul apare și pe nota contabilă.
- Meniul „Plăți de primit” (`account.menu_action_account_payments_receivable`) este redenumit „Receivable payments”.
- Fișa consultant detaliază fluxul pas cu pas, monografia (ex. `Dr 5311 = Cr 4111` la chitanța client), verificările și mesajele de eroare frecvente; nu sunt refăcute aici.

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_account_move_document_type](../l10n_ro_account_move_document_type/index.md)

#### 4. Componente Cheie

**Modele**

- `account.payment` (extins): câmpurile `l10n_ro_cash_document_type` (tip document de casă, obligatoriu, implicit „Altele”) și `l10n_ro_journal_type`; onchange-uri care propun tipul după sensul plății și partener, iar la creare se completează automat dacă lipsește.
- `account.move` (extins): `l10n_ro_cash_document_type` (legat de plata de origine); `_l10n_ro_get_document_type()` întoarce tipul de casă pe notele de tip `entry`; `_get_last_sequence_domain()` și `_get_starting_sequence()` separă seria pe tip și pun prefixul (CH, PL, DP, DI, IT).
- `account.journal` (extins): `_sync_cash_payment_accounts()` pune contul implicit al jurnalului de casă pe metodele de plată; acțiunea `remove_outstanding_accounts()` o poate rula manual, iar `_remove_outstanding_account()` mută liniile existente pe contul casei.

**Vizualizări**

- `view_account_payment_tree`: coloana **Tip document** în lista plăților.
- `view_account_payment_search`: câmp de căutare și grupare după tipul documentului.
- `view_account_payment_form`: câmpul **Tip document**, vizibil doar pe jurnalele de casă și editabil doar în ciornă.
- `view_move_form`: tipul documentului de casă pe nota contabilă.

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau acțiuni server. O migrare `post-migrate` (19.0.1.1.0) completează documentul justificativ pe notele plăților prin casă existente.

#### 5. Conexiuni

- [l10n_ro_cash_register](../l10n_ro_cash_register/index.md): registrul de casă tipărit; numărul documentului din registru este numărul plății, cu prefixul seriei.
- [l10n_ro_account_vat_journal](../l10n_ro_account_vat_journal/index.md): coloana „Tip document” din jurnalul de TVA citește documentul justificativ al notei.
- [l10n_ro_account_move_document_type](../l10n_ro_account_move_document_type/index.md): furnizează documentul justificativ pus pe nota plății de casă (dependență; fără pagină wiki).
