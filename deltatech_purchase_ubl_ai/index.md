# Purchase UBL AI Product Matching (localizat la `deltatech_purchase_ubl_ai/index.md`)

- **Nume Tehnic:** `deltatech_purchase_ubl_ai`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_purchase_ubl_ai
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_purchase_ubl_ai`
- **Ultima Ingestie:** `2026-10-20`

#### 1. Sumar

Importul facturilor de la furnizori (UBL / e-Factura) recunoaște deja majoritatea liniilor după cod de bare, cod furnizor, referință internă sau denumire exactă. Acest modul se ocupă de restul: pentru liniile pe care potrivirea standard din *Purchase UBL* nu le-a putut asocia (descrieri abreviate, diacritice lipsă, cod nou de furnizor), un agent AI propune produsul, iar o persoană validează întotdeauna sugestia. După validare, codul și descrierea furnizorului sunt memorate, astfel încât factura următoare se potrivește fără AI.

#### 2. Funcționalități Cheie

- **AI doar unde contează:** potrivirea deterministă rulează prima, gratuit; AI-ul este întrebat o singură dată per factură, doar pentru liniile nepotrivite.
- **Fără produse inventate:** agentul alege dintr-o listă de candidați construită în Odoo (liniile comenzii, lista de prețuri a furnizorului, produse cu cuvinte comune în descriere); un răspuns din afara listei este ignorat.
- **Verificări în cod:** unitatea de măsură a liniei trebuie să fie compatibilă cu produsul, iar un preț departe de ultimul preț de achiziție înjumătățește încrederea și este semnalat.
- **Validare umană obligatorie:** în previzualizarea importului sugestia este precompletată (albastru, cu încredere și motiv) și se confirmă odată cu importul. Importul automat (ex. descărcarea din SPV) doar înregistrează sugestiile pe comanda de achiziție, în spatele butonului **AI Suggestions**; factura furnizor nu se creează cât timp există linii nerezolvate și se programează activitatea „SPV import needs review”.
- **Învață din fiecare validare:** codul și descrierea furnizorului se scriu în lista de prețuri a furnizorului; un cod deja folosit de furnizor pentru alt produs nu este suprascris. La validare linia se actualizează sau se adaugă pe comandă și se actualizează prețul furnizorului. **Discard** lasă linia pentru tratare manuală.
- **Cost controlat:** activare opt-in per companie (implicit dezactivat), limită zilnică de apeluri AI (implicit 50, 0 = nelimitat) și încredere minimă (implicit 0,6). O factură reprocesată nu este retrimisă.
- **Furnizorul tău de AI:** folosește framework-ul AI nativ Odoo și cheia din **Setări → AI** (OpenAI, Gemini sau Claude prin `deltatech_ai_anthropic`).
- **Configurare:** **Setări → Achiziții → Facturare → AI Product Matching**; agentul **Purchase Product Matching AI** (AI → Agents) permite schimbarea modelului și rafinarea instrucțiunilor (traductibile).
- **Meniu:** Achiziții → Comenzi → AI Product Suggestions (lista tuturor sugestiilor).

#### 3. Dependențe

- [deltatech_purchase_ubl](../deltatech_purchase_ubl/index.md)
- `ai` (Odoo Enterprise)

#### 4. Componente Cheie

**Modele**

- `purchase.ubl.ai.suggestion`: sugestie AI per linie de factură nepotrivită, cu încredere, motiv și acțiuni Validate / Discard.
- `ai.agent` (extins): agentul de potrivire a produselor.
- `purchase.order` (extins): buton și acces la sugestiile AI.
- `purchase.invoice.import.mixin` (extins): declanșează potrivirea AI pentru liniile nerezolvate.
- `purchase.ubl.import.wizard` / `purchase.ubl.import.wizard.line` (extinse): afișarea sugestiilor în previzualizare.
- `res.company` / `res.config.settings` (extinse): activare, limită zilnică, încredere minimă.

**Vizualizări**

- `purchase_ubl_ai_suggestion_view_list`, `_view_form`, `_view_search`: gestionarea sugestiilor.
- `purchase_order_form_view_inherit_ubl_ai`: butonul **AI Suggestions** pe comanda de achiziție.
- `view_purchase_ubl_import_wizard_inherit_ai`: linii albastre în previzualizarea importului.
- `res_config_settings_view_form_purchase_ubl_ai`: setările modulului.

**Acțiuni Automate / Acțiuni Server**

- `ai_agent_purchase_product_matching` (date `ai.agent`): agentul AI implicit; nu există cron-uri sau acțiuni server.

#### 5. Conexiuni

- [deltatech_ai_anthropic](../deltatech_ai_anthropic/index.md): permite folosirea Claude ca furnizor AI.
