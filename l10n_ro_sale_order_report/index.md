# Terrabit Sale Order Report (localizat la `l10n_ro_sale_order_report/index.md`)

- **Nume Tehnic:** `l10n_ro_sale_order_report`
- **Versiune:** `19.0.1.0.4`
- **Cale:** `https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_sale_order_report`
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_sale_order_report`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Acest modul permite tipărirea de facturi proforme direct din oferta (cotația) de vânzare. Sunt disponibile două tipuri de proformă: o proformă inițială, al cărei cuantum este calculat din liniile termenului de plată (prima linie de tip „procent" sau „fix"), și o proformă finală, care reflectă suma rămasă de încasat. Modulul este util pentru companiile care lucrează cu avansuri și plăți eșalonate, oferind clienților documente de plată clare înainte de emiterea facturii fiscale.

#### 2. Funcționalități Cheie

- Tipărirea unei facturi proforme inițiale din cotație, cu suma calculată din prima linie a termenului de plată (de tip „procent" sau „fix").
- Tipărirea unei facturi proforme finale, cu suma rămasă de încasat (necesită procesarea prealabilă a unei plăți prin modulul Deltatech Sale Payment).

#### 3. Dependențe

- `sale`
- `l10n_ro_config`

#### 4. Componente Cheie

Fișierul `readme/DESCRIPTION.md` este prezent și acoperă scopul și funcționalitățile modulului; conform fluxului de ingestie, analiza suplimentară a codului pentru această secțiune a fost omisă.

#### 5. Conexiuni

- `deltatech_sale_payment`: necesar pentru procesarea plăților, astfel încât proforma finală să poată reflecta suma rămasă de încasat.
