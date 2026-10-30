# Romania - Partner Autocomplete from ANAF (localizat la `l10n_ro_partner_autocomplete/index.md`)

- **Nume Tehnic:** `l10n_ro_partner_autocomplete`
- **Versiune:** `19.0.1.3.1`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_partner_autocomplete
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_partner_autocomplete`
- **Ultima Ingestie:** `2026-10-30`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Completarea automată standard a partenerilor din Odoo sugerează firmele din serviciul IAP și consumă credite la fiecare completare. Pentru o firmă din România sursa oficială este ANAF, iar interogarea ei este gratuită. Modulul înlocuiește IAP cu ANAF pentru un CUI românesc: tastat acolo unde Odoo oferă completarea automată, CUI-ul aduce sugestia direct de la ANAF, iar alegerea ei completează partenerul, fără niciun credit consumat. Restul cazurilor (căutarea după denumire, firmele din alte țări, ANAF indisponibil) rămân la IAP, ca în standard.

#### 2. Funcționalități Cheie

- **Sugestie din ANAF la CUI:** un CUI românesc, cu sau fără `RO`, tastat în *Cod fiscal (TVA)* sau *Nume* ale partenerului, în câmpul *Client* dintr-o ofertă sau factură ori în fișa clientului din Punctul de vânzare, arată firma găsită la ANAF. Nici căutarea, nici îmbogățirea nu mai merg la IAP.
- **Date completate:** denumire, cod fiscal (cu `RO` doar pentru plătitorii de TVA), stradă și număr, detalii de adresă, localitate, județ, cod poștal, număr de înregistrare la Registrul Comerțului și telefon; pentru București, sectorul ca localitate, cum cere e-Factura. Istoricul (chatter) primește o notă că datele vin de la ANAF, cu data.
- **Buton „Actualizează din ANAF”:** pe o companie românească cu cod fiscal, sub câmpul TVA, reîncarcă datele din ANAF (nume, adresă, cod fiscal, NRC; un telefon existent se păstrează). Istoricul listează fiecare câmp modificat, cu valoarea veche și cea nouă, și avertizează când ANAF arată firma ca radiată sau inactivă.
- **Partener creat cu CUI-ul drept nume:** alegerea *Creează* după ce ai tastat un CUI într-un câmp precum *Client*, sau importul de parteneri al căror nume este un CUI, îi completează tot din ANAF. Valorile date explicit se păstrează; un partener care are deja cod fiscal, o persoană de contact sau o țară diferită rămâne neschimbat. Cheia de context `l10n_ro_anaf_no_autofill` oprește comportamentul (de exemplu la importuri în masă).
- **Oraș și cod poștal:** cu lista orașelor din România (`l10n_ro_city`), orașul se alege și din listă, iar alegerea păstrează codul poștal deja existent în loc să-l înlocuiască cu cel al orașului.
- **Rămâne la IAP:** căutarea după denumire, firmele din alte țări și un CUI românesc când ANAF nu răspunde.
- **Setări:** în *Setări → Configurări generale → Contacte → Completarea automată a partenerului* apare o notă despre completarea din ANAF fără credite. Opțiunea standard trebuie să fie bifată, altfel nu se oferă nicio sugestie.
- **Incompatibilitate:** nu se instalează împreună cu `l10n_ro_partner_create_by_vat` (OCA), pentru că ambele completează partenerul din ANAF, fiecare în felul lui; acela se dezinstalează întâi, cu modulele care depind de el.

Fluxul pas cu pas, cu capturi, este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `partner_autocomplete`
- [l10n_ro_anaf_partner_lookup](../l10n_ro_anaf_partner_lookup/index.md)

Excludere (`excludes`): `l10n_ro_partner_create_by_vat`.

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins): suprascrie `autocomplete_by_vat`, `autocomplete_by_name` și `enrich_by_duns` ca un CUI românesc să fie rezolvat prin ANAF (`l10n.ro.anaf.partner.lookup`) și să nu ajungă la IAP; `onchange` adaugă sugestia; `enrich_company_message_post` pune nota din istoric; `action_l10n_ro_anaf_refresh` reîncarcă datele din ANAF și listează modificările; `create` completează un partener al cărui nume este un CUI (dezactivabil cu `l10n_ro_anaf_no_autofill`).

**Vizualizări**

- `view_partner_form_anaf_refresh`: moștenește `base.view_partner_form` și adaugă butonul *Actualizează din ANAF* sub codul fiscal.
- `res_config_settings_view_form_anaf`: moștenește setarea `partner_autocomplete` din configurări și adaugă nota despre ANAF.

**Acțiuni Automate / Acțiuni Server**

- Nu are acțiuni automate sau acțiuni server.

#### 5. Conexiuni

- [l10n_ro_anaf_partner_lookup](../l10n_ro_anaf_partner_lookup/index.md): face interogarea efectivă către ANAF; acest modul o leagă de completarea automată a partenerilor.
- `l10n_ro_city`: lista orașelor din România; când este instalat, orașul se alege din listă și se păstrează codul poștal existent.
- `l10n_ro_partner_create_by_vat`: modul OCA incompatibil (exclus).
