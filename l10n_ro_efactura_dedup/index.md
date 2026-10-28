# Romania - Deduplicare facturi din SPV (localizat la `l10n_ro_efactura_dedup/index.md`)

- **Nume Tehnic:** `l10n_ro_efactura_dedup`
- **Versiune:** `19.0.1.0.6`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_efactura_dedup
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_efactura_dedup`
- **Ultima Ingestie:** `2026-10-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul previne duplicatele la importul și la trimiterea facturilor prin SPV ANAF. Odoo standard (`l10n_ro_edi`) folosește o cheie simplă (CUI furnizor, sumă totală, dată), care poate rata duplicate sau poate confunda două facturi diferite. Modulul înlocuiește cheia cu una extinsă, un SHA-256 din CUI, numărul facturii, dată și sumă, astfel încât același document să fie recunoscut chiar dacă reapare în SPV, iar facturile diferite să nu se confunde.

#### 2. Funcționalități Cheie

- **Cheie de deduplicare extinsă:** câmpul `l10n_ro_edi_dedup_key` pe factură, calculat automat ca SHA-256 din CUI-ul partenerului, numărul facturii, dată și suma totală, indexat în baza de date. CUI-ul se compară normalizat: `RO20603502`, `20603502` și `RO 20603502` dau aceeași cheie.
- **Numărul din cheie:** la facturile și notele de credit de achiziție se folosește numărul furnizorului (câmpul *Referință*, BT-1 din XML), la documentele emise numărul propriu. Pe achiziții, înainte de versiunea `19.0.1.0.1`, se folosea secvența internă, iar deduplicarea nu prindea nimic.
- **Deduplicare la import (inbound):** la sincronizarea inbox-ului SPV, un mesaj cu o cheie deja existentă este ignorat, factura existentă este marcată **Duplicat SPV**, iar în chatter apare o notă despre mesajul ignorat.
- **Avertisment la trimitere (outbound):** dacă există deja o altă factură validată de SPV, din aceeași companie, cu aceeași cheie, trimiterea se oprește cu mesajul „Possible SPV duplicate”.
- **Revizuire manuală:** banner de avertizare pe factura marcată, fila **Deduplicare SPV** cu comutatorul de duplicat și cheia (readonly), și lista *Facturi posibil duplicate SPV*. Lista nu are intrare de meniu proprie. La un fals pozitiv, comutatorul se dezactivează manual.
- Fără setări proprii: deduplicarea funcționează imediat după instalare. Facturile create înainte de instalare nu sunt detectate retroactiv; cheia se calculează la modificarea numărului, referinței, datei, sumei sau CUI-ului partenerului.
- Bază legală: Cod Fiscal art. 319 alin. (7) (unicitatea facturii prin număr) și CIUS-RO v1.0.1.

#### 3. Dependențe

- `l10n_ro_edi`

#### 4. Componente Cheie

**Modele**

- `account.move` (extins): câmpurile `l10n_ro_edi_dedup_key` (Char, stocat, indexat, necopiabil) și `l10n_ro_edi_is_duplicate` (Boolean); calculul cheii; `_l10n_ro_edi_get_pre_send_errors` (avertisment la trimitere); `_l10n_ro_edi_process_bill_messages` (filtrarea duplicatelor la import și setarea cheii pe facturile noi); extragerea CUI-ului furnizorului din XML-ul UBL (`PartyTaxScheme/CompanyID`).

**Vizualizări**

- `view_move_form_l10n_ro_efactura_dedup`: extinde `account.view_move_form` cu bannerul de duplicat și fila *SPV Deduplication* (comutator și cheie readonly).
- `action_move_in_invoice_type_l10n_ro_dedup_filter`: acțiune de listă pentru facturile și notele de credit de furnizor marcate ca posibil duplicat SPV.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server. Deduplicarea la import rulează în cadrul sincronizării standard a inbox-ului SPV din `l10n_ro_edi`.

#### 5. Conexiuni

- [l10n_ro_efactura_consumer](../l10n_ro_efactura_consumer/index.md): fluxuri e-Factura pentru persoane fizice, menționat în fișa consultant ca modul conex.
- `account`: facturi furnizor și atașamente.
