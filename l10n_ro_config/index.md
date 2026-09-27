# Romania - Localization Config (localizat la `l10n_ro_config/index.md`)

- **Nume Tehnic:** `l10n_ro_config`
- **Versiune:** `20.0.0.9.0`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_config
- **Cale Locală:** `odoo-addons/l10n-romania-oca/l10n_ro_config`
- **Ultima Ingestie:** `2026-09-27`

#### 1. Sumar

Acest modul este poarta de intrare a localizării românești în Odoo: instalează automat (`auto_install`) odată cu modulul de bază `l10n_ro` și oferă o pagină dedicată în Configurare de unde se pot activa restul modulelor din suita de localizare română (facturare electronică, ANAF, stoc, TVA la încasare etc.). Pe lângă acest rol de "hub" de instalare, adaugă și câmpurile specifice legislației românești pe companie, parteneri, conturi bancare și jurnale contabile — vizibile doar pentru companiile care au bifat "Utilizează Contabilitatea Românească".

#### 2. Funcționalități Cheie

- Pagină dedicată "România" în Setări → Contabilitate/Facturare (vizibilă doar dacă țara companiei este RO), organizată pe blocuri: Parteneri & Adrese, Contabilitate, Integrare ANAF, Stoc — de unde se pot activa module opționale (adrese extinse, orașe/SIRUTA, unicitate parteneri după CUI, creare parteneri după CUI/VIES, validare fiscală, TVA la încasare, închidere perioade contabile, raport factură românesc, curs valutar editabil, sincronizare ANAF, contabilitate stoc, DVI etc.).
- Câmpuri dedicate pe companie: capital social (`l10n_ro_share_capital`), cod CAEN, taxe implicite pentru servicii (vânzare/achiziție), poziții fiscale pentru TVA la încasare și taxare inversă, conturi contabile pentru operațiuni de stoc (custodie, transfer, discount comercial, TVA neeligibil) și cont implicit de cheltuială nedeductibilă.
- Câmpuri dedicate pe partener: "TVA Subjected" (persoană plătitoare de TVA), cod CAEN, e-Facturare, plus separarea automată a CUI-ului de prefixul de țară (`l10n_ro_vat_number`) — permite introducerea unui CUI/CIF fără prefixul "RO" sau al altei țări (ex. un adószám maghiar pe 11 cifre, acceptat de VIES doar în forma pe 8 cifre).
- Pe contul bancar și pe jurnalul contabil (jurnal de bancă) există opțiunea "Ro Print in Report" pentru a decide ce cont bancar apare pe rapoarte (ex. antetul facturii); jurnalele contabile primesc și câmpuri pentru "Casă de marcat fiscală" și poziție fiscală românească.
- Pe produse de tip serviciu, taxele implicite de vânzare/achiziție definite la nivel de companie se aplică automat la schimbarea tipului produsului.
- Mixin-ul `l10n.ro.mixin` (folosit de mai multe modele — companie, partener, cont bancar, jurnal, `res.config.settings`) ascunde automat câmpurile, grupurile, filtrele și butoanele specifice localizării românești (`l10n_ro*`) din formulare/liste/căutări pentru companiile care nu folosesc contabilitatea românească, păstrând interfața curată pentru clienții non-RO.
- Grup de securitate dedicat "Romania Menus" (`group_ro_menus`) care controlează vizibilitatea paginii de configurare și a filei ANAF din formularul de partener.

#### 3. Dependențe

- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `res.company` (extins): zeci de câmpuri `l10n_ro_*` pentru capital social, cod CAEN, taxe implicite de servicii, poziții fiscale (TVA la încasare, taxare inversă) și conturi contabile de stoc/discount/nedeductibil; câmpul calculat `l10n_ro_accounting` (adevărat dacă șablonul de plan de conturi al companiei este `ro`).
- `res.partner` (extins, cu `l10n.ro.mixin`): `l10n_ro_vat_subjected`, `l10n_ro_vat_number` (calculat), `l10n_ro_caen_code`, `l10n_ro_e_invoice`; reimplementează separarea CUI/prefix de țară (`_split_vat`) rămasă fără echivalent în `base` după ce Odoo 20 a integrat `base_vat` în nucleu.
- `res.partner.bank` (extins, cu `l10n.ro.mixin`): câmpul `l10n_ro_print_report` pentru a marca ce cont bancar apare pe rapoarte.
- `account.journal` (extins, cu `l10n.ro.mixin`): `l10n_ro_print_report` (calculat din contul bancar), `l10n_ro_fiscal_receipt` (jurnal de bonuri fiscale), `l10n_ro_fiscal_position_id`.
- `product.template` (extins, cu `l10n.ro.mixin`): aplică automat taxele implicite de serviciu ale companiei la produsele de tip serviciu.
- `l10n.ro.mixin`: model abstract central, oferă câmpul `is_l10n_ro_record` și suprascrie `get_view` pentru a ascunde dinamic elementele de interfață `l10n_ro*` pe companiile non-românești.
- `ir.ui.menu` (extins): câmp `is_l10n_ro_record`.
- `ir.actions.actions` (extins): `get_bindings` elimină acțiunile contextuale definite de module `l10n_ro*` din meniul de acțiuni pe companiile non-românești.
- `account.chart.template` (extins, șablon `ro`): completează pe planul de conturi românesc valorile implicite pentru conturile/taxele de mai sus (ex. `pcg_371`, `pcg_4081`, `pcg_418`, taxe `tvac_21_s`/`tvad_21_s`).
- `res.config.settings` (wizard, cu `l10n.ro.mixin`): expune toate câmpurile de companie de mai sus, plus zeci de comutatoare `module_l10n_ro_*` pentru instalarea la cerere a celorlalte module din suita de localizare (adrese extinse, orașe, SIRUTA, unicitate parteneri, creare parteneri după CUI, validare fiscală, TVA la încasare, închidere perioade, rapoarte de plată, TVA nedeductibil, sincronizare ANAF, raport factură, curs valutar editabil, stoc, contabilitate stoc, diferență de preț, dată contabilă stoc, rapoarte de stoc, DVI etc.).

**Vizualizări**

- `view_account_bank_journal_tree` / `view_account_bank_journal_form`: adaugă pe jurnalul de bancă/casă câmpurile `l10n_ro_print_report`, `l10n_ro_fiscal_receipt`, `l10n_ro_fiscal_position_id`.
- `view_partner_bank_form` / `_tree` / `_search`: adaugă `l10n_ro_print_report` pe conturile bancare de parteneri.
- `view_partner_create_by_vat`: adaugă pe formularul de partener codul CAEN, bifa "TVA Subjected" și câmpul ascuns `l10n_ro_vat_number`, condiționate de `is_company`.
- `view_partner_anaf_status_form`: adaugă fila "ANAF" (vizibilă doar grupului `group_ro_menus`) pe formularul de partener, lângă fila Contabilitate.
- `res_config_settings_view_form` (moștenire pe formularul de setări): adaugă aplicația "România" (vizibilă doar dacă `country_code == 'RO'` și utilizatorul e în `group_ro_menus`), organizată în blocurile Parteneri & Adrese, Contabilitate, Integrare ANAF, Stoc, cu zeci de comutatoare de module și câmpuri de configurare.
- `res_config_settings_account_view_form` (moștenire pe setările de Contabilitate): adaugă comutatorul de actualizare curs BNR și taxele implicite de servicii (vânzare/achiziție).
- Template-uri QWeb `l10n_ro_config.banks` și `l10n_ro_config.report_address_company`: bloc reutilizabil pentru antetul de raport/factură — afișează adresa companiei, conturile bancare marcate „Print in Report”, CUI, NRC și capitalul social.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește `ir.cron`, `base.automation` sau `ir.actions.server`; automatizările sale sunt suprascrieri Python (`get_view`, `get_bindings`, `_check_vat`) executate sincron, nu joburi programate.

#### 5. Conexiuni

- `l10n_ro`: dependința directă, oferă planul de conturi și baza localizării peste care acest modul adaugă configurarea.
- `account`: extinde formularul de setări contabile și modelele `account.journal` / `account.chart.template`.
- `base`: extinde `res.partner`, `res.partner.bank`, `res.config.settings`, `ir.ui.menu`, `ir.actions.actions`.
- Zeci de module opționale `l10n_ro_*` (adresă extinsă, oraș, SIRUTA, unicitate parteneri, creare parteneri după CUI, validare fiscală, TVA la încasare, închidere perioade contabile, raport factură, curs valutar editabil, sincronizare ANAF, stoc, contabilitate stoc, diferență de preț, dată contabilă stoc, rapoarte de stoc, DVI etc.) sunt activabile din pagina de configurare a acestui modul, dar nu sunt dependențe stricte — nu au încă pagină wiki proprie.
