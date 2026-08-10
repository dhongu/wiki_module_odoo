# Product Valuation Check Report (localizat la `deltatech_valuation_report/index.md`)

- **Nume Tehnic:** `deltatech_valuation_report`
- **Versiune:** `19.0.0.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_valuation_report
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_valuation_report`
- **Ultima Ingestie:** `2026-07-31`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă un raport de tip Enterprise (în cadrul framework-ului `account_reports`) care verifică, pentru fiecare cont de evaluare a stocului, dacă valoarea calculată prin evaluarea produselor (`deltatech_stock_valuation`) coincide cu soldul contabil al contului respectiv. Diferența dintre cele două — cauzată de obicei de înregistrări contabile pe conturile de stoc fără produs atașat — este afișată explicit și poate fi investigată printr-un clic direct pe liniile contabile responsabile, ajutând echipa contabilă să identifice rapid și să corecteze abaterile de evaluare a stocului.

#### 2. Funcționalități Cheie

- Raport dedicat „Stock Valuation vs Balance Check", accesibil din meniul de rapoarte financiare (Contabilitate → Raportare).
- Compară, per cont de evaluare a stocului, soldul contabil complet cu totalul liniilor care poartă un produs (adică exact ce agregă evaluarea produsului).
- Afișează diferența drept sumă a liniilor contabile fără produs asociat pe conturile de stoc — acestea nu pot fi alocate niciunei evaluări de produs.
- Acțiune de tip „caret" pe fiecare linie de cont, care deschide direct lista liniilor contabile fără produs, pentru audit și corecție rapidă (asignare produs sau mutare pe un cont fără evaluare).
- Suportă filtrare pe interval de dată și selecție multi-companie, conform standardului framework-ului `account_reports`.

#### 3. Dependențe

- `account_reports`
- [deltatech_stock_valuation](../deltatech_stock_valuation/index.md)

#### 4. Componente Cheie

**Modele**

- `valuation.check.report.handler` (model abstract, moștenește `account.report.custom.handler`): implementează motorul custom al raportului — calculează prin SQL, pentru fiecare cont marcat `is_for_stock_valuation`, soldul contabil, valoarea liniilor cu produs și diferența liniilor fără produs; oferă și acțiunea „caret" care deschide liniile fără produs pentru auditare.

**Vizualizări**

- `valuation_check_report` (`account.report`): definește raportul cu trei coloane monetare — Sold Cont (`balance`), Evaluare — linii cu produs (`valuation`) și Diferență — linii fără produs (`difference`) — grupate pe cont contabil (`account_id`).
- `action_valuation_check_report` (`ir.actions.client`, tag `account_report`): acțiunea client care deschide raportul.

**Acțiuni Automate / Acțiuni Server**

- Nu există `ir.cron`, `base.automation` sau `ir.actions.server` definite în acest modul.
- `menu_valuation_check_report`: intrare de meniu sub „Contabilitate → Raportare" care lansează acțiunea raportului (nu este o acțiune automată, ci un simplu punct de navigare).

#### 5. Conexiuni

- [deltatech_stock_valuation](../deltatech_stock_valuation/index.md): furnizează logica de evaluare a stocului pe produs, față de care acest raport validează soldul contabil.
- `account_reports`: framework-ul Enterprise de raportare contabilă (motor custom, coloane, filtre) pe care se construiește acest raport.
