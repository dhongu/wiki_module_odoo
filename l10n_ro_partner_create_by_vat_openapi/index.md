# Partner Data from OpenAPI (localizat la `l10n_ro_partner_create_by_vat_openapi/index.md`)

- **Nume Tehnic:** `l10n_ro_partner_create_by_vat_openapi`
- **Versiune:** `20.0.1.0.7`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_partner_create_by_vat_openapi
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_partner_create_by_vat_openapi`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modul **fără dezvoltare nouă**: pentru o firmă din România se recomandă [l10n_ro_partner_autocomplete](../l10n_ro_partner_autocomplete/index.md), care completează partenerul din ANAF, gratuit și fără cheie OpenAPI, și nu depinde de `l10n_ro_partner_create_by_vat` (OCA). Acest modul primește doar corecții, până când bazele de date care îl folosesc trec pe noul modul. Adaugă în formularul de contact acțiunea „Get Partner Data OpenAPI", care completează datele partenerului pe baza CUI-ului, folosind cheia OpenAPI proprie.

#### 2. Funcționalități Cheie

- Adaugă acțiunea „Get Partner Data OpenAPI" în formularul de contact.
- CUI-ul (numărul de TVA) se introduce în câmpul de nume.
- La apăsarea butonului pornește o căutare cu cheia OpenAPI proprie.
- Completează informațiile preluate în câmpurile goale ale contactului.

#### 3. Dependențe

- [l10n_ro_config](../l10n_ro_config/index.md)
- [l10n_ro_partner_create_by_vat](../l10n_ro_partner_create_by_vat/index.md)
- [l10n_ro_partner_create_by_vat_button](../l10n_ro_partner_create_by_vat_button/index.md)

#### 4. Componente Cheie

*Secțiune omisă: `readme/DESCRIPTION.md` acoperă scopul modulului și nu solicită analiza componentelor tehnice.*

#### 5. Conexiuni

- [l10n_ro_partner_autocomplete](../l10n_ro_partner_autocomplete/index.md): înlocuitorul recomandat, fără cheie OpenAPI.
- [l10n_ro_partner_create_by_vat](../l10n_ro_partner_create_by_vat/index.md): modul de bază pentru crearea partenerului după CUI, extins cu sursa OpenAPI.
- [l10n_ro_partner_create_by_vat_button](../l10n_ro_partner_create_by_vat_button/index.md): furnizează butonul din formularul de contact.
