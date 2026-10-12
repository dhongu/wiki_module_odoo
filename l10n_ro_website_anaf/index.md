# Romania - Website ANAF (localizat la `l10n_ro_website_anaf/index.md`)

- **Nume Tehnic:** `l10n_ro_website_anaf`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_website_anaf
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_website_anaf`
- **Ultima Ingestie:** `2026-10-12`

#### 1. Sumar

Modulul aduce interogarea ANAF în formularele de adresă din website (finalizarea comenzii și portalul clientului), pentru o adresă de facturare din România. Pe măsură ce clientul tastează codul fiscal (CUI), îi sunt afișate firma găsită la ANAF și datele ei, iar câmpurile goale se completează automat; la trimiterea adresei, codul fiscal este verificat, astfel încât factura și e-Factura să fie emise pe denumirea legală corectă.

#### 2. Funcționalități Cheie

**La tastarea codului fiscal:**

- Sub câmpul de cod fiscal apare firma găsită la ANAF: denumirea pe care se emite factura, adresa și dacă este plătitoare de TVA.
- Câmpurile goale (denumire firmă, nr. de înregistrare la registrul comerțului, stradă, oraș, cod poștal, județ) se completează imediat; butonul **Fill in from ANAF** înlocuiește și ce a introdus clientul, doar la cerere.
- O firmă inactivă fiscal primește un avertisment, o firmă radiată este informată că nu poate comanda, iar un CNP introdus din greșeală are mesaj propriu.
- Rută publică cu limită pe vizitator (20 de interogări la 10 minute) și cache de o zi per cod fiscal: ANAF nu este întrebat de două ori pentru aceeași firmă.

**La trimiterea adresei:**

- O firmă negăsită sau radiată la ANAF este refuzată; un CNP are mesaj propriu.
- O firmă găsită primește pe partener denumirea legală (pe ea se emit factura și e-Factura); adresa tastată de client se păstrează, ANAF completează doar câmpurile goale.
- O firmă inactivă fiscal poate comanda: coșul primește o notă internă pentru vânzător (cod TVA anulat: factură cu TVA, fără taxare inversă, de verificat încasarea).
- Dacă ANAF nu răspunde, vânzarea nu este oprită: numărul este acceptat ca introdus, iar coșul primește o notă.

**Reutilizare și configurare:**

- Orice formular poate folosi căutarea: un input marcat cu `data-anaf-lookup` și o hartă `data-anaf-fill` a câmpurilor de completat (o folosește și formularul de cerere cont B2B din `deltatech_b2b_portal`).
- Nu necesită configurare; adresa ANAF și cheia API (dacă există) sunt cele din `l10n_ro_partner_create_by_vat` (parametri de sistem `l10n_ro_partner_create_by_vat.*`).

#### 3. Dependențe

- `website_sale`
- `l10n_ro_partner_create_by_vat`

#### 4. Componente Cheie

**Modele**

- Modulul nu definește modele noi; extinde comportamentul controllerului `WebsiteSale` (`WebsiteSaleAnaf`).

**Vizualizări**

- `address_form_fields_anaf`: moștenește `portal.address_form_fields` și marchează câmpul `vat` cu `data-anaf-lookup`, țara România și harta `data-anaf-fill`.
- Asset frontend `anaf_lookup.esm.js` (interacțiune JS care apelează căutarea) și tur de test `anaf_prefill_tour.esm.js`.

**Acțiuni Automate / Acțiuni Server**

- Rută publică `/l10n_ro/anaf_lookup` (JSON-RPC, POST) cu limită de interogări și cache de o zi.
- Validarea adresei în `_validate_address_values` (`_l10n_ro_anaf_check`) și nota internă pe coș (`_l10n_ro_cart_note`).
- Nu există cron-uri sau acțiuni server.

#### 5. Conexiuni

- [deltatech_b2b_portal](../deltatech_b2b_portal/index.md): formularul de cerere cont B2B folosește aceeași căutare ANAF.
