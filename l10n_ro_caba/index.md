# Romania - TVA la încasare (CABA) (localizat la `l10n_ro_caba/index.md`)

- **Nume Tehnic:** `l10n_ro_caba`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_caba
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_caba`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul completează configurarea TVA la încasare (mecanismul nativ Odoo *cash basis*, cu jurnalul
CABA) pe planul de conturi al României. Planul RO aduce taxele la încasare, poziția fiscală
„Sistem de colectare TVA" și jurnalul CABA, dar lasă nesetat contul tehnic pe care se scriu
liniile de bază din notele de exigibilitate — fără el, la fiecare încasare baza rulează debit =
credit pe contul de venit sau cheltuială al facturii, ceea ce umflă rulajul acelui cont. Peste
configurarea automată, modulul decide **cine e efectiv la TVA la încasare** pe fiecare document —
firmă proprie, furnizor sau client — combinând bifa companiei cu poziția fiscală de pe partener,
astfel încât o firmă normală nu ajunge niciodată să vândă cu TVA la încasare doar pentru că regimul
clientului o cerea. Semnalează în Setări orice configurare incompletă și oferă contabilului o fișă
consultant cu fluxul complet, matricea celor 8 cazuri, notele contabile și reflectarea în D300.

#### 2. Funcționalități Cheie

- La instalare și la încărcarea planului RO setează automat, **doar unde e gol**: bifa Baza de
  numerar (`tax_exigibility`), jurnalul CABA (`tax_cash_basis_journal_id`) și contul tehnic
  **442830 „Bază TVA - cont tehnic (sold zero)"**, creat dacă lipsește; nu suprascrie valorile deja
  alese de contabil. Rulează doar dacă firma are taxe la încasare (`tax_exigibility = on_payment`)
  configurate pe planul RO.
- Bifă nouă în Setări, **Compania aplică TVA la încasare** (`l10n_ro_caba_company`): pentru o firmă
  înregistrată la ANAF în sistem, toate facturile și comenzile (vânzare, achiziție, POS) cu
  parteneri din România primesc singure poziția fiscală **Sistem de colectare TVA**, fără să mai
  fie nevoie s-o pună cineva pe fiecare partener. O poziție deja aleasă manual pe partener (ex.
  taxare inversă) câștigă și nu e înlocuită.
- Pentru o firmă **normală** (bifa nebifată), regimul se citește doar de pe partener: o achiziție
  de la un furnizor cu poziția **Sistem de colectare TVA** e la încasare, dar o vânzare **niciodată**
  — chiar dacă furnizorul respectiv e și client, factura lui de vânzare rămâne la TVA obișnuit
  (regimul cumpărătorului nu contează pentru exigibilitate, art. 282 alin. (3) Cod fiscal). Modulul
  scoate automat poziția la încasare de pe facturile de vânzare ale firmei normale la calculul
  poziției fiscale.
- **Alegere automată după registrul RTVAI** (din 19.0.1.2.0): pe o firmă normală, factura de achiziție de la un furnizor fără poziție fiscală pusă de mână primește singură poziția **Sistem de colectare TVA** când furnizorul e în registrul RTVAI la data facturii, după perioadele sincronizate de [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md) (dacă e instalat și OCA `l10n_ro_vat_on_payment` nu e). Poziția se recalculează la schimbarea datei facturii, iar storno-ul urmează factura corectată. Verificarea din Setări semnalează furnizorii la care poziția pusă de mână contrazice registrul.
- **Cine e la încasare** (compania proprie × operațiune × partener): firmă normală — vânzare către orice client = TVA obișnuit (poziția se scoate singură), achiziție de la furnizor normal = TVA obișnuit, achiziție de la furnizor în sistem = la încasare (44282); firmă în sistem — vânzare către orice client din România = la încasare (44281), achiziție de la orice furnizor din România = la încasare (44282).
- **Excepții:** firmele din același grup (persoane afiliate) facturează cu TVA obișnuit, dar modulul nu le recunoaște singur — pe factura de vânzare se schimbă poziția în **Regimul național (TVA)** înainte de confirmare; partenerii din alte țări nu primesc poziția automat (o vânzare taxabilă în România către un partener străin se încadrează de mână); o altă poziție pusă pe partener (ex. taxare inversă) are prioritate; comenzile de vânzare și comenzile POS către un furnizor în sistem care e și client preiau poziția de pe partener și se corectează înainte de confirmare; operațiunile scutite, taxarea inversă, importul și achizițiile intracomunitare rămân pe regulile generale. Bifa **Compania aplică TVA la încasare** nu are dată: se schimbă exact la data de efect, după confirmarea ciornelor (comenzile și ciornele create înainte păstrează poziția veche).
- Contul tehnic pentru bază este **442830**; 44281 și 44282 sunt conturile de tranziție ale TVA-ului și nu se folosesc pentru bază (verificarea din Setări marchează cazul cu roșu). La o încasare parțială, TVA-ul se mută proporțional din 44281 în 4427 (la achiziții din 44282 în 4426), iar baza trece tehnic pe 442830, o dată pe debit și o dată pe credit; nota CABA se deschide din butonul **Înregistrări pe bază de numerar** de pe factură. În D300, baza și TVA-ul intră în perioada încasării sau plății, pe rândurile obișnuite ale cotei, fără rânduri separate pentru TVA la încasare.
- În **Contabilitate → Configurare → Setări → Taxe**, sub blocul „Baza de numerar", adaugă blocul
  „Configurare TVA la încasare (RO)" cu o verificare vizibilă doar pentru companii cu țara fiscală
  România (afișată acum pe toată lățimea blocului, nu doar pe lățimea textului): CABA dezactivat,
  jurnal lipsă, taxe la încasare fără cont de tranziție (4428), cont de bază gol, cont de bază
  suprapus peste 44281/44282 sau pus pe un cont de venituri/cheltuieli, taxe interne nemapate de
  poziția fiscală pe încasare.
  Butonul **Completează configurarea** rulează aceeași setare automată din instalare, doar pe
  compania curentă.
- Redenumește în interfață câmpul „Cont de primire fiscală de bază" (traducere greșită moștenită
  din nucleu) în „Cont tehnic pentru baza TVA la încasare" și explică rolul lui în tooltip.
- Fișa consultant, verificată de expert contabil, descrie fluxul complet: configurare inițială,
  matricea celor 8 cazuri companie × partener × sens (cine e la încasare, pe vânzare și pe
  achiziție), excepțiile (firme din același grup, parteneri străini, persoane fizice, TVA
  nedeductibil), intrarea și ieșirea din sistem, limitarea comenzilor de vânzare și POS către un
  furnizor care e și client, notele contabile la facturare și la încasările/plățile parțiale,
  reflectarea în D300, operațiunile excluse din mecanism și motivul alegerii contului tehnic 442830
  (analitic al 4428, lângă 44281/44282) în locul contului 473 (sume în curs de clarificare).
- Nu depinde de modulul OCA `l10n_ro_vat_on_payment` (lista ANAF de firme la încasare și aplicarea
  automată a poziției fiscale pe factură) și nici de `l10n_ro_anaf_partner`; cele două module se pot instala împreună. Controlul pe
  perioadele deja declarate rămâne în `l10n_ro_vat_on_payment_lock`.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `res.company` (extindere): adaugă `account_cash_basis_base_account_id` (contul tehnic 442830) și
  bifa `l10n_ro_caba_company` (Compania aplică TVA la încasare); metodele
  `_l10n_ro_caba_setup()` (completează configurarea, doar câmpurile goale),
  `_l10n_ro_caba_check()` / `_l10n_ro_caba_check_html()` (verificarea afișată în Setări),
  `_l10n_ro_caba_get_base_account()` (caută sau creează contul 442830), `_l10n_ro_caba_applies()`
  (compania, sau părintele ei pentru o ramură, e în sistem), `_l10n_ro_caba_domestic_partner()`
  (partenerul e din România sau fără țară), `_l10n_ro_caba_replaceable()` (doar poziția obișnuită
  se înlocuiește cu cea la încasare, nu o poziție specială aleasă manual) și
  `_l10n_ro_caba_fiscal_position()` (poziția „Sistem TVA la încasare" din planul RO).
- `account.fiscal.position` (extindere): `_get_fiscal_position()` aplică poziția la încasare
  automat pentru o companie în sistem, pe orice document cu partener intern fără poziție pusă
  manual — de aici o iau atât facturile, cât și comenzile de vânzare și de achiziție.
- `account.move` (extindere): `_compute_fiscal_position_id()` scoate poziția la încasare de pe
  facturile de vânzare ale unei firme **normale** (fără bifa `l10n_ro_caba_company`), chiar dacă
  clientul e și furnizor cu poziția pusă pe partener — regimul cumpărătorului nu influențează
  exigibilitatea la vânzare. Pe o firmă normală, la achiziții aplică poziția la încasare când
  furnizorul e în registrul RTVAI la data facturii (`_l10n_ro_caba_supplier_on_payment`, doar dacă
  `l10n_ro_anaf_partner` e instalat și OCA `l10n_ro_vat_on_payment` nu e).
- `account.chart.template` (extindere): `_post_load_data()` rulează `_l10n_ro_caba_setup()` după
  încărcarea planului de conturi RO, ca pas echivalent celui din `post_init_hook` pentru companiile
  create după instalarea modulului.
- `res.config.settings` (extindere): expune `account_cash_basis_base_account_id`,
  `l10n_ro_caba_company` (related pe companie) și câmpul calculat `l10n_ro_caba_check_html`;
  acțiunea `action_l10n_ro_caba_setup()` din butonul „Completează configurarea" declanșează setarea
  și reîncarcă pagina.

**Vizualizări**

- `res_config_settings_view_form_l10n_ro_caba`: extinde formularul de setări contabile — redenumește
  eticheta câmpului de cont tehnic și adaugă blocul „Configurare TVA la încasare (RO)" (vizibil doar
  pentru `country_code = 'RO'`) cu bifa Compania aplică TVA la încasare, textul verificării pe toată
  lățimea blocului și butonul de completare automată.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: la instalarea modulului rulează `_l10n_ro_caba_setup()` pe toate companiile
  existente.

#### 5. Conexiuni

- [l10n_ro_vat_on_payment_lock](../l10n_ro_vat_on_payment_lock/index.md): controlează perioadele deja
  declarate pentru TVA la încasare; `l10n_ro_caba` doar completează configurarea contabilă a
  mecanismului.
- `l10n_ro_vat_on_payment` (OCA): aduce lista ANAF a firmelor la TVA la încasare și aplicarea
  automată a poziției fiscale pe factură; se poate instala împreună cu `l10n_ro_caba`, fără
  dependență între ele.
- [l10n_ro_account_vat_journal](../l10n_ro_account_vat_journal/index.md): jurnalele de TVA pe
  regimuri folosesc aceleași taxe la încasare configurate corect de acest modul.
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): declarația D300 preia baza și TVA-ul din
  notele CABA generate la încasarea/plata facturilor, în luna încasării.
- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md): opțional — registrul RTVAI sincronizat de acest modul alimentează alegerea automată a poziției la încasare pe achiziții și verificarea furnizorilor din Setări; fără el, regimul furnizorului se pune manual pe partener.
- `l10n_ro_dvi`: modul fără pagină wiki încă.
- `l10n_ro_nondeductible_vat`: modul fără pagină wiki încă; a inspirat convenția de a folosi un
  analitic al 4428 pentru contul tehnic de bază, în loc de 473.
