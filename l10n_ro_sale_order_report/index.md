# Romania - Proforma Invoice Report (localizat la `l10n_ro_sale_order_report/index.md`)

- **Nume Tehnic:** `l10n_ro_sale_order_report`
- **Versiune:** `20.0.1.1.1`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_sale_order_report
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_sale_order_report`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaptează oferta/comanda de vânzare tipărită la uzul din România și permite tipărirea proformelor direct din ofertă. Sunt disponibile două proforme: cea inițială, calculată din liniile termenului de plată (prima linie de tip „procent” sau „fix”), și cea finală, cu suma rămasă de încasat. Este util firmelor care lucrează cu avansuri și plăți eșalonate.

#### 2. Funcționalități Cheie

- Proforma inițială (avansul), cu suma din prima linie de tip „procent” sau „fix” a termenului de plată.
- Proforma finală, cu restul de plată; necesită modulul Deltatech Sale Payment, care aduce suma încasată pe comandă.
- Oferta tipărită primește datele firmei emitente și ale clientului în antet.
- Opțiuni pe companie, în Vânzări → Configurare → Setări (blocul Oferte și Comenzi): numerotarea liniilor, descriere fără denumirea produsului, descriere micșorată, valoarea taxelor și totalul cu taxe pe linie, termen de livrare.
- Proforma nu este document fiscal; factura de avans se face separat. Detaliile și capturile sunt în fișa consultant.

#### 3. Dependențe

- `sale`
- [l10n_ro_report_common](../l10n_ro_report_common/index.md)
- [deltatech_sale_order_image](../deltatech_sale_order_image/index.md)

#### 4. Componente Cheie

**Modele**

- `res.company` și `res.config.settings` (extinse): opțiunile de tipărire (`counter_on_sale_order`, `exclude_product_name_from_description_offer`, `make_description_smaller`, `show_total_amount_with_taxes_on_so`, `show_lead_time`).

**Vizualizări**

- `views/sale_order.xml`: extinde raportul de ofertă (`sale.report_saleorder_document`) cu datele firmei și coloanele opționale și definește șabloanele proformei (`saleorder_proforma_percent_*`).
- `views/res_config_view.xml`: opțiunile din Setări.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- [deltatech_sale_payment](../deltatech_sale_payment/index.md): aduce suma încasată pe comandă, necesară proformei finale pe comenzile cu termene de plată.
