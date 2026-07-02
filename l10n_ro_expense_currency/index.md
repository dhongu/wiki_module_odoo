# Romania - Avansuri Trezorerie Valutare (542) (localizat la `l10n_ro_expense_currency/index.md`)

- **Nume Tehnic:** `l10n_ro_expense_currency`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_expense_currency
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_expense_currency`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

## 1. Sumar

Modul pentru gestionarea avansurilor de trezorerie acordate angajaților în valută, cu justificarea decontului și recunoașterea diferențelor de curs valutar conform OMFP 1802/2014. Acoperă întregul flux: acordarea avansului (Dr 542 = Cr 5121), justificarea cu recunoașterea diferențelor de curs (665/765) și returul restului.

## 2. Funcționalități Cheie

- **Acordare avans** la cursul BNR din data acordării: `Dr 542 = Cr 5121`.
- **Justificare decont** la cursul zilei cu recunoașterea diferenței de curs: `Dr 6xx = Cr 542` plus `Dr 665 / Cr 765`.
- **Retur rest** la cursul avansului: `Dr 5121 = Cr 542`.
- **Configurare conturi** (542, 665, 765) și jurnal implicit în setările de localizare România.
- **Stări avans:** Schiță → Acordat → Justificat → Închis, cu trecere în Anulat (stornare automată a notelor generate) din orice stare.

## 3. Dependențe

- `account`
- `l10n_ro`
- `hr`

## 4. Componente Cheie

### Modele

- `l10n.ro.cash.advance`: modelul avansului de trezorerie valutar, cu state machine și notele contabile aferente acordării, justificării și returului.
- `res.config.settings`: extins cu configurarea conturilor 542/665/765 și a jurnalului implicit.

### Vizualizări / Date

- `views/l10n_ro_cash_advance_views.xml`: vizualizările avansului de trezorerie.
- `views/res_config_settings_views.xml`: opțiunile de configurare a conturilor și jurnalului.

### Acțiuni Automate / Acțiuni Server

*Nu au fost identificate acțiuni automate; notele contabile se generează la tranzițiile de stare.*

## 5. Conexiuni

- `[[l10n_ro_expense_allowance]]`
- `[[l10n_ro_currency_revaluation]]`
