# Romania - Partner Create by VAT Button (localizat la `l10n_ro_partner_create_by_vat_button/index.md`)

- **Nume Tehnic:** `l10n_ro_partner_create_by_vat_button`
- **Versiune:** `19.0.1.1.7`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_partner_create_by_vat_button
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_partner_create_by_vat_button`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Acest modul adaugă un buton în ecranul partenerului care permite recitirea (reîncărcarea) datelor de la ANAF pe baza codului de TVA. Astfel, utilizatorii pot actualiza manual informațiile unui partener (de exemplu denumire, adresă, status TVA) preluate din registrul ANAF, fără a fi nevoiți să recreeze fișa partenerului.

#### 2. Funcționalități Cheie

- Buton în formularul partenerului pentru recitirea datelor de la ANAF pe baza codului de TVA.

#### 3. Dependențe

- `l10n_ro_config`
- `l10n_ro_partner_create_by_vat`

#### 4. Componente Cheie

Fișierul `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie, dar nu detaliază componentele tehnice (modele, vizualizări, acțiuni). Conform schemei wiki, analiza codului pentru această secțiune a fost omisă.

#### 5. Conexiuni

- `l10n_ro_partner_create_by_vat`: modulul de bază care implementează crearea partenerului pe baza codului de TVA prin preluarea datelor de la ANAF; acest modul extinde funcționalitatea cu un buton de recitire.
