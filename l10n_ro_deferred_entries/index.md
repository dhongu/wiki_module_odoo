# Romania - Venituri și Cheltuieli Înregistrate în Avans (471/472) (localizat la `l10n_ro_deferred_entries/index.md`)

- **Nume Tehnic:** `l10n_ro_deferred_entries`
- **Versiune:** `19.0.2.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_deferred_entries
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_deferred_entries`
- **Ultima Ingestie:** 2026-06-09
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul configurează automat mecanismul nativ Odoo Enterprise de recunoaștere a cheltuielilor și veniturilor înregistrate în avans, conform OMFP 1802/2014 pct. 233–237, folosind conturile 4711 (Cheltuieli înregistrate în avans) și 4721 (Venituri înregistrate în avans) din planul de conturi românesc. Se bazează pe motorul nativ `account_accountant` (Enterprise) — câmpurile „Deferred Date" (Start Date / End Date) de pe liniile de factură și raportul Deferred Expenses/Revenues sunt disponibile fără cod custom adițional. Astfel, după instalare, contabilul completează doar intervalul de recunoaștere pe linia de factură, iar Odoo generează singur nota de transfer și notele lunare de recunoaștere până la epuizarea soldului.

#### 2. Funcționalități Cheie

- Configurare automată la instalare: contul `4711` devine `Deferred Expense Account`, iar contul `4721` devine `Deferred Revenue Account` în setările companiei.
- Jurnalul de Operațiuni diverse este setat automat ca jurnal de amânare.
- Metoda de calcul implicită: Months (recunoaștere liniară pe luni calendaristice).
- Pe linia de factură (cont 6xx sau 7xx) se completează câmpul „Deferred Date" cu intervalul de recunoaștere (Start → End).
- La postarea facturii, Odoo generează automat intrarea de transfer (`Dr 4711 = Cr 6xx`) și planifică notele lunare de recunoaștere (`Dr 6xx = Cr 4711`).

#### 3. Dependențe

- `account_accountant`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

Modulul nu definește și nu extinde modele Python — reutilizează integral mecanismul nativ de amânare din `account_accountant`, bazat pe câmpurile `deferred_start_date` / `deferred_end_date` de pe `account.move.line` și pe conturile/jurnalul de amânare configurate pe `res.company`.

**Vizualizări**

Modulul nu adaugă vizualizări proprii (`data` este gol în manifest); se folosesc câmpurile și rapoartele native Enterprise (raportul Deferred Expense / Deferred Revenue).

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook` (`hooks.py`, expus în `__init__.py`): rulează o singură dată la instalare. Caută companiile cu țara fiscală RO și completează automat `deferred_expense_account_id` (cont `4711%`), `deferred_revenue_account_id` (cont `4721%`) și jurnalul de amânare (jurnalul de tip `general`), dacă acestea nu sunt deja setate.
- Recunoașterea lunară este realizată de mecanismul standard de amânare din `account_accountant`, care generează și postează notele la scadență.

#### 5. Conexiuni

- [l10n_ro_fixed_assets](../l10n_ro_fixed_assets/index.md): mecanism nativ Enterprise similar (amortizare mijloace fixe) configurat pentru planul de conturi RO.
- [l10n_ro_financial_notes](../l10n_ro_financial_notes/index.md): notele explicative la situațiile financiare, unde se reflectă soldurile de venituri și cheltuieli în avans.
