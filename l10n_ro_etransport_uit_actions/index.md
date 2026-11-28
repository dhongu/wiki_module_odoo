# e-Transport UIT Actions (localizat la `l10n_ro_etransport_uit_actions/index.md`)

- **Nume Tehnic:** `l10n_ro_etransport_uit_actions`
- **Versiune:** `20.0.1.2.0`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_etransport_uit_actions
- **Cale Locală:** odoo-addons/l10n-romania/l10n_ro_etransport_uit_actions
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Permite trimiterea la ANAF, direct din transfer, a evenimentelor ulterioare unui UIT e-Transport: ștergerea notificării, confirmarea sosirii mărfii și schimbarea vehiculului. Fiecare eveniment este urmărit separat, iar efectele se aplică pe transfer abia după ce ANAF îl validează.

#### 2. Funcționalități Cheie

- Trei acțiuni pe un transfer cu notificare **Validată**: **Șterge UIT** (DEL), **Confirmă UIT** (CON: confirmat, parțial confirmat sau refuzat, cu observație) și **Schimbă vehiculul** (MVH: noile numere de vehicul și remorcă, cu data modificării).
- Un singur dialog, cu acțiunea presetată de butonul apăsat; opțional observație și indicatorul de declarație post-avarie (`declPostAvarie`, OUG 41/2022).
- Fiecare eveniment este o înregistrare proprie (`l10n.ro.etransport.event`), cu XML-ul trimis, indexul de încărcare ANAF și starea proprie: Trimis, apoi Validat sau Eroare. Starea notificării standard nu se modifică.
- ANAF răspunde la upload doar cu un index de încărcare; starea se verifică automat la 15 minute sau la cerere (**Fetch Event Status**). Cât timp un eveniment e în așteptare, nu se poate trimite altul pentru același UIT.
- Noul număr de vehicul și marcajul „UIT șters” se aplică doar după validarea de la ANAF; după o ștergere validată apare un banner roșu și nu se mai oferă acțiuni.
- Anularea unui transfer cu UIT valabil trece prin ștergere: **Anulează** deschide dialogul DEL, iar transferul se anulează imediat ce ANAF primește ștergerea. Dacă ștergerea e refuzată ulterior, se programează o activitate de avertizare. Anulările din cod (ex. la anularea comenzii de vânzare) nu sunt afectate.
- Configurare: doar setările e-Transport standard (token ANAF, mediu test/producție); acțiunea programată se ajustează din Setări, Tehnic, Automatizare.
- Fluxul detaliat este în fișa consultant.

#### 3. Dependențe

- [l10n_ro_etransport_enhancement](../l10n_ro_etransport_enhancement/index.md)

#### 4. Componente Cheie

Descrierea modulului nu cere analiză de cod; mai jos, componentele principale.

**Modele**

- `l10n.ro.etransport.event`: evenimentul trimis la ANAF (tip, XML, index încărcare, stare).
- `l10n.ro.etransport.action.wizard`: dialogul de trimitere a evenimentelor DEL, CON, MVH.
- `stock.picking`: butoane, tabel de evenimente și blocarea anulării cu UIT valabil.

**Vizualizări**

- `views/etransport_event_view.xml`: evenimentele UIT.
- `wizards/etransport_action_wizard_view.xml`: dialogul de trimitere.
- `views/stock_picking_view.xml`: butoanele din antet și tabelul **UIT Events** din tab-ul eTransport.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_etransport_event_fetch_status`: „RO e-Transport: UIT event status update”, rulează la 15 minute și actualizează starea evenimentelor.

#### 5. Conexiuni

- [l10n_ro_etransport_enhancement](../l10n_ro_etransport_enhancement/index.md): declarația e-Transport de bază, pe care se aplică evenimentele.
- [l10n_ro_etransport_uit_actions_batch](../l10n_ro_etransport_uit_actions_batch/index.md): aceleași acțiuni pentru loturi de transferuri.
