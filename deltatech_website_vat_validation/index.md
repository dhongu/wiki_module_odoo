# Website VAT Validation (localizat la `deltatech_website_vat_validation/index.md`)

- **Nume Tehnic:** `deltatech_website_vat_validation`
- **Versiune:** `20.0.0.3.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_website_vat_validation`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_vat_validation`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul curăță formularul de adresă din comanda online și din portalul clientului și împiedică un client autentificat să înregistreze un cod fiscal sau o adresă de e-mail care aparțin deja altui client. În plus, păstrează setarea de afișare a prețurilor pe website (cu sau fără taxe), care altfel ar putea fi resetată în fundal. Formatul codului fiscal este verificat de Odoo; verificările românești (ANAF, CNP, firmă radiată) sunt în `l10n_ro_website_anaf`, astfel că acest modul rămâne neutru ca țară.

#### 2. Funcționalități Cheie

- **Valori curățate**: spațiile din jurul codului fiscal, e-mailului și telefonului din formularul de adresă sunt eliminate.
- **Cod fiscal duplicat blocat**: un client autentificat nu poate folosi un cod fiscal al altui client. Codurile se compară fără prefixul de țară și fără spații (`RO 12 34 56 07`, `ro12345607` și `12345607` sunt același cod).
- **E-mail duplicat blocat**: un client autentificat nu poate folosi adresa de e-mail a altui cont; mesajul îl îndeamnă să se autentifice cu acel cont sau să folosească altă adresă.
- **Mesaje care spun ce să faci**: pentru un cod fiscal deja folosit, clientul este rugat să ceară acces de la un coleg care are cont, să trimită o cerere de acces din pagina `/b2b` (cu `deltatech_b2b_portal`) sau să contacteze magazinul. Contul găsit nu este numit niciodată.
- **Fără false duplicate**: firma proprie a clientului și contactele ei nu sunt duplicate, iar telefonul nu este verificat (colegii folosesc același telefon de firmă).
- **Comanda ca vizitator rămâne neschimbată**: verificările rulează doar pentru clienții autentificați, ca mesajul să nu dezvăluie cuiva că un e-mail sau un cod fiscal aparține unui client existent.
- **Fără a doua firmă la comandă**: o persoană care completează firma și codul fiscal în adresa de facturare cumpără pentru acea firmă (Odoo 20 o creează ca partener și persoana devine contactul ei). Modulul permite acest lucru doar pentru un cod fiscal pe care nu-l are alt client; un vizitator care tastează codul unui client existent îl păstrează pe propria adresă, nu se creează a doua firmă și nu este atașat la firma existentă.
- **Afișarea prețurilor păstrată**: setarea *Display Product Prices* (cu sau fără taxe) își păstrează valoarea salvată când Odoo o recalculează, de exemplu după rescrierea adresei partenerului companiei de o sincronizare ANAF.
- Verificările rulează la salvarea formularelor din pasul *Adresă* al comenzii și din *Contul meu > Editare informații* / *Adrese*; modulul nu are setări proprii. Fluxul detaliat este în fișa consultantului.
- Actualizare de la o versiune mai veche decât 19.0.0.2.0: verificările ANAF s-au mutat în `l10n_ro_website_anaf`, instalat la actualizare dacă l10n-romania este în addons path.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

- `website`: extins pentru a păstra valoarea setării `show_line_subtotals_tax_selection` la recalculare.

**Vizualizări**

- Modulul nu definește vizualizări; validările sunt în controlerul `website_sale` (`_validate_address_values`, `_create_or_update_address`).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- [l10n_ro_website_anaf](../l10n_ro_website_anaf/index.md): verificările românești ale codului fiscal (ANAF, CNP, firmă radiată), complementare acestui modul.
- [deltatech_b2b_portal](../deltatech_b2b_portal/index.md): pagina `/b2b` cu cererea de acces, indicată în mesajul pentru un cod fiscal deja folosit (opțional).
