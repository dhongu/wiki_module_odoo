# Purchase Create Bill Button (localizat la `deltatech_purchase_create_bill_button/index.md`)

- **Nume Tehnic:** `deltatech_purchase_create_bill_button`
- **Versiune:** `20.0.1.1.2`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_purchase_create_bill_button`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_create_bill_button`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul readuce butonul clasic „Create Bill" pe comanda de achiziție și în liste. În Odoo standard, crearea facturii din formular trece prin widget-ul „Upload Bill", care cere un fișier; cu acest modul comenzile se pot factura direct, dintr-un singur clic, fără atașarea unui document.

#### 2. Funcționalități Cheie

- Buton „Create Bill" pe formularul comenzii de achiziție, lângă widget-ul de încărcare a facturii.
- Butonul „Create Bills" și pe lista cererilor de ofertă (lista implicită a tabloului de bord), pentru a selecta mai multe comenzi și a le factura odată; retururile devin automat notă de credit furnizor când totalul este negativ.
- Copierea automată a „Vendor Reference" din comandă în câmpurile „Reference" și „Payment Reference" ale facturii furnizor create din comandă.
- Fluxul pas-cu-pas, cu capturi, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `purchase`

#### 4. Componente Cheie

**Modele**

- `purchase.order` (extins): `_prepare_invoice` copiază referința furnizorului în factură.

**Vizualizări**

- `purchase_order_form`: adaugă butonul „Create Bill" înaintea widget-ului `purchase_file_uploader`.
- `purchase_order_kpis_tree`: adaugă butonul „Create Bills" în antetul listei.
- `static/src/views/purchase_listview.xml`: extensie de șablon al listei (asset `web.assets_backend`) care readuce butonul în lista de cereri de ofertă.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate, sarcini `ir.cron` sau acțiuni server.

#### 5. Conexiuni

- [deltatech_fast_purchase](../deltatech_fast_purchase/index.md): extinde fluxul de achiziții din aceeași suită deltatech.
- [deltatech_purchase_price](../deltatech_purchase_price/index.md): completează modulul de achiziții cu logică de prețuri.
- [deltatech_purchase_add_extra_line](../deltatech_purchase_add_extra_line/index.md): extensie pe comenzile de achiziție.
