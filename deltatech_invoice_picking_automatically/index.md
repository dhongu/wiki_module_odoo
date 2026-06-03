# Invoice Pickings Automatically (localizat la `deltatech_invoice_picking_automatically/index.md`)

- **Nume Tehnic:** `deltatech_invoice_picking_automatically`
- **Versiune:** `19.0.0.0.4`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_invoice_picking_automatically`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_invoice_picking_automatically`
- **Ultima Ingestie:** `2026-06-02`

#### 1. Sumar

Acest modul automatizează generarea facturilor pornind de la livrările de marfă (pickings) după validarea acestora. Pe fiecare tip de operațiune de stoc se poate configura dacă, la finalizarea livrării, sistemul trebuie să creeze automat factura și, opțional, să o și valideze. Un proces planificat preia periodic livrările marcate pentru facturare și emite facturile fără intervenție manuală, reducând timpul administrativ și eliminând riscul de a uita facturarea unei livrări. Valoarea principală pentru afacere este fluidizarea ciclului vânzare → livrare → factură, mai ales pentru companiile cu volum mare de expedieri.

#### 2. Funcționalități Cheie

- Configurare pe tipul de operațiune de stoc (picking type) pentru crearea automată a facturii.
- Configurare pe tipul de operațiune de stoc pentru validarea (postarea) automată a facturii.
- Proces planificat (cron) care generează automat facturile pentru livrările marcate pentru facturare.
- Gestionează eficient mai multe livrări aparținând aceleiași comenzi de vânzare, procesându-le împreună.
- Tratarea erorilor: dacă facturarea eșuează, livrarea este marcată ca „Failed" pentru a evita încercările repetate eșuate.

#### 3. Dependențe

- `stock_account`
- `sale_stock`
- `sale`
- `stock`
- `account`

#### 4. Componente Cheie

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_generate_invoices` (Generate Invoices from Pickings): proces planificat care rulează zilnic și apelează `model._cron_generate_invoices()` pentru a genera automat facturile aferente livrărilor marcate pentru facturare.

#### 5. Conexiuni

- [deltatech_invoice_picking](../deltatech_invoice_picking/index.md): modul înrudit din aceeași suită care tratează facturarea pornind de la livrări; acest modul adaugă componenta de automatizare (configurare pe tip de operațiune și cron) peste fluxul de facturare din livrări.
