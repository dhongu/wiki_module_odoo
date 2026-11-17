# Quality Management ISO 9001

- **Nume Tehnic:** `deltatech_qms`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_qms
- **Cale Locală:** `odoo-addons/bitshop/deltatech_qms`
- **Ultima Ingestie:** `2026-11-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Managementul calității pentru companiile care dețin sau pregătesc certificarea ISO 9001, într-un singur loc în Odoo, în locul tabelelor și al e-mailurilor: documente controlate, audituri interne, neconformități cu acțiuni corective și preventive (CAPA), obiective ale calității, reclamații ale clienților și un raport de pregătire pentru certificare. Modulul depinde doar de Discuss (`mail`). Titlurile clauzelor și întrebările din lista de verificare sunt redactate de Terrabit; textul standardului ISO nu este inclus.

#### 2. Funcționalități Cheie

- **Documente controlate (clauza 7.5):** proceduri, instrucțiuni, formulare și politici trec prin Ciornă, Analiză și Aprobare. Fiecare aprobare păstrează o revizie numerotată, cu descrierea modificării; revizia anterioară devine învechită. Un document aprobat este doar-citire, iar o modificare pornește o revizie nouă (buton **New revision**).
- **Audituri interne (clauza 9.2):** program de audit pe perioadă, aprobat de responsabilul calității, cu progres; audituri de sistem de calitate, de proces și de furnizor (cu furnizorul auditat), cu calendar; liste de verificare copiate din șabloane reutilizabile (este inclus un șablon de bază pentru clauzele 4–10), rezultat pe fiecare verificare (Conform, Observație, Neconformitate) și generarea unui NCR dintr-un clic. Un audit nu se poate închide cât timp o verificare nu are rezultat.
- **Neconformități și CAPA (clauza 10.2):** severitate, cauză radăcină, acțiuni corective și preventive cu responsabil, termen și activitate de tip to-do. O neconformitate se închide doar când toate acțiunile sunt verificate ca eficiente de responsabilul calității.
- **Obiectivele calității (clauza 6.2):** țintă, unitate, direcție (mai mare sau mai mic e mai bine) și măsurători; obiectivul arată dacă ultima măsurătoare atinge ținta.
- **Reclamații ale clienților (clauza 9.1.2):** termen de răspuns în zile lucrătoare (implicit 5, setat per companie), reclamații depășite evidențiate, escaladare la NCR dintr-un clic.
- **Pregătire pentru certificare:** câte un rând pentru fiecare clauză principală (4–10), cu documentele în vigoare, verificările auditate și neconformitățile deschise, cu status Ready, Partial sau Gap; se poate tipări ca PDF (*Reporting > Certification readiness*).
- **Niveluri de acces:** Utilizator, Auditor intern și Responsabil calitate (setate în *Settings > Users & Companies > Users*, grupul Quality Management (ISO 9001)). Doar responsabilul calității aprobă documente, verifică acțiuni, închide neconformități și escaladează reclamații.
- **Multi-companie:** documentele, auditurile, neconformitățile, acțiunile, obiectivele și reclamațiile aparțin unei companii; clauzele și șabloanele de verificare pot fi partajate între companii.
- **Configurare:** *Quality ISO 9001 > Configuration > Settings* pentru termenul de răspuns la reclamații; *Audits > Checklist templates* pentru adaptarea șablonului de bază.

#### 3. Dependențe

- `mail`

#### 4. Componente Cheie

**Modele**

- `qms.document` / `qms.document.revision`: documentul controlat și reviziile sale numerotate.
- `qms.audit.program`: programul de audit pe perioadă, cu aprobare și progres.
- `qms.audit` / `qms.audit.line`: auditul intern și verificările sale, cu rezultat pe fiecare linie.
- `qms.audit.template` / `qms.audit.template.line`: șabloane reutilizabile de listă de verificare.
- `qms.nonconformity` / `qms.capa`: neconformitatea (NCR) și acțiunile corective/preventive.
- `qms.objective` / `qms.objective.measurement`: obiectivele calității și măsurătorile lor.
- `qms.complaint`: reclamația clientului, cu termen de răspuns și escaladare la NCR.
- `qms.clause`: clauzele standardului (cu date predefinite), folosite în raportul de pregătire.
- `res.company`, `res.config.settings` (extinse): termenul de răspuns la reclamații, per companie.

**Vizualizări**

- Vizualizări de listă/formular pentru documente, programe de audit, audituri, neconformități, obiective, reclamații și clauze (`views/qms_*_views.xml`).
- Setări (`views/res_config_settings_views.xml`) și meniul aplicației (`views/qms_menus.xml`): Documents, Audits, Improvement, Objectives, Reporting, Configuration.
- Raport PDF Certification readiness (`report/qms_readiness_report.xml`).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`. Modulul livrează secvențe, clauzele ISO și șablonul de audit de bază ca date.

#### 5. Conexiuni

- `mail`: modelele principale folosesc `mail.thread` și `mail.activity.mixin` (istoric și activități to-do pentru acțiunile CAPA).
- `res.partner` (Contacte): furnizorul auditat într-un audit de tip Supplier și clientul din reclamații.
