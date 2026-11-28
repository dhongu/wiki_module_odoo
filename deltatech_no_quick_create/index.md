# No Quick Create (localizat la `deltatech_no_quick_create/index.md`)

- **Nume Tehnic:** `deltatech_no_quick_create`
- **Versiune:** `20.0.2.1.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_no_quick_create
- **Cale Locală:** `odoo-addons/deltatech/deltatech_no_quick_create`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul dezactivează, la nivel global, opțiunea de „creare rapidă" din câmpurile de tip relație (Many2one) din interfața Odoo. În mod normal, când utilizatorul tastează o valoare care nu există, Odoo oferă crearea instantanee a unei înregistrări fără formular. Fără această opțiune, se previne apariția de produse, contacte etc. goale sau incomplete, iar datele se completează prin formularul de editare.

#### 2. Funcționalități Cheie

- Elimină opțiunea **Create "..."** din toate câmpurile many2one (simplu, avatar, barcode, reference); rămâne disponibilă opțiunea **Create and edit...**, care deschide formularul cu numele tastat deja completat.
- Nu necesită configurare: după instalare (și reîncărcarea paginii) comportamentul se aplică peste tot (client, produs, categorie, vânzător etc.).
- Fără cod Python, doar un fișier JavaScript; poate fi folosit și pe Odoo Online (plan Custom), încărcând arhiva din **Apps > Import Module**, pe lângă Odoo.sh și on-premise.
- Fluxul pas-cu-pas, cu capturi, se află în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `base`
- `web`

#### 4. Componente Cheie

Modulul nu definește modele, vizualizări XML, acțiuni automate sau acțiuni server; funcționalitatea este doar în frontend.

**Asset-uri JavaScript**

- `static/src/js/fields.esm.js`: aplică un `patch` pe componenta OWL de bază `Many2One` (`@web/views/fields/many2one/many2one`), prin care se randează `Many2OneField`, `Many2OneBarcodeField`, `Many2OneAvatarField`, `ReferenceField` etc., setând `quickCreate: null` în `many2XAutocompleteProps`. Un patch pe un singur widget ar fi ratat variantele precum `many2one_barcode`. Asset-ul se încarcă în `web.assets_backend`.

#### 5. Conexiuni

Modulul nu are conexiuni funcționale specifice cu alte module documentate; este o utilitate transversală de interfață care influențează toate câmpurile Many2one din backend.
