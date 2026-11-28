# Sale from Store (localizat la `deltatech_sale_store/index.md`)

- **Nume Tehnic:** `deltatech_sale_store`
- **Versiune:** `20.0.2.5.17`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_sale_store
- **Cale Locală:** `odoo-addons/bitshop/deltatech_sale_store`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite vânzarea la tejghea din modulul Vânzări, cu bon fiscal pe casa de marcat românească, fără a folosi Point of Sale. Dintr-o ofertă, un singur gest confirmă comanda, livrează marfa, emite factura (sau bonul, pentru clienții ocazionali), înregistrează plata și trimite bonul la casa de marcat.

#### 2. Funcționalități Cheie

- **Vânzare din magazin într-un singur pas**: butonul **Vânzare din magazin** (Sale from store) de pe ofertă confirmă comanda, verifică stocul, validează livrarea, postează factura, înregistrează plata și tipărește bonul fiscal. Dacă un produs lipsește din stoc, vânzarea se oprește și nu se creează nimic.
- **Clienți ocazionali**: vânzările către partenerul generic al companiei se documentează cu bon (chitanță de vânzare), fără factură; ulterior, bonul poate fi transformat în factură cu **Bon în factură** (Receipt To Invoice), cu mențiunea bonului fiscal, iar plata se mută pe factură.
- **Bon fiscal din factură**: **Tipărire bon fiscal** (Print Fiscal Receipt) pe o factură plătită integral o trimite la casa de marcat; un bon nu poate fi tipărit de două ori.
- **Jurnale pentru bon fiscal**: jurnal de vânzări dedicat (recomandat codul `BF`) și jurnale de numerar marcate „Bon fiscal”, cu codul ECR de plată (0 numerar, 1 tichet de masă, 2 card); utilizatorii pot fi limitați la propriile jurnale. Când există mai multe jurnale marcate, un **Tip de comandă** (Vânzări → Configurare → Tipuri de comandă) alege jurnalul și bifează *Vânzare din magazin* / *Vânzare fără factură*.
- **Case de marcat și drivere**: Datecs, Optima, Incotex, Daisy și Succes, prin fișier de comenzi sau prin agentul local Terrabit Connect; testat extensiv cu driverele certificate FiscalWire și FiscalNet. Transportul se alege din parametrii de sistem `account_invoice.ecr_transport` (`file`, `connect`, `fisco`, `dxprint`), cu parametri dedicați pentru URL-urile agenților și formatul comenzilor (`ecr_type`).
- **Pregătit pentru SAGA**: documentele din vânzările de magazin și bonurile sunt marcate astfel încât exportul SAGA (`deltatech_saga`) să seteze tipul corect de document (`f`, `B`, `C` în coloana `TIP`).
- Fluxul pas-cu-pas, conturile implicate și capturile de ecran sunt în fișa consultantului.

#### 3. Dependențe

- `account`
- `web`
- `sale`
- `stock`
- `sales_team`
- [deltatech_ecr_fiscal](../deltatech_ecr_fiscal/index.md)
- [deltatech_partner_generic](../deltatech_partner_generic/index.md)
- [deltatech_record_type](../deltatech_record_type/index.md)
- [deltatech_ecr_connect](../deltatech_ecr_connect/index.md)

#### 4. Componente Cheie

Documentația de Sumar și Funcționalități Cheie este preluată din `readme/DESCRIPTION.md`, completată cu `readme/USAGE.md` și `readme/CONFIGURE.md`. Pe baza structurii modulului:

**Modele**

- `sale.order` (extins): butonul și logica de vânzare din magazin, indicatorul *Vânzare fără factură*.
- `account.move` (extins): bonul fiscal pe factură (**Tipărire bon fiscal**) și marcajul de vânzare din magazin.
- `account.journal` (extins): marcajul „Bon fiscal”, codul ECR și permisiunile de vânzare din magazin.
- `res.company`, `res.config.settings`, `res.users`, `crm.team` (extinse): partener generic, restricția jurnalelor, jurnale permise per utilizator, setări de echipă.
- `stock.picking` (extins): legătura cu livrarea validată în fluxul de vânzare.

**Vizualizări**

- Wizard-ul **Confirmă vânzarea** (`wizard/sale_store_view.xml`): sumă, jurnal de plată, buton *Tipărire*.
- Wizard-ul **Bon în factură** (`wizard/account_receipt_to_invoice_view.xml`).
- Extinderi de vizualizări pentru comandă, factură, jurnal, utilizator, plată, transfer și echipă de vânzări; indicator în bara de sus pentru starea agentului casei de marcat (`fiscal_status.esm.js`).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni programate sau automate.

#### 5. Conexiuni

- [deltatech_ecr_connect](../deltatech_ecr_connect/index.md): conectarea la casa de marcat (ECR) folosită pentru tipărirea bonurilor.
- [deltatech_ecr_fiscal](../deltatech_ecr_fiscal/index.md): formatarea comenzilor pentru casa de marcat.
- [deltatech_saga](../deltatech_saga/index.md): fluxul de documente (factură/bon fiscal/storno) alimentează coloana `TIP` din exportul SAGA.
- [deltatech_payment_report](../deltatech_payment_report/index.md): definește conturile contabile reutilizate de fluxul de plăți/încasări asociat bonurilor.
