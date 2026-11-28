# Romania - Partner Create by VAT Button (localizat la `l10n_ro_partner_create_by_vat_button/index.md`)

- **Nume Tehnic:** `l10n_ro_partner_create_by_vat_button`
- **Versiune:** `20.0.1.1.13`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_partner_create_by_vat_button
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_partner_create_by_vat_button`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modul **fără dezvoltare nouă**: pentru completarea partenerilor români din ANAF se recomandă [l10n_ro_partner_autocomplete](../l10n_ro_partner_autocomplete/index.md), care preia datele gratuit din CUI-ul scris în nume sau în Cod fiscal, are buton **Actualizează din ANAF** pe partener, nu depinde de `l10n_ro_partner_create_by_vat` (OCA) și nu poate fi instalat împreună cu acesta. Modulul de față primește doar corecții, până când bazele de date care îl folosesc trec pe noul modul. Adaugă un buton pe formularul partenerului pentru recitirea datelor de la ANAF și completează un partener nou din CUI-ul scris în nume.

#### 2. Funcționalități Cheie

- Buton pe formularul partenerului pentru recitirea datelor de la ANAF (sau de la VIES, pentru un partener dintr-o altă țară UE).
- Completarea unui partener nou pe baza CUI-ului scris în câmpul de nume.

#### 3. Dependențe

- [l10n_ro_config](../l10n_ro_config/index.md)
- [l10n_ro_partner_create_by_vat](../l10n_ro_partner_create_by_vat/index.md)

#### 4. Componente Cheie

*Secțiune omisă: `readme/DESCRIPTION.md` acoperă scopul modulului și nu solicită analiza componentelor tehnice.*

#### 5. Conexiuni

- [l10n_ro_partner_autocomplete](../l10n_ro_partner_autocomplete/index.md): înlocuitorul recomandat (gratuit, din ANAF); nu poate fi instalat împreună cu acest modul.
- [l10n_ro_partner_create_by_vat](../l10n_ro_partner_create_by_vat/index.md): modulul de bază care implementează crearea partenerului după CUI; acest modul adaugă butonul de recitire.
