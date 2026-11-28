# Website llms.txt (localizat la `deltatech_website_llms_txt/index.md`)

- **Nume Tehnic:** `deltatech_website_llms_txt`
- **Versiune:** `20.0.1.1.0`
- **Cale:** [https://github.com/dhongu/deltatech/tree/20.0/deltatech_website_llms_txt](https://github.com/dhongu/deltatech/tree/20.0/deltatech_website_llms_txt)
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_llms_txt`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul publică `/llms.txt` pe website-ul Odoo: un scurt rezumat Markdown al site-ului, în formatul [llms.txt](https://llmstxt.org), pe care ChatGPT, Claude, Perplexity și alți asistenți AI îl citesc pentru a înțelege cine sunteți și care pagini contează, în loc să ghicească din HTML.

#### 2. Funcționalități Cheie

- **Generat din website**: numele site-ului, un rezumat, datele de contact ale companiei, paginile publicate și indexate (cu meta description), magazinul și categoriile lui când eCommerce este instalat, plus sitemap-ul.
- **Cuvintele dumneavoastră primele**: un rezumat și un text Markdown liber (zone de livrare, plată, retururi, ce trebuie să știe un asistent înainte să vă recomande) se scriu per website, în tab-ul *llms.txt* al formularului website-ului. Fără rezumat se folosește meta description a paginii de start.
- **Control deplin**: un fișier personalizat (*Custom llms.txt*), dacă este completat, este servit ca atare în locul celui generat; fișierul poate fi dezactivat per website.
- **Un fișier per website**: pe o bază multi-website fiecare domeniu servește fișierul propriu, cu paginile și categoriile proprii.
- Configurare: *Website > Configuration > Settings*, secțiunea *Tracking & SEO*, setarea *llms.txt* rămâne bifată, *Edit llms.txt* deschide tab-ul, iar *View llms.txt* verifică fișierul servit la `https://<domeniu>/llms.txt`. Pașii detaliați, cu capturi, sunt în fișa consultant.
- Date publicate: doar ce este deja public pe website (pagini publicate, categorii din magazin, e-mailul, telefonul, orașul și țara companiei) și textele scrise pentru fișier.

#### 3. Dependențe

- `website`

#### 4. Componente Cheie

**Modele**

- `website` (extins): rezumatul, detaliile, fișierul personalizat, publicarea per website și generarea conținutului (`_get_llms_txt`, secțiuni, contact, descrieri de pagini).
- `res.config.settings` (extins): setarea *llms.txt* și acțiunea `action_open_llms_txt`.

**Vizualizări**

- `views/res_config_settings_views.xml`: setarea *llms.txt* în *Tracking & SEO*, cu linkurile *Edit* și *View*.
- `views/website_views.xml`: tab-ul *llms.txt* din formularul website-ului.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite. Controllerul `WebsiteLlmsTxt` expune ruta publică `/llms.txt`.

#### 5. Conexiuni

- [deltatech_website_indexnow](../deltatech_website_indexnow/index.md): trimite motoarelor de căutare paginile modificate; complementar vizibilității pentru AI.
