# Van Sales (localizat la `deltatech_van_sales/index.md`)

- **Nume Tehnic:** `deltatech_van_sales`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_van_sales
- **Cale Locală:** `odoo-addons/bitshop/deltatech_van_sales`
- **Ultima Ingestie:** `2026-09-13`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul transformă orice depozit Odoo într-o flotă de dube pentru vânzare mobilă: un agent
încarcă marfă dimineața, confirmă și livrează comenzi pe teren dintr-un singur click, încasează
cash sau card pe loc, iar seara returnează stocul nevândut. Este un MVP simplu, gândit pentru
distribuitori mici și medii — nu concurează cu un SFA complet (nu are planificare de rute/vizite,
GPS sau execuție de retail cu poze) —, dar acoperă solid nucleul operațional: livrare instantă din
stocul dubei, încasare pe loc și facturare centralizată, în batch, la birou, cu reconciliere
contabilă automată.

#### 2. Funcționalități Cheie

- Fiecare dubă e propriul mini-depozit Odoo (`stock.warehouse` de tip ship-only), creat automat la
  salvare — folosește integral motorul nativ de stoc, rute și facturare, fără cod de stoc custom.
- Configurare dubă în **Van Sales > Configuration > Vans**: nume, cod (reutilizat ca și cod de
  warehouse), agent responsabil și depozitul de restocare.
- **Load Stock** pe formularul dubei deschide un transfer intern precompletat (de la depozitul de
  restocare la locația dubei) pentru încărcarea de dimineață.
- Câmpul **Van** pe comanda de vânzare setează automat warehouse-ul dubei și politica de livrare
  „cât mai curând posibil", și dezvăluie butonul **Confirm & Deliver**.
- **Confirm & Deliver** confirmă comanda și validează livrarea din stocul dubei într-un singur
  click, fără a genera vreo factură.
- **Register Collection** deschide un dialog precompletat cu suma comenzii, dubă și agent; alegerea
  Cash/Card creează și postează o plată standard (`account.payment`), neconciliată.
- **Return Unsold Stock** pe formularul dubei creează transferul invers către depozitul de
  restocare, precompletat cu stocul rămas pe hand în locația dubei, seara.
- Meniul **Van Sales > To Invoice** (doar grupul Manager) listează comenzile de tip van livrate și
  nefacturate încă (`invoice_status = 'to invoice'`), pentru facturarea în batch la birou;
  reconcilierea facturii cu încasarea deja înregistrată se face prin fluxul contabil standard Odoo.
- Meniul **Van Sales > Reports** deschide un wizard pentru două rapoarte PDF pe interval de date,
  filtrabile pe dubă sau agent: **Van Sales** (comenzi pe dubă, cu totaluri) și **Collections**
  (încasări pe agent, grupate pe metodă de plată).
- Două grupuri de securitate dedicate: **Van Sales / Agent** (vede doar dubă și comenzile/
  încasările proprii, `agent_id = user.id`) și **Van Sales / Manager** (vede tot, singurul cu acces
  la meniurile Configurare > Vans și To Invoice).
- Încasarea caută automat, per companie, primul jurnal **Cash** (pentru Cash) sau **Bank** (pentru
  Card) — trebuie să existe câte un jurnal de fiecare tip folosit, altfel apare eroare explicită.

#### 3. Dependențe

- `sale_stock`
- `stock`
- `account`
- `barcodes`
- [deltatech_barcode_sale](../deltatech_barcode_sale/index.md)

#### 4. Componente Cheie

*Nesintetizat din cod — Sumarul și Funcționalitățile Cheie provin din `readme/DESCRIPTION.md` /
`readme/USAGE.md`, conform priorității din `schema.md`. Fluxul detaliat pas-cu-pas și inventarul
complet de modele/vederi rămân în fișa consultant.*

#### 5. Conexiuni

- `sale_stock`: livrarea și legătura comandă-transfer sunt 100% native, fără suprascriere.
- `account`: încasarea creează un `account.payment` standard; reconcilierea cu factura folosește
  fluxul contabil obișnuit.
- `barcodes`: scanarea de coduri de bare pe formularul de comandă e moștenită de la dependință.
- [deltatech_barcode_sale](../deltatech_barcode_sale/index.md): widget-ul de scanare pe formularul
  de comandă (`barcode_handler`) e reutilizat, nu reimplementat.
- `deltatech_invoice_picking_automatically`: dacă e instalat și activat pe tipul de operațiune al
  dubei, ar factura automat la livrare — ceea ce contrazice decizia de scop a acestui MVP
  (facturare batch, nu instant); nu se combină pe același tip de livrare.
