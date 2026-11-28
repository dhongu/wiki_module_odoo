# e-Transport UIT Actions for Batches (localizat la `l10n_ro_etransport_uit_actions_batch/index.md`)

- **Nume Tehnic:** `l10n_ro_etransport_uit_actions_batch`
- **Versiune:** `20.0.1.1.0`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_etransport_uit_actions_batch
- **Cale Locală:** odoo-addons/l10n-romania/l10n_ro_etransport_uit_actions_batch
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Aduce acțiunile pe UIT (ștergere, confirmare, schimbare vehicul) și pe loturile de transferuri declarate cu `l10n_ro_edi_stock`, unde un camion (un lot) poartă un singur UIT pentru mai multe transferuri. Se instalează automat când ambele module părinte sunt prezente.

#### 2. Funcționalități Cheie

- Butoanele **Șterge UIT**, **Confirmă UIT** și **Schimbă vehiculul** pe un lot cu notificare **Validată**, cu același dialog ca pe transfer.
- Evenimentele se păstrează pe lot (tabelul **UIT Events** din tab-ul eTransport), se înregistrează în chatter și li se verifică starea la ANAF ca la un transfer singular.
- O schimbare de vehicul validată actualizează numerele pe lot; o ștergere validată marchează UIT-ul lotului ca șters.
- **Anulează** pe un lot cu UIT valabil deschide dialogul de ștergere și anulează lotul imediat ce ANAF primește ștergerea.
- Fluxul detaliat este în fișa consultant.

#### 3. Dependențe

- [l10n_ro_etransport_uit_actions](../l10n_ro_etransport_uit_actions/index.md)
- `l10n_ro_edi_stock`

#### 4. Componente Cheie

**Modele**

- `stock.picking.batch`: acțiuni UIT, evenimente și anulare cu ștergere.
- `l10n.ro.etransport.event`: evenimentul extins pentru a putea aparține unui lot.
- `l10n.ro.etransport.action.wizard`: dialogul extins pentru loturi.

**Vizualizări**

- `views/stock_picking_batch_view.xml`: butoanele și tabelul de evenimente pe lot.
- `views/etransport_event_view.xml`: evenimentul cu legătura către lot.

**Acțiuni Automate / Acțiuni Server**

- Nu are; folosește acțiunea programată din `l10n_ro_etransport_uit_actions`.

#### 5. Conexiuni

- [l10n_ro_etransport_batch_enhancement](../l10n_ro_etransport_batch_enhancement/index.md): declarația e-Transport pe lot, al cărei UIT este gestionat aici.
- [l10n_ro_etransport_enhancement](../l10n_ro_etransport_enhancement/index.md): declarația e-Transport de bază.
