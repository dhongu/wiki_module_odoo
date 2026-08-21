# Bank Reconciliation AI Fallback (localizat la `deltatech_bank_reconcile_ai/index.md`)

- **Nume Tehnic:** `deltatech_bank_reconcile_ai`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_bank_reconcile_ai
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_bank_reconcile_ai`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Reconcilierea bancară automată a Odoo rezolvă deja marea majoritate a liniilor din extrasul de cont. Modulul `deltatech_bank_reconcile_ai` intervine doar acolo unde mecanismul standard renunță — referințe deteriorate, parteneri lipsă sau comisioane bancare recurente — și cere unui agent AI o sugestie de potrivire sau de cont de contrapartidă. Contabilul rămâne mereu cel care decide: fiecare sugestie așteaptă o validare cu un singur clic, nimic nu se postează automat.

#### 2. Funcționalități Cheie

- AI folosit doar acolo unde aduce valoare: potrivirea deterministă standard (referință de plată, sumă, partener, modele de reconciliere) rulează prima, gratuit; AI-ul este întrebat doar despre liniile rămase nereconciliate.
- Două tipuri de sugestii: potrivirea cu o factură sau plată deschisă existentă, sau — când nimic nu se potrivește — propunerea contului de cheltuială/venit pentru o nouă înregistrare de contrapartidă (comisioane bancare, dobânzi).
- Validare umană, întotdeauna: sugestiile ajung într-o listă de revizuire (Contabilitate → Închidere → Sugestii de Reconciliere AI) cu scorul de încredere al AI-ului și o explicație în limbaj simplu; se validează sau se resping cu un clic, individual sau în masă.
- Acțiune „AI Suggestion" direct din widgetul nativ de reconciliere bancară Odoo Enterprise, pe orice linie de extras nereconciliată.
- Cost sub control: opțiune activabilă per companie (dezactivată implicit), cu o limită zilnică configurabilă a apelurilor AI, ca plasă de siguranță pe bugetul API.
- Plan de conturi propriu, regulile proprii: conturile pe care AI-ul le poate propune sunt scrise în instrucțiunile agentului, în limbaj simplu, editabile per bază de date, fără modificare de cod; conservator prin design — la orice îndoială, AI-ul refuză în loc să ghicească.
- Cunoștințe contabile localizate: instrucțiunile agentului sunt traductibile; traducerea în română este ajustată pentru planul de conturi românesc (OMFP 1802/2014 — 627 comisioane bancare, 666/766 dobânzi), iar AI-ul este adresat în limba companiei.
- Configurare minimă: folosește framework-ul oficial AI al Odoo și cheia OpenAI/Gemini existentă din Setări → AI, fără conector terț sau abonament separat.

**Cum funcționează:**

1. Cron-ul standard de auto-reconciliere rulează ca de obicei.
2. Pentru fiecare linie rămasă nereconciliată, agentul AI primește linia (dată, sumă, referință, partener) și o listă scurtă de note contabile deschise candidate.
3. Agentul răspunde într-un format strict, verificat automat: cea mai bună potrivire, un cont de contrapartidă din lista permisă, sau explicit „nimic plauzibil".
4. Contabilul revizuiește sugestiile în așteptare și le validează sau le respinge. Validarea reconciliază prin mecanismele standard Odoo — inclusiv taxe și modele de reconciliere automată.

#### 3. Dependențe

- `account_accountant`
- `ai`

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, care acoperă Sumarul și Funcționalitățile Cheie; componentele de mai jos sunt cele menționate explicit acolo, completate cu o scurtă trecere prin cod pentru precizie tehnică.

**Modele**

- `bank.statement.ai.suggestion`: modelul central al modulului — stochează o sugestie AI pentru o linie de extras (`statement_line_id`), tipul acesteia (`match` — potrivire cu o notă existentă, sau `counterpart` — cont nou de contrapartidă), scorul de încredere, explicația AI și starea (`pending`/`validated`/`discarded`); acțiunile `action_validate`/`action_discard` reconciliază linia prin mecanismele standard Odoo.
- `account.bank.statement.line` (extindere): adaugă `_ai_suggest_reconciliation()` ca fallback după `_try_auto_reconcile_statement_lines()` standard, și acțiunea `action_suggest_ai_match()` apelabilă manual din widgetul de reconciliere.
- `ai.agent` (extindere) și `res.company` (extindere): adaugă `bank_rec_ai_enabled` (activare per companie, dezactivat implicit) și `bank_rec_ai_daily_limit` (plafon zilnic de apeluri AI, 0 = fără limită).
- `res.config.settings` (extindere): expune opțiunile de mai sus în Setări → Contabilitate.

**Vizualizări**

- `bank_statement_ai_suggestion_views.xml`: lista/formularul de revizuire a sugestiilor AI (Contabilitate → Închidere → Sugestii de Reconciliere AI), cu scor de încredere, rationale AI și acțiuni de validare/respingere.
- `res_config_settings_views.xml`: secțiunea de configurare a fallback-ului AI (activare, limită zilnică) în setările de Contabilitate.
- `bank_statement_ai_bulk_validate_wizard_views.xml`: wizard pentru validarea în masă a mai multor sugestii AI simultan.

**Acțiuni Automate / Date**

- `data/ai_agent_data.xml`: creează la instalare agentul AI `ai_agent_bank_reconciliation` („Bank Reconciliation AI (fallback)"), cu promptul de sistem care descrie regulile de potrivire (MATCH/ACCOUNT/NOTHING) și lista de conturi permise pentru propuneri de contrapartidă (implicit 627, 666, 766 — editabilă per bază de date).

#### 5. Conexiuni

- `account_accountant`: modulul Enterprise de contabilitate al cărui widget de reconciliere bancară este extins cu acțiunea „AI Suggestion" și al cărui mecanism standard de auto-reconciliere este cel completat de acest fallback AI.
- `ai`: modulul Enterprise care furnizează infrastructura de agenți AI și conexiunea la furnizorul AI (OpenAI, Google Gemini etc.), folosită pentru a genera efectiv sugestiile de reconciliere.
