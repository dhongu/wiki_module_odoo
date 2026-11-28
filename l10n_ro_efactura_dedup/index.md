# Romania - Deduplicare facturi din SPV (localizat la `l10n_ro_efactura_dedup/index.md`)

- **Nume Tehnic:** `l10n_ro_efactura_dedup`
- **Versiune:** `20.0.1.0.6`
- **Cale:** `https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_efactura_dedup`
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_efactura_dedup`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Previne facturile duplicate la importul din SPV ANAF și la trimiterea facturilor emise. Odoo standard (`l10n_ro_edi`) folosește cheia (CUI furnizor, sumă totală, dată), care dă fals pozitive (două facturi diferite, aceeași zi și sumă) și fals negative (aceeași factură retrimisă sub alt index SPV). Modulul introduce o cheie extinsă SHA-256 din CUI, serie/număr, dată și sumă, care elimină ambele erori.

#### 2. Funcționalități Cheie

- **Cheie de deduplicare extinsă** `l10n_ro_edi_dedup_key` pe `account.move`: `SHA-256(CUI | serie/număr | dată | sumă totală)`, indexată, recalculată la orice schimbare. CUI-ul se compară normalizat (`RO20603502`, `20603502` și `RO 20603502` dau aceeași cheie); la facturile de achiziție se ia numărul furnizorului (câmpul Referință), la cele emise numărul propriu.
- **Deduplicare la import:** la sincronizarea inbox-ului SPV, mesajul cu cheie existentă este ignorat, factura existentă primește `l10n_ro_edi_is_duplicate = True` și o notă în chatter cu mesajul SPV ignorat.
- **Avertisment la trimitere:** dacă există deja o factură validată cu aceeași cheie, se afișează un avertisment; trimiterea poate fi forțată pentru corecții legitime.
- **Revizuire manuală:** banner portocaliu pe factura marcată, fila **Deduplicare SPV** cu cheia (readonly) și comutatorul **Duplicat SPV** (se dezactivează la un fals pozitiv), plus lista „Facturi posibil duplicate SPV”.
- Fără setări proprii: funcționează imediat după instalare, peste importul e-Factura din `l10n_ro_edi`.
- Bază legală: Cod Fiscal art. 319 alin. (7); CIUS-RO v1.0.1.

#### 3. Dependențe

- `l10n_ro_edi`

#### 4. Componente Cheie

**Modele**

- `account.move` (extindere): câmpurile `l10n_ro_edi_dedup_key` (Char, store, index) și `l10n_ro_edi_is_duplicate` (Boolean), calculul cheii (`_compute_l10n_ro_edi_dedup_key`), avertismentul la trimitere (`_l10n_ro_edi_get_pre_send_errors`) și deduplicarea la import (`_l10n_ro_edi_process_bill_messages`).

**Vizualizări**

- `view_move_form_l10n_ro_efactura_dedup`: bannerul de duplicat și fila Deduplicare SPV pe factură.
- `action_move_in_invoice_type_l10n_ro_dedup_filter`: acțiunea „Facturi posibil duplicate SPV”.

**Acțiuni Automate / Acțiuni Server**

- Niciuna proprie; deduplicarea la import rulează în sincronizarea standard a inbox-ului SPV din `l10n_ro_edi`.

#### 5. Conexiuni

- [l10n_ro_efactura_consumer](../l10n_ro_efactura_consumer/index.md): e-Factura B2C, același ecosistem `l10n_ro_edi`.
- [l10n_ro_etransport_block](../l10n_ro_etransport_block/index.md): blocarea documentelor e-Transport, alt modul de control peste fluxurile ANAF.
