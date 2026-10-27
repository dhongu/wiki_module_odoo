# Financial Analysis AI (Plutus)

- **Nume Tehnic:** `deltatech_ai_financial_analysis`
- **Versiune:** `19.0.1.2.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_ai_financial_analysis
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_financial_analysis`
- **Ultima Ingestie:** `2026-10-27`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă un agent AI, Plutus, peste analiza financiară pe perioade. Motorul de calcul determină indicatorii, comparațiile și abaterile semnificative pornind de la balanța de verificare, iar Plutus scrie doar comentariul: un rezumat al perioadei, câte un comentariu pentru fiecare abatere semnificativă, riscurile și ce trebuie verificat de un om. Agentul nu calculează nicio cifră, iar codul verifică fiecare sumă și procent din răspuns față de datele calculate, astfel încât conducerea primește o interpretare lunară sau anuală fără riscul unor cifre inventate.

#### 2. Funcționalități Cheie

- **Un click, un apel:** butonul **Comentează cu Plutus** pe o analiză calculată trimite o singură dată indicatorii, abaterile (cu conturile și partenerii din spatele lor), alertele și controalele; răspunsul se scrie pe analiză și pe fiecare abatere.
- **Cifre verificate în cod:** orice sumă sau procent din comentariu trebuie să existe în datele trimise agentului. Cifra care nu există este evidențiată, listată pe analiză, iar comentariul primește starea *Comentat, cifre de verificat*.
- **Comentarii după metoda analizei de închidere de lună:** suma și procentul abaterii, cauza principală cu cifra ei (preț, volum, mix, când motorul le furnizează), dacă e punctuală sau continuă și o acțiune concretă. Funcționează pe analize lunare, trimestriale, cumulate de la început de an și anuale.
- **Perioade provizorii:** când perioada nu e închisă, Plutus o spune de la început și nu interpretează liniile afectate.
- **Întrebări în chat:** Plutus răspunde la întrebări de tip „de ce a scăzut marja în septembrie?” sau „ce clienți au cele mai mari solduri?” folosind unelte read-only (indicatori, tendințe, abateri cu cauze, vechime creanțe/datorii, stare închidere). Cu `deltatech_ai_agent_delegate` i se poate adăuga un agent specialist de contabilitate.
- **Rezumat lunar automat:** în ziua aleasă, luna precedentă este analizată, comentată (dacă luna e închisă) și postată într-un canal Discuss; contabilul primește o activitate de verificare și validare.
- **Confidențialitate și cost sub control:** nu se trimit articole contabile și nici identificatori fiscali; partenerii pot fi trimiși ca pseudonime și sunt repuși în comentariu. Există o limită zilnică de apeluri AI pe companie. Dacă AI-ul eșuează, analiza rămâne cea calculată.
- **Stări ale comentariului AI:** *Necomentat*, *Comentat*, *Comentat, cifre de verificat*, *Eșuat*, *Omis: limita zilnică atinsă*; starea e vizibilă și în lista analizelor.
- **Flux de utilizare:** în **Contabilitate → Raportare → Analiză financiară** se deschide o analiză calculată, se apasă **Comentează cu Plutus**, se citește fila **Comentariu** (rezumat, riscuri, ce se verifică) și fila **Abateri**, se editează după nevoie, apoi se **Validează**. Recalcularea șterge comentariul; o analiză validată îl păstrează.
- **Configurare:** în **Contabilitate → Configurare → Setări → Analiză financiară → Plutus** se aleg agentul (implicit Plutus), numărul maxim de comentarii AI pe zi pe companie (0 = fără limită), trimiterea partenerilor ca pseudonime și rezumatul lunar (ziua 1–28, canalul Discuss, contabilul care primește activitatea). Modelul se setează pe agent în **AI → Agenți → Plutus**; cu `deltatech_ai_anthropic` instalat, la instalare se setează Claude Sonnet.
- **AI nativ Odoo:** folosește agenții AI din Odoo 19 Enterprise și furnizorul deja configurat (OpenAI, Gemini sau Claude prin `deltatech_ai_anthropic`).

Pașii detaliați, cu capturi de ecran, sunt în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_financial_analysis](../deltatech_financial_analysis/index.md)
- `ai`

#### 4. Componente Cheie

**Modele**

- `financial.analysis` (extins): câmpurile de comentariu AI (stare, rezumat, cifre de verificat, eroare, datele trimise, data și durata apelului) și logica de apel către agent și de verificare a cifrelor.
- `financial.analysis.variance` (extins): comentariul AI pe abatere și marcajul de cifre neverificate.
- `ai.agent` (extins): prompt de sistem traductibil.
- `res.company` / `res.config.settings` (extinse): agentul, pseudonimizarea partenerilor, limita zilnică și parametrii rezumatului lunar (`fa_ai_*`).

**Vizualizări**

- `financial_analysis_view_form` / `financial_analysis_view_list`: butonul **Comentează cu Plutus**, fila Comentariu și starea AI în listă.
- `financial_analysis_variance_view_list` / `financial_analysis_variance_view_form`: comentariul pe abatere.
- `res_config_settings_view_form`: blocul de setări Plutus.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_financial_analysis_digest`: rulează zilnic (`_cron_ai_monthly_digest`) și, în ziua aleasă, analizează luna precedentă, o comentează dacă e închisă, postă rezumatul în canal și creează activitatea pentru contabil.
- Unelte AI (`ir.actions.server`, topic *Financial Analysis*): indicatorii unei perioade, tendința unui indicator, explicarea unei abateri, vechimea creanțelor/datoriilor, starea închiderii perioadei.
- `ai_agent_plutus`: agentul Plutus, creat la instalare.

#### 5. Conexiuni

- [deltatech_ai_agent_delegate](../deltatech_ai_agent_delegate/index.md): permite adăugarea unui agent specialist de contabilitate la Plutus.
- [deltatech_ai_anthropic](../deltatech_ai_anthropic/index.md): furnizor Claude; la instalare agentul primește modelul Claude Sonnet.
- [l10n_ro_ai_administrators_report](../l10n_ro_ai_administrators_report/index.md): Plutus scrie draftul raportului administratorilor (OMFP pct. 489–491).
- [l10n_ro_ai_partner_financials](../l10n_ro_ai_partner_financials/index.md): unealta de bonitate a partenerilor din bilanțurile MFinanțe.
