# Purchase Add Extra Line (localizat la `deltatech_purchase_add_extra_line/index.md`)

- **Nume Tehnic:** `deltatech_purchase_add_extra_line`
- **Versiune:** `20.0.1.6.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_purchase_add_extra_line`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_add_extra_line`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă automat pe comenzile de achiziție linii suplimentare (taxe de serviciu, manipulare, ambalaje), în funcție de produsul comandat. Echipa de achiziții nu mai introduce manual aceste costuri, iar riscul de omisiuni sau greșeli scade.

#### 2. Funcționalități Cheie

- Produs suplimentar configurabil pe fișa produsului (`extra_product_id`): de fiecare dată când produsul principal intră pe o comandă de achiziție, se adaugă o linie separată cu produsul suplimentar.
- Preț flexibil: dacă procentul este setat, prețul unitar al liniei suplimentare este un procent din prețul liniei principale; dacă procentul este zero, se aplică calculul standard (prețul furnizorului pentru produsul suplimentar, în moneda și unitatea de măsură ale comenzii).
- Cantitatea liniei suplimentare urmărește linia principală.
- Un preț unitar introdus manual pe linia suplimentară este păstrat și nu mai este recalculat; pentru revenirea la prețul calculat se șterge linia suplimentară, iar ea se regenerează automat.
- Configurare: *Purchase > Products > Products*, secțiunea de configurare a liniei suplimentare de pe produs. Fluxul pas-cu-pas, cu capturi, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `purchase`

#### 4. Componente Cheie

**Modele**

- `product.template` (extins): câmpurile `extra_product_id`, `extra_percent`, `extra_qty`.
- `purchase.order` (extins): reacționează la confirmare, trimiterea cererii de ofertă și modificarea liniilor ca să mențină liniile suplimentare.
- `purchase.order.line` (extins): câmpurile `is_extra_line`, `line_uuid`, `extra_price_computed`; creează, sincronizează și șterge linia suplimentară.

**Vizualizări**

- `product_template_form_view`: configurarea produsului suplimentar și a procentului pe fișa produsului.
- `purchase_order_form`: extensie a formularului comenzii de achiziție pentru liniile suplimentare.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate, sarcini `ir.cron` sau acțiuni server.

#### 5. Conexiuni

- [deltatech_sale_add_extra_line](../deltatech_sale_add_extra_line/index.md): modul soră care aplică același mecanism pe comenzile de vânzare; câmpurile de configurare de pe `product.template` sunt partajate.
