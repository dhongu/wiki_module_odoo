# Terrabit IAP AI (localizat la `terrabit_iap_ai/index.md`)

- **Nume Tehnic:** `terrabit_iap_ai`
- **Versiune:** `20.0.2.0.2`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/20.0/terrabit_iap_ai
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_ai`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Direcționează AI-ul nativ din Odoo 20 (chat, agenți, câmpuri AI, acțiuni server AI din Enterprise `ai`) prin serverul IAP Terrabit în loc de serverul Odoo AI, astfel încât consumul AI să fie facturat în credite Terrabit. Instalarea nu schimbă furnizorul: AI-ul rămâne pe Odoo până când un administrator alege Terrabit.

#### 2. Funcționalități Cheie

- Setarea **AI Provider** (Odoo / Terrabit) în *Setări > General Settings > IAP Client*; alegerea Terrabit mută conturile IAP `odoo_ai` și parametrul `ai.endpoint` pe serverul Terrabit, iar revenirea la Odoo șterge `ai.endpoint`.
- Endpoint implicit `https://terrabit.odoo.com`, modificabil dacă Terrabit indică altul.
- Buton **Register AI Account** care înregistrează contul `odoo_ai` al companiei curente (se repetă în fiecare companie); serverul leagă contul de client prin CUI, deci compania trebuie să aibă CUI completat.
- Furnizorul este global (`ai.endpoint`), valabil pentru toate companiile bazei.
- Răspunsurile din chat vin prin webhook `/ai/completion_result_ready`, deci baza trebuie să fie accesibilă din internet; pentru baze locale se setează `ai.use_webhook` pe `False`.
- Domeniu curent (etapa 1): completări text cu unelte, sincron și asincron; embeddings, transcriere, generare de imagini și căutare web cer încă serverul Odoo AI.
- Codul AI al Odoo nu este suprascris. Nu are fișă de consultant.

#### 3. Dependențe

- `ai`
- [terrabit_iap](../terrabit_iap/index.md)

#### 4. Componente Cheie

**Modele**

- `iap.account` (extins): sincronizează/șterge `ai.endpoint` pentru conturile `odoo_ai`.
- `res.config.settings` (extins): `terrabit_ai_provider`, `terrabit_ai_endpoint`, acțiunea de înregistrare a contului AI.

**Vizualizări**

- `res_config_settings_view_form`: blocul AI Provider din setări.

**Acțiuni Automate / Acțiuni Server**

- Niciuna. Există o migrare `pre-migrate` pentru versiunea 20.0.2.0.0.

#### 5. Conexiuni

- [terrabit_iap](../terrabit_iap/index.md): clientul IAP Terrabit pe care se sprijină conturile.
- [terrabit_helpdesk_ai_reply](../terrabit_helpdesk_ai_reply/index.md): agentul Tibi poate folosi acest furnizor AI.
