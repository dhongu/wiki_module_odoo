# eTransport UIT Actions (localizat la `l10n_ro_etransport_uit_actions/index.md`)

- **Nume Tehnic:** `l10n_ro_etransport_uit_actions`
- **Versiune:** `19.0.1.1.2`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_etransport_uit_actions
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_etransport_uit_actions`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul permite transmiterea către ANAF, direct din transferul de stoc, a evenimentelor care urmează după o notificare eTransport cu cod UIT deja validată: ștergerea UIT-ului, confirmarea lui sau schimbarea vehiculului. Fiecare eveniment este o înregistrare proprie, cu starea lui, iar starea notificării din modulul standard rămâne neatinsă, astfel încât fluxurile existente continuă să funcționeze la fel.

#### 2. Funcționalități Cheie

- **Ștergere (DEL):** invalidează notificarea; marfa nu mai poate circula sub acel UIT. După validarea ștergerii, transferul afișează bannerul roșu „UIT deleted" și nu mai oferă alte acțiuni; pentru transport trebuie trimisă o notificare nouă.
- **Confirmare (CON):** confirmat / parțial confirmat / refuzat, cu observație opțională.
- **Schimbare vehicul (MVH):** numere noi pentru vehicul și remorcă, cu data modificării.
- **Butoane pe transfer:** pe un transfer cu notificarea în starea *Validated* apar în antet butoanele **Delete UIT**, **Confirm UIT** și **Change Vehicle**. Toate deschid același dialog cu acțiunea preselectată; se completează câmpurile specifice, opțional observația și indicatorul de declarație post-avarie, apoi **Send to ANAF**.
- **Evenimente ca înregistrări proprii:** tabelul *UIT Events* din tabul eTransport păstrează XML-ul trimis, indexul de încărcare ANAF și starea: *Sent* → *Validated* / *Error*. Cât timp un eveniment este în așteptare, nu se poate trimite altul pentru același UIT.
- **Verificarea stării:** ANAF răspunde la încărcare doar cu indexul de încărcare; acceptarea sau respingerea vin ulterior. Starea se interoghează automat la 15 minute sau la cerere, prin butonul **Fetch Event Status**.
- **Efecte aplicate doar după validare:** noul număr de vehicul și marcajul „UIT deleted" se aplică pe transfer numai după ce ANAF validează evenimentul, nu imediat după trimitere.
- **Declarație post-avarie:** indicator opțional (`declPostAvarie`, OUG 41/2022 art. 8 alin. 1^3) pe orice eveniment.
- **Configurare:** nu cere nimic în plus față de setarea standard eTransport (token de acces ANAF și mediul test/producție pe companie). Frecvența acțiunii programate se ajustează din Setări → Tehnic → Acțiuni programate.

#### 3. Dependențe

- [l10n_ro_etransport_enhancement](../l10n_ro_etransport_enhancement/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.etransport.event`: evenimentul trimis către ANAF (tip, UIT, XML, index de încărcare, stare); are punctul de extensie `_get_parent()`.
- `l10n.ro.etransport.action.wizard` (tranzitoriu): dialogul de trimitere a acțiunii DEL / CON / MVH.
- `stock.picking` (extins): butoanele de acțiune, tabelul de evenimente și marcajul „UIT deleted".
- `ETransportActionsAPI`: clasă Python (nu model Odoo) care extinde clientul API eTransport cu apelurile pentru aceste evenimente.

**Vizualizări**

- `view_etransport_event_list`: lista evenimentelor UIT.
- `view_etransport_action_wizard_form`: formularul dialogului de trimitere.
- `view_picking_form`: extinde formularul transferului cu butoane, banner și tabelul de evenimente.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_etransport_event_fetch_status` („RO e-Transport: UIT event status update"): interoghează la 15 minute starea evenimentelor trimise și aplică efectele după validare.

#### 5. Conexiuni

- [l10n_ro_etransport_block](../l10n_ro_etransport_block/index.md): modul eTransport înrudit din aceeași suită.
- `stock`: evenimentele se atașează transferurilor (`stock.picking`).
- Punctul de extensie `_get_parent()` permite unui modul separat (pentru loturi de transferuri) să atașeze evenimente unui lot, fără a duplica logica.
