# No quick_create (localizat la `deltatech_no_quick_create/index.md`)

- **Nume Tehnic:** `deltatech_no_quick_create`
- **Versiune:** `19.0.2.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_no_quick_create
- **Cale Locală:** `odoo-addons/deltatech/deltatech_no_quick_create`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul dezactivează, la nivel global, opțiunea de „creare rapidă" (quick create) din câmpurile de tip relație (Many2one) afișate în interfața Odoo. În mod implicit, atunci când un utilizator tastează o valoare nouă într-un astfel de câmp, Odoo oferă crearea instantanee a unei înregistrări fără a deschide formularul complet. Dezactivând acest comportament, modulul previne apariția de înregistrări incomplete sau goale (produse, parteneri, contacte etc.), obligând utilizatorul să completeze datele necesare prin formularul de editare. Rezultatul este o calitate mai bună a datelor și mai puține înregistrări eronate în baza de date.

#### 2. Funcționalități Cheie

- Dezactivează opțiunea de creare rapidă a noilor înregistrări direct din câmpurile relaționale, fără editarea lor.
- Previne crearea de înregistrări goale sau incomplete (produse, parteneri, contacte etc.).
- Se aplică automat la nivel global în interfața de backend, fără configurare suplimentară.

#### 3. Dependențe

- `base`
- `web`

#### 4. Componente Cheie

**Vizualizări**

Modulul nu definește modele, vizualizări XML, acțiuni automate sau acțiuni server. Întreaga funcționalitate este implementată în partea de frontend.

**Asset-uri JavaScript**

- `static/src/js/fields.esm.js`: aplică un `patch` pe componenta OWL `Many2OneField` (din `@web/views/fields/many2one/many2one_field`) pentru a forța dezactivarea creării rapide (`canQuickCreate = false`) în toate câmpurile Many2one. Asset-ul este încărcat în bundle-ul `web.assets_backend`.

#### 5. Conexiuni

Modulul nu are conexiuni funcționale specifice cu alte module documentate; este o utilitate transversală de interfață care influențează comportamentul tuturor câmpurilor Many2one din backend.
