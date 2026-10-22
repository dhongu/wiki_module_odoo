# Website llms.txt

- **Nume Tehnic:** `deltatech_website_llms_txt`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_llms_txt
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_llms_txt`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Modulul publică pe site-ul Odoo fișierul `/llms.txt`: un rezumat scurt, în format Markdown ([llms.txt](https://llmstxt.org)), pe care asistenții AI (ChatGPT, Claude, Perplexity etc.) îl citesc ca să înțeleagă cine sunteți și care sunt paginile importante, în loc să deducă din HTML. Fișierul se generează automat din site, iar textele proprii pot fi completate din setările site-ului.

#### 2. Funcționalități Cheie

- **Generat din site:** numele site-ului, un rezumat, datele de contact ale companiei (email, telefon, oraș, țară), paginile publicate și indexate (cu meta descriere), magazinul și categoriile lui (dacă eCommerce e instalat) și sitemap-ul.
- **Textele dumneavoastră au prioritate:** un *Rezumat* (fără el se folosește meta descrierea paginii de start) și *Detalii* în Markdown (zone de livrare, plată, retururi, ce trebuie să știe un asistent înainte să vă recomande), setate per website.
- **Control deplin:** un *Fișier personalizat*, dacă e completat, este servit ca atare în locul celui generat; fișierul poate fi dezactivat per website (răspuns 404).
- **Un fișier per website:** în bazele multi-website fiecare domeniu servește fișierul propriu, cu paginile și categoriile lui.
- **Configurare:** *Website > Configurare > Setări*, secțiunea *Tracking & SEO*, setarea *llms.txt*; butonul *View llms.txt* deschide fișierul servit la `https://<domeniu>/llms.txt`.
- **Date publicate:** doar ce este deja public pe site (pagini publicate, categorii de magazin, emailul, telefonul și orașul companiei) și textele introduse în setări. Fiecare secțiune listează cel mult 100 de linkuri.

#### 3. Dependențe

- `website`

#### 4. Componente Cheie

**Modele**

- `website` (extins): câmpurile `llms_txt_enabled`, `llms_txt_summary`, `llms_txt_details`, `llms_txt_custom` și metodele care generează conținutul (`_get_llms_txt`, `_get_llms_txt_sections` etc.; alte module își pot adăuga secțiuni).
- `res.config.settings` (extins): câmpuri related către setările de mai sus.

**Vizualizări**

- `res_config_settings_view_form`: setarea *llms.txt* în configurarea Website.

**Acțiuni Automate / Acțiuni Server**

- Nu există. Ruta publică `/llms.txt` (controller `WebsiteLlmsTxt`) servește fișierul ca `text/plain`.

#### 5. Conexiuni

- `website_sale`: dacă este instalat, fișierul include magazinul și categoriile publice (legătură opțională, fără dependență).
