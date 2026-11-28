# Barcode Sale (localizat la `deltatech_barcode_sale/index.md`)

- **Nume Tehnic:** `deltatech_barcode_sale`
- **Versiune:** `20.0.2.1.7`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_barcode_sale`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_barcode_sale`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul optimizează procesul de vânzare prin scanarea codurilor de bare direct în comanda de vânzare, astfel încât reprezentanții să poată construi rapid și corect cotații și comenzi. Din punct de vedere comercial, accelerează ciclul tranzacției, reduce erorile de introducere și oferă clienților o experiență mai profesionistă, mai ales în medii de tip retail.

#### 2. Funcționalități Cheie

- Introducere accelerată a comenzilor: produsele se adaugă prin scanarea codului de bare, ceea ce scurtează timpul de așteptare al clientului.
- Mai puține erori: se elimină greșelile de tastare, iar produsul și varianta corectă ajung pe comandă.
- Identificare în timp real a produsului prin cod de bare, utilă pentru evidențe de stoc corecte în timpul vânzării.
- Personalul de vânzări se poate concentra pe client și pe vânzarea încrucișată, nu pe introducerea manuală.
- Comportamente observate în cod: prima scanare adaugă linia, următoarele cresc cantitatea; un cod de ambalaj adaugă ambalajul produsului; un produs nevandabil sau un cod necunoscut afișează un mesaj și nu modifică comanda.
- Fluxul pas-cu-pas, cu capturi, este în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `sale`
- [deltatech_barcode_handler](../deltatech_barcode_handler/index.md)

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): implementează `on_barcode_scanned()` și `_add_product()` pentru a adăuga sau a crește cantitatea liniilor de comandă din codul scanat.

**Vizualizări**

- `view_sale_order_barcode_inherit_form`: adaugă câmpul de captare a scanărilor pe formularul comenzii de vânzare.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- [deltatech_barcode_picking](../deltatech_barcode_picking/index.md): același principiu de scanare, aplicat pe transferurile de stoc.
