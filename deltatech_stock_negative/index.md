# Fără Stoc Negativ (localizat la `deltatech_stock_negative/index.md`)

- **Nume Tehnic:** `deltatech_stock_negative`
- **Versiune:** `19.0.2.1.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_stock_negative`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_negative`
- **Ultima Ingestie:** `2026-10-22`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

În mod implicit, Odoo permite validarea unui transfer chiar dacă marfa nu este în stoc, iar cantitatea din locație scade discret sub zero; eroarea iese la iveală abia la următorul inventar. Acest modul oprește operațiunea chiar la validare și îi spune utilizatorului ce a rămas de fapt în locație. Pentru situațiile în care stocul negativ trebuie acceptat (zonă de producție, marfă în consignație, casă de marcat), regula se poate relaxa pe locații sau pe companie.

#### 2. Funcționalități Cheie

- **Blocare la validare:** un transfer care ar duce o locație internă sub zero nu poate fi validat; mesajul indică produsul, locația și cantitatea care ar rămâne, apoi îndrumă spre corectarea cantităților sau o ajustare de inventar.
- **Verificare pe stocul fizic:** se compară cantitatea fizică din locație, pe lot, pachet și proprietar, nu stocul previzionat. Sunt verificate doar produsele cu stoc urmărit (produsele consumabile fără „Urmărire inventar” nu sunt blocate).
- **Transferuri cu mai multe linii:** liniile aceluiași produs dintr-o singură validare se adună, deci nu pot depăși stocul împreună.
- **Setare per companie:** se activează din `Inventar → Configurare → Setări → Trasabilitate`, bifa „Fără stoc negativ”.
- **Excepții per locație:** din `Inventar → Configurare → Locații` se bifează „Permite stoc negativ” pe locațiile unde este acceptat.
- **Produse cu serie:** „Verifică nr. de serie” (activ implicit) face verificarea pe fiecare serie; debifat, produsul se verifică în total pe locație, iar rezervarea ignoră seria.
- **Punct de vânzare (POS):** setarea „Permite stoc negativ din Punctul de vânzare” (activă implicit, vizibilă doar când regula e pornită) lasă livrarea unei bon POS să se valideze chiar sub zero, deoarece marfa a plecat deja de la casă iar POS înghite erorile de validare; fiecare ocolire este logată, iar abaterea rămâne vizibilă ca stoc negativ de corectat. Debifată, regula se aplică și POS.
- **Ocolire programatică:** cheia de context `skip_negative_stock_check` permite forțarea cunoscută a unei validări.
- **Corecții:** un stoc deja greșit se poate aduce la zi oricând printr-o ajustare de inventar (nu trece prin această verificare).
- Fluxul detaliat pas-cu-pas, cu capturi, este în [Fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

**Modele**

- `stock.move.line` (extins): `_action_done()` apelează `_check_no_negative_stock()` pe întregul set de linii înainte de scrierea în quant-uri; sunt avute în vedere liniile care scot marfă dintr-o locație internă, fără excepție, pentru companii cu regula activă; blochează cu `UserError` dacă stocul fizic ar scădea sub zero. `_is_pos_delivery()` detectează livrările POS fără dependență de `point_of_sale`.
- `stock.quant` (extins): `_get_available_quantity` ignoră lotul/seria pentru produsele cu serie pe locațiile cu „Verifică nr. de serie” debifat și fără stoc negativ permis.
- `stock.location` (extins): câmpurile `allow_negative_stock` și `check_serial_no`.
- `res.company` (extins): `no_negative_stock` și `no_negative_stock_pos_bypass`.
- `res.config.settings` (extins): câmpuri related pe companie pentru cele două opțiuni.

**Vizualizări**

- `views/res_config_view.xml`: opțiunile „Fără stoc negativ” și „Permite stoc negativ din Punctul de vânzare” în setările de inventar.
- `views/stock_location_view.xml`: opțiunile „Permite stoc negativ” și „Verifică nr. de serie” pe formularul locației.

**Acțiuni Automate / Acțiuni Server**

- Nu există. Un script de migrare (`migrations/19.0.2.0.11/post-migration.py`) reîncarcă traducerile românești corectate la actualizare.

#### 5. Conexiuni

- `point_of_sale`: livrările bonurilor POS pot fi ocolite prin setarea `no_negative_stock_pos_bypass` (legătură prin câmpul `pos_order_id`, fără dependență în manifest).
