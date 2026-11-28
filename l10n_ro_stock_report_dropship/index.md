# Romania - Stock Storage Sheet Dropship

- **Nume Tehnic:** `l10n_ro_stock_report_dropship`
- **Versiune:** `20.0.1.1.3`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_stock_report_dropship
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_stock_report_dropship`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaugă mișcările dropship în fișa de magazie a stivei OCA de evaluare (`l10n_ro_stock_report` peste `l10n_ro_stock_account`). Un dropship merge de la furnizor direct la client, fără să intre în depozit, dar motorul OCA îl evaluează pe contul de mărfuri (de regulă 371); fișa trebuie deci să-l arate ca intrare și ieșire de aceeași cantitate și valoare.

#### 2. Funcționalități Cheie

- Mișcările dropship primesc tipul de evaluare *Dropship* și apar în liniile fișei, lângă recepții și livrări.
- În lista fișei (*Inventar → Rapoarte → Fișa de magazie*, **Arată fișa**) transferul apare ca un rând de intrare și unul de ieșire cu aceeași valoare.
- **Arată fișa PDF** tipărește rândurile pe contul de stoc al categoriei produsului (ex. 371000), iar după ele stocul revine la valoarea anterioară.
- Nu are meniu sau setări proprii; este un add-on tehnic.
- Se aplică doar fișei OCA `l10n_ro_stock_report`, nu și lui `l10n_ro_storage_sheet` (bazat pe evaluarea nativă Odoo). Fluxul complet este în fișa consultantului.

#### 3. Dependențe

- [l10n_ro_stock_report](../l10n_ro_stock_report/index.md)
- `l10n_ro_stock_account`
- `stock_dropshipping`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.stock.storage.sheet`: extins pentru includerea mișcărilor dropship.
- `l10n.ro.stock.storage.sheet.line`: extins cu tipul de evaluare *Dropship*.

**Vizualizări**

- Nu adaugă vizualizări; logica este în `report/stock_report.py`.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_ro_stock_report](../l10n_ro_stock_report/index.md): fișa de magazie pe care o extinde.
- `l10n_ro_stock_account`: motorul de evaluare care postează nota 607 = 371 a dropship-ului.
