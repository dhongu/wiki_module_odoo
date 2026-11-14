# Romania - Invoice Report for Odoo Online (localizat la `l10n_ro_invoice_report_online/index.md`)

- **Nume Tehnic:** `l10n_ro_invoice_report_online`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_invoice_report_online
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_invoice_report_online`
- **Ultima Ingestie:** `2026-11-14`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Machetele românești ale facturii și ale chitanței, disponibile și pe Odoo Online. Modulul nu conține cod Python și se importă ca arhivă zip (Aplicații > Import Module). Este varianta „doar date” a modulului `l10n_ro_invoice_report`, pentru bazele de date unde nu poate rula cod personalizat. Are nevoie de `l10n_ro_report_common_online`, importat primul.

#### 2. Funcționalități Cheie

- **Factura** (raportul standard *Facturi*, modificat pe loc):
  - antet cu furnizorul și clientul alăturat: adresă, conturi bancare, CIF, NRC, capital social, TVA la încasare, adresă de livrare; unitatea operațională a jurnalului, când este setată;
  - linii cu număr de linie opțional, preț unitar fără TVA, valoarea TVA pe linie, total cu TVA opțional, preț de listă înainte de discount opțional, denumirea produsului scoasă din descriere la cerere; notele de credit se tipăresc cu valori negative;
  - subsol cu emitentul, delegatul și mijlocul de transport, livrările (sau recepțiile) facturii cu numerele AWB, mențiunea legală că factura este valabilă fără semnătură și ștampilă, informațiile suplimentare ale clientului, logo Coface opțional;
  - facturile plătite în numerar poartă dedesubt chitanța, cu suma în litere (doar la *Invoice PDF*, nu și la *PDF without Payment*).
- **Alte rapoarte:** *Voucher / Payment* (chitanță sau dispoziție de plată; la jurnal de numerar adaugă formularul 14-4-1 / 14-4-4, casieria și, la plăți, rândul actului de identitate) și *Invoices in company language* (limba partenerului companiei).
- **Setări pe companie**, fila *Romanian Invoice*: marcaj, e-mail și telefon în adrese, număr de linie, total cu TVA, preț de listă, denumire produs, comunicare plată, livrări, delegat, logo Coface. Pe contul bancar al companiei se bifează *Romania - Print in Report*.
- **Unitate operațională** pe jurnalul de vânzări (Facturare > Configurare > Jurnale): numele și adresa apar sub furnizor, iar conturile ei bancare le înlocuiesc pe cele ale companiei.
- **Câmpuri pe partener** (fila *Sales & Purchase*, grupul *Misc*): *Payment bank account* (contul companiei în care plătește clientul, setat pe facturile de client) și *Mean transport* (completat la delegat); în fila *Invoicing*, *Additional info for invoice*. Dacă se folosește contul de plată, contul bancar al companiei se marchează de încredere (*Send Money*), altfel Odoo nu confirmă facturile.
- **Delegat pe factură:** la alegerea delegatului (persoană, nu companie), mijlocul lui de transport se copiază pe factură.
- **Acțiunea *Set origin from pickings*** (Acțiuni, pe factură): scrie livrările (sau recepțiile) efectuate în câmpul *Source*.
- **Filtre de scadență** pe facturile de client: scadente mâine, azi, restante 1-7, 8-14, 15-30 zile și peste 30 de zile.
- Față de `l10n_ro_invoice_report`: nu modifică extrasele bancare și nu setează delegatul implicit din context.
- Fluxul pas cu pas este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `base_automation`
- `l10n_ro_report_common_online`

Modulul **exclude** `l10n_ro_invoice_report` (aceleași date în câmpuri diferite): cele două nu pot fi instalate împreună.

#### 4. Componente Cheie

**Modele**

Fără cod Python. Câmpurile personalizate (prefix `x_l10n_ro_`, ex. `x_l10n_ro_delegate_id`, `x_l10n_ro_mean_transp`) sunt declarate prin `data/ir_model_fields_data.xml` pe `account.move`, jurnal, partener și companie.

**Vizualizări**

- `views/invoice_report.xml`: macheta facturii (raportul standard modificat).
- `views/payment_report.xml`: raportul *Voucher / Payment*.
- `views/account_voucher_report.xml`: chitanța / dispoziția de plată.
- `views/account_move_views.xml`: delegat, mijloc de transport, filtre de scadență.
- `views/account_journal_views.xml`: unitatea operațională pe jurnal.
- `views/res_partner_views.xml`: cont bancar de plată, mijloc de transport, informații suplimentare.
- `views/res_company_views.xml`: fila *Romanian Invoice*.

**Acțiuni Automate / Acțiuni Server**

Definite în `data/base_automation_data.xml`, în locul codului Python:

- *Invoice: means of transport of the delegate*: la schimbarea delegatului, copiază mijlocul de transport pe factură.
- *Invoice: payment bank account of the partner* (și varianta pe formular): setează contul bancar de plată al partenerului pe facturile de client.
- *Set origin from pickings*: acțiune server manuală, scrie livrările în originea facturii.

#### 5. Conexiuni

- [l10n_ro_invoice_report](../l10n_ro_invoice_report/index.md): varianta cu cod Python a aceluiași raport (incompatibilă la instalare).
- `l10n_ro_report_common_online`: baza comună, necesară înainte de import.
