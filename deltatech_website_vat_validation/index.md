# Website VAT Validation (localizat la `deltatech_website_vat_validation/index.md`)

- **Nume Tehnic:** `deltatech_website_vat_validation`
- **Versiune:** `19.0.0.2.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_vat_validation`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_vat_validation`
- **Ultima Ingestie:** `2026-10-12`

#### 1. Sumar

Acest modul îmbunătățește validarea codului de TVA și a adresei de e-mail în procesul de comandă (checkout) de pe website și în portalul de client din Odoo. Scopul principal este creșterea calității datelor și prevenirea conturilor duplicate pentru aceeași firmă, oferind clientului logat un mesaj clar despre ce poate face. Modulul este neutru din punct de vedere al țării: verificările specifice României (interogarea ANAF, cod numeric personal, firmă radiată) se găsesc în modulul `l10n_ro_website_anaf` din suita l10n-romania.

#### 2. Funcționalități Cheie

- Eliminarea automată a spațiilor din valorile introduse pentru TVA, e-mail și telefon
- Verificarea codului de TVA duplicat la checkout și în portal, doar pentru clientul logat (vizitatorul anonim nu este verificat, ca să nu se poată afla dacă un cod aparține unui client existent)
- Compararea codului de TVA fără prefixul de țară și fără spații (`RO12345678` = `12345678`)
- Mesaj de eroare orientat spre acțiune când firma are deja cont: clientul este îndrumat să ceară unui coleg cu acces să-l adauge, să trimită o cerere de acces din pagina `/b2b` (dacă este instalat `deltatech_b2b_portal`) sau să ne contacteze
- Verificarea e-mailului: o adresă aparținând altui cont cere autentificarea cu acel cont sau folosirea altei adrese
- Firma proprie a clientului și contactele ei nu sunt considerate duplicate; telefonul nu se mai verifică (colegii folosesc același telefon)
- Mesajele nu dezvăluie niciodată contul găsit
- Păstrarea opțiunii „Display Product Prices” a website-ului la recalcularea țării fiscale a companiei (nu se mai resetează tăcut la `tax_excluded`)
- La actualizare, o bază de date care avea verificarea ANAF (`l10n_ro_partner_create_by_vat` instalat) primește automat `l10n_ro_website_anaf`, dacă l10n-romania este în addons path; altfel se scrie un avertisment în log

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

Sumarul și funcționalitățile provin din `readme/DESCRIPTION.md` și `readme/HISTORY.md`; analiza detaliată a codului este omisă, conform fluxului de ingestie (modulul nu are modele noi, vizualizări sau acțiuni automate; extinde un controller și modelul `website`).

#### 5. Conexiuni

- `website_sale`: modulul standard de e-commerce Odoo pe care îl extinde (`_validate_address_values`) pentru validarea la checkout și în portal.
- [deltatech_b2b_portal](../deltatech_b2b_portal/index.md): dacă este instalat, mesajul de TVA duplicat trimite clientul la formularul de cerere de acces `/b2b`.
- `l10n_ro_website_anaf` (l10n-romania): verificările românești ale codului fiscal (ANAF, CNP, firmă radiată), mutate din acest modul.
