# Deltatech EDI Base Connector (localizat la `deltatech_edi/index.md`)

- **Nume Tehnic:** `deltatech_edi`
- **Versiune:** `19.0.0.1.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_edi
- **Cale Locală:** `odoo-addons/bitshop/deltatech_edi`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul reprezintă conectorul EDI (Electronic Data Interchange) de bază pentru Odoo, facilitând comunicarea electronică standardizată cu partenerii și sistemele externe. Din perspectivă de business, conectorul EDI este un instrument esențial pentru digitalizarea lanțului de aprovizionare, reducerea documentelor pe hârtie și îmbunătățirea vitezei și acurateței tranzacțiilor. El permite schimbul automatizat de documente comerciale (facturi, comenzi de achiziție, avize de expediție) între platforme, eliminând introducerea manuală a datelor și reducând costurile operaționale.

#### 2. Funcționalități Cheie

- Comunicare standardizată: implementarea de protocoale EDI standard din industrie pentru schimbul de documente comerciale (de ex. facturi, comenzi de achiziție) cu partenerii.
- Procesare mai rapidă a tranzacțiilor: automatizarea schimbului de documente între sisteme pentru o comunicare aproape instantanee.
- Acuratețe îmbunătățită a datelor: eliminarea erorilor de introducere manuală prin transmiterea electronică a informațiilor între platforme.
- Costuri operaționale reduse: minimizarea efortului administrativ prin automatizarea schimburilor de documente de rutină și a sarcinilor de reconciliere.
- Interoperabilitate scalabilă: adăugarea cu ușurință de noi parteneri și protocoale EDI pe măsură ce afacerea și rețeaua de parteneri cresc.

#### 3. Dependențe

- `stock`
- `sale_stock`
- [deltatech_gln](../deltatech_gln/index.md)
- `account`

#### 4. Componente Cheie

**Modele**

- `account.move`: extinde factura cu hook-uri pentru schimbul EDI și pentru personalizarea documentului de factură.
- `account.tax.group`: extindere pentru maparea grupelor de taxe în mesajele EDI.
- `res.partner`: extindere a partenerului cu informații necesare schimbului EDI.
- `sale.order`: extindere a comenzii de vânzare pentru fluxul EDI.
- `stock.picking`: extindere a transferului de stoc pentru generarea avizului de expediție (DESADV).
- `product.product` / `uom.uom`: extinderi pentru maparea produselor și a unităților de măsură în EDI.

**Vizualizări**

- `account_move_view.xml`: ajustări pe formularul de factură pentru câmpurile EDI.
- `invoice_template.xml`: personalizări QWeb ale șablonului de factură pentru EDI.
- `desadv_template.xml`: șablon pentru documentul de aviz de expediție (DESADV).
- `stock_picking_view.xml`, `res_partner_view.xml`, `account_tax_views.xml`: vizualizări auxiliare pentru câmpurile EDI pe transfer, partener și grupe de taxe.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server în acest modul.

#### 5. Conexiuni

- [deltatech_gln](../deltatech_gln/index.md): furnizează codurile GLN (Global Location Number) necesare identificării partenerilor în schimbul EDI.
- `deltatech_ediconnect`: modul soră care extinde conectorul EDI de bază cu logica de conectare/transport a mesajelor.
- `deltatech_edinet`: modul soră care implementează integrarea cu rețeaua/serviciul EDI.
