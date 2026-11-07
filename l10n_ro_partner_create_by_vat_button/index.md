# Romania - Partner Create by VAT Button (localizat la `l10n_ro_partner_create_by_vat_button/index.md`)

- **Nume Tehnic:** `l10n_ro_partner_create_by_vat_button`
- **Versiune:** `19.0.1.1.13`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_partner_create_by_vat_button
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_partner_create_by_vat_button`
- **Ultima Ingestie:** `2026-11-07`

#### 1. Sumar

Acest modul adaugă un buton în ecranul partenerului care permite recitirea (reîncărcarea) datelor de la ANAF pe baza codului de TVA și completează un partener nou din CUI-ul scris în denumire. Astfel, utilizatorii pot actualiza manual informațiile unui partener (de exemplu denumire, adresă, status TVA), fără a fi nevoiți să recreeze fișa partenerului. **Modulul nu mai este dezvoltat**: primește doar corecturi, până când bazele de date care îl folosesc trec pe [l10n_ro_partner_autocomplete](../l10n_ro_partner_autocomplete/index.md).

#### 2. Funcționalități Cheie

- Buton în formularul partenerului pentru recitirea datelor de la ANAF pe baza codului de TVA; pentru un partener dintr-o altă țară UE datele se citesc de la VIES.
- Completarea unui partener nou pe baza CUI-ului scris în denumire.
- **Modul în curs de înlocuire:** [l10n_ro_partner_autocomplete](../l10n_ro_partner_autocomplete/index.md) completează partenerul din ANAF gratuit, din CUI-ul scris în denumire sau în Tax ID, și are butonul „Update from ANAF" pe partener. Nu depinde de modulul OCA `l10n_ro_partner_create_by_vat`, de care are nevoie acest modul, și nu poate fi instalat împreună cu el.

#### 3. Dependențe

- `l10n_ro_config`
- `l10n_ro_partner_create_by_vat`

#### 4. Componente Cheie

Fișierul `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie, dar nu detaliază componentele tehnice (modele, vizualizări, acțiuni). Conform schemei wiki, analiza codului pentru această secțiune a fost omisă.

#### 5. Conexiuni

- [l10n_ro_partner_autocomplete](../l10n_ro_partner_autocomplete/index.md): modulul recomandat în loc de acesta pentru completarea partenerului din ANAF; cele două nu pot fi instalate împreună.
- [l10n_ro_partner_create_by_vat_openapi](../l10n_ro_partner_create_by_vat_openapi/index.md): sursă alternativă de date (OpenAPI), construită peste acest modul.
- `l10n_ro_partner_create_by_vat`: modulul de bază care implementează crearea partenerului pe baza codului de TVA prin preluarea datelor de la ANAF; acest modul extinde funcționalitatea cu un buton de recitire.
