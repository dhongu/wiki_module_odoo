# Romania - Bonitatea partenerilor pentru Plutus (AI)

- **Nume Tehnic:** `l10n_ro_ai_partner_financials`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_ai_partner_financials
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_ai_partner_financials`
- **Ultima Ingestie:** `2026-10-27`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă lui **Plutus**, agentul AI de analiză financiară, o unealtă de evaluare a bonității partenerilor (clienți sau furnizori). Pe baza bilanțurilor publice de la Ministerul Finanțelor, deja preluate în Odoo, agentul poate răspunde la întrebări de tipul „ce bonitate are clientul cu CUI ...?” și poate evidenția clienții mari cu creanțe restante și bonitate slabă. Unealta doar citește datele existente, nu interoghează MFinanțe în timpul conversației.

#### 2. Funcționalități Cheie

- **Unealta „Bonitatea partenerului”** în chatul lui Plutus: căutare după cod fiscal (cu sau fără prefixul RO) sau după nume; întoarce pe ani cifra de afaceri, rezultatul net, capitalurile proprii, datoriile, numărul de salariați, lichiditatea, solvabilitatea, îndatorarea, marja netă și rentabilitatea capitalurilor proprii, împreună cu data preluării. Dacă numele se potrivește la mai mulți parteneri, îi listează (maximum 10) și cere codul fiscal. Se pot cere până la 10 ani.
- **Semnale de risc calculate în Python**, nu de agentul AI: capitaluri proprii negative (Legea 31/1990, art. 153^24), pierdere netă, scăderea cifrei de afaceri cu cel puțin 20% față de anul precedent și date vechi (cel mai recent bilanț disponibil nu e preluat).
- **Vechimea creanțelor cu bonitate**: în unealta de vechime a creanțelor, clienții mari din listă primesc pe linie semnalele lor de risc.
- **Doar citire**: dacă bilanțul lipsește, agentul spune asta și trimite la butonul MFinanțe de pe fișa partenerului (sau la cronul din `l10n_ro_partner_financials`).
- **Integrare MCP**: aceeași unealtă, `mcp_fa_partner_credit` (argumente `partner` și `years`), poate fi expusă prin serverul MCP, adăugând metoda modelului `financial.analysis` în politica serverului.
- **Topic AI dedicat** („Partner Credit (Romania)”) cu instrucțiuni pentru agent: cifrele și semnalele se prezintă exact cum le întoarce unealta, cu anul bilanțului și data preluării, fără rating propriu sau probabilitate de insolvență. Topicul este atașat lui Plutus la instalare.
- Fluxul pas-cu-pas, cu capturi, este în [Fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- [l10n_ro_partner_financials](../l10n_ro_partner_financials/index.md)
- [deltatech_ai_financial_analysis](../deltatech_ai_financial_analysis/index.md)

#### 4. Componente Cheie

**Modele**

- `financial.analysis` (extins): adaugă metoda `_fa_tool_partner_credit` și metoda MCP `mcp_fa_partner_credit`, căutarea partenerilor după CUI/nume, calculul semnalelor de risc (`_credit_signals`) și completarea uneltei de vechime a creanțelor (`_fa_tool_aging`) cu semnalele de risc.

**Vizualizări**

- Modulul nu adaugă vizualizări.

**Acțiuni Automate / Acțiuni Server**

- `ir_actions_server_fa_partner_credit`: acțiune server (cod) „AI: Partner Credit (Public Balance Sheets)”, expusă ca unealtă AI.
- `ai_topic_partner_credit`: topicul AI cu instrucțiunile uneltei; `post_init_hook` îl atașează agentului Plutus (acesta fiind `noupdate`).

#### 5. Conexiuni

- [l10n_ro_partner_financials](../l10n_ro_partner_financials/index.md): sursa bilanțurilor publice MFinanțe (buton pe fișa partenerului și cron de preluare).
- [deltatech_mcp_server](../deltatech_mcp_server/index.md): expune unealta `mcp_fa_partner_credit` prin MCP.
- [deltatech_financial_analysis](../deltatech_financial_analysis/index.md): modelul `financial.analysis` și uneltele de bază (inclusiv vechimea creanțelor), extinse aici.
