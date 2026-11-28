# Portal Clienți B2B

- **Nume Tehnic:** `deltatech_b2b_portal`
- **Versiune:** `20.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_b2b_portal
- **Cale Locală:** `odoo-addons/bitshop/deltatech_b2b_portal`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Portal pentru clienții companie pe website-ul Odoo: firmele cer un cont dintr-o pagină publică, un agent de vânzări îl aprobă dintr-un clic, iar apoi fiecare contact al firmei vede în portal ce contează pentru un cumpărător business: soldul, facturile restante, creditul disponibil și agentul de vânzări. Este baza familiei B2B Terrabit; comanda rapidă, listele salvate și treptele de preț sunt module separate construite deasupra.

#### 2. Funcționalități Cheie

- Pagina publică `/b2b` cu formularul de cerere de cont (firmă, CUI, registrul comerțului, adresă, persoană de contact), cu capcană anti-spam și, opțional, acceptarea termenilor B2B; email opțional de confirmare și limită de 5 cereri pe oră de la aceeași adresă.
- Cererea este chiar clientul: se creează firma în starea *Solicitat*, cu contactul sub ea, și o activitate pentru agent; potrivirea se face după CUI (`RO 1234 5678` și `12345678` sunt aceeași firmă), iar datele unui vizitator anonim nu suprascriu un client existent.
- Aprobare dintr-un clic (contactele care au cerut acces primesc invitația standard de portal) și respingere cu motiv obligatoriu, cu opțiunea de arhivare pentru cereri false.
- Stare cont B2B pe firmă (solicitat, activ, suspendat, respins) și rol pe contact: *Poate comanda* sau *Doar vizualizare*; liste în *Vânzări ▸ Comenzi ▸ Cereri cont B2B* și *Clienți B2B*; activarea unui client existent prin *Acțiune ▸ Activează cont B2B*.
- Tablou de bord pe `/my`: sold, restanțe, credit disponibil cu bară de utilizare, oferte în așteptare, facturi de plată cu zilele de întârziere și agentul de vânzări.
- Protecție la comandă: un contact doar cu vizualizare sau un cont suspendat nu poate finaliza coșul și nici semna o ofertă în portal.
- Opțional, per website, prețuri doar pentru clienții companie: catalogul rămâne public și indexat, dar vizitatorul fără cont B2B activ nu vede preț, stoc, filtru de preț și nici *Adaugă în coș*; prețurile sunt excluse de server, inclusiv din feed-ul Google Merchant.
- Setări în *Website ▸ Configurare ▸ Setări ▸ Portal B2B* (agentul pentru cereri, termenii B2B, prețuri doar pentru companii); drepturi *Portal B2B ▸ Utilizator* și *Administrator*.
- Nu include aprobarea comenzilor colegilor și completarea automată din registre publice (planificate). Fluxul pas cu pas este în fișa consultantului.

#### 3. Dependențe

- `website_sale`
- `sale_management`

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins): starea contului B2B, rolul contactului, soldul, restanțele, creditul disponibil, aprobare/respingere/suspendare.
- `res.config.settings` și `website` (extinse): setările portalului B2B și opțiunea de prețuri doar pentru companii.
- `product.template`, `product.product`, `product.feed` (extinse): ascunderea prețului și a stocului pentru cei fără cont B2B activ.
- `website.checkout.step` (extins): blocarea finalizării pentru contactele fără drept de comandă.

**Vizualizări**

- `view_partner_form_b2b`: tabul *B2B* al clientului, cu butoanele *Aprobă* și *Respinge*.
- `view_partner_b2b_request_list` / `action_b2b_requests`: lista cererilor de cont.
- `view_partner_b2b_customer_list` / `action_b2b_customers`: lista clienților B2B.
- `view_b2b_reject_wizard_form`: fereastra de respingere cu motiv.
- `view_res_partner_filter_b2b`: filtrele de căutare B2B.
- `res_config_settings_view_form`: blocul *Portal B2B* din setări.

**Acțiuni Automate / Acțiuni Server**

- `action_server_b2b_activate`: activează contul B2B al unui client existent.
- `mail_activity_type_b2b_request`: tipul de activitate *Cerere cont B2B* pentru agent.
- `mail_template_b2b_request_received`: emailul de confirmare a cererii.

#### 5. Conexiuni

- [deltatech_b2b_announcement](../deltatech_b2b_announcement/index.md): anunțuri datate pe pagina `/my`.
- [deltatech_b2b_price_tier](../deltatech_b2b_price_tier/index.md): prețul pe cantitate în pagina de produs.
- [deltatech_b2b_website_restrict](../deltatech_b2b_website_restrict/index.md): website închis vizitatorilor.
- [terrabit_partner_credit_limit](../terrabit_partner_credit_limit/index.md) și [terrabit_partner_credit_limit_website](../terrabit_partner_credit_limit_website/index.md): aplică limita de credit și restanțele pe website; portalul doar le afișează.
