# Romania - Documente HR (localizat la `l10n_ro_hr_documents/index.md`)

- **Nume Tehnic:** `l10n_ro_hr_documents`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_hr_documents
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_hr_documents`
- **Ultima Ingestie:** `2026-10-05`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul pregătește documentele de personal direct din fișa angajatului și din versiunile contractului, fără retastarea datelor: contractul individual de muncă, actul adițional, deciziile de suspendare și de încetare, cererea de demisie și adeverința de vechime la angajator. Fiecare document primește număr de înregistrare, are text editabil cât timp e ciornă, iar PDF-ul se arhivează pe fișa angajatului. Modulul este în stadiul Alpha.

> **Atenție:** modelele sunt cele uzuale, nu modelul-cadru al contractului, și **trebuie validate juridic** de consilierul juridic al firmei înainte de utilizare.

#### 2. Funcționalități Cheie

- **Șase tipuri de documente**, create pe angajat, cu text precompletat din fișa angajatului, din versiunea contractului și din datele companiei:
    - **Contract individual de muncă:** clauzele esențiale din Codul muncii (art. 17): părțile, funcția și codul COR, durata, perioada de probă (art. 31, cel mult 90 de zile la execuție și 120 la conducere), locul muncii, timpul de muncă, concediul de odihnă (art. 145, minimum 20 de zile lucrătoare), salariul, preavizul (art. 81 și 75); clauzele se iau din versiunea contractului aleasă (implicit prima, cea de la angajare), iar modulul avertizează dacă data documentului depășește termenul din art. 16 (ziua anterioară începerii activității);
    - **Act adițional (art. 41):** alegeți versiunea anterioară și cea nouă a contractului; tabelul din fila *Date* listează doar elementele care diferă (funcție, COR, departament, salariu, timp de muncă, normă, durată, loc de muncă); cu versiuni identice documentul nu se poate emite;
    - **Decizie de suspendare:** temeiul (art. 50, 51, 52 alin. (1) lit. c), art. 54), perioada și efectele (art. 49);
    - **Decizie de încetare:** temeiul (art. 55 lit. b, 56, 81, 61 lit. a, c, d, art. 65), data și motivele; preavizul (minimum 20 de zile lucrătoare, art. 75) apare doar la art. 61 lit. c, d și art. 65, iar concedierea disciplinară nu are preaviz; termenul de contestare (art. 268) este de 30 de zile la sancțiunea disciplinară și de 45 la celelalte; la concediere, fără motive și instanță documentul nu se poate emite (art. 62, 76, 78);
    - **Cerere de demisie:** preavizul în zile lucrătoare (cel mult 20 la funcții de execuție, 45 la conducere, art. 81 alin. (4)) și data la care se împlinește, calculată automat; se semnează de salariat;
    - **Adeverință de vechime în muncă la angajator (art. 34 alin. (5)):** perioadele, funcțiile, normele și salariul din istoricul versiunilor contractului, plus vechimea la angajator calculată calendaristic.
- **Date REGES preluate** din [l10n_ro_reges](../l10n_ro_reges/index.md): COR, durată, normă, temei de încetare sau suspendare.
- **Două semnături:** angajatorul (implicit «Administrator») și, la contract, act adițional și cerere de demisie, salariatul (completat automat); la decizii, cel care a întocmit documentul.
- **Emitere:** la apăsarea butonului *Emite* documentul primește număr din secvență (`HR/an/nr`), iar PDF-ul se arhivează ca atașament pe fișa angajatului; un document emis nu se șterge, doar se anulează; la revenirea în ciornă și reemitere își păstrează numărul și înlocuiește PDF-ul (stări: ciornă, emis, anulat; istoric în chatter).
- **Avertismente și blocaje:** limitele probei și ale preavizului, data contractului și a actului adițional, CNP lipsă, temei sau dată lipsă.
- **Meniu:** *Angajați → Documente HR (RO)*, pentru grupul *Ofițer* din Angajați. Pe companie se completează denumirea, adresa, CUI-ul și numărul din Registrul Comerțului; pe angajat CNP-ul și adresa, iar pe versiunea contractului funcția, salariul, codul COR, durata, norma și datele REGES.
- **Limite:**
    - modelele sunt cele uzuale (nu modelul-cadru) și trebuie validate juridic; firma răspunde de conținutul final;
    - nu sunt incluse decizia de nominalizare REGES, regulamentul intern și fișa postului;
    - modulul nu transmite nimic în REGES: transmiterea contractelor, modificărilor, suspendărilor și încetărilor se face din `l10n_ro_reges`;
    - la cererea de demisie, sărbătorile legale se scad din preaviz doar dacă există în calendarul companiei (introduse manual sau generate cu modulul opțional `l10n_ro_hr_pontaj`); altfel data se corectează manual;
    - vechimea în meserie și în specialitate și perioadele de suspendare din adeverință se completează manual;
    - clauzele din art. 17 alin. (3) neacoperite de model se completează manual în contract: ore suplimentare și compensarea lor, programul în schimburi, condițiile perioadei de probă, deplasarea la loc de muncă mobil, alte avantaje.

#### 3. Dependențe

- [l10n_ro_reges](../l10n_ro_reges/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.hr.document` (nou, cu `mail.thread`, multi-companie): documentul HR, cu tipul (`contract`, `addendum`, `suspension`, `termination`, `resignation`, `service_proof`), temeiul de încetare sau suspendare, versiunile comparate, semnăturile, textul (editabil în ciornă), tabelul (act adițional și adeverință), atașamentul PDF și metodele `action_issue`, `action_cancel`, `action_draft`, `action_print`.

**Vizualizări**

- `view_l10n_ro_hr_document_form`: formularul documentului, cu filele *Text* și *Date*.
- `view_l10n_ro_hr_document_list` și `view_l10n_ro_hr_document_search`: lista și filtrele (tip, stare).
- `action_l10n_ro_hr_document` / `menu_l10n_ro_hr_document`: acțiunea și meniul *Documente HR (RO)* sub *Angajați*.
- `action_report_hr_document`: raportul PDF al documentului, cu două semnături.
- `data/document_templates.xml`: șabloane QWeb pentru părți (`party_employer`, `party_employee`), pentru textul fiecărui tip (`body_contract`, `body_addendum`, `body_suspension`, `body_termination`, `body_resignation`, `body_service_proof`) și pentru tabel (`table_document`).

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`. Definește secvența `seq_l10n_ro_hr_document` (numerotarea `HR/an/nr`) și o regulă multi-companie (`l10n_ro_hr_document_company_rule`).

#### 5. Conexiuni

- [l10n_ro_reges](../l10n_ro_reges/index.md): sursa datelor REGES din versiunile contractului (COR, durată, normă, temeiuri); transmiterea în REGES se face de acolo, nu din acest modul.
- [l10n_ro_hr_pontaj](../l10n_ro_hr_pontaj/index.md): opțional, generează sărbătorile legale în calendarul companiei, folosite la calculul preavizului din cererea de demisie.
- `hr`: angajatul și versiunile contractului.
