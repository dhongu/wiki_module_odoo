# Creare Partener după CUI din OpenAPI (localizat la `l10n_ro_partner_create_by_vat_openapi/index.md`)

- **Nume Tehnic:** `l10n_ro_partner_create_by_vat_openapi`
- **Versiune:** `19.0.1.0.2`
- **Cale:** `https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_partner_create_by_vat_openapi`
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_partner_create_by_vat_openapi`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Acest modul adaugă în formularul de contact acțiunea „Get Partner Data OpenAPI", care permite completarea automată a datelor unui partener pe baza codului de identificare fiscală (CUI). Utilizatorul introduce numărul de TVA în câmpul de nume, apasă butonul, iar modulul pornește o căutare folosind cheia OpenAPI și completează informațiile lipsă în câmpurile goale ale contactului. Astfel, crearea partenerilor români devine mai rapidă și mai puțin predispusă la erori de introducere manuală.

#### 2. Funcționalități Cheie

- Adaugă acțiunea „Get Partner Data OpenAPI" în formularul de contact.
- Permite introducerea numărului de TVA (CUI) direct în câmpul de nume.
- Pornește o căutare folosind cheia OpenAPI proprie la apăsarea butonului.
- Completează automat câmpurile goale ale contactului cu informațiile preluate.

#### 3. Dependențe

- `base_vat`
- `l10n_ro_config`
- `l10n_ro_partner_create_by_vat`
- `l10n_ro_partner_create_by_vat_button`

#### 4. Componente Cheie

Fișierul `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie, fără a solicita detalierea componentelor tehnice. Conform fluxului de ingestie, analiza codului pentru această secțiune a fost omisă.

#### 5. Conexiuni

- `l10n_ro_partner_create_by_vat`: modul de bază pentru crearea partenerului după CUI, extins de acest modul cu sursa de date OpenAPI.
- `l10n_ro_partner_create_by_vat_button`: furnizează butonul în formularul de contact pe care se sprijină această acțiune.
- `l10n_ro_config`: configurarea localizării României, unde se gestionează parametrii de localizare.
