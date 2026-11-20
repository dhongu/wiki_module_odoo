# Quality Management ISO 9001 (localizat la `deltatech_qms/index.md`)

- **Nume Tehnic:** `deltatech_qms`
- **Versiune:** `19.0.1.1.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_qms
- **Cale Locală:** `odoo-addons/bitshop/deltatech_qms`
- **Ultima Ingestie:** `2026-11-19`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Managementul calității pentru companiile care dețin sau pregătesc certificarea ISO 9001, într-un singur loc în Odoo, în locul tabelelor și al e-mailurilor: documente controlate, audituri interne, neconformități cu acțiuni corective și preventive (CAPA), registru de riscuri și oportunități, analiză efectuată de management, obiective ale calității, reclamații ale clienților, un tablou de bord cu indicatori și un raport de pregătire pentru certificare. Titlurile clauzelor și întrebările din lista de verificare sunt redactate de Terrabit; textul standardului ISO nu este inclus.

#### 2. Funcționalități Cheie

- **Documente controlate (clauza 7.5):** proceduri, instrucțiuni, formulare și politici trec prin Ciornă, Analiză și Aprobare. Fiecare aprobare păstrează o revizie numerotată, cu descrierea modificării; revizia anterioară devine învechită. Un document aprobat este doar-citire, iar o modificare pornește o revizie nouă (buton **New revision**). Fiecare document are un interval de revizuire (implicit 12 luni).
- **Audituri interne (clauza 9.2):** program de audit pe perioadă, aprobat de responsabilul calității, cu progres; audituri de sistem de calitate, de proces și de furnizor (cu furnizorul auditat), cu calendar; liste de verificare copiate din șabloane reutilizabile (șablon de bază pentru clauzele 4–10), rezultat pe fiecare verificare (Conform, Observație, Neconformitate) și generarea unui NCR dintr-un clic. Un audit nu se poate închide cât timp o verificare nu are rezultat.
- **Neconformități și CAPA (clauza 10.2):** severitate, cauză rădăcină, acțiuni corective și preventive cu responsabil, termen și activitate de tip to-do. O neconformitate se închide doar când toate acțiunile sunt verificate ca eficiente de responsabilul calității. Acțiunile pot proveni și dintr-un risc sau dintr-o analiză de management, în aceeași listă.
- **Riscuri și oportunități (clauza 6.1):** probabilitate și impact de la 1 la 5, scor și nivel (Scăzut, Mediu, Ridicat, Critic), acțiuni de tratare și data următoarei revizuiri; utilizatorul vede riscurile pe care le deține.
- **Analiza efectuată de management (clauza 9.3):** participanți, date de intrare, decizii și acțiuni de urmărire, plus un instantaneu al indicatorilor din tabloul de bord, luat dintr-un clic, pentru perioada de la analiza anterioară.
- **Obiectivele calității (clauza 6.2):** țintă, unitate, direcție (mai mare sau mai mic e mai bine) și măsurători; obiectivul arată dacă ultima măsurătoare atinge ținta.
- **Reclamații ale clienților (clauza 9.1.2):** termen de răspuns în zile lucrătoare (implicit 5, setat per companie), reclamații depășite evidențiate, escaladare la NCR dintr-un clic.
- **Tablou de bord:** șapte carduri KPI (neconformități deschise, acțiuni întârziate, audituri în luna curentă, documente de revizuit, obiective neatinse, reclamații întârziate, riscuri ridicate și critice); un clic deschide înregistrările din spatele cifrei.
- **Mementouri zilnice:** activități to-do pentru verificarea eficienței acțiunilor încheiate (după 30 de zile, implicit), revizuirea documentelor, răspunsul la reclamațiile întârziate și revizuirea riscurilor.
- **Pregătire pentru certificare:** câte un rând pentru fiecare clauză principală (4–10), cu documentele în vigoare, riscurile și analizele de management, verificările auditate și neconformitățile deschise, cu status Ready, Partial sau Gap; se poate tipări ca PDF (*Reporting > Certification readiness*).
- **Rapoarte PDF:** raport de neconformitate, raport CAPA și raport de audit intern.
- **Niveluri de acces:** Utilizator, Auditor intern și Responsabil calitate (setate în *Settings > Users & Companies > Users*, grupul Quality Management (ISO 9001)). Doar responsabilul calității aprobă documente, verifică acțiuni, închide neconformități și escaladează reclamații.
- **Multi-companie:** documentele, auditurile, neconformitățile, acțiunile, riscurile, analizele, obiectivele și reclamațiile aparțin unei companii; clauzele și șabloanele de verificare pot fi partajate.
- **Configurare:** *Quality ISO 9001 > Configuration > Settings* pentru termenul de răspuns la reclamații și verificarea eficienței CAPA (zile după încheierea acțiunii); *Audits > Checklist templates* pentru adaptarea șablonului de bază.

#### 3. Dependențe

- `mail`
- [deltatech_web_kpi_cards](../deltatech_web_kpi_cards/index.md)

#### 4. Componente Cheie

**Modele**

- `qms.document` / `qms.document.revision`: documentul controlat și reviziile sale numerotate.
- `qms.audit.program`: programul de audit pe perioadă, cu aprobare și progres.
- `qms.audit` / `qms.audit.line`: auditul intern și verificările sale, cu rezultat pe fiecare linie.
- `qms.audit.template` / `qms.audit.template.line`: șabloane reutilizabile de listă de verificare.
- `qms.nonconformity` / `qms.capa`: neconformitatea (NCR) și acțiunile corective/preventive (din NCR, risc sau analiză de management).
- `qms.risk`: registrul de riscuri și oportunități, cu scor și nivel.
- `qms.management.review`: analiza efectuată de management, cu instantaneu KPI.
- `qms.objective` / `qms.objective.measurement`: obiectivele calității și măsurătorile lor.
- `qms.complaint`: reclamația clientului, cu termen de răspuns și escaladare la NCR.
- `qms.clause`: clauzele standardului (cu date predefinite), folosite în raportul de pregătire.
- `qms.dashboard`: calculează cardurile KPI și rulează mementourile zilnice.
- `res.company`, `res.config.settings` (extinse): termenul de răspuns la reclamații și verificarea eficienței CAPA.

**Vizualizări**

- Vizualizări de listă/formular pentru documente, programe de audit, audituri, neconformități, obiective, reclamații, riscuri, analize de management și clauze (`views/qms_*_views.xml`).
- Tablou de bord (`views/qms_dashboard_views.xml`, componenta OWL din `static/src/dashboard/`, bazată pe cardurile KPI din `deltatech_web_kpi_cards`).
- Setări (`views/res_config_settings_views.xml`) și meniul aplicației (`views/qms_menus.xml`).
- Rapoarte PDF: Certification readiness (`report/qms_readiness_report.xml`) și rapoartele de înregistrări NCR, CAPA și audit (`report/qms_record_reports.xml`).

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_qms_reminders` (Quality ISO 9001: reminders): rulează zilnic `qms.dashboard._cron_send_reminders()` și creează activități to-do pentru verificarea eficienței CAPA, revizuirea documentelor, reclamațiile întârziate și revizuirea riscurilor.
- Nu sunt definite `base.automation` sau `ir.actions.server`. Modulul livrează și secvențe, clauzele ISO, șablonul de audit de bază și tipuri de activități ca date.

#### 5. Conexiuni

- [deltatech_web_kpi_cards](../deltatech_web_kpi_cards/index.md): componenta `KpiCards` este importată în tabloul de bord al calității.
- `mail`: modelele principale folosesc `mail.thread` și `mail.activity.mixin` (istoric și activități to-do pentru acțiunile CAPA).
- `res.partner` (Contacte): furnizorul auditat într-un audit de tip Supplier și clientul din reclamații.
