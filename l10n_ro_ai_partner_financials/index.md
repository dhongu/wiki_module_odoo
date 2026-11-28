# Romania - Bonitatea partenerilor pentru Plutus (AI) (localizat la `l10n_ro_ai_partner_financials/index.md`)

- **Nume Tehnic:** `l10n_ro_ai_partner_financials`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_ai_partner_financials
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_ai_partner_financials`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaugă o unealtă de bonitate a partenerilor pentru Plutus, agentul AI de analiză financiară, și pentru serverul MCP. Folosește bilanțurile publice MFinanțe deja preluate și arată, pe ani, indicatorii și semnalele de risc ale unui partener, astfel încât clienții mari cu bonitate slabă să fie observați din timp.

#### 2. Funcționalități Cheie

- Unealta *Bonitatea partenerului* în chatul lui Plutus: după cod fiscal (cu sau fără RO) sau după nume, întoarce pe ani cifra de afaceri, rezultatul net, capitalurile proprii, datoriile, salariații, lichiditatea, solvabilitatea, îndatorarea, marja netă și rentabilitatea capitalurilor proprii, cu data preluării. La nume ambiguu listează partenerii și cere codul fiscal.
- Semnale de risc calculate în Python, nu de agent: capitaluri proprii negative, capitaluri proprii sub jumătate din capitalul subscris vărsat (estimare din bilanțul public, nu constatare juridică), pierdere, scăderea cifrei de afaceri cu cel puțin 20% și date vechi.
- Vechimea creanțelor cu bonitate: în unealta de vechime a creanțelor, clienții mari primesc pe linie semnalele lor de risc.
- MCP: aceeași unealtă, `mcp_fa_partner_credit` (argumente `partner` și `years`), poate fi expusă prin serverul MCP.
- Doar citire: nu interoghează MFinanțe în timpul conversației; dacă bilanțul lipsește, trimite la butonul MFinanțe de pe fișa partenerului.
- Bilanțurile se preiau din fișa partenerului sau prin cronul din `l10n_ro_partner_financials`; detaliile sunt în fișa consultantului.

#### 3. Dependențe

- [l10n_ro_partner_financials](../l10n_ro_partner_financials/index.md)
- [deltatech_ai_financial_analysis](../deltatech_ai_financial_analysis/index.md)

#### 4. Componente Cheie

**Modele**

- `financial.analysis` (extins): unealta `_fa_tool_partner_credit`, calculul semnalelor de risc, metoda MCP `mcp_fa_partner_credit` și îmbogățirea uneltei de vechime a creanțelor (`_fa_tool_aging`).

**Vizualizări**

- Nu adaugă vizualizări; unealta apare în chatul lui Plutus.

**Acțiuni Automate / Acțiuni Server**

- `ir_actions_server_fa_partner_credit` (`ir.actions.server`): acțiunea serverului care expune unealta de bonitate.
- `ai_skill_partner_credit` (`ai.skill`): abilitatea lui Plutus pentru bonitatea partenerului, înregistrată la instalare (`post_init_hook`).

#### 5. Conexiuni

- [deltatech_mcp_server](../deltatech_mcp_server/index.md): expune unealta `mcp_fa_partner_credit` prin politica serverului MCP.
- [l10n_ro_ai_administrators_report](../l10n_ro_ai_administrators_report/index.md): altă extensie Plutus pentru contabilitate, fără dependență directă.
