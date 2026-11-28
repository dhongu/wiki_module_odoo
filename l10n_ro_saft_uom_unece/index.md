# Romania - Cod UN/ECE al unității de măsură în SAF-T (localizat la `l10n_ro_saft_uom_unece/index.md`)

- **Nume Tehnic:** `l10n_ro_saft_uom_unece`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_saft_uom_unece
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_saft_uom_unece`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

În exportul SAF-T (D406), fiecare unitate de măsură se declară cu un cod UN/ECE. Raportul standard ia codul dintr-o listă fixă și pune `C62` (bucată) pentru orice unitate creată de firmă, de exemplu „Cutie 13 kg” sau „Rolă”. Modulul face ca exportul să folosească codul ales pe fiecare unitate, din nomenclatorul ANAF adus de [deltatech_uom_unece](../deltatech_uom_unece/index.md), același cod folosit deja la e-Factura și e-Transport.

#### 2. Funcționalități Cheie

- Exportul D406 declară codul UN/ECE ales pe unitate în `UOMTable` (`UnitOfMeasure`), la produs (`UOMBase`, `UOMStandard`) și pe linia facturii (`InvoiceUOM`).
- Unitățile fără cod ales rămân cu maparea standard a raportului (`C62` pentru cele create de firmă).
- Codul se alege pe unitate în câmpul **Cod UNECE** (de exemplu `XBX` pentru cutie, `MTK` pentru metru pătrat), vizibil administratorilor. Lista unităților se deschide din **Contabilitate → Configurare → Setări**, blocul *Unități și ambalaje*, cu bifa *Unități de măsură și ambalaje*.
- Nu adaugă meniuri; declarația se generează ca înainte, din Carte Mare, meniul ⚙ **SAF-T (Declarația D406)**.
- Verificările pas cu pas sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `l10n_ro_saft`
- [deltatech_uom_unece](../deltatech_uom_unece/index.md)

#### 4. Componente Cheie

**Modele**

- `account.general.ledger.report.handler`: suprascrie `_l10n_ro_saft_fill_uom_values` ca să preia explicit `unece_code_id` de pe unitate.

**Vizualizări**

- Nu adaugă vizualizări; câmpul **Cod UNECE** vine din `deltatech_uom_unece`.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_ro_saft_export_fix](../l10n_ro_saft_export_fix/index.md): alte corecții ale exportului D406; funcționează independent.
- [l10n_ro_saft_validator](../l10n_ro_saft_validator/index.md): pre-validarea D406; funcționează independent.
