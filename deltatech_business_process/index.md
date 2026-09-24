# Business process (localizat la `deltatech_business_process/index.md`)

- **Nume Tehnic:** `deltatech_business_process`
- **Versiune:** `19.0.1.9.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_business_process
- **Cale Locală:** `odoo-addons/deltatech/deltatech_business_process`
- **Ultima Ingestie:** `2026-09-24`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul ajută echipele de implementare să structureze și să execute proiectele de implementare Odoo într-un mod controlat. Introduce conceptele de Proiect, Procese de Afaceri și Pașii acestora, împreună cu fluxuri de Testare și de gestionare a Problemelor (issues), astfel încât procesele să poată fi proiectate, validate și livrate ordonat. Valoarea principală constă în faptul că oferă un spațiu de lucru unic în care un proiect este descompus în procese, fiecare proces în pași, iar pașii pot fi testați și corectați până la momentul punerii în producție, cu evidența documentelor, a responsabililor și a progresului pe parcursul întregului ciclu. Ediția curentă adaugă și o Bibliotecă de Procese reutilizabilă, alimentată din module Odoo instalate și/sau din repository-uri git externe.

#### 2. Funcționalități Cheie

- Spațiu de lucru pentru proiect: gestionează proiectele de implementare, fazele și progresul general; codul proiectului (`P00001`) se dă automat, iar starea (Pregătire → Realizare → Lansare → În exploatare) se schimbă din bara de stare.
- Procese de afaceri: definește procese per proiect, grupate pe zonă de afaceri și, opțional, pe grup de procese; un proces nou dintr-o arie cu responsabil primește automat *Responsabil implementare*.
- Pași: descompune fiecare proces în pași ordonați, cu responsabili și tranzacții asociate; pașii se pot modifica doar cât procesul e în *Ciornă* sau *Proiectare*.
- Ciclul de viață al procesului: Ciornă → Proiectare → Test → Gata → Producție (sau Abandonat). **Doar grupul „Admin procese” poate schimba starea procesului** — butoanele de stare apar și pentru „Responsabil proces”, dar acel grup nu are drept de scriere pe proces și primește eroare de acces.
- Testare: creează teste ale Implementatorului, de Integrare și de Acceptanță a Utilizatorului (UAT), pornite din meniul „Acțiuni” al listei de procese; fiecare test se creează cu toți pașii procesului. Pornirea unui test pe o selecție de mai multe procese **nu funcționează corect**: testul implementatorului dă eroare, iar testele de integrare/acceptanță se creează doar pentru primul proces selectat — porniți testele pe un singur proces odată.
- Butonul inteligent „Pornire test” (cu contor) din formularul procesului **creează un test de acceptanță nou la fiecare apăsare**; pentru a reveni la un test existent se folosește butonul „Teste”.
- Rularea testului: rezultatul (Trecut/Eșuat) se trece pe fiecare pas, nu pe test în ansamblu. „Efectuat” închide testul și **marchează drept „Trecut” inclusiv pașii eșuați**; pașii rămași în *Ciornă* nu se modifică — testul se închide doar după ce toate problemele lui au fost rezolvate. Butonul „Așteaptă” **blochează testul**: din starea *Așteptare* nu mai există niciun buton de ieșire (remediere: un Admin procese șterge testul și pornește altul).
- Probleme (issues): înregistrează problemele apărute la testare sau în execuție pe un proces ori pe un pas specific de test, le urmărește printr-un flux de stări (Deschis → Alocat → Rezolvat → În testare la client → Închis/Redeschis) și le închide cu validări; o problemă închisă marchează automat pasul de test drept *Trecut*, dacă nu mai rămân alte probleme deschise pe acel pas.
- Dezvoltări: leagă elementele de dezvoltare de procese și/sau proiecte pentru a urmări personalizările necesare, cu aprobare și contribuție la durata proiectului.
- Atașamente: acces rapid la toate documentele asociate proiectului, proceselor, pașilor, testelor și problemelor, printr-un buton inteligent cu vizualizare consolidată.
- Rapoarte: tipărește rapoartele de Proces de Afaceri (pași pe proiect, arie și stare) și de Test de Proces (pași de test pe arie și rezultat), plus un raport de Probleme pe arie și severitate; exportă/importă procese ca JSON pentru reutilizare (cu opțiuni pentru includerea testelor, a responsabilului, a clientului și a informațiilor de suport).
- Raport Excel: din proiect, „Acțiuni → Descarcă raportul Excel” generează `Project_Report.xlsx` cu procesele grupate pe arie și duratele de configurare/instruire/testare/migrare de date, evidențiind cu roșu procesele cu durată totală zero. **Coloanele „Testing duration” și „Data Migration Duration” sunt inversate** — valoarea migrării apare sub *Testing duration* și invers, inclusiv în totaluri; doar totalul pe rând (*Total Duration*) e corect.
- Bibliotecă de procese: sursă reutilizabilă de procese, populată din module instalate care conțin un folder `processes/` (ex. `l10n_ro_process_library`) și/sau din repository-uri git externe configurabile din Setări (URL-uri separate prin virgulă, cu buton „Sincronizează acum” pentru clonare/actualizare locală); importul selectiv se face în proiect prin acțiunea „Import din bibliotecă”, cu comutator „Include durations” pentru a aduce sau nu estimările de efort (tot sau nimic pentru procesele selectate). Deschiderea bibliotecii creează automat ariile lipsă, chiar dacă nu se importă nimic.
- Suport pentru repository-uri git private HTTPS: utilizator (implicit `x-access-token` pentru GitHub, `oauth2` pentru GitLab) și token/parolă, trimise ca antet HTTP Basic Authorization, fără a fi scrise pe disc în configurația clonei; URL-urile SSH sau cele cu credențiale incluse sunt folosite ca atare.
- Instalare de module direct de pe un proces, pentru proiecte locale (blocată intenționat pentru proiectele remote — „La distanță”).
- Vizibilitate pe proces: câmpul „Vizibil doar pentru” (tab „Responsabil”, editabil doar de Admin procese) restrânge procesul, pașii, testele, problemele și rândurile din rapoarte la utilizatorii din listă; gol înseamnă vizibil tuturor.
- Securitate și chatter: majoritatea înregistrărilor moștenesc `mail.thread`/activity pentru urmăritori, jurnalizare și notificări, abonând automat participanții cheie; la crearea unei probleme și la aprobarea unei dezvoltări pleacă e-mailuri automate către managerul de proiect.

Detaliile pas-cu-pas (configurare inițială, fluxul complet, tabele de stări, mesaje de eroare frecvente) sunt în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

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

- [l10n_ro_process_library](../l10n_ro_process_library/index.md): biblioteca de procese RO (contabilitate, TVA, declarații ANAF, trezorerie, imobilizări, stocuri); instalarea ei le face disponibile la „Import din bibliotecă".
- `l10n_ro_doc_screenshots`: generează capturile fișei consultant a acestui modul (dependență doar pentru teste).
