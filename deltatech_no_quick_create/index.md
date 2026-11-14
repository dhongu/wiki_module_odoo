# No quick_create (localizat la `deltatech_no_quick_create/index.md`)

- **Nume Tehnic:** `deltatech_no_quick_create`
- **Versiune:** `19.0.2.1.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_no_quick_create
- **Cale Locală:** `odoo-addons/deltatech/deltatech_no_quick_create`
- **Ultima Ingestie:** `2026-11-14`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul dezactivează, la nivel global, opțiunea de „creare rapidă" (quick create) din câmpurile de tip relație (Many2one) afișate în interfața Odoo. În mod implicit, atunci când un utilizator tastează o valoare nouă într-un astfel de câmp, Odoo oferă crearea instantanee a unei înregistrări fără a deschide formularul complet. Dezactivând acest comportament, modulul previne apariția de înregistrări incomplete sau goale (produse, parteneri, contacte etc.), obligând utilizatorul să completeze datele necesare prin formularul de editare. Rezultatul este o calitate mai bună a datelor și mai puține înregistrări eronate în baza de date.

#### 2. Funcționalități Cheie

- Dezactivează opțiunea de creare rapidă (`Create "..."`) direct din câmpurile relaționale, pentru a preveni produse, contacte etc. goale.
- Se aplică tuturor widget-urilor many2one (simplu, avatar, barcode, reference); opțiunea **Create and edit...** rămâne disponibilă, cu numele tastat deja completat în dialog.
- Nu necesită configurare: după instalare și reîncărcarea paginii, comportamentul e activ peste tot (ex. **Contacte > Contacte**, câmpul **Company**).
- Modulul nu conține cod Python, doar un fișier JavaScript, deci poate fi folosit și pe Odoo Online (plan Custom): arhiva zip se încarcă din **Apps > Import Module** (mod developer), pe lângă Odoo.sh și on-premise.
- Pașii ilustrați cu capturi se găsesc în fișa consultant.

#### 3. Dependențe

- `base`
- `web`

#### 4. Componente Cheie

**Modele, vizualizări, acțiuni**

Modulul nu definește modele, vizualizări XML, acțiuni automate sau acțiuni server și nu conține cod Python (nu are nici `__init__.py`). Întreaga funcționalitate este implementată în frontend (JavaScript).

**Asset-uri JavaScript**

- `static/src/js/fields.esm.js`: aplică un `patch` pe componenta OWL de bază `Many2One` (din `@web/views/fields/many2one/many2one`), care este componenta partajată prin care se randează `Many2OneField`, `Many2OneBarcodeField`, `Many2OneAvatarField`, `ReferenceField` etc. Prin patch-ul aplicat pe `many2XAutocompleteProps` (setare `quickCreate: null`), crearea rapidă este dezactivată peste tot, indiferent de widget-ul folosit — un patch pe un singur widget (ex. doar pe `Many2OneField`) ar fi ratat variantele precum `many2one_barcode`. Asset-ul este încărcat în bundle-ul `web.assets_backend`. Codul conține și o linie comentată pentru dezactivarea opțiunii „Create and edit...” (`activeActions.createEdit`), momentan neactivată.

#### 5. Conexiuni

Modulul nu are conexiuni funcționale specifice cu alte module documentate; este o utilitate transversală de interfață care influențează comportamentul tuturor câmpurilor Many2one din backend.
