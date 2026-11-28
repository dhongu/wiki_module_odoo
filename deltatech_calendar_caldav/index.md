# Calendar CalDAV Sync (localizat la `deltatech_calendar_caldav/index.md`)

- **Nume Tehnic:** `deltatech_calendar_caldav`
- **Versiune:** `20.0.3.3.1`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_calendar_caldav`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_calendar_caldav`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul sincronizează în ambele sensuri evenimentele dintre un server CalDAV extern (de exemplu un calendar găzduit în cPanel sau orice furnizor CalDAV standard) și calendarul Odoo. Un cont CalDAV oglindește un calendar Odoo, iar acesta poate fi partajat cu alți utilizatori, care văd și editează aceleași programări fără să aibă un cont CalDAV propriu.

#### 2. Funcționalități Cheie

- CalDAV către Odoo: o acțiune programată (sau butonul **Sync Now**) aduce evenimentele de pe server. Odoo către CalDAV: crearea, modificarea sau ștergerea unui eveniment se trimite imediat pe server.
- Evenimente recurente (RRULE): o serie Odoo ajunge pe server ca un singur eveniment-master, iar o serie de pe server se importă ca o singură serie Odoo.
- Memento-uri (VALARM): notificare devine `DISPLAY`, email devine `EMAIL`.
- Participanți: liniile `ATTENDEE` / `ORGANIZER` se mapează pe participanți; contactele se potrivesc după email sau se creează. Proprietarul calendarului apare mereu ca participant.
- Detectarea conflictelor (ETag): dacă e modificat pe server, push-ul local este sărit, iar următoarea sincronizare aduce versiunea serverului. Detectarea schimbărilor (CTag): dacă nimic nu s-a schimbat, aducerea se omite.
- Un singur eveniment Odoo per eveniment de server (UID); îl păstrează contul organizatorului.
- Configurare: **Setări > Tehnic > CalDAV Accounts** (mod dezvoltator) sau, pentru titular, **Calendar > My Calendars**; câmpuri **Server URL**, **Username**, **Password**, **Owner**, **Odoo Calendar**; **Test Connection** descoperă calendarul și completează **Calendar Url**; **Sync Days Past / Future** (implicit 7 și 90 de zile).
- Partajare: calendarul Odoo al proprietarului se partajează prin **Shared with**, cu **Default visibility** pe **Shared Calendar Members Only** sau **Public**; nu se dă asistentului un al doilea cont CalDAV pe același calendar.
- Acțiunea programată este dezactivată după instalare și se activează din **Setări > Tehnic > Scheduled Actions**.
- Securitate: parola CalDAV se stochează în clar pe cont (de preferat o parolă de aplicație); doar administratorii schimbă câmpurile de server, iar proprietarul poate schimba parola. Biblioteca Python `caldav` trebuie instalată în intervalul `>=1.3.9,<=2.0.1`.
- Limitări: ștergerea unei singure ocurențe dintr-o serie nu se trimite pe server; o ocurență modificată și mutată poate crea un duplicat pe server.
- Fluxul pas-cu-pas, cu capturi, este în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `calendar`

Dependențe externe Python: `caldav`, `icalendar`.

#### 4. Componente Cheie

**Modele**

- `caldav.account` (nou): un cont este un calendar CalDAV, cu URL, utilizator, parolă, `calendar_url` descoperit automat, proprietar, fereastra de sincronizare și starea ultimei rulări (data, status, ctag).
- `calendar.event` (extins): câmpuri `caldav_account_id`, `caldav_uid`, `caldav_recurrence_id`, `caldav_etag`; la `create` / `write` / `unlink` trimite modificările pe serverul contului asociat.

**Vizualizări**

- `view_caldav_account_form` / `view_caldav_account_tree`: formularul (cu **Test Connection**, **Sync Now** și butonul **Events**) și lista conturilor, pentru administratori.
- `view_caldav_account_form_user` / `view_caldav_account_tree_user`: variantele pentru titularul contului.
- `view_calendar_event_list_caldav` / `view_calendar_event_search_caldav`: lista și căutarea evenimentelor sincronizate.
- `action_caldav_synced_events`: deschide evenimentele legate de un cont.

**Acțiuni Automate / Acțiuni Server**

- `CalDAV: Sync Accounts` (`ir.cron`, dezactivat implicit, la 15 minute): rulează `caldav.account._cron_sync_accounts()` pentru conturile active.

#### 5. Conexiuni

- `calendar`: evenimentele sincronizate sunt reuniunile native Odoo, vizibile în aplicația Calendar și luate în calcul la disponibilitate.
