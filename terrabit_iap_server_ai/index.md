# Terrabit IAP Server AI (localizat la `terrabit_iap_server_ai/index.md`)

- **Nume Tehnic:** `terrabit_iap_server_ai`
- **Versiune:** `20.0.1.2.0`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/20.0/terrabit_iap_server_ai
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_server_ai`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Adaugă un serviciu AI pe serverul Terrabit IAP, astfel încât clienții conectați să folosească funcții AI prin server, fără să configureze un furnizor AI pe fiecare bază. AI-ul nativ din Odoo 20 (modulul Enterprise `ai`) trimite fiecare cerere la endpoint-ul din parametrul de sistem `ai.endpoint`; acest modul servește acel protocol, deci agenții, câmpurile și acțiunile AI ale clientului rulează pe credite Terrabit.

#### 2. Funcționalități Cheie

- **Rute Odoo AI**: `/api/odoo_ai/1/get_completions_sync` răspunde în aceeași cerere; `/api/odoo_ai/1/get_completions` acceptă cererea imediat și trimite rezultatul mai târziu la webhook-ul `/ai/completion_result_ready` al clientului, semnat cu secretul per cerere.
- **Traducere către OpenAI Responses API**: text, imagini și PDF-uri în conversație, apeluri de funcții, ieșire structurată (JSON schema) și „Think longer" (efort de raționament mai mare). Căutarea web și generarea de imagini sunt refuzate deocamdată cu un mesaj clar.
- **Credite**: fiecare cerere rezervă o estimare (dimensiunea intrării plus ieșirea maximă) și captează costul real după răspuns, din numărul de tokeni și prețurile per milion de tokeni ale serviciului, cu un minim per cerere. La sold insuficient clientul primește notificarea standard *Not enough credits* cu linkul de cumpărare; o cerere eșuată nu costă nimic.
- **Jurnal**: fiecare cerere apare în *IAP > AI Requests* (eticheta de utilizare, model, tokeni, credite, starea livrării webhook-ului); conversația se șterge după procesare.
- **Configurare**: în *IAP > IAP Service* > **Odoo AI**, grupul *OpenAI* (cheia API, modelul — implicit `gpt-5-mini` — și **Reasoning Effort**, *None* pentru modele fără raționament) și grupul *Pricing* (credite per milion de tokeni de intrare și ieșire, minim per cerere). Pe client se orientează contul IAP `odoo_ai` spre acest server cu modulul `terrabit_iap_ai`.

#### 3. Dependențe

- `iap`
- [terrabit_iap_server](../terrabit_iap_server/index.md)

#### 4. Componente Cheie

**Modele**

- `iap.server.ai.request`: jurnalul cererilor AI (model, tokeni, credite, livrare webhook).
- `iap.server.service` (extins): câmpurile OpenAI și de preț ale serviciului AI.
- `iap.server.account` (extins): legătura contului cu cererile AI.

**Vizualizări**

- `view_iap_server_ai_request_form` / `_list` / `_search`: cererile AI.
- `view_iap_server_service_form` (moștenit): grupurile *OpenAI* și *Pricing*.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_process_ai_requests`: procesează cererile asincrone și livrările webhook.
- Servicii predefinite: `iap_server_service_ai` și `iap_server_service_odoo_ai`.

#### 5. Conexiuni

- [terrabit_iap_server](../terrabit_iap_server/index.md): serverul IAP pe care se adaugă serviciul.
- [terrabit_iap](../terrabit_iap/index.md): clientul IAP.
- `terrabit_iap_ai`: modulul client care îndreaptă contul `odoo_ai` spre acest server.
