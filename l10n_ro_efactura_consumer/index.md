# Romania - e-Factura B2C (persoane fizice) (localizat la `l10n_ro_efactura_consumer/index.md`)

- **Nume Tehnic:** `l10n_ro_efactura_consumer`
- **Nume anterior:** `l10n_ro_efactura_b2c` (redenumit pe 23.09.2026: numele vechi e ocupat pe Odoo Apps de alt furnizor)
- **Versiune:** `20.0.1.0.8`
- **Cale:** `https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_efactura_consumer`
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_efactura_consumer`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Extinde `l10n_ro_edi` pentru facturile e-Factura transmise către persoane fizice (B2C) prin SPV, conform CIUS-RO. Adaugă CNP-ul pe partener, îl validează prin algoritmul Luhn RO și îl pune în XML-ul UBL cu `schemeID="CNP"`, în locul valorii implicite `0000000000000`. Firmele care facturează doar către persoane juridice cu cod de TVA nu au nevoie de modul.

#### 2. Funcționalități Cheie

- Câmpul **CNP (Persoană Fizică RO)** pe partener (Facturare → Clienți), vizibil sub TVA cât timp partenerul nu are cod TVA și țara fiscală a firmei este România; criteriul este lipsa codului TVA, nu tipul Persoană/Companie. Coloană opțională **CNP** în lista de clienți.
- Validare la salvare prin algoritmul Luhn RO (13 cifre, prima cifră 1–8, cifră de control corectă): un CNP greșit nu se salvează; câmpul calculat **CNP Valid** indică rezultatul.
- XML CIUS-RO B2C corect: `schemeID="CNP"` în `PartyLegalEntity/CompanyID` și `PartyIdentification/ID`.
- Blocare la trimiterea în SPV dacă CNP-ul este completat dar invalid; dacă lipsește, factura se trimite cu identificatorul anonim `0000000000000` (comportamentul standard).
- Banner de avertizare pe factură când clientul persoană fizică română nu are CNP valid.
- La instalare, migrarea CNP-urilor din câmpul `cnp` al `deltatech_contact` în `l10n_ro_cnp` (doar unde câmpul nou e gol; nu rulează la instalarea ulterioară a lui `deltatech_contact`).
- Protecție GDPR: câmpul CNP este accesibil doar utilizatorilor interni (`base.group_user`).
- Fără setări proprii: conexiunea la SPV rămâne în `l10n_ro_edi`.

#### 3. Dependențe

- `l10n_ro_edi`

#### 4. Componente Cheie

**Modele**

- `res.partner` (extindere): câmpul `l10n_ro_cnp` și câmpul calculat „CNP Valid” (validare Luhn RO).
- `account.move` (extindere): validarea pre-trimitere și avertizarea pentru persoane fizice fără CNP valid.
- `account.edi.xml.ubl_ro` (extindere): generatorul XML CIUS-RO folosește CNP-ul cu `schemeID="CNP"` în locul valorii implicite.

**Vizualizări**

- `view_partner_form_cnp_ro_inherit`: câmpul CNP și indicatorul de validitate pe formularul partenerului.
- `view_partner_list_cnp_ro_inherit`: coloana opțională CNP în lista de parteneri.
- `view_move_form_cnp_b2c_inherit`: avertizarea pe formularul facturii.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook` (`hooks.py`): migrarea CNP-urilor existente din `deltatech_contact`, dacă modulul este prezent.

#### 5. Conexiuni

- [l10n_ro_efactura_dedup](../l10n_ro_efactura_dedup/index.md): deduplicarea facturilor din SPV, același ecosistem `l10n_ro_edi`.
- [l10n_ro_etransport_block](../l10n_ro_etransport_block/index.md): blocarea documentelor e-Transport, alt modul de control peste fluxurile ANAF.
- [deltatech_contact](../deltatech_contact/index.md): sursa câmpului `cnp` migrat la instalare (legătură opțională).
