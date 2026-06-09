# Accounting Scenario AI Generator (localizat la `deltatech_account_scenario_ai/index.md`)

- **Nume Tehnic:** `deltatech_account_scenario_ai`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/bitshop_ent/tree/19.0/deltatech_account_scenario_ai
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_account_scenario_ai`
- **Ultima Ingestie:** `2026-06-09`

#### 1. Sumar

Modulul `deltatech_account_scenario_ai` extinde modulul `deltatech_account_scenario` adăugând generarea de scenarii contabile cu ajutorul inteligenței artificiale. Utilizatorul descrie un proces de afaceri în text simplu (de exemplu „achiziție de marfă de la furnizor, recepție în stoc, factură furnizor și plată"), iar Odoo folosește un agent AID dedicat pentru a genera automat o definiție JSON validă a scenariului, gata de a fi executată și validată de cadrul de scenarii. Astfel, crearea scenariilor contabile devine mult mai rapidă și accesibilă, eliminând necesitatea scrierii manuale a structurii JSON complexe.

#### 2. Funcționalități Cheie

- Generarea unui scenariu contabil în format JSON pornind de la o descriere în text liber a procesului de afaceri.
- Câmp suplimentar **AI Prompt** pentru instrucțiuni adiționale către AI (conturi specifice, sume, parteneri, reguli de validare).
- Buton **Generate with AI** pe fișa scenariului, vizibil când starea este `Draft` sau `Failed`, care trimite descrierea și promptul către agentul AI și completează automat câmpul `json_data`.
- Agent AI dedicat (`ai_agent_scenario_generator`), creat automat la instalare, configurat cu un prompt de sistem care îl direcționează să respecte strict documentația cadrului de scenarii.
- Sursă de cunoștințe atașată agentului: fișierul `USAGE.MD` din `deltatech_account_scenario`, încărcat ca `ir.attachment` și legat prin `source_ids`, conținând formatul JSON, toate cele 25 de tipuri de pași, descrierile câmpurilor, verificările (`checks`), `expected_account_moves` și un exemplu complet.
- Flux integrat cu cadrul de scenarii: după generare, JSON-ul poate fi revizuit, apoi marcat **Set Ready** și executat ca orice scenariu standard.

#### 3. Dependențe

- [deltatech_account_scenario](../deltatech_account_scenario/index.md)
- `ai`

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, modulul adaugă următoarele elemente menționate explicit:

**Modele (câmpuri și acțiuni adăugate)**

- Extinde modelul scenariului contabil din `deltatech_account_scenario` cu câmpul `ai_prompt` — instrucțiuni adiționale pentru AI (conturi, sume, parteneri, reguli de validare).
- Acțiune **Generate with AI**: trimite descrierea și promptul AI către agentul `ai_agent_scenario_generator` și populează câmpul `json_data` cu scenariul JSON returnat.

**Acțiuni Automate / Date**

- `data/ai_agent_data.xml`: creează automat la instalare agentul AI `ai_agent_scenario_generator`, împreună cu promptul de sistem și sursa de cunoștințe (`ai.agent.source`) bazată pe fișierul `USAGE.MD`.

#### 5. Conexiuni

- [deltatech_account_scenario](../deltatech_account_scenario/index.md): modulul de bază pe care îl extinde; furnizează cadrul de scenarii contabile (modelul scenariului, tipurile de pași, execuția și validarea) și fișierul de documentație `USAGE.MD` folosit ca sursă de cunoștințe pentru AI.
- `ai`: modulul Enterprise care oferă infrastructura de agenți AI și conexiunea la furnizorul AI (OpenAI, Google Gemini etc.), necesar pentru generarea efectivă a scenariilor.
