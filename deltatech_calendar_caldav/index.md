# Sincronizare Calendar CalDAV

- **Nume Tehnic:** `deltatech_calendar_caldav`
- **Versiune:** `19.0.3.2.4`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_calendar_caldav`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_calendar_caldav`
- **Ultima Ingestie:** `2026-09-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul sincronizează calendarul Odoo (`calendar.event`) cu un server CalDAV extern (cPanel/Horde/SOGo, Nextcloud, sau orice server care implementează standardul CalDAV RFC 4791), în ambele direcții. Un cron (sau butonul „Sync Now") aduce evenimentele de pe server în Odoo; crearea, modificarea sau ștergerea unui eveniment Odoo pentru un utilizator cu cont CalDAV configurat trimite imediat schimbarea pe server. Spre deosebire de Google Calendar/Microsoft 365 (sincronizate nativ de Odoo), CalDAV nu are conector nativ — acest modul umple acel gol, generic, fără cod specific per furnizor.

#### 2. Funcționalități Cheie

- Sincronizare bidirecțională CalDAV ↔ Odoo (pull programat/manual + push imediat la create/write/unlink).
- Evenimente recurente: o serie recurentă Odoo se trimite ca **o singură resursă CalDAV** (eveniment „master" cu regulă `RRULE`), nu ca evenimente separate; ocurențele aduse de pe server sunt expandate și importate individual, mapate pe `calendar.recurrence` nativ al Odoo (nu mai apar ca evenimente „orfane").
- Reminder-e: alarmele Odoo (`calendar.alarm`) se mapează pe/din componente `VALARM` (notificare → `DISPLAY`, email → `EMAIL`).
- Participanți: `partner_ids`/organizatorul se mapează pe/din `ATTENDEE`/`ORGANIZER`, cu potrivire automată a contactelor după adresa de email (creare automată dacă lipsesc).
- Detectare conflicte (ETag): înainte de a suprascrie un eveniment pe server, verifică dacă acesta s-a schimbat de la ultima sincronizare; dacă da, push-ul e sărit (serverul câștigă), nu suprascrie orbește.
- Detectare schimbări (CTag): verifică marca de schimbare a colecției înainte de fiecare sincronizare; dacă nimic nu s-a schimbat, sare peste pull-ul complet.
- Cont personal pentru fiecare utilizator: intrarea **Calendar > My Calendars** deschide propriul cont CalDAV al utilizatorului (setările serverului apar doar în citire, iar parola o poate introduce chiar titularul); o regulă de acces îl ține pe propria înregistrare, iar crearea și ștergerea conturilor rămân în sarcina administratorului (**Settings > Technical > CalDAV Accounts**).
- Evenimentele importate îl listează mereu pe proprietarul calendarului ca participant, astfel încât intervalul ocupat să fie raportat corect paginilor de programări (Odoo deduce ocupat/liber din `partner_ids`).
- Timeout de 30 de secunde pe conexiunea CalDAV: un server care nu răspunde nu mai blochează cronul sau butonul Test Connection.
- Comportamente așteptate: ștergerea unei singure ocurențe dintr-o serie în Odoo nu se trimite pe server; o ocurență mutată și editată poate apărea pe server ca eveniment separat.
- Pull-ul scrie doar câmpurile care s-au schimbat efectiv, ca sincronizarea să nu rupă o serie recurentă existentă rescriind inutil `start`/`stop` pe ocurențe neschimbate.

#### 3. Dependențe

- `calendar`

#### 4. Componente Cheie

**Modele**

- `caldav.account` (model nou): un cont = un calendar CalDAV — `url`, `username`, `password` (restricționat la grupul Setări), `calendar_url` (descoperit automat la Test Connection), `user_id` (proprietarul evenimentelor sincronizate), `sync_days_past`/`sync_days_future` (fereastra de sincronizare, implicit -7/+90 zile), `last_sync`/`last_sync_status`/`last_ctag`. Conține logica de conectare (`caldav`/`icalendar`), construirea/parsarea iCalendar (RRULE, VALARM, ATTENDEE/ORGANIZER) și push/pull. Pull-ul cere resursa brută de pe server (`expand=False`, nu expandată) și mapează `RRULE`-ul pe `calendar.recurrence` nativ al Odoo, astfel încât o serie rămâne o singură serie; ocurențele-excepție (`RECURRENCE-ID`) sunt atașate ocurenței cărora le aparțin, nu create ca evenimente noi. Fusul orar al recurenței se ia doar dintr-un `TZID` explicit trimis de server (nu mai cade pe fusul orar al utilizatorului curent).
- `calendar.event` (extindere): câmpuri noi `caldav_account_id`, `caldav_uid` (identificatorul pe server), `caldav_recurrence_id` (pentru o ocurență a unei serii), `caldav_etag`; suprascrie `create`/`write`/`unlink` pentru a trimite schimbările pe serverul CalDAV al contului asociat utilizatorului evenimentului (operațiune rulată `sudo`, ca sincronizarea să nu depindă de drepturile utilizatorului curent pe `caldav.account`).

**Securitate**

- Regulă de acces `caldav_account_rule_own`: utilizatorul intern vede doar contul al cărui proprietar este; `caldav_account_rule_manager` dă acces complet grupului Setări. Utilizatorii interni au drept de citire/scriere, fără creare/ștergere.

**Vizualizări**

- `view_caldav_account_form`: formularul contului, cu butoanele **Test Connection** și **Sync Now**, butonul-statistică **Events** (evenimentele sincronizate) și secțiunea de sincronizare (zile trecut/viitor, ultima sincronizare, status, ctag).
- `view_caldav_account_tree`: lista conturilor CalDAV (nume, proprietar, URL, ultima sincronizare, status).
- `view_caldav_account_form_user` / `view_caldav_account_tree_user` / `action_caldav_account_user`: ecranul **My Calendars** pentru titularul contului (setări server în citire, parola editabilă).
- `action_caldav_synced_events`: acțiune care deschide evenimentele legate de un cont CalDAV (listă/formular/calendar).

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_caldav_sync` (`ir.cron`, dezactivat implicit, interval 15 minute): rulează `caldav.account._cron_sync_accounts()`, care sincronizează toate conturile active.

#### 5. Conexiuni

- `calendar`: datele sincronizate sunt evenimentele native de calendar ale utilizatorului — modulul nu introduce o interfață separată, folosește aplicația Calendar existentă.
