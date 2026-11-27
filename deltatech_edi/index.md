# EDI Base Connector (localizat la `deltatech_edi/index.md`)

- **Nume Tehnic:** `deltatech_edi`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_edi
- **Cale Locală:** `odoo-addons/bitshop/deltatech_edi`
- **Ultima Ingestie:** `2026-11-27`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul reprezintă conectorul EDI (Electronic Data Interchange) de bază pentru Odoo, facilitând comunicarea electronică standardizată cu partenerii și sistemele externe. Din perspectivă de business, conectorul EDI este un instrument esențial pentru digitalizarea lanțului de aprovizionare, reducerea documentelor pe hârtie și îmbunătățirea vitezei și acurateței tranzacțiilor. El permite schimbul automatizat de documente comerciale (facturi, comenzi, avize de expediție) între platforme, eliminând introducerea manuală a datelor și reducând costurile operaționale.

#### 2. Funcționalități Cheie

- GLN standard: identificarea partenerilor se face prin câmpul standard `global_location_number` (din `account_add_gln`), nu prin `gln` din [deltatech_gln](../deltatech_gln/index.md); câmpul apare în formular și pe companii, nu doar pe adresele de livrare. La upgrade, vechiul `gln` se copiază unde câmpul standard e gol (la conflict se păstrează valoarea standard, iar partenerul se loghează).
- Configurare pe grupe de taxe: **EDI Code** și **EDI Percent** (*Facturare > Configurare > Grupuri de taxe*) devin `TaxCategoryCoded` și `TaxPercent` în XML-ul facturii.
- Configurare partener: **Edi System** (valorile vin de la conectorul instalat), **GLN** pe companie și pe fiecare adresă de livrare (magazin), **EDI Bayer** și **EDI Seller** (obligatoriu pentru DESADV).
- Import comenzi: clientul și adresa de livrare se găsesc după GLN, produsele după cod de bare, apoi referință internă, apoi codul clientului; numărul comenzii clientului intră în **Customer Reference**; un mesaj primit de două ori nu creează o a doua comandă. Liniile importate nu primesc discount, iar descrierea lor poartă codul clientului (`[BuyerItemID] nume`).
- Găsirea partenerului: căutarea după GLN se face doar când partidul are GLN (un GLN gol nu mai potrivește orice partener fără GLN); fără GLN se caută după CUI, apoi după nume exact, altfel se creează un partener nou; un partid cu GLN e o locație și nu se potrivește niciodată după nume sau CUI.
- Prețuri la import: când mesajul nu are prețuri, se folosește referința clientului, apoi lista de prețuri; când prețul net diferă de o regulă din lista de prețuri, se postează o notă internă în chatter, fără a modifica lista.
- Coduri de articol ale clientului: codul cumpărătorului (`BuyerItemID`) se ține în `product.customerinfo` (din [deltatech_sale_product_reference](../deltatech_sale_product_reference/index.md)), nu în `product.supplierinfo`; cumpărătorul EDI nu mai apare ca furnizor. Referința introdusă manual are prioritate față de cea scrisă de import.
- Cod export determinist: `BuyerItemID` se rezolvă după precedență (variantă peste șablon, partener exact peste entitatea comercială, apoi secvență), fără revenire tăcută la `default_code` propriu.
- Buton **Export EDI** comun tuturor conectorilor: apare doar pe facturile/notele de credit clienți postate și pe livrările validate către clienți; verifică documentul, partenerul și sistemul EDI, apoi apelează conectorul; dacă sistemul EDI nu poate exporta documentul, oprește cu mesaj clar.
- Aviz de expediție (DESADV) și factură: XML generat și validat pe schema XSD (DESADV, respectiv INVOICE); eroarea de validare apare în chatter. La nota de credit se alege **Invoice EDI Type**: *Return* (numărul avizului de retur în **Reference**), *Storno* / *Correction* (`număr factură|dată` în **Reference**). Codurile din XML (`RETURN`, `O`, `R`, `C`, `PCE`) nu se traduc.
- Fără **Edi System** pe partener, exportul se oprește cu mesajul „Please select an EDI system for partner …”.

#### 3. Dependențe

- `stock`
- `sale_stock`
- `account_add_gln`
- `account`
- [deltatech_sale_product_reference](../deltatech_sale_product_reference/index.md)

#### 4. Componente Cheie

**Modele**

- `account.move`: câmpurile **Invoice EDI Type** și **EDI Order Number**; verificările comune și butonul de export (`action_export_edi`, `button_export_edi`, `_create_edi_xml`).
- `account.tax.group`: câmpurile `edi_code` și `edi_percent` pentru maparea grupelor de taxe în mesajele EDI.
- `res.partner`: câmpurile `edi_system`, `edi_id_bayer`, `edi_id_seller`.
- `sale.order`: importul comenzilor EDI (`_import_edi`), găsirea partenerului și a produsului, nota cu diferențele față de lista de prețuri.
- `stock.picking`: exportul avizului de expediție (DESADV).
- `product.product` / `uom.uom`: `get_buyer_code` (citirea codului cumpărătorului din `product.customerinfo`) și codul EDI al unității de măsură.

**Vizualizări**

- `account_move_view.xml`: ajustări pe formularul de factură pentru câmpurile și butonul EDI.
- `invoice_template.xml`: șablonul XML al facturii EDI.
- `desadv_template.xml`: șablonul XML al avizului de expediție (DESADV).
- `stock_picking_view.xml`, `res_partner_view.xml`, `account_tax_views.xml`: câmpurile EDI pe transfer, partener și grupe de taxe.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server în acest modul.

#### 5. Conexiuni

- [deltatech_gln](../deltatech_gln/index.md): câmpul `gln` vechi; modulul nu mai e dependență, iar valorile se migrează în câmpul standard `global_location_number`.
- [deltatech_sale_product_reference](../deltatech_sale_product_reference/index.md): furnizează `product.customerinfo` și `_get_reference()` pentru codurile de articol ale clientului.
- [deltatech_ediconnect](../deltatech_ediconnect/index.md): conector care extinde baza cu logica de conectare/transport a mesajelor.
- [deltatech_edinet](../deltatech_edinet/index.md): conector care implementează integrarea cu serviciul Edinet.
