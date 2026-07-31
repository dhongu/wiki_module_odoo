# Romania - e-Factura B2C (Persoane Fizice) (localizat la `l10n_ro_efactura_b2c/index.md`)

- **Nume Tehnic:** `l10n_ro_efactura_b2c`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_efactura_b2c
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_efactura_b2c`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

## 1. Sumar

Extinde modulul `l10n_ro_edi` pentru a suporta transmiterea facturilor către persoane fizice (B2C) prin SPV (Spațiul Privat Virtual) conform CIUS-RO. Adaugă câmpul CNP pe partener cu validare automată, înlocuiește VAT-ul implicit din XML cu CNP-ul real și blochează trimiterea facturilor cu CNP invalid, asigurând conformitatea declarațiilor B2C.

## 2. Funcționalități Cheie

- **Câmp CNP pe partener:** vizibil pentru persoane fizice din România, cu validare automată prin algoritmul Luhn RO (13 cifre) și câmp calculat „CNP Valid".
- **Generare XML CIUS-RO B2C:** când clientul este persoană fizică cu CNP valid, generatorul înlocuiește `DEFAULT_VAT = '0000000000000'` cu CNP-ul real, cu `schemeID="CNP"`.
- **Validare pre-trimitere:** blochează trimiterea în SPV dacă CNP-ul este completat dar invalid.
- **Avertizare pe factură:** afișează avertisment când clientul este persoană fizică română fără CNP valid.
- **Migrare date:** la instalare, dacă `deltatech_contact` este prezent, copiază CNP-urile existente în `l10n_ro_cnp`.
- **Protecție GDPR:** câmpul CNP este restricționat la grupul `base.group_user` (utilizatori interni).

## 3. Dependențe

- `l10n_ro_edi`

## 4. Componente Cheie

### Modele

- `res.partner`: extins cu câmpul `l10n_ro_cnp` și câmpul calculat „CNP Valid" (validare Luhn RO).
- `account.move`: extins cu validarea pre-trimitere și avertizarea pentru persoane fizice fără CNP valid, plus generarea XML CIUS-RO B2C.

### Vizualizări / Date

- `views/res_partner_views.xml`: câmpul CNP și indicatorul de validitate pe partener.
- `views/account_move_views.xml`: avertizarea pe formularul facturii.

### Acțiuni Automate / Acțiuni Server

- `post_init_hook`: migrarea CNP-urilor existente din `deltatech_contact` (dacă modulul este prezent).

## 5. Conexiuni

- `[[l10n_ro_efactura_dedup]]`
- `[[l10n_ro_etransport_block]]`
