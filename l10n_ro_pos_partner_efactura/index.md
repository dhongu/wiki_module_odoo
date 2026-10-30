# Romania - POS Partner e-Factura Check

- **Nume Tehnic:** `l10n_ro_pos_partner_efactura`
- **Versiune:** `19.0.1.1.2`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_pos_partner_efactura
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_pos_partner_efactura`
- **Ultima Ingestie:** `2026-10-27`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

La casă, clientul care cere factură este creat în grabă de casier din ecranul POS, iar lipsa adresei sau a CUI-ului se descoperă abia la trimiterea facturii în SPV. Modulul mută controlul la momentul creării clientului: casierul găsește firma după CUI direct din ecranul *Alege clientul* (preluare de la ANAF), iar formularul de partener deschis din POS cere datele de care are nevoie o factură e-Factura (CIUS-RO); partenerul nu poate fi salvat până nu sunt complete. Bonul fiscal rămâne bon: alegerea unei firme nu bifează factura.

#### 2. Funcționalități Cheie

- Formularul de partener deschis din POS cere stradă, localitate, județ și țară; pentru firme cere și CUI-ul (Tax ID).
- Pentru județul București, localitatea trebuie să fie sectorul (`Sector 1` ... `Sector 6`); `București` este refuzat la salvare.
- La un client nou, țara se completează implicit cu țara companiei POS.
- **Client după CUI:** dacă în căutarea din *Alege clientul* se tastează un CUI (cu sau fără `RO`) și nu se găsește nimeni, apare butonul **Caută în ANAF**. Un client existent pe acel CUI este oferit chiar dacă nu e încărcat în POS; altfel firma este preluată de la ANAF și creată.
- După preluare, formularul de partener se deschide cu datele ANAF și o avertizare cu ce pare greșit: date lipsă, stradă fără număr, localitate care nu aparține județului. Clientul ajunge pe comandă doar după **Salvare**; dacă formularul se închide, clientul rămâne neconfirmat și la următoarea alegere din listă formularul se deschide din nou. Un client existent pe care e-Factura l-ar refuza este tratat ca unul nou.
- O firmă radiată la ANAF este refuzată; „ANAF nu răspunde" este deosebit de „firma nu există". Pentru firme inactive fiscal se lasă o notă în chatter.
- Cu modulul de autocompletare ANAF instalat, aceleași date sunt oferite și la tastarea CUI-ului în câmpul *Tax ID* din formularul clientului, ca în backoffice.
- Când ANAF nu răspunde, câmpurile rămân editabile și casierul le completează manual.
- Regulile se aplică doar formularului deschis din POS; partenerii creați din backoffice și persoanele de contact ale unei firme (adresa vine de la firmă) nu sunt verificate.
- CNP-ul nu se cere; clientul persoană fizică are nevoie doar de adresa completă.
- În România, alegerea unei firme drept client nu bifează „Factură": bonul fiscal încheie vânzarea, iar factura se emite doar la cerere.
- Modulul exclude `l10n_ro_pos_partner` (OCA, aceeași căutare după CUI la casă), ca să nu existe două butoane ANAF.
- Nu există setări proprii: modulul este activ pe toate punctele de vânzare după instalare. Fluxul pas-cu-pas este în fișa consultantului.

#### 3. Dependențe

- `point_of_sale`
- `l10n_ro_edi`
- [l10n_ro_anaf_partner_lookup](../l10n_ro_anaf_partner_lookup/index.md)

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins):
  - câmpuri: `l10n_ro_pos_anaf_to_confirm` (clientul preluat de la ANAF, încă neconfirmat de casier; încărcat în POS) și `l10n_ro_pos_anaf_warnings` (text calculat cu avertizările afișate în formular);
  - constrângerea `_check_pos_efactura_data` (activă doar cu cheia de context `pos_efactura_check`) și metoda `_get_pos_efactura_missing_data`, care întoarce problemele de date e-Factura (stradă, localitate, județ, țară, CUI la firme, sector la București), refolosind `SECTOR_RO_CODES` și `get_formatted_sector_ro` din `l10n_ro_edi`;
  - `_get_l10n_ro_anaf_address_warnings`: stradă fără număr, localitate care nu e în județ (comparație normalizată cu `res.city`);
  - `l10n_ro_pos_partner_from_cui` (apelat din POS): validează CUI-ul, caută clientul existent sau îl creează prin `l10n.ro.anaf.partner.lookup` (`_l10n_ro_pos_partner_from_anaf`), refuză firmele radiate;
  - `l10n_ro_pos_anaf_confirm`: verifică datele și scoate marcajul „de confirmat" după salvarea formularului.

**Vizualizări**

- `view_partner_form_pos_efactura`: moștenește `base.view_partner_form` și marchează câmpurile de adresă și CUI ca obligatorii doar când contextul conține `pos_efactura_check` (și partenerul nu are părinte).
- `view_partner_form_pos_efactura_anaf`: banner de avertizare „Date preluate de la ANAF" cu lista de avertismente, vizibil doar în formularul din POS pentru clienți neconfirmați.
- `static/src/app/services/pos_store.esm.js`: patch pe `PosStore.editPartnerContext` care adaugă `pos_efactura_check` și țara implicită a companiei.
- `static/src/app/screens/partner_list/` (`.esm.js` + `.xml`): patch pe `PartnerList` — butonul **Caută în ANAF**, apelul `l10n_ro_pos_partner_from_cui`, deschiderea formularului și confirmarea înainte de alegerea clientului.
- `static/src/app/models/pos_order.esm.js`: patch pe `PosOrder.setPartner` care nu bifează factura la alegerea clientului când țara companiei este România.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [l10n_ro_anaf_partner_lookup](../l10n_ro_anaf_partner_lookup/index.md): furnizează `l10n.ro.anaf.partner.lookup` (normalizare și validare CUI, căutare la ANAF, stări găsit / indisponibil / radiat / inactiv).
- `l10n_ro_edi`: regulile CIUS-RO (sectoarele Bucureștiului) pentru e-Factura în SPV.
- `l10n_ro_pos_partner` (OCA): exclus (`excludes`), aceeași căutare după CUI la casă; nu se instalează împreună.
- [l10n_ro_doc_screenshots](../l10n_ro_doc_screenshots/index.md): mixinul `ScreenshotCase` folosit de testul care generează capturile fișei (import defensiv; testul folosește opțional și `l10n_ro_partner_create_by_vat`).
