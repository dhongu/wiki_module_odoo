# Romania - EU Legal Guarantee Notice (localizat la `l10n_ro_website_legal_guarantee/index.md`)

- **Nume Tehnic:** `l10n_ro_website_legal_guarantee`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_website_legal_guarantee
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_website_legal_guarantee`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Modulul afișează pe site-ul de comerț electronic notificarea armonizată a Uniunii Europene privind garanția legală de conformitate, obligatorie pentru vânzătorii de bunuri de la 27 septembrie 2026 (Regulamentul de punere în aplicare (UE) 2025/1960, Directiva (UE) 2024/825 și OUG nr. 34/2014, modificată prin OUG nr. 18/2026). Notificarea este fișierul oficial al Comisiei Europene, nemodificat, în română pentru site-urile în limba română și în engleză pentru celelalte limbi.

#### 2. Funcționalități Cheie

- Pagina publică `/garantie` cu notificarea oficială întreagă, linkul către portalul „Europa ta” (aceeași destinație ca și codul QR din notificare, pe limba curentă), notificarea în PDF, drepturile consumatorului pe scurt (OUG nr. 140/2021), cum se semnalează o problemă și datele vânzătorului.
- Linkul „Garanția legală” în footer, pe rândul de copyright.
- Linkul „Drepturile tale privind garanția legală” pe pagina de produs și la pasul de plată, care deschide notificarea la primul clic (recomandarea ghidului practic DG JUST, aprilie 2026).
- Configurare per website, din *Website → Configurare → Setări*, secțiunea *Notificarea UE privind garanția legală*: se alege în care dintre locurile footer / pagina de produs / pasul de plată apare linkul (toate bifate implicit).
- Pagina `/garantie` preia telefonul, e-mailul, codul fiscal și adresa companiei website-ului; conținut suplimentar (de exemplu termenele proprii de service) se adaugă din editorul de site, în zonele de deasupra și de sub conținutul paginii.
- Limite: notificarea este o obligație a vânzătorului la nivel de magazin; eticheta GARAN (garanția comercială de durabilitate) este o obligație separată, per produs, și nu este acoperită. Includerea notificării în e-mailul de confirmare a comenzii (recomandată de ghid) se face per client, șabloanele fiind `noupdate`.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

- `website` (extins): trei câmpuri booleene (`legal_guarantee_footer`, `legal_guarantee_product`, `legal_guarantee_checkout`, implicit adevărate) și metoda `_get_legal_guarantee_notice`, care alege imaginea/PDF-ul (RO sau EN) și linkul „Europa ta” în funcție de limba curentă.
- `res.config.settings` (extins): câmpuri related către cele trei opțiuni ale website-ului.

**Vizualizări**

- `legal_guarantee_page`: pagina publică `/garantie` (controller `LegalGuarantee`, rută publică inclusă în sitemap).
- `legal_guarantee_footer`: linkul din footer (moștenește `web.frontend_layout`).
- `legal_guarantee_product`: linkul de pe pagina de produs (moștenește `website_sale.product`).
- `legal_guarantee_payment`: linkul de la pasul de plată (moștenește `website_sale.payment`).
- `legal_guarantee_modal`: fereastra modală cu notificarea (moștenește `web.frontend_layout`).
- `res_config_settings_view_form`: secțiunea de setări pentru alegerea locurilor de afișare.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- `website_sale`: modulul își atașează linkurile la pagina de produs și la pasul de plată din magazinul online.
