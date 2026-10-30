# Trial Balance PDF Import with AI (Import balanță din PDF cu AI)

- **Nume Tehnic:** `deltatech_ai_trial_balance_import`
- **Versiune:** `19.0.1.3.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_ai_trial_balance_import
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_trial_balance_import`
- **Ultima Ingestie:** `2026-10-30`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

La punerea în funcțiune, soldurile din Odoo trebuie să coincidă cu balanța din programul de contabilitate anterior, iar această balanță vine de obicei sub formă de PDF. Modulul încarcă balanța PDF în sincronizarea planului de conturi (`deltatech_chart_of_accounts`): un agent AI citește rândurile, Odoo le potrivește și le verifică, iar o persoană le revizuiește înainte să fie scrise ca sume externe. Diferența se postează apoi din sincronizare, ca până acum. Agentul AI doar transcrie; potrivirea conturilor și a partenerilor, verificările și scrierea sunt deterministe, iar nimic nu se postează automat.

#### 2. Funcționalități Cheie

- **Din PDF în sincronizare**: butonul **Încarcă balanța din PDF (AI)** de pe o sincronizare în ciornă citește balanța și scrie rândurile ca debit / credit extern, pe cont sau, cu detaliu pe parteneri, pe cont și partener. Liniile lipsă ale sincronizării se creează.
- **Balanță sintetică sau pe parteneri**: conturi sintetice cu analitice (ex. 5121.01) sau balanță analitică de parteneri (clienți, furnizori) pentru unul sau mai multe conturi. Se aplică doar cel mai detaliat rând al fiecărui cont; rândurile superioare și totalurile servesc doar la verificare.
- **Coloana încărcată**: solduri finale (implicit) sau rulaje totale (pentru modul de postare „potrivire totaluri debit/credit”).
- **Verificări pe balanța însăși**: fiecare rând (rulajele și soldul final dau același sold), fiecare total tipărit (cont, clasă, total general, reportări), debit = credit pe fiecare coloană a balanței sintetice, data balanței și codul fiscal al firmei. Erorile blochează aplicarea; avertizările cer o confirmare („Am verificat avertizările”).
- **Verificări față de textul PDF-ului**: sumele și codul de cont al fiecărui rând sunt căutate în textul paginii, deci o cifră transcrisă greșit care totuși se echilibrează este semnalată; codurile fiscale se verifică cu cifra de control (CUI, CNP, TVA UE), iar unul invalid nu se folosește la potrivirea partenerului. Un PDF scanat nu se verifică față de text.
- **Potrivirea conturilor**: după codul din celălalt program, după o mapare memorată, apoi după codul completat (4111 -> 411100) când este singurul cont cu acel prefix. Dacă sunt mai multe conturi pe prefix, alege utilizatorul (cu cod completat propus); alegerile se rețin pentru balanțele următoare.
- **Potrivirea partenerilor**: după cod fiscal (cu sau fără prefix RO), apoi după nume fără diacritice, punctuație și formă juridică; un nume apropiat este doar propus. Partenerul lipsă se creează doar la cerere (din PDF).
- **Linii lipsă din balanță**: sincronizarea pornește cu sumele din Odoo ca sume externe, deci liniile absente din balanță se pun pe 0 (toate la o balanță completă, doar conturile citite la una pe parteneri), afișat înainte de aplicare.
- **Balanțe lungi**: PDF-ul se citește pagină cu pagină, cu dialog de progres; o pagină eșuată poate fi recitită (doar paginile cu erori sau cele alese; corecțiile de pe celelalte pagini se păstrează, iar „Citește din nou” citește tot documentul și le uită).
- **Revizuire**: butonul **De verificat** listează rândurile de rezolvat (cont/partener lipsă sau ambiguu, propuneri de confirmat, parteneri lipsă); un rând poate fi exclus. **Aplică în sincronizare** generează liniile, scrie sumele externe și pune pe 0 liniile lipsă; apoi se bifează **Echilibrat** și se postează diferența din sincronizare.
- **Istoric**: fiecare import rămâne pe sincronizare, cu PDF-ul, rândurile citite, cine l-a aplicat și când.
- **Cost controlat**: activare opțională pe companie (implicit dezactivat) și limită zilnică de balanțe citite cu AI (implicit 20, 0 = nelimitat); recitirea unor pagini nu intră în limită.
- **Configurare**: activare în **Setări → Facturare → Go-live → Trial Balance PDF Import with AI**; cheia furnizorului AI din **Setări → AI**; agentul **Trial Balance PDF Reader AI** (AI → Agenți) permite alegerea modelului, care trebuie să accepte fișiere PDF (OpenAI GPT-4o sau ulterior, Google Gemini, sau Claude cu `deltatech_ai_anthropic`). Parametri de sistem opționali: `deltatech_ai_trial_balance_import.timeout` (300 s), `.pages_per_call` (1), `.parallel_calls` (3).
- **Siguranță**: documentul este tratat ca date, agentul are instrucțiunea să nu urmeze comenzi scrise în el. Atenție: balanța (conturi, parteneri, sume) se trimite furnizorului AI ales.

