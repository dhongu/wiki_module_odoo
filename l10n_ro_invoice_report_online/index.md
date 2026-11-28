# Romania - Invoice Report for Odoo Online (localizat la `l10n_ro_invoice_report_online/index.md`)

- **Nume Tehnic:** `l10n_ro_invoice_report_online`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_invoice_report_online
- **Cale Locală:** odoo-addons/l10n-romania/l10n_ro_invoice_report_online
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Machetă românească pentru factură și chitanță, utilizabilă și pe **Odoo Online**: modulul nu are cod Python și se importă ca zip (Aplicații, Import modul). Este varianta doar cu date a modulului [l10n_ro_invoice_report](../l10n_ro_invoice_report/index.md), pentru baze de date unde nu rulează cod Python personalizat. Necesită `l10n_ro_report_common_online`, importat primul.

#### 2. Funcționalități Cheie

- **Factura** (raportul standard, modificat pe loc): furnizor și client alăturat, cu adrese, conturi bancare, CIF, NRC, capital social, TVA la încasare și adresă de livrare; punctul de lucru al jurnalului, când e setat.
- Linii: număr curent opțional, preț fără TVA, valoarea TVA pe linie, total cu TVA opțional, preț de listă înainte de discount, numele produsului scos din descriere la cerere; notele de credit tipărite cu valori negative.
- Subsol: emitent, delegat și mijloc de transport, livrările (sau recepțiile) facturii cu numerele AWB, mențiunea legală de valabilitate fără semnătură și ștampilă, informațiile suplimentare ale clientului, logo Coface opțional.
- Facturile plătite în numerar poartă dedesubt chitanța, cu suma în litere (doar pe **Invoice PDF**, nu pe varianta fără plată).
- Alte rapoarte: **Voucher / Payment** (chitanță sau dispoziție de plată, formularele 14-4-1 și 14-4-4 pentru casierie) și **Invoices in company language**.
- Setările se fac pe companie, tab-ul **Factură România** (e-mail, telefon, marcaj în adrese, nr. crt., total cu TVA, preț fără discount, nume produs, comunicare plată, livrări, delegat, logo Coface); pe contul bancar al firmei se bifează tipărirea în raport.
- Pe jurnalul de vânzări se setează **Punct de lucru**; pe partener, **Cont bancar de plată**, **Mijloc transport** și **Informații suplimentare în factură**.
- Filtre de scadență pe facturile client: scadent mâine, azi, restanțe 1-7, 8-14, 15-30 și peste 30 de zile.
- Automatizări în locul codului Python: mijlocul de transport al delegatului pe factură, contul bancar de plată al partenerului pe facturile client și acțiunea **Set origin from pickings**, care scrie livrările în originea facturii.
- Față de `l10n_ro_invoice_report`, nu modifică extrasele bancare și nu are delegat implicit din context. Nu se poate instala împreună cu acesta (manifestul îl exclude), pentru că păstrează aceleași date în câmpuri diferite.
- Pașii de configurare și utilizare sunt în fișa consultant.

#### 3. Dependențe

- `account`
- `base_automation`
- `l10n_ro_report_common_online`

Exclude: [l10n_ro_invoice_report](../l10n_ro_invoice_report/index.md).

#### 4. Componente Cheie

Descrierea modulului nu cere analiză de cod; mai jos, elementele principale.

**Modele**

- Nu definește clase Python; adaugă câmpuri prin `data/ir_model_fields_data.xml` pe `account.move`, `account.journal`, `res.partner` și `res.company`.

**Vizualizări**

- `views/invoice_report.xml`, `views/payment_report.xml`, `views/account_voucher_report.xml`: machetele de tipărire.
- `views/account_move_views.xml`, `views/account_journal_views.xml`, `views/res_partner_views.xml`, `views/res_company_views.xml`: câmpurile și filtrele adăugate.

**Acțiuni Automate / Acțiuni Server**

- `automation_delegate_mean_transp`: copiază mijlocul de transport al delegatului pe factură.
- `automation_partner_payment_bank_onchange` și `automation_partner_payment_bank`: setează contul bancar de plată al partenerului pe facturile client.
- Acțiunea server **Set origin from pickings**: completează originea facturii din livrări.

#### 5. Conexiuni

- [l10n_ro_invoice_report](../l10n_ro_invoice_report/index.md): varianta cu Python, incompatibilă cu aceasta.
- `l10n_ro_report_common_online`: baza comună a rapoartelor românești pentru Odoo Online.
