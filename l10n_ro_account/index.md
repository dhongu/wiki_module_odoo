# Romania - Account

- **Nume Tehnic:** `l10n_ro_account`
- **Versiune:** `20.0.0.5.1`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_account
- **Cale Locală:** odoo-addons/l10n-romania-oca/l10n_ro_account
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modul de bază pentru contabilitatea românească, care adaugă mici reguli de lucru specifice localizării: limitarea încasărilor în numerar, afișarea conturilor în format scurt (cum se folosește în practica contabilă din România) și corecția traducerii pentru încasări.

#### 2. Funcționalități Cheie

- Limitarea încasărilor în numerar de la clienți: la înregistrarea unei plăți primite într-un jurnal de tip numerar, suma este verificată față de plafoane diferite pentru persoane juridice (implicit 5000) și persoane fizice (implicit 10000). Plafoanele se pot schimba prin parametrii de sistem `l10n_ro_accounting.amount_company_limit` și `l10n_ro_accounting.amount_person_limit`.
- Verificarea se aplică atât plăților (`account.payment`), cât și asistentului de înregistrare a plății de pe factură, doar pentru companiile cu localizare română.
- Afișarea conturilor în format scurt (ex. `5121` în loc de `512100`, sau `4426.1` pentru analitice) în numele afișat al contului, când compania are contabilitatea românească activă.
- Corecție de traducere pentru termenul „încasare”.

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_config](../l10n_ro_config/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.mixin.payment.check`: mixin abstract cu verificarea plafonului de încasare în numerar.
- `account.payment`: extins cu mixinul de verificare.
- `account.payment.register`: wizard extins; `action_create_payments` verifică suma înainte de creare.
- `account.account`: câmpul calculat `l10n_ro_external_code` (cod scurt) și numele afișat în format scurt.

**Vizualizări**

- Modulul nu definește vizualizări.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [l10n_ro_config](../l10n_ro_config/index.md): furnizează mixinul `l10n.ro.mixin` și setările de localizare.
