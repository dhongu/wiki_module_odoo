# Managementul calității ISO 9001

- **Nume Tehnic:** `deltatech_qms`
- **Versiune:** `20.0.1.1.1`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_qms`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_qms`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Managementul calității pentru companiile care dețin sau pregătesc certificarea ISO 9001, într-un singur loc în Odoo, în locul tabelelor și al e-mailurilor: documente controlate, audituri interne, neconformități și acțiuni corective/preventive (CAPA), riscuri, analiză de management, obiective, reclamații ale clienților, panou de indicatori și verificarea stadiului de pregătire pentru certificare. Titlurile clauzelor și întrebările din listele de verificare sunt scrise de Terrabit; textul standardului ISO nu este inclus.

#### 2. Funcționalități Cheie

- **Documente controlate** (clauza 7.5): procedurile, instrucțiunile, formularele și politicile trec prin Ciornă, Analiză și Aprobare. Fiecare aprobare păstrează o revizie numerotată cu descrierea modificării, iar revizia anterioară devine perimată; un document aprobat e doar-citire, o modificare pornește o revizie nouă. Interval de revizuire pe document (12 luni implicit).
- **Audituri interne** (clauza 9.2): program de audit pe perioadă, aprobat de responsabilul calității, cu progres; audituri de sistem, de proces și de furnizor, listă de verificare copiată din șabloane reutilizabile (listă de bază pentru clauzele 4-10), rezultat pe fiecare verificare și neconformitate creată dintr-o verificare neconformă. Auditul nu se închide cât timp o verificare nu are rezultat.
- **Neconformități și CAPA** (clauza 10.2): gravitate, cauză rădăcină, acțiuni corective și preventive cu responsabil, termen și activitate. Neconformitatea se închide doar când toate acțiunile sunt verificate ca eficiente de responsabilul calității; acțiunile pot proveni și din riscuri sau din analiza de management.
- **Riscuri și oportunități** (clauza 6.1): probabilitate și impact de la 1 la 5, scor și nivel (Scăzut, Mediu, Ridicat, Critic), acțiuni de tratare, următoarea revizuire.
- **Analiza de management** (clauza 9.3): participanți, date de intrare, decizii, acțiuni, plus un instantaneu al indicatorilor din panou, pentru perioada de la analiza anterioară.
- **Obiective ale calității** (clauza 6.2): țintă, sens (mai mare sau mai mic e mai bine) și măsurători.
- **Reclamații ale clienților** (clauza 9.1.2): termen de răspuns în zile lucrătoare (5 implicit, per companie), reclamații depășite evidențiate, escaladare într-o neconformitate.
- **Pregătire pentru certificare**: câte un rând pe clauză principală (4-10) cu documentele în vigoare, riscurile, analizele, verificările auditate și neconformitățile deschise, cu stare Pregătit, Parțial sau Lipsă; se poate tipări PDF.
- **Panou**: șapte carduri KPI (neconformități deschise, acțiuni întârziate, audituri în luna curentă, documente de revizuit, obiective neatinse, reclamații întârziate, riscuri ridicate și critice), cu acces la înregistrările din spatele cifrei.
- **Mementouri** zilnice: verificarea eficienței acțiunilor (după 30 de zile implicit), revizuirea documentelor, răspunsul la reclamații, revizuirea riscurilor.
- **Rapoarte PDF**: raport de neconformitate, raport CAPA, raport de audit intern.
- Trei niveluri de acces: Utilizator, Auditor intern, Responsabil calitate (în *Setări > Utilizatori*); în *Calitate ISO 9001 > Configurare > Setări* se stabilesc timpul de răspuns la reclamații și verificarea eficienței CAPA. Fluxul pas-cu-pas este în fișa consultantului.

#### 3. Dependențe

- `mail`
- `deltatech_web_kpi_cards`

#### 4. Componente Cheie

**Modele**

- `qms.document`, `qms.document.revision`: documente controlate și reviziile lor.
- `qms.audit.program`, `qms.audit`, `qms.audit.line`, `qms.audit.template`, `qms.audit.template.line`: programe, audituri, verificări și șabloane de listă de verificare.
- `qms.nonconformity`, `qms.capa`: neconformități și acțiuni corective/preventive.
- `qms.risk`, `qms.management.review`, `qms.objective`, `qms.objective.measurement`, `qms.complaint`: riscuri, analize de management, obiective cu măsurători și reclamații.
- `qms.clause`: clauzele standardului (titluri scrise de Terrabit).
- `qms.dashboard`: calculul indicatorilor panoului.
- `res.company`, `res.config.settings` (extinse): setările modulului.

**Vizualizări**

- Liste, formulare și căutări pentru fiecare model (de exemplu `qms_document_view_form`, `qms_document_view_list`), panoul de calitate (componentă OWL cu carduri KPI) și vizualizarea Pregătire pentru certificare.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_qms_reminders`: job zilnic (`_cron_send_reminders`) care creează activități pentru verificarea eficienței acțiunilor, revizuirea documentelor, reclamații întârziate și revizuirea riscurilor.
- Rapoarte PDF: `action_report_qms_nonconformity`, `action_report_qms_capa`, `action_report_qms_audit`, `action_report_qms_readiness`.

#### 5. Conexiuni

- Niciuna verificată cu alte pagini wiki existente.
