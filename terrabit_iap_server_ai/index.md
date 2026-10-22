# Terrabit IAP Server AI (localizat la `terrabit_iap_server_ai/index.md`)

- **Nume Tehnic:** `terrabit_iap_server_ai`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_iap_server_ai
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_server_ai`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Modulul adaugă un serviciu de inteligență artificială (AI) în serverul IAP Terrabit. Clienții conectați folosesc funcțiile AI prin serverul IAP, în loc să configureze un furnizor AI pe fiecare instanță, iar consumul se plătește din credite Terrabit. Include și suport pentru AI-ul nativ din Odoo 20, ale cărui cereri sunt servite de acest server. Modulul are starea de dezvoltare „Beta".

#### 2. Funcționalități Cheie

- **AI nativ Odoo 20.** Clientul își îndreaptă `ai.endpoint` către serverul IAP, iar agenții AI, câmpurile AI și acțiunile server AI rulează pe creditele Terrabit. Serverul expune două rute:
  - `/api/odoo_ai/1/get_completions_sync` răspunde în aceeași cerere;
  - `/api/odoo_ai/1/get_completions` acceptă cererea imediat și trimite rezultatul ulterior la webhook-ul `/ai/completion_result_ready` al clientului, semnat cu secretul per cerere.
- **Traducere către OpenAI Responses API:** text, imagini și PDF în conversație, apeluri de unelte (function calling), ieșire structurată (JSON schema) și „Think longer" (efort de raționament mai mare). Căutarea web și generarea de imagini sunt refuzate deocamdată cu un mesaj clar.
- **Credite.** Fiecare cerere rezervă o estimare (dimensiunea intrării plus ieșirea maximă) și consumă costul real după răspunsul furnizorului, din numărul de tokeni și prețurile per milion de tokeni setate pe serviciu, cu un minim per cerere. La sold insuficient clientul primește notificarea standard „Not enough credits", cu link de cumpărare. O cerere eșuată nu costă nimic.
- **Jurnal.** Fiecare cerere apare în *IAP > AI Requests*, cu eticheta de utilizare, modelul, tokenii, creditele și starea livrării webhook-ului; conversația se șterge după procesare.
- **Configurare** (*IAP > IAP Service > Odoo AI*): în grupul *OpenAI* se setează cheia API și modelul AI (implicit `gpt-5-mini`; efortul de raționament se pune pe *None* pentru modele fără raționament); în grupul *Pricing*, creditele per milion de tokeni de intrare/ieșire și minimul per cerere. Pe clientul Odoo 20, contul `odoo_ai` se îndreaptă către server cu modulul `terrabit_iap_ai` și se înregistrează.
- Serviciul generic „AI" (cod `ai`) rămâne disponibil în lista de servicii, ca orice alt serviciu al serverului IAP.

#### 3. Dependențe

- `iap`
- [terrabit_iap_server](../terrabit_iap_server/index.md)

#### 4. Componente Cheie

**Modele**

- `iap.server.service` (extins): adaugă codurile `ai` și `odoo_ai` în `service_code` și câmpurile de configurare AI (cheie OpenAI, model, efort de raționament, tokeni maximi de ieșire, timeout furnizor, credite per 1M tokeni intrare/ieșire, credit minim).
- `iap.server.ai.request`: jurnalul cererilor AI (UUID, cont, tranzacție, mod sync/webhook, stare, utilizare, model, tokeni, credite, eroare, date webhook).

**Vizualizări**

- `view_iap_server_service_form` (moștenire): grupurile *OpenAI* și *Pricing* pe formularul serviciului.
- `view_iap_server_ai_request_form`, `view_iap_server_ai_request_list`, `view_iap_server_ai_request_search`: formular, listă și căutare pentru cererile AI.
- `action_iap_server_ai_request`: acțiunea „AI Requests" din meniul IAP.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_process_ai_requests`: procesează cererile asincrone în așteptare (la 5 minute, ca plasă de siguranță; ruta `get_completions` îl declanșează imediat) și închide cererile rămase `running` peste 30 de minute, eliberând creditele și anunțând clientul.
- Date: serviciile `iap_server_service_ai` (cod `ai`) și `iap_server_service_odoo_ai` (cod `odoo_ai`).
- Cod: furnizorul `providers/openai_responses.py` (traducerea cererilor către OpenAI Responses API).

#### 5. Conexiuni

- [terrabit_iap_ai](../terrabit_iap_ai/index.md): modulul client care îndreaptă contul `odoo_ai` către acest server.
- [terrabit_iap_server_helpdesk](../terrabit_iap_server_helpdesk/index.md): alt serviciu adăugat peste același server IAP.
- [terrabit_iap_server_sale](../terrabit_iap_server_sale/index.md): alt serviciu adăugat peste același server IAP.
