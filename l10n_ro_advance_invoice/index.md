

# `l10n_ro_advance_invoice`

- **Nume Prietenesc:** Romania - Avansuri Clienți/Furnizori cu TVA (419/4091/4092)
- **Nume Tehnic:** `l10n_ro_advance_invoice`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_advance_invoice
- **Ultima Ingestie:** 2026-05-31
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

## 1. Sumar

Acest modul gestionează facturile de avans cu TVA conform **Art. 282 alin. 2 Cod Fiscal** (faptul generator = data încasării) și realizează regularizarea automată a acestora la emiterea facturii finale. Simplifică procesul contabil pentru avansuri și asigură conformitatea cu declarațiile D300 și D394.

## 2. Funcționalități Cheie

- **Facturi de avans clienți:** Marcarea facturilor de avans client (`out_invoice`, cont 419) cu `l10n_ro_is_advance=True` pentru identificare în D394 (`TipDoc=5`).
- **Facturi de avans furnizori:** Flux simetric pentru facturile de avans furnizor (`in_invoice`, cont 4091).
- **Regularizare automată:** La factura finală, se generează automat linii negative pe conturile 419 și 4427 pentru regularizare (fără `is_storno`, fiind o operațiune normală).
- **D300:** TVA-ul avansului este inclus în rândurile standard D300 (Rd.9/10/11) prin taxele standard `l10n_ro`.
- **D394:** Câmpul `l10n_ro_is_advance` semnalează `TipDoc=5` generatorului D394.
- **Raport avansuri neregularizate:** Generează un raport cu avansurile clienți/furnizori neregularizate (sold 419/4091 deschis), filtrabil per partener/dată.

## 3. Dependențe

- `account`
- `l10n_ro`

## 4. Componente Cheie

### Modele

- `account.move`: Extinde modelul de note contabile pentru a introduce logica de gestionare a avansurilor (câmpuri și metode pentru marcare și regularizare).
- `l10n_ro_advance_wizard`: Un wizard dedicat pentru gestionarea avansurilor (conform fișierelor XML).

### Vizualizări / Date

- `security/ir.model.access.csv`: Definește drepturile de acces pentru noile modele/câmpuri.
- `wizard/l10n_ro_advance_wizard_views.xml`: Definește interfața wizard-ului pentru avansuri.
- `views/account_move_views.xml`: Modifică vizualizările notelor contabile pentru a integra funcționalitățile de avans.
- `views/l10n_ro_advance_report_views.xml`: Definește vizualizările pentru raportul de avansuri neregularizate.

### Acțiuni Automate / Acțiuni Server

- `_l10n_ro_create_advance_invoice()`: Metodă pentru crearea facturii de avans cu TVA, apelată dintr-un wizard sau direct.
- `_l10n_ro_apply_advances()`: Metodă pe `account.move` pentru aplicarea avansurilor selectate pe factura finală, generând linii de stornare TVA și regularizare sold 419.
- `action_open_unregularized_advances_report()`: Acțiune pentru deschiderea raportului cu avansurile clienți/furnizori neregularizate.

## 5. Conexiuni

- `l10n_ro_anaf_base`: Modulul de bază pentru declarații ANAF, care utilizează câmpul `l10n_ro_is_advance` pentru a genera `TipDoc=5` în D394.
- Alte module de localizare românească pentru declarații ANAF (ex. D300, D394).
