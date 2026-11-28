# e-Transport for Transfer Batches (localizat la `l10n_ro_etransport_batch_enhancement/index.md`)

- **Nume Tehnic:** `l10n_ro_etransport_batch_enhancement`
- **Versiune:** `20.0.0.4.3`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_etransport_batch_enhancement
- **Cale Locală:** odoo-addons/l10n-romania/l10n_ro_etransport_batch_enhancement
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Extinde declarația e-Transport pentru loturile de transferuri (`stock.picking.batch`), astfel încât un camion care duce mai multe livrări să poată fi declarat la ANAF dintr-un singur loc: transportatorul, greutățile și documentele se gestionează central, pe lot, și se propagă către transferurile componente.

#### 2. Funcționalități Cheie

- Câmp pentru partenerul de transport pe lot (`l10n_ro_transport_partner_id`), sincronizat automat către toate transferurile din lot.
- Curier (`delivery.carrier`) ales la nivel de lot, propagat către transferurile individuale.
- Greutăți la nivel de lot: calculul pe liniile de transfer și distribuirea greutății totale (netă și brută) proporțional pe liniile lotului.
- Avertisment când unor mișcări din lot le lipsește linia de greutate, ca declarația să nu plece la ANAF cu greutăți incomplete.
- Validarea datelor e-Transport pentru loturi, cu partenerul de transport injectat corect în datele trimise la ANAF.
- Documente însoțitoare (CMR, avize) pe lot și corecția declarației lotului după validarea UIT.
- Numărul UIT afișat pe raportul de livrare al lotului.
- Fluxul pas cu pas este în fișa consultant.

#### 3. Dependențe

- `l10n_ro_edi`
- `l10n_ro_edi_stock`
- [l10n_ro_etransport_enhancement](../l10n_ro_etransport_enhancement/index.md)
- `l10n_ro_stock_picking_batch_report`

#### 4. Componente Cheie

Descrierea modulului nu detaliază componentele; mai jos, cele extinse.

**Modele**

- `stock.picking.batch`: câmpuri e-Transport pe lot (necesar, transportator, greutăți, documente, declarație post-avarie).
- `l10n.ro.stock.picking.weight.line`: linia de greutate legată de lot (`batch_id`).
- `l10n.ro.etransport.document`: documente e-Transport extinse pentru lot.
- `stock.picking`: sincronizarea transportatorului cu lotul.

**Vizualizări**

- `views/stock_picking_batch_view.xml`: tab-ul eTransport și câmpurile de transport pe formularul lotului.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_ro_etransport_enhancement](../l10n_ro_etransport_enhancement/index.md): declarația e-Transport pe transferuri, pe care acest modul o extinde la loturi.
- [l10n_ro_etransport_uit_actions_batch](../l10n_ro_etransport_uit_actions_batch/index.md): ștergere, confirmare și schimbare vehicul pe UIT-ul unui lot.
