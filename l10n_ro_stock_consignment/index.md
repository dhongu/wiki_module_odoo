# Romania - Stocuri în custodie (localizat la `l10n_ro_stock_consignment/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_consignment`
- **Nume anterior:** `l10n_ro_stock_custody` (redenumit pe 23.09.2026: numele vechi e ocupat pe Odoo Apps de alt furnizor)
- **Versiune:** `19.0.1.2.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_stock_consignment
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_consignment`
- **Ultima Ingestie:** 2026-10-20
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul gestionează bunurile primite sau date în custodie, adică mărfuri care circulă între companie și un terț fără transfer de proprietate, conform OMFP 1802/2014. Bunurile primite se țin în afara bilanțului, pe contul **8033 — Valori materiale primite în păstrare sau custodie**, ca să nu distorsioneze stocul propriu valorizat și nici rezultatul financiar. Bunurile proprii date la terți rămân în patrimoniu și se urmăresc separat pe conturile 35x (de exemplu 357 — Mărfuri aflate la terți). Pe lângă custodie, modulul acoperă stocurile la dispoziția clientului (call-off) pentru bunuri trimise la un client dintr-un alt stat membru UE (art. 270^1 Cod fiscal), cu evidență, termen de 12 luni și preluare contabilizată.

#### 2. Funcționalități Cheie

- **Custodie primită** — la validarea recepției, modulul setează proprietarul (terțul) înainte de mișcarea de stoc (consignație nativă Odoo), astfel încât bunurile nu intră în valorizarea proprie, și generează nota extrabilanțieră **Dr 8033 = Cr 803999**, la prețul din procesul-verbal de predare-primire (altfel la costul produsului). Prețul se trece în coloana **Preț unitar custodie** de pe linii. Referința notei se salvează pe transfer.
- **Stornare la retur** — returul, total sau parțial, stornează automat nota pentru cantitatea returnată (Dr 803999 = Cr 8033), la prețurile notei inițiale. Butonul **Stornează nota de custodie** stornează restul și nu permite o a doua stornare.
- **Contrapartidă comună 803999** — nota folosește contrapartida tehnică comună din `l10n_ro_off_balance`, nu 8039 (care are funcțiune proprie în OMFP 1802/2014). La migrarea de la versiunile anterioare, soldul lui 8039 provenit din notele de custodie se mută pe 803999 printr-o notă de transfer **în ciornă** (jurnal EXTR), pe care contabilul o verifică și o postează.
- **Custodie dată** — transferul marcat *Date în custodie* duce bunurile proprii într-o locație „la terți” (tip Client) cu contul de evaluare 35x potrivit contului de stoc al produsului: mărfuri 357, materii și materiale 351, produse 354, active biologice de natura stocurilor 356, ambalaje 358. Din versiunea 19.0.1.1.4 modulul **nu mai generează notă proprie** pentru custodia dată: nota **Dr 35x = Cr contul de stoc** o face Odoo, prin contul de evaluare al locației, la costul real al ieșirii, iar la retur nota inversă, la valoarea ieșirii inițiale. Modulul refuză destinațiile greșite (locație internă, fără cont de evaluare sau cu alt cont) și bunurile terților.
- **Stocuri la dispoziția clientului (call-off)** — pe transferul de custodie dată se bifează **Stoc la dispoziția clientului (call-off)**, cu **Client vizat** (din alt stat UE, cu cod de TVA) și **Data sosirii** (goală = data validării). La validare se creează liniile din evidența call-off. Transferul se validează în ziua plecării bunurilor, pentru că data validării e luna expedierii din D390.
- **Evidența call-off** (`l10n.ro.call.off.line`, Inventar → Raportare → *Stoc la dispoziția clientului (call-off)*) — urmărește, pe produs, cantitățile expediate, preluate, returnate și rămase, valoarea din 357 și termenul de **12 luni de la sosire**. Este suportul registrului cerut de art. 321 alin. (6) Cod fiscal; câmpurile complete din art. 54a al Regulamentului (UE) 282/2011 se adaugă într-o versiune următoare.
- **Preluarea de către client** — butonul **Preluare** de pe linie deschide un wizard (cantitate, data preluării, factura, dacă există). Bunurile ies din locația „la terți” către client, fără să treacă prin depozit, iar modulul postează nota **Dr 607 = Cr 357** la valoarea expedierii (pro rata pe cantitate; ultima preluare ia exact valoarea rămasă). O factură către alt client este refuzată, pentru că livrarea către altă persoană încheie regimul (art. 270^1 alin. (8)). Factura de livrare intracomunitară scutită se emite direct din Contabilitate, nu din comanda de vânzare.
- **Retur din call-off** — butonul **Retur** (pe linie sau pe expediere) readuce bunurile în stoc cu nota Dr 371 = Cr 357.
- **Termen și reamintiri** — un cron zilnic programează o activitate de reamintire înainte de termen (implicit 30 de zile, configurabil în Setări) și una de expirare în ziua următoare termenului, pe transferul de expediere. După termen, preluarea și returul din evidență sunt refuzate, iar transferul în statul de destinație se tratează manual (autofactură, D390). Încă neautomatizate: înlocuirea clientului, transferul la expirare sau la pierderea bunurilor și expedierea mai departe în alt stat.
- **Raport Bunuri în custodie** — listează stocurile ținute pe seama terților (quant-uri cu proprietar setat) **doar pe locații interne și de tranzit**, accesibil din Inventar → Raportare. Lista poate fi grupată pe proprietar.
- **Proces-verbal predare-primire custodie** — raport PDF imprimabil de pe transferul de stoc, cu produsele, cantitățile și valorile.
- **Conturi configurabile** — în Contabilitate → Setări, secțiunea *România - Custodie stocuri*: contul de custodie (implicit 8033, căutat automat după cod), contrapartida (gol = 803999), jurnalul (gol = EXTR) și numărul de zile al reamintirii call-off. Conturile 35x se pun pe locațiile „la terți”, în câmpul **Cont stocuri aflate la terți (35x)**.
- **Secțiunea III din D390** — o completează modulul-punte [l10n_ro_stock_consignment_d390](../l10n_ro_stock_consignment_d390/index.md), instalat automat odată cu D390 sau cu acest modul.

