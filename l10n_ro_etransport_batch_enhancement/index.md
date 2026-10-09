# eTransport Batch Enhancement (localizat la `l10n_ro_etransport_batch_enhancement/index.md`)

- **Nume Tehnic:** `l10n_ro_etransport_batch_enhancement`
- **Versiune:** `19.0.0.3.3`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_etransport_batch_enhancement
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_etransport_batch_enhancement`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul extinde declararea e-Transport la nivel de lot de transferuri (`stock.picking.batch`). Transportatorul, curierul și greutățile se gestionează o singură dată, pe lot, iar datele se propagă automat către transferurile componente. Astfel, declarația către ANAF se poate transmite pentru întregul lot, cu avertisment atunci când greutățile sunt incomplete.

#### 2. Funcționalități Cheie

- Câmp pentru partenerul de transport (`l10n_ro_transport_partner_id`) pe lot, sincronizat automat către toate transferurile componente.
- Curier (`delivery.carrier`) specificat la nivel de lot și propagat către transferurile individuale.
- Gestionarea greutăților la nivel de lot:
  - calculul liniilor de greutate pe baza transferurilor din lot;
  - distribuirea greutății totale (netă și brută) proporțional pe liniile lotului;
  - avertisment când unor mișcări din lot le lipsește linia de greutate, ca declarația să nu plece incompletă către ANAF fără să se vadă.
- Documentele e-Transport pot fi atașate direct lotului; lotul afișează și documentele transferurilor sale.
- Validarea datelor e-Transport pentru loturi, cu injectarea partenerului de transport setat manual pe lot în datele trimise către ANAF, plus preluarea stării declarației din buton pe lot.
- Documentele însoțitoare declarate fără observație nu mai generează `observatii=""` în XML (respins de ANAF); atributul se omite când lipsește.
- Afișarea numărului UIT pe raportul de livrare al lotului.

#### 3. Dependențe

- `l10n_ro_edi`
- `l10n_ro_edi_stock`
- `l10n_ro_edi_stock_batch`
- [l10n_ro_etransport_enhancement](../l10n_ro_etransport_enhancement/index.md)
- `l10n_ro_stock_picking_batch_report`

#### 4. Componente Cheie

**Modele**

- `stock.picking.batch` (extins): câmpuri e-Transport pe lot (necesitate, curier, partener de transport, referință de urmărire, greutăți personalizate, greutate netă/brută totală, avertisment linii de greutate lipsă, documente e-Transport); metode `l10n_ro_compute_weight_lines`, `l10n_ro_distribute_weights`, `_l10n_ro_edi_stock_validate_data`, `action_l10n_ro_edi_stock_fetch_status`.
- `l10n.ro.etransport.document` (extins): adaugă `batch_id` (lot de transfer) și face `picking_id` opțional; o constrângere verifică existența părintelui.
- `l10n.ro.stock.picking.weight.line` (extins): legătură `batch_id` către lot.

**Vizualizări**

- `l10n_ro_edi_stock_view_batch_form`: extinde formularul lotului cu câmpurile e-Transport, butoanele aferente și liniile de greutate.
- Moștenire a raportului de livrare al lotului (xpath după `report_delivery_sign`): afișează numărul UIT.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- [l10n_ro_etransport_enhancement](../l10n_ro_etransport_enhancement/index.md): logica e-Transport pe transferurile individuale, replicată aici la nivel de lot.
