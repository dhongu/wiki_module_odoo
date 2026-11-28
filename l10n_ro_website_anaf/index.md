# Romania - Website ANAF (`l10n_ro_website_anaf`)

- **Nume Tehnic:** `l10n_ro_website_anaf`
- **Versiune:** `20.0.1.2.2`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_website_anaf
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_website_anaf`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Aduce ANAF în formularele de adresă ale website-ului (checkout și portal client), pentru o adresă de facturare din România. Firma este completată din datele ANAF în timp ce clientul tastează codul fiscal și este verificată la trimiterea adresei, deci facturile și e-Factura pornesc de la datele legale corecte.

#### 2. Funcționalități Cheie

- **La tastarea CUI:** sub cod apare firma găsită la ANAF (denumirea pe care se emite factura, adresa, plătitor de TVA); câmpurile goale (firmă, stradă, oraș, cod poștal, județ, nr. registrul comerțului unde există) se completează imediat, iar butonul **Fill in from ANAF** le înlocuiește și pe cele tastate, doar la cererea clientului.
- Firma inactivă fiscal primește un avertisment, firma radiată află că nu poate comanda, iar un CNP tastat din greșeală are mesaj propriu.
- Rută publică cu limită per vizitator (20 de căutări la 10 minute) și cache de o zi per cod fiscal.
- **La trimiterea adresei:** firma negăsită sau radiată este refuzată, iar CNP-ul are mesaj propriu. Firma găsită primește denumirea legală (entitatea comercială pe care se emit factura și e-Factura; contactul păstrează numele tastat), iar adresa tastată se păstrează, ANAF completând doar câmpurile goale.
- Firma inactivă fiscal poate comanda: coșul primește o notă internă pentru vânzător (cod TVA anulat: factură cu TVA, fără taxare inversă, verifică încasarea).
- Dacă ANAF nu răspunde, vânzarea nu se oprește: numărul se acceptă așa cum a fost tastat, iar coșul primește o notă.
- Orice formular poate folosi căutarea, printr-un câmp cu `data-anaf-lookup` și o hartă `data-anaf-fill` a câmpurilor de completat (o folosește formularul de cont B2B din `deltatech_b2b_portal`).
- Configurare: nu necesită; adresa serviciului ANAF este cea din `l10n_ro_anaf_partner_lookup` (parametrul `l10n_ro_anaf_partner_lookup.url`), iar site-ul așteaptă cel mult 5 secunde un răspuns. Fluxul cu capturi este în fișa consultantului.

#### 3. Dependențe

- `website_sale`
- `l10n_ro_anaf_partner_lookup`

#### 4. Componente Cheie

**Modele**

- Nu definește modele; extinde controllerul `WebsiteSale` (`WebsiteSaleAnaf`) pentru verificarea la trimiterea adresei.

**Vizualizări**

- `address_form_fields_anaf` (moștenește `portal.address_form_fields`): adaugă căutarea ANAF în formularele de adresă.
- `static/src/interactions/anaf_lookup.esm.js`: interacțiunea frontend care apelează ruta de căutare.

**Acțiuni Automate / Acțiuni Server**

- Ruta publică `/l10n_ro/anaf_lookup` (jsonrpc, POST), cu limită per vizitator și cache. Nu există cron-uri.

#### 5. Conexiuni

- [deltatech_b2b_portal](../deltatech_b2b_portal/index.md): formularul de cont B2B folosește căutarea ANAF prin `data-anaf-lookup`.
- `l10n_ro_anaf_partner_lookup`: furnizează serviciul ANAF folosit de modul.
