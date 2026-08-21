# No quick_create (localizat la `deltatech_no_quick_create/index.md`)

- **Nume Tehnic:** `deltatech_no_quick_create`
- **Versiune:** `19.0.2.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_no_quick_create
- **Cale Locală:** `odoo-addons/deltatech/deltatech_no_quick_create`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul dezactivează, la nivel global, opțiunea de „creare rapidă" (quick create) din câmpurile de tip relație (Many2one) afișate în interfața Odoo. În mod implicit, atunci când un utilizator tastează o valoare nouă într-un astfel de câmp, Odoo oferă crearea instantanee a unei înregistrări fără a deschide formularul complet. Dezactivând acest comportament, modulul previne apariția de înregistrări incomplete sau goale (produse, parteneri, contacte etc.), obligând utilizatorul să completeze datele necesare prin formularul de editare. Rezultatul este o calitate mai bună a datelor și mai puține înregistrări eronate în baza de date.

#### 2. Funcționalități Cheie

- Dezactivează opțiunea de creare rapidă a noilor înregistrări direct din câmpurile relaționale, fără editarea lor, pentru a preveni produse, contacte etc. goale.

#### 3. Dependențe

- `base`
- `web`

#### 4. Componente Cheie

**Vizualizări**

Modulul nu definește modele, vizualizări XML, acțiuni automate sau acțiuni server. Întreaga funcționalitate este implementată în partea de frontend (JavaScript).

**Asset-uri JavaScript**

- `static/src/js/fields.esm.js`: aplică un `patch` pe componenta OWL de bază `Many2One` (din `@web/views/fields/many2one/many2one`), care este componenta partajată prin care se randează `Many2OneField`, `Many2OneBarcodeField`, `Many2OneAvatarField`, `ReferenceField` etc. Prin patch-ul aplicat pe `many2XAutocompleteProps` (setare `quickCreate: null`), crearea rapidă este dezactivată peste tot, indiferent de widget-ul folosit — un patch pe un singur widget (ex. doar pe `Many2OneField`) ar fi ratat variantele precum `many2one_barcode`. Asset-ul este încărcat în bundle-ul `web.assets_backend`. Codul conține și o linie comentată pentru dezactivarea opțiunii „Create and edit...” (`activeActions.createEdit`), momentan neactivată.

#### 5. Conexiuni

Modulul nu are conexiuni funcționale specifice cu alte module documentate; este o utilitate transversală de interfață care influențează comportamentul tuturor câmpurilor Many2one din backend.
