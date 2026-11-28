# Romania - Stocuri în custodie (localizat la `l10n_ro_stock_consignment/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_consignment`
- **Versiune:** `20.0.1.2.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_stock_consignment
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_consignment`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul gestionează bunurile primite sau date în custodie, fără transfer de proprietate, conform OMFP 1802/2014. Bunurile primite se țin în afara bilanțului (contul 8033), iar bunurile proprii date la terți trec în conturile de stocuri aflate la terți (357, 351, 354, 356 sau 358). Acoperă și stocurile la dispoziția clientului (call-off) trimise în alt stat membru UE, cu evidența termenului de 12 luni.

#### 2. Funcționalități Cheie

- **Custodie primită:** la validarea recepției, proprietarul (terțul) se setează înainte de mișcarea de stoc, deci bunurile nu intră în valorizarea proprie; se generează nota extrabilanțieră `Dr 8033 = Cr 803999` la prețul din procesul-verbal.
- **Stornare la retur:** returul total sau parțial stornează automat nota pentru cantitatea returnată; butonul **Stornează nota de custodie** stornează restul și nu permite o a doua stornare.
- **Custodie dată:** transferul marcat *Date în custodie* trebuie să ducă bunurile într-o locație „la terți” cu contul de evaluare 35x potrivit (mărfuri 357, materii 351, produse 354, active biologice 356, ambalaje 358); modulul refuză destinațiile greșite și bunurile terților.
- **Raport Bunuri în custodie** (Inventar → Raportare) și proces-verbal de predare-primire în PDF.
- **Conturi configurabile** în Contabilitate → Setări: cont de custodie (implicit 8033), contrapartidă (implicit 803999) și jurnal (implicit EXTR); conturile 35x se pun pe locațiile „la terți”.
- **Call-off (art. 270^1 Cod fiscal):** transferul se marchează *Stoc la dispoziția clientului (call-off)*, cu client vizat și dată a sosirii; evidența din Inventar → Raportare urmărește cantitățile expediate, preluate, returnate și rămase, valoarea din 357 și termenul de 12 luni, cu activități de reamintire și de expirare.
- **Preluare și retur call-off:** butonul **Preluare** postează `Dr 607 = Cr 357` la valoarea expedierii și cere factura către clientul vizat; butonul **Retur** deschide transferul de retur în ciornă, cu cantitatea rămasă, iar returul validat face nota `Dr 371 = Cr 357`.
- Secțiunea III din D390 o completează modulul-punte [l10n_ro_stock_consignment_d390](../l10n_ro_stock_consignment_d390/index.md).
- Fluxul pas-cu-pas, cu capturi, este în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `stock_account`
- `l10n_ro`
- [l10n_ro_off_balance](../l10n_ro_off_balance/index.md)

#### 4. Componente Cheie

**Modele**

- `stock.picking` (extins): tipul de custodie, nota generată la validare, stornarea notei și câmpurile call-off (client vizat, dată sosire).
- `stock.move` (extins): marcarea proprietarului și verificarea locațiilor „la terți”.
- `l10n.ro.call.off.line`: evidența call-off (expediat, preluat, returnat, rămas, valoare, termen, stare).
- `l10n.ro.call.off.take.over` (tranzitoriu): fereastra de preluare a bunurilor de către client.
- `res.company` / `res.config.settings` (extinse): conturile și jurnalul de custodie.

**Vizualizări**

- `view_picking_form_custody` / `view_picking_form_call_off`: câmpul **Custodie**, nota generată, butoanele de stornare și datele call-off pe transfer.
- `res_config_settings_view_form_custody`: conturile și jurnalul de custodie în Contabilitate → Setări.
- `view_location_form_custody`: configurarea locațiilor „la terți”.
- `action_l10n_ro_custody_quants` / `menu_l10n_ro_custody_quants`: raportul Bunuri în custodie.
- `action_l10n_ro_call_off_line` / `menu_l10n_ro_call_off_line`: evidența call-off.
- `view_l10n_ro_call_off_take_over_form`: fereastra de preluare.
- `action_report_l10n_ro_custody_pv`: raport PDF „Proces-verbal predare-primire custodie".

**Acțiuni Automate / Acțiuni Server**

- `Romania: call-off stock deadlines` (`data/ir_cron_data.xml`): cron zilnic care generează activitățile de reamintire înainte de termen și de expirare.

#### 5. Conexiuni

- [l10n_ro_stock_consignment_d390](../l10n_ro_stock_consignment_d390/index.md): completează secțiunea III din D390 cu expedierile și returnările call-off.
- [l10n_ro_off_balance](../l10n_ro_off_balance/index.md): conturile extrabilanțiere (8033/803999) folosite la custodia primită.
- `stock` / `stock_account`: consignația nativă (proprietar pe stoc) folosită pentru a exclude bunurile terților din valorizare.
