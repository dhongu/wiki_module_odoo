# Romania - POS Partner e-Factura Check

- **Nume Tehnic:** `l10n_ro_pos_partner_efactura`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_pos_partner_efactura
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_pos_partner_efactura`
- **Ultima Ingestie:** `2026-10-22`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

La casă, clientul care cere factură este creat în grabă de casier din ecranul POS, iar lipsa adresei se descoperă abia la trimiterea facturii în SPV. Modulul mută controlul la momentul creării clientului: formularul de partener deschis din POS cere datele de care are nevoie o factură e-Factura (CIUS-RO), iar partenerul nu poate fi salvat până nu sunt complete.

#### 2. Funcționalități Cheie

- Formularul de partener deschis din POS cere stradă, localitate, județ și țară.
- CUI-ul nu se cere: pe Odoo 20, tipul partenerului nu se mai alege în formular, ci se deduce din CUI (`is_company` calculat de `l10n_ro_edi`). Un client cu CUI valid este firmă; unul fără CUI este persoană fizică și se facturează fără CUI.
- Pentru județul București, localitatea trebuie să fie sectorul (`Sector 1` ... `Sector 6`); `București` este refuzat la salvare.
- La un client nou, țara se completează implicit cu țara companiei POS.
- Datele firmei se preiau de la ANAF după CUI, dacă este instalat un modul de creare partener după CUI; când ANAF nu răspunde, câmpurile rămân editabile și casierul le completează manual.
- Regulile se aplică doar formularului deschis din POS; partenerii creați din backoffice și persoanele de contact ale unei firme (adresa vine de la firmă) nu sunt verificate.
- CNP-ul nu se cere; clientul persoană fizică are nevoie doar de adresa completă.
- Nu există setări proprii: modulul este activ pe toate punctele de vânzare după instalare. Fluxul pas-cu-pas este în fișa consultantului.

#### 3. Dependențe

- `point_of_sale`
- `l10n_ro_edi`

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins): constrângerea `_check_pos_efactura_data` (activă doar cu cheia de context `pos_efactura_check`, declanșată de adresă, `parent_id` și `type`) și metoda `_get_pos_efactura_missing_data`, care întoarce problemele de date e-Factura (stradă, localitate, județ, țară, sector la București), refolosind `SECTOR_RO_CODES` și `get_formatted_sector_ro` din `l10n_ro_edi`.

**Vizualizări**

- `view_partner_form_pos_efactura`: moștenește `point_of_sale.view_partner_form_pos_ui` (formularul propriu al POS pe Odoo 20) și marchează câmpurile de adresă ca obligatorii doar când contextul conține `pos_efactura_check` (și partenerul nu are părinte).
- `static/src/app/services/pos_store.esm.js`: patch pe `PosStore.editPartnerContext` care adaugă `pos_efactura_check` și țara implicită a companiei (aplicată de formular doar unui partener nou).

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [l10n_ro_doc_screenshots](../l10n_ro_doc_screenshots/index.md): mixinul `ScreenshotCase` folosit de testul care generează capturile fișei (import defensiv).
- [l10n_ro_partner_create_by_vat](../l10n_ro_partner_create_by_vat/index.md): opțional, preia datele firmei de la ANAF după CUI.
