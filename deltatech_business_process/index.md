# Business process (localizat la `deltatech_business_process/index.md`)

- **Nume Tehnic:** `deltatech_business_process`
- **Versiune:** `19.0.1.4.9`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_business_process
- **Cale Locală:** `odoo-addons/deltatech/deltatech_business_process`
- **Ultima Ingestie:** `2026-06-01`

#### 1. Sumar

Modulul ajută echipele de implementare să structureze și să execute proiectele de implementare Odoo într-un mod controlat. Introduce conceptele de Proiect, Procese de Afaceri și Pașii acestora, împreună cu fluxuri de Testare și de gestionare a Problemelor (issues), astfel încât procesele să poată fi proiectate, validate și livrate ordonat. Valoarea principală constă în faptul că oferă un spațiu de lucru unic în care un proiect este descompus în procese, fiecare proces în pași, iar pașii pot fi testați și corectați până la momentul punerii în producție, cu evidența documentelor, a responsabililor și a progresului pe parcursul întregului ciclu.

#### 2. Funcționalități Cheie

- Spațiu de lucru pentru proiect: gestionează proiectele de implementare, fazele și progresul general.
- Procese de afaceri: definește procese per proiect, grupate pe zonă de afaceri și, opțional, pe grup de procese.
- Pași: descompune fiecare proces în pași ordonați, cu responsabili și tranzacții asociate.
- Testare: creează teste Interne, de Integrare și de Acceptanță de Utilizator (UAT) care reflectă pașii procesului și urmăresc starea și rezultatul execuției pentru fiecare pas.
- Probleme (issues): înregistrează problemele apărute la testare sau în execuție pe un proces ori pe un pas specific de test, le urmărește prin stări și le închide cu validări.
- Dezvoltări: leagă elementele de dezvoltare de procese și/sau proiecte pentru a urmări personalizările necesare.
- Atașamente: acces rapid la toate documentele asociate proiectului, proceselor, pașilor, testelor și problemelor.
- Rapoarte: tipărește rapoartele de Proces de Afaceri și de Test de Proces; exportă/importă procese ca JSON pentru reutilizare.
- Raport Excel: generează din proiect un sumar Excel care grupează procesele pe zonă și agregă duratele de configurare/instruire/testare/migrare de date, evidențiind procesele cu durată totală zero.
- Securitate și chatter: majoritatea înregistrărilor moștenesc `mail.thread`/activity pentru urmăritori, jurnalizare și notificări, abonând automat participanții cheie.

#### 3. Dependențe

- `base`
- `mail`

#### 4. Componente Cheie

**Modele** (conform secțiunii „Data model at a glance" din `readme/DESCRIPTION.md`)

- `business.project`: containerul proiectului; agregă procesele, problemele, dezvoltările și atașamentele; poate genera un raport sumar Excel.
- `business.process`: entitatea centrală care descrie un proces într-un proiect; are pași, teste, dezvoltări și contoare calculate.
- `business.process.step`: o activitate ordonată dintr-un proces; poate referi o tranzacție de afaceri și un partener responsabil.
- `business.process.test`: o instanță de test pentru un proces (domeniu: intern/integrare/acceptanță de utilizator); generează automat testele de pas și urmărește progresul și finalizarea.
- `business.process.step.test`: oglindește un pas de proces pentru un test specific; înregistrează date, rezultat (ciornă/trecut/eșuat) și observații; numără problemele asociate.
- `business.issue`: probleme descoperite la testare sau în execuție; ciclu de viață ciornă → deschis/alocat → rezolvat/în test → închis/redeschis; integrat cu urmăritori și email.
- `business.development` (+ tip): dezvoltări de referință legate de procese/proiecte; pot contribui la durata proiectului.
- `business.area` și `business.process.group`: clasifică procesele pe zonă și pe grup.

**Vizualizări**

- Vizualizări de formular și listă pentru proiecte, procese, pași, teste și probleme (definite în `views/`).
- Rapoarte QWeb pentru Procesul de Afaceri și Testul de Proces (definite în `report/`).

**Acțiuni Automate / Acțiuni Server**

- Secvențe definite în `data/ir_sequence_data.xml` și șabloane de email în `data/email_templates.xml`, încărcate la instalare.
- Vrăjitoare de export/import procese ca JSON (`wizard/`): exportul din lista de procese (cu opțiuni pentru teste, responsabil, client și suport) și importul dintr-un JSON pe formularul proiectului.

#### 5. Conexiuni

- Nu sunt declarate conexiuni funcționale către alte module documentate în wiki. Modulul depinde doar de `base` și `mail`.
