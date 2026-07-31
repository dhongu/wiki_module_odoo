# Romania - e-Factura Deduplicare SPV (localizat la `l10n_ro_efactura_dedup/index.md`)

- **Nume Tehnic:** `l10n_ro_efactura_dedup`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_efactura_dedup
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_efactura_dedup`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

## 1. Sumar

Modul de prevenire a duplicatelor la trimiterea și importul facturilor prin SPV ANAF. Odoo standard (`l10n_ro_edi`) folosește o cheie de deduplicare simplă (CUI furnizor + sumă totală + dată), care poate genera false positive și false negative. Acest modul introduce o cheie extinsă bazată pe SHA-256 din CUI, serie/număr factură, dată și valoare, eliminând astfel ambele tipuri de erori.

## 2. Funcționalități Cheie

- **Cheie de deduplicare extinsă:** câmpul `l10n_ro_edi_dedup_key` pe `account.move`, calculat automat ca `SHA-256(CUI | serie/nr | dată | sumă)`, indexat în baza de date și recalculat la orice schimbare.
- **Avertisment la trimitere (outbound):** verifică existența unei facturi validate cu aceeași cheie și permite forțarea trimiterii pentru corecții legitime.
- **Deduplicare la import (inbound):** la sincronizarea inbox-ului SPV, mesajele duplicat sunt ignorate, factura existentă primește flag `l10n_ro_edi_is_duplicate = True` și notificare în chatter.
- **Vizualizare:** banner portocaliu pe factura marcată ca duplicat, câmpul cheie readonly și acțiunea „Facturi posibil duplicate SPV" pentru revizuire manuală.

## 3. Dependențe

- `l10n_ro_edi`

## 4. Componente Cheie

### Modele

- `account.move`: extins cu câmpurile `l10n_ro_edi_dedup_key` (Char, store, index) și `l10n_ro_edi_is_duplicate` (Boolean), plus logica de avertizare la trimitere și deduplicare la import (`_l10n_ro_edi_process_bill_messages`).

### Vizualizări / Date

- `views/account_move_views.xml`: bannerul de duplicat, câmpul cheie readonly și acțiunea de revizuire a posibilelor duplicate.

### Acțiuni Automate / Acțiuni Server

*Deduplicarea la import se realizează în cadrul sincronizării standard a inbox-ului SPV din `l10n_ro_edi`.*

## 5. Conexiuni

- `[[l10n_ro_efactura_b2c]]`
- `[[l10n_ro_etransport_block]]`
