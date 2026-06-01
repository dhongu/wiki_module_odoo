# Checklist Închidere Perioadă (localizat la `l10n_ro_period_close_enhanced/index.md`)

- **Nume Tehnic:** `l10n_ro_period_close_enhanced`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_period_close_enhanced
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_period_close_enhanced`
- **Ultima Ingestie:** 2026-06-01

#### 1. Sumar

Modulul implementează un checklist lunar de închidere a perioadei contabile, folosind infrastructura Enterprise `account.return.type` din `account_reports`. La fiecare închidere lunară, contabilul creează un checklist care parcurge automat sau manual o serie de verificări obligatorii conform OMFP 1802/2014 (facturi draft, extrase nereconciliate, coeficient K, CMP periodic, reevaluare valutară etc.), asigurând o închidere consistentă și auditabilă.

#### 2. Funcționalități Cheie

- Checklist de perioadă (tip audit) creat per lună pe baza cadrului Account Returns din Enterprise.
- Verificări automate evaluate prin model + domeniu: facturi/avize în Draft (`account.move`), linii de extras bancar nereconciliate (`account.bank.statement.line`).
- Verificări personalizate Python, active doar dacă modulul opțional corespunzător este instalat: coeficient K postat (`l10n_ro_stock_k_coefficient`), notă CMP periodic postată (`l10n_ro_stock_cmp_periodic`), reevaluare valutară postată (`l10n_ro_currency_revaluation`).
- Verificări manuale confirmate de contabil: sold registru de casă, inventar stocuri regularizat, reconciliere conturi clienți/furnizori.
- Flux de lucru: New → Refresh Checks → Review → Submit.
- Fără configurare specială; verificările opționale apar doar dacă modulul aferent este instalat.

#### 3. Dependențe

- `account_reports`
- `account`
- `[[l10n_ro]]`

#### 4. Componente Cheie

**Modele**

- Folosește și configurează `account.return.type` și `account.return` din Enterprise pentru a defini și evalua checklist-ul de închidere (inclusiv verificările Python condiționate).

**Vizualizări / Date**

- `data/period_close_return_type.xml`: Definește tipul de return audit și verificările aferente.
- `data/menu.xml`: Intrarea de meniu pentru checklist-ul de închidere.

**Acțiuni Automate / Acțiuni Server**

- Acțiunea Refresh Checks evaluează automat verificările cu model+domeniu și verificările Python condiționate.

#### 5. Conexiuni

- `[[l10n_ro_account_return_pl_closing]]`
- `[[l10n_ro_inventory_register]]`
- `[[l10n_ro_mrp_labour_account]]`
