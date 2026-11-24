# Romania - Retururi POS (localizat la `l10n_ro_pos_returns/index.md`)

- **Nume Tehnic:** `l10n_ro_pos_returns`
- **Versiune:** `19.0.1.1.11`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_pos_returns
- **Cale Locală:** odoo-addons/l10n_ro_ent/l10n_ro_pos_returns
- **Ultima Ingestie:** `2026-11-24`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul tratează returul din comerțul cu amănuntul așa cum îl cere legislația română, pe două laturi care nu au sens una fără alta. Prima: la fiecare bon de retur se emite **factura de retur (storno)**, documentul pe care normele îl cer pentru ajustarea bazei de impozitare a TVA — vânzarea la casa de marcat e scutită de factură, dar scutirea nu se extinde la retur, iar fără acel document contabilul nu are pe ce să diminueze TVA-ul colectat. A doua: **restituirile de numerar apar pe rândul de plăți al registrului de casă**, nu netate în încasarea zilei, cum le scrie Odoo implicit. Modulul a pornit din tichetul #9362 (client Damira), unde 870 de retururi din doi ani și jumătate nu aveau niciun document fiscal, iar în registrul de casă restituirile erau invizibile.

#### 2. Funcționalități Cheie

- **Factură de retur automată** la finalizarea bonului de retur: document `out_refund` postat, cu cota de TVA și valoarea pe fiecare articol — exact informațiile pe care le cere contabilitatea.
- **Cumpărător identificat obligatoriu la retur.** Nu e vorba de completarea unui câmp: partenerul generic pentru clienți anonimi (desemnat prin modulul de partener generic al suitei) este refuzat, iar contactul trebuie să aibă datele cerute destinatarului unei facturi RO — țară, județ, oraș, stradă. Verificarea rulează la sincronizarea bonului, deci mesajul apare **la casă**, cât clientul e încă acolo, nu ca eroare de postare după ce a plecat cu banii.
- **Încasările brute și restituirile pe linii separate** pe contul de casă, la închiderea sesiunii — pentru registrul de casă cod 14-4-7A, care cere încasările pe rândul lor și plățile pe al lor. Soldul rămâne neschimbat.
- **Restul dat clientului rămâne netat**, fiind tot o plată de numerar negativă, dar pe un bon cu total pozitiv: un bon de 15,50 lei încasat cu 200 lei este o încasare de 15,50, nu o încasare de 200 și o plată de 184,50.
- **Emiterea în lot pentru perioada scursă** (`Issue Return Invoices`), din lista de comenzi POS: pentru un bon din sesiune închisă factura primește data curentă, iar contribuția bonului din nota de închidere se reversează în aceeași perioadă — TVA-ul nu se mută între perioade și nu sunt necesare declarații rectificative. Bonurile care nu pot fi facturate sunt sărite, cu motivul raportat.
- **Jurnal dedicat opțional** pentru facturile de retur, separat de jurnalul de facturi al punctului de vânzare.
- **Filtrele „Returns" și „Returns without Invoice"** pe comenzile POS, pentru inventarierea situației.
- **Dispoziția de plată din bonul de retur**, când e instalat modulul de casierie: butonul întocmește documentul pe casieria bonului, cu numerarul efectiv restituit.
- Interfață tradusă în română (`i18n/ro.po`).
- **Setări per punct de vânzare** (**Punct de vânzare → Configurare → Setări**, secțiunea **RO Return Invoicing**; repetate pentru fiecare casă): **Automatic Return Invoice** (emiterea facturii la fiecare bon de retur; oprită implicit), **Customer Required on Returns** (activă implicit; blochează finalizarea unui retur fără cumpărător) și **Return Invoice Journal** (gol = jurnalul de facturi al punctului de vânzare, care trebuie să existe, cerință a nucleului POS). **Atenție la combinație:** cu prima oprită și a doua pornită (starea implicită), casa blochează retururile fără client fără să emită vreo factură — se pornesc ambele (recomandat) sau se opresc ambele.
- **Separarea încasărilor de restituiri** se activează la nivel de companie, în **Contabilitate → Configurare → Setări**, secțiunea **RO Cash Register** → **Split POS Cash Receipts and Returns**; activă implicit la instalare, se aplică sesiunilor închise după activare (cele deja închise păstrează linia netă).
- **Clientul anonim**: contactul care ține locul cumpărătorului anonim se desemnează **partener generic** al companiei, cu modulul de partener generic al suitei (setările de contabilitate → Partener generic); rămâne utilizabil la vânzare, dar e refuzat la retur. Fără acel modul, verificarea se reduce la datele de identificare ale contactului ales.
- **Verificare**: în **Punct de vânzare → Comenzi**, filtrul **Returns without Invoice** trebuie să rămână gol în funcționare normală; ce apare acolo are nevoie de atenție (retururi fără cumpărător identificat sau bonuri venite prin sincronizare offline). Emiterea în lot se rulează din **Acțiuni → Emite facturile de retur**, iar notificarea spune câte facturi s-au emis și câte bonuri au fost sărite (fără cumpărător, contact incomplet, bon nefinalizat, deja facturat sau fără jurnal de facturi pe casă).
- **Panglica „Inversat"** de pe factura de retur nu înseamnă anulare: Odoo o afișează după ce documentul a fost stins integral prin plata de pe bon. La un retur introdus prin butonul de retur al POS-ului, în **Termeni și condiții** apare trimiterea la bonul stornat.
- **Transmitere în SPV**: pentru facturile de retur către persoane fizice se instalează și modulul de e-Factura B2C, care completează CNP-ul în XML-ul CIUS-RO.
- **Incompatibil cu `l10n_ro_pos_refund` (OCA)** (`excludes` în manifest): ambele emit factura storno și scriu restituirea pe linie proprie de casă, deci împreună ar dubla documentele.

