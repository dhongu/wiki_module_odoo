# Romania - Gestiuni contabile de stoc (FR-54) (localizat la `l10n_ro_stock_gestiune/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_gestiune`
- **Versiune:** `19.0.3.1.0`
- **Cale:** `https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_stock_gestiune`
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_gestiune`
- **Ultima Ingestie:** `2026-09-25`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul aduce în Odoo evidența gestiunilor contabile de stoc așa cum o cere legislația românească (Legea 82/1991 și OMFP 2861/2009). Fiecare gestiune (depozit, magazin, punct de lucru) devine o entitate contabilă completă, cu propriul model `l10n.ro.gestiune`: are un gestionar responsabil, un cont de stoc propriu din clasa 3 (folosit doar la transferul între gestiuni, nu la recepții), un marcaj de „Subunitate cu contabilitate proprie", un cont de transfer inter-gestiune (481/482, doar pentru subunități), un cont de recepție fără factură (408) și o politică de inventariere, plus o fereastră de valabilitate. Pe lângă organizarea gestiunilor și atribuirea lor pe locațiile interne, modulul automatizează trei operațiuni-cheie: generează nota de transfer valoric la mutarea mărfii între gestiuni cu conturi de stoc diferite (direct `371.B = 371.A` între gestiuni ale aceleiași contabilități, prin contul de tranzit al locației sau, la subunități, prin 481/482), validează (opțional, strict) aceste transferuri și blochează recepțiile/ieșirile directe pe o gestiune cu cont propriu, și gestionează recepția fără factură (nota 371 = 408), astfel încât marfa primită de la furnizor să fie înregistrată corect în contabilitate chiar înainte de sosirea facturii, cu stingerea determinată de documente — fără reconciliere manuală. Scopul este o evidență de stoc conformă, cu trasabilitate clară a responsabilităților și a fluxului valoric pe gestiune, monografii aliniate la OMFP 1802/2014 după auditul contabil al fișei de consultanță (versiunea 19.0.3.1.0).

#### 2. Funcționalități Cheie

- **Model propriu de gestiune contabilă** (`l10n.ro.gestiune`, meniu Inventar → Configurare → Gestiunea depozitului → Gestiuni contabile): cod, gestionar responsabil (OMFP 2861/2009), cont de stoc principal (clasa 3, ex. 371.01), marcaj **Subunitate cu contabilitate proprie**, cont de transfer inter-gestiune (481/482, folosit doar dacă marcajul e bifat), cont de recepție fără factură (408) propriu (opțional, altfel se folosește cel al companiei), jurnal de transfer propriu, politică de inventariere (la cerere / periodică / anuală), perioadă de valabilitate (valabil de la / până la) și stare activ/inactiv.
- **Locații pe gestiune:** fiecare locație internă (`stock.location`) se asociază unei gestiuni contabile, direct sau prin asistentul de atribuire în masă; câmpul apare pe formularul locației, în grupul „Informații suplimentare", vizibil doar pentru locațiile interne. Locația de tip *Tranzit* primește propriul câmp **Cont de stoc pentru tranzit** (ex. 371.T), vizibil doar pentru locațiile de tranzit. O gestiune nu poate aparține altei companii decât locația (constrângere).
- **Notă de transfer valoric inter-gestiune:** între gestiuni ale aceleiași contabilități, nota e directă, `371.B = 371.A`, fără 481 (OMFP 1802/2014, pct. 95). La o subunitate cu contabilitate proprie, fiecare latură trece prin contul de transfer (481/482): `Cr 371.A / Dr 481` la ieșire, `Dr 371.B / Cr 481` la intrare. Prin tranzit, valoarea stă temporar pe contul de tranzit al locației: `371.T = 371.A` la plecare, `371.B = 371.T` la sosire (481/482 dacă gestiunea capătului e subunitate). Valoarea = cost curent (CMP/standard) × cantitate, iar pentru produsele valorizate pe lot/serie (`lot_valuated`), valoarea fiecărui lot mutat (cost specific al lotului × cantitate). Nota folosește jurnalul gestiunii, cu fallback pe jurnalul de stoc al companiei. Participarea la transfer e opt-in, prin contul de stoc propriu setat pe gestiune.
- **Validarea transferurilor inter-gestiune:** cu opțiunea **Blocare transfer fără cont de contrapartidă** activă (Inventar → Configurare → Setări, blocul Evaluare), transferul între gestiuni cu conturi de stoc diferite este blocat dacă lipsește contul de contrapartidă necesar — contul de tranzit al locației de tranzit, sau contul de transfer al unei subunități cu contabilitate proprie. Fără regula strictă, tranzitul fără cont de tranzit nu generează nicio notă contabilă (marfa se mută doar fizic).
- **Gestiune cu cont propriu, folosit doar la transfer:** pe o gestiune al cărei cont de stoc diferă de contul categoriei produsului, recepțiile și ieșirile directe (vânzare, consum, inventar, casare, retur) sunt blocate — acestea se contabilizează pe contul categoriei și ar lăsa sold rezidual pe contul gestiunii. Marfa intră și iese din ea doar prin transfer, dintr-o gestiune care folosește contul categoriei.
- **Evidență obligatorie pe gestiuni (opțional):** validarea unei mișcări valorizate poate fi blocată dacă o locație internă implicată nu are gestiune contabilă atribuită sau dacă gestiunea nu este validă (activă și în fereastra de valabilitate) la data mișcării.
- **Wizard de atribuire în masă:** propune locațiile interne fără gestiune și le atribuie unei gestiuni alese, util la activarea evidenței pe gestiuni.
- **Raport de excepții:** identifică dintr-o privire locațiile fără gestiune, gestiunile fără cont de stoc, stocurile negative în locațiile gestiunilor și loturile valorizate fără cost.
- **Recepție fără factură (371 = 408):** pentru produse stocabile cu valorizare perpetuă, la recepția de la furnizor se generează automat nota 371 = 408 — fie global (setarea de companie „Recepție fără factură (371 = 408)"), fie punctual, per transfer marcat „Recepție pe aviz" (`l10n_ro_notice`), cu posibilitate de valoare implicită pe tipul de operațiune. Recepția intră pe contul de stoc al **categoriei produsului**, nu pe contul propriu al gestiunii. Linia 408 poartă furnizorul comercial al transferului (sau al comenzii de achiziție, sau al recepției originale la retur), astfel încât 408 se stinge și pe fișa furnizorului (OMFP 1802/2014, pct. 329).
- **Stingerea pivotului 408 la factură, fără reconciliere:** la postarea facturii furnizorului, linia de produs este rutată automat pe contul 408 (nu pe 371); închiderea este determinată de documente, nu de potrivirea sumelor, deci 408 nu trebuie marcat „Permite reconcilierea".
- **Suport multi-monedă:** pentru achiziții în valută, latura 408 de la recepție păstrează valuta comenzii; diferența de curs recepție↔factură se recunoaște automat pe 765/665 la primirea facturii. Stocul (371) rămâne la cursul recepției — activ nemonetar, nu se reevaluează la curs.
- **Tratarea diferenței de preț:** când prețul de pe factură diferă de valoarea recepției, diferența se contează pe 308 (materii prime/materiale) sau 378 (mărfuri) la cost standard, sau pe contul de stoc 371 (FIFO/CMP), corectând costul stocului ca în comportamentul nativ Odoo.
- **Firmele cu storno la retururi/facturi:** diferențele de curs recepție↔factură și majorarea de preț se contabilizează în negru, pe latura normală (`Dr 408 / Cr 765`, `Dr 665 / Cr 408`, `Dr 371 / Cr 408`); doar reducerea de preț se stornează în roșu, pe ambele linii ale notei (`371 = 408` cu semn negativ) — conform OMFP 1802/2014, pct. 69, care tratează reducerea de preț ca o corecție a valorii recepției, nu ca o operațiune nouă.
- **Storno la retur către furnizor:** nota 371 = 408 se stornează în roșu (OMFP 1802) proporțional cu valoarea returnată, cu separare corectă a stornourilor de facturare/notele de credit pe cantitatea acoperită.
- **Compatibilitate cu OCA `l10n_ro_stock_account`:** dezactivează automat câmpul „aviz" duplicat din view-ul OCA, la instalare și la fiecare update; instalarea simultană a ambelor module nu este recomandată.
- **Metode utile pe `stock.move`** pentru raportare și decizii contabile: `l10n_ro_is_inter_gestiune()`, `_l10n_ro_needs_transfer_entry()`, `_l10n_ro_transfer_legs()` / `_l10n_ro_transfer_lines()`.

#### 3. Dependențe

- `stock_account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.gestiune` (nou): entitatea gestiunii contabile — cod, nume, gestionar responsabil, cont de stoc principal, marcaj „Subunitate cu contabilitate proprie", cont de transfer inter-gestiune, cont 408 propriu, jurnal de transfer, politică de inventariere, fereastră de valabilitate, locațiile asociate.
- `stock.location` (extins): câmpul `l10n_ro_gestiune_id` care leagă locația internă de gestiunea sa contabilă (cu constrângere de companie) și `l10n_ro_account_transit_id`, contul de stoc pentru tranzit pe locațiile de tip *Tranzit*.
- `stock.move` (extins): generează nota de transfer valoric inter-gestiune (`l10n_ro_transfer_move_id`, direct/tranzit/481-482) și nota de recepție fără factură 371 = 408 (`l10n_ro_rni_move_id`), inclusiv stornarea la retur; blochează recepțiile/ieșirile directe pe o gestiune cu cont propriu și transferurile fără cont de contrapartidă la `_action_done`; expune metodele utilitare inter-gestiune.
- `account.move` (extins): rutează liniile facturii furnizorului pe contul 408 și adaugă liniile de închidere a pivotului (diferență de preț, diferență de curs); păstrează legătura cu recepția de origine (`l10n_ro_rni_origin_move_id`).
- `account.move.line` (extins): calculează valorile de recepție din notele RNI, descompune diferența dintre factură și recepție în diferență de preț și diferență de curs, și decide stornarea în roșu (doar reducerea de preț, pe firmele cu `account_storno`).
- `res.company` (extins): flagurile `l10n_ro_gestiune_strict` (blocare transfer fără cont de contrapartidă), `l10n_ro_gestiune_required` (gestiune obligatorie pe locații), `l10n_ro_rni_enabled` (activare recepție fără factură global) și contul 408 implicit (`l10n_ro_account_rni_id`).
- `res.config.settings` (extins): expune în Setări → Contabilitate opțiunile de mai sus.
- `stock.picking` / `stock.picking.type` (extinse): câmpul `l10n_ro_notice` (aviz, per transfer) și `l10n_ro_notice_default` (implicit pe tipul de operațiune).
- `l10n.ro.gestiune.assign.wizard` (tranzitoriu): wizard de atribuire în masă a gestiunii pe locațiile fără gestiune.
- `l10n.ro.gestiune.exception.report` / `l10n.ro.gestiune.exception.line` (tranzitorii): raportul de excepții (locații fără gestiune, gestiuni fără cont de stoc, stoc negativ, loturi fără cost).

**Vizualizări**

- `view_l10n_ro_gestiune_form` / `view_l10n_ro_gestiune_list`: formularul și lista gestiunilor contabile, cu toate câmpurile RO, inclusiv marcajul „Subunitate cu contabilitate proprie" și contul de transfer (vizibil doar când marcajul e bifat).
- `action_l10n_ro_gestiune` / `menu_l10n_ro_gestiune`: meniul Inventar → Configurare → Gestiuni contabile.
- `res_config_settings_view_form_l10n_ro_gestiune`: extinde Setări → Contabilitate cu opțiunile „Recepție fără factură", **Blocare transfer fără cont de contrapartidă** (redenumită față de „...fără cont de transfer") și „Necesită gestiune contabilă".
- `view_location_form_l10n_ro_gestiune`: adaugă gestiunea contabilă (locații interne) și contul de stoc pentru tranzit (locații de tranzit) pe formularul locației, în grupul „Informații suplimentare", cu etichetă.
- `view_picking_form_l10n_ro_notice` / `view_picking_tree_l10n_ro_notice` / `view_picking_internal_search_l10n_ro_notice` / `view_picking_type_form_l10n_ro_notice`: câmpul „aviz" pe transfer, listă, căutare și tipul de operațiune.
- `view_l10n_ro_gestiune_assign_wizard_form` / `action_l10n_ro_gestiune_assign_wizard` / `menu_l10n_ro_gestiune_assign`: wizard-ul de atribuire în masă.
- `view_l10n_ro_gestiune_exception_report_form` / `action_l10n_ro_gestiune_exception_report` / `menu_l10n_ro_gestiune_exception`: raportul de excepții.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește sarcini `ir.cron` sau reguli `base.automation`. La instalare și la fiecare update rulează o funcție de date (`_l10n_ro_gestiune_deactivate_oca_notice_view`, prin `data/deactivate_oca_view.xml`) care dezactivează view-ul OCA `l10n_ro_stock_account.view_picking_form` dacă e prezent, pentru a evita duplicarea câmpului „aviz" pe formularul transferului. Restul automatizărilor (generarea notei de transfer, nota 371 = 408, stingerea pivotului, storno-ul) sunt implementate direct în logica modelelor `stock.move`, `stock.picking` și `account.move`.

#### 5. Conexiuni

- [l10n_ro_stock_gestiune_valuation](../l10n_ro_stock_gestiune_valuation/index.md): modul-punte (auto_install) care transformă fiecare gestiune într-o arie de evaluare (`deltatech_valuation_area`), astfel încât notele generate de acest modul să poarte dimensiunea contabilă `valuation_area_id` pentru balanțe pe gestiune.
- [l10n_ro_stock_sheet](../l10n_ro_stock_sheet/index.md): balanța analitică a stocurilor (cantitate + valoare + diferență) și fișa de magazie folosite pentru a verifica firul valoric al acestui modul; cu puntea `l10n_ro_stock_sheet_gestiune` (auto_install), transferul între gestiuni apare ca ieșire din sursă și intrare în destinație, cu valoarea notei de transfer, iar *Diferența* e 0 pe fiecare cont de gestiune.
- [l10n_ro_stock_sheet_gestiune](../l10n_ro_stock_sheet_gestiune/index.md): modul-punte (auto_install) care adaugă Fișa de magazie / Balanța stocurilor filtrată pe gestiune și butonul „Fișă de magazie" din formularul gestiunii.
- [l10n_ro_currency_revaluation](../l10n_ro_currency_revaluation/index.md): contul 408 alimentat de recepția fără factură în valută este element monetar, dar **nu e reevaluat lunar** de acest modul în configurația standard RO — reevaluarea automată selectează doar conturile cu valută sau de tip creanță/datorie comercială, iar 408 e cont curent fără valută pe planul RO. Soldul 408 în valută rămas nefacturat la finele lunii trebuie reevaluat manual.
- `l10n_ro_stock_account` (OCA): oferă un câmp „aviz" similar pe formularul de transfer; instalarea simultană cu acest modul nu este recomandată — modulul dezactivează automat view-ul OCA corespunzător.

#### Limitări cunoscute (din fișa consultant, versiunea 19.0.3.1.0)

- **Contul propriu al gestiunii e folosit doar la transfer.** Pe o gestiune cu cont diferit de contul categoriei, recepțiile și ieșirile directe sunt blocate; o gestiune din care se vinde direct trebuie să folosească contul categoriei.
- **Tranzitul fără cont de tranzit pe locație** e blocat doar cu regula strictă activă; fără ea, nu se generează nicio notă, iar valoarea rămâne pe contul gestiunii sursă.
- **Balanța filtrată pe gestiune** are *Soldul sintetic* nefiltrat (soldul întreg al conturilor), deci *Diferența* nu e 0 pe un cont folosit și de alte gestiuni; cantitățile și valorile analitice sunt corecte.
- **Valoarea transferului** e costul curent × cantitatea; la FIFO nu se mută straturile consumate.
- **408 în valută nu e reevaluat lunar de `l10n_ro_currency_revaluation`** în configurația standard RO (408 e cont curent fără valută pe planul RO); se reevaluează manual.
- **Liniile 408 contate înainte de 19.0.3.1.0** nu au partener; soldul 408 pe furnizor al acestor recepții se corectează manual.
