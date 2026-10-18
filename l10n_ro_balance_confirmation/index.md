# Romania - Confirmare de sold (localizat la `l10n_ro_balance_confirmation/index.md`)

- **Nume Tehnic:** `l10n_ro_balance_confirmation`
- **Versiune:** `19.0.2.3.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_balance_confirmation
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_balance_confirmation`
- **Ultima Ingestie:** `2026-10-14`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul generează documente de confirmare a soldului (extras de cont) pentru partenerii de afaceri, conform cerințelor contabile din România. Combină două fluxuri complementare: tipărirea la cerere pentru unul sau mai mulți parteneri la o dată aleasă și o campanie de trimitere în masă prin email, cu un document dedicat care păstrează câte o linie per partener și urmărește starea fiecărei confirmări. Extrasul arată soldul la dată, documentele rămase deschise la acea dată, defalcarea pe monede și semnăturile conducerii. Emailul campaniei rămâne în chatterul partenerului, iar răspunsul partenerului intră în același fir și marchează linia; contabilul decide apoi dacă soldul e confirmat sau nu. Ajută firmele să deruleze campanii periodice de reconciliere a soldurilor, să urmărească soldurile neconfirmate la inventariere și să păstreze un istoric auditabil al comunicării cu partenerii.

#### 2. Funcționalități Cheie

- **Tipărire la cerere**: din **Facturare → Clienți → Clienți**, se bifează partenerii și se alege **Tipăriți → Confirmare sold**. Dialogul cere data confirmării, data emiterii, tipul de partener (client / furnizor / ambele), termenul de răspuns (zile), afișarea avansurilor și opțiunile documentului. Rezultatul e un PDF cu câte un extras per partener.
- **Soldul la o dată specifică**: calculat ca sumă `debit - credit` a liniilor postate până la dată, independent de reconcilierile ulterioare. Pe planul de conturi românesc se confirmă doar conturile comerciale (clienți 411x/413x, furnizori 401x/403x/404x); conturi precum 461, 462, 421 sau 4551 sunt excluse. Pe alt plan de conturi filtrarea rămâne după tipul contului.
- **Documente deschise la data confirmării** *(nou)*: sub sold apare tabelul documentelor deschise (tip și număr, plus numărul furnizorului la facturile de achiziție, dată, scadență, valoare inițială, rest de plată). Restul se calculează **la data confirmării**, scăzând doar reconcilierile parțiale cu `max_date` ≤ dată: o factură achitată ulterior apare integral. Plățile, avansurile și notele nealocate pot fi listate separat; totalul tabelului egalează soldul.
- **Confirmare în valută** *(nou)*: documentele sunt grupate pe monedă, cu suma în valută și contravaloarea în lei la cursul documentelor. Filtru de monedă: toate, doar moneda companiei sau o anumită monedă.
- **Export XLSX** *(nou)*: documentele deschise (partener, CIF, tip cont, tip document, număr, dată, scadență, monedă, valoare inițială și rest, în valută și în lei), din dialogul de tipărire și din campanie.
- **Avansuri**: soldurile conturilor 409/419, calculate la data confirmării, tipărite pe rânduri separate sub soldul principal.
- **Semnături cu nume și funcție** *(nou)*: conducătorul unității și conducătorul compartimentului financiar-contabil, cu valori implicite pe companie (**Setări → Utilizatori și companii → Companii**, fila **Confirmare sold**), modificabile la fiecare tipărire sau campanie. Titlul documentului e editabil (implicit „EXTRAS DE CONT”).
- **Șablon de document**: emitent și destinatar, textul standard de confirmare și formular de răspuns (sumă confirmată în moneda documentului, modalitate de plată, obiecții, semnături). Partenerii din România primesc documentul în română, ceilalți în limba lor.
- **Campanie pe email cu urmărire**: document numerotat `CONF/YYYY/00001` (**Facturare → Clienți → Confirmări de sold**), cu flux `draft → generated → sent → done`. Scop pe parteneri sau pe tip de cont (creanțe / datorii / ambele), opțiunea **Doar cu sold**; partenerii se aleg după soldul la dată, nu după starea de reconciliere de azi. Câte o linie per partener (`ready` / `no email` / `sent` / `error`) cu soldul, PDF-ul atașat și data trimiterii. Butoane: **Generează liniile → Generează PDF-urile → Trimite email-urile** sau **Generează și trimite**. Șablon de email bilingv (RO/EN, după limba de pe fișa partenerului) cu PDF atașat, postat în **chatterul partenerului** (fără copie la urmăritorii fișei). Contoare live și istoric în chatter.
- **Urmărirea răspunsurilor** *(nou, 19.0.2.3.0)*: răspunsul partenerului la emailul confirmării (prin catchall) intră în chatterul lui și trece linia din **Așteaptă răspuns** în **Răspuns primit**, cu notă în chatterul campaniei. Un email nou al partenerului, care nu e răspuns la confirmare, nu atinge linia. Contabilul marchează linia **Confirmat** sau **Neconfirmat**; la neconfirmare completează soldul declarat de partener, iar **Diferența** (sold nostru − sold partener) se calculează automat, cu observații. Campania are contoare pe răspunsuri și butonul **Răspunsuri de verificat**; meniul **Facturare → Clienți → Răspunsuri la confirmările de sold** listează liniile trimise din toate campaniile, cu filtre pe răspuns, pentru situația soldurilor neconfirmate și în litigiu de la inventariere.
- **Reluare după erori**: o eroare de la serverul de email (SMTP) duce linia în starea `error`, cu mesajul serverului; **Trimite email-urile** retrimite liniile cu eroare și pe cele fără email care au primit între timp o adresă.
- **Drepturi de acces**: grupurile „Poate tipări confirmare sold” și „Trimitere confirmări de sold”. Cu Contabilitate (Enterprise) le primesc rolurile Contabil și Administrator; doar cu Facturare (Community) le primește rolul Administrator.
- **Cerințe**: partenerii din campanie trebuie să aibă email completat, iar serverul de email de ieșire trebuie configurat. Ca răspunsurile să intre automat în Odoo: domeniu de alias, adresă catchall și server de email de intrare; fără ele, emailul apare tot în chatterul partenerului, dar linia se marchează manual.

