# AI - Agent Delegation (localizat la `deltatech_ai_agent_delegate/index.md`)

- **Nume Tehnic:** `deltatech_ai_agent_delegate`
- **Versiune:** `20.0.2.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_ai_agent_delegate
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_agent_delegate`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

În Odoo 20 Enterprise un agent AI poate consulta nativ alți agenți: **Allowed Agents** (fila *Skills* a agentului) pornesc ca sub-sesiuni, fiecare cu sursele, instrucțiunile și modelul propriu. Modulul păstrează pe această bază configurarea și comportamentul versiunii Odoo 19, astfel încât agentul integrator să continue să consulte aceiași specialiști, iar linkurile din răspunsuri să fie clicabile.

#### 2. Funcționalități Cheie

- **Specialiștii devin Allowed Agents**: la upgrade-ul unei baze din Odoo 19, **Specialist Agents** ai fiecărui agent se adaugă la **Allowed Agents**; subiectul *Specialist Agents* și unealta *AI: Ask a Specialist Agent* nu mai sunt necesare și se elimină.
- **Linkuri clicabile**: URL-urile scrise ca text simplu în răspunsurile finale ale agenților (de exemplu copiate din răspunsul unui agent permis) devin linkuri, lucru pe care conversia Markdown standard îl lasă ca text.
- **Bază nouă Odoo 20**: modulul adaugă doar linkurile clicabile; agenții permiși se aleg direct în câmpul standard.
- **Utilizare**: în *AI > Agents* fiecare agent consultat primește un **subtitlu** clar (integratorul alege pe cine întreabă după nume și subtitlu); în agentul integrator, fila **Skills**, se verifică **Allowed Agents**; o întrebare care acoperă mai multe domenii pornește câte o sesiune cu fiecare agent permis, iar integratorul răspunde o singură dată.

#### 3. Dependențe

- `ai_agentic`

#### 4. Componente Cheie

Secțiunea nu este detaliată: documentația se bazează pe `readme/DESCRIPTION.md`, care nu solicită explicit analiza componentelor tehnice (modele, vizualizări, acțiuni automate). Din cod: extinderea modelului `ai.session` (metoda `_format_final_message` transformă URL-urile simple în autolinkuri Markdown, fără a atinge codul). Modulul nu are vizualizări sau acțiuni programate.

#### 5. Conexiuni

- `deltatech_ai_financial_analysis`: agentul Plutus poate primi un agent specialist de contabilitate prin delegare (vezi pagina [deltatech_ai_financial_analysis](../deltatech_ai_financial_analysis/index.md)).
