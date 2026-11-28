# Romania - Autocompletare parteneri din ANAF

- **Nume Tehnic:** `l10n_ro_partner_autocomplete`
- **Versiune:** `20.0.1.5.1`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_partner_autocomplete
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_partner_autocomplete`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Autocompletarea standard de parteneri din Odoo propune companii din IAP și consumă credite. Pentru o firmă românească sursa autoritativă este ANAF, gratuit. Cu acest modul, un CUI românesc tastat acolo unde Odoo oferă autocompletarea arată firma găsită la ANAF, iar alegerea ei completează partenerul. Un cod de TVA din alt stat UE se caută în VIES. Niciun credit IAP nu se consumă pentru un CUI românesc.

#### 2. Funcționalități Cheie

- Completare din ANAF: denumire, CUI (cu `RO` doar la plătitor de TVA), plătitor TVA, stradă cu număr, localitate, județ, cod poștal, nr. registrul comerțului, telefon; la București sectorul ca localitate (cerință e-Factura); notă în chatter cu sursa și data. Funcționează în câmpurile *CUI* / *Nume* ale partenerului, *Client* la ofertă și factură și formularul de client din POS.
- Firme din UE prin VIES: nume, stradă, cod poștal, oraș, țară, notă în chatter; dacă VIES nu răspunde sau țara ține numele secret (Germania, Spania), se întreabă IAP. Pentru un plătitor român nota arată și dacă firma e în VIES.
- Butonul **Actualizare din ANAF** lângă CUI: reîncarcă datele (telefonul existent se păstrează); chatterul listează fiecare câmp modificat cu valoarea veche și nouă și semnalează firma radiată sau inactivă; cu `l10n_ro_anaf_partner` se actualizează și *TVA la încasare (RTVAI)*. La o firmă UE reîncarcă din VIES și setează *Valid intracomunitar*.
- Partener creat cu CUI-ul ca nume (*Creează* sau import): se completează din ANAF; valorile date explicit se păstrează, iar partenerul cu CUI, persoanele de contact și partenerii din altă țară rămân neatinși. Cheia de context `l10n_ro_anaf_no_autofill` dezactivează funcția (ex. import în masă).
- Câmpul **Plătitor TVA** pe formular, CUI-ul păstrat fără prefix de țară; alegerea orașului (cu `l10n_ro_city`) păstrează codul poștal existent.
- Acțiunea **Îmbogățește** (Odoo 20) din listă și formular întreabă ANAF (după CUI sau ID companie) sau VIES și completează doar câmpurile goale.
- *Valid intracomunitar* se setează cu `l10n_eu_account_vies`; fără el, răspunsul VIES apare doar în chatter. Fluxul pas cu pas: [Fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `partner_autocomplete`
- [l10n_ro_anaf_partner_lookup](../l10n_ro_anaf_partner_lookup/index.md)

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins): căutare ANAF / VIES, completare, actualizare și îmbogățire.

**Vizualizări**

- `view_partner_form_anaf_refresh`: butonul de actualizare din ANAF lângă CUI.
- `res_config_settings_view_form_anaf`: setările de autocompletare.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [l10n_ro_anaf_partner_lookup](../l10n_ro_anaf_partner_lookup/index.md): căutarea în ANAF folosită la completare.
- [l10n_ro_partner_create_by_vat](../l10n_ro_partner_create_by_vat/index.md): alternativă care completează tot din ANAF; se exclud reciproc.