#### 3. Dependențe

- `account`
- `l10n_ro`
- `mail`

#### 4. Componente Cheie

**Modele**

- `res.partner` (`models/res_partner.py`): `_credit_debit_get` cu context `date_to` pentru soldurile de încasat/plătit la o dată dată; `_message_post_after_hook` leagă emailul primit (`parent_id` = mesajul confirmării) de linia campaniei.
- `account.move.line` (`models/account_move_line.py`): suport pentru calculul soldurilor și al restului la dată istorică.
- `res.company` (`models/res_company.py`): numele și funcția semnatarilor impliciți.
- `l10n.ro.balance.confirmation.options` (`models/l10n_ro_balance_confirmation_options.py`): model abstract cu opțiunile documentului (documente deschise, filtru de monedă, titlu, semnatari), comun dialogului de tipărire și campaniei.
- `l10n.ro.balance.confirmation` (`models/l10n_ro_balance_confirmation.py`): documentul de campanie, cu numerotare, dată de referință, tip de cont, filtrare parteneri și flux `draft → generated → sent → done`.
- `l10n.ro.balance.confirmation.line` (`models/l10n_ro_balance_confirmation_line.py`): linia per partener, cu stare, sold, PDF atașat și data trimiterii; mesajul trimis (`mail_message_id`), starea răspunsului (`response_state`: pending / replied / confirmed / disputed), data și mesajul răspunsului, soldul partenerului, diferența și observațiile. Trimiterea se face cu `message_post` pe partener, sincron, ca eroarea SMTP să marcheze linia.
- `l10n_ro.balance_confirm_dialog` (`wizard/confirm_balance.py`): dialogul de tipărire la cerere.
- `report.l10n_ro_balance_confirmation.report_partner_balance` (`report/res_partner.py`): raport QWeb cu logica de calcul a documentelor deschise, a restului la dată și a grupării pe monede.

**Vizualizări**

- `views/res_partner_balance.xml`: șablonul QWeb al extrasului și acțiunea de raport (`action_report_partner_balance`).
- `wizard/confirm_balance.xml`: dialogul și acțiunea de tipărire (`action_balance_confirmation`).
- `l10n_ro_balance_confirmation_view_form` / `l10n_ro_balance_confirmation_view_list`: formular și listă pentru campanie, cu contoare și fila **Document**.
- `l10n_ro_balance_confirmation_line_view_list` / `l10n_ro_balance_confirmation_line_view_search` / `l10n_ro_balance_confirmation_line_action`: lista editabilă a răspunsurilor, cu filtre și grupări, sub meniul `menu_l10n_ro_balance_confirmation_line`.
- `view_company_form_balance_confirmation`: fila **Confirmare sold** pe companie, pentru semnatarii impliciți.

**Acțiuni Automate / Acțiuni Server**

- Nu are cron-uri sau acțiuni server. Datele: `seq_balance_confirmation` (secvența `CONF/YYYY/00001`) și `mail_template_balance_confirmation` (șablonul de email bilingv). Securitate: grupurile `group_print_balance` și `group_balance_confirmation_send`, plus regulile multi-companie `balance_confirmation_company_rule` și `balance_confirmation_line_company_rule`.

#### 5. Conexiuni

- `account`: sursa soldurilor și a reconcilierilor parțiale (`account.partial.reconcile`) folosite la calculul restului la dată.
- `l10n_ro`: planul de conturi românesc, pe baza căruia se filtrează conturile comerciale.
- `mail`: trimiterea emailurilor prin chatterul partenerului, primirea răspunsurilor prin gateway și chatter-ul campaniei.
- [l10n_ro_partner_trial_balance](../l10n_ro_partner_trial_balance/index.md): balanța analitică pe parteneri pentru bănci, cu aceeași convenție a avansurilor 409 / 419 legate de partener; marchează 421 / 425 / 463 necomerciale, deci le scoate din filtrul comercial.