#### 3. Dependențe

- [deltatech_chart_of_accounts](../deltatech_chart_of_accounts/index.md)
- `ai`
- [deltatech_ai_pdf_base](../deltatech_ai_pdf_base/index.md)
- [deltatech_partner_match](../deltatech_partner_match/index.md)

#### 4. Componente Cheie

**Modele**

- `trial.balance.ai.import`: importul unei balanțe PDF pe o sincronizare; păstrează PDF-ul, paginile, rândurile citite, erorile/avertizările și aplicarea.
- `trial.balance.ai.import.page`: o pagină (sau grup de pagini) citită cu AI, pentru progres și recitire selectivă.
- `trial.balance.ai.import.line`: un rând citit din balanță, cu contul și partenerul potrivite, starea de verificare și posibilitatea de excludere.
- `trial.balance.account.map`: maparea memorată între codul din celălalt program și contul Odoo.
- `sync.chart.of.accounts` (extins): butonul de încărcare din PDF și legătura cu importurile.
- `ai.agent` (extins), `res.company`, `res.config.settings`: agentul de citire, activarea pe companie și limita zilnică.

**Vizualizări**

- `view_trial_balance_ai_import_form` / `view_trial_balance_ai_import_list`: formularul importului (bannere de erori/avertizări, progres, aplicare) și lista.
- `view_trial_balance_ai_import_line_list` / `view_trial_balance_ai_import_line_search` / `action_trial_balance_ai_import_line`: rândurile de verificat.
- `view_sync_chart_of_accounts_form_trial_balance_ai`: butonul **Încarcă balanța din PDF (AI)** pe sincronizare.
- `res_config_settings_view_form_trial_balance_ai`: setarea de activare și limita zilnică.
- Dialog JS de progres al citirii (`static/src/read_progress`).

**Acțiuni Automate / Acțiuni Server**

- `ai_agent_trial_balance_reader`: agentul AI „Trial Balance PDF Reader AI” (implicit `gpt-4o`), care transcrie balanța în JSON strict. Nu există cron-uri.

#### 5. Conexiuni

- [deltatech_ai_pdf_base](../deltatech_ai_pdf_base/index.md): extrage textul PDF-ului și verifică codurile fiscale, pentru controlul față de textul paginii.
- [deltatech_chart_of_accounts](../deltatech_chart_of_accounts/index.md): sincronizarea planului de conturi în care se încarcă balanța.
- [deltatech_partner_match](../deltatech_partner_match/index.md): regulile de potrivire a partenerilor, comune cu importul din marketplace și detectorul de dubluri.
- [deltatech_ai_anthropic](../deltatech_ai_anthropic/index.md): permite folosirea modelelor Claude cu fișiere PDF.
