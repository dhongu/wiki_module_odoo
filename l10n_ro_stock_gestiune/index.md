# Romania - Gestiuni contabile de stoc (localizat la `l10n_ro_stock_gestiune/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_gestiune`
- **Versiune:** `20.0.3.2.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_stock_gestiune
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_gestiune`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul ține evidența gestiunilor contabile de stoc conform Legii 82/1991 și OMFP 2861/2009. Fiecare gestiune are gestionar responsabil, conturi proprii și locații interne asociate. Modulul oferă și transferul valoric între gestiuni (direct, prin tranzit sau, la subunitățile cu contabilitate proprie, prin 481/482) și recepția fără factură (371 = 408). Se adresează firmelor cu mai multe depozite, magazine sau puncte de lucru.

#### 2. Funcționalități Cheie

- **Model gestiune RO:** cod, gestionar, cont de stoc principal, marcaj de subunitate cu contabilitate proprie și cont de transfer 481/482, cont 408 propriu, jurnal de transfer, politică de inventariere (la cerere / periodică / anuală), perioadă de valabilitate și stare activ/inactiv. Meniu: Inventar → Configurare → Gestiuni contabile.
- **Locații pe gestiune:** fiecare locație internă se asociază unei gestiuni; wizardul de atribuire propune în masă locațiile fără gestiune.
- **Transfer valoric inter-gestiune:** direct `371.B = 371.A`, prin tranzit (`371.T = 371.A` la plecare, `371.B = 371.T` la sosire, cu contul de tranzit pe locația de tranzit) sau prin 481/482 la subunități; valoarea este costul curent × cantitatea, iar la produsele valorizate pe lot/serie, costul specific al fiecărui lot. Opt-in prin contul de stoc propriu al gestiunii.
- **Blocări configurabile:** transfer fără cont de contrapartidă (blocare strictă), gestiune obligatorie pe locațiile implicate în mișcări valorizate, valabilitatea gestiunii la data locală a mișcării. Pe o gestiune cu cont propriu, recepțiile și ieșirile directe sunt blocate, iar soldul contului rămâne egal cu valoarea mărfii.
- **Recepție fără factură (371 = 408):** nota se generează automat la recepție, linia facturii furnizorului se rutează pe 408, iar pivotul se stinge prin document, cu diferența de preț pe 308/371 și diferența de curs pe 765/665; storno la retur. Contul 408 nu trebuie să fie reconciliabil.
- **Raport de excepții:** locații fără gestiune, gestiuni fără cont de stoc, stoc negativ, loturi fără cost.
- **Aviz pe transfer:** câmpul `l10n_ro_notice`, cu valoare implicită pe tipul de operațiune.
- Fluxurile detaliate, cu capturi, sunt în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `stock_account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.gestiune` (nou): gestiunea contabilă, cu toate câmpurile RO.
- `stock.location` (extins): `l10n_ro_gestiune_id` și contul de stoc pentru tranzit.
- `stock.move` (extins): notele de transfer inter-gestiune și de recepție fără factură (371 = 408), storno la retur, blocările pe gestiuni cu cont propriu.
- `account.move` / `account.move.line` (extinse): rutarea liniilor pe 408, închiderea pivotului cu diferență de preț și de curs, legătura cu recepția de origine.
- `stock.picking` / `stock.picking.type` (extinse): câmpul aviz și valoarea implicită.
- `res.company` / `res.config.settings` (extinse): blocare strictă, gestiune obligatorie, recepție fără factură, contul 408 implicit.
- `l10n.ro.gestiune.assign.wizard`, `l10n.ro.gestiune.exception.report` / `.line` (tranzitorii): atribuirea în masă și raportul de excepții.

**Vizualizări**

- `view_l10n_ro_gestiune_form` / `view_l10n_ro_gestiune_list`, `action_l10n_ro_gestiune` / `menu_l10n_ro_gestiune`: gestiunile contabile.
- `res_config_settings_view_form_l10n_ro_gestiune`: opțiunile din Setări → Contabilitate.
- `view_location_form_l10n_ro_gestiune`: gestiunea și contul de tranzit pe locație.
- `view_picking_form_l10n_ro_notice` și vizualizările înrudite: avizul pe transfer, listă, căutare și tipul de operațiune.
- `action_l10n_ro_gestiune_assign_wizard` și `action_l10n_ro_gestiune_exception_report`: wizardul de atribuire și raportul de excepții.

**Acțiuni Automate / Acțiuni Server**

- Nu există `ir.cron` sau `base.automation`. `data/deactivate_oca_view.xml` dezactivează view-ul OCA `l10n_ro_stock_account.view_picking_form`, dacă e prezent, ca să nu se dubleze câmpul „aviz"; notele contabile se generează în logica modelelor, la validarea transferului și la postarea facturii.

#### 5. Conexiuni

- [l10n_ro_stock_gestiune_valuation](../l10n_ro_stock_gestiune_valuation/index.md): puntea (auto_install) care leagă fiecare gestiune de o arie de evaluare.
- [l10n_ro_stock_sheet](../l10n_ro_stock_sheet/index.md): balanța analitică a stocurilor și fișa de magazie, pentru verificarea firului valoric.
- [l10n_ro_stock_sheet_gestiune](../l10n_ro_stock_sheet_gestiune/index.md): puntea (auto_install) care filtrează fișa de magazie și balanța pe gestiune.
- [l10n_ro_stock_constraints](../l10n_ro_stock_constraints/index.md): protecția datelor de stoc după validare.
- [l10n_ro_currency_revaluation](../l10n_ro_currency_revaluation/index.md): 408 în valută nu e reevaluat lunar în configurația standard RO; soldul rămas nefacturat se reevaluează manual.
- `l10n_ro_stock_account` (OCA): oferă un câmp „aviz" similar; instalarea simultană nu e recomandată, iar view-ul OCA se dezactivează automat.

#### Limitări cunoscute (din fișa consultant)

- **Contul propriu al gestiunii e folosit doar la transfer.** O gestiune din care se vinde direct trebuie să folosească contul categoriei.
- **Tranzitul fără cont de tranzit pe locație** e blocat doar cu regula strictă activă; altfel nu se generează nicio notă.
- **Balanța filtrată pe gestiune** are *Soldul sintetic* nefiltrat, deci *Diferența* nu e 0 pe un cont folosit de mai multe gestiuni.
- **Valoarea transferului** e costul curent × cantitatea; la FIFO nu se mută straturile consumate.
- **408 în valută** nu e reevaluat lunar automat.
