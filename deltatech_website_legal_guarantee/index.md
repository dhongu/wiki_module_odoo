# EU Legal Guarantee Notice (localizat la `deltatech_website_legal_guarantee/index.md`)

- **Nume Tehnic:** `deltatech_website_legal_guarantee`
- **Versiune:** `20.0.1.0.0`
- **Cale:** [https://github.com/dhongu/deltatech/tree/20.0/deltatech_website_legal_guarantee](https://github.com/dhongu/deltatech/tree/20.0/deltatech_website_legal_guarantee)
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_legal_guarantee`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul afișează pe website nota armonizată a Uniunii Europene privind garanția legală de conformitate, obligatorie pentru vânzătorii de bunuri către consumatori începând cu 27 septembrie 2026, în toate limbile UE. Vânzătorul își îndeplinește astfel obligația de informare fără configurare suplimentară.

#### 2. Funcționalități Cheie

- Pagina publică `/garantie` cu nota oficială completă (clic pe imagine deschide PDF-ul), linkul către portalul „Your Europe”, drepturile consumatorului pe scurt, cum se raportează o problemă și datele vânzătorului (telefon, e-mail, CUI, adresă ale companiei website-ului).
- Linkul „Legal guarantee” în subsolul paginii, în rândul de copyright.
- Linkul „Your legal guarantee rights” pe pagina produsului și la pasul de plată, care deschide nota la primul clic, conform ghidului practic al Comisiei (DG JUST, aprilie 2026).
- Nota este fișierul oficial al Comisiei Europene, în culori și nemodificat, în limba paginii, pentru cele 24 de limbi oficiale UE (engleză pentru orice altă limbă); paginile și linkurile sunt traduse în aceleași limbi.
- Rezumatul drepturilor urmează Directiva (UE) 2019/771; pentru țara companiei website-ului se afișează un bloc cu regulile naționale. Modulul include blocul pentru România (OUG 140/2021, ANPC); alte țări se adaugă cu un template `national_<cod țară>`.
- Setări per website în *Website > Configuration > Settings*, secțiunea *EU legal guarantee notice*: unde apare linkul (subsol, pagina produsului, checkout), toate bifate implicit.
- Conținut suplimentar (ex. termenii proprii de service) se adaugă din editorul website, în zonele de deasupra și de sub conținutul paginii.
- Nu acoperă eticheta GARAN (garanția comercială de durabilitate), care este o obligație separată, per produs. Nota în e-mailul de confirmare a comenzii se adaugă per client, șabloanele fiind `noupdate`.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

- `website` (extins): câmpurile `legal_guarantee_footer`, `legal_guarantee_product`, `legal_guarantee_checkout` și metodele pentru nota, șablonul național și datele vânzătorului.
- `res.config.settings` (extins): opțiunile din setări legate de website.

**Vizualizări**

- `views/templates.xml`: pagina `/garantie`, linkurile din subsol, pagina produsului și checkout.
- `views/national_ro.xml`: blocul cu regulile naționale pentru România.
- `views/res_config_settings_views.xml`: secțiunea *EU legal guarantee notice* din setări.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite. Controllerul `LegalGuarantee` expune ruta publică `/garantie`.

#### 5. Conexiuni

- `website_sale`: pagina produsului și pasul de plată în care apare linkul.