#### 3. Dependențe

- `point_of_sale`
- `l10n_ro`

Manifestul declară și `excludes: l10n_ro_pos_refund` (vezi mai sus).

#### 4. Componente Cheie

**Modele**

- `pos.order` (extindere): câmpul stocat `l10n_ro_is_return`, marcarea bonului „de facturat" în `_process_saved_order`, verificarea de identificare a cumpărătorului, jurnalul dedicat și trimiterea la documentul stornat în `_prepare_invoice_vals`, acțiunea de emitere în lot și butonul de dispoziție de casă.
- `pos.session` (extindere): rescrie `_create_cash_statement_lines_and_cash_move_lines` ca să producă două linii de extras per metodă de plată — încasări brute pe debit, restituiri pe credit.
- `pos.config` (extindere): comutatoarele per punct de vânzare — factură de retur automată, client obligatoriu la retur, jurnal de facturi de retur.
- `res.company` (extindere): comutatorul `l10n_ro_pos_cash_split` pentru separarea încasărilor de restituiri.

Trei decizii de proiectare merită reținute, pentru că ghidează orice extindere:

1. **Returul se recunoaște după totalul negativ al bonului, nu după `is_refund`.** La casele reale returul se introduce cu cantități negative direct pe bon, iar indicatorul rămâne gol — măsurat în producție, `is_refund` era adevărat pe 6 bonuri din 75 cu total negativ.
2. **Poarta pentru client nu e scrisă în modul.** Bonul e marcat „de facturat", iar nucleul cere clientul în `OrderPaymentValidation.isOrderValid`, cu dialogul și traducerile lui. Verificarea server-side acoperă bonurile ajunse pe alte căi (sincronizare offline, alt client, import).
3. **Cheia `combine_receivables_cash` se golește înainte de `super()`**, ca nucleul să nu mai scrie linia netă; liniile se construiesc apoi cu helperii lui. Reconcilierea se face pe set, per cont, deci două linii se sting la fel de bine ca una. Partea `split` rămâne neatinsă, iar `l10n_ro_pos` (OCA) atinge doar `_accumulate_amounts`, deci nu se suprapun.

**Vizualizări**

- `res_config_settings_view_form_pos_return`: secțiunea „RO Return Invoicing" în setările punctului de vânzare.
- `res_config_settings_view_form_cash_split`: secțiunea „RO Cash Register" în setările de contabilitate.
- `view_pos_order_filter_l10n_ro_return`: filtrele „Returns" și „Returns without Invoice".
- `view_pos_pos_form_l10n_ro_cash_order`: butonul de dispoziție de casă pe bonul de retur.

**Acțiuni Automate / Acțiuni Server**

- `action_l10n_ro_invoice_returns`: acțiune de server legată pe `pos.order` (listă și formular), pentru emiterea în lot a facturilor de retur pe perioada scursă. Nu generează PDF și nu trimite e-mail — documentele se transmit ulterior, controlat, prin fluxul de e-Factura.

**Componente front-end**

- `static/src/js/pos_returns.esm.js`: marchează bonul de retur „de facturat" la intrarea în ecranul de plată, ca poarta nucleului pentru client să se aplice de la sine.

#### 5. Conexiuni

- [l10n_ro_cash_bank_enhanced](../l10n_ro_cash_bank_enhanced/index.md): găzduiește registrul dispozițiilor de casă (14-4-4) pe care butonul din bonul de retur îl alimentează. Legătura e verificată la rulare (modelul există în bază), nu prin dependență — dispoziția e necesară la orice ieșire de numerar, nu doar la retururi din POS.
- [l10n_ro_invoice_report](../l10n_ro_invoice_report/index.md): tipărește dispoziția de plată pentru plățile înregistrate ca `account.payment`; modulul de aici nu dublează acel flux.
- [l10n_ro_pos_fiscal_compliance](../l10n_ro_pos_fiscal_compliance/index.md): evidența bonului fiscal AMEF și raportul Z; când e instalat, trimiterea la bonul fiscal inițial intră în descrierea facturii de retur.
- `l10n_ro_pos` (OCA): scoate din nota de închidere liniile de ieșire din gestiune, pentru companiile cu contabilitate RO; atinge `_accumulate_amounts`, complementar cu acest modul.
- [deltatech_partner_generic](../deltatech_partner_generic/index.md): desemnează partenerul generic pentru clienți anonimi, pe care verificarea de la retur îl refuză.
- [l10n_ro_cash_register_report](../l10n_ro_cash_register_report/index.md) și `l10n_ro_cash_register` (OCA): cele două forme de registru de casă folosite în practică; ambele citesc liniile contabile de pe contul jurnalului, deci beneficiază de separarea încasări/restituiri fără modificări proprii.
- [l10n_ro_efactura_consumer](../l10n_ro_efactura_consumer/index.md): completează CNP-ul în XML-ul CIUS-RO pentru facturile către persoane fizice, utile la transmiterea facturilor de retur în SPV.
