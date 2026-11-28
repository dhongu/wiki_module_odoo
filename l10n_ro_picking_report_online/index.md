# Romania - Picking Reports for Odoo Online

- **Nume Tehnic:** `l10n_ro_picking_report_online`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_picking_report_online
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_picking_report_online`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Documentele de stoc românești (NIR, aviz, bon de consum, transfer intern), disponibile și pe Odoo Online. Modulul nu conține cod Python și se importă ca arhivă zip (Aplicații > Importați modulul). Este varianta fără Python a modulului [l10n_ro_picking_report](../l10n_ro_picking_report/index.md), pentru bazele în care codul propriu nu poate rula.

#### 2. Funcționalități Cheie

- Rapoarte din meniul **Tipăriți** al transferului: Recepție (NIR), Recepție fără TVA și Recepție cu preț de vânzare (doar pe recepții), Aviz, Aviz cu preț, Bon de consum și Notă de transfer.
- NIR cu preț unitar, valoare, TVA, preț de vânzare și adaos procentual; cantități și prețuri în unitatea de pe document (o cutie de 13 kg rămâne cutie); prețul din comanda de achiziție sau din valoarea mișcării.
- Aviz și Aviz cu preț: prețul din comanda de vânzare (cu discount, cu TVA inclus sau nu); fără comandă, prețul din lista clientului, altfel prețul de listă.
- Livrarea bifată *Aviz de însoțire* se tipărește ca „Aviz de însoțire a mărfii" (14-3-6A); celelalte au titlul „Livrare".
- Pe documente: datele firmei și conturile bancare, gestionarul locației, delegatul și mijlocul de transport, numărul AWB (când e instalat modulul de curierat), semnăturile.
- Setări pe firmă (fila *Factură România*, grupul *Documente de stoc*): ascunde TVA pe NIR, ascunde băncile; pe locație: lista de prețuri a magazinului, gestionarul, *Este locație de tip magazin*.
- Automatizări în locul codului Python: delegatul aduce mijlocul de transport; prețul de vânzare se fixează pe mișcare la validarea recepției; recepția din comanda de achiziție primește ca document sursă referința furnizorului.
- Față de `l10n_ro_picking_report` nu are: rapoartele cumulative pe perioadă, butonul *Tipăriți* care alege singur raportul, facturarea din livrare cu delegatul și atașarea livrării semnate.
- Ordinea de import: `l10n_ro_report_common_online`, `l10n_ro_invoice_report_online`, apoi acest modul; limba română se instalează înainte. Pașii sunt în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `purchase_stock`
- `sale_stock`
- `l10n_ro_invoice_report_online`

#### 4. Componente Cheie

Descrierea din Readme nu detaliază componentele tehnice; lista provine din analiza datelor modulului (fără modele Python).

**Modele**

- `stock.picking`, `stock.move`, `stock.location`, `res.company`: câmpuri manuale (`x_`) create prin `data/ir_model_fields_data.xml`, cerute de Odoo Online.

**Vizualizări**

- `views/report_actions.xml`: acțiunile de raport (Delivery, Delivery with price, Consume Voucher, Reception, Reception without tax, Reception with sale price, Internal transfer).
- `views/report_picking.xml`: șabloanele QWeb ale documentelor.
- `views/stock_picking_views.xml`, `views/stock_location_views.xml`, `views/res_company_views.xml`: câmpurile pe transfer, locație și firmă.

**Acțiuni Automate / Acțiuni Server**

- `automation_picking_delegate_mean_transp`: mijlocul de transport al delegatului pe transfer.
- `automation_move_freeze_sale_price`: fixează prețul de vânzare pe mișcare la validarea recepției.
- `automation_move_purchase_origin`: referința furnizorului devine document sursă al recepției.

#### 5. Conexiuni

- [l10n_ro_picking_report](../l10n_ro_picking_report/index.md): varianta cu Python; nu se instalează împreună (excludere în manifest, import refuzat cât timp e instalat).
- [l10n_ro_report_common_online](../l10n_ro_report_common_online/index.md): blocurile comune de antet, cerute indirect prin `l10n_ro_invoice_report_online`.
