# Romania - Accounting Document Type

- **Nume Tehnic:** `l10n_ro_account_move_document_type`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_account_move_document_type
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_account_move_document_type`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaugă pe notele contabile **tipul documentului justificativ**, astfel încât registrele și jurnalele românești să arate ce document stă la baza fiecărei înregistrări: factură, notă de credit, factură de la furnizor, declarație vamală de import (DVI), chitanță, dispoziție de plată, extras de cont, stat de plată, decont de cheltuieli sau notă contabilă simplă.

#### 2. Funcționalități Cheie

- Facturile și chitanțele primesc tipul automat, după felul documentului.
- Liniile de extras bancar au tipul *Extras de cont*; o plată într-un jurnal bancar este *Ordin de plată / Document bancar* (se contabilizează pe contul de decontare, înainte de extras, uneori fără reconciliere). În jurnalele de numerar ambele sunt *Document de casă*.
- Orice altă înregistrare este *Notă contabilă*, până când modulul care o creează stabilește altceva (nota DVI din `l10n_ro_customs_dvi`, încasările și plățile de casă din `l10n_ro_account_sequence`).
- Pe o notă contabilă, contabilul poate schimba tipul din formular (de exemplu, TVA de import înregistrat manual, justificat prin DVI), la **Contabilitate > Contabilitate > Note contabile**.
- Coloana opțională *Tip document* și gruparea după tip în lista notelor contabile.
- Jurnalul de TVA la cumpărări și vânzări din [l10n_ro_account_vat_journal](../l10n_ro_account_vat_journal/index.md) folosește tipul pentru coloana *Tip document*.
- Fluxul pas cu pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.move` (extins): câmpul `l10n_ro_document_type` și calculul lui implicit.

**Vizualizări**

- `view_move_form`, `view_move_tree`, `view_account_move_filter`: câmpul pe formular, coloana opțională în listă și gruparea în căutare.

**Acțiuni Automate / Acțiuni Server**

- Nu are. Un `pre_init_hook` pregătește câmpul la instalare.

#### 5. Conexiuni

- [l10n_ro_account_vat_journal](../l10n_ro_account_vat_journal/index.md): folosește tipul în coloana *Tip document*.
- [l10n_ro_customs_dvi](../l10n_ro_customs_dvi/index.md): nota DVI primește tipul *Import (DVI)*.
- [l10n_ro_account_sequence](../l10n_ro_account_sequence/index.md): încasările și plățile de casă își stabilesc tipul.
