# Romania - Avansuri Clienți/Furnizori cu TVA (419/4091/4092) (localizat la `l10n_ro_advance_invoice/index.md`)

- **Nume Tehnic:** `l10n_ro_advance_invoice`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_advance_invoice
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_advance_invoice`
- **Ultima Ingestie:** `2026-08-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul pentru gestionarea facturilor de avans cu TVA conform **Art. 282 alin. 2 Cod Fiscal** (faptul generator = data încasării) și regularizarea automată la factura finală. Este adresat companiilor care încasează sau plătesc avansuri cu TVA înainte de livrarea bunurilor sau prestarea serviciilor.

#### 2. Funcționalități Cheie

- **Factură de avans client** (`out_invoice`, cont 419): marcată cu `l10n_ro_is_advance=True` pentru identificare în D394 (`TipDoc=5`).
- **Factură de avans furnizor** (`in_invoice`, cont 4091): flux simetric cu cel de client.
- **Regularizare automată** la factura finală: linii negative pe 419/4091 și 4427/4426 (fără `is_storno` — regularizarea este operațiune normală, nu corecție de eroare).
- **D300**: TVA-ul avansului merge în Rd.9/10/11 prin taxele standard `l10n_ro`; nu sunt necesare rânduri distincte.
- **D394**: câmpul `l10n_ro_is_advance` semnalează `TipDoc=5` generatorului D394.
- **Raport avansuri neregularizate**: sold 419/4091 deschis, filtrabil per partener/dată.
- **Banner vizual** pe factura de avans și tab „Avansuri" pe factura finală.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.move`: Extinde modelul de note contabile cu câmpul `l10n_ro_is_advance` (marcare factură de avans), câmpul de legătură către facturile finale/de avans asociate și metodele de creare/aplicare a avansurilor.

**Vizualizări**

- `account_move_views.xml`: adaugă banner-ul vizual pe factura de avans și fila „Avansuri" (selectare avansuri de regularizat, buton „Aplică avansuri selectate") pe factura finală.
- `l10n_ro_advance_wizard_views.xml`: formularul wizard-ului de emitere a facturii de avans (tip avans, partener, sumă netă, TVA, jurnal, dată, referință).
- `l10n_ro_advance_report_views.xml`: vizualizările raportului de avansuri neregularizate (listă filtrabilă per partener/dată/tip).

**Acțiuni Automate / Acțiuni Server**

- `_l10n_ro_create_advance_invoice()`: creează factura de avans cu TVA din wizard, marcată automat cu `l10n_ro_is_advance=True`.
- `_l10n_ro_apply_advances()`: aplică avansurile selectate pe factura finală, generând liniile negative de regularizare pe 419/4091 și 4427/4426.
- `action_open_unregularized_advances_report()`: deschide raportul cu avansurile clienți/furnizori neregularizate (postate, fără factură finală asociată).

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): generatorul D394 citește câmpul `l10n_ro_is_advance` pentru a raporta facturile de avans cu `TipDoc=5`.
