# Romania - POS Partner e-Factura Check

- **Nume Tehnic:** `l10n_ro_pos_partner_efactura`
- **Versiune:** `19.0.1.1.2`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_pos_partner_efactura
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_pos_partner_efactura`
- **Ultima Ingestie:** `2026-10-22`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

La casă, clientul care cere factură este creat în grabă de casier din ecranul POS, iar lipsa adresei sau a CUI-ului se descoperă abia la trimiterea facturii în SPV. Modulul mută controlul la momentul creării clientului: formularul de partener deschis din POS cere datele de care are nevoie o factură e-Factura (CIUS-RO), iar partenerul nu poate fi salvat până nu sunt complete.

#### 2. Funcționalități Cheie

- Formularul de partener deschis din POS cere stradă, localitate, județ și țară; pentru firme cere și CUI-ul (Tax ID).
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

- `res.partner` (extins): constrângerea `_check_pos_efactura_data` (activă doar cu cheia de context `pos_efactura_check`) și metoda `_get_pos_efactura_missing_data`, care întoarce problemele de date e-Factura (stradă, localitate, județ, țară, CUI la firme, sector la București), refolosind `SECTOR_RO_CODES` și `get_formatted_sector_ro` din `l10n_ro_edi`.

**Vizualizări**

- `view_partner_form_pos_efactura`: moștenește `base.view_partner_form` și marchează câmpurile de adresă și CUI ca obligatorii doar când contextul conține `pos_efactura_check` (și partenerul nu are părinte).
- `static/src/app/services/pos_store.esm.js`: patch pe `PosStore.editPartnerContext` care adaugă `pos_efactura_check` și țara implicită a companiei.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [l10n_ro_doc_screenshots](../l10n_ro_doc_screenshots/index.md): mixinul `ScreenshotCase` folosit de testul care generează capturile fișei (import defensiv).
- `l10n_ro_partner_create_by_vat`: opțional, preia datele firmei de la ANAF după CUI.
