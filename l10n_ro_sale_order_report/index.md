# Romania - Proforma Invoice Report (localizat la `l10n_ro_sale_order_report/index.md`)

- **Nume Tehnic:** `l10n_ro_sale_order_report`
- **Versiune:** `19.0.1.0.14`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_sale_order_report
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_sale_order_report`
- **Ultima Ingestie:** `2026-10-26`

#### 1. Sumar

Acest modul permite tipărirea de facturi proforme direct din oferta (cotația) de vânzare. Sunt disponibile două tipuri de proformă: o proformă inițială, al cărei cuantum este calculat din liniile termenului de plată (prima linie de tip „procent" sau „fix"), și o proformă finală, care reflectă suma rămasă de încasat. Modulul este util pentru companiile care lucrează cu avansuri și plăți eșalonate, oferind clienților documente de plată clare înainte de emiterea facturii fiscale. În plus, personalizează formularul standard al ofertei de vânzare (adresă companie, numerotare, imagini, coloane suplimentare), pe baza unor opțiuni din setări.

#### 2. Funcționalități Cheie

- Tipărirea unei facturi proforme inițiale („Percent Proforma - first") din cotație, cu suma calculată din prima linie a termenului de plată (de tip „procent" sau „fix").
- Tipărirea unei facturi proforme finale („Percent Proforma - last"), cu suma rămasă de încasat (necesită procesarea prealabilă a unei plăți prin modulul Deltatech Sale Payment; fără plată, se tipărește suma întreagă).
- Opțiuni pe companie, în Setări, la blocul de cotații (setările comenzilor de vânzare), pentru formularul ofertei:
  - numărător al liniilor (activ implicit) și imaginea produsului pe linie (activă implicit);
  - excluderea numelui produsului din descrierea liniei, sau reducerea mărimii descrierii;
  - afișarea valorii taxelor și a totalului cu taxe pe fiecare linie;
  - afișarea termenului de livrare (lead time) în zile, doar dacă vreo linie îl are.
- Blocul de adresă al formularului ofertei folosește datele companiei din `l10n_ro_report_common`.
- La termene de plată cu două linii, formularul ofertei afișează tranșele de plată și valoarea fiecăreia.

#### 3. Dependențe

- `sale`
- [l10n_ro_report_common](../l10n_ro_report_common/index.md)

#### 4. Componente Cheie

**Modele**

- `res.company` (extins): câmpurile `counter_on_sale_order`, `include_image_line`, `exclude_product_name_from_description_offer`, `make_description_smaller`, `show_total_amount_with_taxes_on_so`, `show_lead_time`.
- `res.config.settings` (extins): expune opțiunile de mai sus în Setări.

**Vizualizări**

- `views/sale_order.xml`: extinde raportul standard `sale.report_saleorder_document` (`sale_order_company_data`) și definește șabloanele proformelor (`saleorder_proforma_percent_document`, `saleorder_proforma_percent_init`, `saleorder_proforma_percent_final`).
- `views/res_config_view.xml` (`res_config_settings_view_form`): opțiunile în blocul de cotații din setările de contabilitate.

**Acțiuni Automate / Acțiuni Server**

- `action_report_percent_proforma_init` și `action_report_percent_proforma_final` (`ir.actions.report`, PDF pe `sale.order`): rapoartele de proformă, disponibile din meniul Tipărire al ofertei. Nu există cron-uri.

#### 5. Conexiuni

- [deltatech_sale_payment](../deltatech_sale_payment/index.md): necesar pentru procesarea plăților, astfel încât proforma finală să poată reflecta suma rămasă de încasat (dependență comentată în manifest).
