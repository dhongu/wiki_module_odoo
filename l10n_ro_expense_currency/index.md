# Romania - Avansuri de trezorerie în valută (542) (localizat la `l10n_ro_expense_currency/index.md`)

- **Nume Tehnic:** `l10n_ro_expense_currency`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_expense_currency
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_expense_currency`
- **Ultima Ingestie:** `2026-10-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul gestionează avansurile de trezorerie acordate angajaților în valută, cu justificarea decontului și recunoașterea diferențelor de curs valutar conform OMFP 1802/2014. Acoperă tot fluxul: acordarea avansului (Dr 542 = Cr bancă/casă), justificarea cu diferența de curs (665/765) și returul restului nejustificat. Este util companiilor ai căror angajați primesc avansuri în EUR, USD etc., de exemplu pentru deplasări externe.

#### 2. Funcționalități Cheie

- **Acordare avans:** nota contabilă Dr 542 = Cr cont de bancă sau casă, la cursul BNR din data acordării (editabil). Se completează referința, angajatul, valuta, data și suma acordată.
- **Justificare decont:** se completează data justificării, suma justificată, cursul la data justificării și contul de cheltuieli (de exemplu 625 sau 624). Nota recunoaște cheltuiala, stinge contul 542 și înregistrează diferența de curs: pierdere pe 665, câștig pe 765. Suma justificată nu poate depăși suma acordată; este permisă o singură justificare pe avans. Dacă suma justificată este egală cu cea acordată, avansul se închide direct.
- **Retur rest:** dacă suma justificată este mai mică, butonul **Retur rest** generează nota pentru partea nejustificată, la cursul avansului, iar avansul se închide.
- **Anulare:** notele generate se anulează în ordine inversă (retur, justificare, acordare); un avans anulat poate fi readus în Schiță cu **Resetează în Schiță**. Dacă perioada este blocată fiscal, notele nu pot fi anulate.
- **Stări:** Schiță → Acordat → Justificat → Închis, plus Anulat.
- **Configurare:** în **Contabilitate → Configurare → Setări**, secțiunea *Avansuri Trezorerie Valutare (542)*: conturile 542, 665, 765 și jurnalul de acordare (bancă sau casă). Conturile 665 și 765 sunt necesare doar la o diferență de curs diferită de zero. Cursurile se iau din tabelul de cursuri Odoo (provider BNR); dacă lipsește cursul unei date, se preia ultima valoare disponibilă.
- **Meniu:** **Contabilitate → Contabilitate → Avansuri 542 → Avansuri Trezorerie Valutare**.

#### 3. Dependențe

- `account`
- `l10n_ro`
- `hr`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.cash.advance`: avansul de trezorerie în valută (cu `mail.thread`), cu mașină de stări și acțiunile `action_post_advance`, `action_post_justification`, `action_post_return`, `action_cancel` și `action_reset_draft`. Calculează cursurile, echivalentul în lei și `exchange_difference` = suma justificată × (curs justificare − curs acordare); pozitiv înseamnă pierdere (665), negativ câștig (765).
- `res.company` (extins): `l10n_ro_advance_account_id` (542), `l10n_ro_advance_loss_account_id` (665), `l10n_ro_advance_gain_account_id` (765) și `l10n_ro_advance_journal_id`.
- `res.config.settings` (extins): expune în setări conturile și jurnalul de mai sus.

**Vizualizări**

- `l10n_ro_cash_advance_view_form`, `l10n_ro_cash_advance_view_list`, `l10n_ro_cash_advance_view_search`: formularul, lista și căutarea avansurilor; acțiunea `l10n_ro_cash_advance_action` are implicit filtrul `open`.
- `res_config_settings_view_form_l10n_ro_expense_currency`: secțiunea de configurare a conturilor și jurnalului.
- Meniuri `l10n_ro_cash_advance_menu_root` („Treasury Advances 542”, sub `account.menu_finance_entries`) și `l10n_ro_cash_advance_menu_list`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server; notele contabile se generează la apăsarea butoanelor de pe avans.

#### 5. Conexiuni

- [l10n_ro_currency_revaluation](../l10n_ro_currency_revaluation/index.md): reevaluarea valutară generală, separată de fluxul avansurilor (menționată în fișa consultant).
