# Romania - Retururi POS (localizat la `l10n_ro_pos_returns/index.md`)

- **Nume Tehnic:** `l10n_ro_pos_returns`
- **Versiune:** `20.0.1.1.11`
- **Cale:** [https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_pos_returns](https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_pos_returns)
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_pos_returns`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul tratează returul din comerțul cu amănuntul așa cum îl cere legislația română: cu **factură de retur** pentru ajustarea bazei de TVA, cu **cumpărătorul identificat** încă de la casă și, împreună cu modulul de casierie, cu **dispoziția de plată** pentru numerarul restituit. Vânzarea la casa de marcat este scutită de factură (art. 319 alin. (10) lit. a) din Codul fiscal), dar scutirea nu se extinde la retur: pentru reducerea bazei de impozitare, normele de aplicare (HG 1/2016, pct. 32) cer o factură cu valori negative, iar bonul fiscal restituit și nota de stoc nu țin locul ei. Modulul a pornit din tichetul #9362 (client Damira), unde 870 de retururi din doi ani și jumătate nu aveau niciun document fiscal.

#### 2. Funcționalități Cheie

- **Factură de retur automată** la finalizarea bonului de retur, postată, de tip notă de credit, cu TVA și valoare pe fiecare articol; la returul introdus prin butonul de retur al POS, factura poartă trimiterea la bonul stornat (în Termeni și condiții). Se activează pe fiecare punct de vânzare, în **Punct de vânzare → Configurare → Setări**, secțiunea „Facturarea retururilor (RO)".
- **Identificarea obligatorie a cumpărătorului**: partenerul generic pentru clienți anonimi este refuzat la retur, iar contactul trebuie să aibă țara, județul, orașul și strada. Mesajul apare la casă, iar verificarea rulează și pe bonurile ajunse pe alte căi (sincronizare offline, alt client, import). Câmpul „Client obligatoriu la retur" este activ implicit.
- **Jurnal dedicat** pentru facturile de retur (opțional); gol, se folosește jurnalul de facturi al casei.
- **Atenție la combinația setărilor:** cu factura automată oprită și clientul obligatoriu pornit (starea implicită), casa blochează retururile fără client și nu emite nicio factură; setările se pornesc sau se opresc împreună.
- **Recunoașterea returului** după totalul negativ al bonului, nu după indicatorul de retur al POS (care rămâne gol la cantitățile negative introduse direct pe bon). Restul dat la o vânzare nu e retur.
- **Emitere pentru perioada scursă**, în lot, din lista de comenzi (**Acțiuni → Emite facturile de retur**): pentru o sesiune închisă factura primește data curentă, iar contribuția bonului din nota de închidere se reversează în aceeași perioadă. Nu generează PDF și nu trimite e-mail. Filtrele „Retururi" și „Retururi fără factură" ajută la inventariere.
- **Dispoziție de casă** (cod 14-4-4, OMFP 2634/2015) din butonul de pe bonul de retur, cu numerarul efectiv restituit și clientul ca beneficiar, dacă este instalat modulul de casierie; returul pe card nu primește dispoziție.
- **Registrul de casă:** pe Odoo 20 separarea încasărilor de restituiri o face nucleul POS (note de închidere distincte, cu linii de extras separate), nu modulul. Câmpul `l10n_ro_pos_cash_split` de pe companie a rămas doar ca să nu se piardă valoarea de pe 19.0.
- **Incompatibil cu `l10n_ro_pos_refund` (OCA)**, declarat în `excludes`: ambele emit factura de retur și ar dubla documentele.

#### 3. Dependențe

- `point_of_sale`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `pos.order` (extindere): câmpul stocat `l10n_ro_is_return`, marcarea bonului „de facturat" în `_process_saved_order`, verificarea cumpărătorului, jurnalul dedicat și trimiterea la bonul stornat în factură, acțiunea de emitere în lot și butonul de dispoziție de casă.
- `pos.config` / `res.config.settings` (extindere): comutatoarele per punct de vânzare — factură de retur automată, client obligatoriu, jurnal de facturi de retur.
- `res.company` (extindere): câmpul `l10n_ro_pos_cash_split`, fără efect pe 20.0 (păstrat pentru compatibilitate).

Decizia de proiectare care contează: poarta pentru client nu e scrisă în modul. Bonul e marcat „de facturat", iar nucleul POS cere clientul înainte de validare; verificarea de pe server acoperă bonurile ajunse pe alte căi.

**Vizualizări**

- `res_config_settings_view_form_pos_return`: secțiunea „Facturarea retururilor (RO)" în setările punctului de vânzare.
- `view_pos_order_filter_l10n_ro_return`: filtrele „Retururi" și „Retururi fără factură".
- `view_pos_pos_form_l10n_ro_cash_order`: butonul de dispoziție de casă pe bonul de retur.

**Acțiuni Automate / Acțiuni Server**

- `action_l10n_ro_invoice_returns`: acțiune de server pe `pos.order` (listă și formular), pentru emiterea în lot a facturilor de retur pe perioada scursă.

**Componente front-end**

- `static/src/js/pos_returns.esm.js`: marchează bonul de retur „de facturat" la intrarea în ecranul de plată, ca poarta nucleului pentru client să se aplice de la sine.

#### 5. Conexiuni

- [l10n_ro_cash_bank_enhanced](../l10n_ro_cash_bank_enhanced/index.md): găzduiește registrul dispozițiilor de casă (14-4-4) alimentat de butonul din bonul de retur; legătura e verificată la rulare, nu prin dependență.
- [l10n_ro_invoice_report](../l10n_ro_invoice_report/index.md): tipărește dispoziția de plată pentru plățile înregistrate ca `account.payment`.
- [l10n_ro_pos_fiscal_compliance](../l10n_ro_pos_fiscal_compliance/index.md): evidența bonului fiscal AMEF; când e instalat, trimiterea la bonul fiscal inițial intră în descrierea facturii de retur.
- [deltatech_partner_generic](../deltatech_partner_generic/index.md): desemnează partenerul generic pentru clienți anonimi, refuzat la retur.
- [l10n_ro_cash_register_report](../l10n_ro_cash_register_report/index.md): registrul de casă care citește liniile separate de încasări și restituiri.
- [l10n_ro_efactura_consumer](../l10n_ro_efactura_consumer/index.md): completează CNP-ul în XML-ul CIUS-RO pentru facturile către persoane fizice, util la transmiterea facturilor de retur în SPV.
- `l10n_ro_pos_refund` (OCA): modul exclus, care emite și el factura de retur.