> **De reținut** (din documentația modulului): readuceți bunurile în stoc numai cu **Retur**, nu printr-un transfer manual (se evaluează la costul curent și poate rămâne diferență pe 35x); nu vindeți și nu consumați direct din locația „la terți” (în afara preluării call-off); produsele fără cost nu intră în nota extrabilanțieră și pe transfer apare un mesaj; la produsele cu evaluare periodică nota 35x apare la închiderea evaluării stocului.

#### 3. Dependențe

- `stock_account`
- `l10n_ro`
- [l10n_ro_off_balance](../l10n_ro_off_balance/index.md)

#### 4. Componente Cheie

**Modele**

- `stock.picking` (extins): câmpurile `l10n_ro_custody_type` (primite/date în custodie), `l10n_ro_custody_move_id` și `l10n_ro_custody_reversal_move_id` (nota și stornarea ei) și `l10n_ro_custody_open`; la `button_validate()` verifică destinația custodiei date și generează nota extrabilanțieră pentru custodia primită; expune `action_l10n_ro_reverse_custody()`. Notele se creează cu `sudo()`, ca utilizatorii de stoc fără drepturi contabile să poată valida transferul.
- `stock.picking` (call-off, `stock_picking_call_off.py`): `l10n_ro_call_off`, `l10n_ro_call_off_partner_id`, `l10n_ro_call_off_arrival_date`, liniile de evidență, transferul/linia de preluare, nota și factura de preluare; verifică condițiile înainte de validare și creează liniile din evidență (cu `sudo()`).
- `stock.move` (extins): `l10n_ro_custody_price_unit`, `l10n_ro_custody_qty`, `l10n_ro_custody_value` (prețul din procesul-verbal și valoarea notei).
- `l10n.ro.call.off.line`: evidența call-off, pe produs (expediat/preluat/returnat/rămas, valoare, data sosirii, termen, stare, expirat); acțiunile `action_take_over()` și `action_return()` și cron-ul `_cron_l10n_ro_call_off_deadlines()`.
- `l10n.ro.call.off.take.over` (wizard): preluarea de către client (cantitate, dată, factură); creează transferul de preluare și postează nota Dr 607 = Cr 357.
- `res.company` (extins): conturile și jurnalul de custodie, `l10n_ro_call_off_alert_days`, metodele `_l10n_ro_get_custody_account()` și `_l10n_ro_custody_given_code()` (contul 35x potrivit produsului).
- `res.config.settings` (extins): câmpuri `related` către setările de pe companie.

**Vizualizări**

- `view_picking_form_custody`: pe transfer, câmpul **Custodie**, nota generată, **Preț unitar custodie** pe linii și butonul de stornare.
- `view_picking_form_call_off`: câmpurile call-off pe transfer și butonul către liniile de evidență.
- `view_l10n_ro_call_off_line_list` / `view_l10n_ro_call_off_line_search` / `action_l10n_ro_call_off_line` / `menu_l10n_ro_call_off_line`: evidența call-off, în Inventar → Raportare.
- `view_l10n_ro_call_off_take_over_form`: wizard-ul de preluare.
- `view_location_form_custody`: câmpul **Cont stocuri aflate la terți (35x)** pe locație.
- `res_config_settings_view_form_custody`: secțiunea de setări *România - Custodie stocuri*.
- `view_l10n_ro_custody_quant_list` / `action_l10n_ro_custody_quants` / `menu_l10n_ro_custody_quants`: raportul „Bunuri în custodie” (`stock.quant` cu proprietar, pe locații interne/tranzit).
- `action_report_l10n_ro_custody_pv`: raport QWeb-PDF „Proces-verbal predare-primire custodie”.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_l10n_ro_call_off_deadlines` („Romania: call-off stock deadlines”): rulează zilnic; programează activitatea de reamintire înainte de termen și pe cea de expirare, pe transferul de expediere. Restul logicii (note, stornări) rulează sincron la validare sau la apăsarea butoanelor.

#### 5. Conexiuni

- [l10n_ro_stock_consignment_d390](../l10n_ro_stock_consignment_d390/index.md): puntea către D390, completează secțiunea III cu stocurile la dispoziția clientului.
- [l10n_ro_anaf_d390](../l10n_ro_anaf_d390/index.md): declarația D390, în care apar bunurile expediate în regim call-off (instalare automată a punții).
- [l10n_ro_off_balance](../l10n_ro_off_balance/index.md): contrapartida tehnică comună 803999, jurnalul EXTR și nota de transfer folosită la migrare.
- `stock` / `stock_account`: consignația nativă (proprietar pe `stock.quant`/`stock.move.line`) și nota de evaluare 35x a locațiilor „la terți”.
- `l10n_ro`: planul de conturi românesc, sursa conturilor 8033, 35x, 371 și 607.
