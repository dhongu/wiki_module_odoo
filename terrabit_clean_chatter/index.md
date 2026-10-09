# Terrabit Clean Chatter (localizat la `terrabit_clean_chatter/index.md`)

- **Nume Tehnic:** `terrabit_clean_chatter`
- **Versiune:** `19.0.1.0.12`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_clean_chatter
- **Cale Locală:** `odoo-addons/terrabit/terrabit_clean_chatter`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul curăță chatter-ul tichetelor de helpdesk primite prin email de citatele integrale ale firului anterior, de semnăturile grafice (tabele cu logo și date de contact) și de disclaimerele de confidențialitate/GDPR, păstrând doar mesajul real al clientului. Deduplică atașamentele identice rămase orfane și șterge pozele minuscule (logo-uri de semnătură, pixeli de urmărire). Tichetele devin mai ușor de citit, iar baza de date și stocarea de fișiere scad. Aceleași reguli se pot aplica și pe task-urile de proiect și pe lead-urile CRM.

#### 2. Funcționalități Cheie

- Eliminare citate, semnături grafice și disclaimere din reply-urile primite pe email; mesajul de creare al tichetului nu este niciodată modificat, iar tichetele cu marcaje de migrare Freshdesk rămân neatinse.
- Deduplicare atașamente identice orfane și ștergere a oricărei imagini de cel mult 1 KB.
- Rulare pe loturi (implicit 1000 de tichete), doar pe tichete create de mai mult de 30 de zile, cu progres reținut între rulări (cursor) și procesare pe sub-loturi de 100 cu salvare după fiecare.
- Rulare manuală din *Helpdesk > Configurare > Curățare chatter*, prin ⚙ Acțiuni → **Rulează curățarea acum**.
- Cron zilnic pe helpdesk și cron zilnic separat pe task-uri de proiect, ambele dezactivate implicit, cu cursoare independente.
- Acțiunea **Curăță chatter** din meniul ⚙ Acțiuni al tichetelor, task-urilor și lead-urilor: curăță imediat înregistrările selectate, fără prag de vârstă și fără cursor (utilă pe tichete recente sau cu reply-uri noi după o curățare anterioară). Rulările pe task-uri apar în *Proiect > Configurare > Curățare chatter (task-uri)*.
- Rezultatul fiecărei rulări (tichete scanate, mesaje curățate, mesaje sărite, atașamente duplicate șterse, bytes eliberați, log pe tichet) se vede în lista de rulări; progresul apare în timp real în Setări → Tehnic → Jurnalizare.
- Backup complet (body original și atașamentele șterse) și rollback prin butonul **Restore** pe o rulare finalizată.
- Acces: manageri helpdesk, manageri proiect și administratori.

#### 3. Dependențe

- `helpdesk`
- `project`
- `crm`

#### 4. Componente Cheie

**Modele**

- `chatter.cleanup.run`: o rulare de curățare (manuală sau cron); ține contoarele, cursorul, log-ul, acțiunile de rulare și de restaurare.
- `chatter.cleanup.run.message`: backup-ul mesajelor modificate (body original), folosit la rollback.
- `chatter.cleanup.run.attachment`: backup-ul atașamentelor șterse, recreate la restaurare.
- `models/chatter_cleaner_engine.py`: motor de curățare a HTML-ului (funcția `clean_reply_body`), fără model propriu.

**Vizualizări**

- `chatter.cleanup.run.list` / `chatter.cleanup.run.form`: lista și formularul rulărilor, cu butonul Restore.
- Acțiuni server **Curăță chatter** legate de `helpdesk.ticket`, `project.task` și `crm.lead`; meniuri de configurare pentru helpdesk și proiect.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_chatter_cleanup`: „Terrabit: curățare chatter tichete helpdesk”, zilnic, dezactivat implicit.
- `ir_cron_chatter_cleanup_task`: „Terrabit: curățare chatter task-uri proiect”, zilnic, dezactivat implicit.
- Acțiunea server „Rulează curățarea acum” pe lista rulărilor.

#### 5. Conexiuni

- `helpdesk`, `project`, `crm`: modelele pe care se aplică curățarea (tichete, task-uri, lead-uri).
