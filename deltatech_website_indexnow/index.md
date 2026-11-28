# Website IndexNow (localizat la `deltatech_website_indexnow/index.md`)

- **Nume Tehnic:** `deltatech_website_indexnow`
- **Versiune:** `20.0.1.0.0`
- **Cale:** [https://github.com/dhongu/deltatech/tree/20.0/deltatech_website_indexnow](https://github.com/dhongu/deltatech/tree/20.0/deltatech_website_indexnow)
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_indexnow`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul anunță motoarele de căutare din protocolul [IndexNow](https://www.indexnow.org) (Bing, Yandex, Seznam, Naver) care pagini ale website-ului au fost publicate sau modificate, pentru ca acestea să le reindexeze în câteva minute. Bing alimentează și căutarea web din ChatGPT și Copilot. Google nu folosește IndexNow, deci sitemap-ul rămâne de trimis în Google Search Console.

#### 2. Funcționalități Cheie

- **Fișier cheie servit de Odoo**: cheia care dovedește că site-ul este al dumneavoastră se generează la activare și se servește la `https://<domeniu>/<cheie>.txt`; se poate lipi și o cheie existentă (8–128 litere, cifre sau cratime).
- **Doar ce s-a schimbat, din oră în oră**: o acțiune programată trimite paginile publicate modificate de la ultima rulare, inclusiv conținutul editat în website builder, plus produsele, articolele de blog, evenimentele, joburile și cursurile publicate din aplicațiile instalate.
- **Tot, la cerere**: *Send all pages now* trimite o dată toate paginile publicate, după prima configurare sau după o modificare mare.
- **Rezultat la vedere**: setările arată ora și rezultatul ultimei trimiteri, cu mesaj clar când fișierul cheie nu este găsit sau URL-urile nu aparțin domeniului.
- **O cheie per website**: pe o bază multi-website fiecare domeniu are cheia proprie și trimite doar paginile proprii.
- Configurare: se setează *Domain* pe website, apoi în *Website > Configuration > Settings*, secțiunea *Tracking & SEO*, se bifează *IndexNow*; *View key file* trebuie să afișeze doar cheia.
- Datele trimise: doar adresele paginilor deja publice, domeniul și cheia. Pașii detaliați, cu capturi, sunt în fișa consultant.

#### 3. Dependențe

- `website`

#### 4. Componente Cheie

**Modele**

- `website` (extins): `indexnow_enabled`, `indexnow_key`, `indexnow_key_url`, `indexnow_last_submit`, `indexnow_last_run`, `indexnow_last_result` și logica de trimitere (`_cron_indexnow`).
- `res.config.settings` (extins): câmpurile din setări legate de website.
- `ir.http` (extins): servirea fișierului cheie `<cheie>.txt`.

**Vizualizări**

- `views/res_config_settings_views.xml`: setarea IndexNow în secțiunea *Tracking & SEO*.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_indexnow` (*Website: IndexNow*): rulează din oră în oră și trimite paginile modificate de la ultima trimitere reușită.

#### 5. Conexiuni

- `website`: modulul de bază al site-ului ale cărui pagini sunt trimise.
- [deltatech_website_llms_txt](../deltatech_website_llms_txt/index.md): îmbunătățește vizibilitatea website-ului pentru asistenții AI, complementar IndexNow.
