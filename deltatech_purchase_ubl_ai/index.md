# Purchase UBL AI Product Matching

- **Nume Tehnic:** `deltatech_purchase_ubl_ai`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_purchase_ubl_ai
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_purchase_ubl_ai`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Importul facturilor de la furnizori (UBL / e-Factura) potrivește deja majoritatea liniilor cu un produs. Acest modul preia doar liniile rămase nepotrivite (descrieri prescurtate, diacritice lipsă, cod nou de furnizor) și întreabă un agent AI ce produs este. Sugestia e validată mereu de o persoană, iar după validare codul și descrierea furnizorului sunt reținute, așa că factura următoare se potrivește fără AI.

#### 2. Funcționalități Cheie

- **AI doar unde contează**: potrivirea deterministă rulează prima; AI e întrebat o singură dată pe factură, doar despre liniile nepotrivite.
- **Fără produse inventate**: agentul alege dintr-o listă de candidați construită în Odoo (liniile comenzii, lista de prețuri a furnizorului, produse cu cuvinte comune); un răspuns din afara listei e ignorat.
- **Verificări în cod**: unitatea de măsură trebuie să fie compatibilă cu produsul, iar un preț departe de ultimul preț de achiziție înjumătățește încrederea și e semnalat.
- **Validare umană**: în previzualizarea importului (buton *Import UBL* pe comanda de achiziție) sugestia apare precompletată, în albastru, cu încredere și motiv. Importul automat (ex. descărcarea din SPV) doar înregistrează sugestiile pe comandă, în spatele butonului **AI Suggestions** (și meniul *Purchase → Orders → AI Product Suggestions*); **Validate** actualizează linia și prețul, **Discard** lasă linia pentru tratare manuală. Factura nu se creează cât timp există linii nerezolvate.
- **Învață din validări**: codul și descrierea furnizorului se scriu pe lista de prețuri a furnizorului; un cod deja folosit pentru alt produs nu se suprascrie.
- **Cost controlat**: activare opțională pe companie (*Settings → Purchase → Invoicing → AI Product Matching*), limită zilnică de apeluri AI (implicit 50, 0 = nelimitat) și încredere minimă (implicit 0,6).
- **Furnizorul tău AI**: framework-ul AI nativ Odoo și cheia din **Settings → AI**; agentul *Purchase Product Matching AI* (**AI → Agents**) poate fi ajustat (model, instrucțiuni traductibile).

#### 3. Dependențe

- [deltatech_purchase_ubl](../deltatech_purchase_ubl/index.md)
- `ai`

#### 4. Componente Cheie

**Modele**

- `purchase.ubl.ai.suggestion`: sugestia AI pentru o linie nepotrivită (produs, încredere, motiv, stare).
- `ai.agent` (extins): agentul de potrivire a produselor.
- `purchase.order`, `purchase.invoice.import.mixin`, `purchase.ubl.import.wizard` și `purchase.ubl.import.wizard.line` (extinse): integrarea sugestiilor în import.
- `res.company`, `res.config.settings` (extinse): activarea, limita zilnică și încrederea minimă.

**Vizualizări**

- `views/purchase_ubl_ai_suggestion_views.xml`: lista/formularul sugestiilor.
- `views/purchase_order_views.xml`: butonul **AI Suggestions** pe comandă.
- `views/ubl_import_wizard_views.xml`: liniile albastre din previzualizare.
- `views/res_config_settings_views.xml`: setările.

**Acțiuni Automate / Acțiuni Server**

- `ai_agent_purchase_product_matching` (`data/ai_agent_data.xml`): agentul AI furnizat de modul.

#### 5. Conexiuni

- [deltatech_ai_anthropic](../deltatech_ai_anthropic/index.md): permite folosirea Claude ca furnizor AI.
