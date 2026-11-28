# Romania - Taxare inversă art. 331 (localizat la `l10n_ro_reverse_charge_331/index.md`)

- **Nume Tehnic:** `l10n_ro_reverse_charge_331`
- **Versiune:** `20.0.1.2.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_reverse_charge_331
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_reverse_charge_331`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul aplică automat taxarea inversă internă conform **art. 331 din Codul fiscal** (Legea 227/2015), dar numai când legea o permite: atât furnizorul, cât și cumpărătorul trebuie să fie înregistrați în scopuri de TVA conform art. 316. Odoo nu poate exprima singur această condiție, fiindcă poziția fiscală a regimului național se atribuie oricărui partener românesc, plătitor sau nu. Modulul adaugă taxele dedicate, bifele de configurare și gărzile care împiedică taxarea inversă pe un beneficiar sau un furnizor neînregistrat, atât la vânzare, cât și la achiziție.

#### 2. Funcționalități Cheie

- Taxa de vânzare **0% R331**, raportată pe rândul 13 din D300 („livrări supuse măsurilor de simplificare"), cu mențiunea legală cerută de art. 331 alin. (3) pe factură.
- Partea de e-Factura (CIUS-RO): categoria `AE`, codul `VATEX-EU-AE` și mențiunea „Taxare inversă" în română în motivul scutirii (BT-120), completat în câmpul standard *Tax Exemption Reason* al taxei; un text personalizat de acolo are prioritate.
- Bifa **Taxare inversă art. 331** pe taxele domestice de vânzare și de achiziție: bifarea ei este toată configurarea, iar maparea de înlocuire (taxa originală plus poziția fiscală) o scrie modulul; debifarea o desface.
- Bifa **Taxare inversă art. 331** pe poziția fiscală a plătitorilor de TVA (se alege manual, nu se ghicește din poziția implicită a bazei).
- Garda de înregistrare: înlocuirea se sare pentru un client sau furnizor care nu e înregistrat în scopuri de TVA (după **Plătitor TVA (scpTVA)** dacă există, altfel după prefixul `RO` al CUI), pe oferte, comenzi și facturi.
- Blocare la postare a oricărei facturi care poartă taxa art. 331 pentru o parte neînregistrată (poziție atribuită manual, taxă aleasă direct pe linie, document importat).
- Partea de achiziție: taxa **21% R331** cu autolichidare (`Dr 4426 = Cr 4427`, rândurile 12.1 și 26.1 din D300), aceeași bifă, aceeași gardă și același blocaj pe facturile de furnizor. Taxa de achiziție bifată trebuie să aibă cota de 21%; un furnizor neînregistrat se tratează fără TVA, cu baza pe rândul 29.
- Documentele existente nu se rescriu: ofertele și facturile în ciornă își păstrează taxa până la schimbarea clientului sau a poziției fiscale.
- Pasul-cu-pas, verificarea în D300 și cazurile speciale (note de credit, facturi e-Factura din SPV, furnizor cu cod de TVA anulat) sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `account_edi_ubl_cii`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.tax`: câmpurile `l10n_ro_reverse_charge_331` (bifă pe taxa domestică sursă, de vânzare sau de achiziție) și `l10n_ro_is_reverse_charge_331` (marcaj tehnic pe taxa de destinație, **0% R331** sau **21% R331**); ține maparea sincronizată cu bifele, refuză o sursă nedomestică, o cotă de achiziție diferită de cea a autolichidării și o dublă înlocuire a aceleiași surse pe aceeași poziție fiscală.
- `account.fiscal.position`: câmpul `l10n_ro_reverse_charge_331`; suprascrie `map_tax` pentru a anula înlocuirea când partenerul nu e înregistrat în scopuri de TVA (statutul vine din context, fiindcă `map_tax` nu primește partenerul).
- `account.move.line`: suprascrie `_get_computed_taxes` și propagă în context statutul de TVA al partenerului relevant.
- `account.move`: `_l10n_ro_check_reverse_charge_331`, apelat din `_post`, blochează postarea cu taxă art. 331 către o parte neînregistrată.
- `res.partner`: `_l10n_ro_is_vat_registered`, sursa unică a statutului de TVA.
- `account.chart.template`: creează pe planul RO taxele **0% R331** și **21% R331**.
- `account.edi.common` și `account.edi.ubl_cen_en16931`: setează categoria `AE` și mențiunea de taxare inversă în XML-ul e-Facturii.

**Vizualizări**

- `view_tax_form` / `view_tax_tree` (moștenite din `account`): bifa pe taxă, vizibilă doar pentru taxe de vânzare sau de achiziție domestice RO.
- `view_account_position_form` (moștenit din `account`): bifa pe poziția fiscală, cu un mesaj care explică ambele sensuri (vânzare → **0% R331**, achiziție → **21% R331**).

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: la instalare creează sau adoptă taxele **0% R331** și **21% R331** pe companiile RO cu plan de conturi deja încărcat, copiind etichetele de raportare și repartiția de pe taxele native, și completează motivul scutirii din e-Factura.

#### 5. Conexiuni

- [l10n_ro_reverse_charge_331_sale](../l10n_ro_reverse_charge_331_sale/index.md): garda art. 331 pe ofertele și comenzile de vânzare (punte `auto_install`).
- [l10n_ro_reverse_charge_331_purchase](../l10n_ro_reverse_charge_331_purchase/index.md): aceeași gardă pe cererile de ofertă și comenzile de achiziție.
- [l10n_ro_reverse_charge_331_pos](../l10n_ro_reverse_charge_331_pos/index.md): aceeași gardă în Punctul de vânzare.
- [l10n_ro_config](../l10n_ro_config/index.md): sursa câmpului `l10n_ro_vat_subjected` citit de gardă, dacă e instalat.
- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md): alternativă pentru `l10n_ro_vat_subjected`, sincronizat din registrul ANAF.
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): declarația D300 în care apar rândurile 12.1, 13, 26.1 și 29.
