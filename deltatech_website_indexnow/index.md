# Website IndexNow (localizat la `deltatech_website_indexnow/index.md`)

- **Nume Tehnic:** `deltatech_website_indexnow`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_indexnow
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_indexnow`
- **Ultima Ingestie:** `2026-11-03`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul anunță motoarele de căutare care folosesc protocolul IndexNow (Bing, Yandex, Seznam, Naver) ce pagini ale site-ului Odoo au fost publicate sau modificate, astfel încât acestea să fie reindexate în câteva minute, nu la următoarea vizită a robotului. Bing alimentează și căutarea web din ChatGPT și Copilot, deci modificările apar mai repede și acolo. Google nu folosește IndexNow, deci sitemap-ul trebuie trimis în continuare în Google Search Console.

#### 2. Funcționalități Cheie

- **Fișier-cheie servit de Odoo:** cheia care dovedește că site-ul este al dumneavoastră se generează la activarea IndexNow și este servită la `https://<domeniu>/<cheie>.txt`; se poate lipi și o cheie existentă (8–128 litere, cifre sau cratime).
- **Doar ce s-a schimbat, la fiecare oră:** o acțiune programată trimite paginile publicate modificate de la ultima rulare, inclusiv conținutul editat în website builder, plus produsele, articolele de blog, evenimentele, joburile și cursurile publicate din aplicațiile instalate.
- **Tot, la cerere:** *Send all pages now* trimite o dată toate paginile publicate, după prima configurare sau după o modificare mare.
- **Rezultat la vedere:** în setări apar data/ora și rezultatul ultimei trimiteri, cu mesaje clare când fișierul-cheie nu e găsit sau URL-urile nu aparțin domeniului.
- **O cheie per website:** în bazele multi-website fiecare domeniu are cheia proprie și trimite doar paginile proprii.
- **Configurare:** se setează *Domain* pe website, apoi *Website > Configuration > Settings*, secțiunea *Tracking & SEO*: se bifează *IndexNow*, se salvează, se verifică fișierul prin *View key file* (trebuie să afișeze doar cheia) și se apasă o dată *Send all pages now*.
- **Date trimise:** doar adresele paginilor deja publice, domeniul și cheia. Fluxul pas-cu-pas, cu capturi, este în fișa consultantului.

#### 3. Dependențe

- `website`

#### 4. Componente Cheie

**Modele**

- `website` (extins): câmpuri `indexnow_enabled`, `indexnow_key`, `indexnow_key_url`, `indexnow_last_submit`, `indexnow_last_run`, `indexnow_last_result`; generează/validează cheia, colectează URL-urile publicate (`_indexnow_get_urls`), le trimite (`_indexnow_submit`) și rulează ciclul (`_indexnow_run`, `_cron_indexnow`).
- `res.config.settings` (extins): expune setările IndexNow și acțiunea `action_indexnow_submit_all` („Send all pages now").
- `ir.http` (extins): prin `_serve_fallback` servește `/<cheie>.txt` ca text simplu, fără a ascunde alte fișiere `.txt` ale site-ului.

**Vizualizări**

- `res_config_settings_view_form`: moștenește setările Website și adaugă opțiunea IndexNow, cheia, linkul *View key file* și butonul de trimitere.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_indexnow` (*Website: IndexNow*): rulează din oră în oră `model._cron_indexnow()` pe `website` și trimite paginile modificate de la ultima trimitere reușită.

#### 5. Conexiuni

- [deltatech_website_seo](../deltatech_website_seo/index.md): completează optimizarea SEO (date structurate pentru Google) cu notificarea rapidă a celorlalte motoare de căutare.
