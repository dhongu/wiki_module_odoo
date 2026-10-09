# eTransport UIT Actions - Batch

- **Nume Tehnic:** `l10n_ro_etransport_uit_actions_batch`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_etransport_uit_actions_batch
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_etransport_uit_actions_batch`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Extinde acțiunile asupra codului UIT din eTransport (ștergere, confirmare, schimbarea vehiculului) la loturile de transfer declarate prin `l10n_ro_edi_stock_batch`, unde un singur camion (un lot) transportă un singur UIT pentru mai multe transferuri. Utilizatorul poate astfel corecta un UIT direct din lot, fără pași manuali în afara Odoo. Modulul se instalează automat când ambele module părinte sunt prezente.

#### 2. Funcționalități Cheie

- Butoanele **Delete UIT**, **Confirm UIT** și **Change Vehicle** apar în antetul unui lot a cărui notificare eTransport este *Validated*, cu același dialog ca pe un transfer.
- Evenimentele trimise pentru lot se rețin pe lot, se înregistrează în chatter și li se interoghează starea la ANAF la fel ca cele ale unui transfer singular; sunt listate în tabelul *UIT Events* din fila eTransport a lotului.
- O schimbare de vehicul validată actualizează numerele de înmatriculare pe lot.
- O ștergere validată marchează UIT-ul lotului ca șters.
- Acțiunile sunt disponibile doar cât timp lotul are UIT, este validat în stoc, UIT-ul nu a fost șters și nu există un eveniment în așteptare (trimis, dar încă nevalidat).

#### 3. Dependențe

- `l10n_ro_etransport_uit_actions`
- `l10n_ro_edi_stock_batch`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.etransport.event` (extins): adaugă `batch_id`; `picking_id` nu mai e obligatoriu, iar o constrângere cere ca evenimentul să aparțină fie unui transfer, fie unui lot.
- `l10n.ro.etransport.action.wizard` (extins): adaugă `batch_id`; valorile evenimentului și implicitele de vehicul se preiau din lot.
- `stock.picking.batch` (extins): câmpul `l10n_ro_etransport_event_ids`, indicatorii calculați (UIT șters, eveniment în așteptare, acțiuni activate) și metodele de deschidere a wizardului și de verificare a stării evenimentelor.

**Vizualizări**

- `view_picking_batch_form`: butoanele de acțiune și tabelul *UIT Events* pe formularul lotului.
- `view_etransport_action_wizard_form`: extinde wizardul cu câmpul lot, afișat doar când acțiunea pornește dintr-un lot.

**Acțiuni Automate / Acțiuni Server**

- Nu definește cron-uri sau acțiuni server proprii.

#### 5. Conexiuni

- `l10n_ro_etransport_uit_actions`: modulul de bază al acțiunilor UIT pe un singur transfer; logica este reutilizată pentru loturi.
- `l10n_ro_edi_stock_batch`: declarația eTransport pe lot de transfer, care emite UIT-ul pe care acționează acest modul.
