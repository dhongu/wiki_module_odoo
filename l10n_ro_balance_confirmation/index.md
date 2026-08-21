# Romania - Balance Confirmation (localizat la `l10n_ro_balance_confirmation/index.md`)

- **Nume Tehnic:** `l10n_ro_balance_confirmation`
- **Versiune:** `19.0.2.1.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_balance_confirmation
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_balance_confirmation`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul „Romania - Balance Confirmation" generează documente de confirmare a soldului pentru partenerii de afaceri, conform cerințelor contabile din România. Combină două fluxuri complementare: tipărirea la cerere a extrasului de cont pentru unul sau mai mulți parteneri la o dată aleasă, și o campanie de trimitere în masă prin email, cu un document dedicat care păstrează câte o linie per partener și urmărește starea fiecărei confirmări (generată, trimisă, cu eroare). Ajută firmele să deruleze campanii periodice de reconciliere a soldurilor și să păstreze un istoric auditabil al comunicării cu partenerii.

#### 2. Funcționalități Cheie

- **Generarea extrasului de cont**: creează extrase de cont pentru parteneri la o dată specificată, în format standard românesc, cu generare PDF și posibilitatea selectării mai multor parteneri pentru generare în lot.
- **Trimitere în masă prin email, cu urmărire** *(nou)*: un document persistent numerotat `CONF/YYYY/00001`, cu flux `draft → generated → sent → done`; câte o linie per partener cu propria stare (`ready` / `no email` / `sent` / `error`), soldul la data de referință, PDF-ul atașat și data trimiterii. Șablon de email bilingv (RO/EN, după limba partenerului) cu PDF-ul de confirmare atașat. Buton unic **Generare linii → Randare PDF-uri → Trimitere email-uri** (sau **Generează și trimite**). Scop configurabil pe parteneri sau pe tip de cont (de încasat / de plătit / ambele), cu opțiunea de a sări peste soldurile zero. Contoare live (ready / trimise / fără email / eroare) și istoric complet în chatter.
- **Calculul soldului la o dată specifică**: calcul precis al soldurilor partenerilor la o dată dată, cu suport pentru debite și credite, extinzând funcționalitatea nativă Odoo pentru raportare la dată istorică și afișarea corectă a soldurilor în moneda companiei.
- **Șablon de document personalizat**: format standard de extras de cont conform normelor românești, cu secțiune pentru emitent (companie) și destinatar (partener), afișarea soldului la data specificată, textul standard de confirmare și un formular de răspuns integrat (sumă confirmată, modalitate de plată, obiecții, semnături). Parametri configurabili ai documentului: data emiterii, numărul documentului, termenul de răspuns recomandat (în zile), tipul de partener (client / furnizor / ambele — comută soldul de încasat/plătit afișat) și soldul opțional de avans (conturile 409/419) afișat sub soldul principal.

#### 3. Dependențe

- `account`
- `l10n_ro`
- `l10n_ro_report_common`
- `mail`

#### 4. Componente Cheie

Conform secțiunii „Technical Implementation" din `readme/DESCRIPTION.md`, completată cu structura fișierelor din modul:

**Modele**

- `res.partner` (`models/res_partner.py`): extins pentru calculul soldurilor de încasat/plătit la o dată dată, prin `_credit_debit_get` cu context `date_to`, implementat cu `_read_group` peste `amount_residual` (compatibil Odoo 19).
- `account.move.line` (`models/account_move_line.py`): suport pentru calculul soldurilor la dată istorică.
- `l10n.ro.balance.confirmation` (`models/l10n_ro_balance_confirmation.py`): documentul de campanie (batch) cu numerotare, dată de referință, tip de cont, filtrare parteneri și flux `draft → generated → sent → done`.
- `l10n.ro.balance.confirmation.line` (`models/l10n_ro_balance_confirmation_line.py`): linia per partener din campanie, cu starea proprie (`ready` / `no email` / `sent` / `error`), soldul calculat, PDF-ul atașat și data trimiterii.

**Vizualizări**

- `res_partner_balance.xml`: acțiune/wizard de tipărire a confirmării de sold direct din fișa partenerului.
- `l10n_ro_balance_confirmation_views.xml`: formular și listă pentru documentul de campanie și liniile aferente, cu contoare (ready / trimise / fără email / eroare).
- `wizard/confirm_balance.xml`: wizard-ul (`l10n_ro.balance_confirm_dialog`) pentru tipărirea la cerere, cu selectarea datei și a partenerilor.

**Rapoarte**

- Șablon QWeb pentru extrasul de cont (confirmarea de sold), în format standard românesc, cu formular de răspuns integrat.

**Date**

- `data/sequence_data.xml`: secvența de numerotare a documentelor de campanie (`CONF/YYYY/00001`).
- `data/mail_template_data.xml`: șablonul de email bilingv (RO/EN) folosit la trimiterea în masă a confirmărilor.

#### 5. Conexiuni

- `account`: contabilitatea de bază, sursa soldurilor (`amount_residual`) folosite în confirmare.
- `l10n_ro`: localizarea românească pe care se sprijină formatul documentului.
- `l10n_ro_report_common`: componentele de raportare comune pentru localizarea românească, reutilizate de șablonul QWeb.
- `mail`: infrastructura de trimitere email și tracking (chatter) folosită de campania în masă.
