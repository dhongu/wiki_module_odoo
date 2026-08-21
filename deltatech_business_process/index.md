# Business process (localizat la `deltatech_business_process/index.md`)

- **Nume Tehnic:** `deltatech_business_process`
- **Versiune:** `19.0.1.9.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_business_process
- **Cale Locală:** `odoo-addons/deltatech/deltatech_business_process`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul ajută echipele de implementare să structureze și să execute proiectele de implementare Odoo într-un mod controlat. Introduce conceptele de Proiect, Procese de Afaceri și Pașii acestora, împreună cu fluxuri de Testare și de gestionare a Problemelor (issues), astfel încât procesele să poată fi proiectate, validate și livrate ordonat. Valoarea principală constă în faptul că oferă un spațiu de lucru unic în care un proiect este descompus în procese, fiecare proces în pași, iar pașii pot fi testați și corectați până la momentul punerii în producție, cu evidența documentelor, a responsabililor și a progresului pe parcursul întregului ciclu. Ediția curentă adaugă și o Bibliotecă de Procese reutilizabilă, alimentată din module Odoo instalate și/sau din repository-uri git externe.

#### 2. Funcționalități Cheie

- Spațiu de lucru pentru proiect: gestionează proiectele de implementare, fazele și progresul general.
- Procese de afaceri: definește procese per proiect, grupate pe zonă de afaceri și, opțional, pe grup de procese.
- Pași: descompune fiecare proces în pași ordonați, cu responsabili și tranzacții asociate.
- Testare: creează teste Interne, de Integrare și de Acceptanță de Utilizator (UAT) care reflectă pașii procesului și urmăresc starea și rezultatul execuției pentru fiecare pas.
- Probleme (issues): înregistrează problemele apărute la testare sau în execuție pe un proces ori pe un pas specific de test, le urmărește prin stări și le închide cu validări (o problemă rezolvată poate marca automat pasul de test drept trecut, dacă nu mai rămân alte probleme deschise pe acel pas).
- Dezvoltări: leagă elementele de dezvoltare de procese și/sau proiecte pentru a urmări personalizările necesare.
- Atașamente: acces rapid la toate documentele asociate proiectului, proceselor, pașilor, testelor și problemelor, printr-un buton inteligent cu vizualizare consolidată.
- Rapoarte: tipărește rapoartele de Proces de Afaceri și de Test de Proces; exportă/importă procese ca JSON pentru reutilizare (cu opțiuni pentru includerea testelor, a responsabilului, a clientului și a informațiilor de suport).
- Raport Excel: generează din proiect un sumar Excel care grupează procesele pe zonă și agregă duratele de configurare/instruire/testare/migrare de date, evidențiind procesele cu durată totală zero.
- Bibliotecă de procese: sursă reutilizabilă de procese, populată din module instalate care conțin un folder `processes/` și/sau din repository-uri git externe configurabile din Setări (URL-uri separate prin virgulă, cu buton „Sincronizează acum" pentru clonare/actualizare locală); importul selectiv se face în proiect prin acțiunea „Process Library", cu comutator „Include durations" pentru a aduce sau nu estimările de efort.
- Suport pentru repository-uri git private HTTPS: utilizator (implicit `x-access-token` pentru GitHub, `oauth2` pentru GitLab) și token/parolă, trimise ca antet HTTP Basic Authorization, fără a fi scrise pe disc în configurația clonei; URL-urile SSH sau cele cu credențiale incluse sunt folosite ca atare.
- Instalare de module direct de pe un proces, pentru proiecte locale (blocată intenționat pentru proiectele remote).
- Securitate și chatter: majoritatea înregistrărilor moștenesc `mail.thread`/activity pentru urmăritori, jurnalizare și notificări, abonând automat participanții cheie.

#### 3. Dependențe

- `base`
- `mail`

#### 4. Componente Cheie

**Modele** (conform secțiunii „Data model at a glance" din `readme/DESCRIPTION.md`, completată cu analiza codului din `models/`)

- `business.project`: containerul proiectului; agregă procesele, problemele, dezvoltările și atașamentele; poate genera un raport sumar Excel.
- `business.process`: entitatea centrală care descrie un proces într-un proiect; are pași, teste, dezvoltări și contoare calculate.
- `business.process.step`: o activitate ordonată dintr-un proces; poate referi o tranzacție de afaceri și un partener responsabil.
- `business.process.test`: o instanță de test pentru un proces (domeniu: intern/integrare/acceptanță de utilizator); generează automat testele de pas și urmărește progresul și finalizarea.
- `business.process.step.test`: oglindește un pas de proces pentru un test specific; înregistrează date, rezultat (ciornă/trecut/eșuat) și observații; numără problemele asociate.
- `business.issue`: probleme descoperite la testare sau în execuție; ciclu de viață ciornă → deschis/alocat → rezolvat/în test → închis/redeschis; integrat cu urmăritori și email.
- `business.development` (+ `business.development.type`): dezvoltări de referință legate de procese/proiecte; pot contribui la durata proiectului.
- `business.area` și `business.process.group`: clasifică procesele pe zonă și pe grup.
- `business.process.implementation.stage`: etapele de implementare (ex: configurare, instruire, testare, migrare date) atribuibile unui proces.
- `business.role`: rolurile de business asociate pașilor/proceselor.
- `business.transaction`: tranzacțiile de afaceri care pot fi referite de pașii unui proces.
- `business.process.library` (model abstract): motorul Bibliotecii de Procese — descoperă surse din module instalate (`processes/`) și din repository-uri git externe (clonare/pull, autentificare HTTP Basic pentru HTTPS private), listează procesele disponibile din `process.json` și le importă selectiv (cu sau fără durate) într-un proiect.
- `res.config.settings` (extindere): configurarea listei de repository-uri git ale Bibliotecii de Procese și declanșarea sincronizării.

**Vizualizări**

- Vizualizări de formular, listă și kanban pentru proiecte, procese, pași, teste, probleme, dezvoltări, arii, roluri, tranzacții și etape de implementare (definite în `views/`, ex: `business_project_view.xml`, `business_process_view.xml`, `business_process_step_view.xml`, `business_issue_view.xml`).
- `views/res_config_settings_views.xml`: secțiunea de setări pentru configurarea repository-urilor git ale Bibliotecii de Procese.
- `views/menu.xml`: structura de meniu a aplicației.
- Rapoarte QWeb pentru Procesul de Afaceri și Testul de Proces (`report/business_process_report_view.xml`, `report/business_process_test_report_view.xml`).

**Acțiuni Automate / Acțiuni Server**

- Secvențe definite în `data/ir_sequence_data.xml` și șabloane de email în `data/email_templates.xml`, încărcate la instalare.
- Date implicite pentru etapele de implementare în `data/implementation_stage_data.xml` și date generale în `data/data.xml`.
- Vrăjitoare de export/import procese ca JSON (`wizard/export_business_process.py`, `wizard/import_business_process.py`): exportul din lista de procese (cu opțiuni pentru teste, responsabil, client și suport) și importul dintr-un JSON pe formularul proiectului.
- Migrare de date la actualizare (`migrations/19.0.1.6.0/post-migrate.py`).

#### 5. Conexiuni

- Nu sunt declarate conexiuni funcționale către alte module documentate în wiki. Modulul depinde doar de `base` și `mail`; Biblioteca de Procese poate opțional descoperi conținut din orice alt modul instalat care conține un folder `processes/`, dar aceasta nu constituie o dependență strictă.
