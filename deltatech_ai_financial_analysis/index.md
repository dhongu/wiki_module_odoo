# Financial Analysis AI (Plutus) (localizat la `deltatech_ai_financial_analysis/index.md`)

- **Nume Tehnic:** `deltatech_ai_financial_analysis`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_ai_financial_analysis
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_financial_analysis`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

**Plutus** citește analiza financiară a lunii și spune conducerii ce s-a schimbat, de ce și ce e de făcut. Modulul adaugă un agent AI analizei *Financial Analysis by Period* (`deltatech_financial_analysis`): motorul calculează indicatorii, comparațiile și abaterile semnificative din balanța de verificare, iar Plutus scrie doar comentariul (rezumatul perioadei, câte un comentariu pe abatere, riscurile și ce trebuie verificat de un om). Nu calculează nicio cifră: codul verifică fiecare cifră din răspuns față de datele calculate.

#### 2. Funcționalități Cheie

- **Un click, un apel**: butonul **Comment with Plutus** pe o analiză calculată trimite o singură dată indicatorii, abaterile (cu conturile și partenerii din spate), alertele și controalele, apoi scrie răspunsul pe analiză și pe fiecare abatere.
- **Cifre verificate în cod**: orice sumă sau procent din comentariu trebuie să existe în datele trimise; o cifră care nu există este evidențiată, listată pe analiză, iar comentariul primește starea *Figures to Check*.
- **Comentarii după metoda analizei de final de lună**: suma și procentul abaterii, cauza principală cu cifra ei (preț, volum, mix când motorul le oferă), dacă e punctuală sau continuă, o acțiune concretă; pentru analize lunare, trimestriale, de la începutul anului și anuale.
- **Perioade provizorii**: când perioada nu e închisă, Plutus o spune întâi și nu interpretează liniile afectate.
- **Întrebări în chat**: de ex. „de ce a scăzut marja în septembrie?”; Plutus răspunde cu unelte doar-citire (indicatori, trenduri, abateri cu cauze, vechime creanțe/datorii, starea închiderii). Cu `deltatech_ai_agent_delegate` i se poate adăuga un agent specialist de contabilitate.
- **Rezumat lunar**: în ziua aleasă se analizează luna precedentă, se comentează dacă e închisă și se postează într-un canal Discuss; contabilul primește o activitate de verificare și validare.
- **Confidențialitate și cost**: nu se trimit înregistrări contabile sau coduri fiscale; partenerii pot fi trimiși ca alias și sunt repuși în comentariu; limită zilnică de apeluri AI pe companie. Dacă AI-ul eșuează, analiza rămâne cum a fost calculată.
- **Utilizare**: *Contabilitate > Raportare > Financial Analysis*, **Comment with Plutus**, citiți fila **Comment** și fila **Variances**, editați dacă e nevoie, apoi **Validate**; o recalculare șterge comentariul, o analiză validată îl păstrează.
- **Configurare**: *Contabilitate > Configurare > Setări > Financial Analysis > Plutus* (agentul, limita zilnică, aliasarea partenerilor, **Monthly Digest** cu ziua 1-28, canalul și contabilul); în *AI > Agents > Plutus*, skill-ul *Financial Analysis* dă agentului uneltele de citire.

#### 3. Dependențe

- `deltatech_financial_analysis`
- `ai`

#### 4. Componente Cheie

Secțiunea nu este detaliată: documentația se bazează pe `readme/DESCRIPTION.md`, care nu solicită explicit analiza componentelor tehnice (modele, vizualizări, acțiuni automate). Din cod: extinderi pe `financial.analysis` și `financial.analysis.variance` (apelul către agent și verificarea cifrelor), `ai.agent`, `res.company` și `res.config.settings`; agentul *Plutus* (`ai_agent_plutus`), unelte AI doar-citire definite ca acțiuni server (indicatori, trend, explicarea unei abateri, vechime, starea închiderii) și skill-ul *Financial Analysis*; acțiunea programată `ir_cron_financial_analysis_digest` (zilnic, generează rezumatul lunar în ziua configurată).

#### 5. Conexiuni

- [deltatech_ai_agent_delegate](../deltatech_ai_agent_delegate/index.md): permite adăugarea unui agent specialist de contabilitate lângă Plutus.
