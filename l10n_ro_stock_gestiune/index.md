# Romania - Gestiuni Contabile de Stoc (FR-54) (localizat la `l10n_ro_stock_gestiune/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_gestiune`
- **Versiune:** `19.0.1.5.0`
- **Cale:** `https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_stock_gestiune`
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_gestiune`
- **Ultima Ingestie:** `2026-06-02`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul aduce în Odoo evidența gestiunilor contabile de stoc așa cum o cere legislația românească (Legea 82/1991 și OMFP 2861/2009). Practic, fiecare gestiune devine o entitate contabilă completă: are un gestionar responsabil, un cont de stoc propriu din clasa 3, un cont de transfer valoric între gestiuni și o politică de inventariere. Pe lângă organizarea gestiunilor, modulul automatizează două operațiuni importante: validează transferurile valorice între gestiuni cu conturi de stoc diferite și gestionează recepția fără factură (nota 371 = 408), astfel încât marfa primită de la furnizor să poată fi înregistrată corect în contabilitate chiar înainte de sosirea facturii. Scopul este o evidență de stoc conformă, cu trasabilitate clară a responsabilităților și a fluxului valoric, fără intervenții manuale repetate.

#### 2. Funcționalități Cheie

- **Gestiuni contabile complete** pe modelul `valuation.area`: gestionar responsabil, cont de stoc principal (ex. 371.01), cont de transfer între gestiuni (ex. 481), cont de recepție fără factură (408) per gestiune și politică de inventariere (la cerere / periodică / anuală), cu posibilitatea de a marca gestiunea activă sau inactivă.
- **Validarea transferurilor inter-gestiune:** când este activată opțiunea „Blocare transfer fără cont de transfer", sistemul blochează transferul direct între gestiuni cu conturi de stoc diferite dacă nu există un cont de transfer configurat. Transferurile în aceeași gestiune, între gestiuni cu conturi identice sau prin locații de tranzit rămân permise.
- **Recepție fără factură (371 = 408):** la recepția mărfii de la furnizor (inventar permanent, valorizare perpetuă) se generează automat nota 371 = 408 — marfa intră în gestiune, iar datoria estimată este recunoscută.
- **Stingerea datoriei la factură (408 = 401):** la sosirea facturii furnizorului, linia de produs se contează pe 408 în loc de 371, iar liniile se reconciliază automat. Contul 408 devine pivot între gestiune și furnizor, independent de ordinea recepție/factură.
- **Suport multi-monedă:** pentru comenzi în valută, linia 408 de la recepție păstrează valuta comenzii, iar diferența de curs recepție↔factură se recunoaște automat pe conturile 765/665 la reconciliere. Costul stocului rămâne la cursul recepției (stocul, activ nemonetar, nu se reevaluează la diferențe de curs).
- **Tratarea diferenței de preț:** când prețul de pe factură diferă de valoarea recepției (în RON), diferența se reclasifică de pe 408 pe contul de diferențe de preț (308/378) la cost standard, respectiv pe contul de stoc (371) la FIFO/CMP, corectând costul stocului ca în comportamentul nativ Odoo.
- **Storno la retur către furnizor:** nota 371 = 408 se stornează în roșu (conform OMFP 1802), proporțional cu valoarea returnată, astfel încât 371 și 408 să rămână egale cu gestiunea.
- **Facturare parțială:** o recepție facturată prin mai multe facturi parțiale se reconciliază corect pe 408 la fiecare pas, iar diferența de preț (RON) se contează per factură, nu doar la final.
- **Metode utile pe `stock.move`** pentru raportare și decizii contabile: `l10n_ro_is_inter_gestiune()`, `l10n_ro_needs_transfer_account()`, `l10n_ro_get_transfer_account()`.

#### 3. Dependențe

- `account`
- `stock_account`
- `deltatech_valuation_area`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `valuation.area` (extins): adaugă câmpurile gestiunii RO — gestionar responsabil (`l10n_ro_gestionar_id`), cont de stoc principal (`l10n_ro_account_stock_id`), cont de transfer între gestiuni (`l10n_ro_account_transfer_id`), cont de recepție fără factură 408 (`l10n_ro_account_rni_id`), politica de inventariere (`l10n_ro_inventory_policy`) și marcajul `active`.
- `stock.move` (extins): generează nota de recepție fără factură 371 = 408 la intrarea mărfii, stornează în roșu la retur și expune metodele utilitare inter-gestiune; păstrează legătura cu nota contabilă generată prin câmpul `l10n_ro_rni_move_id` (plus gestionarea valutei pe linia 408).
- `account.move` (extins): rutează liniile facturii furnizorului pe contul 408 și ține evidența recepției de origine prin câmpul `l10n_ro_rni_origin_move_id`.
- `account.move.line` (extins): realizează reconcilierea liniilor cu 408 provenit de la recepție și calculul/conturarea diferenței de preț.
- `res.company` (extins): definește flagurile și conturile la nivel de companie — `l10n_ro_gestiune_strict` (blocare transfer fără cont de transfer), `l10n_ro_rni_enabled` (activare recepție fără factură) și contul 408 implicit (`l10n_ro_account_rni_id`).
- `res.config.settings` (extins): expune în Setări → Contabilitate opțiunile de mai sus.
- `stock.picking` și `stock.location` (extinse): suport pentru fluxul de gestiune și pentru identificarea locațiilor de tranzit.

**Vizualizări**

- `view_valuation_area_form_l10n_ro`: formularul gestiunii, cu câmpurile contabile RO (gestionar, conturi, politică de inventariere).
- `view_valuation_area_list_l10n_ro`: lista gestiunilor.
- `res_config_settings_view_form_l10n_ro_gestiune`: extinde Setări → Contabilitate cu opțiunile de blocare transfer și de recepție fără factură.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau acțiuni server. Automatizările (generarea notei 371 = 408, reconcilierea, storno-ul) sunt implementate direct în logica modelelor `stock.move`, `account.move` și `account.move.line`.

#### 5. Conexiuni

- [l10n_ro_currency_revaluation](../l10n_ro_currency_revaluation/index.md): contul 408 alimentat de recepția fără factură în valută este un element monetar, ale cărui diferențe de curs se reevaluează la închiderea de perioadă conform logicii acestui modul.
