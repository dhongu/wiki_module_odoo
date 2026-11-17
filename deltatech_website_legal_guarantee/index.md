# EU Legal Guarantee Notice (localizat la `deltatech_website_legal_guarantee/index.md`)

- **Nume Tehnic:** `deltatech_website_legal_guarantee`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_legal_guarantee
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_legal_guarantee`
- **Ultima Ingestie:** `2026-11-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Afișează pe site-ul web notificarea armonizată a Uniunii Europene privind garanția legală de conformitate, obligatorie pentru vânzătorii de bunuri către consumatori începând cu 27 septembrie 2026. Notificarea oficială a Comisiei Europene este prezentată nemodificată, în limba paginii, pentru toate cele 24 de limbi oficiale ale UE (în engleză pentru orice altă limbă). Modulul este succesorul generic al modulului `l10n_ro_website_legal_guarantee`.

#### 2. Funcționalități Cheie

- Pagina publică `/garantie` cu notificarea oficială completă (clic pe imagine deschide PDF-ul), linkul către portalul „Your Europe” (aceeași destinație ca QR-ul), drepturile consumatorului pe scurt, modul de raportare a unei probleme și datele vânzătorului (nume, CUI, adresă, telefon, e-mail din compania site-ului).
- Link „Legal guarantee” în subsolul site-ului, în rândul de copyright.
- Link „Your legal guarantee rights” pe pagina de produs (sub detaliile produsului) și la pasul de plată (sub adresa de facturare); la primul clic se deschide notificarea într-o fereastră, fără ca clientul să piardă produsul sau coșul, conform ghidurilor practice ale Comisiei (DG JUST, aprilie 2026).
- Setări per site în *Website → Configuration → Settings*, secțiunea *EU legal guarantee notice*: se alege unde apare linkul (subsol, pagina de produs, checkout); toate sunt bifate implicit.
- Rezumatul drepturilor urmează Directiva (UE) 2019/771; pentru țara companiei site-ului se afișează un bloc cu reguli naționale. Modulul include blocul pentru România (OUG 140/2021, ANPC); alte țări se adaugă printr-un template `national_<cod țară>`.
- Pagina și linkurile sunt traduse în toate limbile UE (traducere asistată de AI).
- Conținut suplimentar (ex.: propriile condiții de service) se adaugă din editorul website, în zonele de deasupra și de sub conținutul paginii.
- Baza legală: Regulamentul de punere în aplicare (UE) 2025/1960 (Anexa I), Directiva (UE) 2024/825 (art. 22a din Directiva 2011/83/UE) și Directiva (UE) 2019/771.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

- `website` (extins): trei câmpuri booleene, implicit active: `legal_guarantee_footer`, `legal_guarantee_product`, `legal_guarantee_checkout`.
- `res.config.settings` (extins): expune cele trei câmpuri ca setări per site.

**Vizualizări**

- `legal_guarantee_page`: pagina publică `/garantie` (controller `main.py`, `auth="public"`, inclusă în sitemap).
- `legal_guarantee_notice`, `legal_guarantee_link`, `legal_guarantee_modal`: notificarea, linkul și fereastra modală.
- `legal_guarantee_footer`, `legal_guarantee_product`, `legal_guarantee_payment`: inserarea linkului în subsol, pe pagina de produs și la plată.
- `national_ro`: blocul cu reguli naționale pentru România.
- `res_config_settings_view_form`: secțiunea de setări în Website.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [l10n_ro_website_legal_guarantee](../l10n_ro_website_legal_guarantee/index.md): modulul predecesor din suita românească, înlocuit de această variantă generică.
