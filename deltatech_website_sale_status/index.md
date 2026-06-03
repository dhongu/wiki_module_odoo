# eCommerce Sale Order status (localizat la `deltatech_website_sale_status/index.md`)

- **Nume Tehnic:** `deltatech_website_sale_status`
- **Versiune:** `19.0.2.0.3`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_sale_status`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_sale_status`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul extinde comenzile de vânzare din magazinul online cu o stare detaliată care urmărește parcursul unei comenzi de la plasarea pe website până la livrarea către client. Astfel, atât operatorii din spate, cât și clienții din portal pot vedea în mod clar în ce etapă se află fiecare comandă (de exemplu „Plasată", „În procesare", „De livrat" sau „Livrată"), iar comenzile pot fi filtrate suplimentar după aceste stări.

#### 2. Funcționalități Cheie

- Filtre suplimentare pentru comenzile de vânzare în funcție de stare.
- Etape dedicate ciclului de viață al unei comenzi eCommerce:
  - **Plasată** – comanda este plasată pe website de client
  - **În procesare** – comanda introdusă de operator
  - **Așteaptă disponibilitate** – nu sunt disponibile toate produsele
  - **Amânată** – livrarea a fost amânată
  - **De livrat** – produsele sunt disponibile și se poate face livrarea
  - **În livrare** – produsele au fost predate la curier
  - **Livrată** – produsele au ajuns la client
  - **Anulată** – comanda de vânzare a fost anulată
  - **Returnată** – comanda a fost returnată de către client

#### 3. Dependențe

- `portal`
- `website_sale_stock`
- [deltatech_delivery_status](../deltatech_delivery_status/index.md)
- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `sale.order`: model extins pentru a gestiona și filtra starea comenzii pe parcursul ciclului de viață eCommerce.
- `sale.report`: raport de vânzări extins pentru raportarea pe baza stărilor comenzilor.

**Vizualizări**

- `views/sale_view.xml`: extinderi ale vizualizărilor de comandă de vânzare cu filtrele și informațiile despre stare.
- `views/templates.xml`: șabloane QWeb pentru afișarea stării comenzii în portalul clientului / magazinul online.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni `ir.cron`, reguli `base.automation` sau acțiuni server în acest modul.

#### 5. Conexiuni

- [deltatech_delivery_status](../deltatech_delivery_status/index.md): furnizează stările de livrare pe care acest modul le folosește pentru ciclul de viață al comenzii eCommerce.
