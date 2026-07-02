

# `l10n_ro_account_return_pl_closing`

- **Nume Prietenesc:** România - Închidere P&L Cont Return (121)
- **Nume Tehnic:** `l10n_ro_account_return_pl_closing`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_account_return_pl_closing
- **Ultima Ingestie:** 2026-05-31
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

## 1. Sumar

Acest modul implementează fluxul de închidere lunară a conturilor de venituri (7xx) și cheltuieli (6xx) prin contul 121 (Profit și Pierdere), utilizând framework-ul standard Enterprise „Returns” (`account.return`) din `account_reports` în Odoo 19. Operațiunea este obligatorie conform reglementărilor contabile românești (OMFP 1802/2014).

## 2. Funcționalități Cheie

- **Închiderea Conturilor P&L:** Aduce soldurile conturilor 6xx și 7xx la zero și reflectă rezultatul perioadei în contul 121.
- **Automatizarea Notei Contabile:** Generează automat nota contabilă de închidere lunară.
- **Flux de Lucru Structurat:** Oferă un flux similar cu cel de închidere TVA, dar dedicat conturilor de Profit și Pierdere.
- **Ghid pentru Contabili:** Include instrucțiuni detaliate de utilizare, configurare inițială și flux lunar de lucru.
- **Gestionarea Erorilor:** Permite resetarea închiderilor și refacerea corecțiilor.
- **Întrebări Frecvente (FAQ):** Răspunde la întrebări comune despre funcționarea închiderii P&L.
- **Suport pentru Conturi Speciale:** Gestionează conturi precum 609, 709, 711 care pot avea sold pe ambele părți (prin `pl_bypass_account_ids`).
- **Comparație cu OCA:** Oferă o comparație detaliată cu modulul alternativ `l10n_ro_account_period_close` (OCA).
- **Considerații Tehnice Odoo 19:** Detaliază aspecte tehnice specifice versiunii 19, cum ar fi utilizarea `type_id` și `company_ids`.

## 3. Dependențe

- `account_reports`
- `account`
- `l10n_ro`
- `l10n_ro_reports`

## 4. Componente Cheie

### Modele Relevante (extinse/utilizate)

- `account.return.type`: Tipul de return (ex. „RO – Închidere P&L”). Extins cu câmpuri suplimentare (`pl_journal_id`, `pl_account_id`, `pl_bypass_account_ids`).
- `account.return`: Instanța concretă per perioadă/companie. Extins pentru a gestiona fluxul de închidere P&L.
- `account.move`: Extins prin câmpul standard `closing_return_id` pentru a lega nota contabilă de return.
- `pl_closing` (model Python): Conține logica principală de închidere a conturilor P&L, inclusiv calculul soldurilor și generarea notei contabile.

### Vizualizări / Date

- `data/account_return_pl_closing.xml`: Definește tipul de return „RO – Închidere venituri/cheltuieli (P&L)” și check-urile asociate.
- `views/account_return_type_views.xml`: Modifică vizualizările tipurilor de return pentru a adăuga câmpurile specifice modulului.
- `data/menu.xml`: Adaugă opțiunea de meniu pentru rularea închiderii P&L.

### Acțiuni Automate / Acțiuni Server

- **Check 2 – Profit/Pierdere estimat(ă):** O acțiune server care calculează și afișează soldul net.
- **Generarea notei contabile:** La apăsarea butonului `Validate` pe `account.return`, modulul suprascrie `action_validate()` pentru a apela `_generate_pl_closing_entries()`, care generează nota contabilă de închidere.

## 5. Conexiuni

- [[l10n_ro_account_chart/|l10n_ro_account_chart]]: Modulul de plan de conturi extins, fundamental pentru structura contabilă.
- [[l10n_ro_account_fisa_cont/|l10n_ro_account_fisa_cont]]: Modulul de raport „Fișă de Cont”, complementar pentru verificarea soldurilor.
- `account_reports`: Framework-ul standard Odoo Enterprise pentru rapoarte și return-uri, pe care se bazează acest modul.
- `l10n_ro_account_period_close` (OCA): Modul alternativ cu funcționalitate similară, dar arhitectură diferită, menționat pentru comparație.
