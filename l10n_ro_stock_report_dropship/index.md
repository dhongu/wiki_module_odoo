# Romania - Fișa de magazie cu Dropship

- **Nume Tehnic:** `l10n_ro_stock_report_dropship`
- **Versiune:** `19.0.1.1.2`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_stock_report_dropship
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_stock_report_dropship`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modul tehnic care completează raportul „Fișa de magazie” din localizarea română cu livrările directe de la furnizor la client (dropshipping). Aceste mișcări nu trec prin nicio locație internă, deci raportul standard nu le vede; cu acest modul ele apar ca rânduri de tip „Dropship”, alături de intrările și ieșirile obișnuite, sub contul de marfă pe care este evaluată mișcarea (de regulă 371000). Nu are meniuri sau setări proprii.

#### 2. Funcționalități Cheie

- Recunoaște ca dropship mișcările efectuate (`done`) între furnizor și client (sau tranzit fără companie), precum și returul lor (client către furnizor).
- Produsele cu mișcări dropship în perioadă sunt incluse în raport chiar dacă nu au nicio mișcare prin locații interne.
- Fiecare mișcare dropship este raportată atât pe intrare, cât și pe ieșire, cu aceeași valoare pozitivă, astfel încât efectul asupra stocului este zero. Este exclusă intenționat din stocul inițial și final, care iau în calcul doar locațiile interne.
- Rândurile apar sub contul contabil al mișcării (ex. 371000), nu într-o grupă „fără cont” (corecție din 19.0.1.1.0).
- Valoarea se recalculează la generarea raportului din valoarea mișcării de stoc, deoarece în Odoo 19 mișcările dropship nu au valoarea stocată și nu generează note contabile.
- Utilizare: se generează fișa de magazie ca de obicei (Inventar > Raportare); rândurile dropship apar automat, cu tipul de evaluare „Dropship”.

#### 3. Dependențe

- [l10n_ro_stock_report](../l10n_ro_stock_report/index.md)
- `l10n_ro_stock_account`
- `stock_dropshipping`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.stock.storage.sheet` (extins, tranzient): adaugă produsele cu mișcări dropship în lista celor raportate, inserează rândurile dropship pe laturile de intrare și ieșire și recalculează sumele din `stock.move._get_value()`.
- `l10n.ro.stock.storage.sheet.line` (extins, tranzient): adaugă valoarea `dropship` în câmpul `valued_type`.

**Vizualizări**

- Modulul nu definește vizualizări.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [l10n_ro_stock_report](../l10n_ro_stock_report/index.md): raportul de bază extins (și dependență directă).
- `l10n_ro_stock_account`: evaluarea stocului și contul `l10n_ro_account_id` de pe mișcare.
